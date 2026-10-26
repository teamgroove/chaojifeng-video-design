#!/usr/bin/env python3
"""Repair intra-repo anchor links after zh->en translation.

Translating a heading changes its GitHub anchor. Heading counts and order were verified
identical per file, so old and new headings can be paired by index: old_anchor[i] now maps
to new_anchor[i]. Every `](file.md#frag)` and `](#frag)` link is rewritten through that map.
Unresolvable fragments are reported, never guessed.

Run from the repo root:  python3 .translate/fix_anchors.py [--dry-run]
"""
import os
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEAD_REF = "HEAD"
DRY = "--dry-run" in sys.argv


def slug(text):
    """GitHub heading anchor: lowercase, drop punctuation, spaces -> '-', keep CJK."""
    s = text.strip().lower()
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)      # links -> visible text
    s = s.replace('`', '')
    s = re.sub(r'[*_~]', '', s)
    out = []
    for ch in s:
        if ch.isalnum() or ch in '-_':
            out.append(ch)
        elif ch in ' \t':
            out.append('-')
    return ''.join(out)


def slugs_for(headings):
    seen, res = {}, []
    for h in headings:
        s = slug(h)
        if s in seen:
            seen[s] += 1
            res.append("%s-%d" % (s, seen[s]))
        else:
            seen[s] = 0
            res.append(s)
    return res


def headings(text):
    return [m.group(2).strip() for m in re.finditer(r'^(#{1,6})\s+(.*)$', text, re.M)]


def git_show(rel):
    p = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (HEAD_REF, rel)],
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None


def walk_md():
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in ('.git', 'node_modules', 'Output', 'output', 'media')]
        for fn in fns:
            if fn.endswith('.md'):
                out.append(os.path.relpath(os.path.join(dp, fn), ROOT))
    return sorted(out)


def main():
    maps, unpaired = {}, []
    for rel in walk_md():
        old = git_show(rel)
        if old is None:
            continue
        new = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        ho, hn = headings(old), headings(new)
        if len(ho) != len(hn):
            unpaired.append((rel, len(ho), len(hn)))
            continue
        maps[rel] = dict(zip(slugs_for(ho), slugs_for(hn)))

    # also allow looking up by file name only (links are relative)
    by_suffix = {}
    for rel in maps:
        by_suffix.setdefault(os.path.basename(rel), []).append(rel)

    changed, unresolved = [], []
    link_re = re.compile(r'\]\(([^)\s]*?)(#[^)\s]+)\)')

    for rel in walk_md():
        path = os.path.join(ROOT, rel)
        text = open(path, encoding='utf-8').read()
        here = os.path.dirname(rel)

        def repl(m):
            target, frag = m.group(1), m.group(2)[1:]
            if target == '':
                tgt_rel = rel
            else:
                tgt_rel = os.path.normpath(os.path.join(here, target)).replace(os.sep, '/')
                if tgt_rel not in maps:
                    cands = by_suffix.get(os.path.basename(target), [])
                    tgt_rel = cands[0] if len(cands) == 1 else None
            if tgt_rel is None or tgt_rel not in maps:
                if re.search(r'[\u4e00-\u9fff]', frag):
                    unresolved.append((rel, m.group(0)))
                return m.group(0)
            old_frag = unquote(frag)
            if not re.search(r'[\u4e00-\u9fff]', old_frag):
                return m.group(0)          # already an English anchor
            new_frag = maps[tgt_rel].get(old_frag)
            if new_frag is None:
                unresolved.append((rel, m.group(0)))
                return m.group(0)
            return '](%s#%s)' % (target, new_frag)

        new_text = link_re.sub(repl, text)
        if new_text != text:
            changed.append(rel)
            if not DRY:
                open(path, 'w', encoding='utf-8').write(new_text)

    print("Dateien mit korrigierten Ankern: %d" % len(changed))
    for c in changed:
        print("  ", c)
    if unpaired:
        print("\nNicht paarbar (Heading-Anzahl differiert) — nicht angefasst:")
        for u in unpaired:
            print("   %s  alt=%d neu=%d" % u)
    if unresolved:
        print("\nNicht auflösbare Fragmente (manuell prüfen):")
        for rel, frag in unresolved:
            print("   %s : %s" % (rel, frag))
    if DRY:
        print("\n[dry-run] nichts geschrieben")


if __name__ == '__main__':
    main()

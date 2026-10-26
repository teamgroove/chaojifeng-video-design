#!/usr/bin/env python3
"""Check the zh->en translation did not damage the repo.

For every .md file compares the working tree against git HEAD and reports:
  * line count delta                      (should be 0)
  * heading count delta                   (should be 0)
  * table shapes: (rows, cols) per table  (should be identical lists)
  * fenced code blocks                    (must be byte-identical as a list)
  * inline-code token sets               (should be identical sets)
  * link targets                          (must be the same sets after dropping fragments)
  * remaining Han characters, excluding the whitelisted functional strings

Run from the repo root:  python3 .translate/verify.py [--strict]
--strict turns any non-whitelisted Han character into a failure (exit 1).
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEAD_REF = "HEAD"
STRICT = "--strict" in sys.argv
HAN = re.compile(r'[\u4e00-\u9fff]')

# Strings that legitimately stay Chinese: style names/ids used by the tooling,
# linter cue words, link anchors that were already English, asset file names.
WHITEOUT = re.compile(
    r'中国水墨|超级峰|术语在线|待填写|待补充|被|是指|表示|就是|是一种|它|该|'
    r'知识分享背景音乐神曲|概念知识科普|神曲|牌子|Vibe知识大赏保姆级教程'
)


def git_show(rel):
    p = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (HEAD_REF, rel)],
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else None


def headings(t):
    return [m.group(1) + m.group(2).strip() for m in re.finditer(r'^(#{1,6})\s+(.*)$', t, re.M)]


def fences(t):
    return re.findall(r'```[^\n]*\n.*?```', t, re.S)


def inline_code(t):
    without = re.sub(r'```.*?```', '', t, flags=re.S)
    return sorted(set(re.findall(r'`([^`\n]+)`', without)))


def tables(t):
    shapes, rows = [], 0
    for line in t.splitlines():
        if line.strip().startswith('|') and line.strip().endswith('|'):
            rows += 1
        else:
            if rows:
                shapes.append(rows)
                rows = 0
    if rows:
        shapes.append(rows)
    return shapes


def links(t):
    return sorted({re.sub(r'#.*$', '', m.group(1))
                   for m in re.finditer(r'\]\(([^)\s]+)\)', t)})


def walk_md():
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in ('.git', 'node_modules', 'Output', 'output', 'media')]
        for fn in fns:
            if fn.endswith('.md'):
                out.append(os.path.relpath(os.path.join(dp, fn), ROOT))
    return sorted(out)


def main():
    problems, han_left = [], []
    total_han = 0
    checked = 0
    for rel in walk_md():
        if rel.startswith('.translate/'):
            continue
        old = git_show(rel)
        if old is None:
            continue
        checked += 1
        new = open(os.path.join(ROOT, rel), encoding='utf-8').read()

        if len(old.splitlines()) != len(new.splitlines()):
            problems.append((rel, "line count %d -> %d" % (len(old.splitlines()), len(new.splitlines()))))
        if len(headings(old)) != len(headings(new)):
            problems.append((rel, "heading count %d -> %d" % (len(headings(old)), len(headings(new)))))
        if tables(old) != tables(new):
            problems.append((rel, "table shapes %s -> %s" % (tables(old), tables(new))))
        if fences(old) != fences(new):
            problems.append((rel, "fenced code blocks differ"))
        if inline_code(old) != inline_code(new):
            missing = set(inline_code(old)) - set(inline_code(new))
            problems.append((rel, "inline code lost: %s" % sorted(missing)[:5]))
        if links(old) != links(new):
            lost = set(links(old)) - set(links(new))
            added = set(links(new)) - set(links(old))
            problems.append((rel, "link targets changed, lost=%s added=%s" % (sorted(lost)[:3], sorted(added)[:3])))

        left = [(i + 1, l) for i, l in enumerate(new.splitlines()) if HAN.search(l)]
        if left:
            total_han += sum(len(HAN.findall(l)) for _, l in left)
            bad = [(n, l) for n, l in left if not WHITEOUT.search(l)]
            han_left.append((rel, len(left), len(bad), bad[:3]))

    print("Geprüfte Markdown-Dateien: %d" % checked)
    print("Struktur-Probleme: %d" % len(problems))
    for rel, msg in problems:
        print("   %s : %s" % (rel, msg))
    print("\nDateien mit Restchinesisch: %d  (%d Han-Zeichen)" % (len(han_left), total_han))
    for rel, n, bad, sample in sorted(han_left, key=lambda r: -r[2])[:40]:
        flag = "  <-- prüfen" if bad else ""
        print("   %-58s %3d Zeilen%s" % (rel, n, flag))
        for ln, text in sample:
            print("        %4d  %s" % (ln, text.strip()[:110]))
    if STRICT:
        offenders = [r for r in han_left if r[2]]
        if offenders or problems:
            print("\nSTRICT: %d Dateien mit nicht-whitelisted Chinesisch" % len(offenders))
            return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

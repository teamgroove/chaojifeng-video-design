#!/usr/bin/env python3
"""Harmonise the 59 opuscar style cards onto one canonical English template.

The Chinese originals are byte-identical apart from two lines (the H1 name and the lead
sentence, which repeats the name). The translation was produced by four parallel batches, so
the same sentences came out in four different wordings. This script rebuilds every card from
one chosen template, keeping what is genuinely per-pack:

  * the H1 line: the Chinese style name, byte-identical (lookup key)
  * the lead sentence: the pack's own `english_name` from style.json
  * the upstream section list: byte-identical, including its 、 separators and final 。

Verification is built in: line count, heading count, link targets and fenced blocks are
compared against git HEAD per file. Run from the repo root.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLES = os.path.join(ROOT, "styles")
TEMPLATE_PACK = "opuscar-ink-wash"      # the cleanest of the four batch translations
DRY = "--dry-run" in sys.argv

SECTIONS_RE = re.compile(r'本包收录章节为(.*?)。', re.S)


def git_show(rel):
    p = subprocess.run(["git", "-C", ROOT, "show", "HEAD:" + rel], capture_output=True, text=True)
    if p.returncode != 0:
        sys.exit("git show failed for " + rel)
    return p.stdout


def heading_count(t):
    return len(re.findall(r'^#{1,6}\s', t, re.M))


def link_targets(t):
    return sorted({re.sub(r'#.*$', '', m.group(1)) for m in re.finditer(r'\]\(([^)\s]+)\)', t)})


def fences(t):
    return re.findall(r'```[^\n]*\n.*?```', t, re.S)


def main():
    template_path = os.path.join(STYLES, TEMPLATE_PACK, "STYLE.md")
    template = open(template_path, encoding="utf-8").read()
    tpl_zh = template.splitlines()[0][2:].strip()
    tpl_en = json.load(open(os.path.join(STYLES, TEMPLATE_PACK, "style.json"), encoding="utf-8"))["english_name"]
    # the template's own section list is no longer marked in Chinese, so take it from HEAD
    tpl_head = git_show("styles/%s/STYLE.md" % TEMPLATE_PACK)
    m = SECTIONS_RE.search(tpl_head)
    if not m:
        sys.exit("template pack has no section marker in HEAD")
    tpl_sections = m.group(1)
    if tpl_sections not in template:
        sys.exit("template section list vanished from the translated file")

    packs = sorted(d for d in os.listdir(STYLES)
                   if d.startswith("opuscar-") and os.path.isdir(os.path.join(STYLES, d)))

    done, skipped = [], []
    for pack in packs:
        rel = "styles/%s/STYLE.md" % pack
        head = git_show(rel)
        zh_name = head.splitlines()[0][2:].strip()
        m = SECTIONS_RE.search(head)
        if not m:
            skipped.append((pack, "no section marker in HEAD"))
            continue
        secs = m.group(1)
        meta = json.load(open(os.path.join(STYLES, pack, "style.json"), encoding="utf-8"))
        english = meta.get("english_name")
        if not english:
            skipped.append((pack, "no english_name"))
            continue
        if zh_name == tpl_zh and english == tpl_en:
            continue                                    # the template pack itself

        # set the two per-pack lines directly instead of string-replacing them
        lines = template.splitlines()
        lines[0] = "# %s" % zh_name
        lines[2] = "Organise the current subject with the materials, composition, motion and " \
                   "sound-image grammar of %s." % english
        new = "\n".join(lines) + "\n"
        new = new.replace(tpl_sections, secs, 1)

        # structure must still match the Chinese original
        if heading_count(new) != heading_count(head):
            skipped.append((pack, "heading count %d != %d" % (heading_count(new), heading_count(head))))
            continue
        if len(new.splitlines()) != len(head.splitlines()):
            skipped.append((pack, "line count %d != %d" % (len(new.splitlines()), len(head.splitlines()))))
            continue
        if link_targets(new) != link_targets(head):
            skipped.append((pack, "link targets differ"))
            continue
        if fences(new) != fences(head):
            skipped.append((pack, "fenced blocks differ"))
            continue

        if not DRY:
            open(os.path.join(STYLES, pack, "STYLE.md"), "w", encoding="utf-8").write(new)
        done.append(pack)

    print("harmonisiert: %d Karten%s" % (len(done), " (dry-run)" if DRY else ""))
    if skipped:
        print("übersprungen:")
        for pack, why in skipped:
            print("   %-40s %s" % (pack, why))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Relative-link checker for the public review mirror.

Every relative Markdown link in every .md file must resolve to a file that exists
in the mirror. v0.21 shipped with REVIEW_INDEX.md pointing at review/SOURCE_VERSION_MAP.md
when the file is at the repository root, and nothing caught it.

Usage: python3 tools/check_mirror_links.py <checkout-dir>
"""
import re, sys
from pathlib import Path
from urllib.parse import unquote

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def main(root: Path):
    bad, checked = [], 0
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for target in LINK.findall(line):
                t = target.split()[0].strip()
                if t.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                t = unquote(t.split("#")[0])
                if not t:
                    continue
                dest = (md.parent / t).resolve()
                checked += 1
                if not dest.exists():
                    bad.append((md.relative_to(root), i, t))
    if bad:
        print(f"BROKEN RELATIVE LINKS: {len(bad)} of {checked} checked\n")
        for f, i, t in bad:
            print(f"  {f}:{i}  ->  {t}")
        return 1
    print(f"All {checked} relative Markdown links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]).resolve()))

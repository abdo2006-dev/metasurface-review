#!/usr/bin/env python3
"""Check the corpus totals stated in prose against the files actually present.

Why this exists. Section 2 of the manuscript states a file count for the reviewed set, and
`source_inventory.md` states the same total. The count moved when three published full texts were
archived alongside their preprints, and neither statement moved with it: the manuscript said 31
files while 34 were present. Nothing checked, because the number is prose in two places and a
directory listing in a third.

What is checked, and what deliberately is not. Only the **file** count is derived from the working
tree, because only that one is mechanically derivable. The **document** count (26) and the
**contribution** count (24) rest on the independence rule of Section 2.4 -- a preprint and its
version of record are one document, supplementary information belongs to its parent paper -- which
is a judgement recorded in `source_inventory.md`, not something a directory listing can decide.
Those two are checked for *agreement between the two prose statements*, never re-derived. A
validator that silently recomputed them would be asserting the independence result rather than
testing it.

    python3 tools/check_corpus_counts.py         # exit 1 on any disagreement
"""
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import ROOT, DOC, MANUSCRIPT

FIGURE_PDF = re.compile(r"^fig\d+_")
SCOPE = MANUSCRIPT / "02_scope_and_method.md"
INVENTORY = DOC / "source_inventory.md"


def present():
    """Corpus PDFs in the working tree: every PDF at the repository root that is not a
    generated figure. The public mirror carries no PDFs, so there it returns None and the
    file-count check is skipped rather than failed."""
    pdfs = [p.name for p in ROOT.glob("*.pdf") if not FIGURE_PDF.match(p.name)]
    return sorted(pdfs) if pdfs else None


def main():
    fails = []

    scope = SCOPE.read_text(encoding="utf-8")
    m = re.search(r"(\d+) distinct research contributions across (\d+) files", scope)
    if not m:
        sys.exit("could not find the corpus sentence in 02_scope_and_method.md")
    contrib_ms, files_ms = int(m.group(1)), int(m.group(2))

    inv = INVENTORY.read_text(encoding="utf-8")
    m = re.search(r"\*\*(\d+) PDF files\*\* → \*\*(\d+) unique documents\*\* → "
                  r"\*\*(\d+) distinct research contributions\*\*", inv)
    if not m:
        sys.exit("could not find the corpus totals line in source_inventory.md")
    files_inv, docs_inv, contrib_inv = (int(x) for x in m.groups())

    print(f"manuscript §2      : {contrib_ms} contributions across {files_ms} files")
    print(f"source_inventory   : {files_inv} files -> {docs_inv} documents -> {contrib_inv} contributions")

    if files_ms != files_inv:
        fails.append(f"file count disagrees between the two statements: §2 says {files_ms}, "
                     f"source_inventory.md says {files_inv}")
    if contrib_ms != contrib_inv:
        fails.append(f"contribution count disagrees: §2 says {contrib_ms}, "
                     f"source_inventory.md says {contrib_inv}")

    files = present()
    if files is None:
        print("working tree      : no corpus PDFs here (public mirror) -- file-count check skipped")
    else:
        print(f"working tree      : {len(files)} non-figure PDFs")
        if len(files) != files_ms:
            fails.append(f"the stated file count ({files_ms}) is not the number of corpus PDFs "
                         f"present ({len(files)}). Either a source was added or removed without "
                         f"updating §2 and source_inventory.md, or a non-corpus PDF is sitting in "
                         f"the repository root.")

    if fails:
        print("\nFAIL:")
        for f in fails:
            print("  - " + f)
        print("\nThe document count (26) and contribution count (24) are NOT re-derived here: "
              "they rest on the independence rule and are recorded in source_inventory.md.")
        return 1
    print("  OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

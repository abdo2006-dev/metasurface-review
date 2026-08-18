#!/usr/bin/env python3
"""Single shared path definition for every script in this package.

Why this module exists. These scripts are executed from two different trees:

  * the private working repository, whose documentation directory is `Documentation/`
  * the sanitized public review mirror, whose documentation directory is `documentation/`

Every script previously hardcoded `Documentation`. That works on macOS, whose default
filesystem is case-insensitive, and fails immediately on a case-sensitive Linux
checkout of the public mirror -- which is where an independent reviewer will actually
run them. The public artifact therefore did not support the reproducibility claim the
manuscript makes for it.

`resolve_dir` picks the first candidate that exists, so the same code is correct in
both trees and on both kinds of filesystem. It never guesses: if no candidate exists
it fails loudly with the names it tried.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def resolve_dir(root: Path, *names: str) -> Path:
    for n in names:
        p = root / n
        if p.is_dir():
            return p
    sys.exit(f"none of {names!r} is a directory under {root}")


# Public-mirror casing is listed first: it is the artifact that must be portable.
DOC = resolve_dir(ROOT, "documentation", "Documentation")
MANUSCRIPT = resolve_dir(DOC, "manuscript") if (DOC / "manuscript").is_dir() \
    else resolve_dir(ROOT, "manuscript", "Manuscript")
TOOLS = ROOT / "tools"

# The decision table and its two retrieval artefacts.
DECISIONS = DOC / "forward_citation_search_results.csv"
WORKS = DOC / "forward_citation_works_deduplicated.csv"
RECORDS = DOC / "forward_citation_records_raw.csv"
REGISTER = DOC / "s11_study_register.md"
MATRIX = DOC / "adaptation_chain_matrix.md"

__all__ = ["ROOT", "DOC", "MANUSCRIPT", "TOOLS", "DECISIONS", "WORKS",
           "RECORDS", "REGISTER", "MATRIX", "resolve_dir"]

#!/usr/bin/env python3
"""Fail if any active document contains a stale S11 or C1 count.

Two drift incidents (v0.21 CURRENT_VERSION.md, v0.22 the whole supporting-documentation
set) had the same cause: scientific counts maintained by hand in prose, in more than one
place, with no mechanism to detect divergence. This script is that mechanism.

It scans every active manuscript and documentation file for numeric patterns that are
known to be superseded, and reports the file and line. Historical CHANGELOG entries and
the generated register are exempt.

Exit status 1 if any hit is found.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "Documentation"
sys.path.insert(0, str(ROOT / "tools"))
from s11_counts import counts

C = counts()
R, A, RO, C1 = C["retrieval"], C["access"], C["roles"], C["c1"]

# Files whose old numbers are legitimately historical.
EXEMPT_FILES = {"CHANGELOG.md", "s11_study_register.md"}
# Lines marked as historical are exempt anywhere.
EXEMPT_LINE = re.compile(r"historical|superseded|v0\.2[01] said|was recorded as|earlier draft|"
                         r"corrected second pass|What the corrected|v1\.[0-7] |was wrong|recount|→", re.I)

STALE = [
    (r"\b21 (?:distinct|candidate|identified|system)", "21 studies -> 20"),
    (r"\b(?:of|the) 21 studies\b", "21 studies -> 20"),
    (r"\b14 of 21\b", "14 of 21 -> 13 of 20"),
    (r"\b13 of 20 candidate studies whose full texts we could read\b", None),  # allowed
    (r"\b14 were read(?:able)? in full\b", "14 read -> 13"),
    (r"\bFourteen of the 21\b", "-> Thirteen of the 20"),
    (r"\b17 of (?:the )?20\b", "17 of 20 -> stale S11 denominator"),
    (r"\b13 of 20\b", None),  # current, allowed
    (r"262 ?(?:→|->) ?64", "stage-1 64 -> 65"),
    (r"\b64 (?:wireless|stage)", "stage-1 64 -> 65"),
    (r"(?:→|->) ?20 ?(?:→|->) ?13\b", None),  # current flow, allowed
    (r"(?:→|->) ?21 ?(?:→|->) ?14\b", "flow 21->14 is stale"),
    (r"\btimes more than five of the ten stages\b", "C1: superseded by the T/(T) split"),
    (r"\bEight retrieved papers\b", "eight -> nine studies"),
    (r"\beight (?:further |retrieved )?papers cite\b", "eight -> nine studies"),
    (r"\bTwo platforms reach five\b", "C1: only one platform reaches five under ·T"),
    (r"\b33 (?:numbered )?references\b", "33 -> current bibliography count"),
]

ACTIVE = sorted(list((DOC / "manuscript").glob("*.md")) + list(DOC.glob("*.md")) +
                list((DOC / "audits").glob("*.md")))

def main():
    hits = []
    for f in ACTIVE:
        if f.name in EXEMPT_FILES:
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if EXEMPT_LINE.search(line):
                continue
            for pat, msg in STALE:
                if msg is None:
                    continue
                if re.search(pat, line):
                    hits.append((f.relative_to(ROOT), i, msg, line.strip()[:110]))
    if hits:
        print(f"STALE S11/C1 COUNTS: {len(hits)} hit(s)\n")
        for f, i, msg, txt in hits:
            print(f"  {f}:{i}\n      [{msg}]\n      {txt}\n")
        return 1
    print("No stale S11/C1 counts found in active documents.")
    print(f"authoritative: {R['records_pre_dedup']} records -> {R['unique_works']} works -> "
          f"{R['stage1_pass']} stage-1 -> {R['stage2_records']} records -> {R['distinct_studies']} studies "
          f"-> {A['studies_read']} read / {A['studies_unread']} unread")
    print(f"roles: propagation {RO['propagation_studies']} studies / {RO['propagation_records']} records; "
          f"no-timing {RO['no_timing_studies']} studies / {RO['no_timing_records']} records")
    print(f"C1: max Q={C1['max_quantitative']} {C1['sources_at_max_quantitative']}; "
          f"max T={C1['max_fully_delimited_T']} {C1['sources_at_max_fully_delimited_T']}; "
          f"max T+(T)={C1['max_any_timing']} {C1['sources_at_max_any_timing']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

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

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import ROOT, DOC, MANUSCRIPT, DECISIONS, WORKS, RECORDS, REGISTER, MATRIX
import re, sys
from pathlib import Path

sys.path.insert(0, str(ROOT / "tools"))
from s11_counts import counts

C = counts()
R, A, RO, C1 = C["retrieval"], C["access"], C["roles"], C["c1"]

# Files whose old numbers are legitimately historical.
EXEMPT_FILES = {"CHANGELOG.md", "s11_study_register.md"}
# Lines marked as historical are exempt anywhere.
EXEMPT_LINE = re.compile(r"historical|superseded|v0\.2[01] said|was recorded as|earlier draft|"
                         r"corrected second pass|What the corrected|v1\.[0-9]+ |was wrong|recount|→|earlier version|credited|Comparison:|Correction \(v0|previously named|previously said|Prior passes|prior revision", re.I)

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
    (r"\b33 entries\b", "33 -> current bibliography count"),
    (r"two platforms reach five", "C1: only one platform reaches five under a strict ·T reading"),
    (r"five stages it times", "C1: LI-25 fully delimits four, not five"),
    (r"forward_citation_stage1_raw\.csv", "obsolete filename -> forward_citation_works_deduplicated.csv"),
    (r"No co-authorship analysis was performed", "false since v0.22: the analysis is performed and C3 rests on it"),
    (r"\b29 ?049\b|\b23 ?472\b", "superseded word count"),
]

def active_files():
    """Every active markdown record, in BOTH tree layouts.

    v0.22 shipped a checker that built DOC/"manuscript" and DOC/"Documentation" and
    therefore scanned nothing at all on a case-sensitive checkout of the public mirror,
    while its docstring claimed it scanned every active file.
    """
    out = []
    out += sorted(MANUSCRIPT.glob("*.md"))
    out += sorted(DOC.glob("*.md"))
    if (DOC / "audits").is_dir():
        out += sorted((DOC / "audits").glob("*.md"))
    for name in ("REVIEW_INDEX.md", "CURRENT_VERSION.md", "SOURCE_VERSION_MAP.md",
                 "README.md", "CHANGELOG.md"):
        f = ROOT / name
        if f.is_file():
            out.append(f)
    f = ROOT / "tools" / "README.md"
    if f.is_file():
        out.append(f)
    tmpl = ROOT / "tools" / "review_repo_templates"
    if tmpl.is_dir():
        out += sorted(tmpl.glob("*.tmpl"))
    return [f for f in dict.fromkeys(out) if f.name not in EXEMPT_FILES]


def executable_tools():
    return sorted((ROOT / "tools").glob("*.py"))


def wireless_alternative_count():
    import importlib.util as il
    sp = il.spec_from_file_location("_fcs", ROOT / "tools" /
                                    "reproduce_forward_citation_search.py")
    m = il.module_from_spec(sp)
    sp.loader.exec_module(m)
    return len(m.WIRELESS_TERMS)

def main():
    hits = []
    for f in active_files():
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if EXEMPT_LINE.search(line):
                continue
            for pat, msg in STALE:
                if msg is None:
                    continue
                if re.search(pat, line):
                    hits.append((f.relative_to(ROOT), i, msg, line.strip()[:110]))
    # --- structural checks (v0.23) -------------------------------------------------
    # sync_review_repo.py runs ONLY in the private working tree, whose directory really
    # is `Documentation/`, and is never shipped to the mirror. check_s11_consistency.py
    # contains these names as literals in its own pattern table. Both are out of scope.
    NOT_SHIPPED = {"_paths.py", "sync_review_repo.py", "check_s11_consistency.py", "validate_public_snapshot.py"}  # meta-tools: these carry the names as literals to test for
    for t in executable_tools():
        if t.name in NOT_SHIPPED:
            continue
        txt = t.read_text(encoding="utf-8")
        for m in re.finditer(r'["\'](Documentation|Manuscript)["\']', txt):
            ln = txt[:m.start()].count("\n") + 1
            hits.append((t.relative_to(ROOT), ln,
                         "wrong-case public path in executable tool -- use tools/_paths.py",
                         m.group(0)))

    n_alt = wireless_alternative_count()
    for f in active_files():
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if EXEMPT_LINE.search(line):
                continue
            for m in re.finditer(r"\b(\d+)[- ]alternative\b", line):
                if int(m.group(1)) != n_alt:
                    hits.append((f.relative_to(ROOT), i,
                                 f"regex alternative count {m.group(1)} != len(WIRELESS_TERMS)={n_alt}",
                                 line.strip()[:110]))

    if hits:
        print(f"STALE S11/C1 COUNTS: {len(hits)} hit(s)\n")
        for f, i, msg, txt in hits:
            print(f"  {f}:{i}\n      [{msg}]\n      {txt}\n")
        return 1
    print(f"No stale S11/C1 counts found. Scanned {len(active_files())} active documents "
          f"and {len(executable_tools())} executable tools.")
    print(f"regex: len(WIRELESS_TERMS) = {wireless_alternative_count()}")
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

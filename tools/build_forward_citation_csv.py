#!/usr/bin/env python3
"""Deterministically rebuild documentation/forward_citation_search_results.csv.

This script contains NO scientific content. It performs exactly three operations:

  1. read the deduplicated work-level retrieval  (documentation/forward_citation_works_deduplicated.csv)
  2. left-join the human-coded stage-2 layer     (documentation/s11_manual_decisions.csv)
  3. emit the decision table                     (documentation/forward_citation_search_results.csv)

Every judgement -- stage-2 inclusion, exclusion reason, full-text access and source,
timing hit, Table 7 row, author-network status, record role, version family -- lives in
the manual-decisions CSV and is joined by OpenAlex identifier. Study-level roles are
derived, not stored twice: a version family propagates if any of its versions does.

Before v0.23 those judgements were a dict inside this file, which is how it came to
hold retired science (the F-ANJ-C / F-ANJ-J split, the withdrawn `counterexample`
role) and would have regenerated it. Moving them out makes that failure impossible:
there is nothing left in this file to go stale.

  --check  rebuild in memory and diff against the committed table; exit 1 on mismatch
"""
import argparse, csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import DOC, DECISIONS, WORKS

MANUAL = DOC / "s11_manual_decisions.csv"

FIELDS = ["openalex_id", "doi", "arxiv_id", "title", "year", "cited_seeds",
          "stage1_regex_pass", "stage2_system_paper", "exclusion_reason",
          "full_text_inspected", "full_text_source", "timing_terminology_hit",
          "table7_row", "author_network_status", "final_role", "version_family",
          "version_family_role"]

MANUAL_FIELDS = ["stage2_system_paper", "exclusion_reason", "full_text_inspected",
                 "full_text_source", "timing_terminology_hit", "table7_row",
                 "author_network_status", "final_role", "version_family"]

STAGE1_FAIL = "did not pass stage-1 title/abstract screen"


def build():
    works = list(csv.DictReader(open(WORKS, encoding="utf-8")))
    manual = {r["openalex_id"]: r for r in csv.DictReader(open(MANUAL, encoding="utf-8"))}

    rows = []
    for w in works:
        r = {k: w.get(k, "") for k in ("openalex_id", "doi", "arxiv_id", "title",
                                       "year", "cited_seeds", "stage1_regex_pass")}
        m = manual.get(w["openalex_id"])
        if w["stage1_regex_pass"] == "yes":
            if m is None:
                sys.exit(f"stage-1 survivor {w['openalex_id']} has no manual decision row")
            for k in MANUAL_FIELDS:
                r[k] = m.get(k, "")
        else:
            for k in MANUAL_FIELDS:
                r[k] = ""
            r["stage2_system_paper"] = "no"
            r["exclusion_reason"] = STAGE1_FAIL
            r["full_text_inspected"] = "no"
            r["final_role"] = "excluded"
        rows.append(r)

    # study-level role, derived: a family propagates if any of its versions does
    fam = {}
    for r in rows:
        if r["stage2_system_paper"] == "yes":
            fam.setdefault(r["version_family"], set()).add(r["final_role"])
    fam_role = {}
    for f, roles in fam.items():
        fam_role[f] = ("propagation" if "propagation" in roles
                       else "no timing value" if "no timing value" in roles
                       else "unread")
    for r in rows:
        r["version_family_role"] = (fam_role.get(r["version_family"], "")
                                    if r["stage2_system_paper"] == "yes" else "")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="diff against the committed table instead of overwriting it")
    a = ap.parse_args()

    rows = build()
    s2 = [r for r in rows if r["stage2_system_paper"] == "yes"]
    fams = sorted({r["version_family"] for r in s2})
    print(f"works {len(rows)} | stage-1 {sum(1 for r in rows if r['stage1_regex_pass']=='yes')} "
          f"| stage-2 records {len(s2)} | study families {len(fams)}")
    roles = {}
    for r in s2:
        roles[r["final_role"]] = roles.get(r["final_role"], 0) + 1
    print("record roles:", dict(sorted(roles.items())))
    if "F-ANJ-C" in fams or "F-ANJ-J" in fams:
        sys.exit("FAILED: retired F-ANJ-C/F-ANJ-J split present")
    if any(r["final_role"] == "counterexample" for r in s2):
        sys.exit("FAILED: retired 'counterexample' role present")

    if a.check:
        have = list(csv.DictReader(open(DECISIONS, encoding="utf-8")))
        if len(have) != len(rows):
            sys.exit(f"FAILED: row count {len(have)} != rebuilt {len(rows)}")
        diffs = []
        for h, r in zip(have, rows):
            for k in FIELDS:
                if (h.get(k) or "") != (r.get(k) or ""):
                    diffs.append((h["openalex_id"], k, h.get(k), r.get(k)))
        if diffs:
            print(f"\nFAILED: {len(diffs)} field difference(s) vs the committed table")
            for d in diffs[:20]:
                print(f"  {d[0]} {d[1]}: committed={d[2]!r} rebuilt={d[3]!r}")
            sys.exit(1)
        print("\nCHECK PASSED: rebuild is field-identical to the committed decision table.")
        return

    with DECISIONS.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader(); w.writerows(rows)
    print(f"wrote {DECISIONS.name}")


if __name__ == "__main__":
    main()

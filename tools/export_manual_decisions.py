#!/usr/bin/env python3
"""Export the human-coded stage-2 layer to documentation/s11_manual_decisions.csv.

The forward-citation pipeline has an automatic half (retrieval, deduplication,
stage-1 regex screening) and a manual half (stage-2 inclusion, full-text access,
timing extraction, version-family assignment, author-network resolution). Until
v0.23 the manual half lived inside build_forward_citation_csv.py as a Python dict.
That is why that script was able to hold pre-v0.22 science -- F-ANJ-C/F-ANJ-J and
the retired `counterexample` role -- and would have regenerated it if run.

Separating the two halves means the builder contains no scientific content at all:
it joins retrieval output to this table and nothing else. Reviewing the human
judgements now means reading a CSV, not reading code.
"""
import csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import DOC, DECISIONS

OUT = DOC / "s11_manual_decisions.csv"
FIELDS = ["openalex_id", "title", "stage2_system_paper", "exclusion_reason",
          "full_text_inspected", "full_text_source", "timing_terminology_hit",
          "table7_row", "author_network_status", "final_role", "version_family"]


def main():
    rows = list(csv.DictReader(open(DECISIONS, encoding="utf-8")))
    # Only stage-1 survivors received a human decision. Works that failed the
    # stage-1 regex were excluded automatically and carry no manual judgement.
    manual = [r for r in rows if r["stage1_regex_pass"] == "yes"]
    manual.sort(key=lambda r: (r["version_family"], r["openalex_id"]))
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        for r in manual:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    print(f"wrote {OUT.name}: {len(manual)} human-coded rows "
          f"({sum(1 for r in manual if r['stage2_system_paper']=='yes')} stage-2)")


if __name__ == "__main__":
    main()

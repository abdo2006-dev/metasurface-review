#!/usr/bin/env python3
"""THE authoritative S11 + C1 counts. Every number in the manuscript and in the
generated review-repository files must come from here, not from hand-maintained prose.

Run directly to print the counts; import `counts()` to consume them.
"""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "Documentation"
DECISIONS = DOC / "forward_citation_search_results.csv"
WORKS = DOC / "forward_citation_works_deduplicated.csv"
RECORDS = DOC / "forward_citation_records_raw.csv"


def counts():
    rows = list(csv.DictReader(open(DECISIONS, encoding="utf-8")))
    s2 = [r for r in rows if r["stage2_system_paper"] == "yes"]

    fams = {}
    for r in s2:
        fams.setdefault(r["version_family"], []).append(r)

    def fam_role(fam):
        return fams[fam][0]["version_family_role"]

    def fams_with(role):
        return sorted(f for f in fams if fam_role(f) == role)

    def recs_with(role):
        return [r for r in s2 if r["final_role"] == role]

    read_fams = sorted(f for f in fams if any(x["full_text_inspected"] == "yes" for x in fams[f]))
    unread_fams = sorted(f for f in fams if f not in read_fams)

    c = {
        "retrieval": {
            "records_pre_dedup": sum(1 for _ in csv.DictReader(open(RECORDS, encoding="utf-8"))),
            "unique_works": len(rows),
            "stage1_pass": sum(1 for r in rows if r["stage1_regex_pass"] == "yes"),
            "stage2_records": len(s2),
            "distinct_studies": len(fams),
        },
        "access": {
            "records_read": sum(1 for r in s2 if r["full_text_inspected"] == "yes"),
            "records_unread": sum(1 for r in s2 if r["full_text_inspected"] != "yes"),
            "studies_read": len(read_fams),
            "studies_unread": len(unread_fams),
            "studies_unread_ids": unread_fams,
        },
        "roles": {
            "propagation_records": len(recs_with("propagation")),
            "propagation_studies": len(fams_with("propagation")),
            "propagation_study_ids": fams_with("propagation"),
            "no_timing_records": len(recs_with("no timing value")),
            "no_timing_studies": len(fams_with("no timing value")),
            "no_timing_study_ids": fams_with("no timing value"),
            "unread_records": len(recs_with("unread")),
            "unread_studies": len(fams_with("unread")),
        },
        "table7": {
            "propagation_rows": sorted({r["table7_row"] for r in s2
                                        if r["table7_row"].startswith("P")}),
            "counterexample_rows": sorted({r["table7_row"] for r in s2
                                           if r["table7_row"].startswith("N")}),
            "author_disjoint_counterexample_studies": sorted(
                {r["version_family"] for r in s2
                 if r["table7_row"].startswith("N")
                 and "AUTHOR-DISJOINT" in r["author_network_status"]}),
            "author_disjoint_groups_reproducing": 0,
        },
    }
    c["roles"]["propagation_instances"] = sum(
        len([x for x in r["table7_row"].split(";") if x.strip().startswith("P")])
        for r in s2 if r["table7_row"].startswith("P"))
    # de-duplicate instances across the F-XIA double-index
    seen = set()
    inst = set()
    for r in s2:
        for code in r["table7_row"].split(";"):
            code = code.strip()
            if code.startswith("P"):
                inst.add(code)
    c["roles"]["propagation_instances"] = len(inst)
    c["roles"]["propagation_instance_ids"] = sorted(inst)

    import subprocess, sys
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "c1_stage_counts.py")],
                         capture_output=True, text=True)
    c["c1"] = json.loads(out.stdout.split("{", 1)[1].rsplit("}", 1)[0].join("{}"))
    return c


if __name__ == "__main__":
    print(json.dumps(counts(), indent=1))

#!/usr/bin/env python3
"""Resolve author_network_status for every stage-2 record from published-record metadata.

The v0.21 standing rule bars a source we have not read from supporting a claim about what
that source CONTAINS. It does not bar a claim about its published authorship, which is
verifiable from Crossref/OpenAlex metadata -- and the manuscript already relies on exactly
that distinction for [33]. Leaving six unread studies as "unresolved" understated what the
metadata establishes and left the independence denominator wrong.
"""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "Documentation"
SRC = DOC / "forward_citation_search_results.csv"

# The FIM system-paper lineage audited in this review, and the three primary hardware seeds.
LINEAGE = {"Jiancheng An", "Chau Yuen", "Marco Di Renzo", "Mérouane Debbah",
           "Lajos Hanzo", "H. Vincent Poor"}

RESOLVED = {
 # openalex id: (status, evidence)
 "W7153065651": ("disjoint from FIM lineage (published-record authorship only; full text not read)",
                 "Zuo, Cheng, Qian, Liao, Ding -- no overlap with the lineage"),
 "W7167212071": ("shares author (An) with FIM lineage (published-record authorship only; full text not read)",
                 "Wang, Zhang, An, Cheng, Dong, Wang"),
 "W4414603557": ("shares author (An) with FIM lineage (published-record authorship only; full text not read)",
                 "Ming, An, Gan, Nallanathan, Al-Dhahir"),
 "W7168251020": ("shares author (An) with FIM lineage (published-record authorship only; full text not read)",
                 "Jiang, An, Gan, Al-Dhahir, Karagiannidis"),
 "W4410640243": ("FIM lineage (An, Yuen, Debbah) (published-record authorship only; full text not read)",
                 "An, Debbah, Cui, Chen, Yuen"),
 "W4417282478": ("shares author (Di Renzo) with FIM lineage (published-record authorship only; full text not read)",
                 "Zarini, Kazemi, Sookhak, Ghrayeb, Di Renzo"),
}


def main():
    rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    fields = list(rows[0].keys())
    changed = []
    for r in rows:
        if r["openalex_id"] in RESOLVED:
            new, why = RESOLVED[r["openalex_id"]]
            changed.append((r["version_family"], r["author_network_status"], new, why))
            r["author_network_status"] = new
    with SRC.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(rows)
    for c in changed:
        print(f"  {c[0]:<8} {c[1]!r} -> {c[2]!r}\n      authors: {c[3]}")

    # recompute the study-level distribution
    s2 = [r for r in rows if r["stage2_system_paper"] == "yes"]
    fam = {}
    for r in s2:
        fam.setdefault(r["version_family"], []).append(r)
    buckets = {"shares an author with the FIM lineage": [],
               "disjoint from the FIM lineage but not from all three seeds": [],
               "fully author-disjoint (lineage and all three seeds)": []}
    for f, rs in fam.items():
        st = rs[0]["author_network_status"]
        if "AUTHOR-DISJOINT" in st:
            buckets["fully author-disjoint (lineage and all three seeds)"].append(f)
        elif "disjoint from FIM lineage" in st:
            buckets["disjoint from the FIM lineage but not from all three seeds"].append(f)
        else:
            buckets["shares an author with the FIM lineage"].append(f)
    print("\nSTUDY-LEVEL AUTHOR-NETWORK DISTRIBUTION (all 20 resolved, none unknown):")
    for k, v in buckets.items():
        print(f"  {len(v):>2} of {len(fam)}  {k}\n        {sorted(v)}")


if __name__ == "__main__":
    main()

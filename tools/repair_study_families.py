#!/usr/bin/env python3
"""v0.22 lineage audit: repair `version_family` and reconcile record roles.

RULE (manuscript section 2.4, item 5): a preprint and its version of record are two
versions of one study; a conference paper and its journal extension are ONE lineage.
Shared authorship alone NEVER collapses two studies -- only a bibliographic/version
relationship does.

Every one of the 24 stage-2 records was checked against its OpenAlex author list,
venue, type and date. The audit outcome is recorded below in full, including the
pairs that were examined and deliberately NOT merged.
"""
import csv
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "Documentation"
SRC = DOC / "forward_citation_search_results.csv"

# ---------------------------------------------------------------- audit outcome
# key = openalex id ; value = (final family, one-line justification)
REASSIGN = {
    # CONFERENCE -> JOURNAL EXTENSION. Identical author list (An, Yuen, Di Renzo,
    # Debbah, Poor, Hanzo); GLOBECOM 2024-12-08 conference-paper -> IEEE TWC
    # 2025-01-22 article; same problem (downlink multiuser MISO FIM). The manuscript
    # reference list already labels the journal version "Journal extension of" the
    # conference version. Counting them as two studies violated our own rule.
    "W4408324568": ("F-ANJ-DL", "GLOBECOM 2024 conference version of the TWC 2025 article"),
    "W4406727975": ("F-ANJ-DL", "IEEE TWC 2025 journal extension; version of record"),
}

# Pairs/groups examined and NOT merged, with the reason. Recorded so the audit is
# falsifiable rather than merely asserted.
NOT_MERGED = [
    ("F-MIMO-ISAC vs F-RAN",
     "Both FIM + MIMO ISAC, both 2026. Different first authors (Teng vs Ranasinghe) and "
     "different groups (Gan/Al-Dhahir vs de Abreu/Bremen); only An in common. No version relationship."),
    ("F-MIMO-ISAC vs F-ANJ-MIMO",
     "Similar titles (MIMO ISAC vs MIMO communications) but different first authors, "
     "different author sets, different problems; the ICC 2026 paper post-dates the TCOMM 2025 article."),
    ("F-SRM vs F-ANJ-DL",
     "Both multiuser MISO FIM sum-rate. Different first author (Jiang) and author set; "
     "no shared venue lineage. Distinct study by an overlapping group."),
    ("F-SENS vs F-MIMO-ISAC",
     "Same first author (Teng) and overlapping group, but different problems "
     "(multi-target sensing vs MIMO ISAC) and no version relationship. Shared authorship alone does not merge."),
    ("F-YAN vs F-FAA",
     "Same first author (Songjie Yang) and both IEEE TWC, but different objects "
     "(FIM architecture vs flexible antenna arrays) and different DOIs. Not versions of one study."),
]

# Already-correct families confirmed by the audit:
#   F-FAA  W4409248529 (ICCT 2024 conference) + W4408145283 (TWC 2025 article)
#          -- identical title AND identical author list: conference -> journal. CORRECT.
#   F-XIA  W4416548650 + W7125600937 -- IDENTICAL DOI 10.1109/twc.2026.3654581:
#          one work indexed twice by OpenAlex. CORRECT.
#   F-HU   W7138939285 (GLOBECOM 2025 conference) + W7164909508 (TWC 2026 article)
#          -- same first author Hu, same problem, conference -> journal. CORRECT.

# ------------------------------------------------- role reconciliation (item 6)
# A study is in the NO-TIMING-VALUE set if it cites one or more of the three primary
# hardware sources and attaches no timing value to that hardware in the versions we
# read. The three Table 7 "N" rows are members of that set that are additionally
# noteworthy -- they are NOT a disjoint fourth category. Previously they carried
# final_role="counterexample", which silently removed them from the set the prose
# said they belonged to.
COUNTEREXAMPLES = {"W7117616820": "N1", "W4408325233": "N2", "W4395683696": "N3"}


def main():
    rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    fields = list(rows[0].keys())

    # rename propagation_case_id -> table7_row (it already held N codes too)
    idx = fields.index("propagation_case_id")
    fields[idx] = "table7_row"
    if "version_family_role" not in fields:
        fields.append("version_family_role")

    changed = []
    for r in rows:
        r["table7_row"] = r.pop("propagation_case_id")
        oid = r["openalex_id"]
        if oid in REASSIGN:
            new, why = REASSIGN[oid]
            if r["version_family"] != new:
                changed.append((oid, r["version_family"], new, why))
                r["version_family"] = new
        if oid in COUNTEREXAMPLES:
            if r["final_role"] != "no timing value":
                changed.append((oid, f"role:{r['final_role']}", "role:no timing value",
                                f"Table 7 row {COUNTEREXAMPLES[oid]} is a member of the "
                                f"no-timing-value set, not a separate class"))
                r["final_role"] = "no timing value"

    # study-level role: a family propagates if ANY of its versions does.
    s2 = [r for r in rows if r["stage2_system_paper"] == "yes"]
    fam_rows = {}
    for r in s2:
        fam_rows.setdefault(r["version_family"], []).append(r)
    fam_role = {}
    for fam, rs in fam_rows.items():
        roles = {x["final_role"] for x in rs}
        if "propagation" in roles:
            fam_role[fam] = "propagation"
        elif "no timing value" in roles:
            fam_role[fam] = "no timing value"
        else:
            fam_role[fam] = "unread"
    for r in rows:
        r["version_family_role"] = fam_role.get(r["version_family"], "") if r["stage2_system_paper"] == "yes" else ""

    with SRC.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print("=== CHANGES ===")
    for c in changed:
        print(f"  {c[0]}: {c[1]} -> {c[2]}\n      {c[3]}")
    print("\n=== EXAMINED AND NOT MERGED ===")
    for n, why in NOT_MERGED:
        print(f"  {n}\n      {why}")
    print(f"\nstage-2 records: {len(s2)}   study families: {len(fam_rows)}")
    for fam in sorted(fam_rows):
        print(f"  {fam:<13} {len(fam_rows[fam])} record(s)  role={fam_role[fam]}")


if __name__ == "__main__":
    main()

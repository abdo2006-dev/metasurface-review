#!/usr/bin/env python3
"""Generate Documentation/s11_study_register.md from the decision CSV.

This file is GENERATED. It exists so that every study-level count in the manuscript
is reconstructable from named rows rather than asserted in prose.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import ROOT, DOC, MANUSCRIPT, DECISIONS, WORKS, RECORDS, REGISTER, MATRIX
import csv, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(ROOT / "tools"))
from s11_counts import counts

# Bibliographic data lives in documentation/s11_study_citations.csv, not here. No tool in
# this package holds scientific content: that is what let a retired family split survive
# inside build_forward_citation_csv.py until v0.23.
def _citations():
    import csv as _csv
    cit, ref = {}, {}
    with (DOC / "s11_study_citations.csv").open(encoding="utf-8") as fh:
        for r in _csv.DictReader(fh):
            cit[r["version_family"]] = r["canonical_citation"]
            ref[r["version_family"]] = r["manuscript_ref"]
    return cit, ref


CITATION, REF = _citations()


def main():
    c = counts()
    rows = list(csv.DictReader(open(DOC / "forward_citation_search_results.csv", encoding="utf-8")))
    s2 = [r for r in rows if r["stage2_system_paper"] == "yes"]
    fams = {}
    for r in s2:
        fams.setdefault(r["version_family"], []).append(r)

    L = []
    L.append("# S11 Study Register — the forward citation search, at study level\n")
    L.append("> **GENERATED FILE — do not edit by hand.** Produced by `tools/build_s11_study_register.py`\n"
             "> from `forward_citation_search_results.csv`. Every study-level count in the manuscript is\n"
             "> reconstructable from the rows below.\n")
    r_ = c["retrieval"]; a_ = c["access"]; ro = c["roles"]
    L.append("## 0. The flow, at both levels\n")
    L.append("| Step | Records | Works / studies |\n|---|---|---|")
    L.append(f"| Seed-wise citing records retrieved | **{r_['records_pre_dedup']}** | — |")
    L.append(f"| Deduplicated by OpenAlex identifier | — | **{r_['unique_works']}** works |")
    L.append(f"| Stage-1 screen (explicit {c['regex']['wireless_alternatives']}-alternative expression) | — | **{r_['stage1_pass']}** works |")
    L.append(f"| Stage-2 screen (system studies) | **{r_['stage2_records']}** records | — |")
    L.append(f"| Version-family collapse (§2.4 independence rule) | — | **{r_['distinct_studies']}** distinct studies |")
    L.append(f"| Read in full | {a_['records_read']} records | **{a_['studies_read']}** studies |")
    L.append(f"| Not readable (paywalled, no open deposit) | {a_['records_unread']} records | **{a_['studies_unread']}** studies |")
    L.append("")
    L.append(f"The {a_['studies_read']} studies read in full partition exactly: "
             f"**{ro['propagation_studies']} propagate** a timing value with its scope changed, and "
             f"**{ro['no_timing_studies']} attach no timing value at all**. "
             f"{ro['propagation_studies']} + {ro['no_timing_studies']} = {a_['studies_read']}.\n")

    def block(title, ids, note=""):
        L.append(f"## {title}\n")
        if note:
            L.append(note + "\n")
        L.append("| Study family | Records | Canonical citation | Ref. | Full text read | Primary hardware cited | Timing hit | Table 7 | Author-network relationship |")
        L.append("|---|---|---|---|---|---|---|---|---|")
        for f in ids:
            rs = fams[f]
            r0 = max(rs, key=lambda x: (x["full_text_inspected"] == "yes", x["year"]))
            seeds = "; ".join(sorted({x["cited_seeds"] for x in rs}))
            t7 = "; ".join(sorted({x["table7_row"] for x in rs if x["table7_row"]})) or "—"
            read = "yes" if any(x["full_text_inspected"] == "yes" for x in rs) else "**no**"
            L.append(f"| **{f}** | {len(rs)} | {CITATION.get(f,'?')} | {REF.get(f,'—')} | {read} | "
                     f"{seeds} | {r0['timing_terminology_hit'] or '—'} | {t7} | {r0['author_network_status']} |")
        L.append("")

    block(f"1. Propagation — {ro['propagation_studies']} studies, {ro['propagation_records']} records, "
          f"{len(ro['propagation_instance_ids'])} instances",
          ro["propagation_study_ids"],
          "A primary timing value is reused with its scope changed. Instances: "
          + ", ".join(ro["propagation_instance_ids"]) + ".")
    block(f"2. No timing value — {ro['no_timing_studies']} studies, {ro['no_timing_records']} records",
          ro["no_timing_study_ids"],
          "**This is the set the manuscript refers to in §8.5.** Each cites one or more of the three primary "
          "hardware sources and attaches no timing value to that hardware anywhere in the version(s) inspected. "
          "Table 7 rows N1–N3 are members of this set that are additionally noteworthy — they are **not** a "
          "separate class. F-ANJ-MIMO (N2) names response time as an unresolved practical limitation without "
          "quantifying it, and is counted here: naming a quantity as unresolved is not attaching a value to it.")
    block(f"3. Not readable — {a_['studies_unread']} studies, {ro['unread_records']} records",
          a_["studies_unread_ids"],
          "No content claim of any kind is made about these. They bound every count above from below.")

    L.append("## 4. Version families containing more than one record\n")
    L.append("| Family | Relationship | Records |\n|---|---|---|")
    L.append("| **F-ANJ-DL** | conference → journal extension (GLOBECOM 2024 → IEEE TWC 2025; identical author list) | W4408324568, W4406727975 |")
    L.append("| **F-FAA** | conference → journal extension (ICCT 2024 → IEEE TWC 2025; identical title and author list) | W4409248529, W4408145283 |")
    L.append("| **F-HU** | conference → journal extension (GLOBECOM 2025 → IEEE TWC 2026) | W7138939285, W7164909508 |")
    L.append("| **F-XIA** | one work indexed twice by OpenAlex (identical DOI 10.1109/twc.2026.3654581) | W4416548650, W7125600937 |")
    L.append("")
    L.append("Only the fourth is a pure indexing artefact; the other three are genuine version lineages that "
             "identifier-level deduplication does not collapse. F-ANJ-DL is the lineage in which a timing "
             "assertion appears in the journal version and is absent from the conference version — the "
             "pattern recorded as Table 7 row P4.\n")
    L.append("## 5. Pairs examined and deliberately NOT merged\n")
    L.append("Shared authorship alone never collapses two studies; only a bibliographic or version "
             "relationship does. These candidate pairs were checked against OpenAlex author lists, venues, "
             "types and dates, and kept distinct. Recorded so the lineage audit is falsifiable rather than "
             "merely asserted.\n")
    L.append("| Pair | Why they are not one study |\n|---|---|")
    for pair, why in [
        ("F-MIMO-ISAC vs F-RAN",
         "Both FIM + MIMO ISAC, both 2026. Different first authors (Teng vs Ranasinghe) and different "
         "groups (Gan/Al-Dhahir vs de Abreu/Bremen); only An in common. No version relationship."),
        ("F-MIMO-ISAC vs F-ANJ-MIMO",
         "Similar titles (MIMO ISAC vs MIMO communications) but different first authors, different author "
         "sets, different problems; the ICC 2026 paper post-dates the TCOMM 2025 article."),
        ("F-SRM vs F-ANJ-DL",
         "Both multiuser MISO FIM sum-rate. Different first author (Jiang) and author set; no shared venue "
         "lineage. Distinct study by an overlapping group."),
        ("F-SENS vs F-MIMO-ISAC",
         "Same first author (Teng) and overlapping group, but different problems (multi-target sensing vs "
         "MIMO ISAC) and no version relationship."),
        ("F-YAN vs F-FAA",
         "Same first author (Songjie Yang) and both IEEE TWC, but different objects (FIM architecture vs "
         "flexible antenna arrays) and different DOIs."),
    ]:
        L.append(f"| **{pair}** | {why} |")
    L.append("")
    L.append("> This reasoning was recorded in a one-shot migration script during v0.22. It is scientific "
             "content, so v0.23 moved it here, where it is reviewable without reading code.\n")
    (DOC / "s11_study_register.md").write_text("\n".join(L), encoding="utf-8")
    print(f"wrote s11_study_register.md ({len(L)} lines)")
    print(f"propagation {ro['propagation_studies']} + no-timing {ro['no_timing_studies']} = {a_['studies_read']} read")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate Documentation/s11_study_register.md from the decision CSV.

This file is GENERATED. It exists so that every study-level count in the manuscript
is reconstructable from named rows rather than asserted in prose.
"""
import csv, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "Documentation"
sys.path.insert(0, str(ROOT / "tools"))
from s11_counts import counts

CITATION = {
 "F-ANJ-DL": "An, Yuen, Di Renzo, Debbah, Poor & Hanzo — GLOBECOM 2024 (conf.) / IEEE TWC 2025 (journal ext.), doi:10.1109/twc.2025.3526843",
 "F-ANJ-MIMO": "An, Han, Niyato, Debbah, Yuen & Hanzo, IEEE Trans. Commun., 2025, doi:10.1109/tcomm.2025.3550318",
 "F-APS": "Zuo, Cheng, Qian, Liao & Ding, Acta Physica Sinica 75(1), 2026, doi:10.7498/aps.75.20260154",
 "F-BAN": "Bansal, Hewson, Santer & Whittow, EuCAP 2024, doi:10.23919/EuCAP60739.2024.10501383",
 "F-DRL": "Wang, Zhang, An, Cheng, Dong & Wang, IEEE Wireless Commun. Lett., 2026, doi:10.1109/lwc.2026.3709756",
 "F-FAA": "Yang, An, Xiu, Lyu, Ning, Zhang, Debbah & Yuen — ICCT 2024 (conf.) / IEEE TWC 2025 (journal ext.), doi:10.1109/twc.2025.3545305",
 "F-FCA": "Guo, Yang, Dong, Yang, Deng, Zhang & Yuen, IEEE Internet Things J., 2025, doi:10.1109/jiot.2025.3580372",
 "F-HU": "Hu, An, Gan, Li, Al-Dhahir, Karagiannidis & Nallanathan — GLOBECOM 2025 (conf.) / IEEE TWC 2026 (journal ext.), doi:10.1109/twc.2026.3701359",
 "F-HUA": "Huang, Chen, Xu, Zhu, Pan, Tafazolli & Huang, IEEE J. Sel. Areas Commun., 2025, doi:10.1109/jsac.2025.3639197",
 "F-KUM": "Kumar, Papazafeiropoulos, Kourtessis, Senior, Chafii, Kaklamani & Venieris, IEEE Wireless Commun. Lett., 2025, doi:10.1109/lwc.2025.3649732",
 "F-MIMO-ISAC": "Teng, An, Gan, Karagiannidis, Nallanathan & Al-Dhahir, ICC 2026, doi:10.1109/icc59461.2026.11588131",
 "F-MING": "Ming, An, Gan, Nallanathan & Al-Dhahir, IEEE Trans. Veh. Technol., 2025, doi:10.1109/tvt.2025.3614693",
 "F-RAN": "Ranasinghe, An, Morales Sandoval, Rou, de Abreu, Yuen & Debbah, IEEE TWC, 2026, doi:10.1109/twc.2026.3668992",
 "F-SENS": "Teng, An, Gan, Al-Dhahir & Han, IEEE Trans. Veh. Technol., 2025, doi:10.1109/tvt.2025.3584865",
 "F-SRM": "Jiang, An, Gan, Al-Dhahir & Karagiannidis, ICC 2026, doi:10.1109/icc59461.2026.11587389",
 "F-T3D": "Mursia, Devoti, Rossanese, Sciancalepore, Gradoni, Di Renzo & Costa-Pérez, IEEE Trans. Commun., 2024, doi:10.1109/tcomm.2024.3443738",
 "F-TAP": "An, Debbah, Cui, Chen & Yuen, IEEE Trans. Antennas Propag., 2025, doi:10.1109/tap.2025.3571069",
 "F-XIA": "Xiao, Wang, Cui, Yang, Li, Niyato & Yuen, IEEE TWC, 2026, doi:10.1109/twc.2026.3654581",
 "F-YAN": "Yang, Wan, Ning, Mei, An, Eldar & Yuen, IEEE TWC, 2025, doi:10.1109/twc.2025.3627095",
 "F-ZAR": "Zarini, Kazemi, Sookhak, Ghrayeb & Di Renzo, PIMRC 2025, doi:10.1109/pimrc62392.2025.11274788",
}
REF = {"F-KUM": "[12]", "F-ANJ-MIMO": "[29]", "F-BAN": "[34]", "F-RAN": "[1]",
       "F-ANJ-DL": "[2] / [32]", "F-HU": "[30]", "F-XIA": "[31]", "F-HUA": "[33]"}


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
    L.append(f"| Stage-1 screen (explicit 47-alternative expression) | — | **{r_['stage1_pass']}** works |")
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
    (DOC / "s11_study_register.md").write_text("\n".join(L), encoding="utf-8")
    print(f"wrote s11_study_register.md ({len(L)} lines)")
    print(f"propagation {ro['propagation_studies']} + no-timing {ro['no_timing_studies']} = {a_['studies_read']} read")


if __name__ == "__main__":
    main()

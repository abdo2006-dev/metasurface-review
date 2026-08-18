# S11 Study Register — the forward citation search, at study level

> **GENERATED FILE — do not edit by hand.** Produced by `tools/build_s11_study_register.py`
> from `forward_citation_search_results.csv`. Every study-level count in the manuscript is
> reconstructable from the rows below.

## 0. The flow, at both levels

| Step | Records | Works / studies |
|---|---|---|
| Seed-wise citing records retrieved | **306** | — |
| Deduplicated by OpenAlex identifier | — | **262** works |
| Stage-1 screen (explicit 47-alternative expression) | — | **65** works |
| Stage-2 screen (system studies) | **24** records | — |
| Version-family collapse (§2.4 independence rule) | — | **20** distinct studies |
| Read in full | 16 records | **13** studies |
| Not readable (paywalled, no open deposit) | 8 records | **7** studies |

The 13 studies read in full partition exactly: **4 propagate** a timing value with its scope changed, and **9 attach no timing value at all**. 4 + 9 = 13.

## 1. Propagation — 4 studies, 5 records, 5 instances

A primary timing value is reused with its scope changed. Instances: P1, P2, P3, P4, P5.

| Study family | Records | Canonical citation | Ref. | Full text read | Primary hardware cited | Timing hit | Table 7 | Author-network relationship |
|---|---|---|---|---|---|---|---|---|
| **F-ANJ-DL** | 2 | An, Yuen, Di Renzo, Debbah, Poor & Hanzo — GLOBECOM 2024 (conf.) / IEEE TWC 2025 (journal ext.), doi:10.1109/twc.2025.3526843 | [2] / [32] | yes | BAI|NI | yes | P4 | FIM lineage (An, Yuen) |
| **F-HU** | 2 | Hu, An, Gan, Li, Al-Dhahir, Karagiannidis & Nallanathan — GLOBECOM 2025 (conf.) / IEEE TWC 2026 (journal ext.), doi:10.1109/twc.2026.3701359 | [30] | yes | BAI|NI; NI | yes | P1;P2 | shares author (An) with FIM lineage |
| **F-RAN** | 1 | Ranasinghe, An, Morales Sandoval, Rou, de Abreu, Yuen & Debbah, IEEE TWC, 2026, doi:10.1109/twc.2026.3668992 | [1] | yes | BAI|NI | yes | P5 | FIM lineage (An, Yuen) |
| **F-XIA** | 2 | Xiao, Wang, Cui, Yang, Li, Niyato & Yuen, IEEE TWC, 2026, doi:10.1109/twc.2026.3654581 | [31] | yes | BAI|LI|NI | yes | P3 | shares author (Yuen) with FIM lineage |

## 2. No timing value — 9 studies, 11 records

**This is the set the manuscript refers to in §8.5.** Each cites one or more of the three primary hardware sources and attaches no timing value to that hardware anywhere in the version(s) inspected. Table 7 rows N1–N3 are members of this set that are additionally noteworthy — they are **not** a separate class. F-ANJ-MIMO (N2) names response time as an unresolved practical limitation without quantifying it, and is counted here: naming a quantity as unresolved is not attaching a value to it.

| Study family | Records | Canonical citation | Ref. | Full text read | Primary hardware cited | Timing hit | Table 7 | Author-network relationship |
|---|---|---|---|---|---|---|---|---|
| **F-ANJ-MIMO** | 1 | An, Han, Niyato, Debbah, Yuen & Hanzo, IEEE Trans. Commun., 2025, doi:10.1109/tcomm.2025.3550318 | [29] | yes | BAI | no | N2 | FIM lineage (An, Yuen) |
| **F-BAN** | 1 | Bansal, Hewson, Santer & Whittow, EuCAP 2024, doi:10.23919/EuCAP60739.2024.10501383 | [34] | yes | BAI | no | N3 | AUTHOR-DISJOINT from FIM lineage and from all three seeds |
| **F-FAA** | 2 | Yang, An, Xiu, Lyu, Ning, Zhang, Debbah & Yuen — ICCT 2024 (conf.) / IEEE TWC 2025 (journal ext.), doi:10.1109/twc.2025.3545305 | — | yes | BAI | no | — | disjoint from FIM lineage |
| **F-FCA** | 1 | Guo, Yang, Dong, Yang, Deng, Zhang & Yuen, IEEE Internet Things J., 2025, doi:10.1109/jiot.2025.3580372 | — | yes | BAI | no | — | disjoint from FIM lineage |
| **F-KUM** | 1 | Kumar, Papazafeiropoulos, Kourtessis, Senior, Chafii, Kaklamani & Venieris, IEEE Wireless Commun. Lett., 2025, doi:10.1109/lwc.2025.3649732 | [12] | yes | BAI | no | N1 | AUTHOR-DISJOINT from FIM lineage and from all three seeds |
| **F-MIMO-ISAC** | 1 | Teng, An, Gan, Karagiannidis, Nallanathan & Al-Dhahir, ICC 2026, doi:10.1109/icc59461.2026.11588131 | — | yes | BAI | no | — | FIM lineage (An, Yuen) |
| **F-SENS** | 1 | Teng, An, Gan, Al-Dhahir & Han, IEEE Trans. Veh. Technol., 2025, doi:10.1109/tvt.2025.3584865 | — | yes | BAI | no | — | shares author with FIM lineage |
| **F-T3D** | 1 | Mursia, Devoti, Rossanese, Sciancalepore, Gradoni, Di Renzo & Costa-Pérez, IEEE Trans. Commun., 2024, doi:10.1109/tcomm.2024.3443738 | — | yes | BAI | no | — | shares author (Di Renzo) with FIM lineage |
| **F-YAN** | 1 | Yang, Wan, Ning, Mei, An, Eldar & Yuen, IEEE TWC, 2025, doi:10.1109/twc.2025.3627095 | — | yes | BAI | no | — | FIM lineage (Yuen) |

## 3. Not readable — 7 studies, 8 records

No content claim of any kind is made about these. They bound every count above from below.

| Study family | Records | Canonical citation | Ref. | Full text read | Primary hardware cited | Timing hit | Table 7 | Author-network relationship |
|---|---|---|---|---|---|---|---|---|
| **F-APS** | 1 | Zuo, Cheng, Qian, Liao & Ding, Acta Physica Sinica 75(1), 2026, doi:10.7498/aps.75.20260154 | — | **no** | NI | unknown | — | AUTHOR-DISJOINT from FIM lineage and from all three seeds (published-record authorship only; full text not read) |
| **F-DRL** | 1 | Wang, Zhang, An, Cheng, Dong & Wang, IEEE Wireless Commun. Lett., 2026, doi:10.1109/lwc.2026.3709756 | — | **no** | BAI | unknown | — | shares author (An) with FIM lineage (published-record authorship only; full text not read) |
| **F-HUA** | 1 | Huang, Chen, Xu, Zhu, Pan, Tafazolli & Huang, IEEE J. Sel. Areas Commun., 2025, doi:10.1109/jsac.2025.3639197 | [33] | **no** | LI | unknown | — | disjoint from FIM lineage; shares author (T. Pan) with seed LI |
| **F-MING** | 1 | Ming, An, Gan, Nallanathan & Al-Dhahir, IEEE Trans. Veh. Technol., 2025, doi:10.1109/tvt.2025.3614693 | — | **no** | BAI|NI | unknown | — | shares author (An) with FIM lineage (published-record authorship only; full text not read) |
| **F-SRM** | 1 | Jiang, An, Gan, Al-Dhahir & Karagiannidis, ICC 2026, doi:10.1109/icc59461.2026.11587389 | — | **no** | BAI|NI | unknown | — | shares author (An) with FIM lineage (published-record authorship only; full text not read) |
| **F-TAP** | 1 | An, Debbah, Cui, Chen & Yuen, IEEE Trans. Antennas Propag., 2025, doi:10.1109/tap.2025.3571069 | — | **no** | BAI|NI | unknown | — | FIM lineage (An, Yuen, Debbah) (published-record authorship only; full text not read) |
| **F-ZAR** | 1 | Zarini, Kazemi, Sookhak, Ghrayeb & Di Renzo, PIMRC 2025, doi:10.1109/pimrc62392.2025.11274788 | — | **no** | BAI | unknown | — | shares author (Di Renzo) with FIM lineage (published-record authorship only; full text not read) |

## 4. Version families containing more than one record

| Family | Relationship | Records |
|---|---|---|
| **F-ANJ-DL** | conference → journal extension (GLOBECOM 2024 → IEEE TWC 2025; identical author list) | W4408324568, W4406727975 |
| **F-FAA** | conference → journal extension (ICCT 2024 → IEEE TWC 2025; identical title and author list) | W4409248529, W4408145283 |
| **F-HU** | conference → journal extension (GLOBECOM 2025 → IEEE TWC 2026) | W7138939285, W7164909508 |
| **F-XIA** | one work indexed twice by OpenAlex (identical DOI 10.1109/twc.2026.3654581) | W4416548650, W7125600937 |

Only the fourth is a pure indexing artefact; the other three are genuine version lineages that identifier-level deduplication does not collapse. F-ANJ-DL is the lineage in which a timing assertion appears in the journal version and is absent from the conference version — the pattern recorded as Table 7 row P4.

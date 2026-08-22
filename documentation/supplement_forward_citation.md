# Supplementary Section S5 — Forward-citation search, screening flow and study-family register

This section records what is needed to audit contribution C3. The per-work decision table (one row for each of the 262 works) and the executable retrieval and screening code are in the public reproducibility repository, `https://github.com/abdo2006-dev/metasurface-review`.

## S5.1 Retrieval and screening flow

| Step | Count |
|---|---|
| Seed-wise citing records retrieved (three primary hardware sources) | **306** |
| Unique works after deduplication by identifier | **262** |
| Passing the stage-1 title/abstract expression | **65** |
| Stage-2 candidate system-study records | **24** |
| Distinct studies after version-family collapse | **20** |
| Read in full | **13** |
| Behind publisher paywalls, no open deposit, not read | **7** |

Stage one is automatic and deterministic for the dated 18 August 2026 search: re-running the published code against the preserved records reproduces it exactly, while a live re-query may differ because OpenAlex is updated continuously. Stage two is a manual judgement recorded per work with its reason. The **13 studies read in full partition exactly into 4 propagation studies and 9 no-timing-value studies**. The remaining **7 of the 20 studies were not readable in full**.

## S5.2 Version-family collapse rule

A preprint and its version of record are two versions of one study; a conference paper and its journal extension are one lineage; supplementary material belongs to its parent paper. Shared authorship alone never collapses two studies — only a bibliographic or version relationship does. Identifier-level deduplication does not perform this collapse: four version groups occur here, of which one is a single work indexed twice and three are genuine conference-to-journal or preprint-to-record lineages. One of those lineages carries a timing assertion in its journal version that is absent from its conference version.

## S5.3 Study-family register — all 20 studies

Author-network status is taken from published-record author lists, which are verifiable even where the full text is not. "Lineage" means the FIM system papers audited in §5.2; "seeds" means the three primary hardware sources.

| Study family | Records | Citation | Full text | Final role | Author network |
|---|---|---|---|---|---|
| **F-ANJ-DL** | 2 | An, Yuen, Di Renzo, Debbah, Poor & Hanzo — GLOBECOM 2024 (conf.) / IEEE TWC 2025 (journal ext.), doi:10.1109/twc.2025.3526843 · [2] / [32] | read | propagation | shares an author with the lineage |
| **F-ANJ-MIMO** | 1 | An, Han, Niyato, Debbah, Yuen & Hanzo, IEEE Trans. Commun., 73(9):7349-7365, Sep. 2025, doi:10.1109/tcomm.2025.3550318 · [29] | read | no timing value | shares an author with the lineage |
| **F-APS** | 1 | Zuo, Cheng, Qian, Liao & Ding, Acta Physica Sinica 75(1), 2026, doi:10.7498/aps.75.20260154  | **not readable** | not readable | disjoint from lineage **and** all three seeds |
| **F-BAN** | 1 | Bansal, Hewson, Santer & Whittow, EuCAP 2024, doi:10.23919/EuCAP60739.2024.10501383 · [34] | read | no timing value | disjoint from lineage **and** all three seeds |
| **F-DRL** | 1 | Wang, Zhang, An, Cheng, Dong & Wang, IEEE Wireless Commun. Lett., 2026, doi:10.1109/lwc.2026.3709756  | **not readable** | not readable | shares an author with the lineage |
| **F-FAA** | 2 | Yang, An, Xiu, Lyu, Ning, Zhang, Debbah & Yuen — ICCT 2024 (conf.) / IEEE TWC 2025 (journal ext.), doi:10.1109/twc.2025.3545305  | read | no timing value | disjoint from the lineage |
| **F-FCA** | 1 | Guo, Yang, Dong, Yang, Deng, Zhang & Yuen, IEEE Internet Things J., 2025, doi:10.1109/jiot.2025.3580372  | read | no timing value | disjoint from the lineage |
| **F-HU** | 2 | Hu, An, Gan, Li, Al-Dhahir, Karagiannidis & Nallanathan — GLOBECOM 2025 (conf.) / IEEE TWC 2026 (journal ext.), doi:10.1109/twc.2026.3701359 · [30] | read | propagation | shares an author with the lineage |
| **F-HUA** | 1 | Huang, Chen, Xu, Zhu, Pan, Tafazolli & Huang, IEEE J. Sel. Areas Commun., 2025, doi:10.1109/jsac.2025.3639197 · [33] | **not readable** | not readable | disjoint from the lineage |
| **F-KUM** | 1 | Kumar, Papazafeiropoulos, Kourtessis, Senior, Chafii, Kaklamani & Venieris, IEEE Wireless Commun. Lett., 2025, doi:10.1109/lwc.2025.3649732 · [12] | read | no timing value | disjoint from lineage **and** all three seeds |
| **F-MIMO-ISAC** | 1 | Teng, An, Gan, Karagiannidis, Nallanathan & Al-Dhahir, ICC 2026, doi:10.1109/icc59461.2026.11588131  | read | no timing value | shares an author with the lineage |
| **F-MING** | 1 | Ming, An, Gan, Nallanathan & Al-Dhahir, IEEE Trans. Veh. Technol., 2025, doi:10.1109/tvt.2025.3614693  | **not readable** | not readable | shares an author with the lineage |
| **F-RAN** | 1 | Ranasinghe, An, Morales Sandoval, Rou, de Abreu, Yuen & Debbah, IEEE TWC, 2026, doi:10.1109/twc.2026.3668992 · [1] | read | propagation | shares an author with the lineage |
| **F-SENS** | 1 | Teng, An, Gan, Al-Dhahir & Han, IEEE Trans. Veh. Technol., 2025, doi:10.1109/tvt.2025.3584865  | read | no timing value | shares an author with the lineage |
| **F-SRM** | 1 | Jiang, An, Gan, Al-Dhahir & Karagiannidis, ICC 2026, doi:10.1109/icc59461.2026.11587389  | **not readable** | not readable | shares an author with the lineage |
| **F-T3D** | 1 | Mursia, Devoti, Rossanese, Sciancalepore, Gradoni, Di Renzo & Costa-Pérez, IEEE Trans. Commun., 2024, doi:10.1109/tcomm.2024.3443738  | read | no timing value | shares an author with the lineage |
| **F-TAP** | 1 | An, Debbah, Cui, Chen & Yuen, IEEE Trans. Antennas Propag., 2025, doi:10.1109/tap.2025.3571069  | **not readable** | not readable | shares an author with the lineage |
| **F-XIA** | 2 | Xiao, Wang, Cui, Yang, Li, Niyato & Yuen, IEEE TWC, 2026, doi:10.1109/twc.2026.3654581 · [31] | read | propagation | shares an author with the lineage |
| **F-YAN** | 1 | Yang, Wan, Ning, Mei, An, Eldar & Yuen, IEEE TWC, 2025, doi:10.1109/twc.2025.3627095  | read | no timing value | shares an author with the lineage |
| **F-ZAR** | 1 | Zarini, Kazemi, Sookhak, Ghrayeb & Di Renzo, PIMRC 2025, doi:10.1109/pimrc62392.2025.11274788  | **not readable** | not readable | shares an author with the lineage |

## S5.4 What the register supports

- **4 studies** reuse a primary timing value with its scope changed, carrying 5 instances (P1, P2, P3, P4, P5), and they form **one connected co-authorship network**.
- **9 studies** cite the same primary hardware and attach no timing value; two of them share no author with the lineage or any seed.
- **0 author-disjoint publication groups** reproduce the practice within the observation window, which is why C3 is held at its stated evidence level.
- **7 studies** could not be read. Exactly one of them is disjoint from both the lineage and all three seeds, so that single study is the whole residual risk to the independence finding. No claim is made about what any unread study contains.

Every count above is a lower bound on a partially observed set, and no prevalence, proportion or rate is estimated from it.

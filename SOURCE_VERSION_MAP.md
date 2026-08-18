# Source Version Map

**Snapshot: manuscript v0.21, documentation v1.8, generated 2026-08-18 19:12 UTC.**

Bibliographic identity and version-inspection status for every source cited in the manuscript's numbered reference list (`manuscript/99_references.md`), plus every external source verified for the bibliography but cited only in passing. **This is metadata only — no source PDF is distributed in this repository.** Every DOI and arXiv identifier here was resolved against the publisher-deposited Crossref record or the arXiv metadata endpoint on 18 August 2026 (`documentation/source_inventory.md` §3b). Full extraction detail, per-quantity locators, and independence-group definitions are in `documentation/source_inventory.md` and `documentation/audits/independence_audit.md`; this table is a navigation aid, not a replacement for them.

**Columns.** *Held* = full text was obtained and inspected by the private working repository (project corpus), independent of whether it is the version of record. *VoR inspected* = the publisher-deposited version of record was itself obtained and read, not merely confirmed to exist. *Family / independence group* = other entries this source is **not** independent of — same study, same prototype, or a materially overlapping author set — per the project's independence rule (independence is judged by author-set intersection, not by which author is listed first). *§* = manuscript sections that cite this reference number.

## FIM system and channel-estimation sources

| # | Key | Title | Authors | Year (VoR) | Venue / identifier | Held | VoR inspected | Family / independence group | § |
|---|---|---|---|---|---|---|---|---|---|
| [1] | RAN-25 | Flexible intelligent metasurfaces in high-mobility MIMO ISAC | Ranasinghe, An, Morales Sandoval, Rou, de Abreu, Yuen, Debbah | 2026 | *IEEE TWC* 25:13319–13335 · 10.1109/TWC.2026.3668992 | Y (preprint + VoR) | Y | **IG-1** with [15] (MOR-26 is an explicitly-stated shorter version of this study, not a second confirmation); preprint arXiv:2507.18793 retained as the earlier version of this same study, not a separate source | 1,3,5,6,8,9 |
| [2] | ANJ-25 | Downlink multiuser communications relying on FIMs | An, Yuen, Di Renzo, Debbah, Poor, Hanzo | 2024 | GLOBECOM, pp. 4932–4937 · 10.1109/GLOBECOM52923.2024.10901792 | Y | Y | **IG-2** with [32] (ANJ-25J) — same team's conference and journal papers on the same result, not two independent confirmations | 1,3,5,6 |
| [3] | YAN-25 | FIM-aided wireless communications: architecture and performance | Yang, Wan, Ning, Mei, An, Eldar, Yuen | 2026 | *IEEE TWC* 25:6823–6836 · 10.1109/TWC.2025.3627095 | Y (preprint + VoR) | Y | **IG-3**; preprint arXiv:2503.11112 retained as the earlier version of this same study | 1,3,5,6,7 |
| [15] | MOR-26 | Bistatic ISAC with FIMs | Morales Sandoval, Venkataramanaiah, Ranasinghe, An, Rou, de Abreu | 2026 | arXiv:2607.29137 | Y | — (preprint only) | **IG-1 — not independent of [1]**; states in its own text that [1] is its extended version | 3,5,6 |
| [19] | XU-22 | Channel estimation for RIS-assisted high-mobility wireless systems | Xu, An, Bai, Sugiura, Maunder, Wang, Yang, Hanzo | 2023 | *IEEE TVT* 72(1):718–734 · 10.1109/TVT.2022.3203818 | Y (draft + VoR) | Y | **IG-4**; held draft retained as the earlier version of this same study | 3,4,5,6 |
| [11] | MA-26 | Survey on reconfigurable and movable antennas | Ma, Zhu, Tan, Zheng, Y. Zhang, Y. Zhang, Ying, Gao, Sun, Shao, Xiao, Niyato, R. Zhang | 2026 | arXiv:2602.17977; TechRxiv preprint DOI 10.36227/techrxiv.176857884.40392967/v1 | Y | — (**no journal version of record located**; cite as preprint) | **IG-11** | 3,5,7 |
| [12] | KUM-25 | FIM for downlink communications under statistical CSI | Kumar, Papazafeiropoulos, Kourtessis, Senior, Chafii, Kaklamani, Venieris | 2026 | *IEEE WCL* 15:1150–1154 · 10.1109/LWC.2025.3649732 | N | Y (read as arXiv:2512.23045) | shares three authors (Kumar, Papazafeiropoulos, Chafii) with [13] — one line of work, not two independent confirmations of statistical-CSI FIM optimisation | 1,4,8 |
| [13] | LFIM-26 | Achievable rate optimisation for large FIM-assisted downlink MISO under statistical CSI | He, Kumar, Papazafeiropoulos, Wen, Tran, Chafii | 2026 | arXiv:2601.15471 | N | **N — identified bibliographically only** | see [12] | 1,4 |
| [14] | FAS-26 | Fluid antenna systems enabling 6G HRLLC with port switching delay | Zhu, Wong, H. Xu, Rao, Shin | 2026 | arXiv:2605.06275 | N | **N — identified bibliographically only**; cited solely as a delay-aware-modelling precedent in an adjacent field | 1 |
| [29] | ANJ-MIMO | FIMs for enhancing MIMO communications | An, Han, Niyato, Debbah, Yuen, Hanzo | 2025 | arXiv:2502.16478 | N | N — author version only; *IEEE Trans. Commun.* record not retrieved | shares authors (An, Yuen) with [1], [2], [32] — see the cross-cutting authorship note below | 4,6,8,9 |
| [30] | HU-26 | Weighted sum-rate enhancement for FIM-assisted multicell systems | Hu, An, Gan, H. Li, Al-Dhahir, Karagiannidis, Nallanathan | 2026 | *IEEE TWC* 25:18579–18595 · 10.1109/TWC.2026.3701359 | N | Y (read as arXiv:2606.06845) | shares author (An) with [1], [2], [29], [32] | 8 |
| [31] | XIA-26 | Channel estimation for FIMs: model-based approaches to neural operators | Xiao, J. Wang, Cui, Y. Yang, X. Li, Niyato, Yuen | 2026 | *IEEE TWC* 25:10684–10701 · 10.1109/TWC.2026.3654581 | N | Y (read as arXiv:2508.00268v4) | shares author (Yuen) with [1], [3] | 8 |
| [32] | ANJ-25J | FIMs for downlink multiuser MISO communications | An, Yuen, Di Renzo, Debbah, Poor, Hanzo | 2025 | *IEEE TWC* 24(4):2940–2955 · 10.1109/TWC.2025.3526843 | N (read from an open institutional repository, not archived locally) | Y | **IG-2 — journal extension of [2]**, same result, not independent | 8 |

**Cross-cutting authorship note.** An and/or Yuen appear as authors on [1], [2], [29], [30], [31] and [32] — the majority of the FIM system-modelling literature cited in this manuscript. Simulated-gain claims drawn from more than one of these papers are reported in the manuscript as coming from *several formulations*, not from *independent* ones (`documentation/manuscript_argument_map.md`; this wording was corrected during the v0.20 self-review — see `CHANGELOG.md` CH-98).

## Hardware evidence sources

| # | Key | Title | Authors | Year | Venue / identifier | Held | Family / independence group | § |
|---|---|---|---|---|---|---|---|---|
| [6] | LI-25 | Flexible intelligent microwave metasurface with shape-guided adaptive programming | F. Li, Pan, W. Li, Peng, Guo, Jia, Hu, L. Wang, W. Wang, Gao, Yao, Zuo, Bi, Weng, Tang, Lin | 2025 | *Nature Commun.* 16:3161 · 10.1038/s41467-025-58249-9 | Y — main text + Supplementary Information + Peer Review File | **IG-5**; SI and peer-review file belong to this study, not independent evidence | 1,3,4,5,6,7,8,9 |
| [7] | BAI-22 | A dynamically reprogrammable surface with self-evolving shape morphing | Bai, H. Wang, Xue, Y. Pan, Kim, X. Ni, Liu, Yang, Han, Y. Huang, Rogers, X. Ni | 2022 | *Nature* 609(7928):701–708 · 10.1038/s41586-022-05061-w | Y — main text + Extended Data + Supplementary Information + Peer Review File | **IG-8**; SI and peer-review file belong to this study, not independent evidence | 1,3,5,6,7,8,9 |
| [8] | NI-22 | Soft shape-programmable surfaces by fast electromagnetic actuation of liquid metal networks | X. Ni, Luan, Kim, Rogge, Bai, Kwak, S. Liu, Yang, S. Li, S. Li, Z. Li, Y. Zhang, Wu, X. Ni, Y. Huang, H. Wang, Rogers | 2022 | *Nature Commun.* 13:5576 · 10.1038/s41467-022-31092-y | Y | **IG-9** | 1,3,5,6,7,8,9 |
| [4] | AKR-26 | A scalable and integrated reconfigurable intelligent surface | Akram, Elsayed, Hameed, M. Ali, Kazim, Imran, Abbasi | **2026** | *Adv. Electron. Mater.* 12(1), art. e00674 · 10.1002/aelm.202500674 (online 12 Dec 2025; issue dated Jan 2026) | Y | **IG-7** | 1,3,5,6,7,9 |
| [5] | NEU-24 | Sub-100 ms liquid crystal RIS based on defected delay lines | Neuder, Späth, Schüßler, Jiménez-Sáez | 2024 | *Commun. Eng.* 3(1), art. 70 · 10.1038/s44172-024-00214-3 | Y | **IG-6** | 1,3,5,6,7 |
| [20] | GAL-22 | Flexible active antenna arrays | Gal-Katziri, Fikes, Hajimiri | 2022 | *npj Flexible Electron.* 6:85 · 10.1038/s41528-022-00218-z | Y | **IG-10** | 3,4,5,6,7,9 |

## Reviews

| # | Key | Title | Authors | Year | Venue / identifier | Held | Family / independence group | § |
|---|---|---|---|---|---|---|---|---|
| [9] | SAI-22 | Recent progress in reconfigurable and intelligent metasurfaces | Saifullah, Y. He, Boag, Yang, F. Xu | 2022 | *Adv. Sci.* 9(33), art. 2203747 · 10.1002/advs.202203747 | Y | **IG-12** | 1,6 |
| [10] | TIS-25 | Multi-functional and hybrid RIS for ISAC — a survey | Tishchenko, Khalily, Shojaeifard, Burton, Björnson, Di Renzo, Tafazolli | 2025 | *IEEE Commun. Surv. Tuts.* 27(5):2895–2936 · 10.1109/COMST.2024.3519785 | Y — published + accepted-manuscript duplicate | **IG-13**; the accepted-manuscript copy is a duplicate of the published version, not independent evidence | 1 |

## Conformal / prior-art / antenna sources

| # | Key | Title | Authors | Year | Venue / identifier | Held | Family / independence group | § |
|---|---|---|---|---|---|---|---|---|
| [16] | GUO-25 | Beam steering flexible transparent metasurfaces | Guo, Xin, H. Sun, H. Li, Chernogor, Jin, Liu, Zheng | 2025 | *Sci. Rep.* 15 · 10.1038/s41598-025-99768-1 | Y | **IG-17** | 3 |
| [17] | LU-25 | A versatile design method applied to conformal metasurface array antenna | Lu, Z. Wang, C. Zhang, Yu | 2025 | *Microw. Opt. Technol. Lett.* 67(3):e70134 · 10.1002/mop.70134 | Y (rasterised; read from rendered page images) | **IG-22** with [18] — same group (Nanjing Univ. Posts & Telecom, Y. Yu corresponding) | 3,9 |
| [18] | LU-26 | Conformal reconfigurable reflectarray antenna based on flexible material | Lu, C. Zhang, Z. Wang, R. Li, Yan, Yu | 2026 | *IEEE AWPL* 25(5):2265–2269 · 10.1109/LAWP.2026.3676871 | Y | **IG-22** with [17] | 3,5,6 |
| [21] | ALE-26 | Curvature effect in flexible antenna arrays for 6G beam alignment | Alesheikh, Saadat, Aghasi | 2025 | *Proc. IEEE AP-S/CNC-USNC-URSI*, pp. 1–4 · 10.1109/AP-S/CNC-USNC-URSI55537.2025.11265965 | Y (arXiv:2409.09590 preprint held) | **IG-18**; VoR full text not retrieved, metadata confirmed | 3 |
| [22] | BUD-22 | Design of planar and conformal, passive, lossless metasurfaces that beamform | Budhu, Szymanski, Grbic | 2022 | *IEEE J. Microw.* 2(3):401–418 · 10.1109/JMW.2022.3181719 | Y | **IG-14**; DOI was corrected during the bibliographic pass — an earlier record pointed to an unrelated paper (`CHANGELOG.md` CH-96) | 3 |
| [23] | YOO-21 | Conformal array of rectangular waveguide-fed metasurfaces | Yoo, Smith | 2021 | arXiv:2109.09450 | Y | **IG-19** | 3 |
| [24] | LIH-19 | Wide-angle beam steering based on an active conformal metasurface lens | H. Li, Ma, Shen, K. Xu, Ye, Huangfu, C. Li, Ran, Denidni | 2019 | *IEEE Access* 7:185264–185272 · 10.1109/ACCESS.2019.2960639 | Y | **IG-15** | 3 |
| [25] | PEP-26 | Conformal RIS: a cylindrical geometry perspective | Pepe, Iudice, Castaldi, Di Renzo, Galdi | 2026 | *Adv. Electron. Mater.* e00550 · 10.1002/aelm.202500550 | Y (rasterised; read from rendered page images) | **IG-21** | 3 |
| [26] | CHE-26 | Wide-angle conformal active metasurface for dynamic beam steering and OAM generation | H. Chen, T. Liu, M. Chen, D. Wang, W. Li, Wu, L. Wang, Liu, L. Wang | **2026** | *Laser Photon. Rev.* 20(3), art. e01500 · 10.1002/lpor.202501500 (online 28 Sep 2025; issue dated Feb 2026) | Y (rasterised; read from rendered page images) | **IG-23** | 3 |
| [27] | HAR-20 | Continuously tunable reflectarray element for 5G metrology in the K-band | Harz, Kleine-Ostmann, Schrader | 2020 | *Adv. Radio Sci.* 18:1–5 · 10.5194/ars-18-1-2020 | Y | **IG-20** with [28] — same group, same design lineage | 3 |
| [28] | HAR-22 | Measurement and optimisation of a continuously tunable 10×10 reflectarray for 5G metrology | Harz, Kleine-Ostmann | 2022 | *Adv. Radio Sci.* 19:215–220 · 10.5194/ars-19-215-2022 | Y | **IG-20** with [27] — not independent | 3 |
| [33] | HUA-25 | Flexible RIS-aided covert communications in UAV networks | C. Huang, G. Chen, Z. Xu, J. Zhu, **T. Pan**, Tafazolli, W. Huang | 2026 | *IEEE JSAC* 44:1577–1588 · 10.1109/JSAC.2025.3639197 | N | Crossref author-list metadata inspected; full text not confirmed read. **Shares author Taisong Pan with [6] (LI-25)** — this is the corrected independence finding behind manuscript Table 7 row N1 (`CHANGELOG.md` CH-97): disjoint from the FIM system-paper lineage that §8's forward search measured, but not disjoint from the cited hardware source | 8 |

## Held but not cited in the v0.20 manuscript text

`TAG-20` (Taghvaee, *Scalability Analysis of Programmable Metasurfaces for Beam Steering*, arXiv:2004.06917) is present in the project corpus and belongs to the separate, out-of-scope CST/full-wave companion project (`documentation/article_type_assessment.md` §6). It does not appear in `manuscript/99_references.md` and carries no manuscript-section citation.

# Literature Search Log

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.1 · **Search conducted:** 17 August 2026; **forward citation search (S11) 18 August 2026** · **Searcher:** Claude (Opus 5)
**Purpose:** to record every search performed *beyond* the supplied project corpus, so that novelty and absence claims can be scoped honestly.

---

## 1. Declared limitations of this search — read before using any absence claim

This log records a **targeted verification search**, not a systematic search. Specifically:

| Requirement of a systematic search | Status here |
|---|---|
| Multiple indexed databases (Scopus, Web of Science, IEEE Xplore, Compendex) queried with recorded strings | ✗ **not done** — only a general web search interface was available |
| Protocol registered or pre-specified before searching | ✗ not done |
| Exhaustive Boolean strings with controlled vocabulary / MeSH-equivalent | ✗ not done |
| Year, language and document-type filters applied and recorded | ✗ not applied |
| Two independent screeners, disagreement resolution | ✗ single agent |
| Full backward citation chasing (all reference lists) | ✗ partial only |
| Full forward citation chasing (cited-by) | ✅ **done 18 Aug 2026 (S11)** — exhaustive cited-by retrieval for BAI-22, NI-22 and LI-25 via the OpenAlex citation graph, 262 unique works screened. Bounded by full-text access: 13 of 20 system papers retrieved, 7 paywalled |
| Duplicate handling and screening flow counts (PRISMA-style) | ✗ not done |
| Reproducible hit counts per string | ✗ the interface does not expose result counts |

**Consequence.** Every conclusion about what does or does not exist in the wider literature must be worded as *"within the reviewed corpus and the searches recorded in this log"*. No unqualified "no prior work exists" statement is licensed by this log. See `absence_claims.md`.

**Interfaces used:** for S1–S10, general web search + direct retrieval of arXiv abstract/HTML pages (result rankings are not deterministic and may differ on repetition). For **S11 (18 Aug 2026)**, the OpenAlex, Crossref and Semantic Scholar REST APIs plus the arXiv PDF endpoint — these *are* deterministic and reproducible, and the exact queries are given in S11. **No paywalled full text was retrieved at any point**; every full text read is an author version, an arXiv deposit, or an open institutional-repository copy. Seven identified papers could not be read for this reason, and every count in S11 is therefore a **lower bound**.

---

## 2. Search objectives

| ID | Objective |
|---|---|
| O1 | Determine whether a FIM-specific *review or survey* exists (which would directly pre-empt this manuscript) |
| O2 | Determine whether *two-timescale / statistical-CSI FIM control* is already published (which would pre-empt the originally proposed framing) |
| O3 | Determine whether *measured FIM actuation latency* exists anywhere (which would close the central validation gap) |
| O4 | Trace the provenance of hardware-feasibility timing claims made in the FIM system literature |
| O5 | Sanity-check the adjacent movable/fluid-antenna field for an equivalent hardware-reporting critique |

---

## 3. Searches performed

### S1 — 17 Aug 2026 · Objective O1, O3
**String:** `flexible intelligent metasurface FIM survey review hardware validation`
**Notable hits:**
- arXiv:2512.23045 / IEEE — *Flexible Intelligent Metasurface for Downlink Communications under Statistical CSI*
- arXiv:2508.00268 — *Channel Estimation for Flexible Intelligent Metasurfaces: From Model-Based Approaches to Neural Operators*
- arXiv:2502.16478 — *Flexible Intelligent Metasurfaces for Enhancing MIMO Communications*
- arXiv:2606.06845 — *Weighted Sum-Rate Enhancement for FIM-Assisted Multicell Systems*
- arXiv:2411.19754 — *Emerging Technologies in Intelligent Metasurfaces* (broad, not FIM-specific)
**Outcome for O1:** **no dedicated FIM review or survey returned.** The FIM literature returned is uniformly primary system-level modelling work.
**Outcome for O3:** no measured FIM actuation latency returned; results describe *assumed* millisecond morphing.

### S2 — 17 Aug 2026 · Objective O2
**String:** `"flexible intelligent metasurface" two-timescale OR "statistical CSI" morphing control`
**Notable hits:** arXiv:2512.23045; arXiv:2601.15471 (*Achievable Rate Optimization for Large FIM Assisted Downlink MISO under Statistical CSI*); arXiv:2605.29227; arXiv:2606.06845.
**Outcome — decisive for this project:** statistical-CSI-based FIM shape optimisation **is already published**. A two-timescale split (phase per coherence interval, shape on a longer statistical timescale) is explicitly present in this literature line.
**Consequence:** the working title *"From Instantaneous Shape Optimization to Two-Timescale Control"* would **overclaim**. Reframed — see `novelty_boundary.md` and `article_type_assessment.md`.

### S3 — 17 Aug 2026 · Objective O2 (verification fetch)
**URL:** `https://arxiv.org/abs/2512.23045`
**Retrieved:** Kumar, Papazafeiropoulos, Kourtessis, Senior, Chafii, Kaklamani, Venieris, *Flexible Intelligent Metasurface for Downlink Communications under Statistical CSI*, submitted 28 Dec 2025. Abstract states the work departs "from prior works that rely on instantaneous channel state information (CSI)" and maximises average sum spectral efficiency **under statistical CSI**, via gradient projection.
**Finding:** confirms O2. The abstract itself contains **no hardware prototype, actuator, or measured latency**. The explicit per-coherence-interval / per-multiple-coherence-interval phrasing seen in search summaries was **not confirmed in the abstract**; treat that specific phrasing as `[FULL TEXT MISSING — VERIFY BEFORE CLAIM]`.

### S4 — 17 Aug 2026 · Objective O3, O4
**String:** `flexible intelligent metasurface prototype actuation latency measured reconfiguration time experiment`
**Notable hits:** LI-25 (already in corpus); arXiv:2502.16478; arXiv:2606.06845; arXiv:2510.07466; RAN-25.
**Finding:** the only *measured* flexible-metasurface loop returned is LI-25, already in the corpus. Search summaries surfaced a recurring claim that "the response time of FIM surface morphing reaches 10 ms" — pursued in S5–S7.

### S5 — 17 Aug 2026 · Objective O4 (verification fetch)
**URL:** `https://arxiv.org/html/2502.16478v2` — An et al., *Flexible Intelligent Metasurfaces for Enhancing MIMO Communications*
**Finding:** **no millisecond figure stated.** Morphing described qualitatively as "rapidly and precisely morphing its surface shape". **Remark 4** states that *"surface shapes of the transmitting and receiving FIMs are only updated on the timescale of the channel's coherence block."*
**Significance:** this is the cleanest available statement of the *modelling assumption* that the entire mechanical adaptation loop completes within one coherence block. Recorded as evidence `E-ASM-02`. `[EXTERNAL — HTML INSPECTED, PDF NOT ARCHIVED]`

### S6 — 17 Aug 2026 · Objective O4 (verification fetch)
**URL:** `https://arxiv.org/html/2510.07466v1` — Hu, An, Gan, Al-Dhahir, *Flexible Intelligent Metasurface for Reconfiguring Radio Environments*
**Finding — verbatim:** *"Moreover, the deformation response time (i.e., reconfigurability rate) of the FIM is on the order of milliseconds, which is comparable to the coherence time of the channel under typical mobile conditions, allowing it to adapt the wireless channel in real time."* Reported as appearing in an explanatory footnote **without a bibliographic citation attached**.
Recorded as `E-ASM-03`. `[EXTERNAL — HTML INSPECTED]`

### S7 — 17 Aug 2026 · Objective O4
**String:** `"flexible intelligent metasurface" "10 ms" morphing response time coherence block`
**Lead:** arXiv:2606.06845 states "the response time of FIM surface morphing reaches 10 ms according to Table I".

### S8 — 17 Aug 2026 · Objective O4 (targeted table retrieval) ★ key result
**URL:** `https://arxiv.org/html/2606.06845v1` — Hu, An, Gan, Li, Al-Dhahir, Karagiannidis, Nallanathan, *Weighted Sum-Rate Enhancement for Flexible Intelligent Metasurface-Assisted Multicell Systems*, 5 Jun 2026.
**Table I "Key Parameters of Existing FIMs" retrieved:**

| | Ni et al. [38] 2022 | Bai et al. [39] 2021 | Niu et al. [40] 2022 |
|---|---|---|---|
| Material | Silicone & Liquid metal | Polyimide & Gold | Hydrogel & SMP & Nanocomposite |
| Actuation principle | Electromagnetic | Electromagnetic | Photomechanical |
| Maximum deformation | 4 mm | 5.5 mm | 0.35 mm |
| Relative max. deformation | 4/7.07 ≈ 0.565 | 5.5/18 ≈ 0.3 | 0.35/0.42 ≈ 0.825 |
| **Morphing period** | **30 ms** | **10 ms** | **500 ms** |

**Cross-check against the primary sources held in this corpus** (see `audits/citation_audit.md` for the full audit):
- **Ni et al. [38] = NI-22.** The 30 ms entry corresponds to NI-22's measured **isolated-ribbon** response (≈30 ms). NI-22's measured **full-surface** development time from flat is ≈**300 ms**, and shape-to-shape switching ≈650 ms. Labelling 30 ms the surface "morphing period" is an element-level → surface-level substitution of one order of magnitude.
- **Bai et al. [39] = BAI-22.** The geometric entries trace correctly (18 mm sample; u/L ≈ 30 % ⇒ ≈5.4 mm). The **10 ms morphing period does not correspond to any value in BAI-22's complete published package** — main text, Extended Data, 71-page supplementary information and peer-review file, all retrieved and searched on 17 August 2026. That package reports element response **< 0.07 s** (measured with a 60 fps camera, i.e. a frame period coarser than 10 ms), system morphing **within 0.1 s**, a function-evaluation cycle of **0.35 ± 0.15 s**, and closed-loop convergence of **≈2.5 min**. Searches for "10 ms", "0.01 s", "sub-element", "filament", "transient" and "rise time" return no occurrence. The year is also given as 2021; BAI-22 is *Nature* 2022. **Still recorded as a discrepancy requiring verification, not an error** — see `audits/citation_audit.md` CA-02.
- **Niu et al. [40]** is **not in this corpus** → `[FULL TEXT MISSING — VERIFY BEFORE CLAIM]`; no statement is made about it.
**Caveat updated 17 August 2026.** The earlier caveat here recorded that BAI-22's Extended Data and Supplementary Notes were not held and could conceivably contain a 10 ms sub-element figure. **That caveat is discharged: the complete package was retrieved and searched, and contains no such figure.** The audit's verdict is nevertheless **unchanged** — it remains a **discrepancy requiring verification, not a proven error** — because the reason has shifted rather than disappeared: we can now observe that the cited paper does not report the value, but we still cannot observe how the citing authors obtained it. The forward citation search (`absence_claims.md` §4, item 2) would quantify how widely the value has propagated and may surface further independent uses of it; it does **not** necessarily recover the derivation, which may not exist in any published record. The verdict should be expected to stand at "discrepancy requiring verification" regardless of its outcome.

### S9 — 17 Aug 2026 · Objective O5
**String:** `review survey "movable antenna" OR "fluid antenna" hardware prototype measurement latency reporting gap 2026`
**Notable hits:** arXiv:2605.06275 (*Fluid Antenna Systems Enabling 6G HRLLC With Port Switching Delay*); arXiv:2511.05048; `10.3390/electronics14071458` (*Designs and Challenges in Fluid Antenna System Hardware*); Frontiers 2026 E-FAS experimental demonstration.
**Finding:** the adjacent fluid-antenna field **has already begun** delay-aware modelling that explicitly rejects "idealized instantaneous switching assumptions". This is a **precedent, not a competitor**: it is FAS port switching, not FIM mechanical morphing. It must be cited so the manuscript does not present delay-aware modelling as a novel idea.

### S10 — 17 Aug 2026 · Objective O1 (final check)
**String:** `"flexible intelligent metasurfaces" tutorial survey overview 2026 An Debbah Yuen`
**Finding:** returns only primary FIM research articles plus the broad *Emerging Technologies in Intelligent Metasurfaces* piece (IEEE TAP, 2025) which is not a FIM hardware-validation review. **No FIM-specific survey found.**
**Bibliographic by-product:** An et al., *"Flexible intelligent metasurfaces for downlink multiuser MISO communications," IEEE Trans. Wireless Commun.*, **24**(4), 2940–2955, 2025 — probable journal version of ANJ-25. `[VERIFY]`

---


### S11 — 18 Aug 2026 · Objective O4 (**forward citation search — U3**) ★★ key result

**This is the forward citation search recorded as blocker U3.** It is reproducible; the tooling and queries are given so a second reader can repeat it.

**Databases and interfaces.** OpenAlex REST API (`api.openalex.org`, citation graph, primary tool); Crossref REST API (publication metadata); arXiv API and PDF endpoint (author-version full texts); Semantic Scholar Graph API (open-access PDF resolution). Google Scholar and Scopus were **not** used — no institutional access; this is a limitation, since Scopus and Scholar index citing works OpenAlex may miss.

**Seed set (cited works).**

| Key | DOI | OpenAlex ID | Citing works |
|---|---|---|---|
| BAI-22 | `10.1038/s41586-022-05061-w` | `W4296552404` | 160 |
| NI-22 | `10.1038/s41467-022-31092-y` | `W4297022396` | 102 |
| LI-25 | `10.1038/s41467-025-58249-9` | `W4409148742` | 44 |

**Query.** `GET /works?filter=cites:{ID}&per-page=200&cursor=*`, paginated to exhaustion, for each seed.

**Screening.** 306 citing records → **262 unique works** (deduplicated by OpenAlex ID). Title+abstract screened with a wireless/communications regular expression (`reconfigurable intelligent surface|metasurface|MIMO|beamforming|ISAC|channel estimation|movable antenna|…`) → **64 wireless-relevant works** → manual exclusion of optics/photonics/materials-only papers → **20 distinct flexible-metasurface or reconfigurable-surface *system* papers**.

**Full-text retrieval.** 13 of 20 obtained (arXiv author versions, plus one institutional-repository copy of an IEEE journal article). **7 could not be retrieved** — IEEE Xplore paywall, no open-access deposit found via Semantic Scholar: the *TAP* review "Emerging Technologies in Intelligent Metasurfaces", Ming *et al.* (beam squint, *TVT* 2025), Zarini *et al.* (PIMRC 2025), Teng *et al.* (ICC 2026), Jiang *et al.* (ICC 2026), Hu *et al.* (GLOBECOM 2025, an earlier version of a paper we did obtain), and Acta Physica Sinica (conformal RIS near-field modelling).

**Extraction.** Each retrieved full text was scanned for `morphing period|morphing time|switching speed|response time|millisecond|<digits> ms|0.0x s`, with ligature normalisation and hyphenated-linebreak repair. Every hit was read in context. **An abstract-level scan of all 64 wireless-relevant works returned zero timing mentions** — propagation occurs only in body text, which is why full-text access bounds this search.

**Result: four instances, zero author-disjoint groups.** See `evidence_matrix.md` **E-FP-01 … E-FP-04** for the cases and **E-FP-C1** for the counterexamples. Independence was tested by author-set intersection against the corpus FIM lineage (An, Yuen, Yang, Di Renzo): **17 of the 20 candidate system papers share at least one author with it**, and all four propagation instances contain An and/or Yuen.

**What this search did not find.** No traceable derivation of the tabulated 10 ms value anywhere in the citing literature. No paper reproducing LI-25's 16.76 ms figure at all. No author-disjoint group reproducing any substitution.

## 4. Sources identified externally — status table

| Source | Relevance | Status |
|---|---|---|
| arXiv:2606.06845 · Hu et al., multicell FIM | **critical** — source of the audited Table I feasibility claim | ✅ **full text retrieved and read 18 Aug 2026 (S11)**; Table I and both escalations verified verbatim (E-FP-01, E-FP-02) |
| arXiv:2502.16478 · An et al., FIM MIMO (IEEE TCOM) | **critical** — Remark 4 coherence-block assumption | ✅ **full text retrieved and read 18 Aug 2026 (S11)**; attaches **no** timing figure — recorded as counterexample E-FP-C2 |
| arXiv:2510.07466 · Hu et al., FIM radio environments | high — unattributed "order of milliseconds" claim | HTML inspected |
| arXiv:2512.23045 · Kumar et al., statistical-CSI FIM | **critical for novelty boundary** | ✅ **full text retrieved and read 18 Aug 2026 (S11)**; no author overlap with the FIM lineage and **no timing claim** — counterexample (E-FP-C1) |
| arXiv:2601.15471 · large FIM, statistical CSI | high (novelty boundary) | title only |
| arXiv:2508.00268 · FIM channel estimation, neural operators | **critical** — millisecond shape-switching assertion | ✅ **full text retrieved and read 18 Aug 2026 (S11)** → E-FP-03 |
| arXiv:2605.29227 · FIM MIMO channel estimation | medium | title only |
| arXiv:2506.23052 · FIM multi-target sensing | medium | ✅ **full text retrieved and read 18 Aug 2026 (S11)**; no timing claim — counterexample (E-FP-C1) |
| arXiv:2511.00878 · stacked FIM | low | title only |
| arXiv:2510.24190 · flexible intelligent layered metasurfaces | low | title only |
| Niu et al. 2022 (photomechanical, cited as [40] in S8) | medium — third hardware platform cited by FIM theory | **not located** |
| arXiv:2605.06275 · FAS port-switching delay | medium — precedent for delay-aware modelling | title/abstract |
| `10.3390/electronics14071458` · FAS hardware challenges | medium | title only |

---

## 5. What would be needed to upgrade this to a systematic search

1. IEEE Xplore, Scopus and Web of Science queries with recorded strings, filters, dates and hit counts.
2. A pre-specified protocol with inclusion/exclusion criteria fixed before screening.
3. Backward chasing of the reference lists of RAN-25, ANJ-25, YAN-25, MA-26 and arXiv:2606.06845.
4. ~~Forward chasing (cited-by) of BAI-22, NI-22 and LI-25.~~ ✅ **Done 18 Aug 2026 — see S11.** What remains outstanding within it is **full-text access**, not citation retrieval: 7 of the 20 identified system papers are paywalled and were not read, so the propagation count is a **lower bound**. Repeating S11 with institutional access to IEEE Xplore is now the highest-value remaining step. The original note read: *this would establish how widely the mis-transcribed morphing figures have propagated and would convert a two-paper observation into a quantified citation-propagation result.
5. A second screener.
6. PRISMA-style flow counts.

Item 4 is the single action most likely to raise this manuscript from "structured critical review" to a defensible "systematic mapping of citation practice".

# Citation Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.1 · 18 August 2026 · adversarial self-review of the draft manuscript (freeze consistency gate; see `CHANGELOG.md` v1.5)

Two things are audited here: (i) whether the manuscript's own citations faithfully represent their sources, and (ii) the traceability finding the manuscript makes about *other* papers' citations, which must be held to a higher standard than anything else in the draft because it is a claim about others' accuracy.

---

## Part 1 — Findings about the reviewed literature

### CA-01 · Element-level response reported as a surface morphing period — **CONFIRMED against primary source**

**Claim in manuscript §6.5.** An external FIM system paper's Table I lists a "Morphing Period" of 30 ms for the liquid-metal platform. That value corresponds to the primary source's *isolated-ribbon* response, not its surface response.

**Verification.** The primary source states, in a single passage: the isolated ribbon reaches stable deformation in ≈30 ms measured (≈50 ms by finite-element analysis); the "experimentally measured total response time for developing a full shape starting from a flat configuration is ~300 ms, dominated by the viscoelastic response of the membrane (~250 ms for the membrane to reach maximum deformation)"; and shape-to-shape switching is ≈300 + ≈50 + ≈300 ms. All three appear on pp. 3–4 of the same paper.

**Verdict: confirmed.** The 30 ms figure is real and correctly attributed to the right paper; it is the wrong quantity for the label "Morphing Period" of a surface, by a factor of ten, and the correct figure appears in the same source within two paragraphs of it.

**Manuscript wording check:** §6.5 says "an element-level figure is presented as a surface morphing period, a substitution of one order of magnitude." ✅ Accurate. Does not allege intent. Passes.

### CA-02 · A tabulated 10 ms with no main-text counterpart — **DISCREPANCY, NOT CONFIRMED AS ERROR**

**Claim in manuscript §6.5.** The same Table I lists a 10 ms "Morphing Period" for the filamentary mechanical platform; that value does not correspond to anything in the primary source's main text.

**Verification against the COMPLETE primary source package.** *(Updated 17 August 2026 — the blocking limitation recorded in v1.0 has been removed. The supplementary package was retrieved from the publisher and is now archived in the corpus as `19S_Bai_Shape_Morphing_Supplementary_Information.pdf` (71 pp.) and `19SB_Bai_Shape_Morphing_Peer_Review_File.pdf` (28 pp.). The main-text PDF already held includes the Extended Data figures.)*

Timing quantities reported anywhere in the package:
- abstract: "dynamic morphing capabilities with response times within 0.1 second"
- p. 2: "response time less than 0.07 s" for the serpentine beam
- p. 4: feedback control cycle "around 0.25 s"; optimisation "takes 5–15 iterations"
- Extended Data Fig. 4: convergence "in 170–510 function evaluations (5-15 iterations)"
- SI Note S5.3: single beam "reaches a steady state within 0.07 s", monitored by a **60 fps** side camera
- SI Note S6: "the time expenditure for each loss function evaluation cycle is ~0.35 s"; **"a 4×4 sample takes an average of ~2.5 min to morph a shape from the zero-actuation initial state"**
- SI Table 1: function-evaluation budget, sum 0.35 ± 0.15 s
- SI Video legends: actuation voltages "updated at a rate of 10 fps"

Full-package search results (ligature-normalised, 71 pp. SI + main text + Extended Data):

| Term | Occurrences |
|---|---|
| "10 ms" | **0** |
| "ms" as a unit, anywhere in the SI | **0** |
| "0.01 s" | 1 — and it is the ± dispersion on `0.06±0.01 s`, not an interval |
| "sub-element" | **0** |
| "filament" | **0** |
| "transient" | **0** |
| "rise time" | **0** |

**Corroborating that the table entry does derive from this paper:** the tabulated aperture (18 mm) matches the reported sample size L = W = 18.0 mm exactly, and the tabulated maximum deformation (5.5 mm, ratio ≈0.3) matches the reported u/L ≈ 30 %. The publication year is given as 2021; the paper is 2022.

**An additional instrumentation observation.** The fastest mechanical quantity in the paper (< 0.07 s) was obtained with a 60 fps camera, i.e. a frame period of ≈16.7 ms. That apparatus could not have resolved a 10 ms interval.

**Verdict: still a discrepancy requiring verification — NOT an error.** The evidential basis is now much stronger: the complete published package contains no value at or near 10 ms, and the instrument used could not have produced one. But the audit's own standard forbids the upgrade. We can observe the tabulating authors' table; we cannot observe their derivation. A tabulated value may have been inferred, unit-converted, or drawn from a source we have not identified, and asserting an error would require ruling those out. **The manuscript must continue to call this a discrepancy.**

**Manuscript wording check:** §6.5 now says the value "does not correspond to any value in that paper's **complete primary source package**", lists the reported values, gives the search results and the 60 fps observation, and states explicitly: "Obtaining the complete package establishes that no such value is reported; it does not establish how the tabulating authors arrived at theirs." §9.4 agrees. ✅ Passes. **Blocking pre-submission action discharged.**

### CA-03 · An uncited feasibility assertion — **CONFIRMED as reported, but second-hand**

A further FIM paper asserts that "the deformation response time (i.e., reconfigurability rate) of the FIM is on the order of milliseconds, which is comparable to the coherence time of the channel under typical mobile conditions", reportedly in a footnote with no bibliographic citation attached.

**Limitation.** We inspected this through an online full-text retrieval, not the archived PDF, and the "no citation attached" observation is second-hand from that retrieval.

**Verdict.** The manuscript's §6.5 footnote 3 says the statement "is reported to appear in an explanatory footnote with no bibliographic citation attached." ✅ The hedge is present and correct. **Recommended strengthening:** verify against the archived PDF before submission, or delete the "no citation" observation, which is not load-bearing.

### CA-04 · The shape-reuse footnote — **CONFIRMED verbatim**

Verified word for word from p. 8 of the held preprint, including that it is footnote 8 and that the surrounding text supplies no bound, no duration and no sensitivity analysis. The paper's own simulations optimise per realisation. ✅ Passes. **Re-verified 17 Aug 2026 against the version of record: the same sentence appears verbatim as footnote 10 on p. 13327, and the surrounding text still supplies no bound.** Cite the version-of-record locator.

### CA-05 · The movement-perturbation footnote — **CONFIRMED verbatim, with a note**

Verified from p. 3 of the corpus PDF. The source spells "negligible" as "neglegible"; the manuscript does not quote this footnote verbatim in the body and so does not need `[sic]`, but the evidence matrix records the spelling so that future term searches do not silently fail. This is not a trivial point: **a naive search for "negligible" in that document returns zero hits.**

---

## Part 2 — Audit of the manuscript's own citations

Every quantitative statement in the draft was re-checked against extracted source text. Findings:

| # | Manuscript statement | Verdict |
|---|---|---|
| 1 | 3 dB at one-wavelength morphing range = 10.8 mm at 28 GHz, stated by the source | ✅ verified — p. 6 conclusion states the mm figure; **this corrects the prior project record, which classified it as our derivation** |
| 2 | ≈2.5 dB and a further ≈2 dB | ✅ verified preprint p. 8 · ✅ **re-verified 18 Aug 2026 against the version of record, p. 13328** |
| 3 | 125 % EM-only over PBF-only | ‼ **verified in the preprint abstract, but REMOVED from the version of record (18 Aug 2026).** No percentage figure appears anywhere in the published technical text. **Withdrawn from the manuscript**, which now carries only the version of record's qualitative statement (p. 6823). See `evidence_matrix.md` E-13, reclassified *superseded-by-version-of-record*. |
| 4 | 28 GHz, 208 m/s, ±λ, N_T = N_R = 4 | ✅ verified Table II (preprint) · ✅ **re-verified 17 Aug 2026 against the version of record, Table III, p. 13327** |
| 5 | Doppler ≈19.4 kHz | ✅ arithmetic re-checked (208 × 28×10⁹ / 3×10⁸ = 1.94×10⁴); **labelled derived in three places** |
| 6 | 51 symbols at >0.5 correlation, 90 mph, 2.6 GHz | ✅ verified draft p. 4 verbatim · ✅ **re-verified 17 Aug 2026 against the version of record, p. 721** |
| 7 | 20 symbols @ 0.95, 40 @ 0.82 | ✅ verified Fig. 4b legend (draft) · ✅ **re-verified 17 Aug 2026 against the version of record, Fig. 4(b), p. 728** |
| 8 | ≈0.51 ms conversion | ✅ **removed from the manuscript 17 Aug 2026.** Two corrections: the source *does* state the symbol rate (f_s = 100 kHz, VoR p. 721), so the earlier "conditional" framing was wrong; and the figure is deleted anyway because the 51-symbol count carries the argument. Retained in `evidence_matrix.md` E-DR-02 only. |
| 9 | 16.76 ms; components 4 / 2 / 5.25 ms; 11.25 ms sum; ≈5.5 ms RS-232 | ✅ all verified p. 4 verbatim; 11.25 ms confirmed as a figure annotation |
| 10 | 480 × 240 mm, 32 × 16, 15 mm period, 0–30 V | ✅ verified p. 3 and Methods |
| 11 | **3.0–3.4 GHz band; up to 270° phase over 0°–45° AOI** | ✅ **verified verbatim p. 4** — see methodological note below |
| 12 | RMSD as low as 2.36 mm at 45 mm | ✅ verified p. 4 verbatim |
| 13 | Bending stiffness reduced by >2 orders of magnitude | ✅ verified p. 3 verbatim |
| 14 | EVM ≈ −20 dB video link under dynamic deformation | ✅ verified p. 6; **detail added in revision: streaming at 3.1 GHz, receiver at 0° or 30°, 2 m, QPSK, on an aerofoil model** |
| 15 | τ_on ≈ 15 ms, τ_off = 72 ms, 10 %/90 %, 4.6 μm, 12 × 10, 62 GHz, 6.8 GHz (10.9 %) | ✅ all verified pp. 1, 5–7; the 10 %/90 % criterion is read from the Fig. 4 panel labels |
| 16 | Reflectarray LC comparator: "few seconds" / "10s of seconds" | ✅ verified p. 7 verbatim |
| 17 | <2 ms projection at 1 μm | ✅ verified p. 7; **labelled projected, not measured, in both §5.2 and the evidence matrix** |
| 18 | <0.1 ms per element; <10 ms per tile; ×¼ multiplexing | ✅ verified abstract, pp. 6, 8, 9 verbatim |
| 19 | 8.25 / 13 / 11.25–11.60 W | ✅ verified p. 9 verbatim |
| 20 | 18.0 mm sample, u/L ≈ 30 %, I < 27.5 mA, B = 224 ± 16 mT, <0.07 s, within 0.1 s | ✅ all verified p. 2 and abstract |
| 21 | ≈0.25 s feedback cycle, 5–15 iterations | ✅ verified p. 4 verbatim — **but the derived 1.25–3.75 s product was WRONG and is retracted; see C5.** Replaced by the source's own ≈2.5 min (SI Note S6) |
| 21a | 0.35 ± 0.15 s function evaluation; 4(N+M)+2 evaluations per iteration; 170–510 evaluations; ≈2.5 min convergence; 10 fps open-loop replay; 60 fps measurement camera | ✅ all verified verbatim against SI Notes S5.3/S6, SI Table 1, Extended Data Fig. 4 and the SI video legends |
| 21b | LI-25 SI: T1 = 4 ms thread-timing average; T2 ≈ 2 ms; T3 = 5.25 ms oscilloscope; 11.25 ms sum; 32 channels at 115 200 bps → 16.76 ms; 60 Hz deformation limit; < 10 ms projection; **16.7 ms trigger → stabilised RF** via AD8317 log detector at 3.1 GHz over −10 to −60 dBm | ✅ all verified verbatim against SI Note 6 and SI Figs. 12–13 |
| 22 | ≈30 ms ribbon, ≈50 ms FEA, ≈300 ms surface, ≈250 ms membrane, ≈650 ms switching, ≈50 ms script | ✅ all verified pp. 3–4 verbatim |
| 23 | 256 elements, 30 × 30 cm, ≈0.1 g cm⁻², bend radii <23 cm, ≈80 mW at ≈1 m, ±10° and 1.6 m range-limited | ✅ all verified abstract and p. 6 |
| 24 | 10 × 10, 9 GHz, PIN, ±45°, 16.13 dBi, acrylic supports at different bending degrees | ✅ verified abstract and p. 2265 verbatim |
| 25 | 15 × 15 liquid metal on PDMS, 10 GHz, 1-bit, 17.9 dBi, ±25 % bending | ✅ verified from rendered abstract page |
| 26 | 0°–50°, ±2°, 9.3–10.5 GHz, 2-bit, 3D-printed curved substrate | ✅ verified from rendered abstract page |
| 27 | ≈195° phase, ±60° coverage | ✅ verified abstract |
| 28 | Ma: mechanical slower than electronic; instantaneous vs statistical CSI; hierarchical control | ✅ verified pp. 3, 20, 26–27 verbatim |
| 29 | Saifullah: >kHz electrical, <1 kHz LC, ms microfluidic, stretchable slow/environment-sensitive/no per-element control | ✅ verified p. 26 verbatim |
| 30 | Three reviews contain zero occurrences of "FIM"/"flexible intelligent metasurface" | ✅ verified by ligature-normalised full-text search; **method stated in a footnote in §1.3** |
| 31 | Yang running time 4 ms – ≈100 ms, benchmark ≈1.2 s, "Running time [Second]" | ✅ verified by reading the rendered figure page; **axis units confirmed, not assumed** |
| 32 | Yang: element moves once per subframe, phase once per time slot | ✅ verified pp. 7–8 verbatim |
| 33 | An: quasi-static flat fading; perfect CSI | ✅ verified pp. 2–3 verbatim |
| 34 | λ/20 ≈ 0.5 mm at 28 GHz | ✅ arithmetic re-checked (10.7/20 = 0.535); **labelled as our illustration, not a source value** |

**No unverified quantitative claim survives in the draft.**

---

## Part 3 — Corrections applied and near-misses

**C1 — corrected.** The prior project record classified "one wavelength = 10.8 mm at 28 GHz" as a derived quantity. It is stated by the source. Reclassified as direct.

**C2 — corrected.** The prior project record stated that the multiuser FIM optimisation "converges after about 10 iterations". The source caps iterations at 100 with a −30 dB fractional-decrease criterion and plots convergence traces over 0–50 iterations; the ≈10-iteration figure belongs to a *different* paper (the bistatic short paper's projected-gradient method). The draft does not repeat the error.

**C3 — near-miss, methodologically important.** In verifying item 11, the figures' axis tick labels in the extracted text include the tokens "3.0", "3.4" and "270", which could easily be mistaken for the reported values. They are tick marks. The claim happens to be independently true — the body text on p. 4 states the band and the 270° range verbatim — but the coincidence is a warning. **Rule adopted:** no numerical claim may rest on a token appearing only in an extracted figure region; body text or a rendered figure must confirm it. Item 31 was resolved by rendering the page for exactly this reason.

**C4 — added.** The same source states that normalised reflection amplitude "remains above 0.4 with all combinations of bias voltage and AOI". This is a material efficiency caveat on the corpus's strongest flexible RF platform and belongs in the evidence matrix. *(Action: add as E-23a.)*

**C5 ‼ — RETRACTION OF ONE OF OUR OWN DERIVED VALUES.** *(17 August 2026, following retrieval of the BAI-22 supplementary information.)*

The draft derived a closed-loop convergence time of ≈1.25–3.75 s by multiplying the main text's "around 0.25 s" feedback control cycle by its "5 to 15 iterations". **The derivation is invalid.** The supplement states that each optimiser iteration comprises 4(N + M) + 2 function evaluations — 34 for a 4 × 4 sample — so 5–15 iterations is 170–510 feedback cycles, not 5–15. Extended Data Fig. 4 confirms the 170–510 count, and SI Note S6 states the convergence time directly: **≈2.5 min**, roughly forty times our figure.

Three things follow, and the third is the reason this entry is written at length rather than silently fixed.

1. **All instances are corrected.** §4.6, §5.3, §6.2, the evidence matrix (E-33, E-DR-03 retracted, T-BA-03/04/05 added), `timescale_matrix.md`, `evidence_strength_matrix.md`, `architecture_taxonomy.md`, `absence_claims.md` A7, `novelty_boundary.md` N3, `literature_search_log.md` and `manuscript_argument_map.md`.
2. **A guard was added.** `evidence_matrix.md` Part C now prohibits multiplying T-BA-03 by an iteration count, and T-BA-04 exists solely to record that an iteration is not a cycle.
3. **The error is the same species as the one the manuscript documents in others.** Two differently-defined quantities shared an informal name ("cycle" / "iteration"), and the substitution produced a figure off by more than an order of magnitude. It was committed by this review, on a source held in full, by an author who had already written the section warning against it. §9.4 and §6.2 report it in the manuscript rather than burying it here. **A reviewer is entitled to weigh this against the manuscript's central claim; we would rather they weigh it with the correction visible than discover it themselves.**

---

## Part 4 — Residual citation risks

| Risk | Severity | Status |
|---|---|---|
| ~~Two supplementary documents unavailable~~ | ~~High~~ → **discharged** | Both retrieved and read 17 Aug 2026 and archived in the corpus. CA-02 is no longer blocked. |
| This review committed a substitution error of the class it documents (C5) | **Medium** | retracted, corrected everywhere, guarded in `evidence_matrix.md` Part C, and **disclosed in the manuscript body** (§6.2, §9.4) rather than only here |
| No source reports repetitions or uncertainty on its headline timing values | **Medium** | recorded as absence claim A15 and `latency_definition_audit.md` F4; stated in §9.4; added as a reporting-framework field |
| Three external sources cited from online full text rather than archived PDFs | **Medium** | flagged with footnotes in §4.5, §6.5; each is marked as located through the external search |
| Three corpus sources readable only as page images | Medium | disclosed in §9.4; only metadata and abstract-level claims drawn from them |
| arXiv versions not cross-checked against journal versions | Medium | disclosed in §9.4 and the source inventory |
| The traceability finding rests on two table rows | ~~Medium~~ → **Low-Medium** | ✅ **forward citation search completed 18 Aug 2026 (S11).** The finding now rests on four documented instances (E-FP-01…E-FP-05), including two escalations — a "1 ms" figure present in no primary source, and a millisecond assertion added between an author's own conference and journal versions. Residual risk is unchanged in kind: **no author-disjoint group reproduces the practice**, so the finding remains about one collaboration network, and 7 paywalled papers were not read |

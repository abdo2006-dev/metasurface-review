# Absence-Claim Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

> ✅ **v1.8 sweep, 18 August 2026.** Every unbounded absence and priority construction in the *active manuscript*, the figure-generation script, all captions and tables was located by literal sweep and bounded (`CHANGELOG.md` CH-108). Figure 3's two `NOT MEASURED ANYWHERE` boxes now read **`NO MEASUREMENT FOUND IN REVIEWED SET`**. Two further rules were adopted in this pass:
> - **The stage-count verb is `times`, never `measures`** — the count is a timing count; under a quantitative reading the maximum is six, not five (CH-100).
> - **No source that has not been read in full may support a statement about what that source does not contain.** One such claim was found and withdrawn (CH-105).

**Version:** 1.0 · 17 August 2026
**Rule:** an absence claim is only as strong as the search that supports it. This project has a corpus and a documented but non-systematic search (`literature_search_log.md` §1). Therefore **no unqualified absence claim is licensed**, with two narrow exceptions noted in §3.

---

## 1. Register of planned absence statements

| # | Draft statement | Supported by | Verdict | **Approved wording** |
|---|---|---|---|---|
| A1 | "No hardware validation exists for FIM adaptation timescales." | corpus audit E-AA-01 | ✗ **reject** — asserts a fact about the world | **"Within the studies reviewed here, no measurement was found of the time required for an RF metasurface aperture to be commanded into a new shape and to return to trustworthy electromagnetic operation."** |
| A2 | "No prior review maps the FIM adaptation chain." | corpus review audit + S1/S10 | ✗ reject as stated | **"None of the reviews in the reviewed set — nor any review located in the searches recorded in our search log — decomposes FIM adaptation into stages and records the evidence level attained at each."** |
| A3 | "FIM surveys do not exist." | S1, S10 | ✗ reject | **"Our searches did not locate a review or survey dedicated to flexible intelligent metasurfaces; the FIM literature we found is uniformly primary system-level modelling work. Because our search was not protocol-driven, this should be read as a search outcome rather than as an established absence."** |
| A4 | "The closest reviews do not discuss FIMs." | E-44, E-47 — ligature-normalised full-text searches returning **zero** occurrences of "FIM" and "flexible intelligent metasurface" in MA-26, TIS-25 and SAI-22 | ✓ **accept** — this is a verifiable property of three specific documents, not a claim about the field | **"Ma et al., Tishchenko et al. and Saifullah et al. do not mention flexible intelligent metasurfaces; a full-text search of each returns no occurrence of the term."** *(state the method in a footnote)* |
| A5 | "Mechanical settling of an RF aperture has never been measured." | T-GAP-02 | ✗ reject | **"No source in the reviewed set reports mechanical settling for an aperture carrying meta-atoms, a bias network and an RF ground plane; the available settling data (≈250 ms of viscoelastic membrane relaxation) are for a bare elastomer surface with no RF layer."** |
| A6 | "Calibration time after deformation is never reported." | E-38, T-GAP-01 | ✗ reject as universal; ✓ accept as source-specific | **"Gal-Katziri et al. demonstrate closed-loop recalibration of a deformed 256-element flexible array but do not report how long it takes; we found no reported figure for this quantity in the reviewed set."** |
| A7 | "The 10 ms FIM morphing period is wrong." | E-ASM-03 vs E-32/E-33, T-BA-01…07 | ✗ **still reject** — the complete package is now held, but the *tabulating authors' derivation* is not observable | **"The 10 ms figure attributed to Bai et al. does not correspond to any value in that paper's complete published package — main text, Extended Data, supplementary information and peer-review file — which reports an element response below 0.07 s, system morphing within 0.1 s, a function-evaluation cycle of 0.35 ± 0.15 s, and closed-loop convergence of approximately 2.5 minutes. A full-text search of that package returns no occurrence of 10 ms or 0.01 s, and the element response was measured with a 60 fps camera whose frame period is coarser than 10 ms. We report this as a discrepancy requiring verification rather than as an error, because establishing that a value is not reported is not the same as establishing how a citing author obtained it."** |
| A8 | "No FIM paper models actuation dynamics." | corpus audit of RAN-25, ANJ-25, YAN-25, MOR-26 | ✓ accept, scoped | **"None of the four FIM system papers reviewed here models actuator dynamics, settling or control-interface delay; geometry is treated as instantaneously selectable within a morphing range."** |
| A9 | "Nobody has combined a flexible RF aperture, controlled geometry and a high-mobility channel." | E-AA-02 | ✗ reject as universal | **"No demonstration in the reviewed set satisfies all three of: a measured RF aperture, geometry treated as a controlled variable, and a mobile channel."** |
| A10 | "Two-timescale FIM control has not been proposed." | — | ✗ **reject outright — the opposite is true** | **Do not write any version of this.** Statistical-CSI FIM optimisation is published (arXiv:2512.23045, arXiv:2601.15471) and a two-rate schedule is already in YAN-25 (E-12). Cite them affirmatively. |
| A11 | "This is the first review to distinguish latency definitions for FIMs." | — | ✗ reject | **"We are not aware of a prior review that records start and end events for every reported timing value in this literature."** (First-person epistemic form; no field-level claim.) |
| A12 | "Iteration counts have never been mistaken for latency." / "…are routinely mistaken for latency." | E-10, T-CH-01 | ✗ reject both — we observed no such misuse | Make no claim. Simply state that iteration counts are reported instead of durations and cannot be converted without an implementation. |
| A13 | "No corpus source reports actuation energy for a morphing RF aperture." | C17 | ✓ accept, scoped | **"Actuation energy is not reported for any morphing RF aperture in the reviewed set; the only measured power figures are electronic panel power for a rigid RIS (8.25–13 W for a 32 × 32 array)."** |
| A14 | ~~"Repeatability and fatigue over shape cycles are unreported."~~ | C18 | ✗ **NOW REJECTED — the supplementary retrievals falsified the previous wording** | **CORRECTED 17 Aug 2026.** The old wording ("neither reports a cycle count, hysteresis figure, or fatigue limit") is **false**. BAI-22 SI Note S5.4 reports a 1 000-cycle bidirectional test at 1 Hz with constant displacement amplitude u = 1.55 ± 0.02 mm at ±10 mA, and a further test at ±20 mA fully reversible over the first 500 cycles. LI-25 SI Note 4 reports 3 000 bending cycles of the strain-sensor array with negligible drift. **Approved replacement: "Mechanical cycling data exist for the actuator and sensor layers — 1 000 reversible actuation cycles on one mechanical platform, 3 000 bending cycles for the shape-sensing array on the flexible RF platform — but no reviewed source reports cycling, hysteresis or fatigue for a *radiating* aperture, nor any accompanying measurement of RF performance drift over cycles."** |
| A15 | "Timing values in this literature are reported without uncertainty." | T-LI-04, T-LI-06, T-BA-05, F4 | ✓ accept, scoped | **"Neither supplementary package reports a repetition count or dispersion for its headline timing value; of the intervals quoted in this review, only the per-step budget of one closed-loop platform carries a stated ± range."** |
| A16 | "RF stabilisation onset is never measured." | superseded by T-LI-06 | ✗ **reject — falsified** | **Do not write this.** One reviewed source measures 16.7 ms from trigger to stabilised RF output on a flexible aperture. **Approved wording: "The onset of stabilised radiation has been measured on a flexible aperture under electronic compensation with static geometry; we found no measurement of it following a commanded geometry change."** |

---

## 2. Standard qualifiers to use

Preferred, in decreasing strength:

1. *"Among the studies reviewed here…"* — for corpus-bounded statements.
2. *"Within the reviewed experimental literature…"* — for hardware-specific statements.
3. *"Our searches, recorded in [search log], did not locate…"* — when the external search is the basis.
4. *"We are not aware of…"* — first-person epistemic; weakest but always safe.
5. *"[Source] does not report X"* — **strongest available**, because it is a checkable property of a named document. Prefer this form whenever it will do the work.

Forbidden without a systematic search: *"no previous work has"*, *"remains unexplored"*, *"the literature lacks"*, *"this is the first"*, *"there is no…"*, *"has never been"*.

---

## 3. The two exceptions

Two classes of absence statement **are** fully licensed, because they are properties of specific documents rather than claims about a literature:

- **Document-level absence** (A4, A6, A8, A13, A14): "Paper P does not report quantity Q." Verified by full-text inspection. State the verification method for term-search-based claims.
- **Matrix-level absence** (A1, A5, A9): "Across the N sources in Table X, no row records Q." Verified by the extraction protocol. Always name N and name the table.

Every absence statement in the manuscript reduces to one of these two forms. No statement about the field as a whole is made anywhere.

---

## 4. Pre-submission requirement

Before submission, absence claims A1, A2, A3, A5, A7 and A9 **must be re-tested** against:
1. a protocol-driven database search (IEEE Xplore, Scopus, Web of Science) with recorded strings and counts;
2. ~~a forward citation search of BAI-22, NI-22 and LI-25.~~ ✅ **Completed 18 August 2026 (S11).** It found four propagation instances and **zero author-disjoint publication groups**, and it also found the opposite pattern — papers citing the same primaries with no timing value attached. What it did **not** resolve is the derivation of the 10 ms value, exactly as the caveat below anticipated. It remains bounded by full-text access: 7 of the 20 identified system studies are paywalled, so its counts are **lower bounds** and A1/A2/A3/A5/A7/A9 still require the protocol-driven database search in item 1.

> ⚠ **What the forward citation search can and cannot do (written 17 Aug 2026; borne out by S11 on 18 Aug 2026).** It may quantify propagation of the Ni and Bai timing values across the citing literature, and may surface further independent uses of them. It does **not** necessarily resolve the origin or derivation of the tabulated 10 ms value, which lies with the citing authors and may not be recoverable from any published record. A7's verdict must therefore not be treated as pending on that search alone.

**Item 3 — retrieval of the BAI-22 and LI-25 supplementary material — was completed on 17 August 2026 and is removed from this list.** Both packages were obtained, read and archived (`source_inventory.md` §2; `CHANGELOG.md` CH-18, CH-20). The retrieval had three effects on this register: it falsified A14, it added A15 and A16, and it placed A7's evidential basis on the *complete* published package rather than the main text alone.

**A7's verdict is unchanged by that retrieval and must remain unchanged.** The complete package contains no 10 ms figure, but this is still a **discrepancy requiring verification rather than a proven error**, because the citing authors' derivation cannot be observed from the cited paper. A7 is no longer blocked on a retrieval, and it must not be strengthened to an accusation of an incorrect citation. The forward citation search in item 2 would quantify how widely the value has propagated; it may or may not reveal the derivation, and **A7's verdict should be expected to remain "discrepancy requiring verification" even after that search is complete.**

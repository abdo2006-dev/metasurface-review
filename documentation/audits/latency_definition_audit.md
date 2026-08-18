# Latency-Definition Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026

Every timing value appearing in the draft manuscript is checked here for three properties: is the **object** named, is the **start event** named, is the **end event** named. A value failing any of the three is either repaired or removed.

---

## 1. Register check

| Value | Object named? | Start named? | End named? | Verdict |
|---|---|---|---|---|
| 16.76 ms | ✅ FISP system, flexible RM | ✅ shape acquisition | ✅ bias-voltage supply | pass — and the manuscript restates all three each time it is used (§1.2, §5.1, §6.3) |
| ≈4 ms | ✅ ANN input path | ✅ sensor data reception | ✅ input prepared | pass |
| ≈2 ms | ✅ 32-channel ANN | ✅ prepared input | ✅ coding output | pass |
| 5.25 ms | ✅ power-supply module | ✅ control output arrives | ✅ bias applied | pass |
| "negligibly short" | ✅ varactor | ✅ bias change | ✅ state change | pass as qualitative; **no number exists — the manuscript never numeric-ises it** |
| ≈5.5 ms RS-232 share | ✅ serial link | — | — | **residual, not an interval.** Manuscript calls it "attributed by the authors to the transmission-rate limitation of the RS-232 protocol" and never presents it as a measured interval. pass |
| τ_on ≈ 15 ms | ✅ 4.6 μm LC delay line | ✅ transition begins | ✅ 90 % threshold | pass — threshold stated |
| τ_off = 72 ms | ✅ same | ✅ relaxation begins | ✅ 10 % threshold | pass — threshold and **direction** stated |
| <2 ms | ✅ hypothetical 1 μm layer | — | — | **projection.** Flagged as projected in §5.2 and excluded from all comparisons. pass |
| "few seconds"/"tens of seconds" | ✅ reflectarray-type LC-RIS | — | — | comparator statement about other work; labelled as such. pass |
| <0.1 ms | ✅ **one element** | ✅ FPGA update command | ✅ element state updated | pass — the manuscript never states this without "per element" |
| <10 ms | ✅ **one 16 × 16 tile** | ✅ pattern command | ✅ tile pattern written | pass |
| ×¼ multiplexing penalty | ✅ control network | — | — | **relative rate, not a latency.** Never summed with anything. pass |
| <0.07 s | ✅ serpentine beam element | ✅ current applied | ⚠ "response time" — threshold not stated by source | **partial fail — source-side.** Manuscript reports it as the source states it and never uses it in a threshold-sensitive comparison. Recorded as a source deficiency motivating reporting-framework Group B. |
| "within 0.1 s" | ✅ 4 × 4 system | ⚠ implied | ⚠ threshold not stated | same as above |
| ≈0.25 s / 0.35 ± 0.15 s per cycle | ✅ closed feedback loop (= one function evaluation) | ✅ image capture | ✅ next actuation | pass |
| 5–15 iterations = 170–510 cycles | ✅ optimisation | ✅ start | ✅ loss below 0.005 f(V=0) | pass **after correction** — the previous entry treated an iteration as a cycle and licensed an invalid product; see C5 in `citation_audit.md` |
| ≈2.5 min convergence | ✅ 4 × 4 sample | ✅ zero-actuation initial state | ✅ stopping criterion met | pass — stated directly by the source, not derived |
| 10 fps replay rate | ✅ stored voltage sequences | — | — | **rate, not a latency.** Never summed or compared with T-BA-05. pass |
| **16.7 ms trigger → stabilised RF** | ✅ FISP system, flexible RM, **static geometry** | ✅ sensor trigger | ✅ stabilised RF output at receiver | pass — and the manuscript states the static-geometry condition at every use, because the interval contains no morphing |
| 60 Hz deformation limit | ✅ deformation input | — | — | **rate constraint** derived by the authors from 16.76 ms. Not used as a latency. pass |
| < 10 ms (LI-25) | ✅ hypothetical faster acquisition + protocol | — | — | **projection.** Flagged as projected; excluded from all comparisons. pass |
| ≈30 ms | ✅ **isolated ribbon** | ✅ current applied | ✅ stable deformation | pass — "isolated ribbon" appears every time |
| ≈300 ms | ✅ **full surface** | ✅ from flat | ✅ full shape developed | pass |
| ≈250 ms | ✅ membrane | ✅ — | ✅ maximum deformation | pass |
| ≈650 ms | ✅ full surface | ✅ first shape command | ✅ second shape developed | pass — decomposition shown |
| ≈50 ms | ✅ **script processing**, not mechanics | — | — | pass — manuscript states it is script processing |
| 4 ms–100 ms; ≈1.2 s | ✅ estimation algorithm, desktop CPU | ✅ algorithm start | ✅ convergence / 400-iteration cap | pass — platform and cap stated |
| 51 symbols | ✅ channel correlation | ✅ reference instant | ✅ correlation = 0.5 | pass — **threshold stated**, and the manuscript no longer converts the count to wall-clock time at all |
| 20 / 40 symbols | ✅ same | ✅ | ✅ 0.95 / 0.82 | pass |
| ≈0.51 ms | ✅ | ✅ | ✅ | **Removed from the manuscript 17 Aug 2026 (U5 resolved).** Two corrections: it was never a *conditional* derivation — XU-22 states f_s = 100 kHz explicitly (VoR p. 721, and the held draft p. 4) — and it is nonetheless deleted, because the 51-symbol figure carries the argument and a derived wall-clock number invites decontextualised quotation. Retained in `evidence_matrix.md` E-DR-02 as a derived value only. **No longer in §3.1.** |
| ≈19.4 kHz | ✅ Doppler shift | n/a | n/a | not a latency; labelled derived in three places. pass |
| 1 + M slots; Q × T₂ | ✅ protocol | — | — | **protocol units.** §3.4 states explicitly they are not converted. pass |
| ≈10 iterations; ≤100 iterations | ✅ optimisation | — | — | **iteration counts.** Never presented as durations. pass |

## 2. Aggregation check

Searched the draft for any pooled statistic across timing values: **none found.** No mean, median, range, "typical", "on the order of" applied across architectures, or single "FIM latency" figure appears.

**Revised 17 August 2026.** §6.2 previously asserted an ordinal three-level structure across two platforms with "roughly an order of magnitude" between levels, and called it the strongest replicated result. That has been withdrawn. It failed three ways: the step sizes are not uniform (BAI-22's element-to-surface step, < 0.07 s to within 0.1 s, is not an order of magnitude); the third level is demonstrated by one platform only, so nothing about it is replicated; and the closed-loop value itself was wrong (C5). §6.2 now asserts only that element response, full-surface morphing and verified closed-loop convergence are **distinct quantities that cannot be substituted**, keeps NI-22's order-of-magnitude element-to-surface step as a **source-specific example**, and states that the ordering is not independently replicated.

**The draft now performs no arithmetic product across timing values.** The previous 5–15 × 0.25 s product is retracted (C5); the convergence figure now used is stated directly by its source.

## 3. Cross-architecture comparison check

Every place where two values from different architectures appear in the same sentence was checked for an explicit non-commensurability statement:

- §6.3 compares 72 ms (A5 liquid crystal, 62 GHz), 16.76 ms (A3 varactor, 3.2 GHz) and ≈300 ms (A4 mechanical, no RF). **Rewritten 17 August 2026, and rewritten again on the same date.** The non-commensurability statement is retained and now made *precise* rather than absolute: the earlier blanket "may not be ordered, differenced, or interpolated" was self-contradictory, because the paragraph then immediately observed the numerical ordering. The rule now reads: these heterogeneous measurements **may be displayed on a common numerical axis to show that their reported ranges overlap, but must not be treated as like-for-like performance measurements, pooled statistically, or used to infer the bottleneck of an integrated architecture.** Observing that 72 ms > 16.76 ms, and that 72 ms is within about a factor of four of ≈300 ms, is compatible with that rule. The conclusion drawn is a *qualification* — architecture labels alone do not establish a universal latency ordering, and "fast electronics, slow mechanics" requires mechanism-, object- and architecture-specific qualification — rather than a claim that the heuristic has been empirically falsified. The section heading was changed from "The first simplification that fails" to "Why 'fast electronics, slow mechanics' requires qualification" for the same reason. **Two claims were deleted:** that a liquid-crystal FIM "would be limited by its material, not by its actuator", and that a varactor or PIN-diode FIM "would be limited by its actuator and its control network". Neither was supportable: the reviewed set contains no integrated LC FIM, no mechanically-morphing radiating aperture, and no platform on which an electronic tuning layer and a commanded mechanical layer were measured together. The paragraph now says so. ✅ **Pass; still the draft's highest-risk paragraph** and should be re-read by any reviewer first.
- §6.4 previously concluded that "the dominant cost is distributing commands across the aperture". **Weakened 17 August 2026** to "can be a major — and in some implementations potentially dominant — contributor", because LI-25's transport share is ≈5.5 ms of 16.76 ms, which is a large individual contribution but not a majority, and the two platforms do not agree closely enough to support a universal claim. The under-modelling point, which does not depend on the magnitude, is preserved. ✅ Pass.
- §1.2 lists six values as an illustration of incommensurability. The framing is explicitly that they are "six measurements of six quantities, on five architectures, with five different definitions of when the clock starts." ✅ Pass.
- §6.6's stage table places evidence from different architectures in adjacent rows, but each row names its architecture in the "Level" column. ✅ Pass.

## 4. Findings and required source-side improvements

**F1.** Two mechanical values (<0.07 s, within 0.1 s) lack a stated threshold in their source. This is a source deficiency, not a manuscript one, and it is one of the specific motivations for reporting-framework Group B. The manuscript does not use either value in a comparison where the threshold would matter.

**F2.** The ≈0.51 ms conditional conversion is the draft's most fragile number. It survives because it is conditional, stated once, and not used in any comparison. **Recommendation: consider deleting it.** The 51-symbol figure carries the argument alone, and the millisecond value invites exactly the kind of decontextualised quotation this review criticises. *(Decision deferred to supervisor; recorded in `unresolved_questions.md`.)*

**F3.** No timing value in the draft is presented without its object. This was the primary failure mode identified in the reviewed literature, and the draft does not reproduce it.

**F4 (new, 17 August 2026).** The supplementary retrievals resolved F1 in one direction and opened a new deficiency in another.

*Resolved:* the mechanical element figure now has a stated criterion — steady state is "no displacement deviation … in sequential frames" of a 60 fps recording — which is a threshold, if a coarse one. It also bounds the measurement: **the instrument cannot resolve intervals below ≈16.7 ms**, which is recorded as T-BA-07 and used in `citation_audit.md` CA-02.

*New deficiency:* **neither supplement reports repetitions, sample size or uncertainty for its headline timing value.** LI-25's 16.76 ms and 16.7 ms and BAI-22's ≈2.5 min are all single stated figures; only BAI-22's per-step budget carries dispersion (± values in SI Table 1). No timing value quoted in this manuscript can therefore be accompanied by an uncertainty, and §9.4 states this. This strengthens the case for reporting-framework Group B, which should now require a repetition count and a dispersion measure alongside every reported interval.

**F5 (new).** §6.6's stage table previously described simulated channel-acquisition evidence as having "adequate measured support", and labelled electronic updating "adequate" and liquid-crystal updating "inadequate" for high mobility. All three were removed. The first was internally inconsistent with the table's own "simulated" classification; the latter two amounted to a latency deadline, which the manuscript elsewhere refuses to define. The table now carries an explicit note that the fast-fading column records a consequence of a named assumption rather than a finding, and the prose states that no update deadline is defined anywhere in this review.

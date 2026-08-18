# Timescale Matrix

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.1 · 18 August 2026 (freeze consistency gate; see `CHANGELOG.md` v1.5)
**Organising principle: by process, not by paper.** Papers appear in several categories; values within a category may be compared ordinally, values across categories may not.

Full per-entry detail (start/end events, conditions, measured/simulated status) lives in `evidence_matrix.md` Part B. This document groups those entries and states what each group can and cannot support.

> **Version-of-record status (17 Aug 2026; amended 18 Aug 2026).** The published full texts of **RAN-25** (*IEEE TWC* **25**, 13319–13335, 2026), **YAN-25** (*IEEE TWC* **25**, 6823–6836, 2026) and **XU-22** (*IEEE TVT* **72**(1), 718–734, **2023**) have been obtained, archived (`01V_…`, `04V_…`, `07V_…`) and inspected. Every load-bearing **timing and parameter** quantity keyed to them survives; locators are now the version-of-record locators. ‼ **One non-timing claim did not survive:** YAN-25's preprint-abstract figure of a 125 % received-power gain for element movement over passive beamforming is **absent from the version of record** and has been withdrawn from the manuscript (see `evidence_matrix.md` E-13, `CHANGELOG.md` CH-66). The earlier preprint/draft copies are retained as **earlier versions within the same independence group**, never as separate sources. One material addition was found — RAN-25's new Remark, pp. 13321–13322 (E-03b, E-03c). Internal keys are unchanged; the bibliography must use the version-of-record years. See `unresolved_questions.md` U6.

---

## Category 1 — Channel and protocol timescales (the demand side)

| Quantity | Value | Conditions | Type | ID |
|---|---|---|---|---|
| Interval over which time correlation > 0.5 | **51 symbols** | 90 mph, 2.6 GHz, 100 kHz bandwidth | simulated | T-CH-02 |
| Illustrative coherence intervals | 20 symbols @ 0.95 corr.; 40 symbols @ 0.82 corr. | same scenario | simulated | T-CH-03 |
| *(Locators are now the version of record: XU-22 = IEEE TVT **72**(1), 718–734, Jan 2023. T-CH-02 p. 721; T-CH-03 Fig. 4(b), p. 728; T-CH-04 pp. 720, 722.)* | | | | |
| Pilot/estimation overhead | 1 + M time slots (M = 16) | ON/OFF RIS protocol | protocol | T-CH-04 |
| FIM protocol update rates | movement once per subframe; phase once per time slot | Q × T₂, T₂ = 9 in simulation | protocol | T-CH-05 |
| Maximum Doppler at the high-mobility FIM operating point | **≈19.4 kHz** | 28 GHz, 208 m/s | **derived** (E-DR-01) | — |
| Wall-clock reading of T-CH-02 | ≈0.51 ms | derived from the source-stated **f_s = 100 kHz** (XU-22 VoR p. 721); **not required by the manuscript argument and deleted from the manuscript** | **derived** (E-DR-02) | — |

**What this category supports.** Three statements, and only three.
1. Coherence time is a **threshold-dependent correlation statistic**, not an interval of constancy — T-CH-02 and T-CH-03 differ by a factor of two purely because the threshold moved from 0.95 to 0.5.
2. The FIM system literature's own high-mobility operating point implies a **maximum Doppler shift of ≈19.4 kHz** (28 GHz, 208 m/s; derived by us, E-DR-01 — the source does not state it).
3. Protocol overhead consumes part of whatever coherence budget applies, **before** any hardware acts.

**Corrected 17 August 2026 — statement 2 previously overreached.** It read: *"…i.e. a fast-variable timescale far below a millisecond."* That inference is not licensed, and three quantities must be kept apart:

| | What it is | Status here |
|---|---|---|
| **Doppler frequency** f_D ≈ 19.4 kHz | a frequency derived from carrier and velocity | derived; exact given the stated parameters |
| **Correlation / coherence interval** | a **threshold-dependent statistic** requiring a stated correlation model and criterion | **not held at 28 GHz.** The only quantified interval in the corpus (T-CH-02, 51 symbols) is a *different scenario*: XU-22 at 2.6 GHz, 90 mph, 100 kHz bandwidth |
| **Update deadline** | how often the hardware must act to keep performance within a stated tolerance | **defined nowhere in this review, by design.** The manuscript refuses to define one |

A Doppler frequency does not convert into a time budget without the middle row, and the middle row does not convert into the bottom row without a performance criterion. **Never write a sentence in which 19.4 kHz becomes, on its own, a deadline of tens of microseconds** — 1/f_D is a reciprocal, not a coherence time, and still less a requirement.

**What this category does not support.** Any single "the channel coherence time is X ms" figure; any universal latency threshold; any statement that a given hardware timescale is too slow, which would presuppose the deadline the review declines to define. The corpus contains no coherence figure at 28 GHz at all.

---

## Category 2 — Computation (wall-clock)

| Quantity | Value | Platform | Type | ID |
|---|---|---|---|---|
| FIM channel-estimation algorithm runtime | ≈4 ms (small virtual array) to ≈100 ms (324-element virtual array); slowest benchmark ≈1.2 s | 13th-Gen Intel i7-13650HX desktop CPU, 400-iteration cap | **measured** | T-YA-01 |
| ANN inference for 32 shape channels | ≈2 ms | embedded FISP implementation | **measured** | T-LI-02 |
| Shape-optimisation convergence | ≈10 iterations (MOR-26); ≤100 iterations (ANJ-25) | — | **iterations — not time** | T-CH-01 |

**Grouping note.** T-YA-01 and T-LI-02 are both wall-clock computation and may be compared *with an explicit processor caveat*. Their significance is opposite in sign: LI-25's 2 ms inference shows a small learned map is cheap; YAN-25's runtime shows that **the sparse-recovery channel estimation that makes FIM movement useful is itself the most expensive computation reported anywhere in the corpus**, and it scales with virtual array size — the very quantity that element movement increases.

**Prohibited.** T-CH-01 must never be reported alongside T-YA-01 or T-LI-02 as if commensurate. An iteration count is not a duration; ANJ-25 and MOR-26 supply no processor, no per-iteration cost and no implementation.

---

## Category 3 — Controller and interface

| Quantity | Value | Object | Type | ID |
|---|---|---|---|---|
| Per-element FPGA update | **< 0.1 ms** | one element of a rigid PIN RIS | measured/design | T-AK-01 |
| Tile configuration update | **< 10 ms** | a full 16 × 16 tile | measured/design | T-AK-02 |
| Bias-voltage supply module response | 5.25 ms | 32-channel supply on a flexible RM | measured | T-LI-03 |
| Multiplexing penalty | ×¼ of raw parallel rate | control-network architecture | design statement | T-AK-03 |
| Serial-interface transport | ≈5.5 ms of a 16.76 ms loop (RS-232) | FISP | derived from authors' attribution | E-DR-04 |

**What this category supports — and it is the most under-appreciated finding in the corpus.** T-AK-01 and T-AK-02 come from the same hardware and are **up to two orders of magnitude apart**, because they time **different objects at different scopes**: one element against a complete 16 × 16 tile.

⚠ **Narrowed 17 August 2026 — do not present T-AK-03 as the explanation of that interval.** Both AKR-26 figures are **upper bounds**, not measured means, so the ratio between them is itself an upper bound; and T-AK-03 is a stated ×¼ penalty on the effective update rate, which is a factor of four, not a factor of one hundred. The paper does **not** decompose the tile-level bound into transfer, latching and switching components, so no account of the full interval can be given from the published record, and this matrix must not supply one. Earlier wording — *"a factor of one hundred … for the same nominal operation … T-AK-03 and E-DR-04 explain why"* — asserted both a same-operation comparison (false: configuring 256 elements is not the operation of switching one) and a causal explanation (unsupported).

**What the pair does license, and it is enough:** an element-level update time **cannot be substituted** for a tile- or aperture-level configuration time, and array-scale command distribution introduces a real, **architecture-dependent** overhead — a stated ×¼ rate penalty here, and roughly a third of FISP's measured partial loop as RS-232 transport rather than physics (E-DR-04) on the other measured platform. Neither figure supports a claim that distribution *dominates*.

**The engineering consequence.** Distribution of commands across the aperture is a **major contributor** in both measured control chains in this corpus. It is **not** established as accounting for the whole element-to-tile interval on the tile-based platform — the ×¼ penalty is a factor of four against an interval of up to two orders of magnitude, and the paper supplies no decomposition — and it is **not** established as universally dominant: on the flexible platform it is ≈5.5 ms of a 16.76 ms loop — about a third, and less than the remaining stages combined. The claim to make is that the cost is **large and unmodelled**, not that it dominates. Element counts in the A1 literature (4 to 16) are far below the 32, 256 and 512 of the measured hardware; a cost that scales with channel count is invisible at the scale the theory simulates.

**Prohibited.** Reporting "the RIS updates in under 0.1 ms" without stating that the object is a single element.

---

## Category 4 — Electronic / material state transition

| Quantity | Value | Mechanism | Type | ID |
|---|---|---|---|---|
| LC switch-on τ_on | ≈15 ms (10 %/90 %) | 4.6 μm liquid crystal, 62 GHz | measured | T-NE-01 |
| LC switch-off τ_off | 72 ms (10 %/90 %) | same device | measured | T-NE-02 |
| Reflectarray-type LC comparator | τ_on "few seconds", τ_off "10s of seconds" | earlier LC architectures | review statement | T-NE-04 |
| Varactor switching | "negligibly short" | FISP meta-atoms | author statement, no number | T-LI-05 |
| Thinner-LC response | < 2 ms | t_LC = 1 μm | **projected, not fabricated** | T-NE-03 |
| Field-level ranking | electrical > kHz; LC < 1 kHz; microfluidic ms-scale; chemical < 0.1 Hz | mechanism classes | review synthesis | E-45 |

**What this supports — restated 17 August 2026, and deliberately weaker than the previous version.**

*On the span.* This entry previously claimed that electronic state change "spans four orders of magnitude". **That figure is withdrawn: it has no quantified lower endpoint.** LI-25 calls varactor switching "negligibly short" and supplies **no number** (T-LI-05), so it cannot anchor the bottom of a range. The quantified values run from **≈15 ms** (T-NE-01, thin LC) to **tens of seconds** (T-NE-04, earlier LC reflectarrays, itself a review statement rather than a measurement) — roughly three orders, and both endpoints are liquid crystal. The defensible statement is that **transition times differ greatly between and within tuning mechanisms**, and that the semiconductor endpoint is unquantified in this corpus. No numerical span may be asserted until a measured varactor or PIN transition time is held.

*On the comparison with mechanics.* The previous wording — *"'Electronic control is fast' is true only for semiconductor tuning; it is false for liquid crystal"* — asserts a universal speed ordering by architecture label, which is precisely what §6.3 of the manuscript now refuses to do. Replace it with the observation and nothing more:

> The **numerical ranges** reported for electronic/material transitions and for mechanical processes **overlap**. NEU-24's τ_off (72 ms) is larger than LI-25's entire measured electronic partial loop (16.76 ms) and lies within a factor of four of NI-22's full-surface mechanical morph (≈300 ms).

**This overlap is not a ranking**, and the three values sit in three different comparability classes (C-EM-STATE, C-PART-LOOP, C-MECH-SURF). The rule, stated precisely: **these heterogeneous measurements may be displayed on a common numerical axis to show that their reported ranges overlap, but they must not be treated as like-for-like performance measurements, pooled statistically, or used to infer the bottleneck of an integrated architecture.** Observing that 72 ms > 16.76 ms, and that 72 ms lies within roughly a factor of four of ≈300 ms, is compatible with that rule; ranking the three devices by speed is not. What the overlap establishes is negative: **an architecture label alone — "electronic", "mechanical" — does not determine which layer binds.** It does not establish that liquid crystal is slower than mechanics, that semiconductors are faster than mechanics, or anything about an integrated device.

**Prohibited in this category.** Inferring the bottleneck of an integrated FIM that has never been built or measured. No reviewed source contains an integrated LC mechanical FIM, or equivalent hardware, from which such a bottleneck could be established.

**Prohibited.** Using T-NE-03 as evidence of anything achieved. Reporting 15/72 ms without the direction and the 10 %/90 % criterion.

---

## Category 5 — Mechanical response, element level

| Quantity | Value | Object | Type | ID |
|---|---|---|---|---|
| Serpentine beam response | **< 0.07 s** | 3.60 mm beam in an 18 mm mechanical mesh, no RF layer | measured | T-BA-01 |
| Isolated liquid-metal ribbon | **≈30 ms** measured (FEA ≈50 ms) | single ribbon, no RF layer | measured + simulated | T-NI-01 |

Two independent platforms (IG-8, IG-9) both place element-level mechanical response on a bare mechanical substrate **in the tens-of-milliseconds decade**. Read this narrowly. T-BA-01 is an **upper bound** obtained from a 60 fps side camera, whose ≈16.7 ms frame period (T-BA-07) is the resolution floor; T-NI-01 is a point value for a different material under a different actuation mechanism. The agreement is that both fall in the same decade, not that they measure the same quantity to the same precision. **This is not a "replicated result" in the sense of a confirmed number**, and no section may promote it to one — see `evidence_matrix.md` Part C.

---

## Category 6 — Mechanical response, surface level

| Quantity | Value | Object | Type | ID |
|---|---|---|---|---|
| System morphing | "within 0.1 s" | 4 × 4 filamentary mesh | measured | T-BA-02 |
| Full surface from flat | **≈300 ms**, of which ≈250 ms is membrane viscoelasticity | liquid-metal/elastomer surface | measured | T-NI-02 |
| Shape-to-shape switching | ≈650 ms (300 + 50 script + 300) | same surface | measured | T-NI-03 |

**A within-platform observation, and only that.** Compare Categories 5 and 6 within each platform, never across them:
- BAI-22: element < 70 ms → system < 100 ms (factor ≈1.4)
- NI-22: ribbon ≈30 ms → surface ≈300 ms (factor ≈10)

The two platforms disagree about the *size* of the element→surface penalty, and agree only on its **sign**. That is the whole of the result: element and surface are distinct quantities, and within each platform the element value is the smaller. It does **not** extend to a three-level ordering including closed-loop convergence, which only BAI-22 measures. NI-22 also names the mechanism — viscoelastic membrane relaxation, ≈250 ms of the ≈300 ms — which is a materials property that an RF stack with a dielectric substrate, meta-atom metallisation and a serpentine ground plane would not obviously improve.

**This is the precise point at which the citation problem in the FIM system literature arises** (see `audits/citation_audit.md`): an external FIM paper tabulates a "Morphing Period" of 30 ms for Ni — the *element* figure — and presents it as the surface morphing period.

---

## Category 7 — Closed mechanical control loop

| Quantity | Value | Object | Type | ID |
|---|---|---|---|---|
| Feedback cycle (= one function evaluation) | **≈0.25 s** (main text) / **0.35 ± 0.15 s** (SI Table 1) | stereo-imaging shape controller | measured | T-BA-03 |
| Iteration cost | **4(N+M)+2 = 34 cycles** for a 4 × 4 sample | same | source statement — **not a duration** | T-BA-04 |
| Convergence | **5–15 iterations = 170–510 function evaluations** | same | measured | T-BA-05 |
| **Convergence time** | **≈2.5 min** (average, 4 × 4, from zero-actuation state) | same | **measured — stated directly by the source** | **T-BA-05** |
| Open-loop replay rate | **10 fps** once voltages are known | same | measured — **a rate, not a latency** | T-BA-06 |

> **⚠ Corrected 17 August 2026.** This category previously recorded an "implied convergence time" of ≈1.25–3.75 s derived as 5–15 × 0.25 s. **That derivation was invalid and is retracted** (E-DR-03; `citation_audit.md` C5): an iteration comprises 34 feedback cycles, and the supplementary information states the convergence time directly as ≈2.5 min — about forty times larger.

One entry, one platform, no RF. But it is the only measurement in this corpus of *what it costs to make a surface actually reach a commanded shape under feedback*, and **on that same platform** it is more than three orders of magnitude larger than the element response (T-BA-01, < 0.07 s) that the system literature cites as the feasibility argument. Because no second platform measures closed-loop convergence, this level of the comparison is **not independently replicated** and must never be presented as one.

The two figures in this category must not be collapsed. **≈2.5 min is the cost of *searching* for the actuation voltages that realise a new target shape** on a nonlinear structure with a camera in the loop; **10 fps is the cost of *replaying* voltages already known.** Both are properties of the same platform. Which one is relevant to a FIM depends on whether the required geometry can be precomputed — a question no reviewed system paper poses. The informal phrase "morphing time" does not distinguish them, which is precisely the failure this matrix exists to prevent.

---

## Category 8 — Partial electronic loops on a flexible RF surface

| Quantity | Value | Interval | Type | ID |
|---|---|---|---|---|
| Data preparation | ≈4 ms | sensor reception + processing | measured | T-LI-01 |
| ANN inference | ≈2 ms | input → coding output | measured | T-LI-02 |
| Bias supply | 5.25 ms | command → bias out | measured | T-LI-03 |
| Component sum | 11.25 ms | — | derived, matches Fig. 3g | E-DR-04 |
| **Measured total** | **16.76 ms** | **shape acquisition → bias-voltage supply** | measured | **T-LI-04** |
| **End-to-end, independent experiment** | **16.7 ms** | **sensor trigger → stabilised RF output** | measured (oscilloscope + log detector, 3.1 GHz) | **T-LI-06** |
| Deformation-rate limit | 60 Hz | derived by the authors from T-LI-04 | measured — **a rate** | T-LI-07 |
| Projected improvement | < 10 ms | requires different acquisition circuits and protocol | **projected, not built** | T-LI-08 |

**T-LI-04 is the single most-cited hardware number available to this project, and it is also the most frequently misused.** It excludes, by the authors' own definition: the deformation that produced the shape, any mechanical settling, and any post-command RF stabilisation. It is a compensation latency, not an adaptation latency.

**T-LI-06 is new to this project (supplementary retrieval, 17 August 2026) and is the only interval anywhere in the corpus whose end event is stabilised radiation.** It is *not* a substitute for the missing RF-aperture morphing measurement: the geometry is static throughout, the trigger is a sensor press, and no shape change occurs inside the interval. Its significance is twofold — it shows the end event is well-defined and instrumentable with ordinary equipment, and it removes any licence to claim that RF stabilisation is never timed in this literature.

---

## Category 9 — Not measured by anything in the corpus

| Missing quantity | ID |
|---|---|
| Commanded mechanical actuation time of an **RF** metasurface aperture | T-GAP-02 |
| Mechanical settling of an aperture carrying meta-atoms, bias network and RF ground | (within T-GAP-02) |
| Calibration / refocusing time after deformation of a flexible RF aperture | T-GAP-01 |
| Post-command RF stabilisation onset | T-GAP-03 |
| End-to-end interval from channel or geometry observation to stabilised RF response | E-AA-01 |
| Repeatability, hysteresis and fatigue of a morphing RF aperture | — |
| Actuation energy per shape change for an RF aperture | — |

---

## Qualitative synthesis figure (manuscript Figure 3)

Because the categories are not commensurable, the manuscript presents them as **ordered bands on a logarithmic axis, each band labelled with the architecture and the start/end events**, and explicitly *not* as a single latency budget:

```
   10 µs        100 µs        1 ms         10 ms        100 ms         1 s          10 s
     │            │            │            │             │             │            │
 [DEMAND]  ◄─ Doppler ≈19 kHz at 28 GHz/208 m/s (derived, E-DR-01)
                          ◄── 51-symbol >0.5-correlation window, 90 mph @ 2.6 GHz (T-CH-02)
 [COMPUTE]                     ├── ANN inference 2 ms (A3, T-LI-02) ──┤
                               ├──── FIM channel estimation 4–100 ms, desktop CPU (A1, T-YA-01) ────┤
 [CONTROL]      ├─ per-element FPGA <0.1 ms (A5, T-AK-01) ─┤
                                    ├── tile update <10 ms (A5, T-AK-02) ──┤
 [EM STATE]                              ├── LC on 15 ms / off 72 ms (A5, T-NE-01/02) ──┤
                                          ◄ varactor "negligible" (A3, T-LI-05) — no number
 [PARTIAL LOOP]                          ├─ FISP 16.76 ms, shape acq → bias out (A3, T-LI-04) ─┤
 [MECH ELEM]                             ├─ ribbon 30 ms (A4) · beam <70 ms (A4) ─┤
 [MECH SURF]                                      ├─ <0.1 s (A4) · 300 ms (A4) · 650 ms (A4) ─┤
 [MECH LOOP — replay]                     ◄ 10 fps open-loop, voltages known (A4, T-BA-06)
 [MECH LOOP — search]                                                              ├── ≈2.5 min closed-loop convergence (A4, T-BA-05) ──┤
 [RF STABILISATION, static geometry]     ├─ 16.7 ms trigger → stable RF (A3, T-LI-06) ─┤
 [COMMANDED ACTUATION, RADIATING APERTURE]                          ▓▓ NO MEASUREMENT FOUND IN REVIEWED SET ▓▓
 [RF SETTLING AFTER COMMANDED MORPH]              ▓▓ NO MEASUREMENT FOUND IN REVIEWED SET ▓▓
```

*Figure note: the two `MECH LOOP` rows belong to one platform and differ by more than three orders of magnitude because they time different operations — replaying a known shape versus searching for an unknown one. Any rendering of this figure must keep them on separate rows and label them, or it will reproduce the substitution the manuscript documents.*

The two shaded bands are the manuscript's conclusion. Every process for which a number exists is measured on an architecture that is missing at least one of: an RF layer, controlled geometry, or a channel.

# Evidence Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.1 · 18 August 2026 (freeze consistency gate; see `CHANGELOG.md` v1.5)

Checks the draft for evidence-level inflation: any place where a simulation, an assumption, a projection or a derivation is presented with more authority than it has.

---

## 1. Upgrade check

Searched the draft for every verb of demonstration ("shows", "demonstrates", "establishes", "confirms", "proves", "validates") and checked the evidence level of what it attaches to.

| Statement | Attached to | Level | Verdict |
|---|---|---|---|
| "the reported benefits are substantial **in simulation**" (§1.1) | 3 dB, 2.5 dB (**the 125 % figure was withdrawn 18 Aug 2026** — absent from YAN-25's version of record; §1.1 now carries that source's qualitative statement instead) | L2 | ✅ qualifier present in the same sentence |
| "Physical flexibility of a large radiating aperture **is demonstrated**" (§7.1) | GAL-22, LI-25, LU-25 | L5–L6 | ✅ correct |
| "In-situ shape sensing **is demonstrated** on three independent platforms" (§7.1) | LI-25, BAI-22, GAL-22 | L4–L6 | ✅ correct; independence verified in `independence_audit.md` |
| "Commanded shape control with closed-loop verification **is demonstrated**" (§7.1) | BAI-22 | L4 | ⚠ **at risk of reading as an RF claim.** §7.1 lists it among RF-adjacent capabilities. **Fix applied:** clause added naming the platform as mechanical. |
| "Deformation-aware electronic compensation is demonstrated **at over-the-air level**" (§7.1) | LI-25 | L6 | ✅ correct |
| ~~"the strongest replicated result in the reviewed set" (§6.2)~~ | ~~element < surface < loop ordering~~ | ~~L4 ×2, independent~~ | ❌ **WITHDRAWN 17 Aug 2026.** Two independence groups establish only that *element ≠ surface*; the closed-loop level rests on BAI-22 alone, so the three-level structure was never replicated. The step sizes also differ (order of magnitude on NI-22, not on BAI-22), and the loop value was wrong. §6.2 now claims only non-substitutability. See `CHANGELOG.md` CH-23. |
| ~~"adequate measured support" for fast stages (§9.1)~~ | ~~AKR-26, NEU-24~~ | ~~L5~~ | ❌ **WITHDRAWN 17 Aug 2026.** "Adequate" is a sufficiency verdict and requires a deadline the evidence does not define; the same phrase was also applied to channel acquisition, whose evidence is **simulated**, making the sentence internally inconsistent. §6.6 and §9.1 now state measured facts without sufficiency verdicts. See `CHANGELOG.md` CH-26 and `latency_definition_audit.md` F5. |
| ~~"we obtain by multiplying the two reported quantities…" (§4.6)~~ | ~~1.25–3.75 s~~ | ~~derived~~ | ❌ **RETRACTED 17 Aug 2026 — the derivation was invalid.** Labelling a derived value as derived is necessary but not sufficient; this one was also *wrong*, because an iteration comprises 34 feedback cycles. §4.6 now cites the source's directly-stated ≈2.5 min. See `citation_audit.md` C5. **Lesson for this audit: the "is it labelled?" check does not test whether the arithmetic is valid. A derivation check was added below.** |
| ≈2.5 min closed-loop convergence (§4.6, §5.3, §6.2) | ≈2.5 min | **source-stated, not derived** | ✅ no derivation required |
| "Derived by us" (§1 fn. 1, §3 fn. 1) | 19.4 kHz | derived | ✅ labelled twice |
| ~~"conditional arithmetic, not a reported value" (§3.1)~~ | 0.51 ms | derived | ✅ **removed from §3.1 on 17 Aug 2026**; the "conditional" label was itself wrong, since the source states f_s = 100 kHz. Retained only in `evidence_matrix.md` E-DR-02. |
| "a tolerance of λ/20 is roughly half a millimetre" (§7.2) | illustration | derived | ✅ presented as an illustration of what a criterion would look like, not as a source's criterion |

**No upgrade found.** One presentation risk found and fixed.

## 2. Downgrade check (the opposite failure)

A review that systematically understates evidence is also inaccurate. Checked for places where the draft is unfairly dismissive:

- **LI-25.** The draft could read as diminishing a *Nature Communications* result by repeatedly noting that its deformation is external. Counterweight verified: §5.1 states the capability "is not in doubt", §7.1 lists it among established capabilities, §5.1 calls it "the reviewed set's most instructive hardware source". ✅ Balanced.
- **BAI-22 / NI-22.** The draft repeatedly notes they have no RF layer. Counterweight verified: §5.3 calls NI-22's decomposition "the single most useful set of numbers in the corpus", and §6.2 treats both platforms as the only sources of measured mechanical timescales. ✅ Balanced. **Note (17 Aug 2026):** §6.2 no longer calls their agreement "the strongest replicated result" — that phrase was withdrawn (CH-23) because the three-level ordering was never replicated. The counterweight now rests on §5.3 alone, which is sufficient.
- **RAN-25.** The draft is critical of footnote 8. Counterweight verified: §4.5 states "We take this claim seriously, because if it holds, the mechanical timescale largely stops mattering and the architecture becomes far easier to defend", and §7.5 states each premise "may turn out to be correct". ✅ Balanced.
- **GAL-22.** Criticised for reporting no timing. Counterweight verified: §5.4 and §7.4 both frame it as the *highest-value cheapest* opportunity precisely because the science is already done. ✅ Balanced.

## 3. Assumption-versus-finding check

Every assumption identified in the reviewed literature is labelled as an assumption in the draft:

| Item | Labelled as | Verdict |
|---|---|---|
| quasi-static flat fading | "assumes" (§2.3 via evidence matrix; §6.6) | ✅ |
| perfect CSI | "assumes" | ✅ |
| movement-induced Doppler perturbation negligible | "declares negligible", "asserted, not bounded" (evidence matrix E-02) | ✅ |
| shape reuse irrespective of delay/Doppler/waveform | "an assertion in a footnote", "It is not derived … and it is not tested" (§4.5) | ✅ |
| shape update per coherence block | "a legitimate modelling choice" / "asserts" (§4.5) | ✅ |
| 10 ms / 30 ms morphing periods | "tabulated", "discrepancy requiring verification" (§6.5) | ✅ |

## 4. Simulation-as-hardware check

Searched for any place a simulated result carries a hardware implication without a qualifier: **none found.** The four FIM system papers are described as simulation throughout; XU-22's 51-symbol figure is labelled "a simulation result, not a measurement" in §3.1; TAG-20 and BUD-22 and YOO-21 are cited only for modelling.

## 5. Fix applied

**E-FIX-1.** §7.1 — clause added identifying the commanded-shape platforms as mechanical, so the capability list cannot be read as claiming an RF demonstration. *(Applied.)*

## 6. Residual evidence risks

| Risk | Severity | Status |
|---|---|---|
| Three external sources at L-external (online full text only) carry two of the three traceability findings | **Medium-high** | disclosed with footnotes at every point of use |
| The "no source reaches L7" claim depends on complete extraction of 24 sources by one reviewer | Medium | bounded to the reviewed set; extraction protocol documented and reproducible |
| Evidence-level assignments for the three image-only sources rest on abstracts | Low | those sources carry no load-bearing claim |

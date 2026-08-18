# Redundancy Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026

Checks whether any idea is developed more than once, and whether each paragraph performs a distinct argumentative function.

---

## 1. Idea ownership check

| Idea | Owner | Appearances elsewhere | Verdict |
|---|---|---|---|
| Comparison against the three closest reviews | §1.3 | §9 does not repeat it | ✅ |
| Contribution list | §1.5 | §9.1–§9.3 answer the question rather than re-list contributions; §10 restates in prose form as a conclusion should | ✅ |
| Seven architecture classes | §2.1 | §5 uses the labels without redefining | ✅ |
| The geometry-as-disturbance inversion | §2.3 | §4.4 (one clause), §7.3 (developed differently — as an *integration* gap rather than a taxonomic one) | ⚠ **borderline.** §2.3 and §7.3 make related points. Judged acceptable: §2.3 is taxonomic (which class does each source belong to), §7.3 is combinatorial (which components does each platform hold). Different work. |
| The empty quadrant | §2.8 | §7.1–§7.2 name the gap without redrawing the quadrant; §10 alludes once | ✅ |
| Coherence time is a threshold | §3.1 | §6 does not restate | ✅ |
| Doppler ≈19.4 kHz | §3.2 | §6.6 table row references it; §1.1 states it once as motivation | ⚠ appears three times. Judged acceptable — §1.1 motivates, §3.2 derives, §6.6 tabulates. Each use is functionally distinct. |
| Ten stage definitions | §4.1 | §5, §6.6, §8 use the labels only | ✅ |
| The element/tile bound pair (up to two orders of magnitude apart) | §6.4 | §1.2 (as the introduction's worked example), §5.2 (as the measurement), §9.2 (as a modelling recommendation) | ⚠ **four appearances — the draft's most repeated fact.** Judged acceptable but at the limit: §1.2 introduces the problem, §5.2 reports the measurement, §6.4 draws the general conclusion, §9.2 converts it to advice. **Recommendation: if the manuscript must be shortened, cut the §1.2 instance and let §5.2 carry it.** |
| Individual timing values | §5 / Table 5 | §6 refers to them; §6.3 restates three values because the comparison requires them side by side | ✅ necessary restatement |
| Pooling prohibition | §6.1 | §8.1 restates the principle in a different register (why the framework prescribes definitions not thresholds) | ✅ different purpose |
| The traceability finding | §6.5 | §7.5 (one sentence), §9.5 (one clause), §10 (one clause) | ✅ referenced, not re-derived |
| G1–G4 | §7.2 | §7.4 ranks them; §8 motivates fields from them; §9.3 turns them into experiments | ✅ each transformation is new work |
| "This does not show FIMs are infeasible" | §7.5 | §9.5 restates | ⚠ **duplicated.** Judged **acceptable and deliberate**: it is the single most important thing for a reader not to misread, and it appears once mid-manuscript and once in the concluding discussion. This is the one place where redundancy is a feature. |
| The stopwatch experiment | §5.4 | §7.4, §9.3, §10 | ⚠ **four appearances.** §5.4 identifies it, §7.4 ranks it, §9.3 specifies it, §10 alludes. **Recommendation: cut the §5.4 instance to a single clause if length is a constraint.** |

## 2. Paragraph-function check

Sampled twenty paragraphs across §§1–9; each was assigned the argumentative function it performs. No two adjacent paragraphs were found to perform the same function. No paragraph was found whose deletion would leave the argument intact, with two exceptions:

- **§2.6 paragraph on A6 (movable antennas)** contributes little beyond what §1.3 already establishes about MA-26. **Retained** because §2.7's transfer rules need A6 defined, but it is the first candidate for compression.
- **§3.5 second paragraph** (the observation that estimation cost scales with virtual array size) partly anticipates §6.4. **Retained** — it makes a different point (computation scaling vs. control-network serialisation) and is one of the draft's more useful observations.

## 3. Structural check

The provisional outline separated electronic and mechanical hardware into two major sections. That structure was tested and rejected: it would have placed the liquid-crystal switch-off time and the mechanical surface-morphing time in different sections, and §6.3's finding — that the two bands overlap — depends on their being presented together. The single hardware section with four subsections organised by *what was measured* is the correct structure and the draft uses it.

## 4. Length discipline

The draft has no background section on the history of metamaterials, 5G, 6G, RIS or ISAC. Section 1 spends four paragraphs on motivation before stating the question. No section summarises the previous section. No section opens with a roadmap sentence. ✅

## 5. Recommendations if compression is needed

In order:
1. Cut the §1.2 instance of the element/tile bound-pair example (−1 paragraph).
2. Compress §5.4's forward reference to the stopwatch experiment to one clause (−3 sentences).
3. Compress §2.6's A6 paragraph (−4 sentences).
4. ~~Delete the ≈0.51 ms conditional conversion in §3.1~~ ✅ **done 17 Aug 2026** (−2 sentences). It was not in fact conditional — the source states f_s = 100 kHz — but it is removed all the same; see `unresolved_questions.md` U5.

Nothing in §§4, 6, 7 or 8 should be cut; those four sections carry the contribution.

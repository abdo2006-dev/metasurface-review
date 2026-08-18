# Independence Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026

Purpose: ensure that no claim in the draft is supported by two sources that are not independent.

---

## 1. Independence groups identified

| Group | Members | Basis for non-independence | Evidence |
|---|---|---|---|
| **IG-1** | RAN-25, MOR-26 | conference/journal lineage of one study | MOR-26 p. 1, verbatim: *"An extended version of this work has been published in the Transactions on Wireless Communications [1]."* Same model, same waveforms, same optimisation, overlapping author set. |
| **IG-13** | TIS-25, TIS-25-AAM | published version and accepted manuscript of the same survey | same DOI |
| **IG-20** | HAR-20, HAR-22 | same group (PTB), same design lineage; the 2022 paper is the array-level follow-up to the 2020 element paper | shared authors, sequential volumes of the same journal |
| **IG-22** | LU-25, LU-26 | same group (Nanjing Univ. of Posts and Telecommunications, corresponding author Y. Yu), same material system (printed liquid metal on PDMS), overlapping author set | verified from both title pages |

## 2. Compliance check on the draft

| Claim in the draft | Sources cited | Independence verdict |
|---|---|---|
| The FIM system literature assumes instantaneous geometry (§4.5) | RAN-25, ANJ-25, YAN-25, MOR-26 | ⚠ **RAN-25 and MOR-26 are IG-1.** The claim is about four papers but rests on three independent lines. **Fix applied:** §4.5 now states the count and the lineage. |
| The movement-perturbation assumption (evidence matrix E-02) | RAN-25 + MOR-26 | ✅ the matrix records both under IG-1 and marks MOR-26 as non-independent; the manuscript body cites only RAN-25 for it |
| ≈10-iteration convergence | MOR-26 | ✅ attributed to the short paper alone; the draft never presents it as confirmation of RAN-25 |
| Element-level and full-surface mechanical response are distinct quantities, with the element value below the surface value **within each platform** (§6.2) | BAI-22 (IG-8), NI-22 (IG-9) | ✅ **the two platforms are genuinely independent** — different groups, materials, actuation geometries, journals — so the *within-platform* element-below-surface observation is made twice independently. ⚠ **Corrected 17 Aug 2026: this does NOT license calling the three-level ordering "replicated".** The step magnitudes differ strongly (≈10× on NI-22; < 0.07 s → 0.1 s on BAI-22, not an order of magnitude), and the third level — closed-loop convergence — rests on BAI-22 alone. Independence of two sources on a two-level observation is not replication of a three-level structure. §6.2 no longer uses the word. See `evidence_audit.md` §1 and `evidence_matrix.md` Part C. |
| In-situ shape sensing on three platforms (§7.1) | LI-25 (IG-5), BAI-22 (IG-8), GAL-22 (IG-10) | ✅ three distinct groups |
| Flexible reconfigurable reflective apertures are buildable (§5.1) | LI-25 (IG-5), LU-26 (IG-22) | ✅ independent of each other — different groups, frequencies, tuning devices, phase resolutions. §5.1 explicitly calls LU-26 "independent confirmation … beyond a single group's platform". |
| Flexible apertures tolerate bending (§7.1) | GAL-22, LI-25, LU-25 | ⚠ **LU-25 and LU-26 are IG-22.** §7.1 cites LU-25 and §5.1 cites LU-26 for adjacent but distinct claims (bending tolerance of a passive coding pattern vs. an electronically reconfigurable aperture). No claim is supported by both. ✅ pass |
| Fixed-curvature conformal design has substantial prior art (§2.5) — *reworded 17 Aug 2026 from "is solved"; six independent groups establish validated methods for important cases, which is not the same as closing the problem* | BUD-22, YOO-21, LIH-19, PEP-26, CHE-26, LU-25 | ✅ six independent groups |
| The reviews partition cleanly (§1.3) | MA-26, TIS-25, SAI-22 | ✅ three independent groups; TIS-25-AAM excluded |
| The traceability finding (§6.5) | **four** citing system papers + BAI-22 + NI-22 + LI-25 | ⚠ **Re-tested 18 Aug 2026 by forward citation search (S11), and the independence result is negative and now measured rather than assumed.** All four papers reproducing the practice share at least one author with the corpus FIM lineage — Jiancheng An appears in three, Chau Yuen in three — and **no author-disjoint publication group reproduces it**; 14 of the 20 identified FIM system studies share an author with that network, 4 are disjoint from it, and 2 are disjoint from both it and all three primary hardware sources (v0.22 recount from published-record authorship; the v1.8 figure of 17 of 20 was wrong and rested on an unresolved category). The case base widened from two papers to four; the independence basis did not widen at all. **Fix applied:** §6.5 states both facts. |

## 3. Fixes applied

**I-FIX-1.** §4.5 — "Across the four FIM system papers reviewed" now notes that two of them are versions of one study, so the claim rests on three independent lines. *(Applied.)*

**I-FIX-2.** §6.5 — the papers exhibiting the tabulated-morphing-period practice share authors; the draft states this and correspondingly weakens the claim from "the FIM system literature does X" to "this collaboration network's papers do X". This is a material weakening and it is correct. *(Applied.)* **Updated 18 Aug 2026:** the forward citation search it called for has now been run. The clause "and we did not test how widely the practice extends" is **withdrawn — we tested it.** The replacement is narrower and better evidenced: the practice is documented in four papers across four first-author teams, **all within one collaboration network**, alongside seven papers that cite the same primaries and attach no timing value. C3 accordingly stays at **Level A** (narrow framing), with a wider case base.

## 4. Supplementary material

Supplementary information belongs to its parent paper and is never independent evidence. **This rule was tested on 17 August 2026 when four supplementary and peer-review PDFs were retrieved and added to the corpus.** They are assigned to their parents' independence groups — LI-25-SI and LI-25-PR to IG-5, BAI-22-SI and BAI-22-PR to IG-8 — and the corpus file count rose from 27 to 31 while the independent-contribution count **stayed at 24**. Retrieved material is subject to the same rule as found material: a supplement that strengthens a finding does not add a source supporting it.

The peer-review files deserve one note. They contain referee reports and author rebuttals, which are neither the authors' claims nor independent studies. Nothing in this review's evidence matrix rests on them; they were read to confirm document identity and completeness of the retrieved packages. **No claim in the manuscript cites a referee's opinion as evidence**, and none should.

## 5. Residual independence risks

| Risk | Severity |
|---|---|
| The external FIM papers located in the search overlap heavily in authorship (An, Yuen, Debbah, Al-Dhahir recur); the field's system-modelling side may be less independent than the citation count suggests | **Medium** — noted in `unresolved_questions.md`; a proper co-authorship analysis was not performed |
| Journal versions of arXiv sources may have merged or split relative to the preprints held here | Low |

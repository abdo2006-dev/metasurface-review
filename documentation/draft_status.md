# Draft Status

**Version:** 1.8 · 18 August 2026 · manuscript draft **v0.21** — reviewer-blocker revision (see `CHANGELOG.md` v1.8)

> **What v0.21 is.** A targeted repair of the methodological and evidentiary problems raised in an independent review of v0.20 — **not** a rewrite, and not a broadening of any claim. Four things changed materially: the adaptation-chain coding was rebuilt on two axes so that a quantitative RF measurement can no longer be counted as a measured latency; the forward citation search was re-executed against an explicit published query, correcting three counts and surfacing one new author-disjoint counterexample; all unbounded absence and priority language was bounded; and four over-reaches were corrected, one of which was a claim resting on a source we had not read. **C3 remains at Level A.** Full change list in `CHANGELOG.md` v1.8. A section-number crosswalk from the v0.14 numbering used throughout the older documentation is at the end of `manuscript_argument_map.md`.

> ⚠ **Two verbs are now load-bearing and must not drift.** The stage count is a **timing** count: *"no source **times** more than five of the ten stages"* — under the quantitative reading the maximum is six. And the C3 finding is stated **within its observation window**: 14 of 21 candidate studies read, an author-disjoint instance among the unread seven not excludable.

---

## 1. Section status

| § | File | Status | Carries | Evidence sufficiency |
|---|---|---|---|---|
| — | `00_front_matter.md` | **complete** | title, abstract, index terms | — |
| 1 | `01_introduction.md` | **complete** | — | good |
| 2 | `02_scope_and_method.md` | **complete** | — | good — new section; states the method where a reviewer will look for it |
| 3 | `03_architectures.md` | **complete** | **Table 1**, **Figure 1** | good |
| 4 | `04_demand_side.md` | **complete** | **Table 2** | **limited** — the only quantified coherence figure in the corpus is at 2.6 GHz; there is no mmWave coherence measurement, and the 28 GHz Doppler figure is ours. Stated in the text. |
| 5 | `05_adaptation_chain.md` | **complete** | **Table 3**, **Figure 2** | good |
| 6 | `06_hardware_evidence.md` | **complete** | **Table 4**, **Table 5** | good — Table 5 is the manuscript's centrepiece and is now produced |
| 7 | `07_synthesis.md` | **complete** | **Table 6**, **Figure 3** | good |
| 8 | `08_traceability.md` | **complete** | **Table 7** | **mixed** — rests partly on external sources read as author versions; every one is identified bibliographically in the reference list |
| 9 | `09_validation_gap.md` | **complete** | **Table 8**, **Figure 4** | good — this section states absences, which the extraction protocol supports |
| 10 | `10_reporting_framework.md` | **complete** | **Table 9** | good — every field traced to an observed deficiency |
| 11 | `11_discussion.md` | **complete** | — | good — limitations stated without hedging |
| 12 | `12_conclusion.md` | **complete** | — | good — answers six questions, ends on priorities |
| — | `99_references.md` | **complete** | 33 entries | every field verified against Crossref or the arXiv metadata endpoint |

**Word count.** **29 049 words** across the twelve sections, front matter and references, of which **23 472 is prose** and 5 577 is table content. Comparison: v0.20 was 25 495 / 19 984; v0.14 was 21 887 / 19 933. The v0.21 growth of ~3 500 words is almost entirely **bounding and conditioning language** — the two-axis coding explanation in §5.2–5.3, the four access limits in §8.5, the reproducibility description in §2.3, and the per-source status tables — which is the intended direction for a revision whose purpose was to make claims harder to overstate.

## 2. What is now done that was not

| Item | v0.14 | v0.20 |
|---|---|---|
| Tables | seven specified, none drawn | **nine produced** — see `manuscript_argument_map.md` §0 for why the count changed |
| Figures | four specified, none drawn | **four produced** as PDF and PNG from `manuscript/figures/make_figures.py`, which is committed and re-runnable |
| Citation system | internal keys (`[RAN-25]`) | **numbered IEEE-style**, ordered by first appearance; keys survive only in the documentation |
| Bibliography | keyed, not formatted | **33 entries**, author lists read from the held PDFs, every DOI resolved against Crossref |
| Method | inside §1.6 | **its own section (§2)**, with the evidence ladder numbered L1–L7 so Table 8's level column is defined |
| Traceability audit | subsection §6.5 | **its own section (§8)** with its own table |

## 3. What is still not done

**No domain-expert review has occurred.** ⚠ *This is an internal project gate and is deliberately **not** stated in the manuscript* — it describes our workflow, not a scientific limitation, and saying it in the paper implied that peer review must precede submission (`CHANGELOG.md` v1.8). The manuscript instead states the scientific version: extraction and classification were performed by a single reviewer and were not independently duplicated or adjudicated.

**No headline interval in the manuscript carries an uncertainty.** No reviewed source reports a repetition count or dispersion for its headline response, morphing or adaptation interval. ⚠ *Not universal across the register* — Table 5 row 28 carries 0.35 ± 0.15 s. Additional literature cannot retroactively supply uncertainty for values already published without it; only raw data, reanalysis, repeated measurement or new experiments could. Group C of the reporting framework asks for it explicitly.

**Seven of the 21 identified system studies are behind publisher paywalls and were not read.** Every count arising from the forward citation search is a lower bound, and an author-disjoint instance reproducing the substitution among them would move C3 from Level A to Level B. **This remains the only open item that could change a contribution's wording.** Note that the v1.8 re-execution added one previously-missed study and read it: it proved to be an author-disjoint *counterexample*, which strengthens the counterexample base without touching the classification.

**Some sources are identified bibliographically only.** ✅ **Audited 18 Aug 2026** — `source_inventory.md` §5b classifies every claim resting on an unread source as load-bearing or peripheral. One over-reach was found and corrected (HUA-25); the remaining bibliographic-only sources are all peripheral, cited for existence or class membership. **Standing rule: no source that has not been read in full may support a statement about what that source does not contain.**

**Stage-2 screening and full-text extraction remain single-reader judgements.** Retrieval and stage-1 screening are now exactly reproducible from a published script; stages 2 and 3 are recorded per work in `forward_citation_search_results.csv` and are auditable, but not re-derivable. A second screener is the improvement most likely to change a cell.

## 4. Claims limited by evidence, and how they are marked

| Claim | Limitation | Marking in v0.21 |
|---|---|---|
| 16.76 ms interval | shape acquisition → bias-voltage supply; excludes deformation and settling | §6.2 states the definition, the per-component method, and that no repetitions are reported; Table 4 names the substitution it invites; Table 5 row 20 carries the events |
| 16.7 ms trigger → stabilised RF | measured on **static geometry** | stated at every use — §6.2, Table 3 ‡ note, Table 5 row 32, Table 6 S10 row, §9.2 G4 |
| All **headline** intervals | no source reports repetitions or dispersion for them; one subordinate quantity does (0.35 ± 0.15 s) | §2.5 and §11.4 state the scope and name the exception; absence claim A15; Table 9 Group C |
| The tabulated 10 ms | complete package held; the tabulating authors' derivation unobservable | §8.4 says "discrepancy requiring verification" and says why the complete package does not upgrade it |
| Our retracted ≈1.25–3.75 s derivation | invalid; superseded by the source's ≈2.5 min | **disclosed in the body** at §7.2 and §11.4 (U12b decision: RETAIN) |
| The propagation practice | four papers forming **one connected co-authorship network**, **zero author-disjoint groups reproducing it**; observed across **14 of 21** studies, 7 unread | §8.5 states all four limits explicitly, including that an author-disjoint instance among the unread seven cannot be excluded; C3 in §1.6 and the abstract carry the 14/21 bound |
| Counterexample independence | **two** counterexamples are now fully author-disjoint; one earlier entry was withdrawn because its full text was never read | Table 7 rows N1 and N3; the withdrawn case (HUA-25) is cited only for verified authorship — **corrected twice, 18 Aug 2026**, see CH-105 |
| Coherence-block update assumption | external source, author version | cited as a numbered reference with its status marked |
| Three image-only sources | abstracts and metadata only | §11.4; no load-bearing claim drawn |
| λ/20 arithmetic in §9.2 | **illustrative of the form of a criterion, not a recommended value** | marked in §9.2 and disclaimed again in Table 9 Group C |

## 5. Gate check against the project brief

| Gate | Status |
|---|---|
| Source inventory | ✅ `source_inventory.md` (+ §3b, the bibliographic completion pass) |
| Duplicate / independence mapping | ✅ `source_inventory.md` §4 + `audits/independence_audit.md` |
| Claim-level evidence matrix | ✅ `evidence_matrix.md` |
| Architecture taxonomy | ✅ `architecture_taxonomy.md` → manuscript Table 1 |
| Timescale matrix | ✅ `timescale_matrix.md` → manuscript Table 5 |
| Evidence-strength matrix | ✅ `evidence_strength_matrix.md` → manuscript Table 8 level column |
| Novelty boundary | ✅ `novelty_boundary.md`, N3 at **Level A** |
| Article-type assessment | ✅ structured critical review; title re-checked against the new structure and retained |
| Manuscript argument map | ✅ **v2.0**, remapped, with the section-number crosswalk |
| Tables and figures | ✅ **produced** |
| Bibliography | ✅ produced, verified |
| CST inclusion gate | ✅ excluded — `article_type_assessment.md` §6 |
| Domain-expert review | ✗ **not done** |

## 6. Immediate next actions, in order

1. **Supervisor / domain-expert review.** Everything else is subordinate to this.
2. **A protocol-driven database search** (IEEE Xplore, Scopus, Web of Science) with recorded strings and counts. This would re-test absence claims A1, A2, A3, A5, A7 and A9, and would resolve whether an author-disjoint instance of the substitution exists — the one finding that could move C3 off Level A.
3. **Retrieve the seven paywalled system papers** if institutional access becomes available, and re-run the S11 extraction over them.
4. **Complete the outstanding version checks** for the sources still identified bibliographically only.
5. **Journal-format conversion** once a venue is selected; the reference list is already in a neutral numbered IEEE style and the figures are vector PDFs.

## 7. Readiness statement

The manuscript is **complete as a draft, materially stronger than v0.20, and not ready for submission.** Readiness is a judgement for an independent reviewer inspecting v0.21, not one this project can make about itself.

What improved is real and can be stated precisely: the argument now proceeds in an order a reader can follow without the audit machinery showing; the method is locatable; the traceability result has the prominence its evidence supports; every table and figure the manuscript refers to exists; and the citations are verified rather than keyed. Two factual errors were caught in the process — a wrong DOI and an overstated independence claim about a counterexample — which is a reminder that a rewrite pass is also an inspection pass.

What has not changed is what keeps it unready. Extraction remains a single-reader exercise. Seven of the 21 identified system studies were not readable, and that bound now appears wherever C3 appears rather than only in a limitations list. And the strongest contribution, the traceability finding, is deliberately held at its narrow framing: four papers in one connected co-authorship network, zero author-disjoint groups reproducing the practice, observed across 14 of 21 studies, no prevalence claim. That wording is load-bearing and was chosen against the evidence rather than by preference — if a later pass finds itself reaching for "the field" or "widespread", the classification is being violated, not the style.

**What v0.21 demonstrated about the method.** Every one of the four corrections in this pass came from performing a check that had not been performed before: writing out a regex that had been elided, resolving a print date rather than trusting an online-first one, asking which source supported a sentence about a document's contents, and asking what a code letter actually meant in each cell. Three of the four had survived a full authoring pass and a prior self-review. That is the argument for the reporting framework in §10 stated as a fact about this project rather than as a recommendation to others.

**Completeness is not readiness, a rewrite is not a review, and a correction found is not a correction absent.**

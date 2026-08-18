# Draft Status

**Version:** 1.7 · 18 August 2026 · manuscript draft **v0.20** — publication-oriented authoring pass (see `CHANGELOG.md` v1.7)

> **What v0.20 is.** A full rewrite and restructuring of the manuscript into twelve sections, with all nine tables and all four figures produced, a numbered IEEE-style reference list built from verified metadata, and the internal evidence keys removed from the reader-facing text. **The scientific evidence base was frozen at documentation v1.6 and was not revised**, apart from two factual corrections found while completing the bibliography (`CHANGELOG.md` CH-96, CH-97). A section-number crosswalk from the v0.14 numbering used throughout the older documentation is at the end of `manuscript_argument_map.md`.

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

**Word count.** 25 495 words across the twelve sections and front matter, of which **19 984 is prose** and the remainder is table content. The comparable v0.14 figures are 21 887 and 19 933: **prose length is unchanged while nine tables, four figures, a methods section and a bibliography were added**, so the rewrite tightened the text by roughly the amount the new material added.

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

**No domain-expert review has occurred.** This remains the largest single gap and it is not one this project can close by itself.

**No interval in the manuscript carries an uncertainty.** No reviewed source reports a repetition count or a dispersion figure for its headline timing value. This is a deficiency in the sources; no further searching would repair it, and the reporting framework asks for it explicitly (Group C).

**Seven identified system papers are behind publisher paywalls and were not read.** Every count arising from the forward citation search is therefore a lower bound, and an author-disjoint instance among them would move C3 from Level A to Level B. This is the only open item that could change a contribution's wording.

**Some sources are identified bibliographically only.** Quantitative claims keyed to them should be re-verified against published versions before submission. The reference list marks each such entry in bold.

## 4. Claims limited by evidence, and how they are marked

| Claim | Limitation | Marking in v0.20 |
|---|---|---|
| 16.76 ms interval | shape acquisition → bias-voltage supply; excludes deformation and settling | §6.2 states the definition, the per-component method, and that no repetitions are reported; Table 4 names the substitution it invites; Table 5 row 20 carries the events |
| 16.7 ms trigger → stabilised RF | measured on **static geometry** | stated at every use — §6.2, Table 3 ‡ note, Table 5 row 32, Table 6 S10 row, §9.2 G4 |
| All quoted intervals | no source reports repetitions or dispersion | §11.4; absence claim A15; Table 9 Group C |
| The tabulated 10 ms | complete package held; the tabulating authors' derivation unobservable | §8.4 says "discrepancy requiring verification" and says why the complete package does not upgrade it |
| Our retracted ≈1.25–3.75 s derivation | invalid; superseded by the source's ≈2.5 min | **disclosed in the body** at §7.2 and §11.4 (U12b decision: RETAIN) |
| The propagation practice | four papers, **zero author-disjoint groups**; 7 papers unread | §8.5 reports the count, the negative independence result and the counterexamples, and declines to generalise |
| Counterexample independence | one counterexample shares an author with a cited hardware paper | §8.5 and Table 7 row N1 state which is fully disjoint and which is not — **corrected 18 Aug 2026** |
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

The manuscript is **complete as a draft, materially stronger than v0.14, and not ready for submission.**

What improved is real and can be stated precisely: the argument now proceeds in an order a reader can follow without the audit machinery showing; the method is locatable; the traceability result has the prominence its evidence supports; every table and figure the manuscript refers to exists; and the citations are verified rather than keyed. Two factual errors were caught in the process — a wrong DOI and an overstated independence claim about a counterexample — which is a reminder that a rewrite pass is also an inspection pass.

What has not changed is what keeps it unready. **It has not been reviewed by a domain expert.** No interval in it carries an uncertainty, because no source reports one. Seven relevant papers were not readable. And the strongest contribution, the traceability finding, is deliberately held at its narrow framing: four papers, zero author-disjoint groups, no prevalence claim. That wording is load-bearing and was chosen against the evidence rather than by preference — if a later pass finds itself reaching for "the field" or "widespread", the classification is being violated, not the style.

**Completeness is not readiness, and a rewrite is not a review.**

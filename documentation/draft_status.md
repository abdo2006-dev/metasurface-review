# Draft Status

**Version:** 1.12 · 22 August 2026 · manuscript draft **v0.28a** — professor-readiness audit (see `CHANGELOG.md` v1.12 and `professor_readiness_v0.28a.md`)

> **What v0.28a is.** A **narrow pre-send audit** on top of v0.28: figures renumbered into order of appearance (they were 1, 3, 2, 4), a stale "Table 8" cross-reference removed from inside Figure 4, the §4.2 controller-write / material-transition distinction stated so the section cannot read as a self-contradiction, an unsupported "cheapest" cost claim removed, §5.2 and the conclusion shortened, and the DOCX given real heading and caption styles. No finding, number, attribution or corpus boundary changed. Main-text prose **13 130**, conclusion **650**, manuscript **27 pages**.
>
> **What v0.28 was.** A **structural and editorial revision, not a scientific one.** No finding was added, removed or changed; C1, C3, C4 and G1–G4 were recomputed from the canonical registers during the restructure and are unaltered. What changed is the article's shape. Twelve sections and fifty subsections re-proved the same eight findings in up to eight places each, and the audit machinery — the coding scheme, the evidence ladder, the per-source stage matrix, the propagation inventory, the full reporting checklist — occupied the main text rather than the supplement. The manuscript is now **seven sections and sixteen subsections**, each finding established once with at most one callback; the machinery moved to new supplementary sections S6, S7 and S8 with **no row of any moved table dropped**. Full disposition in `journalization_v0.28.md`.
>
> *Prior passes:* **v0.27a/b** applied professor-send micro-patches. **v0.27** froze the remaining consistency defects. **v0.25/v0.26** compressed and repaired contradictions found in the rendered export. **v0.24** rebuilt the timing taxonomy from first principles, which is where the `·T` maximum became four. **v0.23** made the public artifact runnable on a case-sensitive checkout. **v0.22** repaired the C1 stage count and collapsed a conference/journal pair the dataset counted as two studies. **C3 remains at Level A throughout.** Section-number crosswalks (v0.14 → v0.20 → v0.28) are at the end of `manuscript_argument_map.md`.

> ⚠ **Two things are load-bearing and must not drift.** (1) **C1 must name its axis.** Three counts exist and differ: quantitatively evidenced stages (max **6**, two platforms), measured stage durations `·T` (max **4**, **BAI-22 alone**, which does not radiate), and any timing information `·T`+`·(T)` (max **6**, **LI-25 alone**). The phrase *"five, reached by two platforms"* follows from no consistent rule and was withdrawn in v0.22; the maximum of five was itself superseded at v0.24, when the timing taxonomy was rebuilt and LI-25's RMSD was reclassified as an accuracy. (2) **C3 is stated within its observation window**: 13 of 20 candidate studies read; of the seven unread, exactly one is author-disjoint from both the lineage and all three seeds, and that one study is the whole residual risk to the independence finding.

---

## 1. Section status

| § | File | Status | Carries | Evidence sufficiency |
|---|---|---|---|---|
| — | `00_front_matter.md` | **complete** | title, abstract (249 words), index terms | — |
| 1 | `01_introduction.md` | **complete** | — | good — absorbs the old §4.1 coherence-threshold material |
| 2 | `02_scope_and_method.md` | **complete** | — | good — the symbolic scheme it used to define is now S6 |
| 3 | `03_architectures.md` | **complete** | **Table 1**, **Figure 1**, the ten-stage definitions | good — merges the old §3, §4 and §5.1 |
| 4 | `04_hardware_evidence.md` | **complete** | **Table 2**, **Figure 2** (timing landscape), **Figure 3** (chain coverage) | good — the core evidence section; each platform described once |
| 5 | `05_validation_gap.md` | **complete** | **Table 3**, **Table 4**, **Figure 4** | good — merges the old §7.5, §8 and §9; the traceability inventory is now S8 |
| 6 | `06_implications.md` | **complete** | **Table 5** | good — merges the old §9.4, §10 and §11 |
| 7 | `07_conclusion.md` | **complete** | — | good — a five-paragraph, 650-word journal conclusion carrying no timing values |
| — | `99_references.md` | **complete** | 34 entries | every field verified against Crossref or the arXiv metadata endpoint |

**Supplementary material.** S1 complete timing register · S2 quantity taxonomy · S3 extraction and version-control notes · S4 the complete reporting checklist · S5 forward-citation flow and study register · **S6 coding scheme, evidence ladder and per-source matrix (new)** · **S7 states tracked (new)** · **S8 propagation inventory (new)**. Assembled by `tools/build_supplement_combined.py`, which fails if a part is missing.

**Word count.** **17 030 words** across seven sections, front matter and references, of which **14 761 is prose** and 2 269 is table content; the main text excluding references is **15 399 / 13 130 prose**. Counted by the standing method: whitespace-delimited tokens per line, with lines beginning `|` attributed to tables. Comparison: v0.27b main text was 22 668 / 18 713 prose, so the journalization removed **31.7 %** of the main text and **29.4 %** of its prose while the supplement grew from 4 551 to 7 729 words. Rendered pages: manuscript **27** (41 at v0.27b, 28 at v0.28), supplement **15** (was 8), brief **2** (unchanged).

## 2. What is now done that was not

| Item | v0.14 | v0.20 |
|---|---|---|
| Tables | seven specified, none drawn | **nine produced** — see `manuscript_argument_map.md` §0 for why the count changed |
| Figures | four specified, none drawn | **four produced** as PDF and PNG from `manuscript/figures/make_figures.py`, which is committed and re-runnable |
| Citation system | internal keys (`[RAN-25]`) | **numbered IEEE-style**, ordered by first appearance; keys survive only in the documentation |
| Bibliography | keyed, not formatted | **34 entries**, author lists read from the held PDFs, every DOI resolved against Crossref |
| Method | inside §1.6 | **its own section (§2)**, with the evidence ladder numbered L1–L7 so Table 8's level column is defined |
| Traceability audit | subsection §6.5 | **its own section (§8)** with its own table |

## 3. What is still not done

**No domain-expert review has occurred.** ⚠ *This is an internal project gate and is deliberately **not** stated in the manuscript* — it describes our workflow, not a scientific limitation, and saying it in the paper implied that peer review must precede submission (`CHANGELOG.md` v1.8). The manuscript instead states the scientific version: extraction and classification were performed by a single reviewer and were not independently duplicated or adjudicated.

**No headline interval in the manuscript carries an uncertainty.** No reviewed source reports a repetition count or dispersion for its headline response, morphing or adaptation interval. ⚠ *Not universal across the register* — Table 5 row 28 carries 0.35 ± 0.15 s. Additional literature cannot retroactively supply uncertainty for values already published without it; only raw data, reanalysis, repeated measurement or new experiments could. Group C of the reporting framework asks for it explicitly.

**Seven of the 20 identified system studies are behind publisher paywalls and were not read.** Every count arising from the forward citation search is a lower bound, and an author-disjoint instance reproducing the substitution among them would move C3 from Level A to Level B. **This remains the only open item that could change a contribution's wording.** Note that the v1.8 re-execution added one previously-missed study and read it: it proved to be an author-disjoint *counterexample*, which strengthens the counterexample base without touching the classification.

**Some sources are identified bibliographically only.** ✅ **Audited 18 Aug 2026** — `source_inventory.md` §5b classifies every claim resting on an unread source as load-bearing or peripheral. One over-reach was found and corrected (HUA-25); the remaining bibliographic-only sources are all peripheral, cited for existence or class membership. **Standing rule: no source that has not been read in full may support a statement about what that source does not contain.**

**Stage-2 screening and full-text extraction remain single-reader judgements.** Retrieval and stage-1 screening are now exactly reproducible from a published script; stages 2 and 3 are recorded per work in `forward_citation_search_results.csv` and are auditable, but not re-derivable. A second screener is the improvement most likely to change a cell.

## 4. Claims limited by evidence, and how they are marked

| Claim | Limitation | Marking in v0.23 |
|---|---|---|
| 16.76 ms interval | shape acquisition → bias-voltage supply; excludes deformation and settling | §6.2 states the definition, the per-component method, and that no repetitions are reported; Table 4 names the substitution it invites; Table 5 row 20 carries the events |
| 16.7 ms trigger → stabilised RF | measured on **static geometry** | stated at every use — §6.2, Table 3 ‡ note, Table 5 row 32, Table 6 S10 row, §9.2 G4 |
| All **headline** intervals | no source reports repetitions or dispersion for them; one subordinate quantity does (0.35 ± 0.15 s) | §2.5 and §11.4 state the scope and name the exception; absence claim A15; Table 9 Group C |
| The tabulated 10 ms | complete package held; the tabulating authors' derivation unobservable | §8.4 says "discrepancy requiring verification" and says why the complete package does not upgrade it |
| Our retracted ≈1.25–3.75 s derivation | invalid; superseded by the source's ≈2.5 min | **disclosed in the body** at §7.2 and §11.4 (U12b decision: RETAIN) |
| The propagation practice | four studies forming **one connected co-authorship network**, **zero author-disjoint groups reproducing it**; observed across **13 of 20** studies, 7 unread | §8.5 states all four limits explicitly, and now names the single unread study that could carry an author-disjoint instance; C3 in §1.6 and the abstract carry the 13/20 bound |
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

The manuscript is **complete as a draft, materially stronger than v0.21, and not ready for submission.** Readiness is a judgement for an independent reviewer inspecting v0.23, not one this project can make about itself.

What improved is real and can be stated precisely: the argument now proceeds in an order a reader can follow without the audit machinery showing; the method is locatable; the traceability result has the prominence its evidence supports; every table and figure the manuscript refers to exists; and the citations are verified rather than keyed. Two factual errors were caught in the process — a wrong DOI and an overstated independence claim about a counterexample — which is a reminder that a rewrite pass is also an inspection pass.

What has not changed is what keeps it unready. Extraction remains a single-reader exercise. Seven of the 20 identified system studies were not readable, and that bound now appears wherever C3 appears rather than only in a limitations list. And the strongest contribution, the traceability finding, is deliberately held at its narrow framing: four studies in one connected co-authorship network, zero author-disjoint groups reproducing the practice, observed across 13 of 20 studies, no prevalence claim. That wording is load-bearing and was chosen against the evidence rather than by preference — if a later pass finds itself reaching for "the field" or "widespread", the classification is being violated, not the style.

**What the v0.21 pass demonstrated about the method (retained as a historical record).** Every one of the four corrections in *that* pass came from performing a check that had not been performed before: writing out a regex that had been elided, resolving a print date rather than trusting an online-first one, asking which source supported a sentence about a document's contents, and asking what a code letter actually meant in each cell. Three of the four had survived a full authoring pass and a prior self-review. The v0.22 and v0.23 passes repeated the lesson: the C1 count, the conference/journal collapse, the case-sensitivity failure and the regex-alternative count were all found by executing a check rather than re-reading prose. That is the argument for the reporting framework in §10 stated as a fact about this project rather than as a recommendation to others.

**Completeness is not readiness, a rewrite is not a review, and a correction found is not a correction absent.**

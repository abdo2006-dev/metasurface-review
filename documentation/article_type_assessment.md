# Article-Type Assessment

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026

---

## 1. Verdict

> **Recommended article type: a structured critical review with an explicit, reproducible extraction protocol.**
>
> Suitable descriptors for the manuscript itself: *"critical review"*, *"evidence-mapping review"*, *"structured critical review"*.
>
> **Explicitly not licensed:** "systematic review", "systematic mapping study", "scoping review (JBI/PRISMA-ScR)", "meta-analysis", or any phrasing implying protocol-driven, database-based, multi-screener source selection.

---

## 2. Why not a systematic review or systematic mapping

A systematic claim requires a reproducible *search*, not merely a reproducible *extraction*. This project has the second and not the first.

| Systematic-review requirement | Status | Evidence |
|---|---|---|
| Databases searched, named and dated | ✗ | `literature_search_log.md` §1 — general web search only, no Scopus / WoS / IEEE Xplore / Compendex |
| Exact search strings with hit counts | partial — strings recorded, **counts not obtainable** from the interface | `literature_search_log.md` §3 |
| Search date | ✓ 17 Aug 2026 | — |
| Pre-specified protocol | ✗ | corpus was assembled by convenience before this audit |
| Inclusion / exclusion criteria applied prospectively | ✗ (defined retrospectively, §3 below) | — |
| Duplicate handling | ✓ | `source_inventory.md` §4 — TIS-25/TIS-25-AAM, IG-1, IG-20, IG-22 |
| Screening procedure with counts (PRISMA flow) | ✗ | — |
| Backward citation searching | partial | reference lists of RAN-25 and MOR-26 inspected; not exhaustive |
| Forward citation searching | ✗ | **the highest-value missing step** |
| Two independent screeners | ✗ single AI-assisted analyst | — |
| Risk-of-bias / quality appraisal instrument | ✓ **substitute present** — the evidence ladder L1–L7 in `evidence_strength_matrix.md` functions as a domain-appropriate appraisal instrument | — |

Calling this a systematic review would be a methodological misstatement of exactly the kind the manuscript criticises in others. It would also be the easiest thing for a reviewer to reject.

## 3. What *is* already satisfied — and is worth claiming

The project genuinely possesses the extraction-side machinery of a rigorous review, and the manuscript should say so plainly rather than overreaching:

1. **A canonical source inventory** with filename audit, duplicate mapping and independence groups (`source_inventory.md`). Three duplicate/lineage pairs were identified and collapsed; two filenames were found to be wrong or missing.
2. **A pre-declared architecture taxonomy** (A1–A7) with explicit transfer rules, applied uniformly (`architecture_taxonomy.md`).
3. **A claim-level evidence matrix** with locators, evidence types, conditions, caveats and manuscript-safe wording; every corpus row verified against the original PDF during this audit (`evidence_matrix.md`).
4. **A timing register** in which every value carries a start event, an end event, a measured/simulated/projected flag, and a comparability class, with an explicit pooling prohibition (`evidence_matrix.md` Part B, Part C).
5. **A stage-resolved extraction template** (S1–S10) applied to every relevant source (`adaptation_chain_matrix.md`).
6. **An evidence-strength appraisal** (L1–L7) applied to eighteen named capabilities (`evidence_strength_matrix.md`).
7. **An independence audit** preventing double counting (`audits/independence_audit.md`).
8. **An absence-claim register** requiring each absence statement to be justified by the search method that supports it (`absence_claims.md`).

Retrospective inclusion criteria, stated for transparency (they describe what the corpus *is*, not a prospective filter):
- **Included:** peer-reviewed articles, preprints and author manuscripts concerning (a) FIM system modelling, (b) flexible or conformal reflective/transmissive metasurface hardware, (c) programmable mechanical surface actuation, (d) electronically reconfigurable RIS hardware with reported timing or power, (e) high-mobility channel estimation for reconfigurable surfaces, (f) reviews of any of the above.
- **Excluded:** sources with no wireless, electromagnetic or mechanical-actuation content; duplicate versions (retained for lineage, not counted as evidence).

**Recommended methods sentence for the manuscript:**
> "This is a structured critical review. Sources were assembled by convenience rather than by a protocol-driven database search; we therefore make no systematic-review claim and bound all absence statements to the reviewed set. One targeted exception is documented: a reproducible forward citation search of the three primary hardware sources, performed through the OpenAlex citation graph, which screened 262 citing works and read 13 of the 20 relevant system papers in full, the remainder being inaccessible. That search supports the traceability finding of Section 6.5 and nothing else. Extraction, by contrast, followed a fixed protocol: a seven-class architecture taxonomy, a ten-stage adaptation-chain template, a seven-level evidence ladder, and a timing register requiring an explicit start event, end event and comparability class for every reported value."

## 4. Consequences for title and contribution

The article-type verdict interacts with the novelty verdict (`novelty_boundary.md` §1). Two-timescale FIM control is already published, so the title must not present it as a destination.

| Candidate title | Verdict |
|---|---|
| *From Instantaneous Shape Optimization to Two-Timescale Control: A Hardware-Validation Review of Flexible Intelligent Metasurfaces for High-Mobility ISAC* | ✗ **reject** — implies the two-timescale move is the contribution; pre-empted by Kumar et al. (arXiv:2512.23045), arXiv:2601.15471, YAN-25 (E-12) and MA-26 (E-41/E-42) |
| **✅ *Flexible Intelligent Metasurfaces for High-Mobility ISAC: Hardware Evidence, Adaptation Timescales, and Validation Gaps*** | ✓ **ADOPTED 17 August 2026; re-checked against the v0.20 structure 18 August 2026 and retained** — conventional, descriptive, and still accurate: the title's three clauses map onto **§6 hardware evidence**, **§7 adaptation timescales**, and **§9 validation gaps**. (Under the v0.14 ten-section outline these were §5, §6 and §7; the restructuring renumbered them without disturbing the mapping.) |
| *What Has Actually Been Measured? Adaptation Timescales and Hardware Evidence for Flexible Intelligent Metasurfaces in High-Mobility ISAC* | ○ **recorded alternative, not in use** — foregrounds the auditing contribution, but the interrogative form makes a rhetorical promise the manuscript then has to defend, and it reads as a polemic against the field rather than as a review of it |

**Decision.** The conventional form is adopted and is now in `manuscript/01_introduction.md`. It was checked against the manuscript architecture for accuracy before adoption, and no section makes it misleading; if anything it under-promises, since it does not signal the traceability audit (N3), which is the strongest contribution. That is an acceptable trade — a title that under-promises is safer for a first submission than one that invites the reader to grade the manuscript against a rhetorical question. The alternative is retained here for the record and may be reconsidered at a venue that favours discursive titles.

**Both are safe on the novelty boundary**: neither claims two-timescale or statistical-CSI FIM control, and the rejected working title is not to be reinstated (`novelty_boundary.md` §3 item 5).

## 5. Venue orientation

The contribution is an evidence audit, not a new technique. That suits:
- a **survey/tutorial-oriented venue** (IEEE Open Journal of the Communications Society; IEEE Access) — but note both TIS-25 and MA-26 already occupy adjacent survey space, so the narrow framing must be evident from the abstract;
- a **magazine** format (IEEE Communications Magazine, IEEE Wireless Communications) if compressed — the traceability finding N3 and the reporting framework N4 are magazine-shaped, and the length would suit;
- a **workshop or conference** track on RIS/metasurface hardware, as a fast route to supervisor-level and community feedback before a longer version.

**Not** a mechanism/materials venue: the manuscript contributes no new hardware.

## 6. CST inclusion gate — verdict

> **Exclude the CST–Python study from this manuscript.**

Applying the gate criteria in the project brief §16:

| Criterion | Status |
|---|---|
| CST methodology validated | ✗ — no CST results existed when this assessment was made (August 2026) |
| Result relevant to the review's central argument | ✗ — the central question is *when* operations must occur and *what has been measured*. The CST study asks how much beam degradation is attributable to curvature, oblique incidence and phase quantisation on a **static** aperture. It contains no time variable. |
| Result provides an interpretable contribution to this argument | ✗ |
| Original technical work suits the selected article type | ✗ — a structured critical review does not require, and a reviewer would not expect, an embedded unrelated full-wave study |
| Prior art already occupies the CST question | largely — PEP-26 (E-54), TAG-20 (E-50), LU-25/LU-26 (E-52/E-53), CHE-26 (E-55) cover fixed-curvature conformal RIS, phase-quantisation scaling and bending tolerance |

**Disposition.** Keep the CST–Python work as a separate technical project and a candidate standalone paper. Its baseline source situation has, in fact, improved during this audit: **HAR-20 is now present in the corpus** (previously logged as missing item M01), and a previously unidentified follow-up, **HAR-22** (`ars-19-215-2022.pdf`), provides array-level measured validation of the same element lineage. That strengthens the CST project on its own terms and is recorded in `unresolved_questions.md`.

The one legitimate connection to this review — that electronic programming can compensate part of a geometry-induced electromagnetic degradation — is already established by measured hardware (LI-25 E-25, LU-26 E-53) and needs no simulation from us.

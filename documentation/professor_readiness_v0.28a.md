# Professor-readiness audit — manuscript v0.28 → v0.28a

**22 August 2026.** A narrow pre-send pass. The seven-section structure, the scientific substance and every frozen result are unchanged; C1, C3, C4 and G1–G4 were recomputed and are identical. v0.28 is preserved at `Documentation/archive/manuscript_v0.28/` and at commit `d850b04`.

## 1. Errors fixed

| | What was wrong | Fix |
|---|---|---|
| **Figure order** | Figures appeared as 1, 3, 2, 4. The timing landscape (§4.5) carried number 3 and the adaptation-chain map (§4.6) carried number 2. | The two were swapped so numbering follows first appearance. Captions, both in-text references, the two PDF/PNG file pairs, `make_figures.py`, the exporter's `FIGFILE` map and the mirror whitelist in `sync_review_repo.py` were all updated together; the figures themselves were regenerated and are otherwise byte-identical in content. |
| **Stale cross-reference inside a figure** | Figure 4's in-image footnote read "G1–G4 name the missing interval (**Table 8**)". Table 8 was v0.27b numbering; the table is now Table 4. This was baked into the rendered image, so no text search of the manuscript would have found it. | Corrected in `make_figures.py` and re-rendered. All four figure PDFs were then searched for embedded cross-references; no other stale one exists. |
| **Apparent self-contradiction, §4.2** | The section reported <0.1 ms per element and <10 ms per tile, then said quantified values across reviewed electronic mechanisms "run from approximately 15 ms to tens of seconds" with "the semiconductor end of the range … no number at all". | Rewritten to name the two quantity types the register already separates. The [4] figures are **controller write** times in the sense of Supplementary Table S2 — command issued to control state written. The [5] figures are **material transitions** of the tuning layer. No number changed, and no semiconductor transition time is inferred: the text states explicitly that none was measured in the reviewed set, that nothing supports an inference that semiconductor transitions are slow, and that the two values do not belong on one scale. |
| **Downstream instance of the same conflation** | §4.6's capability list and the conclusion both said "fast electronic phase reconfiguration … has been measured", which asserts on the material axis what was measured on the controller axis. | Both now read "timed at the controller". |
| **Unsupported cost claim** | The conclusion read "The most valuable next experimental step is also the cheapest", and §6.3 ranked three experiments "by what it would cost to close them". No cost study exists. | Conclusion: "Among the gaps identified, timing the recalibration experiment that has already been performed appears to require the least new hardware." §6.3 now orders the experiments "by how much new hardware each appears to require, which is a judgement about experimental prerequisites and not the result of a cost study; we have performed none." The word *cheap* no longer appears in the manuscript. |
| **False claim in the reference-list header** | The header stated the entries are "numbered in order of first appearance". They are not: the v0.28 restructure moved several first citations, and the order now breaks at [19]→[4], [26]→[12] and [18]→[7]. | Corrected rather than renumbered. The header now states that the numbering is the project's stable source numbering, that the registers and supplement are keyed to it, and that renumbering into citation order is a submission-time step once a venue is chosen. |
| **`verify_professor_export.py` was stale from v0.23** | It opened `Professor_Review_Draft_v0.23.docx`, which no longer exists, and asserted 12 sections and 9 tables. It crashed before reaching any DOCX or PDF check, so **the v0.28 export was never verified against it**. | Filenames now derive from the exporter so they cannot drift; assertions corrected to 7 sections, 5 numbered tables, 6 DOCX tables. New assertions were added for figure and table numbers ascending in order of appearance, figure image filenames matching their numbers, and the heading and caption styles. Suite now reports **47 passed, 0 failed**. |

## 2. Passages materially shortened

| Passage | Before | After | What moved or went |
|---|---|---|---|
| **§5.2**, the reach-of-the-practice paragraph | 316 words | 219 | The author-disjointness case detail, the connected-network reasoning, the residual-risk count for the seven unread studies and the [34] negative case were reduced to a clause and a pointer. All of it already stands in full in **S8.3** and **S8.4**; nothing was deleted from the record. Kept in main text: the 13-of-20 access bound, five instances in four studies, the connected co-authorship network, the preprint-to-journal insertion, the lower-bound statement and the no-prevalence statement. Both author-disjoint restrained cases are still cited ([12], [34]) so no reference lost its main-text home. |
| **§7 Conclusion** | 844 words | **650** | Now does only the five required things: answers the question, states the gap, states the contribution, names the next measurement, states the limitation. The individual timing examples were dropped — the conclusion now carries **no numeric timing value at all** — and the re-proof of §5 went with them. |

Everything else was left alone. Main-text prose is **13 130 words** (was 13 211), total **15 399** (was 15 480); no global length reduction was attempted.

## 3. Wording weakened, and why

- *"the cheapest"* → *"appears to require the least new hardware"*, with the ordering explicitly labelled a judgement rather than a costing. No cost study supports a cost claim.
- *"fast electronic phase reconfiguration … has been measured"* → *"timed at the controller"*, twice. What was measured is a write time, not a device transition.
- *"A widely cited 16.76 ms figure"* (professor brief) → *"A 16.76 ms figure quoted from this literature"*. "Widely cited" is a prevalence claim, and the manuscript makes none.
- *"it is the assumption with the least measurement behind it"* (brief) → prefixed *"within the reviewed set"*.
- *"The remedy … is cheap"* (§5.2) → the cost clause removed.

Nothing was weakened in the other direction, and no numeric value, source attribution, evidence status, architecture definition or corpus boundary was changed anywhere in this pass.

## 4. Tone pass

Ten constructions were replaced, all of them in the categories named in the brief. The named examples went: *"The natural move is to look up… the literature appears to supply the number, and it does not"* → a plain statement that the reported intervals do not describe the same quantity; *"The chain, stated once:"* → *"The resulting chain runs as follows."*; *"an unmeasured quantity has no value rather than a bad one"* → *"these intervals are unquantified rather than quantified and found wanting."* Also removed: *"a table presupposing its own answer would be worthless"*, *"its value stands or falls on the accuracy of its citations"*, *"the content of a category error"*, *"That last item matters most and costs least"*, *"we have no standing to"*, *"misdescribing a method is the kind of failure this manuscript examines in others"*, and the §4.4 heading *"the capability without the clock"*. Body-text bold spans fell from 34 to **21**; em dashes from 5.4 to **4.4 per 1 000 prose words**.

## 5. Formatting and cross-reference fixes

- **Real Word styles.** Headings were hand-formatted Normal paragraphs. The exporter now defines and applies **Heading 1**, **Heading 2**, **Heading 3**, **Caption** and a derived **Table Caption** style, redefined to the body face so Word's blue Calibri defaults do not appear. The DOCX now yields a working navigation pane and table of contents, and can be retargeted to a journal template by editing five styles. Verified: 9 Heading 1, 16 Heading 2, 5 Table Caption, 4 Caption, and every figure and table caption carries the right one.
- **Landscape spacing.** The PDF emitter switched to landscape for a wide table and stayed there until the next heading, stranding the rest of the subsection on a landscape page — Figure 1 and three paragraphs of §3.1 sat on a page that was 55 % blank. It now returns to portrait as soon as the table is placed, matching what the DOCX emitter already did. Manuscript is **27 pages** (was 28), with two landscape pages, each holding one table.
- **Table header clipping.** Table 2's "Arch." header broke across two lines. The column-width floor was estimated from character counts, which cannot know that a bold 6.2 pt "Arch." is wider than four plain digits. It now measures real glyph widths from the font metrics and redistributes width from columns with slack. No table is clipped in any of the three documents.
- **DOCX table width.** Tables are now pinned to 100 % of the text width, so Word cannot lay an autofit table wider than the frame.
- **Figure legibility.** In Figure 2 the "300 ms" and "650 ms" labels touched, because three markers within half a decade were staggered across only two heights. The third label now sits below the lane. No other overlap was found at 420 dpi.
- **Footers** are consistent across all five DOCX sections and every PDF page, portrait and landscape alike.
- **Documentation cross-references** to the renumbered figures were updated in `manuscript_argument_map.md` and `timescale_matrix.md`. `absence_claims.md` is a dated sweep record, so its numbering warning was extended to figures rather than the record being rewritten.

## 6. References and supplement

The shared-bibliography convention is now stated on the page rather than assumed. The manuscript's reference header says one bibliography serves both documents and that [33] is cited in the supplement only; the supplement's header says its bracketed numbers, table numbers and figure numbers are the manuscript's and that it carries no separate list. Checked mechanically: **34 entries, numbered 1–34 with no gaps; every in-text citation in the manuscript and the supplement resolves; no entry is uncited; nothing is cited that is not defined.**

## 7. Final counts

| | v0.28 | v0.28a |
|---|---|---|
| Main-text prose / total | 13 211 / 15 480 | **13 130 / 15 399** |
| Conclusion | 844 | **650** |
| Abstract | 249 | 249 (reviewed, unchanged) |
| Sections / subsections | 7 / 16 | 7 / 16 |
| Manuscript pages | 28 | **27** |
| Brief / supplement pages | 2 / 15 | 2 / 15 |
| Body-text bold spans | 34 | **21** |
| Em dashes per 1 000 prose words | 5.4 | **4.4** |
| Tables / figures | 5 / 4 | 5 / 4 |

`check_s11_consistency.py` clean across 48 documents and 19 tools · `validate_public_snapshot.py` 33 passed, 0 failed · `verify_professor_export.py` 47 passed, 0 failed. C1 max Q = 6 (BAI-22, LI-25), max `·T` = 4 (BAI-22), max `·T`+`·(T)` = 6 (LI-25). C3 306 → 262 → 65 → 24 → 20 → 13 read / 7 unread, 4 propagation, 9 no-timing.

Adversarial sweep: *cheap*, *cheapest* — absent. *infeasible* — one occurrence, inside a denial. *first* — four occurrences, none a priority claim. *never*, *none*, *only*, *no source*, *no platform* — every occurrence bounded to the reviewed set, to a named table, or to a stated rule. Each of the eleven headline timing values has one primary explanatory location; the conclusion now recycles none of them.

## 8. Remaining items for Prof. Mojtaba's judgement

1. **Figure 1's placement.** It is the architecture–evidence map and sits in §3.1, where the taxonomy is established, rather than in §5.3 where the gap is stated. §5.3 refers back to it without re-proving it. Moving it is a one-line change; carried over unresolved from v0.28.
2. **Table 3 occupies a full portrait page**, so the page before it is three-quarters blank. Splitting it across two pages or rotating it to landscape are both available; a full-page table is the more conventional presentation, so it was left.
3. **The closest-review comparison is prose, not a table** (§1), to stay inside the five-table target. The full matrix is in `novelty_boundary.md` §2 if a table is preferred.
4. **Reference numbering is not in citation order** and will need renumbering at submission. This is deliberate: the registers, the evidence matrix and every supplementary table are keyed to the current numbers, so renumbering before the structure is settled would invalidate the audit trail.
5. **Section 4 is still the longest section** at 3 528 prose words. Further compression means thinning the per-platform evidence, which is the part the argument rests on.
6. **The DOCX was audited structurally, not visually rendered.** No Word or LibreOffice renderer is available on this machine, so the DOCX was checked through its XML — styles, section orientation, footers, table and image counts, reference resolution — while the **PDF was inspected page by page at 95 dpi, with the figures re-examined at 420 dpi**. Both documents are emitted from one parsed block stream, so their content cannot diverge, but the DOCX page breaks have not been seen.
7. **Extraction remains single-reviewer.** Unchanged from v0.28 and stated in §6.4; a duplicated extraction is still the single methodological improvement most likely to change a cell.

The manuscript is a working draft for academic review. It is not submission-ready, and no venue has been selected.

# Journalization report — manuscript v0.27b → v0.28

**22 August 2026.** A structural and editorial revision. No scientific finding was added, removed or changed; the frozen results C1–C4 and G1–G4 are byte-for-byte the same claims, recomputed from the same registers. What changed is the article's shape: audit machinery that dominated the main text has been moved to the supplement, and the argument now runs once through seven sections instead of being re-proved across twelve.

v0.27b is preserved intact at `Documentation/archive/manuscript_v0.27b/` and at commit `4e5c89e`.

## 1–4. Length and section count

| | v0.27b | v0.28 | change |
|---|---|---|---|
| Main-manuscript prose words | 18 713 | **13 211** | **−29.4 %** |
| Main-manuscript table words | 3 955 | 2 269 | −42.6 % |
| Main-manuscript total | 22 668 | **15 480** | **−31.7 %** |
| Rendered manuscript pages | 41 | **27** | −34 % |
| Numbered sections | 12 | **7** | −5 |
| Numbered subsections | 50 | **16** | −34 |
| Main tables | 8 | **5** | −3 |
| Main figures | 4 | **4** | unchanged |
| Supplement words | 4 551 | **7 729** | +70 % |
| Supplement pages | 8 | **15** | +7 |
| Prose bold spans (body text) | 241 | **34** | **−86 %** |
| Em dashes per 1 000 words | 10.5 | **5.4** | −49 % |
| Brief pages | 2 | **2** | unchanged |
| References | 34 | **34** | unchanged |

Prose word count is measured excluding table rows, by the standing project method. The 13 211 figure sits inside the 11 000–14 000 editorial target.

## 5. Old section → new location

| v0.27b | Disposition | v0.28 location |
|---|---|---|
| 1.1 A degree of freedom that has to be actuated | kept | §1 |
| 1.2 Why high mobility turns an omission into a question | kept, merged with old 4.1 | §1 |
| 1.3 Why one reported response time cannot answer it | compressed from four worked examples to a single paragraph | §1 |
| 1.4 What the adjacent reviews already establish | kept as prose (see §7 below) | §1 |
| 1.5 The question, and how it is answered | merged into the contributions | §1 |
| 1.6 Contributions C1–C4 | kept verbatim | §1 |
| 2.1 Article type | kept | §2 |
| 2.2 Corpus | kept, version-of-record narrative moved out | §2; narrative → S3 |
| 2.3 Searches | compressed; retrieval mechanics moved out | §2; mechanics → S5 |
| 2.4 Extraction protocol (six numbered items) | **moved to supplement**, replaced by four stated principles | §2 (principles); scheme → **S6** |
| 2.5 What follows from the method | merged | §2, §6.4 |
| 3.1 Why the taxonomy comes first + Table 1 | kept; Table 1 lost one column ("Shape sensed", now in prose) | §3.1, Table 1 |
| 3.2 A1 is a model class | kept | §3.1 |
| 3.3 The realised flexible apertures invert the control problem | kept | §3.1 |
| 3.4 The platforms that command a shape have no radio | compressed to one paragraph | §3.1 |
| 3.5 Fixed-curvature conformal design | compressed from six per-source sentences to one paragraph, all citations retained | §3.1 |
| 3.6 Transfer rules (seven) | reduced to four; rules 5 and 6 restated rule 1, rule 7 moved to the evidence-discipline principles | §3.1, §2 |
| 3.7 The shape of the gap + Figure 1 | kept in §3 (not moved to §5, see §10 below); §5 refers back without re-proving | §3.1 |
| 4.1 Three quantities that must not be collapsed | merged into the introduction | §1 |
| 4.2 The states are plural + Table 2 | **table moved to supplement**; one paragraph retained | §3.3; table → **S7** |
| 4.3 The literature itself offers the slow-geometry reading | kept | §3.3 |
| 4.4 Overhead accrues before the actuator moves | compressed | §3.3 |
| 4.5 What Section 4 establishes | **deleted as redundant** — a section summary restating what precedes it | — |
| 5.1 Why decompose at all + stage table | kept | §3.2 |
| 5.2 Table 3, per-source stage coding | **moved to supplement** | → **S6.3** |
| 5.3 Coverage of the chain | kept, compressed | §4.6 |
| 5.4 The measured stages sit on incompatible platforms | merged with 5.3; four bullets restating table rows became one sentence | §4.6 |
| 5.5 The system papers do not model S5–S9 | merged; the footnote-premise analysis was duplicated in old §8.2 | §3.2, §5.2 |
| 5.6 Where a loop is closed, perception is what binds | compressed | §4.3 |
| 5.7 Two quantities that nothing reports | merged into G2 and G3 | §5.3 |
| 6.1 The quantity types | reduced to two sentences; the table was already in S2 | §4 preamble |
| 6.2 Flexible programmable reflective apertures | kept — the single full description of [6] | §4.1 |
| 6.3 Rigid electronically reconfigurable surfaces | kept — the single full description of [4], [5] | §4.2 |
| 6.4 Commanded mechanical morphing | kept — the single full description of [7], [8] | §4.3 |
| 6.5 Flexible active arrays | kept — the single full description of [20] | §4.4 |
| 6.6 Table 4, timing register | kept, trimmed from 20 rows to 15 | §4.5, **Table 2** |
| 6.7 What the hardware evidence establishes | merged with old 9.1, which restated it | §4.6, §5.3 |
| 7.1 The one comparison the evidence permits + Figure 3 | kept | §4.5 |
| 7.2 What the mechanical measurements do and do not establish | **deleted as redundant** — re-proved §6.4 with the same numbers; the substitution mechanism it illustrated was kept | §4.3 (one sentence) |
| 7.3 Why "fast electronics, slow mechanics" needs qualification | kept, compressed | §4.5 |
| 7.4 Why a latency is a property of an object | merged — third occurrence of the same example | §4.2, §6.2 |
| 7.5 Table 5, stage-by-stage | kept | §5.1, **Table 3** |
| 8.1–8.3 What is audited; premises 1 and 2 | kept, compressed | §5.2 |
| 8.4 Premise 3, the tabulated morphing periods | kept nearly in full — the strongest example | §5.2 |
| 8.5 Forward citation search + Table 6 | **moved to supplement**; ~250 words of finding retained | §5.2; inventory → **S8** |
| 8.6 Why this happens, and what would prevent it | kept, compressed | §5.2 |
| 9.1 What the gap is not | merged with 6.7 | §5.3 |
| 9.2 The gap + Table 7 + G1–G4 | kept | §5.3, **Table 4** |
| 9.3 The deeper gap is structural + Figure 4 | kept | §5.3 |
| 9.4 Ranked by what it would cost to close | merged with old 11.3, which stated the same three experiments | §6.3 |
| 9.5 What this does not show | merged | §5.3, §7 |
| 10.1 Definitions, not thresholds | kept, compressed | §6.1 |
| 10.2 Table 8, ~30 reporting fields | **compressed to 10 fields**; full checklist to supplement | §6.1, **Table 5**; full → **S4** |
| 10.3 The minimum assumption declaration | kept, converted from a numbered list to a paragraph | §6.1 |
| 10.4 Standing and scope | reduced to two sentences | §6.1 |
| 11.1 The answer, stated plainly | merged — restated old 7.5 | §5.1 |
| 11.2 What follows for system modelling | kept | §6.2 |
| 11.3 What follows for hardware work | merged with old 9.4 | §6.3 |
| 11.4 Limitations | kept, compressed | §6.4 |
| 11.5 What this review does not establish | merged | §7 |
| 12 Conclusion | **rewritten** as a five-paragraph journal conclusion; the old four-item list duplicated 11.3 and 9.4 | §7 |

## 6. Tables and figures moved or removed

**Renumbered:** old T1 → T1 · old T4 → T2 · old T5 → T3 · old T7 → T4 · old T8 → T5 (compressed).
**Moved to supplement:** old T2 (states tracked) → **S7** · old T3 (per-source stage coding) → **S6.3** · old T6 (propagation inventory) → **S8.2** · old T8's full field list → **S4**.
**Removed:** none. Every row of every moved table survives in the supplement.
**Figures:** all four retained unchanged, with their source files and captions; only Figure 2's caption was shortened. No figure was regenerated, so no figure content changed.

New supplement sections created to receive the moved material: **S6** (coding scheme, evidence ladder, per-source matrix, the counts), **S7** (states tracked), **S8** (propagation inventory, observation window, opposite pattern). A new `tools/build_supplement_combined.py` assembles S1–S8 in order, so the combined file can no longer drift from its parts.

## 7. Major redundancies eliminated

Each finding now has one primary location and at most one short callback.

| Finding | Was stated in | Now established in |
|---|---|---|
| The 16.76 ms interval is a partial electronic compensation loop | §1.3, §4.2, §5.3, §6.2, §7.3, §9.2, §11.2, §12 (8 sections) | §4.1, with callbacks in §4.5, §4.6, §7 |
| Element ≠ tile ≠ surface ≠ settling | §1.3, §5.3, §6.3, §6.4, §7.2, §7.4, §11.2, §12 | §4.2, callback in §7 |
| Commanded-geometry platforms have no RF layer | §3.4, §5.4, §6.4, §7.5, §9.2, §9.3, §12 | §3.1 (claim), §4.3 (evidence) |
| Calibration demonstrated but untimed | §4.2, §5.7, §6.5, §7.5, §9.2, §11.3, §12 | §4.4, callback in §5.3 (G3) |
| The empty intersection | §3.7, §5.4, §7.5, §9.2, §9.3, §11.5, §12 | §3.1 with Figure 1, restated once as a measurement question in §5.3 |
| Two-timescale control is prior art | §1.4, §4.3, §11.1, §12 | §1, callback in §7 |
| ≈300 ms full-surface morph | 6 sections | §4.3, used again only where the substitution argument needs it |
| The three experiments that would close the gap | §9.4, §11.3, §12 | §6.3, one sentence in §7 |

Individual timing values now appear in at most four files rather than eight, and every remaining occurrence was checked against the question "does this occurrence do work the earlier one did not?"

## 8. Scientific wording that had to be weakened

**None.** No claim was weakened to fit the compression. Four claims were *strengthened* in the direction of corpus-bounding, which the brief required:

| Was | Now | Why |
|---|---|---|
| "What no source measures is the intersection" | "What no reviewed source measures…" | unbounded negative |
| "the four measurements which would settle the matter have not been made" | "within the reviewed set the four measurements…" | unbounded negative |
| "the combination has not been built and timed" | "within the reviewed set the combination has not been built and timed" | unbounded negative |
| "It shows that they have not been measured" | "It shows that within the reviewed set they have not been measured" | unbounded negative |

In the professor brief, "The adaptation chain has not been timed end to end on any one platform" became "Within the reviewed set, no platform times the adaptation chain end to end", and "What has not been demonstrated is both on one object" became "Within the reviewed set, we did not identify a platform combining commanded geometry with measured RF performance on the same object". The brief's traceability paragraph now carries its 13-of-20 bound explicitly, which it previously did not.

Two rhetorical constructions were removed without touching the underlying claim: "the single most consequential fact in the taxonomy" (§3.3) and "the single most useful set of numbers in the corpus" (§6.4).

## 9. Claims whose evidence became uncertain during revision

**None.** A token-level numeric diff of the v0.27b and v0.28 main texts was run to confirm this: **no numeric quantity appears in v0.28 that was not in v0.27b**, and of the nine that left the main text, three moved to the supplement and five were incidental detail carrying no claim (a second carrier bound for [26], a receiver dimension for [20], a bandwidth and array size from the operating-point list whose locator survives in Table 2, and a duplicate 19 kHz rounding of the 19.4 kHz figure). The ninth was a real loss and was restored: the observation that the element response cited downstream as evidence of feasibility (below 0.07 s) and the demonstrated closed-loop convergence (≈150 s) differ by a factor of roughly two thousand, which the reviewed system literature quotes neither side of. It is now in §4.3.

**None.** Every load-bearing number was re-verified against the canonical registers during the move. The frozen results are unchanged and were recomputed, not copied:

- **C1** — max quantitatively evidenced stages 6 (BAI-22, LI-25); max measured stage durations `·T` **4** (BAI-22 alone); max `·T`+`·(T)` **6** (LI-25 alone). Recomputed by `tools/c1_stage_counts.py`.
- **C3** — 306 records → 262 works → 65 stage-1 → 24 stage-2 records → 20 studies → 13 read / 7 unread; 4 propagation, 9 no-timing. Recomputed by `tools/s11_counts.py` via the regenerated S5.
- **G1–G4** — unchanged in wording and in scope.

One bookkeeping consequence of the move is worth recording: reference **[33]** is now cited only in the supplement (the S5 study register), because the traceability inventory that cited it in the main text moved to S8. It remains in the shared numbered bibliography, which the supplement uses. References [27], [28], [31] and [32] would have been left in the same position; they were restored to the main text instead — [27]/[28] in the list of platforms plotted in Figure 1, and [31]/[32] in §5.2's identification of the four propagating studies.

## 10. Remaining issues requiring human or professor judgement

1. **Figure 1's placement.** The brief asked for the architecture–evidence map to be a central figure in the validation-gap section. It was kept in §3 instead, because the brief's own quality gate asks whether a reader can state the contribution "after reading the abstract, introduction and Figure 1" — which requires Figure 1 to be early. §5.3 refers back to the empty cell without re-proving it. If the professor prefers the map alongside G1–G4, moving it is a one-line change and would renumber the figures.
2. **The closest-review comparison is prose, not a table.** The brief allowed either. Prose was kept because a sixth main table would have exceeded the 4–5 table target for no gain; the comparison is one paragraph in §1. The full comparison matrix already exists in `novelty_boundary.md` §2 and could be promoted if the professor wants it visible.
3. **§4 remains the longest section** at 3 362 prose words. It is the core evidence section and holds the only full description of each of the six hardware platforms, so it was not compressed further. If the manuscript must shrink again, §4.1's application-level paragraph and §4.2's power figures are the first candidates, and both would lose real content.
4. **Single-reviewer extraction is unchanged** and remains the most consequential methodological limitation (§6.4). A duplicated extraction is still the improvement most likely to change a cell.
5. **The article type and novelty boundary are untouched.** The research question, the four contributions, the architecture definitions, every numerical value, every source attribution and the corpus boundary are identical to v0.27b. Nothing in §22 of the revision brief's protected list was changed.
6. **Not submission-ready.** No venue has been selected, page count depends on the eventual template, and the manuscript should not be described as ready for submission.

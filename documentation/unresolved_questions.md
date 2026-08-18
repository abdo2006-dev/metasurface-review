# Unresolved Questions

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.1 · 18 August 2026 (freeze consistency gate; see `CHANGELOG.md` v1.5)
Ordered by consequence. Items marked **BLOCKING** must be resolved before submission; the manuscript is coherent without them but a specific claim would have to be weakened or withdrawn.

---

## ✅ RESOLVED (17 August 2026)

### ✅ U1 — Fan Li supplementary information — **RETRIEVED AND READ**
Archived as `23_FanLi_FISP_Supplementary_Information.pdf` (33 pp.) and `23B_FanLi_FISP_Peer_Review_File.pdf` (49 pp.). Supplementary Note 6 read in full.

**What it settled:** the component decomposition (T1 = 4 ms thread-timing average, T2 ≈ 2 ms, T3 = 5.25 ms by oscilloscope), the reason 16.76 ms exceeds the 11.25 ms sum (32 channels over RS-232 at 115 200 bps), a 60 Hz deformation-rate limit, and — the substantive new finding — **a second, independent end-to-end experiment measuring 16.7 ms from sensor trigger to stabilised RF output**. Note 7 confirmed that the mechanical platform is a manually-adjusted fulcrum fixture with no actuation timing, which vindicates the A3 classification.

**What it did not settle:** no repetition count, sample size or uncertainty is reported for any headline interval. This is now recorded as absence claim A15 and as finding F4 in `latency_definition_audit.md`.

**Consequence:** T-GAP-03 was narrowed, gap G4 was rewritten, and capability C14 was upgraded to L5/L6 with a new C14b for the remaining gap.

### ✅ U2 — Bai et al. Extended Data / Supplementary Information — **RETRIEVED AND SEARCHED**
Archived as `19S_Bai_Shape_Morphing_Supplementary_Information.pdf` (71 pp.) and `19SB_Bai_Shape_Morphing_Peer_Review_File.pdf` (28 pp.); the Extended Data figures were already in the main-text PDF.

**What it settled:** no value at or near 10 ms exists anywhere in the complete package, and the 60 fps instrument used for the fastest mechanical figure could not have resolved one. CA-02's evidential basis is much stronger. **The verdict deliberately did not change** — it remains a discrepancy requiring verification, because we can observe the tabulating authors' table but not their derivation.

**What it also did:** it **retracted a derived value of our own** (≈1.25–3.75 s convergence), replacing it with the source's directly-stated ≈2.5 min. See `audits/citation_audit.md` C5. This is disclosed in the manuscript at §6.2 and §9.4 rather than corrected silently.

---

## BLOCKING

> **U3 is resolved and retained here for its audit trail; it is no longer a blocker.** The live blockers in this section are those below it.

### ✅ U3 — Forward citation search of the three primary hardware sources — **PERFORMED 18 August 2026**
*Why it blocked (historical):* the traceability finding rested on **two papers that share authors** (see `independence_audit.md` I-FIX-2), and without a forward search we could not say whether the substituted timing figures were an isolated occurrence or a propagating convention. **This is now answered — and the answer did not license a stronger article-type claim.** The search widened the case base from two papers to four and simultaneously established that the independence basis did not widen at all, so §6.5 stays narrowly framed and C3 stays at **Level A**.
**✅ DONE 18 August 2026 — result: four instances, zero author-disjoint groups.** Method, queries and screening counts are in `literature_search_log.md` **S11**; the cases are `evidence_matrix.md` **E-FP-01 … E-FP-05**, the counterexamples **E-FP-C1/C2**. Summary: OpenAlex cited-by retrieval for all three seeds → 306 records → **262 unique works** → 65 wireless-relevant → 24 stage-2 records → **20 distinct system studies** → **13 full texts obtained** (7 paywalled and unread). *(Counts corrected in v0.22: the stage-1 figure was 64 before the screening expression was written out in full, and the study count passed through an incorrect 21 in v0.21 when a conference/journal pair was left uncollapsed.)*

**What it found.** (i) The tabulation of 30 ms / 10 ms as "Morphing Period" is confirmed verbatim, together with two escalations by the same paper — that morphing "reaches 10 ms … and aligns with typical channel coherence blocks", and that FIM deformation runs "on the order of milliseconds (with the fastest reaching **1 ms**)", a figure **smaller than every entry in that paper's own table** and present in **no** primary source. (ii) A second team describes the prototypes as showing "shape-switching times on the order of milliseconds", citing all three primaries including the one whose geometry is static throughout its timed experiment. (iii) A millisecond assertion appears in the **journal** version of the foundational downlink study and is **absent from its conference version** — the same add-on-at-journal-stage pattern as RAN-25's Remark.

**What it did NOT find, and this is decisive for how C3 is worded.** **No author-disjoint publication group reproduces the practice.** Every instance shares an author with the corpus FIM lineage; 14 of the 20 system studies do, 4 are disjoint from it, and 2 are disjoint from both it and all three primary sources. It also found **no traceable derivation of the 10 ms value in any full text inspected**, and **no paper reproducing LI-25's 16.76 ms in any full text inspected**.

**Residual limitation (now the live one).** 7 of 20 studies are paywalled, so all counts are **lower bounds**. Repeating S11 with IEEE Xplore access is the remaining upgrade path — but it is an upgrade to precision, not a blocker on C3, which is worded at Level A regardless.

⚠ **What it could and could not deliver — written 17 Aug 2026, and borne out exactly on 18 Aug.** The caveat predicted that the search would quantify propagation but would **not** necessarily resolve the origin or derivation of the tabulated 10 ms value, and that **the Bai verdict should be expected to remain "discrepancy requiring verification, not proven error" regardless of the outcome.** Both held. No citing paper among those read in full derives, explains or sources the 10 ms figure; the tabulating paper states it and cites the primary source, nothing more. **E-ASM-03's verdict is unchanged and must not be strengthened on the strength of this search.** The one thing the caveat did not anticipate is that the search would find *escalations* beyond the tabulated value — a "1 ms" figure with no primary-source counterpart at all.

**The further instance flagged for inclusion was included.** RAN-25's version-of-record assertion of *"millisecond switching speeds"* for the filamentary platform (E-03b) is carried in the propagation register as **E-FP-05**, and the search covered the citing FIM system literature generally rather than only the tabulating papers, as instructed.

---

## HIGH

### U4 — The external sources carrying two of three traceability findings are not archived
Table I and the coherence-block Remark were inspected through online full text, not archived PDFs. Both are footnoted as such in the draft. Verifying against the published PDFs would remove the manuscript's most obvious point of reviewer attack.

### U5 — ✅ RESOLVED 17 August 2026 — the ≈0.51 ms conversion is deleted from the manuscript
**And the reason recorded here was itself wrong.** The premise of this question was that the conversion "requires an assumption the source does not state (symbol rate = bandwidth)". The version of record **explicitly defines f_s = 100 kHz as the symbol rate** in its system model (XU-22 p. 721), and the held draft carries the same sentence on its p. 4. The conversion was never conditional.

It is deleted from the manuscript all the same, and the decision is a presentational one rather than an evidential one: the 51-symbol figure carries the argument, and a derived wall-clock number invites exactly the decontextualised quotation the manuscript criticises. It is retained in `evidence_matrix.md` E-DR-02 and `timescale_matrix.md` as a derived value, annotated *"derived from the source-stated f_s = 100 kHz; not required by the manuscript argument."*

### U6 — Publication metadata for six preprints
**Bibliographic half resolved 17 August 2026 from publisher-deposited Crossref records. Content half now closed for three of the six** — the published full texts of RAN-25, YAN-25 and XU-22 were obtained, archived and inspected on 17 August 2026.

| Key | Version of record | Status |
|---|---|---|
| RAN-25 | *IEEE Trans. Wireless Commun.* **25**, 13319–13335, 2026 · DOI 10.1109/TWC.2026.3668992 | ✅ confirmed |
| YAN-25 | *IEEE Trans. Wireless Commun.* **25**, 6823–6836, 2026 · DOI 10.1109/TWC.2025.3627095 | ✅ confirmed |
| XU-22 | *IEEE Trans. Veh. Technol.* **72**(1), 718–734, **Jan 2023** · DOI 10.1109/TVT.2022.3203818 | ✅ confirmed — **year in the key is wrong for the VoR** |
| ANJ-25 | **GLOBECOM 2024**, 4932–4937 · DOI 10.1109/GLOBECOM52923.2024.10901792. Separate journal paper confirmed: *IEEE TWC* **24**(4), 2940–2955, Apr 2025 · DOI 10.1109/TWC.2025.3526843 | ✅ confirmed — held copy is a **published conference paper**, not a preprint |
| ALE-26 | *2025 IEEE AP-S/CNC-USNC-URSI*, 1–4, Jul 2025 · DOI 10.1109/AP-S/CNC-USNC-URSI55537.2025.11265965 | ✅ confirmed — **VoR year is 2025** |
| MA-26 | none found; only TechRxiv preprint DOI 10.36227/techrxiv.176857884.40392967/v1, 16 Jan 2026 | ⚠ **no journal VoR** — cite as preprint |

**What has now been read in full, and what has not.** The published full texts of **RAN-25, YAN-25 and XU-22** were obtained by the user, archived in the corpus as `01V_…`, `04V_…` and `07V_…`, and inspected. For **ANJ-25, ALE-26 and MA-26**, only Crossref publisher-deposited records and IEEE Xplore listings have been seen; **their published full texts have not been retrieved**, and quantitative claims keyed to them remain unverified against a version of record.

**Result of the three version checks: every load-bearing *timing and parameter* quantity survives; one non-timing quantitative claim did not.** The correction is recorded in the table below and in `evidence_matrix.md` E-13. The earlier unqualified wording — *"every load-bearing quantity survives"* — was written before the second sweep of 18 Aug 2026 and was too broad: the first sweep checked the five YAN-25 items enumerated in the review brief and did not re-check YAN-25's abstract-level performance figure.

| Old locator | Version-of-record locator | Outcome |
|---|---|---|
| RAN-25 Table II, p. 8 | **Table III, p. 13327** | ✅ retains 28 GHz, λ = 0.0107 m, B = 20 MHz, N_T = N_R = 4, V_max = 208 m/s, morphing range −λ to +λ |
| RAN-25 footnote 8, p. 8 | **footnote 10, p. 13327** | ✅ shape-reuse statement retained verbatim |
| RAN-25 Fig. 2 discussion, p. 8 | **pp. 13327–13328** | ✅ system parameters p. 13327; Fig. 2 communications discussion continues p. 13328 |
| YAN-25 protocol, pp. 7–8 | **p. 6829** | ✅ element moves once per subframe, phase adjusted once per time slot |
| YAN-25 Fig. 8, p. 11 | **Fig. 8, p. 6833** | ✅ retains i7-13650HX CPU, 400-iteration maximum, 10⁻⁸ tolerance |
| XU-22 51 symbols, p. 4 | **p. 721** | ✅ retains 2.6 GHz, 90 mph, 51 symbols at 0.5 correlation; **and states f_s = 100 kHz** |
| XU-22 Fig. 4b, p. 9 | **Fig. 4(b), p. 728** | ✅ retains 20 symbols @ 0.95 and 40 symbols @ 0.82 |
| XU-22 1 + M slots, pp. 3, 6–8 | **pp. 720, 722, 726** | ✅ retained |
| RAN-25 Eqs. (1a)–(3), p. 3 | **Eqs. (1a)–(3) / (1c), (2), (3), p. 13321** | ✅ retained (added to §1.1 and §2 prose, 18 Aug 2026) |
| RAN-25 mechanical-platform citation, p. 2 | **p. 13320** | ✅ retains the liquid-metal and Lorentz-filament motivation citing NI-22 and BAI-22 |
| RAN-25 waveform-rate equivalence, p. 8 | **p. 13328** | ✅ retained — "the achievable rates for the different waveforms across all the cases are almost identical", "within the constraints of the same physical channel" (E-06) |
| RAN-25 MUSIC spectra, pp. 9–11, Figs. 4–7 | **pp. 13330–13331, Figs. 6–9** | ✅ retained; figure numbers shifted by two (E-07) |
| YAN-25 simulation setup, p. 11 | **pp. 6832–6833** | ✅ retained (E-14) |
| YAN-25 **125 % EM-only gain, abstract p. 1** | **absent from the version of record** | ‼ **DOES NOT SURVIVE.** The preprint abstract's sentence *"In a multi-element, multi-path scenario, the EM-only mode improves the received signal power by 125% compared to the PBF-only mode"* is **deleted** in the published abstract, which keeps only the qualitative comparison (p. 6823). No percentage figure appears anywhere in the version of record's technical text. **Withdrawn from the manuscript**; E-13 reclassified *superseded-by-version-of-record*. Do not re-derive it from a published plot. |

‼ **One material difference was found, and it is not editorial.** RAN-25's version of record adds a **Remark on pp. 13321–13322 that the held preprint does not contain**, asserting *"millisecond switching speeds"* for the filamentary mechanical platform (its reference [36] = BAI-22), *"comparable to typical channel coherence times in high-mobility wireless scenarios"*, and then offering the slower alternative — morphing *"once over several channel coherence intervals to achieve statistically optimal performance"*. Registered as **E-03b** and **E-03c**. The millisecond assertion is a further instance of the substitution documented in §6.5 and is recorded, like the tabulated 10 ms value, as a **discrepancy requiring verification and not as an error**. The statistical-morphing sentence is the two-timescale premise stated by the system paper itself, and §6.5 and §9.1 now cite it as such.

**What remains open under U6 (updated 18 August 2026).** ✅ **ANJ-25 is now closed.** The IEEE published GLOBECOM 2024 record is paywalled, but Semantic Scholar confirms arXiv:2502.16472 **is** that paper, and the team's extended journal article (*IEEE TWC* **24**(4):2940–2955, 2025) was obtained in full from an open institutional repository. **All five load-bearing ANJ-25 claims survive in both versions** — 10.8 mm at 28 GHz, ≈3 dB, the 100-iteration cap with the −30 dB stopping rule, quasi-static flat fading, and perfect CSI. ⚠ One difference: the journal adds a millisecond morphing assertion absent from the conference paper (E-FP-04).
**ALE-26 is closed as far as it can be, and it does not matter.** Semantic Scholar confirms arXiv:2409.09590 is the same work as the 2025 AP-S/CNC-USNC-URSI paper; the published version is paywalled. **ALE-26 supports no active manuscript claim** — its only evidence row, E-59, is not cited anywhere in the manuscript — so no claim is exposed and the conservative scoping costs nothing.
**Genuinely still open:** MA-26 has no journal version of record at all and stays a preprint citation. The RAN/YAN/XU part closed on 17 Aug.

**Keys are not being re-lettered.** `XU-22`, `ANJ-25` and `ALE-26` carry years that do not match their versions of record. Re-keying would touch every documentation file for no analytical gain; the correct years are recorded here and in `source_inventory.md`, and the **bibliography must use the version-of-record year**.

### U7 — Three corpus PDFs have no extractable text layer
The cylindrical conformal RIS paper, one conformal metasurface array paper and the wide-angle conformal active metasurface paper are rasterised Wiley downloads. Metadata and abstracts were read from rendered images; no deeper claim is drawn. If any of these needs to carry weight, page-by-page image reading is required.

### U8 — Author-overlap structure of the FIM system literature
The external search returned many FIM papers with recurring author sets. If the system-modelling side of this field is less independent than its paper count suggests, that is directly relevant to how much confidence the shared assumptions should carry.

**✅ DONE — a co-authorship analysis was performed, and C3 now rests on it.** *(Superseded 18–19 Aug 2026; the previous text of this item said "No co-authorship analysis was performed" and was left standing after the analysis was done.)*

**Method.** Author lists for all 24 stage-2 records were taken from OpenAlex published-record metadata and intersected with (i) the FIM system-paper lineage audited in this review and (ii) the author sets of the three primary hardware sources. Authorship is metadata-verifiable even where the full text is paywalled, so every study resolves; what remains unknowable for an unread paper is its *contents*, not its authorship. Implemented in `tools/resolve_author_network.py`; per-study result in `s11_study_register.md`.

**What it established.** Of the 20 distinct studies: **14 share an author with the FIM lineage, 4 are disjoint from that lineage, and 2 are disjoint from both the lineage and all three primary hardware sources.** The four studies carrying the five propagation instances form **one connected co-authorship network** — connectivity is what was verified, not pairwise sharing. **No author-disjoint publication group reproduces the practice**, which is why C3 is held at Level A. Two fully author-disjoint studies cite the same hardware and attach no timing value, i.e. the counterexamples are independent while the propagation cases are not.

**What remains limited.** The analysis is of *authorship*, not of intellectual independence — shared senior authors are evidence against independence, but their absence does not establish it. Seven studies remain unread, so no statement is made about what they contain; of those seven, exactly one is author-disjoint from both the lineage and all three seeds, and that single study is the entire residual risk to the independence finding. No prevalence, proportion or rate is estimated from any of this.

---

## MEDIUM

### U9 — The third mechanical platform (Niu et al., photomechanical, 500 ms) is not in the corpus
Cited in the audited Table I. No claim is made about it. Retrieving it would complete the audit of that table.

### U10 — Whether liquid crystal is a realistic FIM tuning mechanism
§6.3 observes that LC switch-off exceeds a complete measured electronic loop measured on a different platform. **The manuscript no longer draws the design consequence it previously drew** — that an LC-tuned FIM would be material-limited rather than actuator-limited — because no integrated LC FIM exists in the reviewed set and a bottleneck cannot be established from measurements of separated parts. The question is therefore genuinely open and is recorded here rather than answered in the text. The reviewed LC source argues for LC on cost and large-panel scalability grounds; whether that trade is acceptable is a question the evidence does not settle.

### ✅ U12b — Whether to disclose our own retracted derivation in the manuscript body — **DECIDED 18 August 2026: RETAIN**
**Decision: retain in the manuscript body, at both §6.2 and §9.4.** Applying the stated test — does disclosure materially strengthen the methodological argument, or does it mainly narrate the drafting process? — it strengthens the argument, and does so at the one point where the paper is otherwise weakest. §6.5 asserts that these substitutions follow from underspecified reporting rather than from carelessness, and closes with "we are not accusing anyone of bad faith". Without our own instance that is an assertion; with it, it is a demonstration, and a first-hand one: a review whose explicit purpose was to catch this error class committed it on the same source. The two placements do different work and neither is process narration — §6.2 shows the error *in situ*, beside the values that invite it; §9.4 answers the reviewer's question of whether the authors audited themselves. **If length pressure arises during the authoring pass, compress the §9.4 restatement, not the §6.2 blockquote.** The audit trail in `citation_audit.md` C5 is permanent and independent of this decision.

*(Superseded provisional note, retained for the record: "yes, and it is currently disclosed" at §6.2 and §9.4.)* The argument for disclosure is that the manuscript's central contribution is an audit of exactly this failure mode, and a reviewer who discovered the correction independently would have grounds to doubt the whole. The argument against is that it hands a reviewer a ready-made criticism. **A supervisor may reasonably overrule this**; if so, the correction stays in `citation_audit.md` C5 and the manuscript simply carries the correct figure. The audit trail must retain it either way.

### U11 — Whether the reviewed reviews' published versions differ from the copies held
Particularly the movable-antenna survey, held as an arXiv manuscript. The zero-occurrence finding for "FIM" is a property of the copy we read.

### ✅ U12 — Title — **DECIDED 17 August 2026**
Adopted: *"Flexible Intelligent Metasurfaces for High-Mobility ISAC: Hardware Evidence, Adaptation Timescales, and Validation Gaps."* Checked against the manuscript architecture — its three clauses map onto §5, §6 and §7 — and adopted for being conventional and accurate. The interrogative alternative is retained in `article_type_assessment.md` §4 as a recorded option. The rejected working title is not to be reinstated.

---

## LOW / FOR THE RECORD

### U13 — Two workbook entries corrected by this audit
- The 10.8 mm figure at 28 GHz is stated by its source, not derived (was recorded as derived).
- "Converges after about 10 iterations" was attributed to the wrong paper; the multiuser FIM paper caps iterations at 100 and plots 0–50, while the ≈10-iteration figure belongs to the bistatic short paper.
These are recorded in `CHANGELOG.md` and should be carried back into `Metasurface_Master_Research_Workbook_v1.xlsx` sheet `14_AI_Review_Log` by the user; **this audit did not modify the workbook.**

### U14 — Two files in the corpus were mislabelled or unlabelled
`ars-19-215-2022.pdf` is a previously unrecorded second Harz paper (array-level, 2022) and is not the same work as `21_Harz_…`. Suggested rename: `21B_Harz_10x10_Tunable_Reflectarray_Measurement.pdf`. **No file was renamed by this audit.**

### U15 — All workbook "missing sources" are now resolved
The Harz element paper, the cylindrical conformal RIS paper, both conformal metasurface papers by the Nanjing group, and the wide-angle conformal active metasurface paper were all already in the corpus (M01–M05). **M06, the Fan Li supplement, was retrieved on 17 August 2026 and is now archived.** Workbook sheet `12_Missing_Sources` can be closed in full; **this audit did not modify the workbook.**

### U17 — Neither supplement reports uncertainty on its headline timing value
Recorded as absence claim A15 and finding F4. No interval quoted in this manuscript can be given with a dispersion figure. This is a source-side deficiency, it now motivates an additional field in the reporting framework (repetition count and dispersion), and it should be stated to any reviewer who asks why no error bars appear in Table 5.

### U16 — Whether the reporting framework should propose numerical thresholds
Deliberately it does not (§8.1). If a supervisor or reviewer wants thresholds, the honest answer is that the evidence does not support them and that proposing them would repeat the failure the review documents. This position should be defended, not conceded.

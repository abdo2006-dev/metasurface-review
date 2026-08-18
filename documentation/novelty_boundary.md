# Novelty Boundary and Closest-Review Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.1 · 18 August 2026 (freeze consistency gate; see `CHANGELOG.md` v1.5)
**Verdict scope:** PROJECT CORPUS + the documented searches in `literature_search_log.md`. This is **not** a systematic search. Every conclusion below is bounded accordingly.

> **Version-of-record status (17 Aug 2026; amended 18 Aug 2026).** The published full texts of **RAN-25** (*IEEE TWC* **25**, 13319–13335, 2026), **YAN-25** (*IEEE TWC* **25**, 6823–6836, 2026) and **XU-22** (*IEEE TVT* **72**(1), 718–734, **2023**) have been obtained, archived (`01V_…`, `04V_…`, `07V_…`) and inspected. Every load-bearing **timing and parameter** quantity keyed to them survives; locators are now the version-of-record locators. ‼ **One non-timing claim did not survive:** YAN-25's preprint-abstract figure of a 125 % received-power gain for element movement over passive beamforming is **absent from the version of record** and has been withdrawn from the manuscript (see `evidence_matrix.md` E-13, `CHANGELOG.md` CH-66). The earlier preprint/draft copies are retained as **earlier versions within the same independence group**, never as separate sources. One material addition was found — RAN-25's new Remark, pp. 13321–13322 (E-03b, E-03c). Internal keys are unchanged; the bibliography must use the version-of-record years. See `unresolved_questions.md` U6.

---

## 1. The finding that changes the project

**The originally proposed framing — "From Instantaneous Shape Optimization to Two-Timescale Control" — is no longer defensible as a contribution.**

Search S2/S3 located published work that already performs exactly that move:

- **Kumar, Papazafeiropoulos, Kourtessis, Senior, Chafii, Kaklamani & Venieris**, *Flexible Intelligent Metasurface for Downlink Communications under Statistical CSI* (arXiv:2512.23045, Dec 2025; also an IEEE journal version). The abstract states the work departs "from prior works that rely on instantaneous channel state information (CSI)" and optimises the FIM under **statistical CSI**.
- **arXiv:2601.15471**, *Achievable Rate Optimization for Large Flexible Intelligent Metasurface Assisted Downlink MISO under Statistical CSI*.

And within the project corpus itself, the two-rate idea is already present twice:

- **E-12 (YAN-25, verified verbatim):** "the element moves once per subframe, and the FIM adjusts the phase once per time slot." A two-rate schedule, in a FIM paper, published before this project began.
- **E-41 / E-42 (MA-26, verified verbatim, pp. 20 and 26–27):** instantaneous CSI for quasi-static channels, statistical CSI for fast fading; and hierarchical cross-layer control in which statistical information guides slow movement while rapid state changes are decoupled.

**Conclusion.** Two-timescale FIM control is neither ours to propose nor ours to name. The title, the abstract and the contribution list have been rewritten accordingly (see `article_type_assessment.md` §4).

---

## 2. Closest-review comparison

Assessed against every review-type source in the corpus, plus the external search.

| Question | **MA-26** Ma et al., RA/MA survey | **TIS-25** Tishchenko et al., RIS–ISAC survey | **SAI-22** Saifullah et al., tuning-mechanism review | **External search** |
|---|---|---|---|---|
| Covers movable/reconfigurable hardware taxonomies | ✓ comprehensively | partly (hybrid RIS) | ✓ (tuning mechanisms) | — |
| **Covers FIMs specifically** | ✗ — **zero occurrences** of "FIM" or "flexible intelligent metasurface" (ligature-normalised full-text search, E-44) | ✗ — zero occurrences (E-47) | ✗ — zero occurrences (E-47) | **no FIM-specific review or survey located** (S1, S10) |
| Covers high mobility / Doppler | ✗ — zero occurrences of "Doppler" | ✓ 1 occurrence; links carrier frequency to shorter coherence times (E-48) | ✓ 5 occurrences, optics context | — |
| Covers ISAC | ✓ 46 occurrences | ✓ 21 occurrences | ✗ — zero occurrences | — |
| Covers mechanical tuning / actuation | discussed as movement, no mechanism review | ✗ — zero occurrences of mechanical tuning terms | ✓ MEMS, microfluidic, stretchable, kirigami | — |
| **Maps adaptation-chain stages end to end** | ✗ | ✗ | ✗ | ✗ |
| **Audits measured hardware timing against defined start/end events** | ✗ — *recommends* that models include movement time, settling, friction and energy (E-43), but performs no such audit | ✗ — notes controller/network latency as a concern (E-48), does not audit values | ✗ — gives a mechanism-level qualitative ranking (E-45), explicitly heterogeneous | ✗ |
| Distinguishes latency definitions (element vs surface, on vs off, partial vs full loop) | ✗ | ✗ | ✗ | ✗ |
| Proposes a reporting framework for the missing quantities | ✗ | ✗ | ✗ | ✗ |
| Traces feasibility claims back to primary hardware sources | ✗ | ✗ | ✗ | ✗ |

**The three broad reviews partition cleanly and leave a hole.** SAI-22 covers tuning *mechanisms* without systems, ISAC or latency. TIS-25 covers RIS *systems* and ISAC without mechanics. MA-26 covers movable *antennas* and the timescale principle without FIMs, Doppler or conformal surfaces. None of the three addresses the object this manuscript is about.

---

## 3. What this manuscript MUST NOT claim

Each item is followed by the source that pre-empts it.

1. **Not** the invention of flexible intelligent metasurfaces. *(RAN-25, ANJ-25, YAN-25 and a substantial external FIM literature.)*
2. **Not** the first FIM + high-mobility + ISAC work. *(RAN-25, MOR-26.)*
3. **Not** the first FIM channel-estimation protocol. *(YAN-25; plus external arXiv:2508.00268, arXiv:2605.29227.)*
4. **Not** the concept of slow-mechanical / fast-electronic hierarchical control. *(MA-26 E-41, E-42.)*
5. **Not** two-timescale or statistical-CSI FIM control. *(External: Kumar et al. arXiv:2512.23045; arXiv:2601.15471. Corpus: YAN-25 E-12.)*
6. **Not** the observation that mechanical motion is slower than electronic reconfiguration. *(MA-26 E-40; SAI-22 E-45.)*
7. **Not** the observation that coherence time is a correlation threshold rather than an interval of constancy. *(XU-22 E-15.)*
8. **Not** the idea that models should include actuation time, settling, positioning accuracy and energy. *(MA-26 E-43 states this as a recommendation.)*
9. **Not** delay-aware modelling of reconfigurable-aperture hardware in general. *(External: fluid-antenna port-switching-delay work, arXiv:2605.06275, E-NOV-02.)*
10. **Not** flexible, conformal, or curvature-compensating metasurface hardware. *(LI-25, LU-25, LU-26, PEP-26, CHE-26, GUO-25, LIH-19, BUD-22, YOO-21, GAL-22.)*
11. **Not** deformation-aware calibration of a flexible aperture. *(GAL-22 E-38; LI-25 E-19.)*
12. **Not** a "systematic review" or "systematic mapping". *(No protocol, no database search — `literature_search_log.md` §1.)*
13. **Not** "no hardware validation exists" in unqualified form. *(Absence is bounded by this corpus and these searches — `absence_claims.md`.)*

---

## 4. Strongest defensible contribution

After removing everything in §3, four things remain. They are narrow. They are also, as far as this audit can determine, unoccupied.

### N1 — A stage-resolved adaptation-chain decomposition specific to FIMs, with per-stage evidence levels
Ten stages (S1–S10 in `adaptation_chain_matrix.md`), each classified per source on **two independent axes** — stage evidence status and timing status. The result — that **no source fully delimits more than five of the ten stages and only one reaches five; that the two platforms reaching six under the any-timing reading are disjoint in the decisive respect, one radiating without commanding its shape and the other commanding its shape without a radio-frequency layer; that no source times channel estimation (S3) together with a commanded shape change (S7); that calibration (S9) is timed by no reviewed source; and that stabilised RF operation (S10) is quantitatively measured on five platforms and delimited on one, which holds its geometry static** — is not stated anywhere located in this audit. MA-26 recommends that such quantities be modelled; it does not map which are timed and on what.

⚠ **Wording constraint A (17 August 2026).** This contribution was previously stated as "no source records more than five **contiguous** stages". **That word was mathematically false and must not return.** The largest linked set, LI-25's, covers S1–S2 and S4–S6 — it skips S3, so it is not contiguous under our own taxonomy. Acceptable forms: "the largest set of linked stages timed on one platform"; "five of the ten stages"; "no source times S3 together with S7". Forbidden: "five contiguous stages", "longest contiguous chain", "contiguous run".

⚠ **Wording constraint B (18 August 2026, `CHANGELOG.md` CH-100).** The verb must be **times**, never **measures**. The count is a *timing* count: under the quantitative reading the maximum is six, not five, because several stages carry quantitative RF measurements with no duration attached. **Forbidden: "no source measures more than five stages."** Required: "no source **times** more than five of the ten stages."

### N2 — A timing-definition discipline with explicit start/end events, and the demonstration that it changes conclusions
`evidence_matrix.md` Part B records start event, end event, architecture, and a comparability class for every timing value in the corpus. Two non-obvious results fall out and neither is in any reviewed survey:
- **AKR-26 reports element- and tile-level update bounds at different scopes**, differing by up to two orders of magnitude (< 0.1 ms per element vs < 10 ms per 16 × 16 tile) on the same hardware. It separately reports a ×4 time-multiplexing penalty. Together these establish that panel-scale timing cannot be inferred from element timing and that the control architecture introduces measurable overhead; **they do not establish a decomposition of the full tile-level interval**, and the ×4 factor must not be presented as explaining it (E-29, T-AK-01…03).
- **Electronic and mechanical timescales overlap.** NEU-24's LC τ_off = 72 ms is numerically larger than LI-25's 16.76 ms measured partial electronic compensation chain and within a factor of four of NI-22's ≈300 ms full-surface mechanical morph. The convenient "fast electronics, slow mechanics" dichotomy — including the version MA-26 states qualitatively (E-40) — **requires mechanism-, object- and architecture-specific qualification**: architecture labels alone do not establish a universal latency ordering. These values sit in three comparability classes and may be displayed on a common axis to show range overlap, never pooled or ordered as performance.

### N3 ★ — A traceability audit of the hardware-feasibility premise in the FIM system literature
This is the strongest and most original item. The FIM system literature justifies its feasibility on three assertions, each of which this review traced to source:

| Assertion | Where | What the primary source actually reports |
|---|---|---|
| An optimised shape "can be used irrespective to changes in delays, Doppler shifts and waveform" | RAN-25 **footnote 10, p. 13327** (E-03) | **nothing** — no bound, no lifetime, no sensitivity analysis, no experiment |
| FIM shapes "are only updated on the timescale of the channel's coherence block" | arXiv:2502.16478 Remark 4 (E-ASM-01) | a modelling assumption; no hardware |
| "The response time of FIM surface morphing reaches 10 ms according to Table I" | arXiv:2606.06845 Table I (E-ASM-03) | **BAI-22's complete published package — main text, Extended Data, 71-page SI, peer-review file — reports element response < 0.07 s (measured at 60 fps), system morphing within 0.1 s, a 0.35 ± 0.15 s function-evaluation cycle, and ≈2.5 min closed-loop convergence. It contains no value at or near 10 ms.** The same Table's 30 ms entry for Ni is NI-22's *isolated-ribbon* figure; NI-22's *full-surface* figure is ≈300 ms. |

Tracing a load-bearing feasibility premise back through the citation chain to the primary hardware measurement is a defensible original contribution of a review. Stated precisely, what the audit delivers is this: **it determines what physical process each reported number actually measures, which substitutions between them are unsupported, and which quantities remain unmeasured.**

It does *not* tell the reader which number to use, and the manuscript must not say that it does. The audit's own central finding is that for most of these quantities **there is no single interchangeable number** — "morphing time" on one platform denotes both a sub-0.1 s open-loop actuation and an ≈2.5-minute closed-loop convergence, and which is relevant depends on whether the required geometry can be precomputed, a question the system literature does not pose. Supplying a replacement number would repeat the error being documented.

> ### ★ N3 scope classification — **LEVEL A**, decided 18 August 2026 on the evidence of the forward citation search (S11)
>
> The three permitted levels were fixed **before** the search was run, and the evidence was read against them afterwards:
>
> | Level | Criterion | Met? |
> |---|---|---|
> | **A — isolated cases** | only a few related papers repeat the substitution; C3 must stay framed as *"in the FIM system papers audited here…"* | ✅ **this is the outcome** |
> | **B — multiple independent instances** | the same substitution type appears in **multiple independent publication groups** | ❌ **not met — zero author-disjoint groups** |
> | **C — broad documented propagation** | a reproducible forward search shows the practice widely enough to support a literature-level statement | ❌ not met |
>
> **Why not Level B.** Level B turns on *independent publication groups*, and by the project's own standing independence rule the answer is zero. All four instances (E-FP-01 … E-FP-05) share at least one author with the FIM system papers audited here — Jiancheng An appears in three, Chau Yuen in three — and 14 of the 20 identified FIM system studies share an author with that network. Four different first-author teams is **not** four independent groups when a common senior author runs through them, and this project does not count conference/journal pairs or shared-lineage papers as confirmations. The search also found the opposite pattern in nine studies, including two with no overlap at all, which cite the same primaries and attach no timing figure.
>
> **What did change, and may be claimed.** The case base is now **four documented instances rather than two**, each with verbatim quotation, and it includes two *escalations* the earlier framing did not capture: a "1 ms" figure with no counterpart in any primary source, and a millisecond assertion inserted between an author team's own conference and journal versions. C3 may state the count, the escalations and the negative independence result. **C3 may not state or imply a prevalence, a proportion, or a claim about "the field".**
>
> **What would move this to Level B or C.** Only an author-disjoint instance. Repeating S11 with IEEE Xplore access — 7 of 20 papers were paywalled and unread, so every count here is a lower bound — is the way to test for one. Absent that, the wording stays as it is.

**Two distinctions must be preserved whenever N3 is summarised:**

- **The Ni substitution is confirmed** against the primary source: an element-level figure appears under a surface-level label, with the correct value two paragraphs away in the same paper. This is verified, not conjectured.
- **The Bai 10 ms remains an unresolved discrepancy.** Retrieving the complete package (17 August 2026) establishes that no such value is reported anywhere in it, and that the 60 fps instrument used could not have resolved one. It does **not** establish how the tabulating authors derived their figure, which we can neither observe nor reconstruct. The claim stays worded as a discrepancy requiring verification, **not** as a proven error, and no severity is transferred to it from the confirmed Ni finding. See `audits/citation_audit.md` CA-01 and CA-02.

**Required honesty (updated).** The residual-risk entry that made this contingent on obtaining BAI-22's supplementary material is discharged — the material was obtained and strengthens the finding. A separate and more uncomfortable disclosure now attaches to N3: in the course of this work the review **committed the same class of substitution error itself**, deriving a convergence time from a cycle count multiplied by an iteration count when an iteration comprises 34 cycles. It is retracted and reported in the manuscript (§6.2, §9.4) and in `citation_audit.md` C5. N3 is a claim about the difficulty of a specific citation practice, and the evidence for that difficulty now includes our own instance of it.

### N4 — A FIM-specific reporting framework derived from observed deficiencies
Not a generic wish list. Every field in `manuscript/08_reporting_framework.md` is justified by a specific unreported quantity identified in this corpus (T-GAP-01…03, C11–C14, C17, C18), and the framework prescribes *definitions* — start event, end event, threshold, object — rather than acceptance thresholds, which the evidence does not support.

---

## 5. Residual novelty risks

| Risk | Severity | Mitigation applied |
|---|---|---|
| A FIM survey may have appeared and not been surfaced by a general web search | **High** | title and claims worded corpus-bounded; a proper database search is listed as required pre-submission work |
| ~~N3 could be undermined if BAI-22's supplementary material contains a 10 ms figure~~ | ~~High~~ → **discharged** | **Resolved 17 Aug 2026.** The complete package was retrieved and searched; no value at or near 10 ms occurs, and the 60 fps instrument could not have resolved one. The claim is *strengthened* but deliberately **not upgraded** to an error, since the tabulating authors' derivation remains unobservable. |
| N3's credibility is affected by this review having committed the same substitution error (C5) | **Medium** | disclosed in the manuscript (§6.2, §9.4) rather than only in the audit trail; a guard rule was added to `evidence_matrix.md` Part C. Disclosure is judged safer than silent correction, and the instance is arguably evidence *for* the thesis |
| The FIM literature is moving fast (multiple 2026 preprints found); a paper may already audit hardware assumptions | Medium | searched (S1, S4); none found; must be re-run at submission |
| N2's "overlap" result depends on comparing NEU-24 (62 GHz LC) with LI-25 (3.2 GHz varactor) — different bands and mechanisms | Medium | the manuscript states this explicitly and draws only the mechanism-conditional conclusion |
| Niu et al. (cited as [40] in the audited Table I) is not in the corpus | Low | no claim is made about it |
| MA-26's published version may differ from the arXiv copy | Low | flagged in `unresolved_questions.md` |

---

## 6. Recommended contribution statement (for the manuscript)

> Within the literature reviewed here, we (i) decompose FIM adaptation into ten stages and classify the evidence level attained at each, (ii) record every reported timing value with its start event, end event and architecture, and show that the resulting comparability constraints require two common simplifications to be qualified by mechanism, object and architecture, (iii) trace the hardware-feasibility premises of the FIM system papers audited here back to the primary mechanical measurements they cite, and (iv) propose a reporting set whose fields are motivated by recurring reporting deficiencies and by specific unresolved quantities. We propose no new hardware and no new control algorithm, and we make no novelty claim for the two-timescale or statistical-CSI principle; all four contributions are auditing contributions.

⚠ **Wording constraints, added 17 August 2026.**
> - **Do not write "all of which already exist"** of the hardware/algorithm/two-timescale triple. The two-timescale and statistical-CSI *principles* exist; **self-actuated radiating A1-style FIM hardware does not**, and that is the review's central finding. Collapsing the three into one "already exists" contradicts §2.8. Acceptable form: *"We propose no new hardware and no new control algorithm, and we make no novelty claim for the two-timescale/statistical-CSI principle."*
> - **Do not write that every framework field names a quantity "no reviewed study reports."** Some fields are reported by some sources and absent from others; that inconsistency is itself the deficiency. Acceptable form: *"each field is motivated by a recurring reporting deficiency or a specific unresolved quantity identified in the reviewed set."*
> - **Do not use field-level language** — "the FIM literature does…", "the FIM system literature rests on…", "the literature concludes…" — where the evidence is the audited two-paper chain. Acceptable forms: *"the system papers audited here"*, *"the specific feasibility claims examined here"*, *"in the cases traced here"*. This does **not** weaken the confirmed Ni substitution, and does **not** strengthen the Bai discrepancy to an error.

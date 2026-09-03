# Manuscript Argument Map

**Version:** 2.1 · 18 August 2026 — **remapped to the v0.20 twelve-section structure** produced by the publication-oriented authoring pass (see `CHANGELOG.md` v1.7). Supersedes v1.1, which mapped the ten-section v0.14 outline.

**Central research question the whole manuscript answers:**

> Which operations in a FIM-assisted high-mobility ISAC system must track fast channel variation, which may follow slower geometric or statistical change, and how well are the resulting timescales supported by existing hardware and control demonstrations?

> **Scientific-freeze status.** The evidence base is frozen at documentation v1.6. The authoring pass moved claims between sections, tightened prose, produced the tables and figures, and converted the citation system to numbered references. It did **not** revise the science. Two corrections were made because they were factual errors found while completing the bibliography, and both are recorded in `CHANGELOG.md` v1.7: the DOI held for **BUD-22** was wrong, and one counterexample's author-overlap status (**E-FP-C1**, the JSAC paper) was stated too strongly.

> ✅ **v2.1 — 18 August 2026, reviewer-blocker revision (`CHANGELOG.md` v1.8).** Three wording constraints below changed and are now binding:
> 1. **C1 must name which axis it counts, and `times` means `·T` only.** Three counts exist and differ: quantitatively evidenced stages (max **6**, LI-25 and BAI-22), measured stage durations `·T` (max **4**, **BAI-22 alone**), and any timing information `·T`+`·(T)` (max **6**, **LI-25 alone**). Never write "five, reached by two platforms" — that figure follows from no consistent rule; and since the v0.24 taxonomy rebuild the `·T` maximum is **four**, not five. The two platforms are disjoint under the any-timing reading (LI-25 radiates without commanding its shape; BAI-22 commands its shape without an RF layer). S9 is timed by no source; S10 is quantitatively measured on five platforms and timed on one, with geometry static.
> 2. **C3 must carry its observation window.** State "13 of 20 candidate studies read" and "an author-disjoint instance among the unread seven cannot be excluded" wherever the finding appears. Use **"one connected co-authorship network"**, not "all four share authors".
> 3. **No source unread in full may support a claim about what it does not contain.**

---

## 0. Structure decision (v0.20)

The ten-section outline was restructured into twelve. Four changes, each with a reason:

- **Scope and method became its own section (§2).** In v0.14 it sat at the end of the Introduction, where a reviewer looking for the method had to find it inside a motivating argument. A structured critical review is judged on its method; the method should be locatable.
- **Timescale synthesis and the traceability audit were split (§7 and §8).** In v0.14 both lived in one 4 300-word section, the largest in the manuscript, and the traceability result — the strongest contribution — was its fifth subsection. It now has a section of its own and a table of its own.
- **Hardware evidence and the register were merged (§6).** The register was previously "specified, not drawn". It is now produced, in the section whose values it holds, grouped by quantity type so the comparability rule can be applied by eye.
- **Electronic and mechanical hardware remain in one section**, for the reason given in v1.1: splitting them would hide the finding that their reported ranges overlap.
- **No CST section.** Excluded by the gate in `article_type_assessment.md` §6. Unchanged.

| § | Title | Carries |
|---|---|---|
| 1 | Introduction | — |
| 2 | Scope, corpus and method | — |
| 3 | Seven architecture classes relevant to FIM evidence transfer | **Table 1**, **Figure 1** |
| 4 | What the surface is being asked to track | **Table 2** |
| 5 | The adaptation chain | **Table 3**, **Figure 2** |
| 6 | Hardware evidence, organised by physical process | **Table 4**, **Table 5** |
| 7 | Synthesis: what the register supports, and what it forbids | **Table 6**, **Figure 3** |
| 8 | How timing values travel: a traceability audit | **Table 7** |
| 9 | The validation gap | **Table 8**, **Figure 4** |
| 10 | A reporting framework for FIM adaptation | **Table 9** |
| 11 | Discussion | — |
| 12 | Conclusion | — |
| — | References | **36** entries, numbered by first appearance; one supplement-only source listed separately as [S1] |

**Table and figure inventory.** Nine tables and four figures. The count rose from the seven placeholder tables of v0.14 because two objects that were previously prose needed tabulating: the **timing-quantity taxonomy** (Table 4), which the register is unreadable without, and the **propagation cases** (Table 7), which are the evidence for C3 and were previously buried in a paragraph. The v0.14 placeholders "system assumptions vs evidence" and "validation gaps" were **merged into one table** (Table 8), because separately they repeated each other's rows.

---

## §1 Introduction

**Question answered:** why is a hardware-evidence audit of FIM adaptation timescales needed, and what does this paper add that existing reviews do not?

**Progression (fixed; do not reorder):** what FIMs add physically → why high mobility makes the physical question urgent → why one reported response time cannot settle it → what the adjacent reviews cover → the gap → the question → the instruments → the contributions.

**Essential claims**
1. Geometry is an optimisation variable in the system models, and exercising it requires moving matter. *(E-01, E-02)*
2. **Doppler frequency ≠ correlation interval ≠ update deadline.** §1.2 states the three-way distinction; §4.1 restates it at full precision. *(E-DR-01)*
3. One panel reporting two update times at two scopes is the compact proof that a single "FIM latency" cannot exist. *(E-29, T-AK-01/02)*
4. The nearest reviews cover adjacent ground but not this object. *(E-40 – E-49, E-44, E-47)*
5. **The slow-geometry/fast-electronics division is established, not novel.** *(`novelty_boundary.md` §3 item 4–6)*
6. Contributions C1–C4, all auditing contributions.

⚠ **Wording constraints.**
- Do **not** call the FIM system papers "independent formulations" — An and/or Yuen appear in all of them, and §8 tests independence by author-set intersection. Corrected 18 Aug 2026.
- Do **not** front-load numbers. §1.3's six values are there to be *separated*, not to establish a magnitude.
- Do **not** write "rather than two" of the propagation count — it is a fact about our own earlier draft and means nothing to a reader. Corrected 18 Aug 2026.

---

## §2 Scope, corpus and method

**Question:** on what basis may anything in this paper be believed, and what are the limits of that basis?

**Essential claims**
1. Structured critical review; explicitly **not** systematic, systematic mapping, scoping or PRISMA. *(`article_type_assessment.md` §1–§2)*
2. Corpus: 24 distinct contributions across 31 files; four supplementary/peer-review files belong to their parents.
3. Two searches with different weight: the non-systematic external search (S1–S10) and the **reproducible forward citation search** (S11), the latter bounded by seven paywalled full texts.
4. Extraction protocol: taxonomy, ten-stage template, timing register with comparability classes, **numbered evidence ladder L1–L7**, independence rule, absence-claim rule.
5. Two inherited constraints: absence is bounded to the reviewed set; **no headline interval in the manuscript carries an uncertainty**, because no source reports one for its headline response/morphing/adaptation interval. ⚠ Not universal — Table 5 row 28 carries 0.35 ± 0.15 s; say *headline*.

⚠ The ladder is numbered explicitly here because Table 8 uses L2/L4/L5/L6/L7 as labels. If the ladder wording changes, Table 8's level column must change with it.

---

## §3 Architectures and transfer rules

**Question:** what physically distinct systems are conflated, and what transfer between them is legitimate?

**Essential claims**
1. Seven classes A1–A7, split into **direct** (A1–A4) and **comparator / evidence-donor** (A5–A7). **Table 1 carries them; the prose must not re-enumerate the taxonomy.** ⚠ Do not imply all seven are called "flexible metasurfaces" by their own authors — A5/A6/A7 generally are not.
2. A1 is a **model** class with no hardware instance in the reviewed set. *(E-01, E-AA-01)*
3. The realised A3 apertures treat geometry as a **disturbance**; A1 treats it as a **control variable**. This inversion is the taxonomy's key output. *(E-19, E-20, E-53)*
4. The A4 commanded-shape platforms have **no RF layer**. *(E-32, E-34, E-35)*
5. Fixed-curvature conformal design has **substantial prior art**; time-varying controlled geometry has none. **Do not write "solved", "already solved" or "handled".**
6. Seven transfer rules, applied without exception thereafter.
7. The quadrant map: one cell empty; **A1 names the cell rather than occupying one.**

⚠ Do **not** describe A1 as treating geometry as exogenous — it does the opposite. ⚠ Figure 1 plots demonstrated hardware only; a modelling paper performs no experiment and cannot be placed on experimental axes.

---

## §4 What the surface is being asked to track

**Question:** what does "fast" mean here, and which state actually drives the shape?

**Essential claims**
1. Coherence time is a correlation threshold, not a constancy interval: 20, 40 or 51 symbols in one scenario, at 0.95, 0.82 and 0.5. *(E-15, E-16, E-18)*
2. Maximum Doppler ≈19.4 kHz at the reviewed operating point, **derived by us**, and converted into nothing. *(E-DR-01)*
3. **Table 2 separates the states** — instantaneous fading, statistics, angles/path geometry, target kinematics, blockage, surface geometry, calibration state — with the evidence available for each. **No column of Table 2 contains a deadline, and none is derivable from it.**
4. **RAN-25's version-of-record Remark states both halves of the trade-off**: millisecond feasibility asserted from BAI-22, *and* morphing once over several coherence intervals for statistical optimality. The second half makes two-timescale operation a premise the literature supplies, not one this review imposes. *(E-03b, E-03c)*
5. Overhead: pilot structure scales with controlled element count; the FIM protocol already contains two rates; computation is measured once and scales with virtual array size. *(E-17, T-CH-05, T-YA-01, T-LI-02)*

⚠ **Do not write "only the first is fast", "the fastest quantity" or "the slowest quantity".** No reviewed source fixes the relative rates. ⚠ **Never let 19.4 kHz become a deadline of tens of microseconds** — 1/f_D is a reciprocal, not a requirement.

---

## §5 The adaptation chain

**Question:** what are the stages, why does the decomposition matter physically, and what is claimed for each?

**Essential claims**
1. The chain crosses three physical domains with different governing physics and different scaling laws; that is *why* it is decomposed, and §5.1 must say so before listing the stages.
2. No reviewed source **measures the duration of** more than **four of the ten stages**, and none times S3 with S7. The two best-covered platforms are disjoint: **BAI-22 alone reaches four measured durations** — S1, S2, S5 and S7 — and commands its shape without a radio-frequency layer; **LI-25 measures three** — S4, S6 and S10 — and carries duration information for six once apportioned shares are included, but its geometry is externally imposed. *(Corrected 22 August 2026: this sentence still carried the pre-v0.24 count and contradicted the sentence immediately before it.)* S9 is timed by no source. S10 is quantitatively measured on five platforms and timed on one, with geometry static. **Do not write "contiguous". Do not write "measures" — the count is a timing count; under the quantitative reading the maximum is six** (`CHANGELOG.md` CH-100).
3. The measured stages sit on **four physically non-equivalent architectures**. ⚠ Do not write "mutually incompatible" — it can be misread as claiming these technologies cannot be physically integrated.
4. Concatenating stages across those four platforms is a category error, and the manuscript performs it nowhere.
5. The A1 literature does not model S5–S9, defending the omission with one unquantified footnote. *(E-03, T-ASM-01)*
6. Where a closed loop exists, **perception binds, not actuation** — stated as a property of that platform and a design warning, never as a transferred law. *(E-33, T-BA-03…06)*
7. Two precisely isolated absences: settling of a radiating aperture, and the interval from a *commanded* deformation to trustworthy radiation.

⚠ Table 3's LI-25 S10 cell records **two experiments** and carries the ‡ note. Writing "LI-25 measures S10" without the static-geometry condition asserts a measurement that does not exist.

---

## §6 Hardware evidence and the register

**Question:** what has been measured, on what object, between which events?

**Structure:** §6.1 quantity taxonomy (**Table 4**) → §6.2 A3 flexible programmable apertures → §6.3 A5 rigid comparators → §6.4 A4 commanded mechanics → §6.5 A7 active arrays → §6.6 the register (**Table 5**) → §6.7 what it establishes.

**Essential claims**
1. Table 4 names each quantity type *and the substitution it invites*; every one of those substitutions is observed somewhere in the reviewed material, including once in an earlier draft of this manuscript.
2. **16.76 ms** = shape acquisition → bias-voltage supply. Excludes the deformation before and the settling after. ⚠ It must **never** be labelled mechanical actuation time, mechanical settling, full FIM response, or end-to-end wireless adaptation latency.
3. **16.7 ms** = trigger → stabilised RF, **static geometry**. It removes any licence to say RF stabilisation is never timed, and it is not a post-morph measurement.
4. AKR-26's two bounds are two objects. The ×¼ multiplexing penalty does **not** explain the interval, and no decomposition exists.
5. NEU-24's 15/72 ms carry direction and the 10 %/90 % threshold. The **electronic layer as a whole has no quantified lower endpoint** in this corpus.
6. BAI-22: sub-0.1 s mechanics, 0.35 ± 0.15 s per function evaluation, ≈2.5 min closed-loop **search**, 10 fps open-loop **replay**. Search and replay are different operations.
7. NI-22: 30 ms ribbon / ≈300 ms surface / ≈650 ms shape-to-shape, with the membrane named as the cause.
8. GAL-22: the operation a FIM needs after a shape change, demonstrated and **untimed**.

⚠ Table 5's rows G1–G4 are the only rows with no value, and that is the section's conclusion. ⚠ Report LI-25's reflection amplitude as the source does — a normalised amplitude floor, **not** an efficiency.

---

## §7 Synthesis

**Question:** what does the assembled register support, and what does it forbid?

**Essential claims**
1. **Pooling is invalid.** No mean, median or pooled FIM response time; the licensed comparison is ordinal and within quantity type. *(`evidence_matrix.md` Part C)*
2. Element response, full-surface morphing and verified closed-loop convergence are distinct measurements. The element→surface step is **source-specific**, not a shared law; the third level is **not replicated**; the convergence figure is a property of the **search**.
3. **Simplification 1 qualified:** electronic and mechanical reported ranges **overlap**. Display on a common axis is permitted; pooling, ranking as performance, and inferring an integrated device's bottleneck are not. **Do not name bottlenecks for hypothetical integrated devices.**
4. **Simplification 2 qualified:** a latency is a property of an *object*. Distribution can be a **major contributor**; it is not established as dominant.
5. **Table 6** answers the research question stage by stage and **names the assumption behind every "no"** in its fast-fading column.
6. **No deadline is defined anywhere.** Do not call any measured update time adequate or inadequate.
7. **Absence ≠ infeasibility.** An interval that has not been measured is unquantified, not measured and found wanting.
8. The **self-correction blockquote** stays at §7.2. Written elegantly and briefly; not an incident report. *(U12b, decided RETAIN 18 Aug 2026)*

⚠ The timing-landscape figure (**Figure 2** since v0.28a; Figure 3 in v0.20–v0.28) must keep closed-loop *search* and open-loop *replay* on separate labelled lanes, or it reproduces the substitution the manuscript documents.

---

## §8 Traceability

**Question:** where do the feasibility premises come from, how far has the practice spread, and what may be claimed about that?

**Essential claims**
1. Three premises traced: the unbounded shape-reuse footnote; the coherence-block assumption; the tabulated morphing periods.
2. The **Ni 30 ms substitution is confirmed** against the primary text. The **Bai 10 ms remains a discrepancy requiring verification, not an error** — the complete package reports no such value, but the tabulating authors' derivation is unobservable. **No severity transfers from the confirmed finding to the unresolved one.**
3. **Table 7**: five instances across **four papers**, plus the counterexamples.
4. **Zero author-disjoint publication groups.** This is the load-bearing result and it is negative. *(N3 = Level A)*
5. Counterexamples are recorded so the section cannot read as confirmation-biased. **[KUM-25] is fully author-disjoint; [HUA-25] shares an author with [LI-25]** and is recorded as such rather than counted as fully independent. Corrected 18 Aug 2026.
6. Two structural observations, both bounded to the full texts inspected: no citing paper read derives the 10 ms value; two instances were inserted between an author team's own conference/preprint and journal versions.
7. §8.6 explains the **mechanism** — informal terms permit rescoping when object, start and end are omitted — and disclaims bad faith explicitly.

⚠ **C3 is frozen at Level A.** Permitted: "the system papers audited here", "the cases traced here", "in the four papers located by this search". Forbidden: "the field routinely", "widespread", "systematic literature-wide misuse", "the FIM literature generally", any proportion, any prevalence. Only an **author-disjoint instance** would move this.

---

## §9 The validation gap

**Question:** exactly what is missing, and what would each piece cost to close?

**Essential claims**
1. The gap is **not** flexibility, shape sensing, fast electronic control, or deformation compensation — all reach L5 or L6.
2. The gap is the transition from compensating an exogenous shape to commanding one and knowing when it has arrived, on an aperture that must also radiate.
3. **Table 8** runs assumption → implied capability → closest evidence → level → missing measurement, and names G1–G4.
4. The **structural** gap is deeper than any timing gap: the two best-covered radiating platforms hold three of the four required components ([7], [23]); the commanded-geometry platforms hold two ([22]) and none ([8]), and contribute the component that is not in the set. No platform holds all four. *(C10)*
5. Ranked by closability: G3 (a timed re-run of an existing experiment) → G1/G2 (instrumented morphing of an RF-loaded flexible panel) → G4 → the integration programme.
6. §9.5 states what the review does not show. **Absence of measurement is not evidence of impossibility.**

⚠ The λ/20 arithmetic in §9.2 is **illustrative of the form of a criterion** and is not a recommended value. It must stay marked as such, and §10 repeats the disclaimer.

---

## §10 Reporting framework

**Essential claims**
1. Every field is justified by a **recurring reporting deficiency or a specific unresolved quantity** observed in this review. ⚠ Do **not** write that every field names a quantity "no reviewed study reports" — some are reported by some sources and omitted by others, and that inconsistency is itself the deficiency.
2. **Definitions, not thresholds.** No numerical acceptance threshold is proposed anywhere.
3. Groups A–F for hardware papers (**Table 9**), plus a five-item assumption declaration for system papers.
4. Item 4 of §10.3 — provenance of imported hardware figures — is the cheapest and the most consequential.
5. §10.4 disclaims standing: this is not proposed as a standard.

---

## §11 Discussion · §12 Conclusion

**Essential claims**
1. The answer, stated **conditionally on the two-timescale premise**, with the premise named as a premise and attributed to the literature that supplies it.
2. Demand is established by modelling; supply on the electronic stage is measured, on A5 rigid panels and one A3 flexible aperture. **The comparison inherits the weaker evidence type.**
3. Three consequences for system modelling; three experiments for hardware work.
4. Limitations without hedging: non-systematic search; **no uncertainty on any headline value**; one preprint claim that did not survive its version of record; the supplement that corrected us; three image-only sources; single-reviewer extraction; small set; **no domain-expert review**.
5. §12 answers six questions — what the hardware can do, what is not established, which substitutions are unsafe, which states demand speed, which may be slower, what would close the gap — and ends on **concrete priorities**, not "future work is needed".
6. **No publication-readiness claim anywhere.**

---

## Cross-section redundancy control

| Idea | Owned by | May be *referenced* by |
|---|---|---|
| Review comparison | §1.4 | §11 |
| Method, corpus, searches | §2 | §8.5, §11.4 |
| Architecture quadrant / empty cell | §3.7 (Fig. 1) | §5.4, §9.3, §12 |
| Transfer rules | §3.6 | everywhere, by application not restatement |
| Doppler ≠ coherence ≠ deadline | §1.2, §4.1 | §7.5, §11.1 |
| State separation | §4.2 (Table 2) | §7.5, §11.1 |
| Ten-stage definitions | §5.1 | §6, §7, §9, §10 |
| Individual timing values | §6 (Table 5) | §7 by row number only |
| Pooling prohibition | §6.1, §7.1 | §10.1 |
| Traceability audit | §8 | §9.5, §11.5, §12 |
| Gap ranking | §9.4 | §11.3, §12 |
| Reporting fields | §10 | §12 |
| Self-correction disclosure | §7.2 (full) | §8.6, §11.4 (one line each) |

---

## Section-number crosswalk: v0.14 → v0.20

Documentation written before 18 August 2026 cites the **v0.14** ten-section numbering. Nothing in those files is wrong; the section numbers moved. This is the authoritative mapping.

| v0.14 | v0.20 | Note |
|---|---|---|
| §1 Introduction | **§1** Introduction **+ §2** Scope, corpus and method | §1.6 of v0.14 became a section of its own |
| §2 Architectures (§2.8 quadrant) | **§3** (§3.7 quadrant) | |
| §3 High-mobility timescales (§3.1 coherence threshold) | **§4** (§4.1) | |
| §4 Adaptation chain (§4.5 premises, §4.6 closed loop, §4.7 absences) | **§5** (§5.5, §5.6, §5.7) | |
| §5 Hardware evidence (§5.1 A3, §5.2 A5, §5.3 A4, §5.4 A7) | **§6** (§6.2, §6.3, §6.4, §6.5) | §6.1 taxonomy and §6.6 register are new |
| §6.1–§6.4 Timescale synthesis | **§7.1–§7.4** | the self-correction blockquote moved §6.2 → **§7.2** |
| **§6.5 Traceability** | **§8** — a section of its own | the strongest contribution; previously a subsection |
| §6.6 Stage-by-stage table | **§7.5** (Table 6) | |
| §7 Validation gap (§7.2 G1–G4, §7.3 structural, §7.4 ranking, §7.5 what it does not show) | **§9** (§9.2, §9.3, §9.4, §9.5) | |
| §8 Reporting framework (§8.1 no thresholds, §8.3 assumption set) | **§10** (§10.1, §10.3) | |
| §9 Discussion (§9.1 answer, §9.4 limitations) | **§11** (§11.1, §11.4) | |
| §10 Conclusion | **§12** | |

**Practical rule when reading older documentation:** "§6.5" means the traceability audit, now **§8**; "§9.4" means the limitations, now **§11.4**; "§6.2" means either the mechanical-measurement synthesis (now **§7.2**) or the self-correction blockquote (also **§7.2**); "§5.1" means the flexible-aperture evidence, now **§6.2**.

---

## Section-number crosswalk: v0.20 → v0.28

The twelve-section structure was journalized into **seven sections** on 22 August 2026 (draft v0.28; `CHANGELOG.md` v1.11). Nothing in the older documentation is wrong; the section numbers moved again, and a substantial amount of audit machinery moved out of the main text into the supplement. The full disposition, unit by unit, is `journalization_v0.28.md` §5.

| v0.20 | v0.28 | Note |
|---|---|---|
| §1 Introduction (1.1–1.6) | **§1**, no subsections | absorbs v0.20 §4.1; the four-example response-time survey became one paragraph |
| §2 Scope and method (2.1–2.5) | **§2**, no subsections | §2.4's symbolic scheme → **Supplementary S6** |
| §3 Architectures (3.1–3.7) | **§3.1** | Table 1 kept; Figure 1 kept in place |
| §4 Demand side (4.1–4.5) | **§1** (4.1) and **§3.3** (4.2–4.4) | Table 2 → **Supplementary S7**; §4.5 deleted as a redundant summary |
| §5 Adaptation chain (5.1–5.7) | **§3.2** (5.1) and **§4.6** (5.3, 5.4) | Table 3 → **Supplementary S6.3**; 5.6 → §4.3; 5.7 → §5.3 |
| §6 Hardware evidence (6.1–6.7) | **§4.1–§4.6** | Table 4 → **Table 2**, trimmed 20 → 15 rows |
| §7 Synthesis (7.1–7.5) | **§4.5** (7.1, 7.3), **§4.2/§6.2** (7.4), **§5.1** (7.5) | §7.2 deleted as redundant; Table 5 → **Table 3** |
| **§8 Traceability (8.1–8.6)** | **§5.2** — a subsection again | Table 6 and the study-by-study inventory → **Supplementary S8** |
| §9 Validation gap (9.1–9.5) | **§5.3**; 9.4 → **§6.3** | Table 7 → **Table 4** |
| §10 Reporting framework (10.1–10.4) | **§6.1** | Table 8 compressed 30 → 10 fields as **Table 5**; full list → **Supplementary S4** |
| §11 Discussion (11.1–11.5) | **§5.1** (11.1), **§6.2** (11.2), **§6.3** (11.3), **§6.4** (11.4), **§7** (11.5) | |
| §12 Conclusion | **§7** | rewritten; the old four-item list duplicated §9.4 and §11.3 |

**Main table renumbering:** T1 → T1 · T4 → T2 · T5 → T3 · T7 → T4 · T8 → T5 (compressed). T2, T3 and T6 left the main text intact, as S7, S6.3 and S8.2. **Figures are unchanged and unrenumbered**, F1–F4 in sections 3, 4, 4 and 5.

**Practical rule when reading documentation written before 22 August 2026:** "§8" means the traceability audit, now **§5.2** in the main text with its inventory in **S8**; "§9.2" means the validation gap and G1–G4, now **§5.3**; "§11.4" means the limitations, now **§6.4**; "§6.2" means the flexible-aperture evidence, now **§4.1**; "§5.3" means the stage counts, now **§4.6**; "§7.5" means the stage-by-stage table, now **§5.1** and Table 3.

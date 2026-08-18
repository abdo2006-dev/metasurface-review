<!-- AUTO-GENERATED REVIEW COPY -->
<!-- DO NOT EDIT DIRECTLY -- edit the section files in manuscript/ and re-run tools/sync_review_repo.py -->

> Manuscript v0.22 · generated 2026-08-18 22:32 UTC · private working-repository commit `63424622b7fa1a543e7bf2a1117f702e251cdd72`

---

# Flexible Intelligent Metasurfaces for High-Mobility ISAC: Hardware Evidence, Adaptation Timescales, and Validation Gaps

**Draft v0.22 — structured critical review — 19 August 2026.**
*C1/C3 integrity pass. Supersedes v0.21.*
*Three defects found by independent inspection of the published v0.21 artefact are repaired: the §2.4 method description still defined a one-axis stage coding contradicting §5; the C1 stage count of "five, reached by two platforms" followed from no consistent rule and is replaced by counts that name their axis; and the forward-citation dataset counted a conference paper and its journal extension as two studies, violating this manuscript's own independence rule. All C3 counts are recomputed from the repaired dataset and are now generated from it rather than maintained in prose. Change list in `CHANGELOG.md` v1.9.*

*Prior revision (v0.21).*
*Reviewer-blocker revision. Superseded v0.20. The adaptation-chain evidence coding was rebuilt on two axes, separating what a source establishes about a stage from whether that stage's duration was measured; the forward citation search was re-executed against an explicit, published query and its counts corrected; absence and priority language was bounded throughout; and four bibliographic or evidential over-reaches were corrected. Change list in `CHANGELOG.md` v1.8; provenance for every quantity in `evidence_matrix.md`.*

---

## Abstract

A flexible intelligent metasurface (FIM) treats the physical shape of an aperture as an optimisation variable, and recent work places that variable inside high-mobility integrated sensing and communication (ISAC), where the delay–Doppler channel is strongly time-selective. Whether the combination is physically realisable turns on a question the system literature does not answer: which parts of the adaptation loop must follow fast channel variation, and which may follow slower geometric or statistical change. We treat that as an evidence problem rather than a modelling one. Seven architecture classes relevant to FIM evidence transfer are separated and given explicit transfer rules; FIM adaptation is decomposed into ten stages from sensing to stabilised radio-frequency operation, coded on two independent axes — what a source establishes about a stage, and whether that stage's duration is fully delimited, only partially delimited, or untimed; and every reported timing value in the reviewed set is recorded with its timed object, start event, end event, measurement status and architecture. Three results follow. First, the adaptation chain is not timed end to end on any one object in the reviewed set: no reviewed source fully delimits more than five of the ten stages, only one reaches five, and none couples channel estimation to a commanded shape change. Counting partially delimited stages as well the maximum is six, reached by two platforms that are disjoint in the decisive respect — the one that commands a shape has no radio-frequency layer, and the one that radiates treats shape as an imposed disturbance. Stabilised radio-frequency operation is itself quantitatively measured on five platforms and delimited on one, which holds its geometry static. Second, two convenient simplifications need qualification: the numerical ranges reported for electronic and for mechanical processes overlap, so an architecture label alone does not establish a latency ordering; and an element-level update time cannot stand in for an aperture-level configuration time, as one panel's two bounds — below 0.1 ms per element, below 10 ms per 16 × 16 tile — demonstrate. Third, tracing the hardware-feasibility premises of the FIM system papers audited here back to the mechanical studies they cite shows an element-level response time presented as a surface morphing period, a tabulated value with no counterpart in the cited paper's complete published package, and a load-bearing shape-reuse assertion carried by a footnote without a bound, an experiment or a sensitivity analysis. A forward citation search of the three primary hardware sources through the OpenAlex citation graph reduced 306 citing records to 262 unique works and screened these down to 20 distinct candidate system studies, of which 13 were readable in full, and found the substitution in four studies forming one connected co-authorship network; the other nine studies read cite the same hardware and attach no timing value, two of them fully author-disjoint. Seven studies are paywalled and unread, and because these values propagate only in body text, an author-disjoint instance among them cannot be excluded: the practice is documented within one collaboration network, every count is a lower bound, and no prevalence claim is made. We propose no hardware and no control algorithm, and we make no novelty claim for two-timescale or statistical-CSI operation, which the movable-antenna and FIM literatures already state. The contribution is the audit, together with a reporting set whose fields are motivated by observed reporting deficiencies and by four unresolved quantities: commanded actuation time for a radiating aperture, mechanical settling to an electromagnetically stated tolerance, post-deformation calibration duration, and the onset of trustworthy radiation after a commanded change of shape.

**Index terms** — Flexible intelligent metasurface, reconfigurable intelligent surface, integrated sensing and communication, high mobility, adaptation latency, hardware validation, evidence synthesis, conformal metasurface.

---

## 1. Introduction

### 1.1 A degree of freedom that has to be actuated

A reconfigurable intelligent surface (RIS) changes how it scatters by changing the electromagnetic state of its meta-atoms. A flexible intelligent metasurface changes how it scatters by changing where its elements are. In the system-level formulation, each radiating element carries a coordinate along the surface normal; the vector of those coordinates defines the surface shape; the shape enters the array response through the propagation phase; and it is then optimised jointly with beamforming or sensing objectives, subject to a morphing range [1, Eqs. (1a)–(3), p. 13321; 2, Eq. (1)]. Simulated gains are reported across several formulations — a transmit-power reduction of about 3 dB at a one-wavelength morphing range for a multiuser downlink [2], further gains from introducing and then optimising a surface in a doubly dispersive multiple-input multiple-output ISAC setting [1, p. 13328], and element movement reported as more effective than passive phase control at enhancing received signal strength in a single-input single-output multipath scenario, with joint optimisation better still [3, p. 6823].

What separates this degree of freedom from every other one in the reconfigurable-surface literature is that exercising it requires moving matter. An electromagnetic state change propagates at the speed of a tuning mechanism. A geometry change propagates at the speed of an actuator, a structure and its damping. The system models do not represent the difference, and are not obliged to: in all four FIM system papers reviewed here the shape is a variable that may be set, and the mechanism that sets it lies outside the model.

### 1.2 Why high mobility turns an omission into a question

Idealised actuation is a harmless abstraction while the environment is quasi-static. It stops being harmless when the same framework is carried into high mobility, because the state the surface was configured for goes on changing while the surface responds, and no source in the reviewed set has measured how long the surface takes.

It is worth being precise about what mobility does and does not establish, because the imprecision is the origin of much of what follows. At the operating point of the high-mobility FIM–ISAC study reviewed here — 28 GHz, a maximum velocity of 208 m/s — the maximum Doppler shift is approximately 19 kHz.¹ That figure fixes a *regime*: strongly time-selective, well beyond the carriers and velocities at which reconfigurable-surface hardware has been characterised. It does not fix an *interval*, because a coherence interval is a threshold-dependent correlation statistic and the threshold is a choice. And it does not fix a *deadline*, because a deadline additionally requires a performance tolerance that somebody has selected. This review keeps the three apart throughout, converts none of them into the others, and defines no deadline of its own.

The question that remains is not whether the surface is "fast enough", which cannot be answered without a deadline. It is which operations in the loop are bound to the fast-varying state at all — and that is a question about physical processes and measurements, not about modelling preferences.

### 1.3 Why one reported response time cannot answer it

The natural move is to look up how quickly a flexible metasurface reconfigures. The literature appears to supply the number. It does not, and the reason organises this entire review.

Consider one measured platform: a scalable one-bit PIN-diode RIS with an FPGA integrated into each tile [4]. Its abstract reports an update time below 0.1 ms; its results section reports that a tile can be reconfigured in under 10 ms. Both are correct, and they differ by up to two orders of magnitude, because they time different objects — one element, and then 256 of them. Neither is the interval a system designer needs, which begins when the channel or the geometry is observed and ends when the far field is stable.

The pattern repeats at every level of the stack. A liquid-crystal RIS reports approximately 15 ms and 72 ms, but those are switch-on and switch-off transitions of a 4.6 μm material layer between 10 % and 90 % thresholds [5]. A flexible microwave metasurface reports 16.76 ms, but that interval runs from shape acquisition to bias-voltage supply and contains neither the deformation that produced the shape nor any settling afterwards [6]. A programmable mechanical surface reports response times within 0.1 s, but the object is a filamentary metal mesh with no meta-atoms, no bias network and no ground plane [7]. A soft shape-programmable surface reports approximately 30 ms — for an isolated ribbon, against approximately 300 ms for a full surface developing from flat [8].

These are not competing estimates of one quantity. They are measurements of different quantities, on different architectures, with different definitions of when the clock starts and stops. Averaging them, ranking them, or quoting any one of them as *the* FIM response time yields a figure with no physical referent. The useful alternative is to keep them apart and ask what survives the separation.

### 1.4 What the adjacent reviews already establish

Three broad reviews in the reviewed set border this territory and partition it cleanly enough to leave a specific hole.

Saifullah *et al.* classify tunable metasurfaces by tuning mechanism and rank their speeds qualitatively: electrical tuning is preferred above kilohertz modulation rates, liquid crystal modulates below about 1 kHz, microfluidic tuning operates on a millisecond scale, and mechanically stretchable substrates are slow, environmentally sensitive and unable to address individual unit cells [9]. The coverage of mechanisms is thorough and there is no discussion of ISAC. Tishchenko *et al.* survey multi-functional and hybrid RIS for ISAC, treat controller and network latency as a practical constraint, and link higher carrier frequencies to shorter coherence times [10]; there is no discussion of mechanical tuning. Ma *et al.* survey reconfigurable and movable antennas and state the position closest to ours: mechanical movement is generally slower than electronic reconfiguration; instantaneous-CSI position optimisation suits quasi-static environments with long coherence times, while fast fading calls for statistical-CSI approaches that reduce movement frequency; and hierarchical cross-layer control, in which statistical information guides slow movement while rapid state changes are decoupled, is an open direction [11, pp. 3, 20, 26–27]. The same survey argues that future models should incorporate inertia, settling time, friction, backlash, movement accuracy and energy rather than idealised instantaneous positioning.

Two consequences follow, and the first is a constraint on what this manuscript may claim. **The slow-geometry, fast-electronics division of labour is established rather than novel**, and neither this review nor any FIM paper may present it as new: statistical-CSI FIM optimisation has been published [12, 13], a two-rate schedule — element movement per subframe, phase adjustment per time slot — is already embedded in a FIM channel-estimation protocol [3, p. 6829], and delay-aware modelling of reconfigurable apertures has begun in the adjacent fluid-antenna literature [14]. The second is that none of the three reviews concerns FIMs at all: a full-text search of each returns no occurrence of "FIM" or "flexible intelligent metasurface".² Ma *et al.* recommend that models include movement time, settling and energy; no reviewed source establishes which of those quantities have been measured, on what object, or under what definition.

### 1.5 The question, and how it is answered

> **Which operations in a FIM-assisted high-mobility ISAC system must track fast channel variation, which may follow slower geometric or statistical change, and how well are the resulting timescales supported by existing hardware and control demonstrations?**

We answer it as an evidence-mapping problem rather than a design problem. Three instruments do the work, and each is introduced where it is first needed. An architecture taxonomy (Section 3) separates systems that share a name but not a physical mechanism, and states which measurements may transfer between them. A ten-stage decomposition of the adaptation chain (Section 5) makes it possible to say which process a given number times. A timing register (Section 6) records, for every reported value, the object timed, the start event, the end event, the measured-or-simulated status and the architecture — so that a measurement made on a mechanical mesh is never permitted to stand in for a measurement on a radiating aperture.

### 1.6 Contributions

Within the literature reviewed here and the searches recorded in Section 2:

**C1 — A stage-resolved adaptation-chain decomposition specific to FIMs, coded on two independent axes.** Ten stages from sensing to stabilised radiation, with each source's treatment of each stage classified twice: what the source *establishes* about the stage, and — separately — whether the stage's *duration* was measured. The separation is what makes the resulting counts mean anything, because several stages in this literature carry strong quantitative radio-frequency measurements and no timing at all. The timing axis distinguishes a **fully delimited** stage duration, with identifiable start and end events, from timing information that is only **partially delimited** — a share of an aggregate interval, a rate factor, a residual, or a chosen wait. **No reviewed source fully delimits more than five of the ten stages, and only one reaches five: a mechanical surface that commands its shape but has no radio-frequency layer, timing S1–S2, S4–S5 and S7.** Counting partially delimited stages as well, the maximum rises to six and two platforms reach it; the second is a flexible aperture that radiates but does not command its shape, which associates timing with S1–S2, S4–S6 and S10 while individually delimiting four of them. The two remain disjoint in the way that matters — one carries the radio-frequency stages and cannot command a geometry, the other carries the mechanical stages and does not radiate. No source times channel estimation together with a commanded shape change; calibration is timed by no reviewed source under either reading; and stabilised radio-frequency operation, though quantitatively measured on five platforms, is delimited on one, which holds its geometry static throughout.

**C2 — A timing register with explicit definitions, and the two simplifications it qualifies.** Recording start and end events shows that an element-level update time cannot be substituted for a tile- or aperture-level configuration time — the same panel reports both, up to two orders of magnitude apart — and that the ranges reported for electronic and for mechanical processes overlap once the tuning mechanism is named, a liquid-crystal switch-off exceeding a measured multi-stage electronic compensation chain on a flexible surface.

**C3 — A traceability audit of the hardware-feasibility premises used by the FIM system papers examined here.** Three premises are traced to their primary sources, and the primary measurement is compared with the value in circulation. A forward citation search of the three primary hardware sources — 306 citing records reduced to 262 unique works, screened to 24 records forming **20 distinct candidate system studies**, of which **13 were readable in full and 7 are paywalled** (Section 8) — finds the substitution in four studies, and finds no author-disjoint group reproducing it within that window: the four form one connected co-authorship network. The other nine studies read in full cite the same hardware and attach no timing value at all, two of them fully author-disjoint. Because propagation appears only in body text, the seven unread studies could contain further instances, including author-disjoint ones. This is therefore a documented finding about one collaboration network, bounded by full-text access; every count is a lower bound, and no prevalence claim is made.

**C4 — A reporting framework** in which each field is motivated by a recurring reporting deficiency or by a specific unresolved quantity identified in the reviewed set, and which prescribes definitions rather than acceptance thresholds.

We propose no hardware, no algorithm and no control architecture. The manuscript is an audit, and its value stands or falls on the accuracy of its citations.

---

*Footnotes*

¹ Derived by us from the source's stated parameters (f_c = 28 GHz, v_max = 208 m/s) as f_D = v f_c / c; the source does not report this quantity. Converting a Doppler shift into a coherence time requires a correlation criterion that varies by convention, so we do not do so. Section 4 restates the figure at the precision the argument needs.

² Full-text search with ligature normalisation — the extracted text renders "fi" and "fl" as single glyphs, which defeats naive searching — returning zero occurrences in each of the three documents.

---

## 2. Scope, corpus and method

### 2.1 Article type

This is a **structured critical review**. It is not a systematic review, a systematic mapping study or a scoping review, and it does not adopt PRISMA terminology, because it does not satisfy the requirement those labels carry: a reproducible, protocol-driven, multi-database *search*. What it does possess is a reproducible *extraction* protocol, and the distinction is worth stating plainly rather than blurring, since misdescribing a method is the kind of failure this manuscript examines in others.

### 2.2 Corpus

The reviewed set comprises **24 distinct research contributions across 31 files**. They are *distinct* rather than *independent*: several share authors, and the independence groups below record where. Four of those files are supplementary-information or peer-review documents belonging to two of the papers; they are evidence *about* those papers, not evidence alongside them, and are not counted as separate contributions. Duplicate versions, conference-and-journal pairs and same-group design lineages were identified and collapsed into independence groups, so that related publications are never counted as mutual confirmation of one another. Three sources were readable only as page images and no load-bearing claim is drawn from them.

The corpus was assembled by convenience rather than by a protocol-driven database query. Inclusion criteria are therefore stated retrospectively, and describe what the set *is* rather than a prospective filter: peer-reviewed articles, preprints and author manuscripts concerning FIM system modelling; flexible or conformal reflective and transmissive metasurface hardware; programmable mechanical surface actuation; electronically reconfigurable RIS hardware reporting timing or power; high-mobility channel estimation for reconfigurable surfaces; and reviews of any of these. Sources with no wireless, electromagnetic or mechanical-actuation content were excluded.

Six sources were first read as preprints or author manuscripts. Publisher-deposited records confirm versions of record for five of them, and the published full texts of the three that carry the most weight — the high-mobility FIM–ISAC study, the FIM architecture-and-performance paper and the high-mobility channel-estimation paper — were obtained and inspected. Every load-bearing timing and parameter quantity keyed to them survives at the published locators, which this manuscript cites. One non-timing claim did not survive, and is reported in Section 11.4 as an instance of why the check was worth performing.

### 2.3 Searches

Two kinds of search supplement the corpus, and their evidential weight differs.

**A documented but non-systematic external search** (ten queries, 17 August 2026) established whether a FIM-specific review exists, whether two-timescale or statistical-CSI FIM control is already published, whether any measured FIM actuation latency exists, and where the hardware-feasibility timing claims in the FIM system literature originate. It used a general web-search interface, which does not expose reproducible hit counts; its results are recorded as search outcomes rather than as established absences.

**A forward citation search** (18 August 2026) is reproducible, and its two stages are reproducible in different senses, which we distinguish rather than blur.

*Stage one is automatic and exact.* Every work citing the three primary hardware sources was retrieved through the OpenAlex citation graph — 160, 102 and 44 citing records for the filamentary mechanical platform, the soft shape-programmable surface and the flexible microwave metasurface respectively — giving 306 records and **262 unique works** after deduplication by identifier. Title and abstract were screened against an explicit forty-seven-alternative wireless and communications expression, reducing these to **65**. The seed identifiers, the query, the deduplication rule and the expression in full are published as a runnable script alongside this manuscript, and re-executing it reproduces the retrieval and this screen exactly.

*Stage two is manual and is recorded rather than re-derived.* Excluding optics, photonics, materials, mechanics and imaging work leaves 24 records, which collapse under the independence rule below — a preprint and its version of record are two versions of one study, and a conference paper and its journal extension are one lineage — into **20 distinct flexible-metasurface or reconfigurable-surface system studies**. Identifier-level deduplication does not perform that collapse by itself; four version groups occur here, of which only one is a duplicate index of a single work, the other three being genuine conference-to-journal or preprint-to-record pairs. Every one of the 262 works carries a row in the published screening table giving its stage-one result, its stage-two decision and the reason for it, its full-text status and its final role, so that a reader can audit each judgement individually.

**Thirteen of the 20 studies were read in full**, from arXiv author deposits, one open institutional repository, one open conference deposit and the corpus; each was scanned for timing terminology after ligature normalisation and hyphenated-linebreak repair, and every match was read in context. **Seven are behind publisher paywalls with no open deposit located and were not read; no access control was circumvented.** Every count arising from this search is therefore a lower bound, and Section 8 states what does and does not follow from that bound.

### 2.4 Extraction protocol

Extraction, unlike search, followed a fixed protocol applied uniformly to every source:

1. **A seven-class architecture taxonomy** with explicit transfer rules (Section 3), assigned before any timing value was compared.
2. **A ten-stage adaptation-chain template** (Section 5), against which each source's treatment of each stage is coded on **two independent axes**. Collapsing them into one symbol is what allowed a radiation-pattern measurement to be counted as a measured latency in an earlier draft of this review, so the separation is stated here rather than left to Section 5.

   **Axis A — stage evidence status**, answering *what did this source establish about this stage?* **Q** quantitatively measured (a physical or radio-frequency quantity is reported); **D** demonstrated (shown working, no quantity); **S** simulated; **A** assumed; **✗** absent; **n/a** not applicable to that architecture; **?** unclear; **RS** review statement (an assertion in a survey, carrying no primary evidence of its own).

   **Axis B — timing-evidence status**, answering *what is known about the duration of this stage?* This axis is **not** a binary record of whether a number exists. It has three values:

   - **·T — fully delimited.** A duration is reported for this stage together with an identifiable start event and an identifiable end event, and the stage's own contribution is separable from its neighbours. Only a `·T` cell licenses the verb *times*.
   - **·(T) — partially delimited.** Timing information is associated with the stage, but at least one of the following is unresolved: the start event, the end event, the stage's separation from an adjacent stage, or the fact that the figure is a share of an aggregate interval rather than an independently measured one. A quantity that is a *rate factor*, a *residual* of a larger measurement, an *accuracy* rather than a duration, or a *chosen* wait rather than an observed one is coded `·(T)`, never `·T`.
   - *no marker* — **untimed.** No duration is associated with the stage, whatever else is known about it.

   The two axes are orthogonal: `Q` without a marker (a measured pattern with no duration) and `S·T` (a fully delimited *simulated* runtime) are both routine in this literature, and both would be misread under a single code. Counts reported in this manuscript state which axis they are counting, and where the totals differ under the two axes, both are given.
3. **A timing register** (Section 6) in which every reported value carries a timed object, a named start event, a named end event, a measured/simulated/projected/derived flag, the architecture on which it was obtained, and a comparability class. Two values may be compared only if their comparability classes intersect.
4. **A seven-level evidence ladder**: **L1** analytical or model-based derivation; **L2** communication-system simulation; **L3** full-wave electromagnetic simulation of the actual structure; **L4** component measurement (a unit cell, sensor, actuator or delay line); **L5** prototype radio-frequency measurement of an assembled aperture; **L6** over-the-air demonstration of a working link or application; **L7** end-to-end closed-loop validation — observation, decision, actuation and *verified, timed* stabilised radio-frequency performance. Evidence is never upgraded across levels: a system simulation is not hardware validation, a measured actuator is not a radiating system, and an electronic switching time is not a mechanical settling time. **No reviewed source reaches L7**, and the reason is given in Section 9.3.
5. **An independence rule.** A preprint and its version of record are two versions of one study. A conference paper and its journal extension are one lineage. Supplementary material belongs to its parent paper. Independence between citing works is tested by author-set intersection, not assumed from differing first authors.
6. **An absence-claim rule.** Every statement about what is missing is reduced to one of two checkable forms: *this named document does not report quantity Q*, or *across the N sources in this named table, no row records Q*. No statement about the field as a whole is made anywhere in this manuscript.

### 2.5 What follows from the method

Two constraints are inherited by everything downstream. Absence of a measurement in the literature we read is not evidence that the measurement does not exist, still less that the capability is unattainable; every absence statement below is bounded to the reviewed set or to the searches above. And **no reviewed source reports a repetition count or a dispersion figure for its headline response, morphing or adaptation interval**, so none of the values on which this review's arguments turn carries an uncertainty. The qualification matters: one subordinate process quantity in Table 5 does carry a dispersion — a function-evaluation cycle stated as 0.35 ± 0.15 s — so the deficiency is specific to the headline intervals rather than universal across the register. It is a deficiency in the sources rather than in the extraction, and additional literature cannot retroactively supply uncertainty for values already published without it; closing it would require the original raw data, a reanalysis, repeated measurements, or new experiments. Section 11.4 states the remaining limitations in full.

---

## 3. Seven architecture classes relevant to FIM evidence transfer

### 3.1 Why the taxonomy comes first, and what it is a taxonomy of

Evidence about FIM feasibility is drawn from seven physically distinct kinds of system, and a statement true of one is routinely false of another. A response time measured on a filamentary mechanical mesh, an update rate measured on a rigid PIN-diode panel and a compensation loop measured on a bending varactor-loaded sheet are not three data points describing one technology; they describe three technologies whose measurements are nonetheless quoted in support of one architecture. Everything in Sections 5 to 9 depends on keeping them apart, so the separation is made first.

**These seven classes are not seven things called "flexible metasurfaces".** Only A1 through A4 are named as flexible or morphing metasurfaces by the literature that uses them, and even there the naming is inconsistent. The remaining classes are included because the FIM literature draws evidence from them, not because their authors claim the label:

- **Direct classes — the object under review.** A1 the theoretical FIM, A2 flexible passive reflective metasurfaces, A3 externally deformed shape-aware programmable surfaces, A4 actively self-morphing mechanical surfaces. These share a physical premise — a surface whose geometry is not fixed — and are the classes over which the review's central claim is made.
- **Comparator and evidence-donor classes.** A5 rigid electronically reconfigurable RIS, A6 movable and reconfigurable antenna systems, A7 flexible active antenna arrays. Their authors do not generally call them flexible intelligent metasurfaces, and this review does not either. They appear because they supply the timing comparators, the control-architecture vocabulary and the strongest deformation-aware radio-frequency demonstration in the reviewed set, and because values measured on them are quoted in FIM feasibility arguments. Naming them precisely is what makes the transfer rules of §3.6 statable at all.

Three questions distinguish the classes: **what physically changes**; **whether the change is imposed from outside or commanded by the system**; and **whether the radio-frequency state is independently programmable**. Table 1 answers them, together with the questions that decide what a measurement is worth — whether the shape is sensed, whether radio-frequency performance was measured at all, and whether any mobility was involved. The prose below does not restate the table; it draws the four conclusions the table makes visible.

**Table 1 — Architecture classes drawn on by the FIM evidence base.** A1–A4 are the direct classes; A5–A7 are comparator or evidence-donor classes whose authors do not generally use the FIM label.

| Class | What it is | What changes | Deformation source | RF state programmable | Shape sensed | RF measured | Mobility evidence | Representative sources |
|---|---|---|---|---|---|---|---|---|
| **A1** | Theoretical FIM array with independently movable elements | element coordinates | an optimisation variable — no mechanism specified | in some formulations | n/a | ✗ — no hardware | simulated only | [1], [2], [3], [15] |
| **A2** | Flexible **passive** reflective metasurface | sheet curvature | external | ✗ | ✗ | ✓ at fixed curvatures | ✗ | [16], [17] |
| **A3** | Externally deformed, shape-aware **programmable** reflective surface | curvature **and** meta-atom state | external | ✓ | ✓ ([6]) / a priori ([18]) | ✓ | ✗ | [6], [18] |
| **A4** | Actively self-morphing mechanical surface | commanded local displacement | **self-actuated** | **no RF layer at all** | ✓ ([7], stereo imaging) | ✗ | ✗ | [7], [8] |
| **A5** | Rigid electronically reconfigurable RIS | meta-atom state only | none | ✓ | n/a | ✓ | ✗ | [4], [5], [19] (modelled) |
| **A6** | Movable / reconfigurable antenna system | position, orientation or internal state | self-actuated | ✓ (RA sub-class) | — | outside the reviewed measurement scope | — | [11] (review) |
| **A7** | Flexible **active** antenna array | sheet curvature | external | ✓ (per-element RFIC) | ✓ (on-chip self-sensing) | ✓ | ✗ | [20], [21] |

### 3.2 A1 is a model class, and the platforms cited for its plausibility are A4

No source in the reviewed set demonstrates A1 hardware. The FIM system papers define the surface as a coordinate vector constrained to a morphing range and entering the array response through the propagation phase [1, Eqs. (1a)–(3), p. 13321]; they specify no actuator, no sheet mechanics, no inter-element mechanical coupling and no fabrication route. Where physical plausibility is argued, two mechanical platforms are cited: a liquid-metal microfluidic network in an elastomeric matrix, and an array of metallic filaments actuated by distributed Lorentz forces [1, p. 13320], citing [8] and [7] respectively.

That is a plausibility argument and should be read as one. Both cited platforms are A4: they carry no meta-atoms, no bias network, no dielectric substrate and no radio-frequency ground plane. The distinction is not pedantic, and the reviewed set contains a direct measurement of why. When a flexible reflective microwave surface was actually built, achieving mechanical flexibility required replacing a solid copper ground with a serpentine mesh — a change reported to reduce estimated bending stiffness by more than two orders of magnitude [6, p. 3]. The mechanical properties of a radio-frequency-loaded aperture are a design outcome, not a property inherited from the actuator concept, and nothing in the reviewed set bounds the difference.

### 3.3 The realised flexible apertures invert the control problem

The two realised surfaces in the reviewed set that are simultaneously flexible, reflective and electronically programmable are A3, and they share a property that the A1 formulation reverses.

In the flexible microwave metasurface with shape-guided adaptive programming [6], a 480 × 240 mm sheet carrying 32 × 16 meta-atoms is bent by an external mechanical platform. A conformal array of 32 strain sensors reconstructs the shape — one reported validation gives a root-mean-square deviation as low as 2.36 mm at a maximum displacement of 45 mm — and a trained neural network maps the reconstructed shape to the column bias voltages that restore the intended electromagnetic behaviour. The loop closes on *geometry*: the surface senses a shape it did not choose and compensates for it electronically. There is no channel estimator anywhere in the system. In the conformal reconfigurable reflectarray built from polydimethylsiloxane and printed liquid metal [18], a 10 × 10 array at 9 GHz with per-element PIN diodes achieves ±45° beam scanning and 16.13 dBi peak gain using element-level conformal compensation phase; the prototype is mounted on acrylic supports of different bending degrees, so each curvature is a separate static experiment and the surface neither senses nor commands its shape.

The A1 formulation inverts this. There, geometry is the *primary control variable* — the thing chosen to maximise an objective — and the channel is what is being tracked. **No source in the reviewed set demonstrates that inversion in hardware.** This is the single most consequential fact in the taxonomy, and Sections 5 and 9 return to it.

### 3.4 The platforms that command a shape have no radio

The two A4 platforms supply every measured mechanical timescale in this review, and neither has an electromagnetic function. The filamentary mechanical metasurface [7] is a 4 × 4 mesh of thin metal and polyimide traces on an 18.0 mm sample, driven by distributed Lorentz forces in a 224 ± 16 mT field at currents below 27.5 mA, achieving reversible out-of-plane deformation of about 30 % of the sample length; uniquely in the reviewed set it closes a loop on shape, with in-situ stereo imaging feeding an experiment-driven, self-evolving inverse design. Its demonstrations are optical, structural and multifunctional, and no wireless beamforming is reported. The soft shape-programmable surface [8] uses liquid-metal microfluidic ribbons in an elastomer, actuated by Lorentz forces, and can fix a programmed shape through a liquid-metal phase transition — a mechanism by which a slowly-set geometry could in principle be held without continuous actuation. It reports no reflection phase, gain, radiation pattern or communication result.

These are the right platforms to cite for mechanical feasibility. They are the wrong platforms to cite for a FIM response time, and Section 8 shows that the distinction has not always been maintained.

### 3.5 Fixed-curvature conformal design is substantial prior art, and it is prior art about a different problem

A large body of conformal work concerns apertures whose shape is known and does not change. Rigorous synthesis of planar and conformal beamforming metasurfaces using integral-equation models that account for finite size, coupling and spatial dispersion is established, with a conformal reflectarray among the worked examples [22]. A reduced-order coupled-dipole model of a cylindrically conformal waveguide-fed metasurface agrees closely with full-wave simulation near 28 GHz at large bend radii [23]. An active conformal metasurface lens achieves up to about 195° of transmission-phase tuning and ±60° beam coverage using multiple feeds [24]. Cylindrical RIS design has been carried from idealised surface-impedance synthesis through one-bit meta-atom implementation and validated by full-wave simulation [25]. A 3D-printed curved substrate with voltage-programmable two-bit coding deflects between 0° and 50° over 9.3–10.5 GHz with pointing accuracy better than ±2° [26]. A flexible 15 × 15 liquid-metal-on-PDMS reflectarray maintains favourable radiation characteristics across a ±25 % bending range with a fixed one-bit coding pattern [17].

Taken together these establish that validated design methods and measured hardware exist for important fixed-curvature cases, across several bands, phase resolutions and synthesis approaches. That is prior art, not closure — none of these results claims to bound the general problem, and curvature, oblique local incidence and finite phase resolution remain aperture- and band-specific design constraints. What the group does not address is *change*: none of these surfaces tracks a varying shape, and none reports how long any of its operations takes. **Bending tolerance under a fixed coding pattern is a robustness result, not an adaptation result.**

The adjacent classes contribute in a similar way. Movable and reconfigurable antenna systems (A6) supply the conceptual vocabulary — fast internal state changes, slow physical repositioning, and the resulting case for instantaneous channel information in quasi-static environments and statistical information in fast fading [11] — without supplying FIM measurements. Flexible active antenna arrays (A7) supply the strongest evidence that large flexible coherent apertures are physically realisable: two 256-element, 30 × 30 cm arrays remain fully functional and programmable at concave and convex bend radii below 23 cm, with closed-loop focusing driven by feedback from a remote receiver and calibration explicitly targeting phase offsets caused by manufacturing variation, **shape deformation** and environmental change [20]. Section 6.5 returns to what that demonstration does and does not tell us.

### 3.6 Transfer rules

These follow from §§3.2–3.5 and are applied without exception in the remainder of the manuscript.

1. **A4 timing does not transfer to A1 or A3 without qualification.** A4 platforms have no radio-frequency layer; their measured response times bound a different mechanical object.
2. **An A5 electronic switching time is not a mechanical settling time.**
3. **An A3 partial-loop latency is not a full-loop latency.** The interval reported for the flexible microwave metasurface begins at shape acquisition and ends at bias-voltage supply; it contains no deformation and no radio-frequency settling.
4. **A7 is not A5.** An active array's calibration architecture — self-sensing receivers closing a loop against a remote beacon — does not carry over to a passive reflective aperture, which has neither.
5. **A2 bending tolerance is not adaptation.**
6. **Fixed curvature is not variable geometry.**
7. **Protocol units are not durations.** Subframes, time slots and iteration counts are structure, not time, and none of the sources reporting them supplies the numerology needed to convert.

### 3.7 The shape of the gap

Figure 1 maps the reviewed hardware on two axes that are properties of an experiment: *has the platform demonstrated commanded physical geometry?* and *has radio-frequency performance been measured on it?* The map is drawn over **physically demonstrated platforms only**, and the restriction is deliberate — a modelling paper answers neither question, because it performs no experiment, and placing simulation work in a hardware quadrant would be a category error.

| | **RF performance measured** | **RF performance not measured** |
|---|---|---|
| **Commanded geometry demonstrated** | *(empty)* | A4: [7], [8] |
| **Commanded geometry not demonstrated** | A2, A3, A5, A7: [6], [18], [17], [16], [5], [4], [25], [26], [24], [27]/[28], [20] | A6 platforms outside the reviewed measurement scope |

**One cell is empty: commanded geometry demonstrated *and* radio-frequency performance measured.** No reviewed hardware demonstration sits there.

**A1 does not occupy a cell in this map. It names the cell.** The A1 system model is not physical evidence to be classified; it is the specification of the operating point the empty cell describes — geometry chosen by the optimiser, on an aperture whose radiation is what the optimisation is for. Drawn that way, the map states the review's central structural finding without misdescribing anybody: the modelled target operating point is the one for which no measured platform exists.

> **Figure 1.** *Architecture–evidence map of the reviewed hardware.* Both axes are properties of an experiment, so only platforms that performed one are plotted; the theoretical FIM performs none and is drawn as an annotation on the empty cell rather than as a platform. The empty cell is the review's central structural finding: commanded geometry and measured radio-frequency performance have not been demonstrated together. *(File: `figures/fig1_architecture_evidence_map.pdf`.)*

---

## 4. What the surface is being asked to track

### 4.1 Three quantities that must not be collapsed

The phrase that does most damage in this literature is "within the coherence time", because it is read as "while the channel is constant". It is not. Coherence time is the duration over which multipath fading remains strongly *correlated*, and the correlation threshold is a choice.

The consequence is measurable. In a RIS-assisted high-mobility study at 2.6 GHz with a user moving at 90 mph, the interval over which the time-correlation function exceeds 0.5 is estimated to cover **only 51 symbols** [19, p. 721]; the same paper's bit-error-rate comparison uses coherence durations of 20 symbol periods at 0.95 correlation and 40 symbol periods at 0.82 correlation [19, Fig. 4(b), p. 728]. One scenario, three answers spanning a factor of 2.5, differing only in where the threshold was placed. The paper's own framing is that RIS channel-estimation techniques assuming perfectly time-invariant block fading suffer irreducible error floors precisely because the fading varies, albeit in a correlated way, *within* the coherence time. One caution attaches to these figures and we state it rather than suppress it: they are simulation results. We report them as symbol counts and do not convert them to wall-clock time, because the symbol count is what carries the argument and a derived millisecond figure would invite exactly the decontextualised quotation this review examines.

At the high-mobility FIM operating point — 28 GHz, 0.0107 m wavelength, 20 MHz bandwidth, four transmit and four receive elements, maximum velocity 208 m/s [1, Table III, p. 13327] — the maximum Doppler shift is approximately **19.4 kHz**.¹ Three quantities must be kept apart, and conflating them is the commonest way this comparison is made badly:

- a **Doppler frequency** follows from carrier and velocity, and 19.4 kHz is exact given the stated parameters;
- a **correlation interval** is a threshold-dependent statistic requiring a correlation model and a stated criterion, and the reviewed set contains none at 28 GHz — its only quantified figure comes from a different scenario at 2.6 GHz;
- an **update deadline** additionally requires a performance tolerance that somebody has chosen, and **this review defines none**, here or anywhere else.

What the Doppler figure establishes on its own is a regime, not an interval. We therefore do not convert 19.4 kHz into a time, and no sentence in this review should be read as doing so.

### 4.2 The states are plural, and they do not share a clock

Treating "the channel" as one clock obscures that a FIM-assisted ISAC system tracks several states with different rates and different consequences for failure. Table 2 separates them. Its purpose is to make the load-bearing question askable: *which of these states actually drives the shape optimisation, and when does that state go stale?*

**Table 2 — States a FIM-assisted ISAC system must track, their governing drivers, and the evidence available for each.** No column of this table contains an update deadline, and none is derivable from it; assigning one requires a performance tolerance the reviewed sources do not supply.

| State | What drives its variation | Which control variable it binds | Evidence in the reviewed set | Status of that evidence |
|---|---|---|---|---|
| **Instantaneous complex fading** | Doppler — ≈19.4 kHz at 28 GHz, 208 m/s | electronic phase state, and shape *if* shape is optimised per realisation | Doppler figure derived by us; 51-symbol >0.5-correlation window at 2.6 GHz | derived / simulated; **no measurement, and no interval at 28 GHz** |
| **Channel statistics and spatial correlation** | scattering environment, deliberately treated as slower than fading | shape, under statistical-CSI formulations | statistical-CSI FIM optimisation is published [12, 13]; the instantaneous-versus-statistical distinction is argued in [11, p. 20] | modelling choice, adopted by the literature; **rate not measured** |
| **Angles of arrival and departure; path geometry** | the user's traverse across the cell, not the fading | shape, beam direction | high-mobility models update angles explicitly and separately from fading correlation [19] | modelled; the *separation* is established, the *ratio* is not |
| **Target kinematics (sensing subproblem)** | target motion, independent of the communication user | sensing waveform and shape | communication and sensing may impose different movement and update requirements [11, pp. 24–25] | argued in a review; unquantified for FIM |
| **Blockage** | environmental, typically event-like rather than periodic | triggers reconfiguration rather than setting a rate | not quantified for any reviewed flexible aperture | absent |
| **Surface geometry** | deformation of the aperture itself — aeroelastic, mechanical, or commanded | the compensation layer; the actuator, if commanded | ≈4 ms strain-sensor read and 16.76 ms compensation loop on a flexible aperture [6]; 60 Hz stated deformation-rate limit | measured, on **externally imposed** deformation |
| **Calibration state** | how long the geometry-to-response mapping remains valid after a shape change | when the aperture may be trusted again | closed-loop refocusing demonstrated on a deformed active array [20] | **capability demonstrated, duration not reported** |

Read down the last two columns and the asymmetry is stark. The states with the strongest claim to needing fast updates are supported by models; the states for which measurements exist are the geometric ones. Section 7 shows that this inversion — a demand side established by simulation and a supply side established by measurement — is the opposite of how the comparison is usually presented.

### 4.3 The literature itself offers the slow-geometry reading

It matters for what follows that the two-timescale reading is not this review's reconstruction. The version of record of the high-mobility FIM–ISAC study states both halves of the trade-off explicitly. It asserts on one hand that distributed Lorentz forces "enable rapid reconfiguration of the FIM surface shape within millisecond switching speeds", "comparable to typical channel coherence times in high-mobility wireless scenarios" [1, p. 13321]; and on the other that "the FIM surface shape can also be morphed once over several channel coherence intervals to achieve statistically optimal performance, thus offering a flexible trade-off between achievable performance gains and morphing speed requirements" [1, p. 13322].

The two halves pull in opposite directions, and both should be taken at face value. The second establishes that operating the geometry on a slower schedule than the fading is a design option the system literature already permits, so this manuscript's conditional framing in Section 11.1 is a premise supplied by that literature rather than one imposed on it. The first is an assertion about another paper's hardware, and Section 8 traces it.

A further FIM paper, located through our external search, makes the fast reading more precise and equally untested: FIM surface shapes "are only updated on the timescale of the channel's coherence block" [29]. That is a legitimate modelling choice and it makes the two-rate structure explicit. It also asserts that command transport, actuation, settling and any recalibration all complete inside one coherence block, which is exactly the proposition no reviewed measurement supports.

### 4.4 Overhead accrues before the actuator moves

Two costs are subtracted from whatever budget applies, before any hardware acts.

**Pilot overhead scales with the controlled element count.** The ON/OFF estimation protocol for a passive RIS requires 1 + M time slots to estimate the direct link and M reflected links sequentially [19, p. 720]. The FIM case acquires a two-dimensional measurement: Q subframes each containing T₂ time slots, with the element moving once per subframe and the phase adjusted once per time slot [3, p. 6829]. These are protocol units and we do not convert them to milliseconds — the sources supply no numerology — but their structure matters twice over. The overhead scales with the very quantity that makes a FIM attractive; and the FIM estimation protocol *already contains a two-rate schedule*, so the hierarchical structure a system architect might propose as a solution is present in the FIM literature as a modelling premise, before any hardware has been asked whether it can meet either rate.

**Computation is not free, and the expensive part is the part movement makes necessary.** One reviewed FIM paper reports wall-clock computation time, and it is the only such measurement on a FIM-specific algorithm in the reviewed set: running a clustering mean-field variational sparse Bayesian learning estimator on a stated desktop processor with a 400-iteration cap and a 10⁻⁸ stopping tolerance, the reported runtime rises from roughly 4 ms for a small virtual array to roughly 100 ms at a virtual array size of 324, with the slowest benchmark reaching about 1.2 s [3, Fig. 8, p. 6833].² Two features deserve attention. It is a desktop measurement and therefore bounds nothing for an embedded implementation — but it *is* a measurement, which distinguishes it from the iteration counts the other FIM papers report in place of durations. And it scales with virtual array size, the product of element count and movement slots: the computation that makes element movement useful becomes more expensive precisely as the movement becomes more ambitious. For comparison, the only other wall-clock computation figure in the reviewed set is neural-network inference on the flexible microwave metasurface at approximately 2 ms for 32 shape channels, on the authors' embedded implementation [6, p. 4]. The two are comparable in kind, and their difference in magnitude reflects what they compute: a small learned static map is cheap, and sparse recovery of a high-dimensional cascaded channel is not.

### 4.5 What Section 4 establishes

The demand side is characterised as far as the evidence allows, which is less far than a reader might expect. Fast fading at the reviewed operating point implies a Doppler shift of tens of kilohertz and a strongly time-selective regime; no coherence interval and no update deadline follow from that figure alone, and the reviewed set supplies neither at this carrier. Coherence intervals are threshold-dependent and, in the one quantified high-mobility case available, span tens of symbols. The angular, target, statistical and geometric states are distinct from the fading state and from each other; statistical-CSI approaches are built on that distinction, and the reviewed set fixes no relative rates among them. Pilot overhead and computation consume part of any budget before an actuator moves, and the FIM estimation protocol already assumes two different update rates.

None of this says what the hardware can do. The next two sections decompose the supply side into stages and record what has been measured for each.

---

*Footnotes*

¹ Derived by us as f_D = v f_c / c from the source's stated parameters; the source does not report this quantity. We deliberately do not convert it into a coherence time, since the constant of proportionality depends on a correlation convention that varies across the literature.

² Axis units read from the published figure, whose ordinate is labelled "Running time [Second]".

---

## 5. The adaptation chain

### 5.1 Why decompose at all

"FIM adaptation" names a sequence, not an event, and the sequence crosses three physical domains. Information is acquired by a sensor or a pilot; a decision is computed; a command is transported across an aperture; a semiconductor or a liquid crystal changes state; a structure accelerates, moves and rings down; and only then does the far field become trustworthy again. Each of those processes is governed by different physics, obeys a different scaling law, and would be measured on a different instrument. They have no reason to share a magnitude, and — as Section 6 shows — they do not.

The decomposition below is therefore not a taxonomy for its own sake. It is the instrument that makes it possible to say *which process a given number times*, and it is what turns an apparently contradictory set of reported latencies into a consistent picture. Ten stages are used, chosen so that each corresponds to a distinct physical or computational process that could in principle be timed independently:

| Stage | | Definition |
|---|---|---|
| S1 | Sensing / acquisition | physical observation of the surface or environment — strain sensors, imaging, received pilots |
| S2 | Geometry estimation | conversion of raw sensor data into a surface-shape estimate |
| S3 | Channel estimation | acquisition of instantaneous or statistical channel state |
| S4 | Optimisation / inference | computation of the desired geometry and phase configuration |
| S5 | Control transmission | transport of the command from the compute element to the surface controller |
| S6 | Electronic state update | meta-atom electromagnetic state change |
| S7 | Mechanical morphing | the commanded physical displacement |
| S8 | Mechanical settling | decay of transient motion to within tolerance of the target shape |
| S9 | Calibration | re-establishment of the geometry-to-RF-response mapping after the shape changed |
| S10 | Stabilised RF operation | the interval over which the configured surface delivers its intended behaviour |

The decomposition is deliberately finer than the literature's, and that is the point: the stages the system models collapse into "reconfiguration" are precisely the stages for which no measurement exists.

### 5.2 What each platform actually covers

Table 3 records what each reviewed source establishes about each stage, and — separately — what is known about the *duration* of that stage: fully delimited, partially delimited, or not timed at all. Keeping those two questions apart is not bookkeeping. Several stages in this literature carry strong quantitative radio-frequency measurements and no timing whatever: radiation patterns at a fixed curvature, a gain figure, a delivered power. Coding both under one symbol would let a pattern measurement be counted as a measured latency, which is a version of the same substitution this review documents in others.

**Table 3 — Adaptation-chain coverage, on two axes.**
*Stage evidence status:* **Q** quantitatively measured (a physical or RF quantity reported) · **D** demonstrated (shown working, no quantity) · **S** simulated · **A** assumed · **✗** absent · **n/a** not applicable to the architecture · **RS** review statement.
*Timing status, appended (three-valued — see §2.4):* **·T** **fully delimited** — a duration with identifiable start and end events, separable from its neighbours · **·(T)** **partially delimited** — timing information whose start event, end event or separation from an adjacent stage is unresolved, including a share of an aggregate interval, a rate factor, a residual, or a chosen wait · *no marker* untimed. The two right-hand columns count the `·T` and `·(T)` cells in each row.

| Source | Arch. | S1 sense | S2 geom. est. | S3 chan. est. | S4 optim. | S5 ctrl tx | S6 electronic | S7 morphing | S8 settling | S9 calib. | S10 stable RF | **·T** | **·(T)** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ranasinghe *et al.* [1]** | A1 | ✗ | ✗ | A | S | ✗ | ✗ | A (instant) | ✗ | ✗ | A — unbounded shape reuse | 0 | 0 |
| **An *et al.* [2]** | A1 | ✗ | ✗ | A (perfect CSI) | S | ✗ | ✗ | A (instant) | ✗ | ✗ | A (quasi-static) | 0 | 0 |
| **Yang *et al.* [3]** | A1 | ✗ | ✗ | **S·T** runtime | S | ✗ | A (per slot) | A (per subframe) | ✗ | ✗ | A | 1 | 0 |
| **Morales Sandoval *et al.* [15]** | A1 | ✗ | ✗ | A | S | ✗ | ✗ | A | ✗ | ✗ | A | 0 | 0 |
| **Xu *et al.* [19]** | A5 | S (pilots) | n/a | S | S | ✗ | A | n/a | n/a | ✗ | S | 0 | 0 |
| **Li *et al.* [6]** | A3 | **Q·T** ≈2 ms | **Q·(T)** RMSD 2.36 mm | ✗ **absent** | **Q·T** ≈2 ms | **Q·(T)** RS-232 residual | **Q·T** 5.25 ms supply | ✗ **external** | ✗ | D (folded into a learned map) | **Q·T**‡ | **4** | 2 |
| **Lu *et al.* [18]** | A3 | ✗ | ✗ (a priori) | ✗ | S | ? | D | ✗ (static) | ✗ | D per curvature | **Q** patterns | 0 | 0 |
| **Neuder *et al.* [5]** | A5 | ✗ | n/a | ✗ | ✗ | ✗ | **Q·T** 15 / 72 ms | n/a | n/a | ✗ | **Q** patterns | 1 | 0 |
| **Akram *et al.* [4]** | A5 | ✗ | n/a | ✗ | ✗ | **Q·(T)** ×¼ multiplexing | **Q·T** <0.1 ms / <10 ms | n/a | n/a | ✗ | **Q** patterns, power | 1 | 1 |
| **Bai *et al.* [7]** | A4 | **Q·T** stereo imaging | **Q·T** matching | n/a | **Q·T** search | **Q·T** voltage update | n/a | **Q·T** <0.07 s / <0.1 s | **Q·(T)** fixed pause | ✗ | ✗ **no RF layer** | **5** | 1 |
| **Ni *et al.* [8]** | A4 | ✗ | ✗ | n/a | ✗ (scripted) | **Q·T** ≈50 ms script | n/a | **Q·T** 30 / 300 ms | **Q·T** ≈250 ms | ✗ | ✗ **no RF layer** | **3** | 0 |
| **Gal-Katziri *et al.* [20]** | A7 | D self-sensing | D | ✗ | D | D | D | ✗ external | ✗ | **D — no duration** | **Q** ≈80 mW at 1 m | 0 | 0 |
| **Ma *et al.* [11]** | A6 review | RS | RS | RS | RS | RS | RS | RS — names movement time as a required model input | RS — names settling likewise | RS | RS | 0 | 0 |

‡ **The one cell that records two experiments.** [6]'s S10 must not be collapsed. In the dynamic-bending demonstration the geometry is changing — a QPSK video link is held at error vector magnitude around −20 dB while the surface is bent — and nothing is timed. In the second experiment an interval of 16.7 ms from trigger to stabilised radiation is recorded, and the geometry is **static** throughout. Writing "[6] times S10" without that condition would assert a post-morph stabilisation measurement that does not exist.

### 5.3 One platform fully delimits five stages; two associate timing with six, and they are disjoint

Three counts can be taken from Table 3, and they do not agree. Stating which one is meant is not bookkeeping — an earlier draft of this review reported "five stages, reached by two platforms", a figure that is not produced by any single consistent rule. It counted one platform's partially delimited cells as timed while discarding a fully delimited one, and the other platform's fully delimited cells while discarding its partially delimited one. The corrected counts are these:

- **Quantitatively evidenced stages (axis A, `Q`).** The maximum is **six**, reached by two platforms — [6] and [7].
- **Fully delimited stages (axis B, `·T`).** The maximum is **five**, reached by **one** platform, [7].
- **Stages carrying any timing information (`·T` or `·(T)`).** The maximum is **six**, reached by the same two platforms, [6] and [7].

**Only one reviewed source fully delimits as many as five of the ten stages, and it is the platform that does not radiate.** The filamentary mechanical metasurface delimits S1 sensing, S2 geometry estimation, S4 inference, S5 control transmission and S7 morphing, each with its own start and end events, inside a function-evaluation cycle of 0.35 ± 0.15 s [7]. It **has no radio-frequency layer**: S6, S9 and S10 do not exist on it. Its S8 settling is coded `·(T)` and is excluded from the five, because the 0.1 s appearing in its cycle budget is a **chosen wait**, not an observed settling duration.

**The flexible microwave metasurface associates timing with six stages but individually delimits four** [6]. S1 sensing, S4 inference and S6 electronic update are separately instrumented, and S10 is delimited in a second experiment discussed below. S2 and S5 are `·(T)`: the reported RMSD of 2.36 mm is an *accuracy*, not a duration, and its share of the aggregate interval is not resolved from S1, while the RS-232 figure is a **residual** of the 16.76 ms total rather than an independently timed transfer. The aggregate interval is real and is reported; what it does not do is delimit each stage inside it. The platform **does not command its geometry**: S7 is an external fixture.

Counted on the axis that permits a like-for-like comparison — any timing information at all — the two platforms tie at six and remain disjoint in exactly the way that matters. Their timed sets share S1, S2, S4 and S5, and differ in the two stages that decide the question: [6] carries S6 and S10, the radio-frequency side, and cannot command a shape; [7] carries S7 and S8, the mechanical side, and has no radio at all. Neither can be extended into the other by further measurement; the extension would require different hardware.

Both sets are **linked rather than contiguous**, and the distinction is not pedantry. S3, channel estimation, lies between S2 and S4 in the chain and is absent from both platforms entirely — neither has a channel estimator, because neither is trying to track a channel. A run that skips a stage the architecture never implements does not span the chain; it spans the part of the chain the architecture possesses. For the flexible aperture the correct statement of extent is **six of ten stages carrying timing information — S1–S2, S4–S6 and S10, with S3 absent, and only four of the six individually delimited** — and the hole at S3 is one of this review's findings rather than an accounting artefact.

Where a set ends matters as much as how large it is. For the flexible aperture, S8 is untimed, S9 does not exist as a runtime step having been folded into a pre-trained map, and S10 is delimited only with the geometry held still.

Every other source carries less: one delimited stage each for the rigid electronically reconfigurable surfaces [4, 5] — with a second, partially delimited stage in [4], a multiplexing *rate factor* that names no interval — three for the soft shape-programmable surface [8], and one for the FIM system papers, a desktop channel-estimation runtime [3] which is **simulated rather than measured** (`S·T`) and so delimits a computation, not a physical process. Most tellingly, **none at all for the flexible active array [20]**, which demonstrates seven of the ten stages as working operations and attaches a duration to no single one of them.

So: **no reviewed source fully delimits more than five of the ten stages, and the one that reaches five does not radiate; no source associates timing with more than six; no source times S3 together with S7** — none couples channel estimation to a commanded shape change; **no source times mechanical morphing, settling or calibration on a platform that radiates**; and **S9 is timed by no reviewed source at all, under either reading.** One source does delimit a complete run for a *fixed-geometry electronic compensation* chain, which is a different chain from the one a FIM requires. The distance between them is the subject of Section 9.

**Stabilised radio-frequency operation is the clearest case for keeping the axes apart.** Five reviewed platforms establish it quantitatively — patterns, gain, scan range, insertion loss, delivered power [6, 18, 5, 4, 20]. Exactly one attaches a duration, and that one holds its geometry static [6]. The gap is not that stabilised radiation is unevidenced; it is well evidenced. The gap is that its *onset after a commanded shape change* is untimed in the reviewed set.

### 5.4 The measured stages sit on incompatible platforms

This is the observation that motivates the review, and stating it needs Table 1 and Table 3 together:

- within the reviewed set, **mechanical morphing and settling (S7, S8) are timed only on A4 platforms with no radio-frequency layer**;
- **electronic state transitions (S6) are timed only on A5 rigid panels and one A3 flexible aperture**;
- **sensing, inference and control transport on a flexible radiating surface (S1, S2, S4, S5) are timed only on an A3 platform** where geometry is a disturbance rather than a control variable;
- **post-deformation calibration on a deformable radiating aperture (S9) is demonstrated only on an A7 active transmitter**, and carries no duration there or anywhere else in the reviewed set.

One might be tempted to assemble a total by taking each stage from wherever it was measured: 16.76 ms of electronic loop from A3, plus 300 ms of surface morphing from A4, plus unmeasured settling and calibration terms. We do not do this, and no one should. The sum would concatenate measurements taken on four different physical objects, one of which has no meta-atoms, another of which cannot bend, and none of which has both a controlled geometry and a measured radiation pattern. It would have the form of an engineering estimate and the content of a category error.

What the decomposition licenses instead is weaker and far more defensible: **no reviewed source times the adaptation chain end to end on any single object, and the reason is architectural rather than incidental.** Figure 2 shows the pattern directly — each platform illuminates a different band of the chain, and the bands do not overlap where they would need to.

> **Figure 2.** *Adaptation-chain coverage by architecture class, on two axes.* Rows are platform classes rather than individual papers; cells record the strongest evidence any platform in that class provides for that stage. Fill colour gives the **stage evidence status** — quantitatively measured, demonstrated without a quantity, or assumed and simulated — and the appended marker gives the separate, three-valued timing status: **·T** fully delimited, **·(T)** partially delimited, no marker untimed. The distinction is the figure's point: several cells are quantitatively measured and carry no marker at all, because a radiation pattern, a gain figure or a delivered power is a measurement but not a timing; and several carry **·(T)** rather than **·T**, because a share of an aggregate interval is not an independently delimited stage. Among the four stages on the right, morphing and settling are delimited only on platforms with no radio-frequency layer; calibration is timed nowhere in the reviewed set under either reading; and the one delimited interval ending in stabilised radiation holds its geometry static. *(File: `figures/fig2_adaptation_chain.pdf`.)*

### 5.5 The system papers do not model stages S5 to S9

Across the four reviewed FIM system papers — three distinct studies, since one is a short version of another — control transmission, electronic update, mechanical morphing, settling and calibration are absent from the model or assumed instantaneous. Geometry takes the value the optimiser assigns it, at the moment the optimiser assigns it.

Where the omission is defended at all, it is defended by a single sentence. Having noted that the optimisation could be executed for each distinct channel realisation, the high-mobility FIM–ISAC study states in a footnote that in practice, once the surface shapes have been computed for one realisation, "the optimized surface shapes can be used irrespective to changes in delays, Doppler shifts and waveform" [1, footnote 10, p. 13327].

We take the claim seriously, because if it holds the mechanical timescale largely stops mattering and the architecture becomes much easier to defend. As stated, however, it carries no validity duration, no channel-statistics condition, no degradation bound, no sensitivity study and no experiment; it is not derived in the paper, and it is not tested by the paper's own simulations, which optimise per realisation. It is an assertion in a footnote carrying the weight of the architecture's physical feasibility, and Section 8 examines what happens when that weight is transferred through a citation chain.

### 5.6 Where a loop is closed, perception is what binds

One reviewed source closes a loop on shape — sensing, estimation, optimisation, actuation, and back to sensing [7] — and its cycle budget is instructive in a way nothing else in the corpus is.

Each feedback control cycle takes around 0.25 s, which the paper attributes "mainly to the time overhead from the image processing algorithm", noting that the cycle is "ultimately limited by the mechanical response time (which is less than 0.1 s)" [7, p. 4]. The supplementary information gives the per-cycle budget more precisely as 0.35 ± 0.15 s and, critically, distinguishes a *cycle* from an *iteration*: each optimiser iteration requires 4(N + M) + 2 function evaluations, so the "5 to 15 iterations" quoted in the main text is 170 to 510 cycles. Convergence is stated directly as an average of approximately **2.5 minutes** for a 4 × 4 sample from the zero-actuation state [7, Supplementary Note S6].

Two things follow. First, in the one demonstrated shape-control loop in the reviewed set, **actuation is not the dominant contributor to loop time**; sensing, perception and search are. We state that as a property of this platform rather than as a law: whether a radiating FIM would also be perception-limited depends on its sensing modality, its verification criterion and its compute load, all of which would differ and none of which has been measured. The transferable part is a design warning — a closed-loop FIM's rate may be set by perception rather than by actuation, which is a reason to instrument the sensing path early — together with the purely negative observation that no system model represents this stage at all, so none would detect the problem if it occurred. Second, the gap between the element response time cited as evidence of feasibility (below 0.07 s) and the demonstrated closed-loop convergence (≈150 s) is a factor of roughly two thousand, and the reviewed system literature quotes neither.

The two figures are not competing measurements of one thing, and this review does not treat the slower one as the "true" cost. Open-loop replay of a known shape and closed-loop discovery of an unknown one are different operations with different completion criteria; the same platform replays stored voltage sequences at 10 fps once the voltages are known. Which is relevant to a FIM depends on whether the required geometry can be precomputed — a question the system literature does not pose. That is exactly the point: the informal phrase "morphing time" does not select between them.

### 5.7 Two quantities that nothing in the reviewed set reports

The decomposition isolates two absences precisely, and the precision is what makes them actionable.

**Mechanical settling of a radiating aperture.** One source times settling with a named mechanism: approximately 250 ms of viscoelastic membrane relaxation dominating the approximately 300 ms a soft surface needs to develop a full shape from flat [8, p. 4]. That is a bare elastomer membrane. No source in the reviewed set reports settling for a surface carrying meta-atom metallisation, a dielectric substrate, a bias network and a ground plane — the layers a grounded reflective aperture of the kind the reviewed flexible platforms use is built from, and which the one flexible radiating surface in the reviewed set had to redesign specifically to permit bending at all. Transmissive, active and unbacked architectures have different stacks, and nothing here is claimed about them.

**Calibration duration and the onset of trustworthy radiation after a shape change.** The flexible active array performs closed-loop refocusing using self-sensing receivers against a remote receiver, and reports no time [20]. The flexible microwave metasurface folds the operation into a pre-trained static map, so no explicit calibration step exists in its architecture; its supplementary information does measure a 16.7 ms interval ending at stabilised radiation, but that interval is triggered by a sensor press on a statically held surface and contains no shape change [6, Supplementary Note 6]. The quantity that remains unmeasured is therefore specific: **the interval from a commanded deformation to trustworthy radiation.** It is the stabilisation *end event* that has been shown to be measurable, not the interval the FIM architecture needs.

These two absences, together with the absence of any commanded-actuation measurement on a radiating aperture, are the substance of the validation gap in Section 9 and the origin of the reporting framework in Section 10.

---

## 6. Hardware evidence, organised by physical process

This section reports what has been measured. It is organised by *what was timed* rather than by tuning technology, because one of the review's findings — that electronic and mechanical ranges overlap — becomes invisible the moment the two are separated into different sections.

### 6.1 The quantity types, and where they are usually confused

Before any value can be compared with any other, the type of quantity has to be named. Table 4 lists the types that occur in this literature, each with the start and end events that define it and the object it applies to. The final column records the substitution each type invites — and every one of those substitutions is observed somewhere in the reviewed material, including once in an earlier draft of this manuscript.

**Table 4 — Timing-quantity taxonomy.**

| Quantity type | Start event | End event | Object | The substitution it invites |
|---|---|---|---|---|
| **Element mechanical response** | actuation current or voltage applied | element reaches stable displacement | one actuator or beam | being read as a whole-surface morphing period |
| **Surface mechanical response** | actuation command | full commanded shape developed | the whole surface | being read as the element figure, or as a settled shape |
| **Mechanical settling** | end of gross motion | residual motion within a stated tolerance | the whole surface | being bundled into "response time" with no separate figure |
| **Closed-loop shape convergence** | initial (often zero-actuation) state | verified arrival at a commanded shape | surface plus its sensing and search | being confused with open-loop replay of a known shape |
| **Open-loop replay rate** | — | — | surface with precomputed drive | being quoted as a latency; it is a rate |
| **Meta-atom EM state transition** | bias change applied | material or device state crosses a stated threshold | one meta-atom or one layer | being quoted without its direction or its threshold |
| **Controller / interface write** | command issued by the compute element | control state written to the target | one element, one tile, or the whole panel | **being quoted without naming the object** |
| **Computation wall-clock** | algorithm start | convergence or iteration cap | an implementation on named hardware | being compared across processors, or replaced by an iteration count |
| **Partial electronic loop** | a named intermediate event (e.g. shape acquisition) | a named intermediate event (e.g. bias applied) | a chain of stages, not the whole chain | being read as an end-to-end adaptation latency |
| **Stabilised RF onset** | a named trigger | radiated output stable at a stated detector criterion | the aperture in operation | being read as post-morph stabilisation when the geometry was static |
| **Channel / protocol timescale** | reference instant | correlation crosses a stated threshold | the propagation channel | being read as an interval of constancy, or as a deadline |

Two rules follow and are applied without exception. **Values may be compared only within a quantity type**, and even then only when their objects and architectures match. And **no value is pooled**: this manuscript computes no mean or median FIM response time, no pooled mechanical actuation time and no universal latency threshold, because none is estimable from the available evidence and producing one would require exactly the substitutions Table 4 catalogues.

### 6.2 Flexible programmable reflective apertures

**The most complete adaptation measurement available.** The flexible intelligent microwave metasurface with shape-guided adaptive programming [6] is the reviewed set's most instructive hardware source. The aperture is a 480 × 240 mm three-layer flexible sheet — metallic meta-atoms on polyimide, a polydimethylsiloxane substrate and a serpentine-mesh ground — carrying 32 × 16 meta-atoms at a 15 mm period, with varactors driven over 0–30 V. Control granularity is columnar: the 32 columns share bias voltages, so the surface has 32 independently addressable channels rather than 512 independent elements. Measured operation spans 3.0–3.4 GHz with up to approximately 270° of reflection-phase tuning across incidence angles from 0° to 45°, with the **normalised reflection amplitude** maintained above 0.4 across all bias and incidence combinations. We report that floor as the source reports it and do not convert it into a radiation or reflection efficiency: the source does not define it as an efficiency metric, and the conversion would need loss accounting the paper does not supply.

Its timing decomposition is the only one of its kind in the reviewed set. Data preparation for the network inputs takes approximately 4 ms — about 2 ms of sensor reception at roughly 1200 Hz per channel plus about 2 ms of processing; inference across 32 channels takes approximately 2 ms; and the bias-voltage supply module responds in 5.25 ms. Varactor switching is described as "negligibly short" with no numeric value. The components sum to 11.25 ms, a figure the paper's own timing figure annotates beside the measured total of **16.76 ms**, and the residual of approximately 5.5 ms arises from full-cycle control of all 32 channels over an RS-232 link at 115 200 bps [6, pp. 4–5; Supplementary Note 6]. **Roughly a third of the measured loop is serial-interface transport rather than physics.**

The methods differ between components, which matters for how much weight each carries: the 4 ms and 2 ms figures are **thread-timing averages** taken inside the control program, while the 5.25 ms figure is an **oscilloscope measurement** of the supply module's output following a control signal. No repetition count, sample size, dispersion or uncertainty is stated for any of the three, nor for the total. The supplement adds that deformation intervals must exceed 16.76 ms for voltage updates to remain synchronised — expressed as reliable operation at deformation frequencies up to 60 Hz — and projects, without measuring, that under 10 ms would be reachable with faster acquisition circuits and a different communication protocol.

Three properties of the 16.76 ms interval must travel with it whenever it is quoted. It begins at shape *acquisition*, so it excludes the deformation that produced the shape. It ends at bias-voltage *supply*, so it excludes any mechanical settling and any interval before the far field is stable. And the deformation is externally imposed: the supplement describes the mechanical platform as a frame carrying two telescopic links and three movable fulcrums, adjusted by hand to set the curvature, with no actuation timing and no closed loop around the shape. The system compensates for a shape it did not choose. It is a compensation latency, and calling it a FIM adaptation time would misattribute it by at least two stages at each end.

**An interval that does reach the radio.** The same supplement reports a second, methodologically independent experiment which — uniquely in the reviewed set — terminates at electromagnetic output rather than at a control signal. A finger-triggered sensor replaces the strain input; a dual-channel oscilloscope records the trigger on one channel and, on the other, received beam power demodulated by a logarithmic detector calibrated over −10 to −60 dBm at 3.1 GHz. The measured delay from trigger to **stabilised RF output is 16.7 ms** [6, Supplementary Note 6].

This matters in two opposite directions and both should be stated. It is the only measurement in the reviewed set whose end event is stabilised radiation, so this review cannot and does not claim that radio-frequency stabilisation is never timed in this literature. But the geometry is static throughout: the trigger is a sensor press, not a shape change, and no morphing occurs inside the interval. It bounds the electronic compensation path end to end on a flexible aperture. It does not bound the interval a FIM requires, which begins with a commanded change of shape.

What the platform establishes at application level is substantial and should not be understated. Mounted on an aerofoil model — the motivating scenario being aerofoil flutter under inertial, aerodynamic and elastic forces — it maintains a real-time QPSK video link at 3.1 GHz to a receiver 2 m away at 0° or 30°, with error vector magnitude staying around −20 dB while the surface is bent dynamically. That is shape-aware electronic compensation on a real flexible microwave aperture, demonstrated over the air, and the capability is not in doubt. It is worth naming what kind of dynamics it demonstrates: aeroelastic deformation of the aperture itself, at short range, not a mobile propagation channel.

**A second, independent flexible reconfigurable aperture.** The conformal reconfigurable reflectarray of polydimethylsiloxane and printed liquid metal [18] confirms independently that flexible, electronically reconfigurable reflective apertures are buildable: 10 × 10 elements at 9 GHz with per-element PIN diodes, ±45° beam scanning, 16.13 dBi peak gain, and element-level conformal compensation phase computed for several bending degrees. It has no shape sensing — the curvature is known a priori — and reports no timing of any kind. Its value here is as evidence that the compensation principle generalises beyond one group's platform, at a different frequency, with a different tuning device and a different phase resolution.

### 6.3 Rigid electronically reconfigurable surfaces: the timing comparators

**Two update times on one panel, for two different objects.** The scalable integrated RIS [4] is a one-bit PIN-diode surface at 9–10 GHz with 180° ± 20° phase difference, built as 16 × 16 tiles each carrying an Artix-7 FPGA, with four tiles forming a 32 × 32 prototype. It reports an update time below 0.1 ms per element and below 10 ms for a tile's complete ON/OFF configuration.

Both are bounds rather than measured means, and they describe different objects at different scopes — one diode against 256 of them — so the interval between them is up to two orders of magnitude and is not a discrepancy. The paper also reports that the control network uses time-multiplexed latching, reducing the effective update rate to a quarter of the raw parallel speed. We use that for what it establishes and no further: it shows that array-scale command distribution imposes a real, architecture-dependent penalty. It does not by itself account for the whole interval between the two figures, and since the paper does not decompose the tile-level bound into transfer, latching and switching components, no such account can be given from the published record. What the pair establishes is the substitution rule: **an element-level update time cannot stand in for a tile- or aperture-level configuration time.**

The same paper reports what such a panel costs to run — 8.25 W with all diodes off, 13 W with all on, and 11.25–11.60 W during beam steering for the 32 × 32 array. Measured control power is rare in this literature and this is the only such figure in the reviewed set.

**Transition times vary widely across — and within — tuning mechanisms.** The liquid-crystal RIS based on defected delay lines [5] is the reviewed set's most carefully characterised material transition: a 4.6 μm liquid-crystal layer, 12 × 10 unit cells at 62 GHz, 6.8 GHz (10.9 %) bandwidth, insertion loss below 7 dB, and beam steering from −50° to +50°. Its measured response times are **τ_on ≈ 15 ms and τ_off = 72 ms**, defined between 10 % and 90 % thresholds and strongly asymmetric. The paper supplies the comparator that gives these numbers meaning: reflectarray-type liquid-crystal implementations are expected to have switch-on times of a few seconds and switch-off times of tens of seconds, so the delay-line architecture is a large improvement. A projection of below 2 ms for a 1 μm layer appears in the same discussion and is explicitly not a measurement of the fabricated device.

The quantified values therefore run from approximately 15 ms to tens of seconds — roughly three orders of magnitude, with both endpoints belonging to liquid crystal. The semiconductor end of the range has no number at all: the flexible metasurface calls its varactor switching negligibly short and reports no measurement of it [6], and the mechanism survey's ranking states modulation rates rather than transition times [9]. We therefore attach **no numerical span to the electronic layer as a whole**, because that would require a lower endpoint no reviewed source supplies. What the evidence does establish is that a tuning mechanism must be named before any statement about electronic speed carries content, and that variation within a single mechanism can be as large as variation between mechanisms.

### 6.4 Commanded mechanical morphing, without a radio

**The filamentary mechanical metasurface** [7] achieves reversible out-of-plane deformation of about 30 % of an 18.0 mm sample using distributed Lorentz forces at currents below 27.5 mA in a 224 ± 16 mT field. Element response time is below 0.07 s, measured by monitoring a single serpentine beam with a 60 fps side camera and identifying the frame after which no displacement deviation is visible; system morphing is characterised as within 0.1 s. Its distinguishing feature is closed-loop control: in-situ stereo imaging drives a gradient-based optimiser in an experiment-driven, self-evolving inverse design.

The cost of that loop is the most instructive number the platform reports, and it is fully visible only in the supplementary information. One function evaluation — update the voltages, wait for the sample to settle, capture and process the stereo images, evaluate the loss — costs 0.35 ± 0.15 s, of which 0.19 s is imaging and template matching and 0.1 s is a deliberate settling pause. Each optimiser iteration requires 4(N + M) + 2 function evaluations, which is 34 for a 4 × 4 sample, and convergence takes 5 to 15 iterations, or 170 to 510 function evaluations. The paper states the resulting figure directly: a 4 × 4 sample takes an average of approximately **2.5 minutes** to morph into a shape from the zero-actuation initial state [7, Supplementary Note S6, Supplementary Table 1].

The separation between that figure and the platform's sub-0.1 s mechanics is the whole point. Bare actuator response is not the dominant contributor to closed-loop search time on this platform. What takes 2.5 minutes is *searching* for the voltages that produce a target shape on a nonlinear structure with a camera in the loop; once found, the same platform replays stored voltage sequences open-loop at a 10 fps update rate. The distinction that matters for a FIM is therefore between *searching* for a configuration and *replaying* a known one — a distinction the informal phrase "morphing time" does not make. Whether a FIM would pay the search cost or the replay cost depends on whether its required geometries can be precomputed, and no reviewed system model poses the question, let alone measures either quantity on a radiating aperture.

**The soft shape-programmable surface** [8] uses Lorentz-actuated liquid-metal microfluidic ribbons in an elastomer and reports the three-level decomposition that is, for this review's purposes, the single most useful set of numbers in the corpus: an isolated ribbon responds in approximately 30 ms measured (approximately 50 ms by finite-element analysis); a full surface develops from flat in approximately 300 ms, of which approximately 250 ms is viscoelastic membrane relaxation; and shape-to-shape switching takes approximately 650 ms, being two surface developments plus approximately 50 ms of script processing.

The element-to-surface penalty is a factor of ten, and the paper names its cause: **the membrane, not the actuator**. That matters because a membrane is a materials property. Adding the layers a grounded reflective aperture carries — meta-atom metallisation, a dielectric substrate and a ground plane — to such a surface would change its mass and its damping, and nothing internal to this evidence suggests the change would be favourable. Transmissive and active architectures carry different stacks; the point is that a stack is added, not that this particular one is universal.

The two mechanical platforms agree on the *sign* of the element-to-surface penalty and disagree on its *size* — a factor of about 1.4 for the filamentary mesh against about ten for the soft surface. The disagreement is itself informative: the penalty depends on construction, and no reviewed measurement establishes it for a radio-frequency stack.

### 6.5 Flexible active arrays: the capability without the clock

The flexible active antenna array work [20] demonstrates two 256-element, 30 × 30 cm arrays at mass densities around 0.1 g cm⁻² that remain fully functional and programmable at concave and convex bend radii below 23 cm, and deliver approximately 80 mW of DC power wirelessly to a 6.7 × 11 cm receiver about a metre away. Calibration and closed-loop focusing — using on-chip self-sensing receivers and feedback from a remote receiver — compensate phase offsets arising from manufacturing variation, **shape deformation** and environmental change. The demonstrated steering range of ±10° and focusing range of 1.6 m are stated by the authors to be limited by the measurement range rather than by the array.

This is the closest any reviewed source comes to the operation a FIM would need after changing shape: re-establishing coherent aperture behaviour on a deformed, large, real radiating surface under closed-loop feedback. **It reports no duration for that operation.**

One qualification travels with it. This is an active transmitter with per-element RFICs, phase-locked loops and on-chip self-sensing receivers, not a passive reflector, and its calibration strategy depends on exactly that: it senses through its own transmit chain and closes the loop against a remote beacon. A passive reflective FIM has neither. The demonstration establishes that deformation-aware recalibration of a large flexible aperture is achievable; it does not establish that the same method is available to the architecture the FIM literature describes.

### 6.6 The register

Table 5 is the consolidated result. It is deliberately selective — every value that carries an argument in this manuscript appears, and values that would only pad the list do not — and it is grouped by quantity type, so that the comparability rule of §6.1 can be applied by eye: **compare within a block, never across blocks.**

**Table 5 — Timing register.** M = measured · S = simulated · P = projected · D = derived by us · A = assumed. Architecture classes are those of Table 1.

| # | Quantity | Value | Start event | End event | Object | Arch. | Status | Conditions | Source |
|---|---|---|---|---|---|---|---|---|---|
| | ***Channel and protocol (demand side)*** | | | | | | | | |
| 1 | Correlation > 0.5 window | **51 symbols** | reference instant | correlation falls to 0.5 | propagation channel | A5 | S | 90 mph, 2.6 GHz, 100 kHz | [19] p. 721 |
| 2 | Illustrative coherence cases | 20 symbols @ 0.95; 40 @ 0.82 | — | — | channel | A5 | S | same scenario | [19] Fig. 4(b), p. 728 |
| 3 | Maximum Doppler at the FIM operating point | **≈19.4 kHz** | — | — | channel | A1 | **D** | 28 GHz, 208 m/s; **a frequency, not an interval** | derived from [1] Table III |
| 4 | Pilot overhead | 1 + M slots | pilot start | direct + M links sampled | protocol | A5 | S | M = 16 | [19] p. 720 |
| 5 | FIM protocol rates | move once per subframe; phase once per slot | — | — | protocol | A1 | model | Q × T₂ | [3] p. 6829 |
| | ***Computation (wall-clock)*** | | | | | | | | |
| 6 | FIM channel estimation | ≈4 ms → ≈100 ms (benchmark ≈1.2 s) | algorithm start | convergence / cap | desktop implementation | A1 | **M** | i7-13650HX, virtual array 36–324, 400-iter cap, tol 10⁻⁸ | [3] Fig. 8, p. 6833 |
| 7 | ANN inference, 32 channels | ≈2 ms | prepared input | coding output | embedded implementation | A3 | **M** | authors' implementation | [6] p. 4 |
| 8 | Shape-optimisation convergence | ≈10 iterations; ≤100 iterations | — | — | — | A1 | **not a duration** | no processor, no per-iteration cost | [15] p. 3; [2] p. 5 |
| | ***Controller and interface*** | | | | | | | | |
| 9 | Per-element update | **< 0.1 ms** | FPGA update command | element state written | **one element** | A5 | M/design bound | — | [4] abstract |
| 10 | Tile configuration update | **< 10 ms** | pattern command | tile pattern written | **one 16 × 16 tile** | A5 | M/design bound | — | [4] pp. 8–9 |
| 11 | Multiplexing penalty | ×¼ of raw parallel rate | — | — | control network | A5 | design statement | relative, not absolute | [4] p. 6 |
| 12 | Bias-supply response | 5.25 ms | control output reaches supply | bias applied | 32-channel supply | A3 | **M** (oscilloscope) | — | [6] p. 4 |
| 13 | Serial transport share | ≈5.5 ms of 16.76 ms | — | — | 32 channels over RS-232 | A3 | **D** from authors' attribution | 115 200 bps | [6] SI Note 6 |
| | ***Meta-atom / material state transition*** | | | | | | | | |
| 14 | LC switch-on τ_on | **≈15 ms** | transition begins | 90 % threshold | 4.6 μm LC layer | A5 | **M** | 62 GHz, 10 %/90 % markers | [5] p. 5 |
| 15 | LC switch-off τ_off | **72 ms** | relaxation begins | 10 % threshold | same layer | A5 | **M** | strongly asymmetric | [5] p. 5 |
| 16 | Earlier LC reflectarray comparator | τ_on "few seconds"; τ_off "tens of seconds" | — | — | other architectures | A5 | review statement | — | [5] p. 7 |
| 17 | Thinner-LC projection | < 2 ms | — | — | 1 μm layer | A5 | **P — not fabricated** | — | [5] p. 7 |
| 18 | Varactor switching | "negligibly short" | bias change | state changed | one meta-atom | A3 | author statement, **no number** | — | [6] p. 4 |
| | ***Partial electronic loop on a flexible radiating aperture*** | | | | | | | | |
| 19 | Data preparation | ≈4 ms | sensor reception begins | network input ready | 32 sensor channels | A3 | **M** (thread timing) | ≈1200 Hz per channel | [6] p. 4 |
| 20 | **Compensation loop** | **16.76 ms** | **shape acquisition** | **bias-voltage supply complete** | 32-channel aperture | A3 | **M** | components sum 11.25 ms; **no repetitions or dispersion stated** | [6] pp. 4–5, SI Note 6 |
| 21 | Deformation-rate limit | 60 Hz | — | — | aperture | A3 | **M — a rate** | derived by the authors from row 20 | [6] SI Note 6 |
| 22 | Projected improvement | < 10 ms | — | — | aperture | A3 | **P — not built** | needs different acquisition and protocol | [6] SI Note 6 |
| | ***Mechanical response, element level*** | | | | | | | | |
| 23 | Serpentine beam | **< 0.07 s** | current applied | stable deformation | 3.60 mm beam, **no RF layer** | A4 | **M** | 60 fps camera ⇒ ≈16.7 ms resolution floor | [7] p. 2; SI S5.3 |
| 24 | Isolated liquid-metal ribbon | **≈30 ms** (FEA ≈50 ms) | current applied | stable deformation | one ribbon, **no RF layer** | A4 | **M + S** | — | [8] p. 3 |
| | ***Mechanical response, surface level*** | | | | | | | | |
| 25 | System morphing | "within 0.1 s" | actuation command | morphed shape | 4 × 4 mesh, **no RF layer** | A4 | **M** | — | [7] abstract |
| 26 | Full surface from flat | **≈300 ms** | actuation begins | full shape developed | soft surface, **no RF layer** | A4 | **M** | ≈250 ms is membrane viscoelasticity | [8] p. 4 |
| 27 | Shape-to-shape switching | ≈650 ms | first shape command | second shape developed | same surface | A4 | **M** | 300 + ≈50 script + 300 | [8] p. 4 |
| | ***Closed mechanical control loop*** | | | | | | | | |
| 28 | Function-evaluation cycle | ≈0.25 s (text) / **0.35 ± 0.15 s** (SI) | image capture | next actuation applied | shape controller | A4 | **M** | 0.19 s imaging + matching; 0.1 s settle pause | [7] p. 4; SI Table 1 |
| 29 | Iteration cost | **4(N + M) + 2 = 34 cycles** | — | — | — | A4 | source statement — **not a duration** | 4 × 4 sample | [7] SI Note S6 |
| 30 | **Convergence** | **≈2.5 min** (average) | zero-actuation state | stopping criterion met | 4 × 4 sample, **no RF layer** | A4 | **M — stated by the source** | 170–510 function evaluations | [7] SI Note S6 |
| 31 | Open-loop replay | 10 fps | — | — | same platform | A4 | **M — a rate** | voltages already known | [7] SI video legends |
| | ***Stabilised radiation*** | | | | | | | | |
| 32 | **Trigger → stabilised RF** | **16.7 ms** | finger-triggered sensor fires | stabilised RF at receiver | flexible aperture, **geometry static** | A3 | **M** | dual-channel oscilloscope; log detector −10 to −60 dBm at 3.1 GHz | [6] SI Note 6 |
| 33 | Link held under bending | EVM ≈ −20 dB | — | — | aperture under dynamic bending | A3 | **M, untimed** | QPSK video, 3.1 GHz, 2 m | [6] |
| | ***Assumed, not measured*** | | | | | | | | |
| 34 | Shape-reuse lifetime | **unbounded** — "irrespective to changes in delays, Doppler shifts and waveform" | shape computed for one realisation | *never stated* | A1 model | A1 | **A** | no condition given | [1] footnote 10, p. 13327 |
| 35 | Shape update rate | once per coherence block | — | — | A1 model | A1 | **A** | — | [29] |
| | ***Not measured by anything in the reviewed set*** | | | | | | | | |
| G1 | Commanded actuation of a **radiating** aperture | — | actuation command | intended displacement | RF aperture | A1/A3 | **✗** | — | — |
| G2 | Settling of a radiating aperture to a phase-relevant tolerance | — | end of gross motion | stated electromagnetic criterion | RF aperture | A1/A3 | **✗** | — | — |
| G3 | Post-deformation calibration duration | — | shape change | mapping re-established | flexible RF aperture | A7/A3 | **✗** | operation demonstrated, untimed | [20] (absence) |
| G4 | Stabilised radiation after a **commanded** morph | — | commanded deformation | trustworthy radiation | RF aperture | all | **✗** | row 32 contains no shape change | — |

### 6.7 What the hardware evidence establishes

Six capabilities reach prototype-measurement level or higher: large flexible apertures that still radiate; in-situ shape sensing on three platforms; fast electronic phase reconfiguration; deformation-aware electronic compensation demonstrated over the air; commanded mechanical shape control with closed-loop verification; and conformal design at fixed curvature. **None of these constituent capabilities is absent from the reviewed evidence base when considered separately.** What remains unvalidated is their integration and its timing on one architecture — and separate demonstrations of constituent capabilities do not establish that those capabilities cease to constrain the design once combined, since integration changes the mass, the damping, the control granularity and the calibration burden of each.

What no source measures is the intersection: the time required for an aperture that must radiate to be commanded into a new shape, to settle, to be recalibrated, and to resume trustworthy electromagnetic operation. Those are rows G1 to G4, and they are the only rows of Table 5 with no value in them.

---

## 7. Synthesis: what the register supports, and what it forbids

### 7.1 The one comparison the evidence permits

The values in Table 5 measure different processes on different objects with different start events, and they cannot be pooled. What they do support is **ordinal comparison within a quantity type**, where the type is defined by the process being timed and the object being timed. Three such comparisons survive, and they are the substance of this section. Figure 3 displays them, on a logarithmic axis with each process on its own labelled lane, so that the reader can see where the reported ranges fall without being invited to treat them as interchangeable.

> **Figure 3.** *The timing landscape of the reviewed evidence.* Lanes are separate because the quantities are not commensurable: each was measured on a different object and architecture, between a different pair of start and end events. The axis shows where the reported values fall; it is **not** a latency budget, and no value may be pooled with, ranked against or substituted for a value in another lane. Two lanes carry no value at all — the mechanics of a radiating aperture, and its settling after a commanded morph. Note in particular that the two mechanical-loop lanes belong to the *same* platform and differ by more than three orders of magnitude, because one replays a known shape and the other searches for an unknown one. *(File: `figures/fig3_timing_landscape.pdf`.)*

### 7.2 What the mechanical measurements do and do not establish

Three mechanical quantities are reported, and the central result is that they are **distinct quantities that cannot be substituted for one another**: element-level response, below 0.07 s for a serpentine beam and approximately 30 ms for an isolated liquid-metal ribbon; full-surface response, "within 0.1 s" on one platform and approximately 300 ms from flat on the other; and verified closed-loop convergence to a commanded shape, approximately 2.5 minutes on the one platform that measures it.

The safe conclusion is about *what is being timed* rather than about a numerical ratio. **An element reaching steady state, a surface completing a morph, and a surface verified to have arrived at a commanded shape are three different measurements, and a value for one is not a value for another.** Three limits on that statement must be made explicit, because each is a place where the argument could be overstated.

*The element-to-surface step is not a shared finding.* Within one platform it is an order of magnitude — approximately 30 ms for an isolated ribbon against approximately 300 ms for the full surface, with the two figures two paragraphs apart in the same paper [8]. The other platform does not reproduce it: below 0.07 s for an element against within 0.1 s for the system is not an order of magnitude, and given a 60 fps instrument it may not even be a resolvable separation. The two platforms agree that element and surface are different quantities; they do not agree on the size of the difference.

*The third level is not replicated.* Closed-loop convergence is demonstrated by one platform only [7]. The liquid-metal platform reports no closed-loop verification, so the three-level structure is not an independently replicated result and is not presented as one.

*The convergence figure is a property of the search, not of the mechanics.* The approximately 2.5 minutes is the cost of *discovering* actuation voltages for a new target shape by experiment-driven optimisation, at 34 function evaluations per iteration and 0.35 ± 0.15 s per evaluation dominated by stereo imaging and template matching. Once the voltages are known, the same platform replays shapes open-loop at 10 fps. Closed-loop *discovery* and open-loop *replay* differ by more than three orders of magnitude on one platform, which is this subsection's point in its sharpest form.

Note what none of this says. It says nothing about an aperture carrying meta-atoms, and nothing about any radio-frequency quantity.

> **A correction to our own record.** An earlier version of this review derived a closed-loop convergence figure of approximately 1.25 to 3.75 s by multiplying the main text's "around 0.25 s" feedback cycle by its "5 to 15 iterations". That derivation is wrong: an iteration is not a feedback cycle but a batch of 34 of them, and the supplementary information states the convergence time directly. We record the error because it is an instance of exactly the failure this section documents — one quantity substituted for a differently defined quantity carrying the same informal name — and because we produced it ourselves rather than finding it in the literature.

### 7.3 Why "fast electronics, slow mechanics" needs qualification

The dichotomy is stated qualitatively in the closest survey — mechanical movement is generally slower than electronic reconfiguration [11] — and it is a reasonable first approximation. What the measured values show is that it cannot be applied from an architecture label alone.

Three values make the point. A liquid-crystal switch-off of **72 ms** [5]. A measured multi-stage electronic compensation chain — sensing, inference, control transport, bias application, from shape acquisition to bias-voltage supply — of **16.76 ms** [6]. A full mechanical surface morph from flat of approximately **300 ms** [8]. They were obtained at different frequencies (62 GHz, 3.2 GHz, and no radio at all), on different mechanisms, on different objects, with different start and end events, and they sit in three different quantity types.

The rule we apply is precise rather than absolute: **these heterogeneous measurements may be displayed on a common numerical axis in order to show that their reported ranges overlap, but they must not be treated as like-for-like performance measurements, pooled statistically, or used to infer the bottleneck of an integrated architecture.** Placed on that axis, the observation is about ranges and not about devices: an electronic material transition on one platform (72 ms) is numerically larger than a measured partial electronic chain on another (16.76 ms) and lies within a factor of about four of a full mechanical surface morph on a third (≈300 ms).

The consequence is a qualification rather than a design rule. Architecture labels alone do not establish a universal latency ordering, so **"fast electronics, slow mechanics" holds only with mechanism-, object- and architecture-specific qualification.** Which stage actually binds must be established for the specific combination of material, actuator, control network and aperture in question. We deliberately stop short of naming bottlenecks for hypothetical integrated devices: the reviewed set contains no liquid-crystal FIM, no integrated mechanically morphing radiating aperture, and no platform on which an electronic tuning layer and a commanded mechanical layer were measured together. Statements about what would limit such a device cannot be derived from measurements of its separated parts.

### 7.4 Why a latency is a property of an object, not of a technology

The same one-bit surface reports an update time below 0.1 ms and an update time below 10 ms [4]. Both are correct, and they bound different objects: one element, and one complete 16 × 16 tile. The authors state a ×¼ time-multiplexing penalty — an architecture-dependent factor of four — but do not decompose the tile-level bound further, so we do not present multiplexing as the explanation of the full interval. The comparison establishes something narrower and sufficient: **an element-level update time is not a substitute for a tile- or aperture-level configuration time, and array-scale command distribution introduces non-negligible, architecture-dependent overhead.**

The flexible aperture makes the related point from the other direction. Its measured loop is 16.76 ms; its identified components sum to 11.25 ms; and the approximately 5.5 ms residual is attributed by its authors to full-cycle control of 32 channels over RS-232 [6]. Transport is a **major individual contributor**, at roughly a third of the loop, but it does not exceed the remaining stages combined, so this measurement does not establish that transport dominates.

Taken together: **aperture-scale command distribution can be a major contributor to update latency, and it is absent from the FIM system models reviewed here.** We claim no universal dominance — the two platforms do not agree closely enough to support one, and neither reports the decomposition that would settle it. The implication for the system papers survives either reading, because it concerns whether the cost is modelled at all rather than how large it is. Those papers simulate 4 to 16 movable elements; the measured hardware has 32, 256 or 512 controllable channels. **A cost that scales with channel count is invisible at the scale the theory currently explores, and the theory's element counts are more likely to grow than shrink as apertures scale.**

### 7.5 Stage by stage: the answer the evidence supports

Assembling the demand side of Section 4 with the evidence of Section 6, the review question admits a stage-resolved answer rather than a verdict. Table 6 gives it.

Two conventions govern the table and both matter. The "must it track fast fading?" column records **a consequence of a stated assumption, not a finding** — the assumption is named in the cell, because the central question of this review is precisely which stages are exempt, and a table that presupposed its own answer would be worthless. And the evidence column distinguishes four states that are easily conflated: *capability demonstrated* (the operation was performed), *timing measured* (an interval was reported with events), *timing absent* (the operation was performed but not timed), and *architecture mismatch* (a measurement exists, but on an object unlike the one the claim concerns).

**Table 6 — Stage-by-stage answer to the review question.**

| Stage | Must it track fast fading? | Governing driver | Best available evidence | Evidence status | What this supports |
|---|---|---|---|---|---|
| **S1** sensing (geometry) | no — tracks *deformation*, not fading | platform dynamics | ≈4 ms strain read [6]; 0.35 ± 0.15 s stereo cycle [7] | timing measured (A3, A4) | geometry sensing at deformation rates; imaging, not actuation, sets the closed-loop rate on the one closed platform |
| **S1/S3** channel acquisition | **yes** | Doppler — ≈19.4 kHz at the reviewed operating point | 51-symbol >0.5-correlation window; 1 + M pilot slots | **simulated / modelled — no measurement** | the binding fast constraint, established by model rather than by measurement |
| **S2** geometry estimation | no | deformation rate | RMSD 2.36 mm at 45 mm against a stereo reference | timing and accuracy measured (A3) | demonstrated |
| **S4** optimisation | depends on the variable | fading for phase; statistics for shape | ≈2 ms embedded inference [6]; 4–100 ms desktop estimation [3] | timing measured (A3); wall-clock on non-embedded hardware (A1) | a fixed pre-trained map runs in ≈2 ms; **no embedded implementation of a *shape* optimiser is timed in the reviewed set** |
| **S5** control transmission | with S6 | as S6 | ≈5.5 ms of a 16.76 ms loop over 32 RS-232 channels [6]; ×¼ multiplexing penalty [4] | timing measured (A3, A5) | a major contributor at both measured scales; **absent from the system models** |
| **S6** electronic update | **yes**, if the phase layer is what tracks fading | fading | <0.1 ms/element, <10 ms/tile [4]; LC 15 ms on / 72 ms off [5] | timing measured (A5) | semiconductor tuning is compatible with a sub-millisecond per-element budget; LC transitions are tens of milliseconds. **No deadline is defined here** — sufficiency depends on a state-validity timescale this review declines to fix |
| **S7** mechanical morphing | **not necessarily** — no, *if* geometry is optimised from statistical or geometric state rather than instantaneous fading. That premise is assumed by the system literature and is not established (Section 8) | angular / statistical drift, *if* the premise holds | 30 ms element, ≈300 ms surface [8]; ≈2.5 min closed-loop convergence [7] | timing measured, **architecture mismatch — no RF layer on either platform** | mechanical timescales on non-radiating objects |
| **S8** mechanical settling | as S7 | as S7 | ≈250 ms membrane relaxation [8] | timing measured, **architecture mismatch** | settling on a non-radiating object; **no phase-relevant tolerance is stated by any source** |
| **S9** calibration | no, but it bounds S10 | shape-change rate | closed-loop refocusing on a flexible active array [20] | **capability demonstrated, timing absent** | that the operation is possible on a deformed radiating aperture; nothing about its duration |
| **S10** stabilised RF | — | all of the above | 16.7 ms trigger → stabilised RF, static geometry [6]; EVM ≈ −20 dB under dynamic bending, untimed | **measured for the electronic loop on a fixed-geometry flexible aperture**; absent following a *commanded* morph | that RF stabilisation can be measured, and has been; **no measurement exists of it after a commanded geometry change** |

Read across the rows, three things follow.

**The fast-timescale demand is established by modelling, not by measurement.** Channel acquisition is the stage that must track fading, and the evidence for its timescale — the correlation window, the Doppler figure, the pilot-slot structure — is simulated and analytical throughout. This review found no measurement of channel acquisition under high mobility with a reconfigurable surface in the loop. The demand side of the comparison therefore rests on weaker evidence than the supply side, which is the opposite of how the comparison is usually presented.

**The electronic update stage has measured support, but no deadline is defined for it.** A per-element update below 0.1 ms and a per-tile update below 10 ms are measured facts; whether they are *sufficient* is not a question this review answers, because answering it would require a stated update deadline for the same state variable, on a comparable architecture, at a specified carrier and mobility, against a stated correlation criterion. No reviewed source supplies that combination. The same applies to the liquid-crystal figures: 72 ms is slower than 10 ms, and that is all that follows.

**The geometry stages are where the evidence changes character.** For S7 and S8 the measurements exist and are good, but were taken on objects that do not radiate. For S9 the operation has been demonstrated on an object that does radiate, but was not timed. For S10 the interval has been measured — for an electronic compensation loop on a flexible aperture whose shape was externally imposed and static during the measurement — but, among the sources examined here, not following a commanded morph. These are four different kinds of gap and they call for four different experiments.

None of this shows that the missing intervals are large, or that the architecture is infeasible. It shows that they have not been measured. **An unmeasured quantity has no value, not a bad one**, and Section 9 states the gap in those terms.

---

## 8. How timing values travel: a traceability audit

### 8.1 What is being audited, and what is not

The FIM system papers reviewed here do not claim to have measured their own hardware assumptions, and it would be unreasonable to expect them to. They do, however, rest on three assertions about hardware, and each can be traced to a primary source. This section audits those three assertions in those papers, and then reports how far the practice extends among the papers that cite the same primary sources.

It is worth stating at the outset what this section is not. It is not a characterisation of how a research field reasons, and §8.5 states precisely why that stronger claim is unavailable. It is not an allegation of carelessness: the mechanism at work is structural, and §8.6 sets it out. And it does not supply a replacement number — the audit's own finding is that for most of these quantities there is no single interchangeable value, so offering one would repeat the error being documented.

### 8.2 Premise 1 — an unbounded shape-reuse assertion

"After the surface shapes y_T and y_R have been computed for a distinct realization, the optimized surface shapes can be used irrespective to changes in delays, Doppler shifts and waveform" [1, footnote 10, p. 13327].

Traced to source, this is a footnote. It carries no validity duration, no channel-statistics condition, no degradation bound, no sensitivity analysis and no experiment, and the paper's own simulations optimise per realisation rather than testing reuse. The stake is high in both directions: if the assertion holds, the mechanical timescale largely ceases to constrain the architecture; if it does not, the architecture requires mechanical adaptation at a rate no reviewed measurement supports. Nothing in the reviewed set determines which.

### 8.3 Premise 2 — the coherence-block assumption

FIM surface shapes "are only updated on the timescale of the channel's coherence block" [29]. This is cleaner and more testable than Premise 1, and it makes the two-rate structure explicit. It also asserts that command transport, actuation, settling and any recalibration all complete inside one coherence block — the proposition Sections 5 and 6 show to be unmeasured.

### 8.4 Premise 3 — the tabulated morphing periods

A recent FIM system paper tabulates the "key parameters of existing FIMs", listing morphing periods of 30 ms for the liquid-metal platform, 10 ms for the filamentary platform, and 500 ms for a third, photomechanical platform not held in our corpus, and states in text that "the response time of FIM surface morphing reaches 10 ms according to Table I" [30]. Traced against the primary sources:

**The 30 ms entry** corresponds to the liquid-metal platform's measured **isolated-ribbon** response. That paper's measured **full-surface** development time from flat is approximately **300 ms**, of which approximately 250 ms is viscoelastic membrane relaxation, and its shape-to-shape switching time is approximately 650 ms [8, pp. 3–4]. An element-level figure appears under a surface-level label, a substitution of one order of magnitude, with the correct value two paragraphs away in the same source. This one is confirmed against the primary text.

**The 10 ms entry** attributed to the filamentary platform does not correspond to any value in that paper's **complete primary source package**, which we obtained and examined in full: the main text, the Extended Data figures, the 71-page supplementary information and the peer-review file. The timing quantities reported there are an element response below 0.07 s, system morphing within 0.1 s, a function-evaluation cycle of 0.35 ± 0.15 s, and closed-loop convergence of approximately 2.5 minutes [7]. A full-text search of the package for "10 ms", "0.01 s", "sub-element", "filament", "transient" and "rise time" returns no occurrence, and the unit "ms" does not appear in the supplementary information at all. The tabulated deformation figures do trace correctly — the 18 mm aperture and the ratio of about 0.3 match the reported sample size and 30 % out-of-plane deformation — so the entry is drawn from that paper; the year is additionally given as 2021 rather than 2022. One further observation bears on it: the element response was measured by monitoring the sample with a 60 fps side camera, a frame period of approximately 16.7 ms, so the instrument used to obtain the fastest mechanical quantity in the paper could not have resolved an interval of 10 ms.

We report this as a **discrepancy requiring verification, not as an error**, and the distinction is deliberate. Obtaining the complete package establishes that no such value is reported in it; it does not establish how the tabulating authors arrived at theirs, and we can observe their table but not their derivation. A tabulated value may have been inferred, converted, or taken from a source we have not identified. The point does not in any case depend on resolving it: even taken at face value, the figure is a value for a bare mechanical mesh, being used to argue that a *radiating* aperture can reconfigure within a channel coherence block.

**The chain, stated once.** A mechanical-metasurface paper measures an element on a substrate with no radio; a system paper tabulates that value as a surface morphing period; a further system paper concludes that the morphing period is comparable to the channel coherence time and therefore that real-time adaptation is feasible; and the architecture is analysed on that basis. At no point in the chain is the substituted quantity measured on an object that radiates.

### 8.5 How far it extends: the forward citation search

We tested the reach of the practice rather than assuming it. Every work citing the three primary hardware sources was retrieved through the OpenAlex citation graph on 18 August 2026 — 306 seed-wise citing records, deduplicated to 262 unique works, screened to 65 wireless-relevant works and then to 24 records forming **20 distinct flexible-metasurface or reconfigurable-surface system studies**, of which **13 were read in full and 7 are behind publisher paywalls with no open deposit located**. The record-to-study collapse matters and is applied under §2.4's independence rule: a conference paper and its journal extension are one lineage, and one lineage in this set carries a timing assertion in its journal version that is absent from its conference version. Every count below is therefore a **lower bound**, and §8.5's closing paragraphs state precisely what that bound does and does not permit. Method, seeds, queries and the per-work screening table are in Section 2.3 and the supporting documentation.

**Table 7 — Timing-value propagation among papers citing the primary hardware sources.** Rows P1–P5 are cases in which a primary timing value is reused with its scope changed; rows N1–N3 record the opposite pattern. "Author-disjoint" means sharing no author with the FIM system papers audited here **and** none with the three primary hardware sources.

| # | Citing work | Primary source cited | Value or phrase reproduced | What the primary source measured | Scope change | Verdict | Author-disjoint? |
|---|---|---|---|---|---|---|---|
| **P1** | [30], Table I "Morphing Period" | [8], [7] | 30 ms / 10 ms / 500 ms | [8]'s 30 ms is an **isolated ribbon**; its full surface is ≈300 ms. [7] reports no value at or near 10 ms anywhere in its complete package | element → surface | Ni: **unsupported substitution, confirmed**. Bai: **discrepancy requiring verification** (year also given as 2021) | **No** |
| **P2** | [30], text | [8], [7] | "the deformation response of FIMs operates on the order of milliseconds (with the fastest reaching **1 ms**)" | 1 ms appears in no primary source, and is faster than the minimum entry (10 ms) of this paper's own Table I | escalation beyond the citing paper's own table | **unsupported, and internally inconsistent** | **No** |
| **P3** | [31] | [6], [8], [7] | "shape-switching times on the order of milliseconds, which are comparable to or faster than the channel coherence time in typical mmWave scenarios" | [6] holds its geometry **static** throughout the interval it reports and commands no shape; [8]'s surface morph is ≈300 ms; [7]'s system morph is within 0.1 s | electronic loop presented as mechanical shape switching; adds an unsupported coherence comparison | **unsupported** | **No** |
| **P4** | [32], Remark 4 | [7] | "dynamic surface-shape morphing in just a few milliseconds" | element response < 0.07 s; system morphing within 0.1 s | element → surface | **unsupported**; **absent from the conference version** of the same work | **No** |
| **P5** | [1], Remark, pp. 13321–13322 | [7] | "within millisecond switching speeds" | as above | element → surface | **unsupported**; **absent from the preprint** | **No** |
| **N1** | [12] | [7] | **no timing value attached** | — | none — cited for the *existence* of shape-morphing hardware | **correct use** | **Yes — fully disjoint**, sharing no author with the system-paper lineage or with any of the three primary sources |
| **N2** | [29] | — | **no timing value attached** | — | names response time as an unresolved practical limitation and declines to quantify it | **restrained use** | No |
| **N3** | [34] | [7] | **no timing value attached** | — | proposes a mechanically morphing metasurface lens for radio-frequency beam steering, cites [7] for the existence of shape-morphing hardware, and quantifies displacement and gain but no interval | **correct use** | **Yes — fully disjoint** |

Four limits on this finding must be stated, and the first two are the ones that bound what may be concluded.

**The observation window is 13 of 20 studies, and the finding is stated inside it.** Among the thirteen candidate system studies whose full texts were read, five instances of scope change occur, in four studies. Seven further studies could not be read — publisher paywalls, no open deposit — and an abstract-level scan establishes nothing here, because propagation occurs only in body text: scanning all 65 stage-one abstracts for timing terminology returns no hits at all. **An instance among the seven unread studies cannot be excluded, and neither can an author-disjoint one.** Every count in this section is a lower bound on a partially observed set, and no proportion, rate or prevalence is estimated from it.

**Authorship, unlike content, is resolvable for the unread seven, and it narrows the bound considerably.** Published-record metadata establishes the author list of a paper we could not read; it establishes nothing about what the paper says. Using only that, all twenty studies resolve: **fourteen share an author with the FIM system-paper lineage audited here, four are disjoint from that lineage, and two are disjoint from both the lineage and all three primary hardware sources.** Among the seven unread studies specifically, five share a lineage author and one shares an author with the flexible microwave metasurface [6] — a study of flexible reconfigurable surfaces for covert communication [33], which on authorship alone would have looked like a candidate author-disjoint case in either direction. **Exactly one of the seven, a conformal-RIS near-field modelling paper in a physics journal, is author-disjoint from both the lineage and all three seeds.** So the residual risk to the independence finding is not diffuse across seven unknown papers: if an author-disjoint group reproducing the practice exists in the unread set, it is that one study. Whether it attaches a timing value to the hardware it cites is unknown to us, and we make no claim either way.

**Within that window, no author-disjoint publication group reproduces the practice.** The four papers carrying the five instances form **one connected co-authorship network**: each shares at least one author with another member of the set and with the system papers audited here, and two names recur throughout. We state this as connectivity rather than as pairwise sharing, because connectivity is what we verified. Measured rather than assumed, the independence result is **negative**: four different first authors are not four independent groups when common senior authors run through them, and this review does not count shared-lineage papers as confirmations. What the search widened was the *case base* — from two papers to four, each instance with verbatim quotation, including two escalations the earlier framing did not capture. What it did not widen is the *independence basis*, which is zero within the observed window. **This is therefore a documented finding about one collaboration network, bounded by full-text access, and no statement about prevalence, proportion or the field follows from it.**

**The search found the opposite pattern too, and it is recorded here rather than left out.** The thirteen studies read in full divide exactly in two: four propagate a timing value with its scope changed, and the remaining **nine cite the same primary sources and attach no timing value at all**. Those nine are listed by study-family identifier and citation in the supporting documentation, so the count is reconstructable from named rows rather than asserted. **Two of the nine are fully author-disjoint** — sharing no author with the FIM system-paper lineage and none with any of the three primary hardware sources. One optimises a FIM under statistical channel information and cites the mechanical hardware only for its existence [12]. The other proposes a mechanically morphing metasurface lens for radio-frequency beam steering, cites the filamentary platform directly, quantifies displacement and gain — and states no interval anywhere [34]. That second case is worth its own sentence, because it is an author-disjoint group working on exactly the object this review is about, reaching for the same primary source, and declining to convert it into a timing claim. A third of the nine names response time explicitly as an unresolved practical limitation and declines to quantify it [29]; it is counted inside the no-timing-value set, because naming a quantity as unresolved is not attaching a value to it. Restraint exists in this literature, and it is not confined to authors outside the network.

**Two structural observations survive the bound on access, within the same window.** No derivation, explanation or source for the tabulated 10 ms value was found in any of the full texts inspected, which is why §8.4's verdict remains a discrepancy rather than an error; the seven unread studies cannot be spoken for. And two of the five instances were inserted between an author team's own conference or preprint version and its journal version — a pattern the audit did not anticipate and which is invisible to anyone reading only one version.

### 8.6 Why this happens, and what would prevent it

We are not accusing anyone of bad faith, and the mechanism is worth stating precisely because it suggests the remedy.

Every one of the substitutions in Table 7 is enabled by the same thing: an informal term used where a definition is needed. "Response time", "morphing time", "morphing period" and "switching speed" are all phrases that name a duration without naming the object it applies to, the event that starts it, or the criterion that ends it. Once a value has been reported under such a phrase, nothing on the page distinguishes an element from a surface, an open-loop replay from a closed-loop search, or an electronic compensation chain from a mechanical morph — and a downstream reader has no means of detecting that a scope has changed. The modelling community and the mechanical-metasurface community publish in different venues with different reporting conventions, and a quantity that crosses between them arrives stripped of exactly the context that would have constrained its reuse.

This review made the same class of error itself, on a smaller scale and in the same conditions: an informal phrase, an ambiguous unit, and a plausible arithmetic step (§7.2). We report it because it is the strongest evidence available that the failure is structural rather than personal.

The remedy follows directly and is cheap. A timing value that travels with its object, its start event and its end event cannot be silently rescoped, because the substitution becomes visible on the page. That is what Section 10 asks for, and item 4 of §10.3 in particular: had a provenance column been required of the imported hardware parameters in Table I of [30], the substitution documented in §8.4 would have been apparent to its own authors before it was apparent to us.

---

## 9. The validation gap

### 9.1 What the gap is not

It is worth beginning with what is already established, because the gap is narrower than a reader arriving from the system literature might expect, and misplacing it would misdirect the experimental effort that could close it.

Physical flexibility of a large radiating aperture is demonstrated: 256-element flexible active arrays remain fully functional at bend radii below 23 cm [20]; a 480 × 240 mm flexible reflective metasurface operates across 3.0–3.4 GHz with approximately 270° of phase tuning [6]; a flexible reflectarray maintains favourable radiation characteristics over a ±25 % bending range [17]. In-situ shape sensing is demonstrated on three independent platforms — strain-sensor arrays, stereo imaging, and on-chip self-sensing receivers. Fast electronic phase reconfiguration is measured, at below 0.1 ms per element for semiconductor tuning [4]. Deformation-aware electronic compensation is demonstrated over the air, holding a video link at approximately −20 dB error vector magnitude while the surface is bent [6]. Commanded shape control with closed-loop verification is demonstrated — on mechanical platforms carrying no radio-frequency layer, which is why it appears here as an enabling capability rather than as a radiating result [7]. Conformal design at fixed curvature, including one-bit and two-bit implementations, is measured and full-wave validated [25, 26, 18, 24].

None of these is the gap. Each reaches prototype measurement or higher on the evidence ladder, and several reach over-the-air demonstration.

### 9.2 What the gap is

The gap is the intersection, and it has a precise form: **the transition from compensating a shape imposed from outside to commanding a shape and knowing when it has arrived, on an aperture that must simultaneously radiate.**

Every measurement of the commanded-shape side in the reviewed set was taken on a platform with no meta-atoms, no bias network and no radio-frequency ground plane. Every measurement of the radiating side was taken on a platform where geometry is exogenous. The two sets do not intersect anywhere in the reviewed literature. Table 8 traces the consequence assumption by assumption, from what the system models assume, through the hardware capability each assumption implies, to the closest available evidence and the measurement that is missing.

**Table 8 — System assumptions, the hardware they imply, and the evidence available.** Evidence levels: L2 system simulation · L4 component measurement · L5 prototype RF measurement · L6 over-the-air demonstration · L7 end-to-end closed-loop validation with verified, timed stabilised radiation.

| System-model assumption | Where stated | Hardware capability implied | Closest evidence in the reviewed set | Level | What is missing |
|---|---|---|---|---|---|
| Element coordinates are freely selectable within a morphing range | [1, 2, 3, 15] | a radiating aperture whose geometry the system commands | commanded shape control on **non-radiating** mechanical platforms [7, 8]; radiating apertures with **externally imposed** geometry [6, 18] | L4 / L5, on disjoint platforms | **G1 — commanded actuation time for a radiating aperture** |
| Morphing is instantaneous, or completes within one coherence block | [1]; [29] | actuation plus settling inside a stated interval | ≈300 ms full-surface morph, ≈250 ms of it membrane relaxation, on a bare elastomer [8] | L4, **architecture mismatch** | **G2 — settling of a radiating aperture to an electromagnetically stated tolerance** |
| The optimised shape stays usable "irrespective to changes in delays, Doppler shifts and waveform" | [1, footnote 10] | a shape whose validity outlives the channel state it was computed for | no bound, condition, sensitivity study or experiment in the reviewed set | — | a validity duration, or an explicit statement that none is claimed |
| The geometry-to-response mapping is available whenever it is needed | implicit in all four | recalibration fast enough to be ignored | closed-loop refocusing of a deformed 256-element array, **demonstrated but not timed** [20] | L6, **timing absent** | **G3 — post-deformation calibration duration** |
| Radiation is trustworthy as soon as the shape is set | implicit in all four | a bounded interval from command to usable far field | 16.7 ms trigger → stabilised RF, **geometry static throughout** [6] | L5/L6, wrong start event | **G4 — stabilised radiation after a *commanded* geometry change** |
| Command transport and electronic update are free | all four; none states the assumption | distribution overhead negligible at aperture scale | ≈5.5 ms of a 16.76 ms loop is RS-232 transport [6]; ×¼ multiplexing penalty [4] | L5 — **measured, and non-negligible** | a model containing the cost at all |
| Geometry can be optimised against measured channel state | the premise of the whole A1 formulation | one platform holding aperture, shape sensing, channel estimation and optimisation together | four platforms, each holding **three of the four** | **not attained** | the integration itself (§9.3) |

The four unmeasured intervals deserve individual statement, because their experimental cost differs sharply.

**G1 — commanded actuation time for a radiating aperture.** How long from an actuation command to the intended displacement, on a surface carrying the layers a grounded reflective aperture is built from — meta-atom metallisation, a dielectric substrate and a ground plane. The stack differs for transmissive and active architectures, and the gap is stated here for the grounded reflective case the reviewed flexible platforms exemplify. The nearest available figures — tens of milliseconds at element level, hundreds at surface level — are for bare mechanical substrates. The one flexible radiating surface in the reviewed set required a serpentine-mesh ground plane, reducing estimated bending stiffness by more than two orders of magnitude, simply to permit bending at all [6]; its dynamic properties are not characterised.

**G2 — mechanical settling to a phase-relevant tolerance.** The only settling measurement in the reviewed set attributes approximately 250 ms of a 300 ms surface response to viscoelastic membrane relaxation [8] — a materials property of a bare elastomer. More importantly, no source defines settling in terms that matter electromagnetically: the relevant criterion is not "motion has stopped" but a stated bound on residual phase or radio-frequency performance error, or the displacement tolerance corresponding to it at the operating wavelength. *(To illustrate the form such a criterion takes, and not as a value this review recommends: at 28 GHz one wavelength is 10.7 mm, so a tolerance stated as λ/20 would be roughly half a millimetre. Which fraction is appropriate depends on the phase-error budget of the aperture in question, and no reviewed source derives one.)*

**G3 — post-deformation calibration duration.** The operation is demonstrated on a deformed 256-element flexible aperture using closed-loop focusing against a remote receiver [20]; no duration is reported. The alternative architecture — folding the geometry-to-bias mapping into a pre-trained network, as the flexible microwave metasurface does — sidesteps the question by making calibration a training-time cost, but that approach is validated for a specific aperture, band and deformation family, and its generalisation cost is unmeasured.

**G4 — onset of trustworthy radiation after a commanded geometry change.** This gap must be stated more narrowly than the other three, because one reviewed source does terminate a measured interval at stabilised radiation: 16.7 ms from a sensor trigger, captured on a dual-channel oscilloscope through a logarithmic detector at 3.1 GHz [6, Supplementary Note 6]. That measurement establishes both that the end event is well defined and that it is instrumentable with ordinary laboratory equipment. What it does not contain is a geometry change. **The unmeasured quantity is the interval from a commanded deformation to trustworthy radiation**, and it is the one a system designer actually needs, since it alone bounds the period during which the link must tolerate a degraded aperture.

### 9.3 The deeper gap is structural, not temporal

Timing is the visible problem. Underneath it sits a problem no amount of stopwatch work would solve.

**No reviewed platform is architecturally positioned to optimise geometry against measured channel state.** The flexible microwave metasurface has the aperture, the shape sensors, the inference engine and the controller — and no channel estimator; its loop closes on geometry [6]. The FIM system papers have the channel model, the estimator and the optimiser — and no aperture. The mechanical platforms have commanded shape control and closed-loop verification — and no radio [7, 8]. The flexible active array has the aperture, the sensing and the closed-loop calibration — and its loop closes on a beacon, not on a communication channel [20].

Each of the four holds three of the four necessary components. None holds all four. That is not a measurement gap; it is an integration gap, and it explains why the timing gap has persisted: no platform in the reviewed evidence base is the object whose timing would need measuring. Figure 4 shows the pattern.

> **Figure 4.** *System-model assumptions and the evidence link each one crosses.* Solid links are supported by a measurement on a comparable object; dashed links are not, either because the closest measurement was taken on an architecture that lacks a radio-frequency layer (red) or because the operation was demonstrated without timing, or timed from a start event other than a commanded shape change (amber). G1–G4 name the missing interval in each case. *(File: `figures/fig4_assumption_evidence_map.pdf`.)*

### 9.4 Ranked by what it would cost to close

**G3 appears least demanding, because the experiment has already been performed once.** The flexible active array apparatus already performs closed-loop recalibration of a deformed aperture; what is absent is a reported duration. If that platform remains available, adding synchronised timing from the curvature change to the re-converged focus, at a stated performance tolerance, could close the gap without a new aperture prototype. We state this conditionally: whether the apparatus is still assembled, whether the deformation and the recalibration can be triggered and timestamped against a common clock, and how reproducible the resulting interval would be are all unknown to us and unanswerable from the published record. We do not describe the experiment as free.

**G1 and G2 require an instrumented experiment but no new invention.** Mounting an actuator on an existing flexible reflective aperture and measuring displacement, settling against a stated and justified electromagnetic criterion, and the resulting reflection-phase transient would directly fill G1 and G2 in the reviewed evidence base. Both the apertures and the actuation mechanisms exist; they have not been combined and timed.

**G4 follows from G1–G3** and requires a radio-frequency measurement synchronised to the actuation command — the natural output of the G1/G2 experiment.

**The structural gap of §9.3 is a research programme, not an experiment.** It requires a platform that senses geometry, estimates a channel, optimises both geometry and phase, actuates, and measures the resulting link. Nothing in the reviewed literature is close to it, and no timeline should be asserted for it.

### 9.5 What this does not show

This review does not show that flexible intelligent metasurfaces are infeasible, and no sentence in it should be read that way.

Absence of measurement is not evidence of impossibility. Six of the constituent capabilities are demonstrated, several over the air, and nothing in the measured mechanical record rules out a two-timescale architecture in which geometry follows angular and statistical drift rather than fading. The individual values are compatible with such an architecture: element responses of tens of milliseconds on two bare mechanical platforms, and full-surface responses of hundreds of milliseconds on the one platform reporting the decomposition. We do not extend that compatibility to the closed-loop level, where the only measurement — approximately two and a half minutes on a single platform, for a search rather than a replay — is not independently replicated and belongs to a different kind of operation. Whether the architecture works depends on quantities for which no measurement was found in the reviewed set, and the honest position is that the question is open in both directions.

What the review does show is that **in the specific feasibility claims examined here, the confidence expressed exceeds the evidence traced behind it.** The premises of Section 8 are a footnote without a bound, a modelling assumption, and a table entry whose value appears nowhere in the primary source's complete published package. That is a finding about the premises audited and the four papers in which the forward citation search located the practice — one connected co-authorship network, observed across the 13 of 20 candidate studies whose full texts we could read — and not a measurement of how a field reasons. Each premise may turn out to be correct. None is currently established, and the difference between "plausible" and "established" is the subject of Section 10.

---

## 10. A reporting framework for FIM adaptation

### 10.1 Definitions, not thresholds

The deficiencies documented in Sections 6 to 8 are principally failures of *definition* rather than of measurement quality. Several of the measured values in Table 5 are excellent measurements; what they lack is the context that would allow them to be compared with anything, or that would allow a downstream reader to detect a change of scope. A value reported without its object, its start event and its end event cannot be compared; once such a value enters a citation chain, an element-level figure can become a surface-level one with nothing on the page to signal it.

The framework below therefore prescribes **definitions rather than thresholds**. We do not propose that actuation should complete within any particular time, that settling should meet any particular criterion value, or that any performance target should be met. The evidence supports no numerical acceptance threshold, and inventing one would repeat precisely the error this review documents — a number with no measurement behind it entering circulation because it was useful.

Each field is motivated by a **recurring reporting deficiency or a specific unresolved quantity identified in the reviewed set**. Those are different things: some fields name quantities no reviewed source reports at all, while others name quantities that some sources report and others omit, which is what makes the reported ones incomparable. Fields that would merely be nice to have are omitted. Table 9 gives the set with its motivation field by field.

### 10.2 The minimum reporting set for hardware papers

**Table 9 — Recommended minimum reporting set, with the deficiency motivating each field.** Groups A, B and C are the **core fields** we suggest for any paper reporting a deformable or reconfigurable aperture; D and E apply where a control loop is claimed; F applies to any mobility or ISAC claim. Every field should be reported **when applicable to the platform in question**. This is a recommendation, not a standard — see §10.4.

| Group | Field | Motivating deficiency in the reviewed set |
|---|---|---|
| **A — architecture** | Architecture class: passive flexible / shape-aware programmable / self-morphing / rigid reconfigurable / flexible active | Seven physically distinct systems are grouped under overlapping names (Table 1) |
| | **Deformation source: externally imposed or self-actuated** | The distinction between compensating a shape and commanding one is this review's central taxonomic finding, and it is rarely stated explicitly |
| | Whether a radio-frequency layer is present, and what it consists of | Every measured mechanical timescale in the reviewed set was obtained on a platform with no RF layer |
| | Control granularity: independently addressable channels versus total elements | One reviewed aperture has 512 meta-atoms and 32 control channels; the difference is not usually foregrounded |
| **B — timing** *(the five fields we suggest accompany every reported interval)* | **Object timed** — one element, one tile, or the whole aperture | The same panel reports element- and tile-level bounds up to two orders of magnitude apart, because the object differs |
| | **Start event**, named physically | "Response time" denotes at least five different intervals in the reviewed set |
| | **End event**, named physically, with its threshold | Threshold definitions are inconsistent where present and absent for most reported intervals. The two sources that state one state incommensurable ones: 10 %/90 % amplitude thresholds on a liquid-crystal device, and "the first video frame after which no displacement deviation is visible" on a 60 fps camera — an instrument-limited criterion with a ≈16.7 ms floor |
| | **Measured, simulated, projected or derived** | A projected sub-2 ms figure appears in the same discussion as measured 15 ms and 72 ms values |
| | Direction, where the process is asymmetric | Switch-on and switch-off differ by nearly a factor of five in the reviewed liquid-crystal device |
| **C — mechanics** *(any surface whose geometry changes)* | Actuation mechanism, drive quantity and drive level | Reported for the mechanical platforms; absent for every flexible radiating aperture |
| | Displacement range, in millimetres **and in wavelengths** | The system literature works in wavelengths and the hardware literature in millimetres; almost no source gives both |
| | **A stated and justified electromagnetic settling criterion** — an allowable phase or RF-performance error, or the corresponding displacement tolerance relative to wavelength, with the basis for the value chosen | No reviewed source defines settling electromagnetically; settling is reported, where reported at all, as the cessation of visible motion. This review prescribes no numerical fraction of a wavelength, and none should be inferred from the illustrative arithmetic in §9.2 |
| | Rise time and settling time, separately | Bundled into a single "response time" wherever they are reported |
| | Achieved shape accuracy against the *commanded* shape | Reported for shape *sensing* (RMSD 2.36 mm at 45 mm displacement); not reported for shape *achievement* on a radiating aperture anywhere in the reviewed set |
| | Repeatability, hysteresis, and cycles to a stated **electromagnetic** degradation | Mechanical cycling data exist — 1 000 reversible actuation cycles on one mechanical platform, 3 000 bending cycles for the shape-sensing array on the flexible radiating platform — but no source pairs a cycle count with any measurement of RF performance drift |
| | Repetition count and dispersion for every reported interval | Neither supplementary package reports repetitions or uncertainty for its headline timing value; the intervals quoted in this review are single stated figures |
| | Actuation energy per shape change | Not reported for any radiating aperture; the only measured power figures are electronic panel power for a rigid RIS |
| **D — control chain** | Interface type and its measured transport contribution | Approximately a third of one reviewed loop is RS-232 transport, discoverable only because those authors decomposed their measurement |
| | Serialisation or multiplexing penalty | One reviewed panel loses a factor of four to time-multiplexed latching |
| | Computation platform and wall-clock inference time | One FIM paper reports desktop runtime; the others report iteration counts, which cannot be converted |
| | Whether the loop is open or closed, and on what quantity it closes | The reviewed loops close variously on geometry, on a beacon, or on nothing; **none closes on channel state** |
| **E — electromagnetic re-establishment** | Calibration procedure and its **measured duration** | The one demonstrated post-deformation recalibration of a large flexible aperture reports no time |
| | **Criterion for trustworthy RF operation, and the interval from command to meeting it** | The interval to stabilised radiation has been measured for static-geometry electronic compensation, which establishes that the end event is definable and instrumentable; it remains unreported following a commanded geometry change |
| | Operating band, incidence-angle range and achieved phase range under deformation | Reported by the flexible apertures; absent from the mechanical platforms, which have no radio |
| **F — operating conditions** | Carrier, bandwidth, relative velocity if any, whether the channel is estimated or assumed, whether sensing and communication are both present, and the environmental conditions of any mechanical measurement | No reviewed flexible-aperture demonstration involves a mobile channel. Stating this explicitly would prevent laboratory bending demonstrations from being read as mobility results |

### 10.3 The minimum assumption declaration for system papers

The system literature cannot be expected to measure hardware. It can reasonably be expected to declare what it assumes, and the reviewed papers largely do not. The five items below are what we suggest such a declaration contain.

1. **Which adaptation stages are assumed instantaneous.** In all four reviewed FIM system papers, control transport, actuation, settling and calibration are assumed away; none says so.
2. **The assumed update rate for each control variable, with its basis.** Where a two-rate schedule is used, the paper should state whether the rates are chosen for tractability or justified by hardware.
3. **The assumed validity duration of a computed shape, with its basis.** A claim that an optimised shape can be reused irrespective of delay, Doppler and waveform changes is a strong physical claim; it should carry a bound, a condition, or an explicit acknowledgement that it is an assumption.
4. **The provenance of any hardware figure imported into the paper** — what object it was measured on, and what its start and end events were.
5. **Whether the cited hardware has a radio-frequency layer.** The mechanical platforms cited as evidence of FIM feasibility do not.

Item 4 matters most and costs least. A table of imported hardware parameters carrying an "object measured" column and a "start/end events" column would have made Section 8 of this review unnecessary.

### 10.4 Standing and scope

We do not propose this as a standard, and we have no standing to. We propose it as the minimum set that would have allowed the questions in this review to be answered from the published record. Some of its fields could be reported from measurements already performed — the object and events of an interval that was timed anyway, or the interface and computation platform of a loop that was built anyway. Others require new measurements: settling against an electromagnetic criterion, post-deformation calibration duration, actuation energy, and repetition counts for intervals reported once. We do not claim to know the proportion, because that would require knowing what each group recorded and did not publish.

---

## 11. Discussion

### 11.1 The answer, stated plainly

**Which operations must track fast channel variation?** Conditionally on the two-timescale premise — that the shape is commanded from slower statistical or geometric information rather than from instantaneous small-scale fading — the fast, channel-dependent path comprises channel estimation, the optimisation or inference that produces the fast state, the transport of that command to the surface, and the electronic state update. The geometry stages — geometry sensing, mechanical morphing, settling and geometry-dependent calibration — need not track instantaneous fading *under that premise*.

We state the premise as a premise. It is what the system literature assumes rather than establishes, and this review neither validates it nor presupposes it as a finding. It is not our reconstruction either: the published version of the high-mobility FIM–ISAC study offers morphing "once over several channel coherence intervals to achieve statistically optimal performance" as an alternative to per-realisation morphing, and names the resulting trade-off against "morphing speed requirements" [1, p. 13322]. It is offered there as a design option, with no validity interval and no supporting measurement. We also do not claim the fast path contains nothing else; a specific architecture may place other operations on it.

The evidence behind the fast stages is of two different kinds and should not be described with one word. The **demand** — how fast that path must run — is established by analysis and simulation: a Doppler figure, a correlation window from a different scenario at a different carrier, and a pilot-slot structure. We found no measurement of channel acquisition under high mobility with a reconfigurable surface in the loop. The **supply** on the electronic-update stage is measured, and measured on rigid panels: below 0.1 ms per element and below 10 ms per 16 × 16 tile on semiconductor hardware, against 15 ms and 72 ms for a liquid-crystal layer at the reviewed thickness. Those are two evidence types answering two questions, and the comparison inherits the weaker of them. We call none of the measured values adequate or inadequate: sufficiency needs an update deadline defined for the same state variable, on a comparable architecture, at a stated carrier and mobility, against a stated correlation criterion, and no reviewed source supplies that combination.

**Which operations may follow slower geometric or statistical change?** Geometry itself, together with the sensing and inference that support it, if the premise above holds. This is not our proposal; it is the position already taken by the movable-antenna literature, instantiated in FIM work through statistical-CSI shape optimisation, and already embedded as a two-rate schedule in a FIM channel-estimation protocol.

**How well are the required timescales supported?** Unevenly, and the unevenness is architectural. The fast-path *requirement* rests on analysis and simulation. The fast-path *hardware capability* rests on measurements taken on rigid panels that cannot bend. The slow-path capability rests on measurements taken on mechanical platforms that do not radiate. And the four quantities on which the architecture's viability actually turns — commanded actuation of a radiating aperture, settling to an electromagnetically stated tolerance, post-deformation calibration duration, and the onset of trustworthy radiation after a shape change — are supported by no measurement in the reviewed set at all.

### 11.2 What follows for system modelling

Three consequences, in descending order of confidence.

**Report the object.** The most common failure observed here is not optimism but underspecification. A latency without an object is uninterpretable, and the reviewed set contains a clean demonstration: one panel, two update times bounding two differently scoped objects, up to two orders of magnitude apart, both correct. System papers importing hardware figures should import the object with them.

**Do not assume the electronic layer is uniformly fast.** Electronic update latency is **mechanism-dependent**. The reviewed liquid-crystal device exhibits tens-of-milliseconds transitions at the layer thickness measured, whereas semiconductor control reports different quantities at different granularities — a per-element bound and a per-tile bound, neither of them a material transition time. Whether either mechanism satisfies a particular fast-loop requirement depends on the required state-validity interval and on the architecture, and no reviewed source establishes a scenario-specific deadline against which to judge. We therefore label neither adequate nor inadequate. What follows for design is only that "the electronic layer is the fast one" is not a statement one can make without naming the mechanism, the object and the requirement — and since liquid crystal is attractive for large low-cost panels, as one reviewed source argues explicitly, this is a live consideration rather than a corner case.

**Model the control network.** Aperture-scale command distribution can be a major contributor to update latency — a stated factor-of-four serialisation penalty on one measured panel, roughly a third of the measured loop on the other — and it is **absent from the FIM system models reviewed here**. We claim no dominance: the two platforms do not agree closely enough to support one, and neither reports the decomposition that would settle it. The point is that a cost scaling with channel count is invisible at the scale the theory currently explores — 4 to 16 movable elements, against measured apertures with 32, 256 or 512 controllable channels — and it grows with the aperture sizes the theory wants.

### 11.3 What follows for hardware work

The gap is narrow enough to name three experiments, and the first builds on apparatus that has already been assembled once.

**Time an experiment that already exists.** Closed-loop recalibration of a deformed 256-element flexible active array is demonstrated but not timed. If that platform remains available, adding synchronised timing from the curvature change to the re-converged focus, at a stated performance tolerance, would directly fill G3 in the reviewed evidence base, supplying a quantitative constraint on post-deformation radio-frequency re-establishment without a new aperture prototype. Whether the apparatus is still available, whether the deformation and the radio-frequency measurement can be triggered against a common clock, and how reproducible the interval proves to be are unknown to us.

**Instrument a flexible reflective aperture mechanically.** Attach an actuator to an existing flexible reflective metasurface and measure displacement, settling against a stated and justified electromagnetic criterion, and the resulting reflection-phase transient. We prescribe no particular fraction of a wavelength; choosing and justifying one is part of the experiment. Both the apertures and the actuation mechanisms exist and have not been combined. This addresses two gaps at once and would, incidentally, resolve whether the element-level figures currently in circulation bear any relation to a radiating aperture.

**Close a loop on a channel.** No reviewed platform senses geometry, estimates a channel, optimises both geometry and phase, actuates, and measures the resulting link. Four platforms each hold three of the four required components. Building the fourth combination is a programme rather than an experiment, and we assert no timeline for it.

### 11.4 Limitations

These are substantial and are stated without hedging.

**The search was not systematic.** Sources were assembled by convenience and supplemented by a documented external search, with no protocol-driven indexed-database queries and no second screener. The one exception is the forward citation search of Section 8, which is reproducible — but it too is bounded: 13 of the 20 relevant system papers were obtainable in full text and 7 are behind publisher paywalls, so the practice could extend into papers we could not read, and every count reported is a lower bound. Every absence statement in this manuscript is bounded to the reviewed set or to our recorded searches, and none should be read as a claim about a field.

**No reviewed source reports uncertainty on a headline timing value.** Neither supplementary package states a repetition count, a sample size or a dispersion figure for its principal interval — not for the 16.76 ms compensation loop, the 16.7 ms interval to stabilised radiation, the sub-0.07 s element response or the approximately 2.5 minute convergence. One subordinate quantity is the exception that shows the deficiency is real rather than assumed: the same supplementary package states a function-evaluation cycle as 0.35 ± 0.15 s, so these authors did report dispersion where they had it. The headline intervals are single stated figures. This is a deficiency in the sources rather than in the extraction, and additional literature cannot retroactively supply uncertainty for values already published without it; only the original raw data, a reanalysis, repeated measurements or new experiments could. It is the reason Group C of the reporting framework asks for repetition counts explicitly.

**One preprint claim did not survive its version of record.** A quantitative gain figure stated in the abstract of one preprint is absent from the published paper, whose abstract retains only the qualitative comparison. The claim has been withdrawn from this manuscript and the qualitative statement used instead; we do not reconstruct the figure from a published plot, which would be an upgrade of evidence. The episode is recorded here because it bears directly on Section 8: version identity matters, and two of the five propagation instances were themselves introduced between a conference or preprint version and a journal version.

**Both supplementary packages were obtained, and one of them corrected this review.** The mechanical platform's supplement showed that an iteration comprises 34 feedback cycles and stated its convergence time directly, retracting a derivation of our own that had been a factor of about forty too small (§7.2). The flexible metasurface's supplement supplied a measured interval terminating at stabilised radiation, which required us to narrow a gap claim: G4 now concerns stabilisation after a *commanded geometry change* specifically, rather than radio-frequency stabilisation in general. Obtaining a supplement changed the manuscript in both directions, which is the strongest argument we can make for retrieving them.

**Three sources were readable only as page images**, their metadata and abstracts read from rendered pages, and no load-bearing claim is drawn from them. **Some sources remain identified bibliographically only**, and quantitative claims keyed to them should be re-verified against their published versions before submission.

**Extraction and classification were performed by a single reviewer and were not independently duplicated or adjudicated.** Architecture assignment, stage coding, the timing-status judgements of Table 3 and evidence-level assignment each rest on one reader's judgement, with no second screener and no disagreement-resolution procedure. The boundaries most exposed to this are "assumed" against "unclear" in Table 3, and the distinction between a timed interval and one we have marked as incompletely defined. A duplicated extraction is the single methodological improvement most likely to change a cell.

**The reviewed set is small.** Twenty-four distinct contributions is enough to support the specific traceability and definitional findings, and not enough to support any statistical statement about the literature. We make none.

### 11.5 What this review does not establish

It does not establish that flexible intelligent metasurfaces are infeasible, that the shape-reuse assertion is false, that the tabulated morphing periods are wrong, or that any author has erred. It establishes that four specific quantities have not been measured in the literature we read, that the values currently standing in for them describe different objects, and that the difference between the two situations has not been visible on the page.

Whether the architecture works remains open. The claim made here is narrower and, we think, more useful: **in the cases traced here, the confidence expressed in the feasibility premises exceeds the evidence traced behind them.** That is a finding about the system papers audited and about the four papers in which the forward citation search located the practice, which form one connected co-authorship network. It is not a measurement of a field, and it is bounded twice over: by the reviewed set, and by full-text access to 13 of the 20 candidate system studies the search identified. A prevalence claim would require a protocol-driven search with full-text access to the seven publications we could not read. The experiments that would correct the imbalance are identifiable, and one of them builds on apparatus that has already been assembled.

---

## 12. Conclusion

**What the hardware can already do.** More than a reader arriving from the system literature would expect. Large flexible apertures radiate and remain programmable while bent. Surface shape can be sensed in situ, on three independent platforms and by three different mechanisms. Electronic phase reconfiguration is fast on semiconductor hardware and has been measured. Deformation-aware electronic compensation has been demonstrated over the air, holding a live video link while the aperture is bent. Mechanical surfaces can be commanded into target shapes and can verify, in closed loop, that they arrived. Conformal design at fixed curvature is a mature body of validated work. **None of these constituent capabilities is absent from the reviewed evidence base when considered separately; what remains unvalidated is their integration and its timing on one architecture.**

**What the evidence does not yet establish.** Every one of those capabilities was demonstrated on a platform missing one of the three things a FIM needs together: a radiating layer, a geometry the system commands, and a channel it observes. Four platforms each hold three of the four; none holds all four. Consequently no reviewed source times the adaptation chain end to end on one object, none fully delimits more than five of the ten stages — and the single source that reaches five does not radiate — none associates timing with more than six, and none couples channel estimation to a commanded shape change. Stabilised radiation is itself well evidenced — five reviewed platforms measure it quantitatively — but only one delimits a duration for it, and that one holds its geometry still. Four intervals remain unmeasured in the reviewed set: commanded actuation of a radiating aperture, settling to a tolerance that matters at the operating wavelength, post-deformation calibration duration, and the onset of trustworthy radiation *after the shape has changed*. These are unmeasured, not large — an unmeasured quantity has no value, not a bad one — and that is a more tractable problem than it first appears.

**Which timing substitutions are unsafe.** Three, each demonstrated by a value in Table 5 rather than asserted. An element-level update or response time is not an aperture-level configuration or morphing time: one panel reports both, up to two orders of magnitude apart, and one mechanical platform separates them by a factor of ten with the cause named as the membrane rather than the actuator. An open-loop replay of a known shape is not a closed-loop search for an unknown one: on a single platform those differ by more than three orders of magnitude, and the phrase "morphing time" does not distinguish them. And a partial electronic compensation loop is not an adaptation latency: the 16.76 ms interval most often quoted from this literature begins at shape acquisition and ends at bias-voltage supply, containing neither the deformation before it nor the settling after it. Reported ranges for electronic and mechanical processes also overlap, so an architecture label alone establishes no ordering.

**Which states plausibly demand fast updates, and which do not.** Instantaneous fading supplies the fastest validity timescale among the states considered — but only for operations conditioned on instantaneous channel information, and it is the only state for which a fast requirement is argued at all, by simulation and analysis rather than by measurement, which is the reverse of how the comparison is usually presented. It does not follow that every control variable inherits that timescale. Channel statistics, angular and path geometry, target kinematics, blockage, and the aperture's own deformation and calibration state each vary on their own schedules; the reviewed sources fix no relative rates among them, and nothing in the reviewed evidence requires the surface shape to track every fading realisation. If the shape is optimised from statistical or geometric state rather than per fading realisation — a premise the system literature offers explicitly, without a validity interval or a supporting measurement — then the geometry stages are exempt from the fast path, and the architecture is coherent. Establishing that premise, rather than assuming it, is the single most valuable piece of system-level work this review can point to.

**What would close the gap most efficiently.** Three experiments and one editorial change, in order of cost.

1. **Time an experiment that already exists.** Post-deformation closed-loop recalibration of a large flexible aperture has been demonstrated and not timed. Synchronised timing from a curvature change to a re-converged focus, at a stated performance tolerance, would convert the reviewed set's strongest qualitative demonstration into a quantitative constraint — conditional on the apparatus remaining available and on the two events being timestamped against a common clock.
2. **Instrument a flexible reflective aperture mechanically.** Actuate an existing flexible radiating surface and report displacement, settling against a stated and justified electromagnetic criterion, and the reflection-phase transient. Both the apertures and the actuators exist; they have not been combined and timed. This would directly fill G1 and G2 in the reviewed evidence base, and would settle whether the element-level figures now in circulation bear any relation to a radiating aperture.
3. **Close a loop on a channel.** A platform that senses geometry, estimates a channel, optimises both geometry and phase, actuates, and measures the resulting link. This is a programme, not an experiment, and no timeline should be asserted for it.
4. **Report the object, the start event and the end event.** This costs nothing and would have prevented every substitution documented in Section 8, including the one this review committed itself. A timing value that travels with its definition cannot be silently rescoped, because the change becomes visible on the page.

We propose no new hardware and no new control algorithm, and we make no novelty claim for the two-timescale or statistical-CSI principle, which already exists in the movable-antenna and FIM literatures and is not ours to claim. What is offered is the audit — a taxonomy that says which measurements may transfer, a decomposition that says which process a number times, a register that records the definitions, a traceability result bounded to the cases in which it was verified, and a reporting set derived from the deficiencies rather than from preference.

Every source carrying a load-bearing quantity has been checked against its version of record, and those quantities survive; two corrections came out of that check, and both are reported in §11.4. **One version check remains open, and it is peripheral**: a curvature-aware array-modelling precedent whose published version is paywalled, cited once for class membership, from which no quantity is drawn. One further source has no version of record to check and is cited explicitly as a preprint. No finding in this manuscript is waiting on a version check. Extraction and classification throughout were performed by a single reviewer and were not independently duplicated.

---

## References

*Numbered in order of first appearance. Every field below was verified on 18 August 2026 against the publisher-deposited Crossref record or the arXiv metadata endpoint. Where an internal draft key carried a year that differs from the version of record, the version-of-record year is used here. Entries marked in bold carry an access or version caveat.*

[1] K. R. R. Ranasinghe, J. An, I. A. Morales Sandoval, H. S. Rou, G. T. F. de Abreu, C. Yuen, and M. Debbah, "Flexible intelligent metasurfaces in high-mobility MIMO integrated sensing and communications," *IEEE Trans. Wireless Commun.*, vol. 25, pp. 13319–13335, 2026, doi: 10.1109/TWC.2026.3668992.

[2] J. An, C. Yuen, M. Di Renzo, M. Debbah, H. V. Poor, and L. Hanzo, "Downlink multiuser communications relying on flexible intelligent metasurfaces," in *Proc. IEEE Global Commun. Conf. (GLOBECOM)*, Dec. 2024, pp. 4932–4937, doi: 10.1109/GLOBECOM52923.2024.10901792.

[3] S. Yang, Z. Wan, B. Ning, W. Mei, J. An, Y. C. Eldar, and C. Yuen, "Flexible intelligent metasurface-aided wireless communications: Architecture and performance," *IEEE Trans. Wireless Commun.*, vol. 25, pp. 6823–6836, 2026, doi: 10.1109/TWC.2025.3627095.

[4] Z. Akram, M. Elsayed, H. Hameed, M. S. Ali, J. ur R. Kazim, M. A. Imran, and Q. H. Abbasi, "A scalable and integrated reconfigurable intelligent surface," *Adv. Electron. Mater.*, vol. 12, no. 1, art. e00674, Jan. 2026, doi: 10.1002/aelm.202500674. (Published online 12 Dec. 2025; the volume 12, issue 1 print issue is dated January 2026.)

[5] R. Neuder, M. Späth, M. Schüßler, and A. Jiménez-Sáez, "Architecture for sub-100 ms liquid crystal reconfigurable intelligent surface based on defected delay lines," *Commun. Eng.*, vol. 3, no. 1, art. 70, May 2024, doi: 10.1038/s44172-024-00214-3.

[6] F. Li, T. Pan, W. Li, Z. Peng, D. Guo, X. Jia, T. Hu, L. Wang, W. Wang, M. Gao, G. Yao, L. Zuo, M. Bi, X. Weng, W. Tang, and Y. Lin, "Flexible intelligent microwave metasurface with shape-guided adaptive programming," *Nature Commun.*, vol. 16, no. 1, art. 3161, Apr. 2025, doi: 10.1038/s41467-025-58249-9. (Supplementary Information and Peer Review File retrieved from the publisher and cited by note number.)

[7] Y. Bai, H. Wang, Y. Xue, Y. Pan, J.-T. Kim, X. Ni, T.-L. Liu, Y. Yang, M. Han, Y. Huang, J. A. Rogers, and X. Ni, "A dynamically reprogrammable surface with self-evolving shape morphing," *Nature*, vol. 609, no. 7928, pp. 701–708, Sep. 2022, doi: 10.1038/s41586-022-05061-w. (Extended Data, Supplementary Information and Peer Review File retrieved from the publisher and cited by note number.)

[8] X. Ni, H. Luan, J.-T. Kim, S. I. Rogge, Y. Bai, J. W. Kwak, S. Liu, D. S. Yang, S. Li, S. Li, Z. Li, Y. Zhang, C. Wu, X. Ni, Y. Huang, H. Wang, and J. A. Rogers, "Soft shape-programmable surfaces by fast electromagnetic actuation of liquid metal networks," *Nature Commun.*, vol. 13, no. 1, art. 5576, Sep. 2022, doi: 10.1038/s41467-022-31092-y.

[9] Y. Saifullah, Y. He, A. Boag, G.-M. Yang, and F. Xu, "Recent progress in reconfigurable and intelligent metasurfaces: A comprehensive review of tuning mechanisms, hardware designs, and applications," *Adv. Sci.*, vol. 9, no. 33, art. 2203747, Nov. 2022, doi: 10.1002/advs.202203747.

[10] A. Tishchenko, M. Khalily, A. Shojaeifard, F. Burton, E. Björnson, M. Di Renzo, and R. Tafazolli, "The emergence of multi-functional and hybrid reconfigurable intelligent surfaces for integrated sensing and communications — A survey," *IEEE Commun. Surveys Tuts.*, vol. 27, no. 5, pp. 2895–2936, Oct. 2025, doi: 10.1109/COMST.2024.3519785.

[11] W. Ma, L. Zhu, Y. Tan, B. Zheng, Y. Zhang, Y. Zhang, K. Ying, Z. Gao, H. Sun, X. Shao, Z. Xiao, D. Niyato, and R. Zhang, "A survey on reconfigurable and movable antennas for wireless communications and sensing," 2026, arXiv:2602.17977. **Preprint, read in full; no version of record located.**

[12] V. Kumar, A. Papazafeiropoulos, P. Kourtessis, J. Senior, M. Chafii, D. I. Kaklamani, and I. S. Venieris, "Flexible intelligent metasurface for downlink communications under statistical CSI," *IEEE Wireless Commun. Lett.*, vol. 15, pp. 1150–1154, 2026, doi: 10.1109/LWC.2025.3649732. (Full text read as arXiv:2512.23045.)

[13] L. He, V. Kumar, A. Papazafeiropoulos, M. Wen, L.-N. Tran, and M. Chafii, "Achievable rate optimization for large flexible intelligent metasurface assisted downlink MISO under statistical CSI," 2026, arXiv:2601.15471. **Identified bibliographically; full text not retrieved. Cited only, jointly with [12], for the existence of published statistical-CSI FIM optimisation; shares three authors with [12] and is not an independent confirmation of it.**

[14] X. Zhu, K.-K. Wong, H. Xu, C. Rao, and H. Shin, "Fluid antenna systems enabling 6G HRLLC with port switching delay," 2026, arXiv:2605.06275. **Identified bibliographically; cited only as a precedent for delay-aware modelling in an adjacent field.**

[15] I. A. Morales Sandoval, T. Venkataramanaiah, K. R. R. Ranasinghe, J. An, H. S. Rou, and G. T. F. de Abreu, "Bistatic integrated sensing and communications with flexible intelligent metasurfaces," 2026, arXiv:2607.29137. (An extended version of this work is [1].)

[16] M. Guo, P. Xin, H. Sun, H. Li, L. F. Chernogor, Z. Jin, T. Liu, and Y. Zheng, "Beam steering flexible transparent metasurfaces based on multi-bit phase gradient variations," *Sci. Rep.*, vol. 15, no. 1, May 2025, doi: 10.1038/s41598-025-99768-1.

[17] D. Lu, Z. Wang, C. Zhang, and Y. Yu, "A versatile design method applied to conformal metasurface array antenna," *Microw. Opt. Technol. Lett.*, vol. 67, no. 3, art. e70134, Mar. 2025, doi: 10.1002/mop.70134.

[18] D. Lu, C. Zhang, Z. Wang, R. Li, J. Yan, and Y. Yu, "Design of conformal reconfigurable reflectarray antenna based on flexible material," *IEEE Antennas Wireless Propag. Lett.*, vol. 25, no. 5, pp. 2265–2269, May 2026, doi: 10.1109/LAWP.2026.3676871.

[19] C. Xu, J. An, T. Bai, S. Sugiura, R. G. Maunder, Z. Wang, L.-L. Yang, and L. Hanzo, "Channel estimation for reconfigurable intelligent surface assisted high-mobility wireless systems," *IEEE Trans. Veh. Technol.*, vol. 72, no. 1, pp. 718–734, Jan. 2023, doi: 10.1109/TVT.2022.3203818.

[20] M. Gal-Katziri, A. Fikes, and A. Hajimiri, "Flexible active antenna arrays," *npj Flexible Electron.*, vol. 6, no. 1, art. 85, Oct. 2022, doi: 10.1038/s41528-022-00218-z.

[21] M. Alesheikh, S. Saadat, and H. Aghasi, "Feasibility study of curvature effect in flexible antenna arrays for 2-dimensional beam alignment of 6G wireless systems," in *Proc. IEEE Int. Symp. Antennas Propag. and North Amer. Radio Sci. Meeting (AP-S/CNC-USNC-URSI)*, Jul. 2025, pp. 1–4, doi: 10.1109/AP-S/CNC-USNC-URSI55537.2025.11265965. **Published version paywalled; the held copy is arXiv:2409.09590.**

[22] J. Budhu, L. Szymanski, and A. Grbic, "Design of planar and conformal, passive, lossless metasurfaces that beamform," *IEEE J. Microw.*, vol. 2, no. 3, pp. 401–418, Jul. 2022, doi: 10.1109/JMW.2022.3181719.

[23] I. Yoo and D. R. Smith, "Design of conformal array of rectangular waveguide-fed metasurfaces," 2021, arXiv:2109.09450.

[24] H. Li, C. Ma, F. Shen, K. Xu, D. Ye, J. Huangfu, C. Li, L. Ran, and T. A. Denidni, "Wide-angle beam steering based on an active conformal metasurface lens," *IEEE Access*, vol. 7, pp. 185264–185272, 2019, doi: 10.1109/ACCESS.2019.2960639.

[25] F. Pepe, I. Iudice, G. Castaldi, M. Di Renzo, and V. Galdi, "Conformal reconfigurable intelligent surfaces: A cylindrical geometry perspective," *Adv. Electron. Mater.*, art. e00550, Jan. 2026, doi: 10.1002/aelm.202500550.

[26] H. Chen, T. Liu, M. Chen, D. Wang, W. Li, B. Wu, L. Wang, G. Liu, and L. Wang, "Wide-angle conformal active metasurface for dynamic beam steering and orbital angular momentum generation," *Laser Photon. Rev.*, vol. 20, no. 3, art. e01500, Feb. 2026, doi: 10.1002/lpor.202501500. (Published online 28 Sep. 2025; the volume 20, issue 3 print issue is dated February 2026.)

[27] T. Harz, T. Kleine-Ostmann, and T. Schrader, "Design of a continuously tunable reflectarray element for 5G metrology in the k-band," *Adv. Radio Sci.*, vol. 18, pp. 1–5, Dec. 2020, doi: 10.5194/ars-18-1-2020.

[28] T. Harz and T. Kleine-Ostmann, "Measurement and optimization of a continuously tunable 10 × 10 reflectarray antenna for 5G metrology in the K-band," *Adv. Radio Sci.*, vol. 19, pp. 215–220, Jan. 2022, doi: 10.5194/ars-19-215-2022.

[29] J. An, Z. Han, D. Niyato, M. Debbah, C. Yuen, and L. Hanzo, "Flexible intelligent metasurfaces for enhancing MIMO communications," 2025, arXiv:2502.16478. **Author version, read in full; IEEE Trans. Commun. record not retrieved.**

[30] H. Hu, J. An, L. Gan, H. Li, N. Al-Dhahir, G. K. Karagiannidis, and A. Nallanathan, "Weighted sum-rate enhancement for flexible intelligent metasurface-assisted multicell systems," *IEEE Trans. Wireless Commun.*, vol. 25, pp. 18579–18595, 2026, doi: 10.1109/TWC.2026.3701359. (Full text read as arXiv:2606.06845.)

[31] J. Xiao, J. Wang, Q. Cui, Y. Yang, X. Li, D. Niyato, and C. Yuen, "Channel estimation for flexible intelligent metasurfaces: From model-based approaches to neural operators," *IEEE Trans. Wireless Commun.*, vol. 25, pp. 10684–10701, 2026, doi: 10.1109/TWC.2026.3654581. (Full text read as arXiv:2508.00268v4.)

[32] J. An, C. Yuen, M. Di Renzo, M. Debbah, H. V. Poor, and L. Hanzo, "Flexible intelligent metasurfaces for downlink multiuser MISO communications," *IEEE Trans. Wireless Commun.*, vol. 24, no. 4, pp. 2940–2955, Apr. 2025, doi: 10.1109/TWC.2025.3526843. (Journal extension of [2]; read from an open institutional-repository copy.)

[33] C. Huang, G. Chen, Z. Xu, J. Zhu, T. Pan, R. Tafazolli, and W. Huang, "Flexible reconfigurable intelligent surface-aided covert communications in UAV networks," *IEEE J. Sel. Areas Commun.*, vol. 44, pp. 1577–1588, 2026, doi: 10.1109/JSAC.2025.3639197. **Full text not retrieved (paywalled); cited only for its published-record authorship, which is verified.**

[34] A. Bansal, R. Hewson, M. Santer, and W. G. Whittow, "Optimal morphing metasurface lens for next generation RF sensing and communications," in *Proc. 18th Eur. Conf. Antennas Propag. (EuCAP)*, Mar. 2024, pp. 1–3, doi: 10.23919/EuCAP60739.2024.10501383. (Full text read from the authors' open figshare deposit, 18 August 2026.)

---


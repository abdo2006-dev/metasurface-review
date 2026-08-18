## 2. Scope, corpus and method

### 2.1 Article type

This is a **structured critical review**. It is not a systematic review, a systematic mapping study or a scoping review, and it does not adopt PRISMA terminology, because it does not satisfy the requirement those labels carry: a reproducible, protocol-driven, multi-database *search*. What it does possess is a reproducible *extraction* protocol, and the distinction is worth stating plainly rather than blurring, since misdescribing a method is the kind of failure this manuscript examines in others.

### 2.2 Corpus

The reviewed set comprises **24 independent research contributions across 31 files**. Four of those files are supplementary-information or peer-review documents belonging to two of the papers; they are evidence *about* those papers, not evidence alongside them, and are not counted as separate contributions. Duplicate versions, conference-and-journal pairs and same-group design lineages were identified and collapsed into independence groups, so that related publications are never counted as mutual confirmation of one another. Three sources were readable only as page images and no load-bearing claim is drawn from them.

The corpus was assembled by convenience rather than by a protocol-driven database query. Inclusion criteria are therefore stated retrospectively, and describe what the set *is* rather than a prospective filter: peer-reviewed articles, preprints and author manuscripts concerning FIM system modelling; flexible or conformal reflective and transmissive metasurface hardware; programmable mechanical surface actuation; electronically reconfigurable RIS hardware reporting timing or power; high-mobility channel estimation for reconfigurable surfaces; and reviews of any of these. Sources with no wireless, electromagnetic or mechanical-actuation content were excluded.

Six sources were first read as preprints or author manuscripts. Publisher-deposited records confirm versions of record for five of them, and the published full texts of the three that carry the most weight — the high-mobility FIM–ISAC study, the FIM architecture-and-performance paper and the high-mobility channel-estimation paper — were obtained and inspected. Every load-bearing timing and parameter quantity keyed to them survives at the published locators, which this manuscript cites. One non-timing claim did not survive, and is reported in Section 11.4 as an instance of why the check was worth performing.

### 2.3 Searches

Two kinds of search supplement the corpus, and their evidential weight differs.

**A documented but non-systematic external search** (ten queries, 17 August 2026) established whether a FIM-specific review exists, whether two-timescale or statistical-CSI FIM control is already published, whether any measured FIM actuation latency exists, and where the hardware-feasibility timing claims in the FIM system literature originate. It used a general web-search interface, which does not expose reproducible hit counts; its results are recorded as search outcomes rather than as established absences.

**A forward citation search** (18 August 2026) is reproducible and is reported as such. Every work citing the three primary hardware sources was retrieved through the OpenAlex citation graph — 160, 102 and 44 citing records for the filamentary mechanical platform, the soft shape-programmable surface and the flexible microwave metasurface respectively — giving 306 records and 262 unique works after deduplication. Title-and-abstract screening on a wireless and communications term set reduced these to 64, and manual exclusion of optics, photonics and materials-only work to 20 distinct flexible-metasurface or reconfigurable-surface system papers. Thirteen full texts were obtained from arXiv author deposits and one open institutional repository; each was scanned for timing terminology with ligature normalisation and hyphenated-linebreak repair, and every match was read in context. **Seven papers are behind publisher paywalls and were not read**, so every count arising from this search is a lower bound. Section 8 reports the result; the queries, screening counts and the identity of the unread papers are recorded in the supporting documentation.

### 2.4 Extraction protocol

Extraction, unlike search, followed a fixed protocol applied uniformly to every source:

1. **A seven-class architecture taxonomy** with explicit transfer rules (Section 3), assigned before any timing value was compared.
2. **A ten-stage adaptation-chain template** (Section 5), against which each source's treatment of each stage is coded as demonstrated, measured, simulated, assumed, absent or unclear.
3. **A timing register** (Section 6) in which every reported value carries a timed object, a named start event, a named end event, a measured/simulated/projected/derived flag, the architecture on which it was obtained, and a comparability class. Two values may be compared only if their comparability classes intersect.
4. **A seven-level evidence ladder**: **L1** analytical or model-based derivation; **L2** communication-system simulation; **L3** full-wave electromagnetic simulation of the actual structure; **L4** component measurement (a unit cell, sensor, actuator or delay line); **L5** prototype radio-frequency measurement of an assembled aperture; **L6** over-the-air demonstration of a working link or application; **L7** end-to-end closed-loop validation — observation, decision, actuation and *verified, timed* stabilised radio-frequency performance. Evidence is never upgraded across levels: a system simulation is not hardware validation, a measured actuator is not a radiating system, and an electronic switching time is not a mechanical settling time. **No reviewed source reaches L7**, and the reason is given in Section 9.3.
5. **An independence rule.** A preprint and its version of record are two versions of one study. A conference paper and its journal extension are one lineage. Supplementary material belongs to its parent paper. Independence between citing works is tested by author-set intersection, not assumed from differing first authors.
6. **An absence-claim rule.** Every statement about what is missing is reduced to one of two checkable forms: *this named document does not report quantity Q*, or *across the N sources in this named table, no row records Q*. No statement about the field as a whole is made anywhere in this manuscript.

### 2.5 What follows from the method

Two constraints are inherited by everything downstream. Absence of a measurement in the literature we read is not evidence that the measurement does not exist, still less that the capability is unattainable; every absence statement below is bounded to the reviewed set or to the searches above. And because no reviewed source reports a repetition count or a dispersion figure for its headline timing value, **no interval quoted in this manuscript carries an uncertainty**. That is a deficiency in the sources rather than in the extraction, and no amount of further searching would repair it. Section 11.4 states the remaining limitations in full.

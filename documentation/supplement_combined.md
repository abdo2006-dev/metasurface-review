# Supplementary Material

*Accompanies the manuscript draft of 22 August 2026. This material supports verification; the main manuscript is self-contained without it. Bracketed reference numbers, table numbers and figure numbers are those of the manuscript: one bibliography serves both documents, so this material carries no separate reference list and cites nothing the manuscript's list does not contain.*



# Supplementary Table S1 — Complete timing register

Every timing quantity located in the reviewed set, with its timed object, start event, end event, measurement status and source. The main manuscript reproduces the subset that carries the argument (Table 2); this table is the full record, and the row numbering is continuous with it.

M = measured · S = simulated · P = projected · D = derived by us · A = assumed. Architecture classes are those of Table 1.

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
| 9 | End-to-end reconfiguration | **< 0.1 ms** | host command over the external control link | configuration written to the diode bias; **no EM criterion** | **one 16 × 16 tile** | A5 | M/design bound | ≈40 μs LAN/Wi-Fi, up to 100 μs USB/UART, against ≈40 ns internal once stored; **not per-element** — that reading was withdrawn 22 Aug 2026 | [4] abstract; decomposition p. 6 |
| 10 | Tile configuration update | **< 10 ms** | pattern command | tile pattern written; **no EM criterion** | **one 16 × 16 tile** | A5 | M/design bound | as operated in the measurement campaign; same object as row 9 | [4] p. 8, conclusion p. 9 |
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


# Supplementary Table S2 - Timing-quantity taxonomy

The quantity types used throughout the review, each with its start event, end event and timed object, and the substitution it most often invites. Values may be compared only within a type, and only when their comparability classes intersect.

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


# Supplementary Section S3 — Extraction and version-control notes

These records document how specific quantities in the reviewed set were verified, and where a
verification changed what this review could claim. They are evidence about the extraction process
rather than about the hardware, and are held here so the main manuscript describes the study rather
than its editing history.

**One preprint claim did not survive its version of record.** A quantitative gain figure stated in the abstract of one preprint is absent from the published paper, whose abstract retains only the qualitative comparison. The claim has been withdrawn from this manuscript and the qualitative statement used instead; we do not reconstruct the figure from a published plot, which would be an upgrade of evidence. The episode is recorded here because it bears directly on §5.2: version identity matters, and two of the five propagation instances were themselves introduced between a conference or preprint version and a journal version.


**Both supplementary packages were obtained, and one of them corrected this review.** The mechanical platform's supplement showed that an iteration comprises 34 feedback cycles and stated its convergence time directly, retracting a derivation of our own that had been a factor of about forty too small (§4.3). The flexible metasurface's supplement supplied a measured interval terminating at stabilised radiation, which required us to narrow a gap claim: G4 now concerns stabilisation after a *commanded geometry change* specifically, rather than radio-frequency stabilisation in general. Obtaining a supplement changed the manuscript in both directions, which is the strongest argument we can make for retrieving them.


## S3.3 A withdrawn derivation

An earlier version of this review derived a closed-loop convergence figure of approximately 1.25–3.75 s for the filamentary mechanical platform by multiplying its ≈0.25 s feedback cycle by its reported 5–15 iterations. That derivation was invalid: an iteration on that platform is 4(N+M)+2 = 34 function evaluations, not one cycle. The source states the convergence time directly as approximately 2.5 minutes, and that figure supersedes ours. The error is the same class of substitution the traceability audit documents in others — an informal quantity name, an ambiguous unit, and a plausible arithmetic step — which is why it is reported rather than quietly corrected.


# Supplementary Table S4 — The complete reporting checklist

Manuscript Table 5 gives the ten fields whose absence caused the specific failures documented in this review. This is the complete set, with the observed deficiency motivating every field. Groups A, B and C are the core fields we suggest for any paper reporting a deformable or reconfigurable aperture; D and E apply where a control loop is claimed; F applies to any mobility or ISAC claim. Every field should be reported when applicable to the platform in question. This is a recommendation, not a standard.

| Group | Field | Motivating deficiency in the reviewed set |
|---|---|---|
| **A — architecture** | Architecture class: passive flexible / shape-aware programmable / self-morphing / rigid reconfigurable / flexible active | Seven physically distinct systems are grouped under overlapping names (Table 1) |
| | **Deformation source: externally imposed or self-actuated** | The distinction between compensating a shape and commanding one is this review's central taxonomic finding, and it is rarely stated explicitly |
| | Whether a radio-frequency layer is present, and what it consists of | Every measured mechanical timescale in the reviewed set was obtained on a platform with no RF layer |
| | Control granularity: independently addressable channels versus total elements | One reviewed aperture has 512 meta-atoms and 32 control channels; the difference is not usually foregrounded |
| **B — timing** *(the five fields we suggest accompany every reported interval)* | **Object timed** — one element, one tile, or the whole aperture | One mechanical platform reports element- and full-surface figures a factor of ten apart, and the element figure was tabulated downstream as a surface one; separately, one panel's two bounds on **the same** tile sit two orders of magnitude apart with no object stated in the abstract that carries one of them |
| | **Start event**, named physically | "Response time" denotes at least five different intervals in the reviewed set |
| | **End event**, named physically, with its threshold | Threshold definitions are inconsistent where present and absent for most reported intervals. The two sources that state one state incommensurable ones: 10 %/90 % amplitude thresholds on a liquid-crystal device, and "the first video frame after which no displacement deviation is visible" on a 60 fps camera — an instrument-limited criterion with a ≈16.7 ms floor |
| | **Measured, simulated, projected or derived** | A projected sub-2 ms figure appears in the same discussion as measured 15 ms and 72 ms values |
| | Direction, where the process is asymmetric | Switch-on and switch-off differ by nearly a factor of five in the reviewed liquid-crystal device |
| **C — mechanics** *(any surface whose geometry changes)* | Actuation mechanism, drive quantity and drive level | Reported for the mechanical platforms; absent for every flexible radiating aperture |
| | Displacement range, in millimetres **and in wavelengths** | The system literature works in wavelengths and the hardware literature in millimetres; almost no source gives both |
| | **A stated and justified electromagnetic settling criterion** — an allowable phase or RF-performance error, or the corresponding displacement tolerance relative to wavelength, with the basis for the value chosen | No reviewed source defines settling electromagnetically; settling is reported, where reported at all, as the cessation of visible motion. This review prescribes no numerical fraction of a wavelength, and none should be inferred from the illustrative arithmetic in §5.3 |
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


# Supplementary Section S5 — Forward-citation search, screening flow and study-family register

This section records what is needed to audit contribution C3. The per-work decision table (one row for each of the 262 works) and the executable retrieval and screening code are in the public reproducibility repository, `https://github.com/abdo2006-dev/metasurface-review`.

## S5.1 Retrieval and screening flow

| Step | Count |
|---|---|
| Seed-wise citing records retrieved (three primary hardware sources) | **306** |
| Unique works after deduplication by identifier | **262** |
| Passing the stage-1 title/abstract expression | **65** |
| Stage-2 candidate system-study records | **24** |
| Distinct studies after version-family collapse | **20** |
| Read in full | **13** |
| Behind publisher paywalls, no open deposit, not read | **7** |

Stage one is automatic and deterministic for the dated 18 August 2026 search: re-running the published code against the preserved records reproduces it exactly, while a live re-query may differ because OpenAlex is updated continuously. Stage two is a manual judgement recorded per work with its reason. The **13 studies read in full partition exactly into 4 propagation studies and 9 no-timing-value studies**. The remaining **7 of the 20 studies were not readable in full**.

## S5.2 Version-family collapse rule

A preprint and its version of record are two versions of one study; a conference paper and its journal extension are one lineage; supplementary material belongs to its parent paper. Shared authorship alone never collapses two studies — only a bibliographic or version relationship does. Identifier-level deduplication does not perform this collapse: four version groups occur here, of which one is a single work indexed twice and three are genuine conference-to-journal or preprint-to-record lineages. One of those lineages carries a timing assertion in its journal version that is absent from its conference version.

## S5.3 Study-family register — all 20 studies

Author-network status is taken from published-record author lists, which are verifiable even where the full text is not. "Lineage" means the FIM system papers audited in §5.2; "seeds" means the three primary hardware sources.

| Study family | Records | Citation | Full text | Final role | Author network |
|---|---|---|---|---|---|
| **F-ANJ-DL** | 2 | An, Yuen, Di Renzo, Debbah, Poor & Hanzo — GLOBECOM 2024 (conf.) / IEEE TWC 2025 (journal ext.), doi:10.1109/twc.2025.3526843 · [2] / [32] | read | propagation | shares an author with the lineage |
| **F-ANJ-MIMO** | 1 | An, Han, Niyato, Debbah, Yuen & Hanzo, IEEE Trans. Commun., 73(9):7349-7365, Sep. 2025, doi:10.1109/tcomm.2025.3550318 · [29] | read | no timing value | shares an author with the lineage |
| **F-APS** | 1 | Zuo, Cheng, Qian, Liao & Ding, Acta Physica Sinica 75(1), 2026, doi:10.7498/aps.75.20260154  | **not readable** | not readable | disjoint from lineage **and** all three seeds |
| **F-BAN** | 1 | Bansal, Hewson, Santer & Whittow, EuCAP 2024, doi:10.23919/EuCAP60739.2024.10501383 · [34] | read | no timing value | disjoint from lineage **and** all three seeds |
| **F-DRL** | 1 | Wang, Zhang, An, Cheng, Dong & Wang, IEEE Wireless Commun. Lett., 2026, doi:10.1109/lwc.2026.3709756  | **not readable** | not readable | shares an author with the lineage |
| **F-FAA** | 2 | Yang, An, Xiu, Lyu, Ning, Zhang, Debbah & Yuen — ICCT 2024 (conf.) / IEEE TWC 2025 (journal ext.), doi:10.1109/twc.2025.3545305  | read | no timing value | disjoint from the lineage |
| **F-FCA** | 1 | Guo, Yang, Dong, Yang, Deng, Zhang & Yuen, IEEE Internet Things J., 2025, doi:10.1109/jiot.2025.3580372  | read | no timing value | disjoint from the lineage |
| **F-HU** | 2 | Hu, An, Gan, Li, Al-Dhahir, Karagiannidis & Nallanathan — GLOBECOM 2025 (conf.) / IEEE TWC 2026 (journal ext.), doi:10.1109/twc.2026.3701359 · [30] | read | propagation | shares an author with the lineage |
| **F-HUA** | 1 | Huang, Chen, Xu, Zhu, Pan, Tafazolli & Huang, IEEE J. Sel. Areas Commun., 2025, doi:10.1109/jsac.2025.3639197 · [33] | **not readable** | not readable | disjoint from the lineage |
| **F-KUM** | 1 | Kumar, Papazafeiropoulos, Kourtessis, Senior, Chafii, Kaklamani & Venieris, IEEE Wireless Commun. Lett., 2025, doi:10.1109/lwc.2025.3649732 · [12] | read | no timing value | disjoint from lineage **and** all three seeds |
| **F-MIMO-ISAC** | 1 | Teng, An, Gan, Karagiannidis, Nallanathan & Al-Dhahir, ICC 2026, doi:10.1109/icc59461.2026.11588131  | read | no timing value | shares an author with the lineage |
| **F-MING** | 1 | Ming, An, Gan, Nallanathan & Al-Dhahir, IEEE Trans. Veh. Technol., 2025, doi:10.1109/tvt.2025.3614693  | **not readable** | not readable | shares an author with the lineage |
| **F-RAN** | 1 | Ranasinghe, An, Morales Sandoval, Rou, de Abreu, Yuen & Debbah, IEEE TWC, 2026, doi:10.1109/twc.2026.3668992 · [1] | read | propagation | shares an author with the lineage |
| **F-SENS** | 1 | Teng, An, Gan, Al-Dhahir & Han, IEEE Trans. Veh. Technol., 2025, doi:10.1109/tvt.2025.3584865  | read | no timing value | shares an author with the lineage |
| **F-SRM** | 1 | Jiang, An, Gan, Al-Dhahir & Karagiannidis, ICC 2026, doi:10.1109/icc59461.2026.11587389  | **not readable** | not readable | shares an author with the lineage |
| **F-T3D** | 1 | Mursia, Devoti, Rossanese, Sciancalepore, Gradoni, Di Renzo & Costa-Pérez, IEEE Trans. Commun., 2024, doi:10.1109/tcomm.2024.3443738  | read | no timing value | shares an author with the lineage |
| **F-TAP** | 1 | An, Debbah, Cui, Chen & Yuen, IEEE Trans. Antennas Propag., 2025, doi:10.1109/tap.2025.3571069  | **not readable** | not readable | shares an author with the lineage |
| **F-XIA** | 2 | Xiao, Wang, Cui, Yang, Li, Niyato & Yuen, IEEE TWC, 2026, doi:10.1109/twc.2026.3654581 · [31] | read | propagation | shares an author with the lineage |
| **F-YAN** | 1 | Yang, Wan, Ning, Mei, An, Eldar & Yuen, IEEE TWC, 2025, doi:10.1109/twc.2025.3627095  | read | no timing value | shares an author with the lineage |
| **F-ZAR** | 1 | Zarini, Kazemi, Sookhak, Ghrayeb & Di Renzo, PIMRC 2025, doi:10.1109/pimrc62392.2025.11274788  | **not readable** | not readable | shares an author with the lineage |

## S5.4 What the register supports

- **4 studies** reuse a primary timing value with its scope changed, carrying 5 instances (P1, P2, P3, P4, P5), and they form **one connected co-authorship network**.
- **9 studies** cite the same primary hardware and attach no timing value; two of them share no author with the lineage or any seed.
- **0 author-disjoint publication groups** reproduce the practice within the observation window, which is why C3 is held at its stated evidence level.
- **7 studies** could not be read. Exactly one of them is disjoint from both the lineage and all three seeds, so that single study is the whole residual risk to the independence finding. No claim is made about what any unread study contains.

Every count above is a lower bound on a partially observed set, and no prevalence, proportion or rate is estimated from it.


# Supplementary Section S6 — Coding scheme and the per-source adaptation-chain matrix

The main manuscript states the four principles that govern extraction (Section 2) and reports the counts that follow from them (Section 4). This section gives the symbolic scheme in full, together with the coded matrix from which every count in Section 4 is taken.

## S6.1 Two-axis stage coding

Each source's treatment of each of the ten adaptation stages is coded on two independent axes. Collapsing them into one symbol allows a radiation-pattern measurement to be counted as a measured latency.

**Axis A — stage evidence status**, answering *what did this source establish about this stage?*

| Code | Meaning |
|---|---|
| **Q** | quantitatively measured — a physical or radio-frequency quantity is reported |
| **D** | demonstrated — shown working, no quantity |
| **S** | simulated |
| **A** | assumed |
| **✗** | absent |
| **n/a** | not applicable to that architecture |
| **?** | unclear |
| **RS** | review statement — an assertion in a survey, carrying no primary evidence of its own |

**Axis B — timing-evidence status**, answering *what does the source establish about how long this stage takes?* A quantity belongs on this axis only if it carries information about duration, rate or temporal allocation.

| Code | Meaning |
|---|---|
| **·T** | a stage duration measured or otherwise individually reported, with identifiable start and end events, and separable from neighbouring stages. Only `·T` licenses the verb *times* |
| **·(T)** | duration information genuinely associated with the stage, but only as a stated share, component or residual of a larger aggregate, or otherwise not independently delimited |
| **·[R]** | a temporal rate or relative rate factor. It carries timing-related information but is **not** a duration, and never contributes to a duration count |
| **·[A]** | an interval the experimenter deliberately allocated or waited, **not** an observed process duration, and never contributes to a measured-duration count |
| *(no marker)* | no temporal information |

An accuracy is never timing evidence. A root-mean-square deviation, a displacement error or any other accuracy figure stays on Axis A alone, however quantitative it is.

The two axes are orthogonal. `Q` without a marker — a measured pattern with no duration — and `S·T` — a fully delimited *simulated* runtime — are both routine in this literature, and both would be misread under a single code. Counts reported in the manuscript state which axis they are counting, and where the totals differ under the two axes, both are given.

## S6.2 The evidence ladder

Evidence is never upgraded across levels.

| Level | Meaning |
|---|---|
| **L1** | analytical or model-based derivation |
| **L2** | communication-system simulation |
| **L3** | full-wave electromagnetic simulation of the actual structure |
| **L4** | component measurement — a unit cell, sensor, actuator or delay line |
| **L5** | prototype radio-frequency measurement of an assembled aperture |
| **L6** | over-the-air demonstration of a working link or application |
| **L7** | end-to-end closed-loop validation — observation, decision, actuation and *verified, timed* stabilised radio-frequency performance |

No reviewed source reaches L7. The reason is the integration gap stated in §5.3: no reviewed platform holds an aperture, a commanded geometry and an observed channel together, so no platform is the object whose end-to-end timing would be measured.

## S6.3 The per-source matrix

*Stage evidence status:* **Q** quantitatively measured · **D** demonstrated · **S** simulated · **A** assumed · **✗** absent · **n/a** not applicable · **RS** review statement.
*Timing status, appended:* **·T** a measured stage duration reported in its own right · **·(T)** a share or residual of an aggregate · **·[R]** a rate · **·[A]** an allocated interval · *no marker* untimed. The two right-hand columns count `·T` and `·(T)`.

| Source | Arch. | S1 sense | S2 geom. est. | S3 chan. est. | S4 optim. | S5 ctrl tx | S6 electronic | S7 morphing | S8 settling | S9 calib. | S10 stable RF | **·T** | **·(T)** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ranasinghe *et al.* [1]** | A1 | ✗ | ✗ | A | S | ✗ | ✗ | A (instant) | ✗ | ✗ | A — unbounded shape reuse | 0 | 0 |
| **An *et al.* [2]** | A1 | ✗ | ✗ | A (perfect CSI) | S | ✗ | ✗ | A (instant) | ✗ | ✗ | A (quasi-static) | 0 | 0 |
| **Yang *et al.* [3]** | A1 | ✗ | ✗ | **S·T** runtime | S | ✗ | A (per slot) | A (per subframe) | ✗ | ✗ | A | 1 | 0 |
| **Morales Sandoval *et al.* [15]** | A1 | ✗ | ✗ | A | S | ✗ | ✗ | A | ✗ | ✗ | A | 0 | 0 |
| **Xu *et al.* [19]** | A5 | S (pilots) | n/a | S | S | ✗ | A | n/a | n/a | ✗ | S | 0 | 0 |
| **Li *et al.* [6]** | A3 | **Q·(T)** ≈2 ms reception (share of ≈4 ms) | **Q·(T)** ≈2 ms processing; RMSD 2.36 mm is an *accuracy* | ✗ absent | **Q·T** ANN ≈2 ms | **Q·(T)** ≈5.5 ms RS-232 residual | **Q·T** 5.25 ms supply | ✗ external | ✗ | D (folded into a learned map) | **Q·T**‡ | **3** | 3 |
| **Lu *et al.* [18]** | A3 | ✗ | ✗ (a priori) | ✗ | S | ? | D | ✗ (static) | ✗ | D per curvature | **Q** patterns | 0 | 0 |
| **Neuder *et al.* [5]** | A5 | ✗ | n/a | ✗ | ✗ | ✗ | **Q·T** 15 / 72 ms | n/a | n/a | ✗ | **Q** patterns | 1 | 0 |
| **Akram *et al.* [4]** | A5 | ✗ | n/a | ✗ | ✗ | **Q·[R]** ×¼ multiplexing rate | **Q·T** <0.1 ms / <10 ms | n/a | n/a | ✗ | **Q** patterns, power | **1** | 0 |
| **Bai *et al.* [7]** | A4 | **Q·T** 0.08 ± 0.04 s | **Q·T** 0.11 ± 0.05 s | n/a | **Q·(T)** optimisation ≈0 | **Q·T** 0.06 ± 0.01 s | n/a | **Q·T** <0.07 s / <0.1 s | **Q·[A]** 0.1 ± 0.05 s allocated pause | ✗ | ✗ no RF layer | **4** | 1 |
| **Ni *et al.* [8]** | A4 | ✗ | ✗ | n/a | ✗ (scripted) | **Q·(T)** ≈50 ms script (component of ≈650 ms) | n/a | **Q·T** 30 / 300 ms | **Q·(T)** ≈250 ms within the 300 ms | ✗ | ✗ no RF layer | **1** | 2 |
| **Gal-Katziri *et al.* [20]** | A7 | D self-sensing | D | ✗ | D | D | D | ✗ external | ✗ | **D — no duration** | **Q** ≈80 mW at 1 m | 0 | 0 |
| **Ma *et al.* [11]** | A6 review | RS | RS | RS | RS | RS | RS | RS — names movement time as a required model input | RS — names settling likewise | RS | RS | 0 | 0 |

‡ **The one cell that records two experiments.** [6]'s S10 must not be collapsed. In the dynamic-bending demonstration the geometry is changing — a QPSK video link is held at error vector magnitude around −20 dB while the surface is bent — and nothing is timed. In the second experiment an interval of 16.7 ms from trigger to stabilised radiation is recorded, and the geometry is static throughout. Writing "[6] times S10" without that condition would assert a post-morph stabilisation measurement that does not exist.

## S6.4 The counts that follow

| Count | Value | Reached by |
|---|---|---|
| Quantitatively evidenced stages (Axis A = Q) | **6** | [6], [7] |
| Measured stage durations (`·T`) | **4** | [7] alone |
| Stages carrying any duration information (`·T` + `·(T)`) | **6** | [6] alone |

The timed sets of the two best-covered platforms overlap at S1, S2, S4 and S5 and differ exactly at the boundary the review is about: [6] carries S6 and S10 and cannot command a shape, while [7] carries S7 and does not radiate. These counts are recomputed from the matrix above by `tools/c1_stage_counts.py` in the public reproducibility repository, so they cannot drift from the prose.


# Supplementary Table S7 — States a FIM-assisted ISAC system must track

Section 3.3 states that a FIM-assisted ISAC system tracks several states with different rates and different consequences for failure, and that the reviewed set fixes no relative rates among them. This table records each state with its governing driver, the control variable it binds, and the evidence available for it.

No column of this table contains an update deadline, and none is derivable from it; assigning one requires a performance tolerance the reviewed sources do not supply.

| State | What drives its variation | Which control variable it binds | Evidence in the reviewed set | Status of that evidence |
|---|---|---|---|---|
| **Instantaneous complex fading** | Doppler — ≈19.4 kHz at 28 GHz, 208 m/s | electronic phase state, and shape *if* shape is optimised per realisation | Doppler figure derived by us; 51-symbol >0.5-correlation window at 2.6 GHz | derived / simulated; no measurement, and no interval at 28 GHz |
| **Channel statistics and spatial correlation** | scattering environment, deliberately treated as slower than fading | shape, under statistical-CSI formulations | statistical-CSI FIM optimisation is published [12, 13]; the instantaneous-versus-statistical distinction is argued in [11, p. 20] | modelling choice, adopted by the literature; rate not measured |
| **Angles of arrival and departure; path geometry** | the user's traverse across the cell, not the fading | shape, beam direction | high-mobility models update angles explicitly and separately from fading correlation [19] | modelled; the *separation* is established, the *ratio* is not |
| **Target kinematics (sensing subproblem)** | target motion, independent of the communication user | sensing waveform and shape | communication and sensing may impose different movement and update requirements [11, pp. 24–25] | argued in a review; unquantified for FIM |
| **Blockage** | environmental, typically event-like rather than periodic | triggers reconfiguration rather than setting a rate | not quantified for any reviewed flexible aperture | absent |
| **Surface geometry** | deformation of the aperture itself — aeroelastic, mechanical, or commanded | the compensation layer; the actuator, if commanded | ≈4 ms strain-sensor read and 16.76 ms compensation loop on a flexible aperture [6]; 60 Hz stated deformation-rate limit | measured, on **externally imposed** deformation |
| **Calibration state** | how long the geometry-to-response mapping remains valid after a shape change | when the aperture may be trusted again | closed-loop refocusing demonstrated on a deformed active array [20] | capability demonstrated, duration not reported |

Read down the last two columns and the asymmetry is the one Section 5 develops: the fast-timescale demand is established by simulation and analysis, while the hardware capability is established by measurement on platforms that cannot do the thing being demanded. That is the reverse of how the comparison is usually presented.


# Supplementary Section S8 — Timing-value propagation: the instance inventory

Section 5.2 states the traceability finding and its bounds. This section gives the instance-by-instance inventory behind it, and the author-network resolution that bounds it.

## S8.1 What is audited, and what is not

The FIM system papers do not claim to have measured their own hardware assumptions, and it would be unreasonable to expect them to. What is audited is whether a timing value, once imported, still refers to the object the primary source measured. No claim of bad faith is made anywhere in this review; every verdict below is a statement about a value's scope, not about an author.

## S8.2 The instances

**Table S8 — Timing-value propagation among papers citing the primary hardware sources.** Rows P1–P5 are cases in which a primary timing value is reused with its scope changed; rows N1–N3 record the opposite pattern. "Author-disjoint" means sharing no author with the FIM system papers audited here **and** none with the three primary hardware sources.

| # | Citing work | Primary source cited | Value or phrase reproduced | What the primary source measured | Scope change | Verdict | Author-disjoint? |
|---|---|---|---|---|---|---|---|
| **P1** | [30], Table I "Morphing Period" | [8], [7] | 30 ms / 10 ms / 500 ms | [8]'s 30 ms is an **isolated ribbon**; its full surface is ≈300 ms. [7] reports no value at or near 10 ms anywhere in its complete package | element → surface | Ni: **unsupported substitution, confirmed**. Bai: **discrepancy requiring verification** (year also given as 2021) | No |
| **P2** | [30], text | [8], [7] | "the deformation response of FIMs operates on the order of milliseconds (with the fastest reaching **1 ms**)" | 1 ms appears in no primary source, and is faster than the minimum entry (10 ms) of this paper's own Table I | escalation beyond the citing paper's own table | **unsupported, and internally inconsistent** | No |
| **P3** | [31] | [6], [8], [7] | "shape-switching times on the order of milliseconds, which are comparable to or faster than the channel coherence time in typical mmWave scenarios" | [6] holds its geometry **static** throughout the interval it reports and commands no shape; [8]'s surface morph is ≈300 ms; [7]'s system morph is within 0.1 s | electronic loop presented as mechanical shape switching; adds an unsupported coherence comparison | **unsupported** | No |
| **P4** | [32], Remark 4 | [7] | "dynamic surface-shape morphing in just a few milliseconds" | element response < 0.07 s; system morphing within 0.1 s | element → surface | **unsupported**; **absent from the conference version** of the same work | No |
| **P5** | [1], Remark, pp. 13321–13322 | [7] | "within millisecond switching speeds" | as above | element → surface | **unsupported**; **absent from the preprint** | No |
| **N1** | [12] | [7] | **no timing value attached** | — | none — cited for the *existence* of shape-morphing hardware | **correct use** | **Yes — fully disjoint** |
| **N2** | [29] | — | **no timing value attached** | — | names response time as an unresolved practical limitation and declines to quantify it | **restrained use** | No |
| **N3** | [34] | [7] | **no timing value attached** | — | proposes a mechanically morphing metasurface lens for radio-frequency beam steering, cites [7] for the existence of shape-morphing hardware, and quantifies displacement and gain but no interval | **correct use** | **Yes — fully disjoint** |

## S8.3 The observation window and what it bounds

The window is 13 of 20 studies, and the finding is stated inside it. Among the thirteen candidate system studies whose full texts were read, five instances of scope change occur, in four studies. Seven further studies could not be read — publisher paywalls, no open deposit — and an abstract-level scan establishes nothing here, because propagation occurs only in body text: scanning all 65 stage-one abstracts for timing terminology returns no hits at all. An instance among the seven unread studies cannot be excluded, and neither can an author-disjoint one. Every count is a lower bound on a partially observed set, and no proportion, rate or prevalence is estimated from it.

Authorship is resolvable for the unread studies even where content is not, and it narrows the bound. Using published-record author lists alone, fourteen of the twenty studies share an author with the FIM system-paper lineage, four are disjoint from it, and two are disjoint from both it and all three primary hardware sources. Among the seven unread studies, five share a lineage author and one shares an author with [6]; exactly one is disjoint from both. If an author-disjoint group reproducing the practice exists in the unread set, it is that single study. Whether it attaches a timing value is unknown to us, and we make no claim either way.

Within that window, no author-disjoint publication group reproduces the practice. The four papers carrying the five instances form one connected co-authorship network: each shares at least one author with another member of the set and with the system papers audited here, and two names recur throughout. We state this as connectivity rather than as pairwise sharing, because connectivity is what we verified. Measured rather than assumed, the independence result is negative: four different first authors are not four independent groups when common senior authors run through them. What the search widened was the *case base*, from two papers to four, each instance with verbatim quotation, including two escalations the earlier framing did not capture. What it did not widen is the *independence basis*, which is zero within the observed window. This is therefore a documented finding about one collaboration network, bounded by full-text access, and no statement about prevalence, proportion or the field follows from it.

## S8.4 The opposite pattern

The thirteen studies read in full divide exactly in two: four propagate a timing value with its scope changed, and the remaining nine cite the same primary sources and attach no timing value at all. Those nine are listed by study-family identifier and citation in Supplementary Section S5, so the count is reconstructable from named rows rather than asserted. Two of the nine are fully author-disjoint. One optimises a FIM under statistical channel information and cites the mechanical hardware only for its existence [12]. The other proposes a mechanically morphing metasurface lens for radio-frequency beam steering, cites the filamentary platform directly, quantifies displacement and gain, and states no interval anywhere [34] — an author-disjoint group working on exactly the object this review is about, reaching for the same primary source, and declining to convert it into a timing claim. A third of the nine names response time explicitly as an unresolved practical limitation and declines to quantify it [29]; it is counted inside the no-timing-value set, because naming a quantity as unresolved is not attaching a value to it. Restraint exists in this literature, and it is not confined to authors outside the network.

## 10. A reporting framework for FIM adaptation

### 10.1 Definitions, not thresholds

The deficiencies documented in Sections 6 to 8 are principally failures of *definition* rather than of measurement quality. Several of the measured values in Table 5 are excellent measurements; what they lack is the context that would allow them to be compared with anything, or that would allow a downstream reader to detect a change of scope. A value reported without its object, its start event and its end event cannot be compared; once such a value enters a citation chain, an element-level figure can become a surface-level one with nothing on the page to signal it.

The framework below therefore prescribes **definitions rather than thresholds**. We do not propose that actuation should complete within any particular time, that settling should meet any particular criterion value, or that any performance target should be met. The evidence supports no numerical acceptance threshold, and inventing one would repeat precisely the error this review documents — a number with no measurement behind it entering circulation because it was useful.

Each field is motivated by a **recurring reporting deficiency or a specific unresolved quantity identified in the reviewed set**. Those are different things: some fields name quantities no reviewed source reports at all, while others name quantities that some sources report and others omit, which is what makes the reported ones incomparable. Fields that would merely be nice to have are omitted. Table 9 gives the set with its motivation field by field.

### 10.2 The minimum reporting set for hardware papers

**Table 9 — Minimum reporting set, with the deficiency motivating each field.** Groups A, B and C are mandatory for any paper reporting a deformable or reconfigurable aperture; D and E become mandatory if a control loop is claimed; F is mandatory for any mobility or ISAC claim.

| Group | Field | Motivating deficiency in the reviewed set |
|---|---|---|
| **A — architecture** | Architecture class: passive flexible / shape-aware programmable / self-morphing / rigid reconfigurable / flexible active | Seven physically distinct systems are grouped under overlapping names (Table 1) |
| | **Deformation source: externally imposed or self-actuated** | The distinction between compensating a shape and commanding one is this review's central taxonomic finding, and it is rarely stated explicitly |
| | Whether a radio-frequency layer is present, and what it consists of | Every measured mechanical timescale in the reviewed set was obtained on a platform with no RF layer |
| | Control granularity: independently addressable channels versus total elements | One reviewed aperture has 512 meta-atoms and 32 control channels; the difference is not usually foregrounded |
| **B — timing** *(all five required for every reported interval)* | **Object timed** — one element, one tile, or the whole aperture | The same panel reports element- and tile-level bounds up to two orders of magnitude apart, because the object differs |
| | **Start event**, named physically | "Response time" denotes at least five different intervals in the reviewed set |
| | **End event**, named physically, with its threshold | Threshold definitions are inconsistent where present and absent for most reported intervals. The two sources that state one state incommensurable ones: 10 %/90 % amplitude thresholds on a liquid-crystal device, and "the first video frame after which no displacement deviation is visible" on a 60 fps camera — an instrument-limited criterion with a ≈16.7 ms floor |
| | **Measured, simulated, projected or derived** | A projected sub-2 ms figure appears in the same discussion as measured 15 ms and 72 ms values |
| | Direction, where the process is asymmetric | Switch-on and switch-off differ by nearly a factor of five in the reviewed liquid-crystal device |
| **C — mechanics** *(any surface whose geometry changes)* | Actuation mechanism, drive quantity and drive level | Reported for the mechanical platforms; absent for every flexible radiating aperture |
| | Displacement range, in millimetres **and in wavelengths** | The system literature works in wavelengths and the hardware literature in millimetres; almost no source gives both |
| | **A stated and justified electromagnetic settling criterion** — an allowable phase or RF-performance error, or the corresponding displacement tolerance relative to wavelength, with the basis for the value chosen | No reviewed source defines settling electromagnetically; settling is reported, where reported at all, as the cessation of visible motion. This review prescribes no numerical fraction of a wavelength, and none should be inferred from the illustrative arithmetic in §9.2 |
| | Rise time and settling time, separately | Bundled into a single "response time" wherever they are reported |
| | Achieved shape accuracy against the *commanded* shape | Reported for shape *sensing* (RMSD 2.36 mm at 45 mm displacement) but never for shape *achievement* on a radiating aperture |
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

The system literature cannot be expected to measure hardware. It can be expected to declare what it assumes, and the reviewed papers largely do not.

1. **Which adaptation stages are assumed instantaneous.** In all four reviewed FIM system papers, control transport, actuation, settling and calibration are assumed away; none says so.
2. **The assumed update rate for each control variable, with its basis.** Where a two-rate schedule is used, the paper should state whether the rates are chosen for tractability or justified by hardware.
3. **The assumed validity duration of a computed shape, with its basis.** A claim that an optimised shape can be reused irrespective of delay, Doppler and waveform changes is a strong physical claim; it should carry a bound, a condition, or an explicit acknowledgement that it is an assumption.
4. **The provenance of any hardware figure imported into the paper** — what object it was measured on, and what its start and end events were.
5. **Whether the cited hardware has a radio-frequency layer.** The mechanical platforms cited as evidence of FIM feasibility do not.

Item 4 matters most and costs least. A table of imported hardware parameters carrying an "object measured" column and a "start/end events" column would have made Section 8 of this review unnecessary.

### 10.4 Standing and scope

We do not propose this as a standard, and we have no standing to. We propose it as the minimum set that would have allowed the questions in this review to be answered from the published record. Some of its fields could be reported from measurements already performed — the object and events of an interval that was timed anyway, or the interface and computation platform of a loop that was built anyway. Others require new measurements: settling against an electromagnetic criterion, post-deformation calibration duration, actuation energy, and repetition counts for intervals reported once. We do not claim to know the proportion, because that would require knowing what each group recorded and did not publish.

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

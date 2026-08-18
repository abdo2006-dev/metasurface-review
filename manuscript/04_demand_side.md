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

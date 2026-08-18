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

Table 3 records, for every reviewed source, whether each stage is demonstrated, measured, simulated, assumed, absent or not applicable. Four features of it are worth drawing out, and none is visible without the decomposition.

**Table 3 — Adaptation-chain coverage.** **M** measured (a number with defined start and end events) · **D** demonstrated (shown working, no number) · **S** simulated · **A** assumed · **✗** absent · **n/a** not applicable to the architecture · **RS** review statement.

| Source | Arch. | S1 sense | S2 geom. est. | S3 chan. est. | S4 optim. | S5 ctrl tx | S6 electronic | S7 morphing | S8 settling | S9 calib. | S10 stable RF |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ranasinghe *et al.* [1]** | A1 | ✗ | ✗ | A | S | ✗ | ✗ | A (instant) | ✗ | ✗ | A — unbounded shape reuse |
| **An *et al.* [2]** | A1 | ✗ | ✗ | A (perfect CSI) | S | ✗ | ✗ | A (instant) | ✗ | ✗ | A (quasi-static) |
| **Yang *et al.* [3]** | A1 | ✗ | ✗ | S | S + **M** (runtime) | ✗ | A (per slot) | A (per subframe) | ✗ | ✗ | A |
| **Morales Sandoval *et al.* [15]** | A1 | ✗ | ✗ | A | S | ✗ | ✗ | A | ✗ | ✗ | A |
| **Xu *et al.* [19]** | A5 | S (pilots) | n/a | S | S | ✗ | A | n/a | n/a | ✗ | S |
| **Li *et al.* [6]** | A3 | **M** ≈4 ms | **M** RMSD 2.36 mm | ✗ **absent** | **M** ≈2 ms | **M** RS-232 | **M** 5.25 ms supply | ✗ **external** | ✗ | D (folded into a learned map) | **D** + **M**‡ |
| **Lu *et al.* [18]** | A3 | ✗ | ✗ (a priori) | ✗ | S | ? | D | ✗ (static) | ✗ | D per curvature | **M** patterns |
| **Neuder *et al.* [5]** | A5 | ✗ | n/a | ✗ | ✗ | ✗ | **M** 15 / 72 ms | n/a | n/a | ✗ | **M** patterns |
| **Akram *et al.* [4]** | A5 | ✗ | n/a | ✗ | ✗ | **M** + ×¼ multiplexing | **M** <0.1 ms / <10 ms | n/a | n/a | ✗ | **M** patterns, power |
| **Bai *et al.* [7]** | A4 | **M** stereo imaging | **M** | n/a | **M** search | D | n/a | **M** <0.07 s / <0.1 s | ? (bundled) | ✗ | ✗ **no RF layer** |
| **Ni *et al.* [8]** | A4 | ✗ | ✗ | n/a | ✗ (scripted) | **M** ≈50 ms script | n/a | **M** 30 / 300 ms | **M** ≈250 ms | ✗ | ✗ **no RF layer** |
| **Gal-Katziri *et al.* [20]** | A7 | D self-sensing | D | ✗ | D | D | D | ✗ external | ✗ | **D — no duration** | **M** ≈80 mW at 1 m |
| **Ma *et al.* [11]** | A6 review | RS | RS | RS | RS | RS | RS | RS — names movement time as a required model input | RS — names settling likewise | RS | RS |

‡ **The one cell that records two experiments.** [6]'s S10 must not be collapsed. In *demonstrated* mode the geometry is changing — a QPSK video link is held at error vector magnitude around −20 dB while the surface is bent — and nothing is timed. In *measured* mode an interval of 16.7 ms from trigger to stabilised radiation is recorded, and the geometry is **static** throughout. Writing "[6] measures S10" without that condition would assert a post-morph stabilisation measurement that does not exist.

### 5.3 No source measures more than five stages, and the set is never closed

The largest set of linked stages measured on any one platform belongs to the flexible microwave metasurface: S1 sensing, S2 geometry estimation, S4 inference, S5 control transmission and S6 electronic update, all measured, all falling inside a single reported interval of 16.76 ms [6].

That set is **linked rather than contiguous**, and the distinction is not pedantry. S3, channel estimation, lies between S2 and S4 in the chain and is absent from this platform entirely — it has no channel estimator, because it is not trying to track a channel. A run that skips a stage the architecture never implements does not span the chain; it spans the part of the chain the architecture possesses. The correct statement is one of extent — **five of ten stages, covering S1–S2 and S4–S6, with S3 absent** — and the hole at S3 is one of this review's findings rather than an accounting artefact.

Where the set ends matters as much as how large it is. S7 is external: the deformation is applied by a mechanical fixture with manually adjusted fulcrums, not commanded by the system. S8 is not timed. S9 does not exist as a runtime step, having been folded into a pre-trained map. And S10, as the note to Table 3 records, is measured only with the geometry held still.

Every other source records less. The rigid electronically reconfigurable surfaces record S5, S6 and S10 with numbers and nothing else [4, 5]. The mechanical platforms record S1, S2, S4, S7 and — in one case — S8, with no S3, S6, S9 or S10, because they have no radio [7, 8]. The flexible active array records S1, S2, S4, S5, S6, S9 and S10 as demonstrated operations and attaches a duration to none of them [20]. The FIM system papers record S3 and S4 in simulation and treat S5 through S9 as absent or instantaneous.

So: **no reviewed source measures more than five of the ten stages, and no source measures S3 together with S7** — none couples channel estimation to a commanded shape change. One source does time a complete run for a *fixed-geometry electronic compensation* chain, which is a different chain from the one a FIM requires. The second fact does not supply the first, and the distance between them is the subject of Section 9.

### 5.4 The measured stages sit on incompatible platforms

This is the observation that motivates the review, and stating it needs Table 1 and Table 3 together:

- the only **measured mechanical morphing and settling** (S7, S8) come from A4 platforms with no radio-frequency layer;
- the only **measured electronic state transitions** (S6) come from A5 rigid panels;
- the only **measured sensing, inference and control transport on a flexible radiating surface** (S1, S2, S4, S5) come from an A3 platform where geometry is a disturbance rather than a control variable;
- the only **demonstrated post-deformation calibration on a deformable radiating aperture** (S9) comes from an A7 active transmitter, and carries no duration.

One might be tempted to assemble a total by taking each stage from wherever it was measured: 16.76 ms of electronic loop from A3, plus 300 ms of surface morphing from A4, plus unmeasured settling and calibration terms. We do not do this, and no one should. The sum would concatenate measurements taken on four different physical objects, one of which has no meta-atoms, another of which cannot bend, and none of which has both a controlled geometry and a measured radiation pattern. It would have the form of an engineering estimate and the content of a category error.

What the decomposition licenses instead is weaker and far more defensible: **no reviewed source measures the adaptation chain end to end on any single object, and the reason is architectural rather than incidental.** Figure 2 shows the pattern directly — each platform illuminates a different band of the chain, and the bands do not overlap where they would need to.

> **Figure 2.** *Adaptation-chain coverage by architecture class.* Rows are platform classes rather than individual papers; cells record the strongest evidence any platform in that class provides for that stage. The four stages on the right — mechanical morphing, settling, calibration and stabilised radiation after a shape change — carry measurements only on platforms with no radio-frequency layer, or carry demonstrations with no duration. *(File: `figures/fig2_adaptation_chain.pdf`.)*

### 5.5 The system papers do not model stages S5 to S9

Across the four reviewed FIM system papers — three distinct studies, since one is a short version of another — control transmission, electronic update, mechanical morphing, settling and calibration are absent from the model or assumed instantaneous. Geometry takes the value the optimiser assigns it, at the moment the optimiser assigns it.

Where the omission is defended at all, it is defended by a single sentence. Having noted that the optimisation could be executed for each distinct channel realisation, the high-mobility FIM–ISAC study states in a footnote that in practice, once the surface shapes have been computed for one realisation, "the optimized surface shapes can be used irrespective to changes in delays, Doppler shifts and waveform" [1, footnote 10, p. 13327].

We take the claim seriously, because if it holds the mechanical timescale largely stops mattering and the architecture becomes much easier to defend. As stated, however, it carries no validity duration, no channel-statistics condition, no degradation bound, no sensitivity study and no experiment; it is not derived in the paper, and it is not tested by the paper's own simulations, which optimise per realisation. It is an assertion in a footnote carrying the weight of the architecture's physical feasibility, and Section 8 examines what happens when that weight is transferred through a citation chain.

### 5.6 Where a loop is closed, perception is what binds

One reviewed source closes a loop on shape — sensing, estimation, optimisation, actuation, and back to sensing [7] — and its cycle budget is instructive in a way nothing else in the corpus is.

Each feedback control cycle takes around 0.25 s, which the paper attributes "mainly to the time overhead from the image processing algorithm", noting that the cycle is "ultimately limited by the mechanical response time (which is less than 0.1 s)" [7, p. 4]. The supplementary information gives the per-cycle budget more precisely as 0.35 ± 0.15 s and, critically, distinguishes a *cycle* from an *iteration*: each optimiser iteration requires 4(N + M) + 2 function evaluations, so the "5 to 15 iterations" quoted in the main text is 170 to 510 cycles. Convergence is stated directly as an average of approximately **2.5 minutes** for a 4 × 4 sample from the zero-actuation state [7, Supplementary Note S6].

Two things follow. First, in the only demonstrated shape-control loop in this literature, **actuation is not the bottleneck**; sensing, perception and search are. We state that as a property of this platform rather than as a law: whether a radiating FIM would also be perception-limited depends on its sensing modality, its verification criterion and its compute load, all of which would differ and none of which has been measured. The transferable part is a design warning — a closed-loop FIM's rate may be set by perception rather than by actuation, which is a reason to instrument the sensing path early — together with the purely negative observation that no system model represents this stage at all, so none would detect the problem if it occurred. Second, the gap between the element response time cited as evidence of feasibility (below 0.07 s) and the demonstrated closed-loop convergence (≈150 s) is a factor of roughly two thousand, and the reviewed system literature quotes neither.

The two figures are not competing measurements of one thing, and this review does not treat the slower one as the "true" cost. Open-loop replay of a known shape and closed-loop discovery of an unknown one are different operations with different completion criteria; the same platform replays stored voltage sequences at 10 fps once the voltages are known. Which is relevant to a FIM depends on whether the required geometry can be precomputed — a question the system literature does not pose. That is exactly the point: the informal phrase "morphing time" does not select between them.

### 5.7 Two quantities that nothing in the reviewed set reports

The decomposition isolates two absences precisely, and the precision is what makes them actionable.

**Mechanical settling of a radiating aperture.** One source measures settling with a named mechanism: approximately 250 ms of viscoelastic membrane relaxation dominating the approximately 300 ms a soft surface needs to develop a full shape from flat [8, p. 4]. That is a bare elastomer membrane. No reviewed source reports settling for a surface carrying meta-atom metallisation, a dielectric substrate, a bias network and a ground plane — the components a working reflective aperture necessarily has, and which the one flexible radiating surface in the reviewed set had to redesign specifically to permit bending at all.

**Calibration duration and the onset of trustworthy radiation after a shape change.** The flexible active array performs closed-loop refocusing using self-sensing receivers against a remote receiver, and reports no time [20]. The flexible microwave metasurface folds the operation into a pre-trained static map, so no explicit calibration step exists in its architecture; its supplementary information does measure a 16.7 ms interval ending at stabilised radiation, but that interval is triggered by a sensor press on a statically held surface and contains no shape change [6, Supplementary Note 6]. The quantity that remains unmeasured is therefore specific: **the interval from a commanded deformation to trustworthy radiation.** It is the stabilisation *end event* that has been shown to be measurable, not the interval the FIM architecture needs.

These two absences, together with the absence of any commanded-actuation measurement on a radiating aperture, are the substance of the validation gap in Section 9 and the origin of the reporting framework in Section 10.

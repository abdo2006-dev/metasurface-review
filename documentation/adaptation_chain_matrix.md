# Adaptation-Chain Matrix

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026
**Purpose:** to decompose "FIM adaptation" into ten distinct stages and record, per source, whether each stage is demonstrated, measured, simulated, assumed, absent, or unclear. This is the instrument that prevents any one stage from being reported as the latency of the whole system.

---

## 1. The ten stages

| # | Stage | Definition used throughout this project |
|---|---|---|
| S1 | **Sensing / acquisition** | physical observation of the surface or the environment (strain sensors, imaging, pilots received) |
| S2 | **Geometry estimation** | conversion of raw sensor data into a surface-shape estimate |
| S3 | **Channel estimation** | acquisition of the wireless channel (instantaneous or statistical) |
| S4 | **Optimisation / inference** | computation of the desired geometry and/or phase configuration |
| S5 | **Control transmission** | transport of the resulting command from the compute element to the surface controller |
| S6 | **Electronic state update** | meta-atom EM state change (varactor, PIN, LC) |
| S7 | **Mechanical morphing** | the commanded physical displacement itself |
| S8 | **Mechanical settling** | decay of transient motion to within a tolerance of the target shape |
| S9 | **Calibration** | re-establishment of the geometry→RF-response mapping after the shape changed |
| S10 | **Stabilised RF operation** | the interval over which the configured surface actually delivers its intended RF behaviour |

Codes: **D** demonstrated (shown working, no number) · **M** measured (a number with defined start/end) · **S** simulated · **A** assumed · **✗** absent · **?** unclear.

**A cell may carry more than one code.** Where it does, the codes describe *different experiments under different conditions* and must not be merged. The marker **‡** flags such a cell and points to the condition note below the matrix; the only one at present is LI-25's S10, added 17 August 2026 after the supplementary retrieval.

---

## 2. The matrix

| Source | Arch. | S1 sensing | S2 geometry est. | S3 channel est. | S4 optimisation | S5 control tx | S6 electronic | S7 morphing | S8 settling | S9 calibration | S10 stable RF |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **RAN-25** | A1 | ✗ | ✗ (shape is a free variable) | **A** (parameters available) | **S** E-01/E-05 | ✗ | ✗ | **A** (instant) | ✗ | ✗ | **A** — E-03 asserts unbounded reuse |
| **ANJ-25** | A1 | ✗ | ✗ | **A** perfect CSI, E-09 | **S** E-10 | ✗ | ✗ | **A** (instant) | ✗ | ✗ | **A** quasi-static |
| **YAN-25** | A1 | ✗ | ✗ | **S** protocol + CMFV-SBL, E-12 | **S + M(runtime)** T-YA-01 | ✗ | **A** per time slot, T-CH-05 | **A** per subframe, T-CH-05 | ✗ | ✗ | **A** |
| **MOR-26** | A1 | ✗ | ✗ | **A** | **S** | ✗ | ✗ | **A** | ✗ | ✗ | **A** |
| **XU-22** | A5 | **S** pilots | n/a (rigid) | **S** MMSE interpolation, E-15/E-16 | **S** | ✗ | **A** | n/a | n/a | ✗ | **S** |
| **LI-25** | A3 | **M** 32 strain sensors, T-LI-01 | **M** RMSD 2.36 mm, E-24 | ✗ **absent** | **M** ANN, T-LI-02 | **M** RS-232, inside T-LI-04 | **M** supply 5.25 ms, T-LI-03; varactor qualitative, T-LI-05 | ✗ **external, not commanded** | ✗ | **D** (ANN is the learned geometry→bias map; no separate timed recalibration) | **D + M‡** — **D:** EVM ≈ −20 dB under *dynamic bending*, untimed, E-25. **M‡:** 16.7 ms trigger → stabilised RF, **static geometry**, T-LI-06 |
| **LU-26** | A3 | ✗ | ✗ (bending known a priori) | ✗ | **S** compensation phase | ? | **D** PIN states | ✗ static bending | ✗ | **D** per-curvature compensation | **M** patterns at each fixed curvature, E-53 |
| **NEU-24** | A5 | ✗ | n/a | ✗ | ✗ | ✗ | **M** τ_on/τ_off, T-NE-01/02 | n/a | n/a | ✗ | **M** patterns |
| **AKR-26** | A5 | ✗ | n/a | ✗ | ✗ | **M** interfaces + ×¼ multiplexing, T-AK-03 | **M** T-AK-01, T-AK-02 | n/a | n/a | ✗ | **M** patterns, power |
| **BAI-22** | A4 | **M** stereo imaging, T-BA-03 | **M** (shape extracted from images) | ✗ n/a | **M** 5–15 iterations, T-BA-03 | **D** digital actuation scheme | ✗ n/a | **M** T-BA-01/02 | ? (bundled into "response time") | ✗ | ✗ **no RF layer** |
| **NI-22** | A4 | ✗ (imaging used for characterisation only) | ✗ | ✗ n/a | ✗ (scripted) | **M** ≈50 ms script processing, inside T-NI-03 | ✗ n/a | **M** T-NI-01/02 | **M** — the ≈250 ms viscoelastic term *is* settling, T-NI-02 | ✗ | ✗ **no RF layer** |
| **GAL-22** | A7 | **D** self-sensing receivers | **D** shape estimation mentioned | ✗ | **D** search algorithm | **D** | **D** per-element phase | ✗ external | ✗ | **D** closed-loop focusing, E-38 — **but T-GAP-01: no time reported** | **M** ≈80 mW at 1 m, E-39 |
| **MA-26** | A6 review | RS | RS | RS | RS | RS | RS | RS — identifies movement time as a required model input, E-43 | RS — identifies settling as a required model input | RS | RS |

**‡ Condition note — LI-25, S10 (added 17 August 2026).** This one cell records two experiments that must never be collapsed into a single claim:

| Mode | Condition | What it establishes | ID |
|---|---|---|---|
| **Demonstrated** | *dynamic bending*, geometry changing, no timing | that electronic compensation holds a link while the surface is deformed | E-25 |
| **Measured timing** | *static geometry*, sensor-press trigger, no morphing inside the interval | that stabilised RF is a well-defined, instrumentable end event, reached 16.7 ms after the trigger | T-LI-06 |

The measured mode is **not** an S10 timing following deformation, and this matrix does not record one. The only experiment on this platform that contains a shape change is the demonstrated mode, and it is untimed; the only one that carries a number holds the shape fixed. Writing "LI-25 measures S10" without the static-geometry condition would assert an S10-after-morph measurement that does not exist.

---

## 3. What the matrix shows

### 3.1 No row is complete
Not one source in the corpus records all ten stages, and only **LI-25** records more than four with numbers attached.

**Corrected 17 August 2026 — the word "contiguous" was used incorrectly here.** This section previously described LI-25's **S1 → S2 → S4 → S5 → S6** as "the longest measured contiguous run". Under this project's own S1–S10 taxonomy that sequence is **not contiguous**: S3, channel estimation, lies inside its span and is absent from LI-25 altogether. The correct statement is one of extent, not of contiguity:

> **LI-25 measures the largest set of linked stages on one flexible RF platform, covering S1–S2 and S4–S6, while S3 channel estimation is absent.** Those five stages are linked in the sense that one measured interval, T-LI-04 (16.76 ms), runs from the start of S1 to the end of S6; they are not contiguous in the stage taxonomy, because the platform never estimates a channel.

The gap at S3 is not a bookkeeping detail. It is the same architectural fact recorded in `manuscript/07_validation_gap.md` §7.3: LI-25's loop closes on **geometry**, not on a channel, and a stage the platform does not implement cannot be counted as spanned.

LI-25's chain then **stops** at S6 for the morphing chain: S7 is external and not commanded, S8 and S9 are not timed. S10 is treated separately in §3.4 below, because the supplementary retrieval changed its status.

**Consequence for the manuscript.** No section may claim "five contiguous stages" or a "longest contiguous chain". The defensible forms are *"the largest linked set of stages measured on one platform"* and *"no source measures more than five of the ten stages, and none of them measures S3 together with S7."*

### 3.2 The stages are split across incompatible architectures
- The only **measured S7/S8** (mechanical morphing and settling) come from **A4** platforms with no RF layer.
- The only **measured S6** (electronic state) come from **A5** rigid panels.
- The only **measured S1/S2/S4/S5** on a flexible RF surface come from **A3** with geometry as a *disturbance*.
- The only **demonstrated S9** on a deformable RF aperture (GAL-22) reports no duration.

Concatenating these to produce a total is not a synthesis; it is a category error across four architectures. The manuscript states this explicitly and does not perform the concatenation.

### 3.3 The A1 literature does not model stages S5–S9 at all
Across RAN-25, ANJ-25, YAN-25 and MOR-26, stages S5 (control transmission), S6 (electronic update, except as a protocol slot), S7 (morphing), S8 (settling) and S9 (calibration) are either **absent** or **assumed instantaneous**. The single strongest defence offered for this omission is E-03/T-ASM-01: the claim that a computed shape remains usable indefinitely. That claim is asserted in a footnote with no supporting analysis.

### 3.4 Two stages are unreported by *every* source in the corpus
- **S8 for an RF aperture** — mechanical settling of a surface carrying meta-atoms, bias lines and a ground plane. NI-22 measures settling for a bare elastomer membrane; nothing measures it for an RF stack.
- **S9 timing** — how long the geometry→RF mapping takes to re-establish after a shape change. GAL-22 demonstrates the operation without timing it; LI-25 folds it into a learned static map; nothing measures it.

**S10 onset requires a distinction that this section previously failed to make.** It was formerly listed here as unreported by every source. **That is now false**, and the two cases must be kept apart:

1. **RF stabilisation under electronic compensation with static geometry — MEASURED.** LI-25's supplementary information reports 16.7 ms from a finger-triggered sensor to stabilised RF output, on a dual-channel oscilloscope through an AD8317 logarithmic detector at 3.1 GHz (`T-LI-06`). The end event is well defined and instrumentable with ordinary laboratory equipment.
2. **RF stabilisation following a commanded mechanical morph — NOT FOUND in the reviewed set.** No interval anywhere in the corpus begins with a commanded deformation and ends at trustworthy radiation. The 16.7 ms measurement cannot stand in for it: the surface is held static throughout and no shape change occurs inside the interval.

Only case 2 remains a gap. `T-GAP-03` was narrowed accordingly and must never be stated as "RF stabilisation is unreported".

These are recorded as `T-GAP-01`, `T-GAP-02` and the narrowed `T-GAP-03`, and drive the reporting framework in `manuscript/08_reporting_framework.md`.

### 3.5 Where a closed loop does exist, it is slow for a structural reason
BAI-22 is the only closed geometry loop in the corpus (S1 → S2 → S4 → S7 → back to S1). Its cycle time is ≈0.25 s in the main text and 0.35 ± 0.15 s in the supplementary budget, and it is dominated **not** by mechanics (< 0.1 s) but by **S1/S2 — stereo image capture and processing** (T-BA-03).

**Narrowed 17 August 2026 — this paragraph previously over-transferred.** It formerly read: *"This is a general and transferable observation … Any FIM architecture that needs closed-loop geometry verification inherits this problem."* One platform cannot establish that. The supportable statement is:

> **In BAI-22's demonstrated closed geometry loop, sensing, image processing and the optimiser's search contribute substantially to total loop time and exceed the bare actuator response.** Whether the same holds in an RF FIM — where the sensing modality, the verification criterion and the compute load would all differ — must be **measured rather than assumed**.

Read as a **design warning**, not a transferred result: a closed-loop FIM's rate may well be set by perception rather than by actuation, which is a reason to instrument the sensing path early. It is not evidence that any particular FIM architecture will be perception-limited, and this matrix asserts no such thing. What does hold generally is the weaker and purely negative point: **no A1 paper models this stage at all**, so none of them would detect the problem if it did occur.

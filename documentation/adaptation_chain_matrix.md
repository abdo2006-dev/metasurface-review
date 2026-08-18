# Adaptation-Chain Matrix

> ⚠ **Section numbers in this file are v0.14 numbering except where a v0.20/v0.21 section is named explicitly.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations).

**Version:** 2.0 · 18 August 2026 (**two-axis recoding** — see `CHANGELOG.md` v1.8, CH-100)
**Purpose:** to decompose "FIM adaptation" into ten distinct stages and record, per source, (A) what the source establishes about each stage and (B) whether the *duration* of that stage was measured. This is the instrument that prevents any one stage from being reported as the latency of the whole system.

---

## 0. Why this file was recoded — read first

**Version 1.0 used a single code set in which `M` meant "measured (a number with defined start/end events)".** In practice `M` was also applied to cells recording quantitative radio-frequency measurements that contain no duration at all — LU-26's radiation patterns at fixed curvature, NEU-24's patterns, AKR-26's patterns and power, GAL-22's ≈80 mW delivered at 1 m. Those are genuine measurements; none of them is a timing.

The consequence was a real ambiguity in a load-bearing count. The claim *"no source measures more than five of the ten stages"* is **true under a timing reading and false under a quantitative reading** — under the latter the maximum is six. A reader could not tell which was meant, and the legend said one thing while several cells did the other.

**The fix is structural, not cosmetic: the two concepts are now separate axes.**

| Axis | Question it answers | Codes |
|---|---|---|
| **A — stage evidence status** | *What did this source establish about this stage?* | **Q** quantitatively measured (a physical or RF quantity reported) · **D** demonstrated (shown working, no quantity) · **S** simulated · **A** assumed · **✗** absent · **n/a** not applicable to the architecture · **?** unclear · **RS** review statement |
| **B — timing status** | *Was the duration of this stage measured?* | **T** timed — a duration with identifiable start and end events · **(T)** partially timed — a duration is reported but its start event, end event, or its separation from an adjacent stage is not fully resolved · *no marker* — untimed |

A cell carries an axis-A code, optionally followed by an axis-B marker: `Q·T`, `Q·(T)`, `Q`, `D`, `S·T`, `A`, `✗`.

The two axes are genuinely orthogonal, and one cell proves it: **YAN-25's S3 is `S·T`** — the channel-estimation stage is *simulated*, and the *wall-clock runtime of the simulation* is measured on a named desktop CPU. A simulated stage can have a timed implementation; a measured RF output can have no timing at all.

⚠ **One placement was corrected during the recoding.** v1.0 recorded YAN-25's measured running time under **S4** (optimisation). The timed algorithm is **CMFV-SBL**, which estimates the channel, so the runtime belongs to **S3**. Corrected here and in manuscript Table 3. It does not change any count, because YAN-25 times exactly one stage either way.

**A cell may carry more than one experiment.** Where it does, the experiments ran under *different conditions* and must not be merged. The marker **‡** flags such a cell and points to the condition note below the matrix; the only one at present is LI-25's S10.

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

---

## 2. The matrix

| Source | Arch. | S1 sensing | S2 geometry est. | S3 channel est. | S4 optimisation | S5 control tx | S6 electronic | S7 morphing | S8 settling | S9 calibration | S10 stable RF | Stages **timed** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **RAN-25** | A1 | ✗ | ✗ (shape is a free variable) | **A** (parameters available) | **S** E-01/E-05 | ✗ | ✗ | **A** (instant) | ✗ | ✗ | **A** — E-03 asserts unbounded reuse | **0** |
| **ANJ-25** | A1 | ✗ | ✗ | **A** perfect CSI, E-09 | **S** E-10 | ✗ | ✗ | **A** (instant) | ✗ | ✗ | **A** quasi-static | **0** |
| **YAN-25** | A1 | ✗ | ✗ | **S·T** CMFV-SBL runtime, T-YA-01 | **S** protocol + iteration counts, E-12 | ✗ | **A** per time slot, T-CH-05 | **A** per subframe, T-CH-05 | ✗ | ✗ | **A** | **1** |
| **MOR-26** | A1 | ✗ | ✗ | **A** | **S** | ✗ | ✗ | **A** | ✗ | ✗ | **A** | **0** |
| **XU-22** | A5 | **S** pilots | n/a (rigid) | **S** MMSE interpolation, E-15/E-16 | **S** | ✗ | **A** | n/a | n/a | ✗ | **S** | **0** |
| **LI-25** | A3 | **Q·T** ≈2 ms reception, T-LI-01 | **Q·(T)** RMSD 2.36 mm is an *accuracy*; its ≈2 ms share of T1 is not resolved from S1, E-24 | ✗ **absent** | **Q·T** ANN ≈2 ms, T-LI-02 | **Q·(T)** ≈5.5 ms RS-232, a **residual** of T-LI-04, not independently timed | **Q·T** supply 5.25 ms (oscilloscope), T-LI-03; varactor qualitative, T-LI-05 | ✗ **external, not commanded** | ✗ | **D** ANN is the learned geometry→bias map; no separate timed recalibration | **Q·T‡** — see note | **5** |
| **LU-26** | A3 | ✗ | ✗ (bending known a priori) | ✗ | **S** compensation phase | ? | **D** PIN states | ✗ static bending | ✗ | **D** per-curvature compensation | **Q** patterns, 16.13 dBi, ±45° at each fixed curvature — **untimed**, E-53 | **0** |
| **NEU-24** | A5 | ✗ | n/a | ✗ | ✗ | ✗ | **Q·T** τ_on ≈15 ms / τ_off 72 ms, 10 %/90 % thresholds, T-NE-01/02 | n/a | n/a | ✗ | **Q** patterns, −50°…+50°, IL — **untimed** | **1** |
| **AKR-26** | A5 | ✗ | n/a | ✗ | ✗ | **Q·(T)** ×¼ multiplexing is a **rate factor**, no absolute interval, T-AK-03 | **Q·T** <0.1 ms/element, <10 ms/tile — **upper bounds**, T-AK-01/02 | n/a | n/a | ✗ | **Q** patterns, 20.2 dBi, 8.25–13 W — **untimed** | **1** |
| **BAI-22** | A4 | **Q·T** stereo imaging 0.08 s, T-BA-03 | **Q·T** template matching 0.11 s + reprojection ≈0 | ✗ n/a | **Q·T** optimisation ≈0 per evaluation; ≈2.5 min convergence, T-BA-05 | **Q·T** voltage update 0.06 s | ✗ n/a | **Q·T** element <0.07 s, system within 0.1 s, T-BA-01/02 | **Q·(T)** the 0.1 s in the cycle budget is a **deliberate settling pause**, a chosen wait, not a measured settling time | ✗ | ✗ **no RF layer** | **5** |
| **NI-22** | A4 | ✗ (imaging for characterisation only) | ✗ | ✗ n/a | ✗ (scripted) | **Q·T** ≈50 ms script processing, T-NI-03 | ✗ n/a | **Q·T** 30 ms ribbon / 300 ms surface, T-NI-01/02 | **Q·T** ≈250 ms viscoelastic term *is* settling, T-NI-02 | ✗ | ✗ **no RF layer** | **3** |
| **GAL-22** | A7 | **D** self-sensing receivers | **D** shape estimation mentioned | ✗ | **D** search algorithm | **D** | **D** per-element phase | ✗ external | ✗ | **D** closed-loop focusing, E-38 — **T-GAP-01: no time reported** | **Q** ≈80 mW DC at 1 m — **untimed**, E-39 | **0** |
| **MA-26** | A6 review | RS | RS | RS | RS | RS | RS | RS — identifies movement time as a required model input, E-43 | RS — identifies settling as a required model input | RS | RS | **0** |

**‡ Condition note — LI-25, S10.** This one cell records two experiments that must never be collapsed into a single claim:

| Mode | Axis A | Axis B | Condition | What it establishes | ID |
|---|---|---|---|---|---|
| Dynamic-bending link | **Q** — EVM ≈ −20 dB | untimed | *geometry changing* | that electronic compensation holds a link while the surface is deformed | E-25 |
| Trigger → stabilised RF | **Q** — 16.7 ms | **T** | *geometry static*, sensor-press trigger, no morphing inside the interval | that stabilised RF is a well-defined, instrumentable end event | T-LI-06 |

The timed mode is **not** an S10 timing following deformation, and this matrix does not record one. The only experiment on this platform containing a shape change is untimed; the only one carrying a duration holds the shape fixed.

---

## 3. What the matrix shows

### 3.1 Three counts, which differ — and only one platform reaches five under the strict one

The three counts below are produced by `tools/c1_stage_counts.py`, which parses §2 of this
file. They are **not** interchangeable, and an earlier version of this section presented a
figure that follows from none of them: it credited LI-25 with "five stages it times" by
counting its two `·(T)` cells as timed while dropping its `·T` at S10, and credited BAI-22
with five by counting only its `·T` cells while dropping its `·(T)` at S8 — opposite rules
on the two sides, producing a false symmetry.

| Count | Maximum | Reached by |
|---|---|---|
| **Q** — quantitatively evidenced stages (axis A) | **6** | BAI-22 **and** LI-25 |
| **·T** — fully delimited stages (axis B) | **5** | **BAI-22 alone** |
| **·T + ·(T)** — stages carrying any timing information | **6** | BAI-22 **and** LI-25 |

Per platform, exactly:

| Platform | Arch. | `·T` fully delimited | `·(T)` partially delimited | `·T`+`·(T)` | What it cannot do |
|---|---|---|---|---|---|
| **BAI-22** | A4 | **5** — S1, S2, S4, S5, S7, inside a 0.35 ± 0.15 s function-evaluation cycle | 1 — S8, a **chosen** settling pause, not an observed settling time | **6** | **has no radio-frequency layer** (S6, S9, S10 do not exist on it) |
| **LI-25** | A3 | **4** — S1, S4, S6, and S10 in a separate static-geometry experiment | 2 — S2 (an RMSD is an *accuracy*, and its share of the 16.76 ms total is not resolved from S1) and S5 (a **residual** of that total, not independently timed) | **6** | **does not command its geometry** (S7 is an external fixture) |

**Only BAI-22 fully delimits five stages, and it does not radiate.** Under the strict reading
LI-25 reaches four, not five. The 16.76 ms interval it reports is real and is reported; what
it does not do is delimit each stage inside it.

**The disjointness survives the correction and is sharper than before.** Under the
like-for-like reading — any timing information — the two tie at six. Their sets share S1, S2,
S4 and S5, and differ exactly at **S6 and S10 against S7 and S8**: LI-25 carries the
radio-frequency stages and cannot command a shape; BAI-22 carries the mechanical stages and
has no radio. Neither can be extended into the other by measurement alone.

**Both sets are linked rather than contiguous**, and the wording matters. S3 lies between S2
and S4 in the chain and is absent from both platforms entirely: neither has a channel
estimator, because neither is trying to track a channel. A run that skips a stage the
architecture never implements spans the part of the chain the architecture possesses, not
the chain.

⚠ **Wording constraints (binding).** No section may claim "five contiguous stages" or a
"longest contiguous chain". No section may say "five, reached by two platforms" — that
figure follows from no consistent rule. No section may write "measures" for a timing count.
Acceptable: *"no source **fully delimits** more than five of the ten stages, and only one
reaches five"*; *"no source associates timing with more than six"*; *"no source times S3
together with S7"*.

### 3.2 The quantitative count is six for both platforms — which is why the axes were split

Counting axis-A `Q` cells rather than axis-B markers gives LI-25 six (S1, S2, S4, S5, S6, S10)
and BAI-22 six (S1, S2, S4, S5, S7, S8). **Every count in the manuscript must name the axis it
is counting.** Any sentence of the form "no source measures more than five stages" is
forbidden, and so is any sentence that reports a single stage count without saying which of
the three it is.

### 3.3 Stabilised RF is quantitatively measured on five platforms and timed on one

This is the correction that the recoding surfaces, and it is a stronger statement than v1.0 could make.

| Platform | S10 axis A | S10 axis B |
|---|---|---|
| LI-25 | **Q** EVM ≈ −20 dB under bending; 16.7 ms interval | **T** — but *geometry static* ‡ |
| LU-26 | **Q** patterns, gain, scan range at fixed curvatures | untimed |
| NEU-24 | **Q** patterns, insertion loss, scan range | untimed |
| AKR-26 | **Q** patterns, gain, control power | untimed |
| GAL-22 | **Q** ≈80 mW delivered at 1 m | untimed |

Five reviewed platforms establish quantitatively that a configured surface delivers its intended RF behaviour. **One of them attaches a duration, and that one holds its geometry still.** The gap is not that stabilised RF operation is unevidenced — it is well evidenced — but that its *onset after a commanded shape change* is untimed in the reviewed set.

### 3.4 The stages are split across incompatible architectures

- The only **timed S7/S8** (mechanical morphing and settling) come from **A4** platforms with no RF layer.
- The only **timed S6** (electronic state) come from **A5** rigid panels and one **A3** flexible aperture.
- The only **timed S1/S2/S4/S5 on a flexible RF surface** come from **A3**, where geometry is a *disturbance*.
- **S9 is timed by no source at all.** GAL-22 demonstrates it on a deformable radiating aperture and reports no duration; LI-25 folds it into a pre-trained static map.

Concatenating these to produce a total is not a synthesis; it is a category error across four architectures. The manuscript states this explicitly and does not perform the concatenation.

### 3.5 The A1 literature does not model stages S5–S9 at all
Across RAN-25, ANJ-25, YAN-25 and MOR-26, stages S5, S6 (except as a protocol slot), S7, S8 and S9 are either **absent** or **assumed instantaneous**. The single strongest defence offered for this omission is E-03/T-ASM-01: the claim that a computed shape remains usable indefinitely, asserted in a footnote with no supporting analysis.

### 3.6 Two quantities unreported by every source in the reviewed set
- **S8 for an RF aperture** — mechanical settling of a surface carrying meta-atom metallisation, a bias network and a ground plane. NI-22 times settling for a bare elastomer membrane; no source in the reviewed set times it for a radiating stack.
- **S9 timing** — how long the geometry→RF mapping takes to re-establish after a shape change. Timed by no reviewed source.

**S10 onset requires the distinction §3.3 makes.** Two cases, kept apart:

1. **RF stabilisation under electronic compensation with static geometry — TIMED.** LI-25's supplementary information reports 16.7 ms from a finger-triggered sensor to stabilised RF output, on a dual-channel oscilloscope through an AD8317 logarithmic detector at 3.1 GHz (`T-LI-06`).
2. **RF stabilisation following a commanded mechanical morph — NOT FOUND in the reviewed set.** No interval in the reviewed set begins with a commanded deformation and ends at trustworthy radiation. The 16.7 ms measurement cannot stand in for it: the surface is held static and no shape change occurs inside the interval.

Only case 2 is a gap. `T-GAP-03` was narrowed accordingly and must never be stated as "RF stabilisation is unreported".

These are recorded as `T-GAP-01`, `T-GAP-02` and the narrowed `T-GAP-03`, and drive the reporting framework in manuscript §10.

### 3.7 Where a closed loop does exist, it is slow for a structural reason
BAI-22 is the only closed geometry loop in the reviewed set (S1 → S2 → S4 → S7 → back to S1). Its cycle time is ≈0.25 s in the main text and 0.35 ± 0.15 s in the supplementary budget, and it is dominated **not** by mechanics (< 0.1 s) but by **S1/S2 — stereo image capture and processing** (T-BA-03).

**Narrowed 17 August 2026 — this paragraph previously over-transferred.** One platform cannot establish a general law. The supportable statement is:

> **In BAI-22's demonstrated closed geometry loop, sensing, image processing and the optimiser's search contribute substantially to total loop time and exceed the bare actuator response.** Whether the same holds in an RF FIM — where the sensing modality, the verification criterion and the compute load would all differ — must be **measured rather than assumed**.

Read as a **design warning**, not a transferred result. What does hold generally within the reviewed set is the weaker, purely negative point: **no A1 paper models this stage at all**, so none of them would detect the problem if it did occur.

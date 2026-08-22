# Adaptation-Chain Matrix

> ⚠ **Section numbers in this file are v0.14 numbering except where a v0.20/v0.21 section is named explicitly.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations).

**Version:** 2.0 · 18 August 2026 (**two-axis recoding** — see `CHANGELOG.md` v1.8, CH-100)
**Purpose:** to decompose "FIM adaptation" into ten distinct stages and record, per source, (A) what the source establishes about each stage and (B) whether the *duration* of that stage was measured. This is the instrument that prevents any one stage from being reported as the latency of the whole system.

---

## 0. Why this file was recoded — read first

**Version 1.0 used a single code set in which `M` meant "measured (a number with defined start/end events)".** In practice `M` was also applied to cells recording quantitative radio-frequency measurements that contain no duration at all — LU-26's radiation patterns at fixed curvature, NEU-24's patterns, AKR-26's patterns and power, GAL-22's ≈80 mW delivered at 1 m. Those are genuine measurements; none of them is a timing.

The consequence was a real ambiguity in a load-bearing count. The v1.8 claim *"no source measures more than five of the ten stages"* is **true under a timing reading and false under a quantitative reading** — under the latter the maximum is six. A reader could not tell which was meant, and the legend said one thing while several cells did the other.

**The fix is structural, not cosmetic: the two concepts are now separate axes.**

| Axis | Question it answers | Codes |
|---|---|---|
| **A — stage evidence status** | *What did this source establish about this stage?* | **Q** quantitatively measured (a physical or RF quantity reported) · **D** demonstrated (shown working, no quantity) · **S** simulated · **A** assumed · **✗** absent · **n/a** not applicable to the architecture · **?** unclear · **RS** review statement |
| **B — timing status** | *What does the source establish about how long this stage takes?* | **·T** a measured duration reported for this stage in its own right, with identifiable start and end events · **·(T)** a duration that exists for the stage but is a stated share or a residual of an aggregate interval, not independently measured · **·[R]** a rate or throughput, not a duration · **·[A]** an allocated or chosen interval — a design parameter, not an observation of the process · *no marker* — untimed. **An accuracy is not timing evidence** and never marks a cell, however quantitative it is. |

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
| **LI-25** | A3 | **Q·(T)** ≈2 ms reception — a stated share of the ≈4 ms data-preparation figure, derived from the ≈1200 Hz per-channel sampling rate, T-LI-01 | **Q·(T)** ≈2 ms processing — the other stated share of the same ≈4 ms figure. The RMSD of 2.36 mm is an **accuracy** (E-24) and is *not* timing evidence | ✗ **absent** | **Q·T** ANN inference ≈2 ms, prepared input → coding output, T-LI-02 | **Q·(T)** ≈5.5 ms RS-232 — a **residual** (16.76 − 11.25 ms) attributed by the authors, never measured, and carrying no dispersion | **Q·T** bias supply 5.25 ms, oscilloscope, T-LI-03; varactor qualitative only, T-LI-05 | ✗ **external, not commanded** | ✗ | **D** the ANN *is* the learned geometry→bias map; no separate timed recalibration | **Q·T‡** 16.7 ms trigger → stabilised RF, oscilloscope, T-LI-06 — see note | **3** |
| **LU-26** | A3 | ✗ | ✗ (bending known a priori) | ✗ | **S** compensation phase | ? | **D** PIN states | ✗ static bending | ✗ | **D** per-curvature compensation | **Q** patterns, 16.13 dBi, ±45° at each fixed curvature — **untimed**, E-53 | **0** |
| **NEU-24** | A5 | ✗ | n/a | ✗ | ✗ | ✗ | **Q·T** τ_on ≈15 ms / τ_off 72 ms, 10 %/90 % thresholds, T-NE-01/02 | n/a | n/a | ✗ | **Q** patterns, −50°…+50°, IL — **untimed** | **1** |
| **AKR-26** | A5 | ✗ | n/a | ✗ | ✗ | **Q·[R]** ×¼ multiplexing is a **rate factor** — no absolute interval, and not convertible to one from what the source reports, T-AK-03. The end-to-end figure in S6 includes this link, but the source apportions no share to it, and we do not derive one | **Q·(T)** <0.1 ms and <10 ms are **upper bounds on the same 16 × 16 tile**, both ending at the configuration write with **no electromagnetic end criterion**; the meta-atom transition itself is **untimed in this source**, T-AK-01/02 | n/a | n/a | ✗ | **Q** patterns, 20.2 dBi, 8.25–13 W — **untimed** | **0** |
| **BAI-22** | A4 | **Q·T** stereo imaging **0.08 ± 0.04 s**, SI Table 1 | **Q·T** template matching **0.11 ± 0.05 s** (+ reprojection ≈0), SI Table 1 | ✗ n/a | **Q·(T)** optimisation stated as ≈0 per evaluation — a negligibility statement with no dispersion and no start/end events; closed-loop convergence ≈2.5 min is a *loop* quantity, T-BA-05 | **Q·T** voltage update **0.06 ± 0.01 s**, SI Table 1 | ✗ n/a | **Q·T** element < 0.07 s (T-BA-01) and system within 0.1 s (T-BA-02), each with its own start and end events | **Q·[A]** the 0.1 ± 0.05 s settle **pause** is an interval the experimenters allocated in the cycle budget, not a measured settling duration | ✗ | ✗ **no RF layer** | **4** |
| **NI-22** | A4 | ✗ (imaging for characterisation only) | ✗ | ✗ n/a | ✗ (scripted) | **Q·(T)** ≈50 ms script processing — a stated component of the ≈650 ms shape-to-shape sum, T-NI-03 | ✗ n/a | **Q·T** ≈30 ms ribbon (T-NI-01) and ≈300 ms full surface (T-NI-02), each with its own start and end events | **Q·(T)** ≈250 ms membrane viscoelasticity — identified *within* the 300 ms surface figure, not measured separately, T-NI-02 | ✗ | ✗ **no RF layer** | **1** |
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

### 3.1 Three counts, which differ — and only one platform reaches four measured durations

Produced by `tools/c1_stage_counts.py`, which parses §2. The v0.24 rebuild of axis B changed two of
these: an accuracy is no longer timing evidence, and a stated share or residual of an aggregate is
no longer counted as a measured duration.

| Count | Maximum | Reached by |
|---|---|---|
| **Q** — quantitatively evidenced stages (axis A) | **6** | BAI-22 **and** LI-25 |
| **·T** — measured stage durations (axis B) | **4** | **BAI-22 alone** |
| **·T + ·(T)** — stages carrying any duration information | **6** | **LI-25 alone** |

| Platform | Arch. | `·T` measured | `·(T)` apportioned | other | What it cannot do |
|---|---|---|---|---|---|
| **BAI-22** | A4 | **4** — S1, S2, S5, S7, each with its own value and dispersion in SI Table 1 | 1 — S4, optimisation stated as ≈0 | S8 is an **allocated** 0.1 ± 0.05 s pause, not a measured settling time | **has no radio-frequency layer** (S6, S9, S10 do not exist on it) |
| **LI-25** | A3 | **3** — S4 (thread-timed inference), S6 (oscilloscope bias supply), S10 (oscilloscope, static geometry) | 3 — S1 and S2 are stated shares of the ≈4 ms data-preparation figure; S5 is a residual of the 16.76 ms total | the RMSD of 2.36 mm is an **accuracy**, not timing evidence | **does not command its geometry** (S7 is an external fixture) |

The disjointness survives the correction and is unchanged in substance: the two duration-bearing sets
share S1, S2, S4 and S5 and differ exactly at **S6 and S10 against S7** — LI-25 carries the
radio-frequency stages and cannot command a shape; BAI-22 carries the mechanical stages and has no radio.

**‼ AKR-26 S6 recoded 22 August 2026, from `Q·T` to `Q·(T)`.** The primary source was re-opened. Its
sub-0.1 ms figure occurs once, in the abstract, and traces to p. 6: the **end-to-end reconfiguration
time of one 16 × 16 tile**, about 40 μs over LAN or Wi-Fi and **up to 100 μs over USB/UART**, against an
internal FPGA update of about 40 ns once the configuration is stored. It is not a per-element
measurement — "per-element" does not occur in the paper — and its end event is the diode-bias write,
with **no electromagnetic criterion**. AKR-26 measures no meta-atom transition anywhere: full-text search
returns no "switching time", no "rise time" and no "settl-". S6 is defined as the meta-atom
electromagnetic state change, so the source supplies a duration bounding an aggregate that *contains*
S6's electrical write, not a duration for S6 in its own right. AKR-26's measured-duration count is
therefore **0, not 1**. The three headline maxima are unchanged, because AKR-26 was never at any of them.
S5 keeps `Q·[R]` alone: the p. 6 aggregate includes the external link, but the authors apportion no share
to it and we do not derive one. See `source_inventory.md` AKR-26 and `CHANGELOG.md` CH-151.

Two absences are strengthened by the rebuild. **S8 mechanical settling is now measured by no source at
all**: NI-22's ≈250 ms viscoelastic term is identified within its 300 ms surface figure rather than
measured separately, and BAI-22's 0.1 s is an allocated pause. **S9 calibration remains timed by no
source under any reading.**

⚠ **Wording constraints (binding).** No section may claim "five contiguous stages", a "longest
contiguous chain", or "five, reached by two platforms". No section may write "measures" for a duration
count without naming the axis. Acceptable: *"no source measures the duration of more than four of the
ten stages, and the one that reaches four does not radiate"*; *"no source carries duration information
for more than six"*; *"no source times S3 together with S7"*.

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

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

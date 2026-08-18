# Evidence-Strength Matrix

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026
**Purpose:** to record, for each capability the FIM–ISAC proposition depends on, the *highest* evidence level attained in the reviewed literature and the architecture that attained it. Evidence is never upgraded: a communication-system simulation is not hardware validation; a measured actuator is not an RF system; an electronic switching time is not a mechanical settling time.

---

## 1. The evidence ladder

| Level | Label | Meaning |
|---|---|---|
| L1 | analytical / theoretical | closed-form or model-based derivation |
| L2 | communication-system simulation | link/system-level numerical results |
| L3 | full-wave EM simulation | Maxwell solver on the actual structure |
| L4 | component measurement | a measured part (unit cell, sensor, actuator, delay line) |
| L5 | prototype RF measurement | measured RF response of an assembled aperture |
| L6 | over-the-air demonstration | a working link or application through the surface |
| L7 | end-to-end closed-loop validation | observation → decision → actuation → *verified* stabilised RF performance, timed |

---

## 2. Capability × highest evidence level

| # | Capability the FIM–ISAC proposition requires | Highest level reached | Attained by | Architecture | Evidence IDs | Gap to L7 |
|---|---|---|---|---|---|---|
| C1 | Surface geometry improves a communications objective | **L2** | RAN-25, ANJ-25, YAN-25 | A1 | E-05, E-08, E-13 | never measured on hardware |
| C2 | Surface geometry improves a sensing objective | **L2** | RAN-25 | A1 | E-07 | no physical target experiment |
| C3 | Waveform choice (OFDM/OTFS/AFDM) interacts with FIM geometry | **L2** | RAN-25 | A1 | E-06 | no implementation |
| C4 | A large aperture can be made physically flexible without losing RF function | **L5** | LI-25; GAL-22; LU-25; LU-26 | A3, A7, A2 | E-21, E-22, E-37, E-52, E-53 | **achieved** — this is not the gap |
| C5 | Surface shape can be sensed in situ | **L4/L5** | LI-25 (32 strain sensors, RMSD 2.36 mm); BAI-22 (stereo imaging); GAL-22 (self-sensing receivers) | A3, A4, A7 | E-24, E-33, E-38 | **achieved** on three platforms |
| C6 | Electronic phase state can be reconfigured quickly | **L4/L5** | AKR-26 (< 0.1 ms/element); NEU-24 (15/72 ms); LI-25 (varactor) | A5, A3 | T-AK-01, T-NE-01/02 | **achieved**, but strongly mechanism-dependent. ⚠ *Corrected 17 Aug 2026:* do not quantify the span — the quantified values (≈15 ms to tens of seconds) are all liquid crystal, and the semiconductor endpoint is unmeasured ("negligibly short", no number). See `timescale_matrix.md` Category 4. |
| C7 | A surface can be **commanded** into a target 3-D shape | **L4** | BAI-22, NI-22 | **A4 — no RF layer** | E-32, E-35 | never on an RF aperture |
| C8 | Shape command → achieved shape can be **closed-loop verified** | **L4 (mechanical only)** | BAI-22 | **A4 — no RF layer** | E-33, T-BA-03/05 | never on an RF aperture; 0.35 ± 0.15 s per cycle, **≈2.5 min to converge** |
| C9 | Electronic compensation can hold RF performance while the shape changes | **L6** | LI-25 (video link, EVM ≈ −20 dB under dynamic bending) | A3 | E-25 | **achieved** — but geometry is the disturbance, not the control |
| C10 | Geometry can be optimised against *measured* channel state | **not attained (L1/L2 only)** | — | — | E-09, E-12 | LI-25 has no channel estimator; A1 has no hardware |
| C11 | **Mechanical actuation time of an RF aperture** | **not attained** | — | — | T-GAP-02 | complete gap |
| C12 | **Mechanical settling of an RF aperture** to a phase-relevant tolerance | **not attained** | — | — | T-GAP-02 | complete gap |
| C13 | **Post-deformation calibration time** for a flexible RF aperture | **not attained** | GAL-22 demonstrates the operation at L6, but reports no duration | A7 | E-38, T-GAP-01 | operation achieved, timing absent |
| C14 | **RF stabilisation onset** — *static geometry, electronic compensation* | **L5/L6 — prototype RF measurement** *(upgraded 17 Aug 2026)* | LI-25 SI Note 6: **16.7 ms** trigger → stabilised RF, dual-channel oscilloscope + AD8317 log detector at 3.1 GHz | A3 | **T-LI-06** | the end event *is* instrumentable and has been measured |
| C14b | **RF stabilisation onset after a commanded geometry change** | **not attained** | — | — | T-GAP-03 (narrowed) | complete gap — the interval contains no morphing on any platform |
| C15 | Operation under genuine high mobility | **L2** | RAN-25 (208 m/s simulated), XU-22 (90 mph simulated) | A1, A5 | E-04, E-16 | no mobile RF experiment on any flexible surface |
| C16 | ISAC (joint sensing + communication) on a flexible surface | **L2** | RAN-25, MOR-26 | A1 | E-07 | LI-25's demonstration is communication only |
| C17 | Actuation energy / power budget for a morphing RF aperture | **not attained** | AKR-26 measures *electronic panel* power (8.25–13 W) at L4 for a rigid RIS | A5 | E-30 | no mechanical energy figure for any RF aperture |
| C18 | Repeatability / fatigue over many shape cycles, **mechanical** | **L4 — component measurement** *(upgraded 17 Aug 2026 on supplementary evidence)* | BAI-22 SI S5.4: 1 000 cycles at 1 Hz, u = 1.55 ± 0.02 mm (±10 mA), reversible over first 500 cycles at ±20 mA; LI-25 SI Note 4: 3 000 bending cycles of the strain-sensor array, negligible drift | A4, A3 (sensor layer) | E-36 | measured on actuator and sensor layers only |
| C18b | Repeatability / fatigue over shape cycles, **with RF performance tracked** | **not attained** | no source pairs a cycle count with an RF degradation measurement | — | A14 | the gap is the RF pairing, not the cycling |

---

## 3. Reading of the matrix

**Six of eighteen capabilities reach L5 or higher, and none of them is the one the theory depends on most.** Flexibility (C4), shape sensing (C5), fast electronic reconfiguration (C6) and deformation compensation (C9) are demonstrated — repeatedly, on multiple independent platforms, and in some cases at over-the-air level. The FIM concept is therefore **not** blocked by any of the things a reader might first suspect.

**The gap is narrow, specific and structural.** It sits entirely in capabilities C7, C8, C11–C14: the transition from *compensating a shape imposed from outside* to *commanding a shape and knowing when it has arrived*, on an aperture that also has to radiate. Every measurement that exists for the commanded-shape side (C7, C8) comes from A4 platforms with no meta-atoms, no bias network and no ground plane; every measurement that exists for the RF side (C4, C6, C9) comes from architectures where geometry is exogenous.

**One asymmetry deserves emphasis.** C13 is the most easily closable gap in the list. GAL-22 already performs deformation-aware closed-loop recalibration of a 256-element flexible aperture at L6. It simply does not report how long it takes. A single timed re-run of an existing experiment would move C13 from "not attained" to L5 and would materially constrain the feasibility question. The manuscript says so explicitly.

**One asymmetry cuts the other way.** C10 — optimising geometry against *measured* channel state — is not merely unmeasured; nothing in the corpus is architecturally positioned to attempt it. LI-25 has the surface, the sensors and the controller but no channel estimator; the A1 papers have the estimator but no surface. That combination, not mechanical speed, is the deepest structural gap.

---

## 4. Evidence-level distribution across the corpus

| Level | Count of corpus sources whose *highest* contribution sits here | Sources |
|---|---|---|
| L1 / L2 | 6 | RAN-25, ANJ-25, YAN-25, MOR-26, XU-22, TAG-20 |
| L3 | 3 | BUD-22, YOO-21, PEP-26 |
| L4 | 2 | BAI-22, NI-22 |
| L5 | 8 | NEU-24, AKR-26, LIH-19, GUO-25, LU-25, LU-26, CHE-26, HAR-20/HAR-22 |
| L6 | 2 | **LI-25**, GAL-22 |
| L7 | **0** | — |
| review | 3 | MA-26, SAI-22, TIS-25 |
| (analytical/EM, no RF hardware) | 1 | ALE-26 |

**Zero sources reach L7.** That is the headline of this matrix, and it is reported as a corpus-bounded observation, not as a claim about the field.

**Re-examined 17 August 2026 against the retrieved supplements, and the count stands — but the margin narrowed and the reason should be stated precisely.** LI-25's end-to-end experiment (T-LI-06) times a chain from an external trigger through sensing, inference, control transport and bias application to *verified stabilised RF output*, which satisfies more of the L7 definition than anything else in the corpus. It falls short on one criterion: the loop closes on an externally imposed, static geometry rather than on a state the system controls or on a channel it observes. L7 requires observation → decision → actuation → verified stabilised RF, and the "actuation" here is electronic compensation for a shape the system did not choose.

The honest way to record this is that **LI-25 is L6 with a measured RF-stabilisation end event** — a stronger position than any other source and stronger than this matrix credited it with before the supplement was read. No source reaches L7 because no source closes the loop on geometry it commands while radiating.

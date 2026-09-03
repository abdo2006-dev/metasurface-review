# Supplementary Table S1 — Complete timing register

Every timing quantity located in the reviewed set, with its timed object, start event, end event, measurement status and source. The main manuscript reproduces the subset that carries the argument (Table 2); this table is the full record, and the row numbering is continuous with it.

M = measured · S = simulated · P = projected · D = derived by us · A = assumed. Architecture classes are those of Table 1.

| # | Quantity | Value | Start event | End event | Object | Arch. | Status | Conditions | Source |
|---|---|---|---|---|---|---|---|---|---|
| | ***Channel and protocol (demand side)*** | | | | | | | | |
| 1 | Correlation > 0.5 window | **51 symbols** | reference instant | correlation falls to 0.5 | propagation channel | A5 | S | 90 mph, 2.6 GHz, 100 kHz | [4] p. 721 |
| 2 | Illustrative coherence cases | 20 symbols @ 0.95; 40 @ 0.82 | — | — | channel | A5 | S | same scenario | [4] Fig. 4(b), p. 728 |
| 3 | Maximum Doppler at the FIM operating point | **≈19.4 kHz** | — | — | channel | A1 | **D** | 28 GHz, 208 m/s; **a frequency, not an interval** | derived from [1] Table III |
| 4 | Pilot overhead | 1 + M slots | pilot start | direct + M links sampled | protocol | A5 | S | M = 16 | [4] p. 720 |
| 5 | FIM protocol rates | move once per subframe; phase once per slot | — | — | protocol | A1 | model | Q × T₂ | [3] p. 6829 |
| | ***Computation (wall-clock)*** | | | | | | | | |
| 6 | FIM channel estimation | ≈4 ms → ≈100 ms (benchmark ≈1.2 s) | algorithm start | convergence / cap | desktop implementation | A1 | **M** | i7-13650HX, virtual array 36–324, 400-iter cap, tol 10⁻⁸ | [3] Fig. 8, p. 6833 |
| 7 | ANN inference, 32 channels | ≈2 ms | prepared input | coding output | embedded implementation | A3 | **M** | authors' implementation | [7] p. 4 |
| 8 | Shape-optimisation convergence | ≈10 iterations; ≤100 iterations | — | — | — | A1 | **not a duration** | no processor, no per-iteration cost | [18] p. 3; [2] p. 5 |
| | ***Controller and interface*** | | | | | | | | |
| 9 | End-to-end reconfiguration | **< 0.1 ms** | host command over the external control link | configuration written to the diode bias; **no EM criterion** | **one 16 × 16 tile** | A5 | M/design bound | ≈40 μs LAN/Wi-Fi, up to 100 μs USB/UART, against ≈40 ns internal once stored; **not per-element**: the object is the tile, and no per-element measurement appears in the body | [5] abstract; decomposition p. 6 |
| 10 | Tile configuration update | **< 10 ms** | pattern command | tile pattern written; **no EM criterion** | **one 16 × 16 tile** | A5 | M/design bound | as operated in the measurement campaign; same object as row 9 | [5] p. 8, conclusion p. 9 |
| 11 | Multiplexing penalty | ×¼ of raw parallel rate | — | — | control network | A5 | design statement | relative, not absolute | [5] p. 6 |
| 12 | Bias-supply response | 5.25 ms | control output reaches supply | bias applied | 32-channel supply | A3 | **M** (oscilloscope) | — | [7] p. 4 |
| 13 | Serial transport share | ≈5.5 ms of 16.76 ms | — | — | 32 channels over RS-232 | A3 | **D** from authors' attribution | 115 200 bps | [7] SI Note 6 |
| | ***Meta-atom / material state transition*** | | | | | | | | |
| 14 | LC switch-on τ~on~ | **≈15 ms** | transition begins | 90 % threshold | 4.6 μm LC layer | A5 | **M** | 62 GHz; the 10 %/90 % markers are **read from Fig. 4a** — the text defines τ~on~ as the transition between the two LC permittivity states and states no threshold | [6] p. 5, Fig. 4a |
| 15 | LC switch-off τ~off~ | **72 ms** | relaxation begins | 10 % threshold | same layer | A5 | **M** | strongly asymmetric | [6] p. 5 |
| 16 | Earlier LC reflectarray comparator | τ~on~ "few seconds"; τ~off~ "tens of seconds" | — | — | other architectures | A5 | review statement | — | [6] p. 7 |
| 17 | Thinner-LC projection | < 2 ms | — | — | 1 μm layer | A5 | **P — not fabricated** | — | [6] p. 7 |
| 18 | Varactor switching | "negligibly short" | bias change | state changed | one meta-atom | A3 | author statement, **no number** | — | [7] p. 4 |
| | ***Partial electronic loop on a flexible radiating aperture*** | | | | | | | | |
| 19 | Data preparation | ≈4 ms | sensor reception begins | network input ready | 32 sensor channels | A3 | **M** (thread timing) | ≈1200 Hz per channel | [7] p. 4 |
| 20 | **Compensation loop** | **16.76 ms** | **shape acquisition** | **bias-voltage supply complete** | 32-channel aperture | A3 | **M** | components sum 11.25 ms; **no repetitions or dispersion stated** | [7] pp. 4–5, SI Note 6 |
| 21 | Deformation-rate limit | 60 Hz | — | — | aperture | A3 | **M — a rate** | derived by the authors from row 20 | [7] SI Note 6 |
| 22 | Projected improvement | < 10 ms | — | — | aperture | A3 | **P — not built** | needs different acquisition and protocol | [7] SI Note 6 |
| | ***Mechanical response, element level*** | | | | | | | | |
| 23 | Serpentine beam | **< 0.07 s** | current applied | stable deformation | 3.60 mm beam, **no RF layer** | A4 | **M** | 60 fps camera ⇒ ≈16.7 ms resolution floor | [22] p. 2; SI S5.3 |
| 24 | Isolated liquid-metal ribbon | **≈30 ms** (FEA ≈50 ms) | current applied | stable deformation | one ribbon, **no RF layer** | A4 | **M + S** | — | [8] p. 3 |
| | ***Mechanical response, surface level*** | | | | | | | | |
| 25 | System morphing | "within 0.1 s" | actuation command | morphed shape | 4 × 4 mesh, **no RF layer** | A4 | **M** | — | [22] abstract |
| 26 | Full surface from flat | **≈300 ms** | actuation begins | full shape developed | soft surface, **no RF layer** | A4 | **M** | ≈250 ms is membrane viscoelasticity | [8] p. 4 |
| 27 | Shape-to-shape switching | ≈650 ms | first shape command | second shape developed | same surface | A4 | **M components, D sum** | **the source prints no single figure**; it states the switching speed as a sum of three source-stated components — 300 ms + ≈50 ms script + 300 ms — and the total is our arithmetic | [8] p. 4 |
| | ***Closed mechanical control loop*** | | | | | | | | |
| 28 | Function-evaluation cycle | ≈0.25 s (text) / **0.35 ± 0.15 s** (SI) | image capture | next actuation applied | shape controller | A4 | **M** | 0.19 s imaging + matching; 0.1 s settle pause | [22] p. 4; SI Table 1 |
| 29 | Iteration cost | **4(N + M) + 2 = 34 cycles** | — | — | — | A4 | source statement — **not a duration** | 4 × 4 sample | [22] SI Note S6 |
| 30 | **Convergence** | **≈2.5 min** (average) | zero-actuation state | stopping criterion met | 4 × 4 sample, **no RF layer** | A4 | **M — stated by the source** | 170–510 function evaluations | [22] SI Note S6 |
| 31 | Open-loop actuation update rate | 10 fps | — | — | same platform | A4 | **M — a rate** | the source attaches this rate to demonstrations whose actuation voltages were **designed via its model-driven inverse method**; it is not a replay of voltages found by the closed-loop experiment-driven search | [22] SI video legends, Supplementary Videos 1–2 |
| | ***Stabilised radiation*** | | | | | | | | |
| 32 | **Trigger → stabilised RF** | **16.7 ms** | finger-triggered sensor fires | stabilised RF at receiver | flexible aperture, **geometry static** | A3 | **M** | dual-channel oscilloscope; log detector −10 to −60 dBm at 3.1 GHz | [7] SI Note 6 |
| 33 | Link held under bending | EVM ≈ −20 dB | — | — | aperture under dynamic bending | A3 | **M, untimed** | QPSK video, 3.1 GHz, 2 m | [7] |
| | ***Assumed, not measured*** | | | | | | | | |
| 34 | Shape-reuse lifetime | **unbounded** — "irrespective to changes in delays, Doppler shifts and waveform" | shape computed for one realisation | *never stated* | A1 model | A1 | **A** | no condition given | [1] footnote 10, p. 13327 |
| 35 | Shape update rate | once per coherence block | — | — | A1 model | A1 | **A** | — | [32] |
| | ***Not measured by anything in the reviewed set*** | | | | | | | | |
| G1 | Commanded actuation of a **radiating** aperture | — | actuation command | intended displacement | RF aperture | A1/A3 | **✗** | — | — |
| G2 | Settling of a radiating aperture to a phase-relevant tolerance | — | end of gross motion | stated electromagnetic criterion | RF aperture | A1/A3 | **✗** | — | — |
| G3 | Post-deformation calibration duration | — | shape change | mapping re-established | flexible RF aperture | A7/A3 | **✗** | operation demonstrated, untimed | [23] (absence) |
| G4 | Stabilised radiation after a **commanded** morph | — | commanded deformation | trustworthy radiation | RF aperture | all | **✗** | row 32 contains no shape change | — |

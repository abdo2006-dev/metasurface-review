# Architecture Taxonomy

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026
**Purpose:** to prevent the single most common category error in this literature — transferring a latency, a control capability, a mechanical feasibility argument, or a validation strength from one physical architecture to another.

---

## 1. The seven classes

| Class | Name | What physically changes | Deformation source | RF state electronically programmable? |
|---|---|---|---|---|
| **A1** | Theoretical FIM array with independently movable elements | element coordinates (usually along the surface normal) | unspecified — an optimisation variable | in some formulations yes (element phase), in others the geometry *is* the only control |
| **A2** | Physically flexible **passive** reflective metasurface | whole-sheet curvature | external / mounting | ✗ no |
| **A3** | Externally deformed, shape-aware **programmable** reflective surface | whole-sheet curvature | **external** (hand, platform, mount) | ✓ yes |
| **A4** | Actively self-morphing mechanical surface | commanded local out-of-plane displacement | **self-actuated** | ✗ (no RF layer at all) |
| **A5** | Conventional electronically reconfigurable RIS | nothing mechanical — only meta-atom EM state | none (rigid) | ✓ yes |
| **A6** | Movable / reconfigurable antenna systems | antenna position or orientation, or internal antenna state | self-actuated (motors, MEMS) | ✓ for the RA sub-class |
| **A7** | Flexible **active** antenna array | whole-sheet curvature | external | ✓ (per-element RFIC phase/amplitude) |

**A1 is a model class, not a hardware class.** No source in this corpus demonstrates A1 hardware. The theoretical FIM literature (RAN-25, ANJ-25, YAN-25, MOR-26) motivates A1 by citing A4 platforms (BAI-22, NI-22). That citation is a *plausibility argument*, not a realisation: A4 platforms have no meta-atoms, no bias network, no RF ground plane and no measured electromagnetic response.

---

## 2. Per-source classification

Legend for the evidence columns: **D** demonstrated · **M** measured · **S** simulated · **A** assumed · **✗** not present · **?** unclear.

### A1 — theoretical FIM arrays

| | RAN-25 | ANJ-25 | YAN-25 | MOR-26 |
|---|---|---|---|---|
| What moves | element y-coordinates, TX **and** RX | element y-coordinates at BS | element positions in a plane | element y-coordinates, TX and RX |
| Movement range | y ∈ [−λ, +λ] | 0 ≤ y_n ≤ y_max, ζ up to ≈1.5 λ | 12 × 12 discretised grid | as RAN-25 |
| Actuation mechanism | ✗ none specified | ✗ | ✗ | ✗ |
| External vs self deformation | A (implicitly self) | A | A | A |
| Electronic phase control | ✗ (geometry only) | ✗ (geometry + digital beamformer) | ✓ modelled (PBF mode) | ✗ |
| Geometry sensing | ✗ | ✗ | ✗ | ✗ |
| Channel information used | full DD channel parameters, A | **perfect CSI, stated** | estimated via proposed protocol | full DD channel parameters, A |
| Loop | open (single-shot optimisation) | open | open | open |
| RF performance | **S** | **S** | **S** | **S** |
| High mobility present | ✓ (v ≤ 208 m/s modelled) | ✗ (quasi-static flat fading, stated) | ✗ | ✓ |
| ISAC present | ✓ | ✗ | ✗ | ✓ |
| Measured latency | ✗ | ✗ | **partial** — algorithm runtime only (Fig. 8, seconds) | ✗ |

### A2 — flexible passive reflective metasurfaces

| | GUO-25 | LU-25 |
|---|---|---|
| What changes | sheet curvature; phase set by fixed PB-rotation pattern | sheet curvature; phase set by fixed 1-bit coding |
| Deformation source | external | external (bending applied for measurement) |
| Electronic programmability | ✗ | ✗ |
| Geometry sensing | ✗ | ✗ |
| Loop | none | none |
| Measured RF | ✓ fabricated array, ±50° steering | ✓ 15 × 15 liquid metal on PDMS, 10 GHz dual beam ±45°, 17.9 dBi, radiation stable over **±25 % bending** |
| Latency | ✗ | ✗ |
| High mobility / ISAC | ✗ / ✗ | ✗ / ✗ |

### A3 — externally deformed, shape-aware programmable reflective surfaces ★ the closest realised analogue of a FIM

| | **LI-25** | **LU-26** |
|---|---|---|
| What changes | sheet curvature **and** varactor bias per column | sheet curvature **and** PIN state per element |
| Deformation source | **external**, applied by a custom mechanical platform | **external**, static mounting on acrylic supports of different bending degrees |
| Deformation dynamic during operation? | ✓ yes — compensation demonstrated under *dynamic* bending | ✗ no — each bending degree is a separate static measurement |
| Electronic programmability | ✓ 32 column channels, 0–30 V varactors | ✓ per-element PIN diodes, 1-bit |
| **Geometry sensing** | ✓ **32 flexible strain sensors, RMSD as low as 2.36 mm at 45 mm displacement** | ✗ none — bending state is known a priori |
| Controller | ANN → FPGA → bias-supply module, RS-232 link | not characterised for timing |
| Channel information used | ✗ **none** — the loop closes on *geometry*, not on channel state | ✗ |
| Loop | **closed on shape** (sense → infer → bias), open on channel | open |
| Measured RF | ✓ 3.0–3.4 GHz, ≈270° phase over 0–45° incidence, EM illusion / cloak / reflectarray / video link (EVM ≈ −20 dB) | ✓ 9 GHz, ±45° scanning, 16.13 dBi |
| **Measured latency** | ✓ **partial loop, 16.76 ms** (shape acquisition → bias-voltage supply) + components 4 / 2 / 5.25 ms | ✗ none |
| High mobility / ISAC | ✗ / ✗ | ✗ / ✗ |

**The decisive architectural point.** LI-25 and LU-26 are the corpus's only surfaces that are simultaneously flexible, reflective and electronically programmable. **In both, the geometry is an exogenous disturbance to be compensated, not a control variable to be optimised.** The A1 literature inverts this: it treats geometry as the *primary* control variable. No corpus source demonstrates that inversion in hardware.

### A4 — actively self-morphing mechanical surfaces

| | **BAI-22** | **NI-22** |
|---|---|---|
| What moves | out-of-plane displacement of a 4 × 4 filamentary mesh | out-of-plane displacement of liquid-metal ribbon network |
| Actuation | distributed Lorentz force, I < 27.5 mA, B = 224 ± 16 mT | Lorentz force on liquid-metal microfluidic ribbons |
| **Self-actuated** | ✓ | ✓ |
| Scale | L = W = 18.0 mm, u/L ≈ 30 % (≈5.4 mm) | 4 mm max deformation, 7.07 mm aperture |
| Geometry sensing | ✓ **in-situ stereo imaging** | ✗ (3D imaging used for characterisation, not control) |
| Loop | ✓ **closed-loop, experiment-driven self-evolving inverse design** | open-loop (script-driven) |
| RF layer present | ✗ **none** | ✗ **none** |
| Measured RF performance | ✗ | ✗ |
| **Measured mechanical timing** | ✓ element < 0.07 s (60 fps camera); system "within 0.1 s"; function-evaluation cycle 0.35 ± 0.15 s; **closed-loop convergence ≈2.5 min**; open-loop replay 10 fps | ✓ ribbon ≈30 ms; **full surface from flat ≈300 ms**; shape-to-shape ≈650 ms incl. ≈50 ms script processing |
| High mobility / ISAC | ✗ / ✗ | ✗ / ✗ |

**A4 supplies the only measured mechanical timescales in the corpus, and supplies them for objects with no RF function.** Adding meta-atoms, a bias network, a serpentine RF ground plane and a dielectric substrate (cf. LI-25's mechanical co-design) changes mass, stiffness and damping. Transferring A4 timing to an A1 or A3 RF aperture is therefore an extrapolation, and the corpus contains no measurement bounding its error.

### A5 — conventional electronically reconfigurable RIS

| | NEU-24 | AKR-26 | XU-22 | TAG-20 | PEP-26 | CHE-26 | HAR-20 / HAR-22 |
|---|---|---|---|---|---|---|---|
| Geometry | rigid planar | rigid planar | rigid (modelled) | rigid planar (modelled) | **rigid cylindrical** | **rigid 3D-printed curved** | rigid planar |
| Tuning | liquid crystal | PIN, 1-bit | modelled phase | modelled states | 1-bit meta-atoms | voltage-programmable **2-bit** | varactor, continuous |
| Geometry sensing | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Channel info | ✗ | ✗ | ✓ modelled estimator | ✗ | ✗ | ✗ | ✗ |
| Loop | open | open | open (protocol) | — | — | open | open |
| Measured RF | ✓ | ✓ | ✗ | ✗ | S (full-wave) | ✓ | ✓ (HAR-22 array) |
| **Measured latency** | ✓ **τ_on ≈ 15 ms / τ_off = 72 ms** (10 %/90 %) | ✓ **< 0.1 ms per element; < 10 ms per tile** | ✗ | ✗ | ✗ | ✗ | ✗ |
| High mobility | ✗ | ✗ | ✓ modelled (90 mph) | ✗ | ✗ | ✗ | ✗ |
| ISAC | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ (radar-stealth application) | ✗ |

**PEP-26 and CHE-26 matter to the taxonomy for a specific reason:** they show that *conformality* and *fixed curvature* have validated design methods and measured, full-wave-corroborated hardware behind them for the cases they treat. ⚠ **Corrected 17 Aug 2026 — do not write that curvature is "solved" or universally "handled".** These are important prior-art results for specific apertures, bands and bend families; none claims to bound the general problem, and curvature, oblique local incidence and finite phase resolution remain active design constraints. The defensible contrast is: fixed-curvature conformal design has substantial prior art, whereas **time-varying, controlled geometry with a measured loop** has none.

### A6 / A7 — movable-antenna systems and flexible active arrays

| | MA-26 (review, A6) | GAL-22 (A7) | ALE-26 (A7) |
|---|---|---|---|
| What changes | antenna position/orientation, or internal RA state | sheet curvature | 2-D folding of a 4 × 4 patch array |
| Deformation source | self-actuated (motors, MEMS) | external | external (modelled) |
| Electronic programmability | ✓ | ✓ per-element RFIC | ✓ modelled |
| Geometry sensing | discussed as a requirement | ✓ **self-sensing receivers used for phase calibration and shape estimation** | ✗ |
| Loop | discussed | ✓ **closed-loop focusing via remote-receiver feedback** | ✗ |
| Measured RF | review of others' hardware | ✓ 256 elements, 30 × 30 cm, bend radii < 23 cm, ≈80 mW DC at 1 m | ✗ (HFSS only) |
| **Measured latency** | ✗ (identifies movement time as something models *should* include) | ✗ **none — calibration/refocusing time not reported** | ✗ |
| High mobility / ISAC | discussed / ✓ discussed | ✗ / ✗ | ✗ / ✗ |

---

## 3. Transfer rules (the operative output of this taxonomy)

These rules are used throughout the manuscript and the audits.

1. **A4 → A1/A3 timing transfer is prohibited without qualification.** A4 platforms carry no RF layer. Their measured response times bound a *different mechanical object*.
2. **A5 electronic switching time is not a mechanical settling time.** AKR-26's < 0.1 ms and NEU-24's 15/72 ms describe meta-atom state transitions on rigid substrates.
3. **A3 partial-loop latency is not full-loop latency.** LI-25's 16.76 ms starts *at* shape acquisition and ends *at* bias-voltage supply. It contains no deformation and no RF-settling interval.
4. **A7 is not A5.** GAL-22's flexible array is an active transmitter with per-element RFICs; its calibration architecture does not carry over to a passive reflective aperture.
5. **A2 bending tolerance is not adaptation.** LU-25's stability over ±25 % bending is a *robustness* result for a fixed coding pattern, not evidence of a control loop.
6. **Fixed curvature is not variable geometry.** PEP-26, CHE-26, LIH-19, BUD-22 and YOO-21 all design *for* a known shape. None of them tracks a changing one.
7. **A1 protocol units are not time.** YAN-25's subframes and time slots, and XU-22's 1 + M slots, are protocol structure. Converting them to milliseconds requires numerology that none of these papers supplies.

---

## 4. Where each architecture sits on the two axes that matter

**Corrected 17 August 2026 — the axes are properties of an experiment, and the map covers demonstrated hardware only.** The previous version labelled the lower half "geometry is EXOGENOUS" and left A1 to be read into it. That was wrong in two ways. In the A1 formulation geometry is *not* exogenous — the element coordinates are the primary optimisation variable — so the label inverted the very property the taxonomy exists to track. And A1 has no hardware, so it cannot answer either axis question: it demonstrates no commanded geometry and measures no RF, but it does so by being a model, not by failing an experiment. The axes are now stated as demonstrated capabilities, and A1 is represented as the **target operating point** that names the empty cell rather than as a platform occupying a cell.

```
        COMMANDED PHYSICAL GEOMETRY DEMONSTRATED
                              ▲
                              │
        A4  BAI-22, NI-22 ────┼──── (empty)
        (mechanics only,      │      ← A1's modelled target operating point:
         no RF layer)         │        geometry chosen by the optimiser on an
                              │        aperture whose radiation is the objective
   ───────────────────────────┼───────────────────────────►
    RF NOT measured           │            RF PERFORMANCE MEASURED
                              │
                              │    A3  LI-25, LU-26
                              │    A2  GUO-25, LU-25
                              │    A5  NEU-24, AKR-26, PEP-26, CHE-26, HAR
                              │    A7  GAL-22
        COMMANDED PHYSICAL GEOMETRY NOT DEMONSTRATED
```

The upper-right cell — a measured RF aperture that also commands its own geometry — is **empty in this corpus**. That emptiness, stated at exactly this resolution, is the manuscript's central factual claim.

**Reading rule.** A1 is a model class (§2.2) and is never plotted as a platform. Saying "A1 sits in the lower-left cell" would assert that a modelling paper failed two experiments it never ran; saying "A1 treats geometry as exogenous" would contradict the A1 model itself. The correct form is: *the empty cell is the operating point A1 assumes.* Prose, Figure 1 and `manuscript/02_architecture.md` §2.8 all use this formulation.

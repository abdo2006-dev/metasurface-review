## 3. Seven architecture classes relevant to FIM evidence transfer

### 3.1 Why the taxonomy comes first, and what it is a taxonomy of

Evidence about FIM feasibility is drawn from seven physically distinct kinds of system, and a statement true of one is routinely false of another. A response time measured on a filamentary mechanical mesh, an update rate measured on a rigid PIN-diode panel and a compensation loop measured on a bending varactor-loaded sheet are not three data points describing one technology; they describe three technologies whose measurements are nonetheless quoted in support of one architecture. Everything in Sections 5 to 9 depends on keeping them apart, so the separation is made first.

**These seven classes are not seven things called "flexible metasurfaces".** Only A1 through A4 are named as flexible or morphing metasurfaces by the literature that uses them, and even there the naming is inconsistent. The remaining classes are included because the FIM literature draws evidence from them, not because their authors claim the label:

- **Direct classes — the object under review.** A1 the theoretical FIM, A2 flexible passive reflective metasurfaces, A3 externally deformed shape-aware programmable surfaces, A4 actively self-morphing mechanical surfaces. These share a physical premise — a surface whose geometry is not fixed — and are the classes over which the review's central claim is made.
- **Comparator and evidence-donor classes.** A5 rigid electronically reconfigurable RIS, A6 movable and reconfigurable antenna systems, A7 flexible active antenna arrays. Their authors do not generally call them flexible intelligent metasurfaces, and this review does not either. They appear because they supply the timing comparators, the control-architecture vocabulary and the strongest deformation-aware radio-frequency demonstration in the reviewed set, and because values measured on them are quoted in FIM feasibility arguments. Naming them precisely is what makes the transfer rules of §3.6 statable at all.

Three questions distinguish the classes: **what physically changes**; **whether the change is imposed from outside or commanded by the system**; and **whether the radio-frequency state is independently programmable**. Table 1 answers them, together with the questions that decide what a measurement is worth — whether the shape is sensed, whether radio-frequency performance was measured at all, and whether any mobility was involved. The prose below does not restate the table; it draws the four conclusions the table makes visible.

**Table 1 — Architecture classes drawn on by the FIM evidence base.** A1–A4 are the direct classes; A5–A7 are comparator or evidence-donor classes whose authors do not generally use the FIM label.

| Class | What it is | What changes | Deformation source | RF state programmable | Shape sensed | RF measured | Mobility evidence | Representative sources |
|---|---|---|---|---|---|---|---|---|
| **A1** | Theoretical FIM array with independently movable elements | element coordinates | an optimisation variable — no mechanism specified | in some formulations | n/a | ✗ — no hardware | simulated only | [1], [2], [3], [15] |
| **A2** | Flexible **passive** reflective metasurface | sheet curvature | external | ✗ | ✗ | ✓ at fixed curvatures | ✗ | [16], [17] |
| **A3** | Externally deformed, shape-aware **programmable** reflective surface | curvature **and** meta-atom state | external | ✓ | ✓ ([6]) / a priori ([18]) | ✓ | ✗ | [6], [18] |
| **A4** | Actively self-morphing mechanical surface | commanded local displacement | **self-actuated** | **no RF layer at all** | ✓ ([7], stereo imaging) | ✗ | ✗ | [7], [8] |
| **A5** | Rigid electronically reconfigurable RIS | meta-atom state only | none | ✓ | n/a | ✓ | ✗ | [4], [5], [19] (modelled) |
| **A6** | Movable / reconfigurable antenna system | position, orientation or internal state | self-actuated | ✓ (RA sub-class) | — | outside the reviewed measurement scope | — | [11] (review) |
| **A7** | Flexible **active** antenna array | sheet curvature | external | ✓ (per-element RFIC) | ✓ (on-chip self-sensing) | ✓ | ✗ | [20], [21] |

### 3.2 A1 is a model class, and the platforms cited for its plausibility are A4

No source in the reviewed set demonstrates A1 hardware. The FIM system papers define the surface as a coordinate vector constrained to a morphing range and entering the array response through the propagation phase [1, Eqs. (1a)–(3), p. 13321]; they specify no actuator, no sheet mechanics, no inter-element mechanical coupling and no fabrication route. Where physical plausibility is argued, two mechanical platforms are cited: a liquid-metal microfluidic network in an elastomeric matrix, and an array of metallic filaments actuated by distributed Lorentz forces [1, p. 13320], citing [8] and [7] respectively.

That is a plausibility argument and should be read as one. Both cited platforms are A4: they carry no meta-atoms, no bias network, no dielectric substrate and no radio-frequency ground plane. The distinction is not pedantic, and the reviewed set contains a direct measurement of why. When a flexible reflective microwave surface was actually built, achieving mechanical flexibility required replacing a solid copper ground with a serpentine mesh — a change reported to reduce estimated bending stiffness by more than two orders of magnitude [6, p. 3]. The mechanical properties of a radio-frequency-loaded aperture are a design outcome, not a property inherited from the actuator concept, and nothing in the reviewed set bounds the difference.

### 3.3 The realised flexible apertures invert the control problem

The two realised surfaces in the reviewed set that are simultaneously flexible, reflective and electronically programmable are A3, and they share a property that the A1 formulation reverses.

In the flexible microwave metasurface with shape-guided adaptive programming [6], a 480 × 240 mm sheet carrying 32 × 16 meta-atoms is bent by an external mechanical platform. A conformal array of 32 strain sensors reconstructs the shape — one reported validation gives a root-mean-square deviation as low as 2.36 mm at a maximum displacement of 45 mm — and a trained neural network maps the reconstructed shape to the column bias voltages that restore the intended electromagnetic behaviour. The loop closes on *geometry*: the surface senses a shape it did not choose and compensates for it electronically. There is no channel estimator anywhere in the system. In the conformal reconfigurable reflectarray built from polydimethylsiloxane and printed liquid metal [18], a 10 × 10 array at 9 GHz with per-element PIN diodes achieves ±45° beam scanning and 16.13 dBi peak gain using element-level conformal compensation phase; the prototype is mounted on acrylic supports of different bending degrees, so each curvature is a separate static experiment and the surface neither senses nor commands its shape.

The A1 formulation inverts this. There, geometry is the *primary control variable* — the thing chosen to maximise an objective — and the channel is what is being tracked. **No source in the reviewed set demonstrates that inversion in hardware.** This is the single most consequential fact in the taxonomy, and Sections 5 and 9 return to it.

### 3.4 The platforms that command a shape have no radio

The two A4 platforms supply every measured mechanical timescale in this review, and neither has an electromagnetic function. The filamentary mechanical metasurface [7] is a 4 × 4 mesh of thin metal and polyimide traces on an 18.0 mm sample, driven by distributed Lorentz forces in a 224 ± 16 mT field at currents below 27.5 mA, achieving reversible out-of-plane deformation of about 30 % of the sample length; uniquely in the reviewed set it closes a loop on shape, with in-situ stereo imaging feeding an experiment-driven, self-evolving inverse design. Its demonstrations are optical, structural and multifunctional, and no wireless beamforming is reported. The soft shape-programmable surface [8] uses liquid-metal microfluidic ribbons in an elastomer, actuated by Lorentz forces, and can fix a programmed shape through a liquid-metal phase transition — a mechanism by which a slowly-set geometry could in principle be held without continuous actuation. It reports no reflection phase, gain, radiation pattern or communication result.

These are the right platforms to cite for mechanical feasibility. They are the wrong platforms to cite for a FIM response time, and Section 8 shows that the distinction has not always been maintained.

### 3.5 Fixed-curvature conformal design is substantial prior art, and it is prior art about a different problem

A large body of conformal work concerns apertures whose shape is known and does not change. Rigorous synthesis of planar and conformal beamforming metasurfaces using integral-equation models that account for finite size, coupling and spatial dispersion is established, with a conformal reflectarray among the worked examples [22]. A reduced-order coupled-dipole model of a cylindrically conformal waveguide-fed metasurface agrees closely with full-wave simulation near 28 GHz at large bend radii [23]. An active conformal metasurface lens achieves up to about 195° of transmission-phase tuning and ±60° beam coverage using multiple feeds [24]. Cylindrical RIS design has been carried from idealised surface-impedance synthesis through one-bit meta-atom implementation and validated by full-wave simulation [25]. A 3D-printed curved substrate with voltage-programmable two-bit coding deflects between 0° and 50° over 9.3–10.5 GHz with pointing accuracy better than ±2° [26]. A flexible 15 × 15 liquid-metal-on-PDMS reflectarray maintains favourable radiation characteristics across a ±25 % bending range with a fixed one-bit coding pattern [17].

Taken together these establish that validated design methods and measured hardware exist for important fixed-curvature cases, across several bands, phase resolutions and synthesis approaches. That is prior art, not closure — none of these results claims to bound the general problem, and curvature, oblique local incidence and finite phase resolution remain aperture- and band-specific design constraints. What the group does not address is *change*: none of these surfaces tracks a varying shape, and none reports how long any of its operations takes. **Bending tolerance under a fixed coding pattern is a robustness result, not an adaptation result.**

The adjacent classes contribute in a similar way. Movable and reconfigurable antenna systems (A6) supply the conceptual vocabulary — fast internal state changes, slow physical repositioning, and the resulting case for instantaneous channel information in quasi-static environments and statistical information in fast fading [11] — without supplying FIM measurements. Flexible active antenna arrays (A7) supply the strongest evidence that large flexible coherent apertures are physically realisable: two 256-element, 30 × 30 cm arrays remain fully functional and programmable at concave and convex bend radii below 23 cm, with closed-loop focusing driven by feedback from a remote receiver and calibration explicitly targeting phase offsets caused by manufacturing variation, **shape deformation** and environmental change [20]. Section 6.5 returns to what that demonstration does and does not tell us.

### 3.6 Transfer rules

These follow from §§3.2–3.5 and are applied without exception in the remainder of the manuscript.

1. **A4 timing does not transfer to A1 or A3 without qualification.** A4 platforms have no radio-frequency layer; their measured response times bound a different mechanical object.
2. **An A5 electronic switching time is not a mechanical settling time.**
3. **An A3 partial-loop latency is not a full-loop latency.** The interval reported for the flexible microwave metasurface begins at shape acquisition and ends at bias-voltage supply; it contains no deformation and no radio-frequency settling.
4. **A7 is not A5.** An active array's calibration architecture — self-sensing receivers closing a loop against a remote beacon — does not carry over to a passive reflective aperture, which has neither.
5. **A2 bending tolerance is not adaptation.**
6. **Fixed curvature is not variable geometry.**
7. **Protocol units are not durations.** Subframes, time slots and iteration counts are structure, not time, and none of the sources reporting them supplies the numerology needed to convert.

### 3.7 The shape of the gap

Figure 1 maps the reviewed hardware on two axes that are properties of an experiment: *has the platform demonstrated commanded physical geometry?* and *has radio-frequency performance been measured on it?* The map is drawn over **physically demonstrated platforms only**, and the restriction is deliberate — a modelling paper answers neither question, because it performs no experiment, and placing simulation work in a hardware quadrant would be a category error.

| | **RF performance measured** | **RF performance not measured** |
|---|---|---|
| **Commanded geometry demonstrated** | *(empty)* | A4: [7], [8] |
| **Commanded geometry not demonstrated** | A2, A3, A5, A7: [6], [18], [17], [16], [5], [4], [25], [26], [24], [27]/[28], [20] | A6 platforms outside the reviewed measurement scope |

**One cell is empty: commanded geometry demonstrated *and* radio-frequency performance measured.** No reviewed hardware demonstration sits there.

**A1 does not occupy a cell in this map. It names the cell.** The A1 system model is not physical evidence to be classified; it is the specification of the operating point the empty cell describes — geometry chosen by the optimiser, on an aperture whose radiation is what the optimisation is for. Drawn that way, the map states the review's central structural finding without misdescribing anybody: the modelled target operating point is the one for which no measured platform exists.

> **Figure 1.** *Architecture–evidence map of the reviewed hardware.* Both axes are properties of an experiment, so only platforms that performed one are plotted; the theoretical FIM performs none and is drawn as an annotation on the empty cell rather than as a platform. The empty cell is the review's central structural finding: commanded geometry and measured radio-frequency performance have not been demonstrated together. *(File: `figures/fig1_architecture_evidence_map.pdf`.)*

# Architecture Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026

Checks every cross-architecture statement in the draft against the seven transfer rules of §2.7.

---

## 1. Transfer-rule compliance

| Rule | Where the draft could violate it | Verdict |
|---|---|---|
| **R1** A4 timing does not transfer to A1/A3 without qualification | §5.3, §6.2, §6.5, §6.6 (S7/S8 rows) | ✅ pass. §5.3 opens "neither carries an electromagnetic function"; §6.2 closes "it says nothing about an aperture carrying meta-atoms"; §6.6's S7 and S8 rows read "**no RF layer**" and "unproven for a radiating aperture". Four independent restatements. |
| **R2** A5 electronic switching ≠ mechanical settling | §5.2 vs §5.3 | ✅ pass — the two are in separate subsections and never summed; §6.3 explicitly disclaims commensurability. |
| **R3** A3 partial-loop ≠ full-loop | §1.2, §5.1, §6.3 | ✅ pass. §5.1: "It is a compensation latency, and calling it a FIM adaptation time would misattribute it by at least two stages at each end." |
| **R4** A7 ≠ A5 | §5.4, §7.4 | ✅ pass — §5.4 states "an active transmitter with per-element RFICs … not a passive reflector" (via §2.6). ⚠ **minor gap:** §5.4 itself does not restate the active/passive distinction, relying on §2.6. **Fix applied below.** |
| **R5** A2 bending tolerance ≠ adaptation | §2.5, §7.1 | ✅ pass. §2.5: "Bending tolerance with a fixed coding pattern is a robustness result, not an adaptation result." |
| **R6** Fixed curvature ≠ variable geometry | §2.5, §7.1 | ✅ pass. |
| **R7** Protocol units ≠ durations | §3.4, §6.6 | ✅ pass — §3.4 states "we do not convert them to milliseconds; the sources supply no numerology." |

## 2. Classification review

Each source's architecture assignment was re-checked against the three defining questions (what changes / deformation source / RF programmability).

| Source | Assigned | Challenge | Resolution |
|---|---|---|---|
| LI-25 | **A3** | Could be A4: it is a "flexible intelligent" surface and the FIM literature cites it as hardware evidence | **A3 confirmed.** The deformation is applied by an external custom mechanical platform; the surface has no actuator. The paper's own framing is compensation, not commanded morphing. This is the single most consequential classification in the review and it is stated four times in the draft. |
| LU-26 | **A3** | Could be A2: bending is static | **A3 confirmed** — it is electronically reconfigurable (PIN diodes), which is A3's defining property; the static bending is a measurement protocol, not an architecture property. Noted in §5.1. |
| LU-25 | **A2** | Could be A3 | **A2 confirmed** — 1-bit coding is fixed at fabrication; no reconfiguration. |
| GAL-22 | **A7** | Could be A3: it is flexible, programmable and deformation-aware | **A7 confirmed and the distinction matters.** Per-element RFICs, PLLs and self-sensing receivers make it an active transmitter. Its calibration architecture (closed loop against a remote beacon) is unavailable to a passive reflector, which has no transmit chain to sense with. Draft §2.6 and §7.3 both rely on this. |
| BAI-22, NI-22 | **A4** | Could arguably be "mechanical metamaterial", outside the taxonomy | **A4 confirmed** — they are the platforms the FIM literature cites as its hardware basis, so they must be in the taxonomy to be audited. |
| PEP-26, CHE-26 | **A5-conformal** | Could be A2 (they are curved) | **A5-conformal confirmed** — curvature is fixed at manufacture; the reconfigurability is electronic. CHE-26's substrate is 3D-printed, i.e. rigid by construction. |
| ALE-26 | **A7** | It has no fabricated array | **A7-modelled.** The draft cites it only for curvature-aware array modelling and never as hardware. ✅ |
| XU-22 | **A5** | It models no specific panel | **A5-modelled.** Cited only for channel behaviour and protocol overhead, never as hardware. ✅ |

## 3. The A1 framing check

The draft asserts that A1 is a model class with no hardware instance in the reviewed set. Adversarial challenge: **is that unfair to LI-25, which is literally titled a "flexible intelligent … metasurface"?**

Answer: no, and the reason is architectural rather than nominal. A1's defining property is that element coordinates are *chosen* by an optimiser. LI-25's coordinates are imposed by an external platform and *measured* by strain sensors. The two systems differ in the direction of causality between geometry and control, which is exactly what §2.3 calls the inversion. Naming is not the criterion; the direction of causality is. The draft states this rather than assuming it.

Secondary challenge: **is it unfair to LU-26, which computes a conformal compensation phase for each bending degree?** Also no — the bending degrees are set by the acrylic mounts, and the compensation is a response to them.

## 4. Fix applied

**A-FIX-1.** §5.4 relied on §2.6 for the active/passive distinction. One clause added so the subsection stands alone. *(Applied.)*

## 5. Residual architecture risks

| Risk | Severity |
|---|---|
| The A2/A3 boundary depends on whether reconfigurability is present, which is clear in this corpus but may blur for surfaces with mechanically reconfigurable meta-atoms | Low |
| A1's boundary would need revisiting if a self-actuated RF FIM prototype appears — at which point the review's central finding would change and should | **By design** |
| Classifying the three image-only sources rests on abstracts alone | Low — each is cited only for what its abstract states |

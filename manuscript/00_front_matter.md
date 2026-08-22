# Flexible Intelligent Metasurfaces for High-Mobility ISAC: Hardware Evidence, Adaptation Timescales, and Validation Gaps

**Draft v0.28a — structured critical review — 22 August 2026.**

---

## Abstract

A flexible intelligent metasurface (FIM) treats the physical shape of an aperture as a control variable alongside its electromagnetic state. Some recent system studies place that variable inside high-mobility integrated sensing and communication, where the delay–Doppler channel varies rapidly, and argue that shape adaptation follows it. Whether existing hardware supports that argument is this review's question: which operations in a FIM-assisted high-mobility link plausibly require fast adaptation, which may run on slower geometric or statistical timescales, and what has been measured about either?

We separate the architecture classes the FIM evidence base draws on, decompose FIM adaptation into ten stages from sensing to stabilised radiation, and record every timing value with its timed object, start and end events, and measurement status. Three results follow. No reviewed platform measures the duration of more than four of the ten stages, and the platform reaching four has no radio-frequency layer; the two best-covered platforms are disjoint at the boundary that matters, one commanding shape without radiating, the other radiating without commanding shape. No independently measured settling or post-deformation calibration duration is reported in the reviewed set, and stabilised radiation is timed only with geometry held static. Tracing the hardware-feasibility premises of the FIM system literature to their primary sources shows element-level response times presented as surface morphing periods, and a tabulated value with no counterpart in the cited source.

The contribution is the audit and the reporting discipline it motivates; we propose no hardware and do not claim the architecture is infeasible.

**Index terms** — Flexible intelligent metasurface, reconfigurable intelligent surface, integrated sensing and communication, high mobility, adaptation latency, hardware validation, evidence synthesis, conformal metasurface.

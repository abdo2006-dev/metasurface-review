# Flexible Intelligent Metasurfaces for High-Mobility ISAC — Project Brief

A structured critical review asking what existing hardware actually validates about the *speed* of shape adaptation in flexible intelligent metasurfaces, and where the evidence stops.

## 1. The question

A flexible intelligent metasurface (FIM) treats the physical shape of an aperture as a control variable alongside the electromagnetic state of its elements. Some recent system studies place that variable inside high-mobility integrated sensing and communication, where the channel changes quickly, and assume or argue that shape adaptation can operate on the relevant channel timescale.

> Which operations in a FIM-assisted high-mobility link actually have to track the fast-varying channel, which can run on slower geometric or statistical timescales, and what has hardware demonstrated about either?

## 2. Why it matters

Changing an electromagnetic state and changing a physical shape are different processes. The first propagates at the speed of a tuning mechanism; the second requires moving matter, and so involves actuation, structural dynamics and settling. System models represent shape as a variable that may be set, and are not obliged to model the mechanism that sets it. In quasi-static conditions the abstraction may be less consequential for system-level performance. Under high mobility its timing assumptions become potentially load-bearing, and within the reviewed set it is the assumption with the least measurement behind it.

## 3. What I reviewed

Twenty-four distinct research contributions, assembled by convenience rather than by protocol: FIM system-modelling papers; flexible and conformal RF metasurface hardware; programmable mechanical morphing platforms; electronically reconfigurable RIS hardware reporting switching times; and high-mobility channel-estimation work. Plus a forward citation search of the three primary hardware sources, to test how their timing values are reused downstream.

## 4. Three main findings

**1 — Within the reviewed set, no platform times the adaptation chain end to end.** Decomposing FIM adaptation into ten stages and coding what each source establishes about each stage — and about how long it takes — no reviewed platform measures the duration of more than four of the ten, and the platform reaching four has no radio-frequency layer. The two best-covered platforms are disjoint exactly where the question lies: one commands its shape but does not radiate; the other radiates but does not command its shape.

**2 — The timing numbers in circulation refer to different physical objects.** A 16.76 ms figure quoted from this literature runs from shape acquisition to bias-voltage supply, and contains neither the deformation that produced the shape nor any settling afterwards. One panel reports both a sub-0.1 ms and a sub-10 ms configuration update — same hardware, same 16 × 16 tile, two orders of magnitude apart, with neither bound stating a start event, an end criterion, or the object it applies to in the abstract that carries it. Recording each value with its object, start event and end event makes such differences visible; without that, a substitution is undetectable on the page.

**3 — The gap is the intersection, not the ingredients.** Commanded geometry has been demonstrated. Measured RF performance on flexible apertures has been demonstrated. Within the reviewed set, we did not identify a platform combining commanded geometry with measured RF performance on the same object. No reviewed source measures settling to an electromagnetic tolerance on a commanded radiating aperture; post-deformation recalibration *has* been demonstrated on a flexible active array, but its duration was not reported; and the one reviewed interval ending in stabilised radiation was measured with the geometry held static.

Supporting this, tracing the FIM system papers' hardware-feasibility premises to their primary sources found element-level response times presented as surface morphing periods, and a tabulated 10 ms value with no counterpart in the cited source's complete published package. That finding is bounded to the 13 of 20 candidate citing studies whose full texts were accessible, and the four studies carrying it form one connected co-authorship network, so it documents one collaboration network rather than a field.

## 5. The central figure

Figure 1 states the result in one view: the cell requiring *commanded geometry* and *measured RF performance* together is empty, while its three neighbours are populated.

## 6. What may be publishable

Stated conservatively: an architecture-aware framework for deciding when evidence may transfer between physically different platforms; a stage-resolved timing audit separating measured durations from apportioned ones; a traceability finding about how timing values change scope as they propagate; and a precise statement of the validation gap with the reporting fields that would prevent it recurring.

## 7. What I am not claiming

Not a systematic review — the corpus was assembled by convenience. Not evidence that FIMs are infeasible; nothing here shows the architecture cannot work. Not the invention of two-timescale or statistical-CSI control, which is established in the movable-antenna and FIM literatures and cited as prior work. Not comprehensive field coverage, and no claim about how prevalent any practice is.

## 8. Questions I would value your judgement on

1. Is the framing physically sound — in particular, is separating *measured* stage durations from durations apportioned out of an aggregate the right distinction for an RF and control audience?
2. Is the evidence and traceability gap interesting enough to carry a review article, or is it a section of a larger paper?
3. Which parts would you challenge or cut? The traceability audit has been compressed into the evidence section and its case-by-case inventory moved to the supplement, on the view that it was doing more work than the argument needed; I would value your judgement on whether that is now the right weight.
4. What venue and article format would be realistic — review, tutorial, or a shorter perspective?

*Draft v0.28a for academic review — August 2026. Working paper; not submitted, and not ready for submission. The full manuscript, figures and supplementary material accompany this brief.*

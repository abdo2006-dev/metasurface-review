# Supplementary Table S2 - Timing-quantity taxonomy

The quantity types used throughout the review, each with its start event, end event and timed object, and the substitution it most often invites. Values may be compared only within a type, and only when their comparability classes intersect.

| Quantity type | Start event | End event | Object | The substitution it invites |
|---|---|---|---|---|
| **Element mechanical response** | actuation current or voltage applied | element reaches stable displacement | one actuator or beam | being read as a whole-surface morphing period |
| **Surface mechanical response** | actuation command | full commanded shape developed | the whole surface | being read as the element figure, or as a settled shape |
| **Mechanical settling** | end of gross motion | residual motion within a stated tolerance | the whole surface | being bundled into "response time" with no separate figure |
| **Closed-loop shape convergence** | initial (often zero-actuation) state | verified arrival at a commanded shape | surface plus its sensing and search | being confused with open-loop replay of a known shape |
| **Open-loop replay rate** | — | — | surface with precomputed drive | being quoted as a latency; it is a rate |
| **Meta-atom EM state transition** | bias change applied | material or device state crosses a stated threshold | one meta-atom or one layer | being quoted without its direction or its threshold |
| **Controller / interface write** | command issued by the compute element | control state written to the target | one element, one tile, or the whole panel | **being quoted without naming the object** |
| **Computation wall-clock** | algorithm start | convergence or iteration cap | an implementation on named hardware | being compared across processors, or replaced by an iteration count |
| **Partial electronic loop** | a named intermediate event (e.g. shape acquisition) | a named intermediate event (e.g. bias applied) | a chain of stages, not the whole chain | being read as an end-to-end adaptation latency |
| **Stabilised RF onset** | a named trigger | radiated output stable at a stated detector criterion | the aperture in operation | being read as post-morph stabilisation when the geometry was static |
| **Channel / protocol timescale** | reference instant | correlation crosses a stated threshold | the propagation channel | being read as an interval of constancy, or as a deadline |

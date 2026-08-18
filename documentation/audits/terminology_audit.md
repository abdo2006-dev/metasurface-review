# Terminology Audit

> ⚠ **Section numbers in this file are v0.14 numbering.** The manuscript was restructured into twelve sections on 18 August 2026 (draft v0.20). Use the crosswalk at the end of `manuscript_argument_map.md`; most often, **§6.5 → §8** (traceability) and **§9.4 → §11.4** (limitations). The scientific content of this file is unchanged and still governs.

**Version:** 1.0 · 17 August 2026

---

## 1. Terms whose meaning is fixed for this manuscript

| Term | Meaning used | Meanings deliberately excluded |
|---|---|---|
| **Response time** | never used unqualified | in the reviewed literature it denotes at least five different intervals: an LC state transition, a mechanical element deflection, a mechanical system morph, an electronic partial loop, and a tabulated "morphing period". The draft always names the object and the interval instead. |
| **Adaptation** | the full ten-stage sequence S1→S10 | not any subset |
| **Reconfiguration** | electronic state change only (S6) | not mechanical morphing |
| **Morphing** | commanded mechanical shape change (S7) | not compensation for an externally imposed shape |
| **Compensation** | electronic correction for an exogenous geometry | not morphing |
| **Settling** | decay of transient motion to within a stated tolerance (S8) | not "response time"; never bundled with rise time |
| **Coherence time** | the interval over which fading remains correlated **above a stated threshold** | never "the interval over which the channel is constant" |
| **Latency** | an interval with a named start and end event | never a rate, never an iteration count, never a protocol-unit count |
| **Update time** | always qualified by object: per element or per tile | never unqualified |
| **Closed loop** | a loop that senses the quantity it controls | the draft distinguishes loops closed on *geometry* (LI-25, BAI-22), on a *beacon* (GAL-22), and on a *channel* (none) |
| **Validation** | measurement on the object being claimed about | not simulation, not measurement on an analogous object |
| **FIM** | the A1 model class | the draft does not apply it to any hardware in the reviewed set, and says why (§2.3) |
| **Flexible metasurface** | a physically bendable surface, class-qualified on first use | never used as a synonym for FIM |

## 2. Consistency check across the draft

| Check | Result |
|---|---|
| Is "response time" ever used unqualified? | ✅ no — every instance names the object and interval, or appears inside a quotation from a source |
| Is "reconfiguration" ever applied to mechanical change? | ✅ no |
| Is "coherence time" ever used to mean constancy? | ✅ no — §3.1 exists specifically to prevent it |
| Is "FIM" ever applied to a corpus hardware source? | ✅ no. §2.2 and §2.3 state why. One risk: the reviewed flexible microwave metasurface calls itself "flexible intelligent"; §2.3 and `architecture_audit.md` §3 address the naming collision explicitly |
| Is "validate" applied to a simulation? | ✅ no — "full-wave validated" appears once, in §2.5, describing a paper's own internal validation of a model against a solver, which is the standard use |
| Are architecture classes named on first use in each section? | ✅ §§2, 5, 6.6, 7 all name classes; §§3, 8, 9 do not need them |
| Is "two-timescale" ever presented as the manuscript's own? | ✅ no — §1.3 and §9.1 both attribute it, and `novelty_boundary.md` §3 item 5 forbids it |
| Is "systematic" used of this review? | ✅ no — §1.6 states no systematic-review claim is made |

## 3. Terms deliberately avoided

- **"Real-time"** — used by two reviewed sources with no stated deadline. The draft never uses it except inside quotation.
- **"Fast" / "slow"** as unqualified predicates of a layer — §6.3 exists to show that these are mechanism-dependent, so the draft uses them only with a mechanism named.
- **"State of the art"** — carries an implicit completeness claim the search does not support.
- **"Novel"** — the manuscript's contributions are auditing contributions and are described as such.
- **"Bridging the gap"**, **"paving the way"**, **"it is important to note"**, **"this highlights"** — absent.

## 4. Notation and unit consistency

| Check | Result |
|---|---|
| Times | ms and s used consistently; source-reported values keep their source's unit (0.07 s not 70 ms) so the reader can find them, with the ms equivalent given where a comparison needs it |
| Displacement | millimetres and wavelengths both given wherever both are meaningful; §8.2 Group C makes this a framework requirement |
| Angles | degrees throughout |
| Frequencies | GHz throughout; the LC device's 62 GHz and the flexible surface's 3.2 GHz are always stated when the two are compared |
| Gain | dBi, with the section of the source named where a source reports different values in different sections |

## 5. One residual terminology risk

The word **"intelligent"** in "flexible intelligent metasurface" does no technical work in any reviewed source, and the naming collision it creates between the A1 model class and at least one A3 hardware platform is the single largest source of category confusion in this literature. The draft handles it by classifying on architecture rather than on name, and by stating the criterion (§2.3: the direction of causality between geometry and control). This is a mitigation, not a solution; a reader who skips §2 could still conflate the two.

**Recommendation:** if a reviewer reports confusion on this point, add one sentence to the abstract naming the distinction explicitly. It is not there now because the abstract is already dense.

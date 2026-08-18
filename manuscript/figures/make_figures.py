#!/usr/bin/env python3
"""
Publication figures for:
  "Flexible Intelligent Metasurfaces for High-Mobility ISAC:
   Hardware Evidence, Adaptation Timescales, and Validation Gaps"  (draft v0.21)

Every value drawn here is transcribed from `Documentation/evidence_matrix.md`
Part B and `Documentation/timescale_matrix.md`.  No value is invented, derived
or interpolated in this script.  Figure 3 in particular is a *display* of
heterogeneous quantities on a common axis: it is drawn in separate labelled
lanes precisely so that the reader cannot read it as a single latency budget.

Run:  python3 make_figures.py      (writes fig1..fig4 as .pdf and .png)
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
import matplotlib.patheffects as pe

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 8.5,
    "axes.linewidth": 0.7,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.03,
    "pdf.fonttype": 42,
})

INK   = "#1a1a1a"
GREY  = "#8c8c8c"
LGREY = "#e8e8e8"
MEAS  = "#2b5d8a"   # measured
DEMO  = "#7ba7c7"   # demonstrated, untimed
ASSUM = "#c8c8c8"   # assumed / simulated
GAP   = "#b03a2e"   # no measurement found in the reviewed set


def save(fig, name):
    for ext in ("pdf", "png"):
        fig.savefig(f"{name}.{ext}", dpi=400)
    plt.close(fig)
    print("wrote", name)


# ---------------------------------------------------------------- Figure 1
def figure1():
    """Architecture / evidence map.  Axes are properties of an experiment.
    A1 is drawn as an annotation on the empty cell, not as a plotted platform."""
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.set_xlim(0, 2); ax.set_ylim(0, 2); ax.axis("off")

    cells = {
        (0, 1): ("", ""),                      # top-left: empty cell
        (1, 1): ("A4  self-morphing mechanical",
                 "Bai [7], Ni [8]\ncommanded shape, closed-loop verified\n"
                 "no meta-atoms, no bias network, no RF ground"),
        (0, 0): ("A2 · A3 · A5 · A7  radiating apertures",
                 "[4], [5], [6], [16], [17], [18],\n"
                 "[20], [24], [25], [26], [27], [28]\n"
                 "geometry externally imposed or fixed"),
        (1, 0): ("A6  movable / reconfigurable antennas",
                 "outside the reviewed measurement scope"),
    }
    for (col, row), (title, body) in cells.items():
        x, y = col, row
        empty = (col, row) == (0, 1)
        ax.add_patch(Rectangle((x, y), 1, 1, facecolor="white" if empty else "#f5f7f9",
                               edgecolor=INK, lw=0.8,
                               hatch="" if not empty else None, zorder=1))
        if empty:
            ax.add_patch(Rectangle((x + .04, y + .04), .92, .92, facecolor="none",
                                   edgecolor=GAP, lw=1.4, ls=(0, (4, 3)), zorder=2))
            ax.text(x + .5, y + .70, "E M P T Y", ha="center", va="center",
                    color=GAP, fontsize=11, fontweight="bold")
            ax.text(x + .5, y + .52,
                    "no reviewed platform commands\nits geometry AND radiates",
                    ha="center", va="center", color=GAP, fontsize=8)
            ax.text(x + .5, y + .22,
                    "A1 — the theoretical FIM —\nspecifies this operating point.\n"
                    "It is not a platform in this map;\nit names the empty cell.",
                    ha="center", va="center", color=INK, fontsize=7.4, style="italic")
        else:
            ax.text(x + .5, y + .86, title, ha="center", va="center",
                    fontsize=8.4, fontweight="bold", color=INK)
            ax.text(x + .5, y + .48, body, ha="center", va="center",
                    fontsize=7.2, color="#333333", linespacing=1.45)

    ax.text(0.5, 2.10, "RF performance measured", ha="center", fontsize=8.6, fontweight="bold")
    ax.text(1.5, 2.10, "RF performance not measured", ha="center", fontsize=8.6, fontweight="bold")
    ax.text(-0.06, 1.5, "commanded geometry\ndemonstrated", ha="right", va="center",
            fontsize=8.6, fontweight="bold", linespacing=1.4)
    ax.text(-0.06, 0.5, "commanded geometry\nnot demonstrated", ha="right", va="center",
            fontsize=8.6, fontweight="bold", linespacing=1.4)
    save(fig, "fig1_architecture_evidence_map")


# ---------------------------------------------------------------- Figure 2
def figure2():
    """Ten-stage adaptation chain on TWO axes.

    Fill colour  = stage evidence status (Q quantitative / D demonstrated / A assumed).
    Appended "T" = timing status: the DURATION of that stage was measured.
    "(T)"        = duration reported but incompletely defined or not resolved
                   from an adjacent stage.
    The point of the figure is the cells that are Q with no T: a radiation
    pattern, a gain or a delivered power is a measurement but not a timing.
    """
    stages = ["S1\nsense", "S2\ngeom.\nest.", "S3\nchannel\nest.", "S4\noptimise",
              "S5\ncontrol\ntx", "S6\nelectronic\nupdate", "S7\nmechanical\nmorphing",
              "S8\nsettling", "S9\ncalibration", "S10\nstabilised\nRF"]
    rows = [
        ("A1  theoretical FIM\n[1], [2], [3], [15]",
         ["", "", "S·T", "S", "", "A", "A", "", "", "A"]),
        ("A3  flexible programmable aperture\n[6]   (geometry imposed)",
         ["Q·T", "Q·(T)", "", "Q·T", "Q·(T)", "Q·T", "", "", "D", "Q·T*"]),
        ("A5  rigid reconfigurable RIS\n[4], [5]",
         ["", "", "", "", "Q·(T)", "Q·T", "", "", "", "Q"]),
        ("A4  self-morphing mechanical\n[7], [8]   (no RF layer)",
         ["Q·T", "Q·T", "", "Q·T", "Q·T", "", "Q·T", "Q·T", "", ""]),
        ("A7  flexible active array\n[20]",
         ["D", "D", "", "D", "D", "D", "", "", "D", "Q"]),
    ]
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    nS, nR = len(stages), len(rows)
    for j, (label, codes) in enumerate(rows):
        y = nR - 1 - j
        ax.text(-0.25, y + .5, label, ha="right", va="center", fontsize=7.2,
                linespacing=1.5, color=INK)
        for i, c in enumerate(codes):
            base = c.split("·")[0].rstrip("*")
            fc = {"Q": MEAS, "D": DEMO, "A": ASSUM, "S": ASSUM, "": "white"}[base]
            ax.add_patch(Rectangle((i, y), 1, 1, facecolor=fc,
                                   edgecolor="white" if c else LGREY, lw=1.0))
            if c:
                ax.text(i + .5, y + .5, c, ha="center", va="center", fontsize=6.6,
                        color="white" if base in ("Q", "D") else "#555555",
                        fontweight="bold")

    ax.plot([6.05, 6.05, 9.95, 9.95], [-0.10, -0.28, -0.28, -0.10],
            lw=1.0, color=GAP, clip_on=False)
    ax.text(8.0, -0.42,
            "across the reviewed set, these four stages are timed only on platforms\n"
            "with no RF layer (S7, S8), not timed at all (S9), or timed only with\n"
            "the geometry held static (S10)",
            ha="center", va="top", fontsize=7.1, color=GAP, fontweight="bold",
            linespacing=1.45)

    for i, s_ in enumerate(stages):
        ax.text(i + .5, nR + .10, s_, ha="center", va="bottom", fontsize=6.9,
                linespacing=1.35, color=INK)
    ax.set_xlim(-0.02, nS); ax.set_ylim(-1.75, nR + 0.85); ax.axis("off")

    handles = [Rectangle((0, 0), 1, 1, facecolor=MEAS),
               Rectangle((0, 0), 1, 1, facecolor=DEMO),
               Rectangle((0, 0), 1, 1, facecolor=ASSUM),
               Rectangle((0, 0), 1, 1, facecolor="white", edgecolor=LGREY)]
    ax.legend(handles,
              ["Q  quantitatively measured", "D  demonstrated, no quantity",
               "A / S  assumed or simulated", "     absent / not applicable"],
              loc="upper left", bbox_to_anchor=(-0.30, -0.01), frameon=False,
              fontsize=7, handlelength=1.1, ncol=2, columnspacing=1.4)
    ax.text(-3.05, -1.42,
            "·T  the duration of the stage was measured, with identifiable start and end events\n"
            "·(T)  a duration is reported but incompletely defined, or not resolved from an adjacent stage\n"
            "*  geometry held static throughout the timed interval",
            ha="left", va="bottom", fontsize=6.6, style="italic", color="#555555",
            linespacing=1.6)
    save(fig, "fig2_adaptation_chain")


# ---------------------------------------------------------------- Figure 3
def figure3():
    """Timing landscape.  Separate lanes by process: NOT a latency budget."""
    lanes = [
        ("demand (modelled)", [
            dict(kind="note",
                 text="Doppler \u2248 19.4 kHz at 28 GHz / 208 m/s \u2014 a frequency, not an interval")]),
        ("computation", [
            dict(kind="point", x=2e-3, text="ANN inference 2 ms \u00b7 A3", ha="right"),
            dict(kind="bar", lo=4e-3, hi=1e-1,
                 text="FIM channel estimation 4\u2013100 ms, desktop CPU \u00b7 A1", ha="left")]),
        ("controller / interface", [
            dict(kind="point", x=1e-4, text="< 0.1 ms, one element \u00b7 A5", ha="left"),
            dict(kind="point", x=1e-2, text="< 10 ms, one 16\u00d716 tile \u00b7 A5", ha="left")]),
        ("material / EM state", [
            dict(kind="bar", lo=1.5e-2, hi=7.2e-2,
                 text="liquid crystal, 15 ms on / 72 ms off \u00b7 A5", ha="left")]),
        ("partial electronic loop", [
            dict(kind="point", x=1.676e-2,
                 text="16.76 ms  shape acquisition \u2192 bias supply \u00b7 A3", ha="left")]),
        ("mechanical, element", [
            dict(kind="point", x=3e-2, text="ribbon 30 ms", ha="right"),
            dict(kind="point", x=7e-2, text="beam < 70 ms \u00b7 A4, no RF layer", ha="left")]),
        ("mechanical, surface", [
            dict(kind="multi", xs=[1e-1, 3e-1, 6.5e-1],
                 tags=["< 0.1 s", "300 ms", "650 ms"],
                 text="A4, no RF layer", ha="left")]),
        ("mechanical loop \u2014 replay", [
            dict(kind="point", x=1e-1,
                 text="10 fps open-loop replay, voltages known \u00b7 A4", ha="left")]),
        ("mechanical loop \u2014 search", [
            dict(kind="point", x=1.5e2,
                 text="\u2248 2.5 min closed-loop convergence \u00b7 A4", ha="right")]),
        ("stabilised RF, static geometry", [
            dict(kind="point", x=1.67e-2,
                 text="16.7 ms  trigger \u2192 stabilised RF \u00b7 A3", ha="left")]),
        ("commanded mechanical actuation\nof a radiating aperture",
         [dict(kind="gap", text="NO MEASUREMENT FOUND IN REVIEWED SET")]),
        ("stabilised RF after a\ncommanded morph",
         [dict(kind="gap", text="NO MEASUREMENT FOUND IN REVIEWED SET")]),
    ]
    fig, ax = plt.subplots(figsize=(7.4, 4.5))
    n = len(lanes)
    for k, (lane, items) in enumerate(lanes):
        y = n - 1 - k
        ax.axhspan(y - .45, y + .45, color="#fafafa" if k % 2 == 0 else "white", zorder=0)
        ax.text(-0.015, y, lane, transform=ax.get_yaxis_transform(),
                ha="right", va="center", fontsize=7.4, color=INK, linespacing=1.4)
        for it in items:
            kind = it["kind"]
            if kind == "note":
                ax.text(6e-5, y, it["text"], va="center", fontsize=7.0,
                        color="#555555", style="italic")
            elif kind == "gap":
                ax.add_patch(Rectangle((6e-5, y - .32), 2.5e3, .64,
                                       facecolor="#f7e9e7", edgecolor=GAP,
                                       lw=0.9, ls=(0, (4, 3)), zorder=1))
                ax.text(4e-1, y, it["text"], ha="center", va="center", fontsize=7.2,
                        color=GAP, fontweight="bold", zorder=3)
            elif kind == "point":
                ax.plot([it["x"]], [y], marker="o", ms=4.4, color=MEAS, zorder=3)
                off = 1.45 if it["ha"] == "left" else 1 / 1.45
                ax.text(it["x"] * off, y, it["text"], va="center",
                        ha=it["ha"], fontsize=7.0, color=INK, zorder=3)
            elif kind == "bar":
                ax.plot([it["lo"], it["hi"]], [y, y], lw=5.0, color=MEAS,
                        solid_capstyle="butt", alpha=.85, zorder=2)
                ax.text(it["hi"] * 1.45, y, it["text"], va="center", ha="left",
                        fontsize=7.0, color=INK, zorder=3)
            elif kind == "multi":
                for m, (xv, tag) in enumerate(zip(it["xs"], it["tags"])):
                    ax.plot([xv], [y], marker="o", ms=4.4, color=MEAS, zorder=3)
                    ax.text(xv, y + (.30 if m % 2 else .16), tag, ha="center",
                            va="bottom", fontsize=6.4, color="#333333", zorder=3)
                ax.text(it["xs"][-1] * 1.45, y, it["text"], va="center", ha="left",
                        fontsize=7.0, color=INK, zorder=3)

    ax.set_xscale("log")
    ax.set_xlim(4e-5, 4e3)
    ax.set_ylim(-0.6, n - 0.4)
    ax.set_yticks([])
    ax.set_xlabel("seconds  (logarithmic)", fontsize=8)
    ax.set_xticks([1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1, 1e2, 1e3])
    ax.set_xticklabels(["100 \u00b5s", "1 ms", "10 ms", "100 ms", "1 s", "10 s", "100 s", "1000 s"],
                       fontsize=7.4)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.grid(axis="x", color=LGREY, lw=0.6, zorder=0)
    ax.set_axisbelow(True)
    save(fig, "fig3_timing_landscape")


# ---------------------------------------------------------------- Figure 4
def figure4():
    """System assumptions -> the evidence link each one crosses."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.set_xlim(0, 10); ax.set_ylim(-1.15, 6.5); ax.axis("off")

    assumptions = [
        "geometry freely selectable\nwithin a morphing range",
        "morphing instantaneous, or\nwithin one coherence block",
        "computed shape stays usable\nirrespective of delay / Doppler",
        "mapping re-established\nwhenever needed",
        "radiation trustworthy as\nsoon as the shape is set",
        "command transport and\nelectronic update are free",
    ]
    evidence = [
        ("commanded shape control\n[7], [8] \u2014 no RF layer", "mismatch"),
        ("≈300 ms surface morph\n[8] — bare elastomer", "mismatch"),
        ("no bound, condition or\nexperiment in reviewed set", "none"),
        ("closed-loop refocusing\n[20] \u2014 not timed", "untimed"),
        ("16.7 ms to stabilised RF\n[6] \u2014 geometry static", "wrongevent"),
        ("≈5.5 ms of 16.76 ms; ×¼\nmultiplexing — measured", "measured"),
    ]
    gaps = {0: "G1", 1: "G2", 2: "—", 3: "G3", 4: "G4", 5: "—"}
    colour = {"mismatch": GAP, "none": GAP, "untimed": "#c98a2e",
              "wrongevent": "#c98a2e", "measured": MEAS}

    for i, (a, (e, kind)) in enumerate(zip(assumptions, evidence)):
        y = 5.6 - i * 1.0
        ax.add_patch(Rectangle((0.05, y - .38), 3.0, .76, facecolor="#f5f7f9",
                               edgecolor=GREY, lw=0.6))
        ax.text(1.55, y, a, ha="center", va="center", fontsize=7.1, linespacing=1.45)
        ax.add_patch(Rectangle((6.0, y - .38), 3.3, .76, facecolor="white",
                               edgecolor=colour[kind], lw=0.9))
        ax.text(7.65, y, e, ha="center", va="center", fontsize=7.1, linespacing=1.45)
        style = "-" if kind == "measured" else (0, (4, 3))
        ax.add_patch(FancyArrowPatch((3.15, y), (5.9, y), arrowstyle="-|>",
                                     mutation_scale=9, lw=1.0, ls=style,
                                     color=colour[kind], shrinkA=0, shrinkB=0))
        if gaps[i] != "—":
            ax.text(4.52, y + .22, gaps[i], ha="center", va="bottom", fontsize=7.4,
                    color=GAP, fontweight="bold",
                    path_effects=[pe.withStroke(linewidth=2.2, foreground="white")])

    ax.text(1.55, 6.15, "system-model assumption", ha="center", fontsize=8.2, fontweight="bold")
    ax.text(7.65, 6.15, "closest evidence in the reviewed set", ha="center",
            fontsize=8.2, fontweight="bold")
    ax.text(4.52, 6.15, "link", ha="center", fontsize=8.2, fontweight="bold")
    ax.text(0.05, -0.62,
            "Dashed links are unsupported by a measurement on a comparable object: architecture mismatch "
            "(red), operation\ndemonstrated but untimed or measured from the wrong start event (amber).  "
            "G1–G4 name the missing interval (Table 8).",
            fontsize=6.9, color="#444444", va="bottom", linespacing=1.5)
    save(fig, "fig4_assumption_evidence_map")


if __name__ == "__main__":
    figure1(); figure2(); figure3(); figure4()

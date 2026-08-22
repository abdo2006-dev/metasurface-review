#!/usr/bin/env python3
"""Derive the authoritative C1 per-source stage counts from adaptation_chain_matrix.md.

Axis A (stage evidence status):  Q  D  S  A  ✗  n/a  ?  RS
Axis B (timing status), rebuilt in v0.24 from first principles. A quantity is timing
evidence only if it carries information about temporal duration, rate or allocation.
An accuracy (for example an RMSD in millimetres) is NOT timing evidence, however
quantitative it is, and no longer marks a cell.

  ·T    measured duration, with identifiable start and end events, reported for this
        stage in its own right (its own value, and where available its own dispersion)
  ·(T)  non-separable duration: a duration for this stage exists but is a stated share
        or a residual of an aggregate interval and was not independently measured
  ·[R]  a rate or throughput, not a duration; it cannot be converted into a stage
        duration without information the source does not supply
  ·[A]  an allocated or chosen interval -- a design parameter, not an observation of
        how long the physical process takes
  unmarked -- untimed

Only ·T licenses "times". ·T and ·(T) together are "carries duration information".
·[R] and ·[A] are timing-related but are neither, and are counted separately.

The matrix is the single authoritative source for C1. This script parses it so that
no count in the manuscript is maintained by hand.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import ROOT, DOC, MANUSCRIPT, DECISIONS, WORKS, RECORDS, REGISTER, MATRIX
import re, json, sys
from pathlib import Path

STAGES = [f"S{i}" for i in range(1, 11)]


def parse_matrix():
    lines = MATRIX.read_text(encoding="utf-8").splitlines()
    # the matrix proper: rows beginning "| **NAME** |" inside section 2
    try:
        start = next(i for i, l in enumerate(lines) if l.startswith("## 2. The matrix"))
        end = next(i for i, l in enumerate(lines) if i > start and l.startswith("## 3."))
    except StopIteration:
        sys.exit("could not locate section 2 of the matrix")
    out = {}
    for line in lines[start:end]:
        m = re.match(r"\|\s*\*\*([A-Z]+-\d+)\*\*\s*\|", line)
        if not m:
            continue
        name = m.group(1)
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # cells[0]=source, cells[1]=architecture, cells[2:12]=S1..S10, cells[12]=timed total
        stage_cells = cells[2:12]
        if len(stage_cells) != 10:
            sys.exit(f"{name}: expected 10 stage cells, got {len(stage_cells)}")
        out[name] = {"arch": cells[1], "cells": dict(zip(STAGES, stage_cells)),
                     "recorded_timed": cells[12] if len(cells) > 12 else ""}
    return out


def classify(cell):
    """Return (axis_a, axis_b) for one cell.

    axis_a in {Q,D,S,A,absent,n/a,?,RS}
    axis_b in {T,(T),untimed}
    """
    txt = cell
    # Axis B first -- the marker is unambiguous and may sit on a bolded code.
    if re.search(r"·\[R\]", txt):
        axis_b = "[R]"
    elif re.search(r"·\[A\]", txt):
        axis_b = "[A]"
    elif re.search(r"·\(T\)", txt):
        axis_b = "(T)"
    elif re.search(r"·T", txt):
        axis_b = "T"
    else:
        axis_b = "untimed"

    # Axis A: the leading code, which is bolded when present.
    head = re.sub(r"\s*\(.*", "", txt).strip()
    if head.startswith("n/a"):
        return "n/a", axis_b
    if "RS" in head:
        return "RS", axis_b
    m = re.match(r"\*\*([QDSA])", head)
    if m:
        return m.group(1), axis_b
    if head.startswith("✗"):
        return "absent", axis_b
    if head.startswith("?"):
        return "?", axis_b
    m = re.search(r"\*\*([QDSA])[·\*]", txt)
    if m:
        return m.group(1), axis_b
    if txt.startswith("✗"):
        return "absent", axis_b
    return "?", axis_b


def main():
    matrix = parse_matrix()
    table = {}
    for name, rec in matrix.items():
        q = d = t = tp = 0
        t_stages, tp_stages, q_stages = [], [], []
        rate_stages, alloc_stages = [], []
        simulated_timing = []
        for s in STAGES:
            a, b = classify(rec["cells"][s])
            if a == "Q":
                q += 1; q_stages.append(s)
            if a == "D":
                d += 1
            if b == "T":
                t += 1; t_stages.append(s)
                if a == "S":
                    simulated_timing.append(s)
            elif b == "(T)":
                tp += 1; tp_stages.append(s)
            elif b == "[R]":
                rate_stages.append(s)
            elif b == "[A]":
                alloc_stages.append(s)
        table[name] = {
            "arch": rec["arch"],
            "quantitative_stages": q, "quantitative_stage_ids": q_stages,
            "demonstrated_stages": d,
            "fully_delimited_T": t, "T_stage_ids": t_stages,
            "partially_delimited_T": tp, "partial_stage_ids": tp_stages,
            "any_timing_T_plus_partial": t + tp,
            "rate_only_stage_ids": rate_stages,
            "allocated_interval_stage_ids": alloc_stages,
            "any_timing_stage_ids": sorted(t_stages + tp_stages, key=lambda s: int(s[1:])),
            "timing_that_is_simulated_not_measured": simulated_timing,
            "recorded_timed_column": rec["recorded_timed"],
        }
    maxima = {
        "max_quantitative": max(v["quantitative_stages"] for v in table.values()),
        "max_fully_delimited_T": max(v["fully_delimited_T"] for v in table.values()),
        "max_any_timing": max(v["any_timing_T_plus_partial"] for v in table.values()),
    }
    maxima["sources_at_max_quantitative"] = sorted(
        k for k, v in table.items() if v["quantitative_stages"] == maxima["max_quantitative"])
    maxima["sources_at_max_fully_delimited_T"] = sorted(
        k for k, v in table.items() if v["fully_delimited_T"] == maxima["max_fully_delimited_T"])
    maxima["sources_at_max_any_timing"] = sorted(
        k for k, v in table.items() if v["any_timing_T_plus_partial"] == maxima["max_any_timing"])
    return {"per_source": table, "maxima": maxima}


if __name__ == "__main__":
    res = main()
    hdr = f"{'source':<9} {'arch':<10} {'Q':>2} {'T':>2} {'(T)':>4} {'T+(T)':>6}  T stages"
    print(hdr); print("-" * len(hdr))
    for k, v in sorted(res["per_source"].items()):
        print(f"{k:<9} {v['arch']:<10} {v['quantitative_stages']:>2} {v['fully_delimited_T']:>2} "
              f"{v['partially_delimited_T']:>4} {v['any_timing_T_plus_partial']:>6}  "
              f"{','.join(v['T_stage_ids']) or '-'}"
              f"{'  +(' + ','.join(v['partial_stage_ids']) + ')' if v['partial_stage_ids'] else ''}")
    print()
    print(json.dumps(res["maxima"], indent=1))

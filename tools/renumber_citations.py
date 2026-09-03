#!/usr/bin/env python3
"""Renumber the publication-facing citations into order of first appearance.

The repository keeps a *stable* source numbering so that the evidence matrix, the
adaptation-chain matrix, the timing register and the source inventory can stay keyed to
one identifier across draft revisions. A journal bibliography must instead be numbered in
order of first appearance in the text. Those two requirements are met by keeping the
stable identifiers where they belong -- in the internal registers and the machine-readable
data -- and deriving the display numbering from the manuscript itself.

The map is written to Documentation/citation_display_map.csv so the substitution stays
reproducible after the fact.

    python3 tools/renumber_citations.py            # report the map, change nothing
    python3 tools/renumber_citations.py --apply    # rewrite the display numbering

Applying it twice is a no-op: once the manuscript is in first-appearance order the map is
the identity.
"""
import argparse, csv, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import DOC, MANUSCRIPT

BODY = ["00_front_matter.md", "01_introduction.md", "02_scope_and_method.md",
        "03_architectures.md", "04_hardware_evidence.md", "05_validation_gap.md",
        "06_implications.md", "07_conclusion.md"]
BIB = "99_references.md"
SUPPLEMENT = sorted(DOC.glob("supplement_*.md"))
FIGURES = MANUSCRIPT / "figures" / "make_figures.py"

BRACKET = re.compile(r"\[([^\[\]]*)\]")
ENTRY = re.compile(r"^\[(\d+)\] ", re.M)


def leading_refs(segment):
    """The reference numbers at the head of one ';'-delimited bracket segment.

    A citation may carry locators -- "[6, pp. 4-5]", "[19, p. 721 and Fig. 4(b), p. 728]"
    -- so only the unbroken run of bare integers at the start of a segment is a reference.
    Everything from the first non-integer token onwards is a locator and is left alone.
    """
    toks = [t.strip() for t in segment.split(",")]
    n = 0
    for t in toks:
        if re.fullmatch(r"\d{1,3}", t):
            n += 1
        else:
            break
    return [int(t) for t in toks[:n]], n


def first_appearance_order():
    order = []
    for name in BODY:
        for m in BRACKET.finditer((MANUSCRIPT / name).read_text(encoding="utf-8")):
            for seg in m.group(1).split(";"):
                for r in leading_refs(seg)[0]:
                    if r not in order:
                        order.append(r)
    return order


def rewrite_brackets(text, mp):
    def sub(m):
        inner = m.group(1)
        out = []
        for seg in inner.split(";"):
            refs, n = leading_refs(seg)
            if not refs:
                out.append(seg)
                continue
            if any(r not in mp for r in refs):
                sys.exit(f"unmapped reference in {m.group(0)!r}")
            new = [mp[r] for r in refs]
            toks = [t.strip() for t in seg.split(",")]
            rest = toks[n:]
            lead = " "if seg.startswith(" ") else ""
            if not rest:                      # a pure list: restore ascending order
                new = sorted(new)
            out.append(lead + ", ".join([str(x) for x in new] + rest))
        return "[" + ";".join(out) + "]"
    return BRACKET.sub(sub, text)


STRING_LITERAL = re.compile(r'"(?:[^"\\\n]|\\.)*"' + r"|'(?:[^'\\\n]|\\.)*'")


def rewrite_figure_script(mp):
    """The figures carry citation numbers in their labels.

    make_figures.py is Python, so a bare bracket rewrite would also hit list literals and
    subscripts -- `c.split("\u00b7")[0]` is not a citation. Only string literals are rewritten.
    """
    if not FIGURES.is_file():
        return
    t = FIGURES.read_text(encoding="utf-8")
    n = STRING_LITERAL.sub(lambda m: rewrite_brackets(m.group(0), mp), t)
    if n != t:
        FIGURES.write_text(n, encoding="utf-8")
        print(f"  rewrote {FIGURES.name} (regenerate the figures)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    order = first_appearance_order()
    bib = (MANUSCRIPT / BIB).read_text(encoding="utf-8")
    entries = {int(m.group(1)): m for m in ENTRY.finditer(bib)}
    defined = sorted(entries)

    missing = [r for r in order if r not in entries]
    uncited = [r for r in defined if r not in order]
    if missing:
        sys.exit(f"cited but not in the bibliography: {missing}")
    if uncited:
        sys.exit(f"in the bibliography but never cited in the manuscript: {uncited}\n"
                 "A supplement-only source belongs in the supplementary reference list.")

    mp = {old: new for new, old in enumerate(order, 1)}
    moved = {o: n for o, n in mp.items() if o != n}
    print(f"{len(mp)} references; {len(moved)} change number")
    for o in sorted(moved):
        print(f"  [{o}] -> [{mp[o]}]")
    if not a.apply:
        print("\n(dry run; pass --apply to rewrite)")
        return 0

    # --- bibliography: reorder, then remap the cross-references inside the entries
    blocks = {}
    starts = sorted(m.start() for m in entries.values())
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(bib)
        num = int(ENTRY.match(bib, s).group(1))
        blocks[num] = bib[s:e].rstrip("\n")
    head = bib[:starts[0]]
    out = [head.rstrip("\n") + "\n\n"]
    for new in range(1, len(mp) + 1):
        old = order[new - 1]
        body = ENTRY.sub("", blocks[old], count=1)
        out.append(f"[{new}] " + rewrite_brackets(body, mp) + "\n\n")
    (MANUSCRIPT / BIB).write_text("".join(out).rstrip("\n") + "\n", encoding="utf-8")

    # --- everything that cites
    for f in [MANUSCRIPT / n for n in BODY] + list(SUPPLEMENT):
        if f.name == "supplement_combined.md" or not f.is_file():
            continue
        t = f.read_text(encoding="utf-8")
        n = rewrite_brackets(t, mp)
        if n != t:
            f.write_text(n, encoding="utf-8")
            print(f"  rewrote {f.name}")
    rewrite_figure_script(mp)

    # The map is composed, not overwritten. It records stable source number -> display number,
    # and the numbers this run reads out of the manuscript are already display numbers from the
    # previous run. Rewriting the file from `mp` alone would silently redefine "stable" as
    # "whatever the last renumbering produced", and the internal registers would no longer be
    # reconcilable with the bibliography. Composing preserves the original identifiers.
    mapfile = DOC / "citation_display_map.csv"
    prev = {}
    if mapfile.is_file():
        with open(mapfile, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                prev[int(row["stable_source_number"])] = int(row["display_reference_number"])
    composed = {}
    if prev:
        for stable, disp in prev.items():
            if disp in mp:
                composed[stable] = mp[disp]
        # A reference added since the last renumbering has no stable number yet. It takes the
        # next free one, so the identifier space keeps growing rather than being reused.
        nxt = max(prev) + 1
        for disp in sorted(mp):
            if disp not in prev.values():
                composed[nxt] = mp[disp]
                print(f"  new stable source number {nxt} -> display [{mp[disp]}]")
                nxt += 1
    else:
        composed = dict(mp)

    inv = {old: new_ for new_, old in enumerate(order, 1)}
    with open(mapfile, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["stable_source_number", "display_reference_number", "first_author"])
        for stable in sorted(composed):
            disp = composed[stable]
            body = ENTRY.sub("", blocks[order[disp - 1]], count=1)
            w.writerow([stable, disp, body.split(",")[0].strip()])
    print(f"map written to {DOC.name}/citation_display_map.csv ({len(composed)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

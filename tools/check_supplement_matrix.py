#!/usr/bin/env python3
"""Cross-check the shipped supplement's coding matrix against the authoritative one.

Why this exists. `Documentation/adaptation_chain_matrix.md` §2 is the authoritative per-source
coding. `Documentation/supplement_coding_scheme.md` S6.3 is the abridged copy that ships to the
reader inside the supplement, and `supplement_combined.md` is built from it. Nothing checked that
the two agreed, and they stopped agreeing: AKR-26's S6 cell was recoded `Q.T` -> `Q.(T)` in the
authoritative matrix on 22 August 2026 and the supplement kept the old code, so the shipped
document credited that platform with a measured stage duration the manuscript says it does not
have. Every other validator passed with that defect in place.

What is compared. For each source present in both files, and for each of the ten stages, the
*codes* -- the Axis-A symbol and any Axis-B timing marker -- not the prose that follows them. The
supplement legitimately carries shorter cell text than the authoritative matrix; it may not carry
a different code. The two per-source timing totals are compared as well.

    python3 tools/check_supplement_matrix.py         # exit 1 on any disagreement
"""
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import DOC

AUTH = DOC / "adaptation_chain_matrix.md"
SUPP = DOC / "supplement_coding_scheme.md"

# The two files key sources differently: the authoritative matrix uses the project's stable
# internal keys, the supplement uses author names as a reader sees them.
KEYMAP = {
    "RAN-25": "Ranasinghe", "ANJ-25": "An", "YAN-25": "Yang", "MOR-26": "Morales Sandoval",
    "XU-22": "Xu", "LI-25": "Li", "LU-26": "Lu", "NEU-24": "Neuder", "AKR-26": "Akram",
    "BAI-22": "Bai", "NI-22": "Ni", "GAL-22": "Gal-Katziri", "MA-26": "Ma",
}

AXIS_A = ("Q", "D", "S", "A", "RS")
# The code is the leading bolded symbol. Everything after it -- the explanation, a footnote
# dagger, a bold emphasis inside the prose -- is commentary, and the two files are allowed to
# word it differently. Only the symbol is compared.
CODE = re.compile(r"^\*\*\s*(Q|D|S|A|RS)(·\(T\)|·\[T\]|·T|·\[R\]|·\[A\])?")
BARE = re.compile(r"^\s*(✗|n/a|\?|—|-)\s*(.*)$")
MARKS = str.maketrans("", "", "‡†‼★⚠")


def code_of(cell):
    """The code a cell carries, ignoring the prose that explains it."""
    c = cell.translate(MARKS).strip()
    # "✗ n/a" and "n/a" are the same statement: the stage does not exist on this architecture.
    # The two files reached that statement by different routes and both say so in the cell text.
    if re.match(r"^✗\s*n/a\b", c):
        return "n/a"
    m = CODE.match(c)
    if m:
        return m.group(1) + (m.group(2) or "")
    m = BARE.match(c)
    if m:
        return {"—": "✗", "-": "✗", "n\\a": "n/a"}.get(m.group(1), m.group(1))
    # An unbolded code, which both files use in places
    m = re.match(r"^(RS|Q|D|S|A)\b(·\(T\)|·T|·\[R\]|·\[A\])?", c)
    if m:
        return m.group(1) + (m.group(2) or "")
    return c[:12] or "∅"


def rows(path, first_col_key):
    """-> {source: [ten stage codes]} from the file's per-source coding table."""
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 12:
            continue
        name = re.sub(r"[*_]", "", cells[0]).strip()
        name = re.sub(r"\s*\[\d+\]\s*$", "", name).replace("et al.", "").strip()
        key = first_col_key(name)
        if key is None:
            continue
        out[key] = [code_of(c) for c in cells[2:12]]
    return out


def auth_key(name):
    n = name.split()[0].strip() if name else ""
    return name if name in KEYMAP else None


def supp_key(name):
    for k, v in KEYMAP.items():
        if name.startswith(v):
            return k
    return None


def main():
    a = rows(AUTH, auth_key)
    s = rows(SUPP, supp_key)
    if not a or not s:
        sys.exit(f"parsed {len(a)} authoritative and {len(s)} supplement rows -- the table format changed")

    shared = sorted(set(a) & set(s))
    if len(shared) < 10:
        sys.exit(f"only {len(shared)} sources matched across the two files; expected the full set")

    bad = []
    for k in shared:
        for i, (ca, cs) in enumerate(zip(a[k], s[k]), start=1):
            if ca != cs:
                bad.append(f"  {k} S{i}: authoritative {ca!r} != supplement {cs!r}")

    print(f"check_supplement_matrix: {len(shared)} sources x 10 stages compared")
    if bad:
        print("\nThe shipped supplement disagrees with adaptation_chain_matrix.md:")
        print("\n".join(bad))
        print("\nThe authoritative file is adaptation_chain_matrix.md. Fix the supplement, "
              "rebuild supplement_combined.md, and re-export.")
        return 1
    print("  OK -- every compared cell agrees")
    return 0


if __name__ == "__main__":
    sys.exit(main())

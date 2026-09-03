#!/usr/bin/env python3
"""Check two manuscript statements against the evidence they describe.

Why this exists. Both checks encode a defect that was actually shipped, and neither is
visible to any other validator: the manuscript can be internally consistent, render
cleanly and pass every count check while saying something the registers contradict.

F-16 -- the register count. Section 4.5 tells the reader how many entries the complete
timing register holds. From v0.24 until v0.30c it said "50-entry", and
`supplement_timing_register.md` has never held more than 35 numbered rows: the number was
a drafting error in a table caption, not a lost-rows defect. This check derives the count
from the register itself and requires the manuscript to state that number. It fails if
"50" is reintroduced while the register carries 35.

The G1 ... G4 rows are excluded from the count deliberately. They are absence rows, not
timing entries -- no value, no start-to-end interval, no source -- and they record the
quantities nothing in the reviewed set measures. They are keyed with a letter precisely so
that they stay outside the 1 ... 35 numbering the manuscript's Table 2 shares.

F-17 -- the fast-path evidence claim. Section 5.1 and the Conclusion said the fast path's
hardware capability was "measured on rigid panels that cannot bend". Table 3 attributes
the S4 embedded inference and the S5 control-transport share to the A3 externally deformed
*flexible* aperture, so the claim was false in the manuscript's own table. This check
refuses the exact phrase anywhere in active manuscript prose.

    python3 tools/check_manuscript_claims.py        # exit 1 on any failure
"""
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import DOC, MANUSCRIPT

REGISTER = DOC / "supplement_timing_register.md"
COUNT_CLAIM = re.compile(r"complete\s+(\d+)-entry register")
# Written out as well as in digits, because the pass records used the word form.
WORD_CLAIM = re.compile(r"complete\s+(fifty|thirty-five|forty)-entry register", re.I)
OBSOLETE = "rigid panels that cannot bend"

fails = []


def ck(label, ok, detail="", on_fail=""):
    """`detail` is evidence and prints either way; `on_fail` explains a failure only."""
    note = detail or (on_fail if not ok else "")
    if not ok and detail and on_fail:
        note = f"{detail}; {on_fail}"
    print(("[ OK ] " if ok else "[FAIL] ") + label + (f" -- {note}" if note else ""))
    if not ok:
        fails.append(label)


def numbered_rows(path):
    """Every table row whose first cell is a bare integer. Section headings have an empty
    first cell and the absence rows are keyed G1 ... G4, so both fall out here."""
    nums, gaps = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        first = line.strip().strip("|").split("|")[0].strip()
        if re.fullmatch(r"\d+", first):
            nums.append(int(first))
        elif re.fullmatch(r"G\d+", first):
            gaps.append(first)
    return nums, gaps


nums, gaps = numbered_rows(REGISTER)
n = len(nums)
ck("register has numbered rows", n > 0, f"{n} found in {REGISTER.name}")
ck("register numbering is contiguous from 1",
   nums == list(range(1, n + 1)),
   f"1 ... {max(nums) if nums else 0}, {len(set(nums))} distinct")
ck("absence rows are keyed outside the numbering", bool(gaps), " ".join(gaps) or "none")

# Every active manuscript section file. Archived snapshots are historical records and are
# deliberately not checked; they are corrected forward, not rewritten.
sections = sorted(MANUSCRIPT.glob("*.md"))
ck("manuscript sections found", bool(sections), f"{len(sections)} files")

stated = []
for f in sections:
    text = f.read_text(encoding="utf-8")
    for m in COUNT_CLAIM.finditer(text):
        stated.append((f.name, int(m.group(1)), m.group(0)))
    for m in WORD_CLAIM.finditer(text):
        stated.append((f.name, None, m.group(0)))

# The mirror's manuscript directory also holds `COMPLETE_MANUSCRIPT.md`, the generated
# concatenation of the sections, so the statement legitimately appears more than once
# there. What matters is that at least one exists and that every one of them agrees.
ck("manuscript states the register count",
   bool(stated), "; ".join(f"{a}: {c}" for a, _, c in stated) or "no statement found")

for name, value, phrase in stated:
    ck(f"stated count in {name} is a number, not a word",
       value is not None, phrase)
    if value is not None:
        ck(f"stated count in {name} matches the register",
           value == n, f"manuscript says {value}, register holds {n}")

for f in sections:
    ck(f"{f.name} does not claim the fast path is measured on rigid panels only",
       OBSOLETE not in f.read_text(encoding="utf-8"),
       on_fail=f'contains the obsolete phrase "{OBSOLETE}"')

print(f"\n{len(sections) + 5 + 2 * len(stated) - len(fails)} passed, {len(fails)} failed")
sys.exit(1 if fails else 0)

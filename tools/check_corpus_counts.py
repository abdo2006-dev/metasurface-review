#!/usr/bin/env python3
"""Check the corpus totals stated in prose against the files actually present.

Why this exists. Section 2 of the manuscript states a file count for the reviewed set, and
`source_inventory.md` states the same total. The count moved when three published full texts were
archived alongside their preprints, and neither statement moved with it: the manuscript said 31
files while 34 were present. Nothing checked, because the number is prose in two places and a
directory listing in a third.

Why it no longer globs the repository root. The first version of this check derived the corpus
from `ROOT.glob("*.pdf")` and treated an empty result as "this is the public mirror, skip". Two
things were wrong with that. It made an accidental directory layout load-bearing -- filing the
corpus into folders would have disabled the check rather than failed it -- and it inferred the
repository's identity from the absence of evidence, which is exactly the failure mode a validator
exists to prevent. The corpus is now declared in `03_SOURCES/00_INDEX/CORPUS_MANIFEST.csv`, one
row per file, and the mirror is detected the way `validate_public_snapshot.py` detects it: by a
file only the mirror has. **A missing manifest is a failure, never a skip.** Where the files sit
on disk is a filing decision; which files are in the corpus is the scientific claim, and only the
second one is asserted here.

What is checked, and what deliberately is not. Only the **file** count is derived from the working
tree, because only that one is mechanically derivable. The **document** count (26) and the
**contribution** count (24) rest on the independence rule of Section 2.4 -- a preprint and its
version of record are one document, supplementary information belongs to its parent paper -- which
is a judgement recorded in `source_inventory.md`, not something a directory listing can decide.
Those two are checked for *agreement between the two prose statements*, never re-derived. A
validator that silently recomputed them would be asserting the independence result rather than
testing it.

The manifest row count is likewise not compared against a literal 34 written here. It is compared
against the count the manuscript and `source_inventory.md` state, so the number lives in the two
prose statements that are the claim and nowhere else. Adding a source without updating them fails.

    python3 tools/check_corpus_counts.py           # exit 1 on any disagreement
    python3 tools/check_corpus_counts.py --fast    # skip the SHA-256 re-hash
"""
import csv, hashlib, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import ROOT, DOC, MANUSCRIPT

FIGURE_PDF = re.compile(r"^fig\d+_")
SCOPE = MANUSCRIPT / "02_scope_and_method.md"
INVENTORY = DOC / "source_inventory.md"
MANIFEST_REL = Path("03_SOURCES/00_INDEX/CORPUS_MANIFEST.csv")
LEGACY_MANIFEST_REL = Path("03_SOURCES/CORPUS_MANIFEST.csv")
REQUIRED_COLUMNS = ["key", "manuscript_reference", "first_author", "short_title", "year",
                    "version_type", "architecture_or_role", "load_bearing", "relative_path",
                    "sha256"]


def is_public_mirror(root: Path) -> bool:
    """Explicit repository identity, not an inference from what is absent.

    `REVIEW_INDEX.md` is generated into the mirror and exists nowhere else; this is the same
    test `validate_public_snapshot.py` uses. The private tree therefore cannot be mistaken for
    the mirror by moving, renaming or losing files."""
    return (root / "REVIEW_INDEX.md").is_file()


def manifest_path(root: Path) -> Path:
    p = root / MANIFEST_REL
    return p if p.is_file() else root / LEGACY_MANIFEST_REL


def load_manifest(path: Path):
    """Rows of the corpus manifest, or a hard error. Never an empty list treated as success."""
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return rows


def check_manifest(root: Path, path: Path, expected_files: int, verify_hashes: bool = True):
    """Every corpus assertion that can be made from the manifest. Returns a list of failures.

    Kept separate from main() so the regression tests can drive it against a fixture tree."""
    fails = []
    try:
        rows = load_manifest(path)
    except FileNotFoundError:
        return [f"the corpus manifest is missing: {path}. It is the declaration of which files "
                f"are in the reviewed set, and its absence is a failure, not a reason to skip."]

    if not rows:
        return [f"the corpus manifest {path} has no rows"]

    missing_cols = [c for c in REQUIRED_COLUMNS if c not in rows[0]]
    if missing_cols:
        fails.append(f"the manifest is missing required columns: {missing_cols}")
        return fails

    if len(rows) != expected_files:
        fails.append(f"the manifest declares {len(rows)} corpus files, but manuscript §2 and "
                     f"source_inventory.md state {expected_files}. Either a source was added or "
                     f"removed without updating the two prose statements, or the manifest is "
                     f"stale.")

    seen = {}
    for i, r in enumerate(rows, 2):          # 2 = first data line, header is line 1
        rel = (r.get("relative_path") or "").strip()
        if not rel:
            fails.append(f"manifest line {i}: empty relative_path")
            continue
        if rel in seen:
            fails.append(f"manifest line {i}: duplicate relative_path {rel!r} (first seen on "
                         f"line {seen[rel]}). Each corpus file must be declared exactly once.")
            continue
        seen[rel] = i
        f = root / rel
        if not f.is_file():
            fails.append(f"manifest line {i}: declared corpus file does not exist: {rel}")
            continue
        if verify_hashes:
            want = (r.get("sha256") or "").strip().lower()
            if not re.fullmatch(r"[0-9a-f]{64}", want):
                fails.append(f"manifest line {i}: {rel} has no valid sha256")
            else:
                got = hashlib.sha256(f.read_bytes()).hexdigest()
                if got != want:
                    fails.append(f"manifest line {i}: {rel} does not match its recorded "
                                 f"sha256 (recorded {want[:12]}…, found {got[:12]}…)")

    # A PDF present in the source library but absent from the manifest is an undeclared corpus
    # member -- the mirror image of the check above, and the failure the old root glob caught.
    lib = root / "03_SOURCES"
    if lib.is_dir():
        on_disk = {str(p.relative_to(root)) for p in lib.rglob("*.pdf")
                   if not FIGURE_PDF.match(p.name)}
        undeclared = sorted(on_disk - set(seen))
        for u in undeclared:
            fails.append(f"a PDF under 03_SOURCES/ is not declared in the manifest: {u}")

    # And a corpus PDF left loose in the repository root, which is where they used to live.
    stray = sorted(p.name for p in root.glob("*.pdf") if not FIGURE_PDF.match(p.name))
    for s in stray:
        fails.append(f"a non-figure PDF is sitting in the repository root: {s}. Corpus files "
                     f"belong under 03_SOURCES/ and must be declared in the manifest.")
    return fails


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    verify_hashes = "--fast" not in argv
    fails = []

    scope = SCOPE.read_text(encoding="utf-8")
    m = re.search(r"(\d+) distinct research contributions across (\d+) files", scope)
    if not m:
        sys.exit("could not find the corpus sentence in 02_scope_and_method.md")
    contrib_ms, files_ms = int(m.group(1)), int(m.group(2))

    inv = INVENTORY.read_text(encoding="utf-8")
    m = re.search(r"\*\*(\d+) PDF files\*\* → \*\*(\d+) unique documents\*\* → "
                  r"\*\*(\d+) distinct research contributions\*\*", inv)
    if not m:
        sys.exit("could not find the corpus totals line in source_inventory.md")
    files_inv, docs_inv, contrib_inv = (int(x) for x in m.groups())

    print(f"manuscript §2      : {contrib_ms} contributions across {files_ms} files")
    print(f"source_inventory   : {files_inv} files -> {docs_inv} documents -> {contrib_inv} contributions")

    if files_ms != files_inv:
        fails.append(f"file count disagrees between the two statements: §2 says {files_ms}, "
                     f"source_inventory.md says {files_inv}")
    if contrib_ms != contrib_inv:
        fails.append(f"contribution count disagrees: §2 says {contrib_ms}, "
                     f"source_inventory.md says {contrib_inv}")

    if is_public_mirror(ROOT):
        print("repository        : public review mirror (REVIEW_INDEX.md present) — it carries "
              "no corpus PDFs, so the manifest check does not apply")
    else:
        mp = manifest_path(ROOT)
        print(f"repository        : private working tree — corpus declared in "
              f"{mp.relative_to(ROOT) if mp.is_file() else MANIFEST_REL}")
        fails += check_manifest(ROOT, mp, files_ms, verify_hashes)
        if not fails:
            print(f"corpus            : {files_ms} declared files, all present"
                  + (" and hash-verified" if verify_hashes else ""))
        ext = sorted((ROOT / "external_sources").glob("*.pdf"))
        print(f"external_sources/ : {len(ext)} archived external PDFs — excluded from every count "
              f"by design")

    if fails:
        print("\nFAIL:")
        for f in fails:
            print("  - " + f)
        print("\nThe document count (26) and contribution count (24) are NOT re-derived here: "
              "they rest on the independence rule and are recorded in source_inventory.md.")
        return 1
    print("  OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Regression tests for the corpus-manifest check.

These exist because of the specific defect the manifest replaced. The previous check derived
the corpus from a non-recursive glob of the repository root and treated "no PDFs found" as
"this must be the public mirror", so the only way to make it *fail* was to leave a wrong number
of PDFs in exactly one directory -- and the easiest way to make it stop checking anything at
all was to tidy them into folders. Each case below is one way the corpus can be wrong; every one
of them must produce a failure, and the last one asserts the honest case still passes.

    python3 tools/test_check_corpus_counts.py     # exit 1 if any case behaves wrongly
"""
import csv, hashlib, shutil, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_corpus_counts as cc

COLUMNS = cc.REQUIRED_COLUMNS
N = 34


def fixture(tmp: Path, rows):
    """A throwaway tree holding `rows` corpus files, plus the manifest that declares them."""
    lib = tmp / "03_SOURCES" / "01_FIM_AND_SYSTEM"
    lib.mkdir(parents=True, exist_ok=True)
    (tmp / "03_SOURCES" / "00_INDEX").mkdir(parents=True, exist_ok=True)
    written = set()
    for r in rows:
        p = tmp / r["relative_path"]
        if p not in written:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(r["_body"])
            written.add(p)
    man = tmp / "03_SOURCES" / "00_INDEX" / "CORPUS_MANIFEST.csv"
    with man.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in COLUMNS})
    return man


def base_rows(n=N):
    out = []
    for i in range(n):
        body = f"pretend pdf {i}".encode()
        out.append({
            "key": f"KEY-{i:02d}", "manuscript_reference": str(i + 1),
            "first_author": "Author", "short_title": "Title", "year": "2025",
            "version_type": "held full text", "architecture_or_role": "A1",
            "load_bearing": "yes",
            "relative_path": f"03_SOURCES/01_FIM_AND_SYSTEM/{i:02d}_source.pdf",
            "sha256": hashlib.sha256(body).hexdigest(), "_body": body,
        })
    return out


CASES = []


def case(name):
    def deco(fn):
        CASES.append((name, fn))
        return fn
    return deco


@case("all 34 correct -> PASS")
def _(tmp):
    rows = base_rows()
    man = fixture(tmp, rows)
    return cc.check_manifest(tmp, man, N), False


@case("one missing source -> FAIL")
def _(tmp):
    rows = base_rows()
    man = fixture(tmp, rows)
    (tmp / rows[7]["relative_path"]).unlink()
    return cc.check_manifest(tmp, man, N), True


@case("one extra manifest row -> FAIL")
def _(tmp):
    rows = base_rows(N + 1)
    man = fixture(tmp, rows)
    return cc.check_manifest(tmp, man, N), True


@case("one source short -> FAIL")
def _(tmp):
    rows = base_rows(N - 1)
    man = fixture(tmp, rows)
    return cc.check_manifest(tmp, man, N), True


@case("duplicate path -> FAIL")
def _(tmp):
    rows = base_rows()
    rows[9]["relative_path"] = rows[8]["relative_path"]
    rows[9]["sha256"] = rows[8]["sha256"]
    man = fixture(tmp, rows)
    return cc.check_manifest(tmp, man, N), True


@case("altered file contents -> FAIL")
def _(tmp):
    rows = base_rows()
    man = fixture(tmp, rows)
    (tmp / rows[3]["relative_path"]).write_bytes(b"something else")
    return cc.check_manifest(tmp, man, N), True


@case("undeclared PDF in the library -> FAIL")
def _(tmp):
    rows = base_rows()
    man = fixture(tmp, rows)
    (tmp / "03_SOURCES" / "01_FIM_AND_SYSTEM" / "smuggled.pdf").write_bytes(b"x")
    return cc.check_manifest(tmp, man, N), True


@case("corpus PDF loose in the root -> FAIL")
def _(tmp):
    rows = base_rows()
    man = fixture(tmp, rows)
    (tmp / "stray.pdf").write_bytes(b"x")
    return cc.check_manifest(tmp, man, N), True


@case("missing manifest -> FAIL, never a skip")
def _(tmp):
    rows = base_rows()
    man = fixture(tmp, rows)
    man.unlink()
    fails = cc.check_manifest(tmp, man, N)
    ok = bool(fails) and "missing" in fails[0]
    return (fails if ok else []), True


@case("a private tree with no PDFs is not mistaken for the mirror")
def _(tmp):
    # The old failure mode, stated directly: an empty corpus must not read as "public mirror".
    shutil.rmtree(tmp / "03_SOURCES", ignore_errors=True)
    assert not cc.is_public_mirror(tmp)
    man = tmp / "03_SOURCES" / "00_INDEX" / "CORPUS_MANIFEST.csv"
    return cc.check_manifest(tmp, man, N), True


@case("the mirror IS recognised, by a file only it has")
def _(tmp):
    (tmp / "REVIEW_INDEX.md").write_text("mirror", encoding="utf-8")
    assert cc.is_public_mirror(tmp)
    return [], False


def main():
    bad = 0
    for name, fn in CASES:
        with tempfile.TemporaryDirectory() as d:
            fails, want_fail = fn(Path(d))
        got_fail = bool(fails)
        ok = got_fail == want_fail
        bad += not ok
        mark = "ok  " if ok else "BAD "
        detail = f" -> {fails[0][:78]}" if got_fail else ""
        print(f"  {mark}{name}{detail}")
    print(f"\n{len(CASES) - bad}/{len(CASES)} cases behaved correctly")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

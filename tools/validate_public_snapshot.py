#!/usr/bin/env python3
"""Portability and integrity smoke test for the sanitized public review mirror.

Runs entirely from the mirror, offline except where noted, and asserts that the
artifact actually supports the reproducibility claims the manuscript makes for it.

The v0.22 mirror passed every check that was performed on it and still failed for an
independent reviewer, because the checks were performed on macOS. Everything here is
case-exact and must pass on a case-sensitive Linux checkout.

  python3 tools/validate_public_snapshot.py            # offline checks
  python3 tools/validate_public_snapshot.py --network  # also re-run live retrieval
"""
import argparse, csv, importlib.util, os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAIL, OK = [], []


def check(name, cond, detail=""):
    (OK if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    return cond


def listdir_exact(p: Path):
    """Real on-disk names, so a case-insensitive filesystem cannot mask a wrong case."""
    return set(os.listdir(p))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--network", action="store_true")
    a = ap.parse_args()
    is_mirror = (ROOT / "REVIEW_INDEX.md").is_file()

    print("A. PATHS AND EXACT CASE")
    top = listdir_exact(ROOT)
    if is_mirror:
        for d in ("documentation", "manuscript", "tools"):
            check(f"{d}/ exists with exact lowercase name", d in top,
                  f"found: {sorted(x for x in top if x.lower()==d)}")
        check("no capitalised Documentation/ in mirror", "Documentation" not in top)
    else:
        print("  (private working tree — mirror-only case checks skipped)")
    sys.path.insert(0, str(ROOT / "tools"))
    import _paths
    check("tools/_paths.py resolves the documentation directory", _paths.DOC.is_dir(),
          str(_paths.DOC.name))
    check("tools/_paths.py resolves the manuscript directory", _paths.MANUSCRIPT.is_dir())

    print("\nA2. NO WRONG-CASE PATH IN ANY SHIPPED TOOL")
    NOT_SHIPPED = {"_paths.py", "sync_review_repo.py", "check_s11_consistency.py", "validate_public_snapshot.py"}
    offenders = []
    for t in sorted((ROOT / "tools").glob("*.py")):
        if t.name in NOT_SHIPPED:
            continue
        if re.search(r'["\'](Documentation|Manuscript)["\']', t.read_text(encoding="utf-8")):
            offenders.append(t.name)
    check("no shipped tool hardcodes Documentation/ or Manuscript/", not offenders, str(offenders))

    print("\nB. OFFLINE DERIVATIONS EXECUTE")
    for script in ("c1_stage_counts.py", "s11_counts.py", "check_s11_consistency.py"):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / script)],
                           capture_output=True, text=True)
        check(f"tools/{script} exits 0", r.returncode == 0,
              (r.stderr.strip().splitlines() or [""])[-1][:120])
    with tempfile.TemporaryDirectory():
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "build_s11_study_register.py")],
                           capture_output=True, text=True)
        check("tools/build_s11_study_register.py regenerates the register", r.returncode == 0)
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "build_forward_citation_csv.py"), "--check"],
                       capture_output=True, text=True)
    check("build_forward_citation_csv.py --check reproduces the decision table",
          r.returncode == 0, (r.stdout.strip().splitlines() or [""])[-1][:120])

    print("\nC. EXPECTED CURRENT VALUES")
    from s11_counts import counts
    c = counts()
    r_, ac, ro, c1 = c["retrieval"], c["access"], c["roles"], c["c1"]
    for label, got, want in [
        ("C1 max Q", c1["max_quantitative"], 6),
        # 4, not 5: the v0.24 taxonomy rebuild reclassified LI-25's S2 RMSD as an
        # accuracy rather than timing evidence. This assertion still carried the
        # pre-v0.24 value and would have failed CI on the first push after v0.24.
        ("C1 max measured stage durations T", c1["max_fully_delimited_T"], 4),
        ("C1 max T+(T)", c1["max_any_timing"], 6),
        ("S11 records", r_["records_pre_dedup"], 306),
        ("S11 unique works", r_["unique_works"], 262),
        ("S11 stage-1", r_["stage1_pass"], 65),
        ("S11 stage-2 records", r_["stage2_records"], 24),
        ("S11 distinct studies", r_["distinct_studies"], 20),
        ("S11 studies read", ac["studies_read"], 13),
        ("S11 studies unread", ac["studies_unread"], 7),
        ("propagation studies", ro["propagation_studies"], 4),
        ("no-timing studies", ro["no_timing_studies"], 9),
    ]:
        check(f"{label} = {want}", got == want, f"got {got}")
    check("T-max source is BAI-22 alone", c1["sources_at_max_fully_delimited_T"] == ["BAI-22"],
          str(c1["sources_at_max_fully_delimited_T"]))
    check("T+(T)-max source is LI-25 alone",
          sorted(c1["sources_at_max_any_timing"]) == ["LI-25"],
          str(c1["sources_at_max_any_timing"]))
    check("read studies partition into propagation + no-timing",
          ro["propagation_studies"] + ro["no_timing_studies"] == ac["studies_read"],
          f"{ro['propagation_studies']}+{ro['no_timing_studies']}={ac['studies_read']}")

    print("\nD. SCREENING EXPRESSION")
    print(f"  len(WIRELESS_TERMS) = {c['regex']['wireless_alternatives']}  "
          f"(reported from code, never hardcoded)")
    print(f"  len(TIMING_TERMS)   = {c['regex']['timing_alternatives']}")
    check("no active document claims a different alternative count",
          subprocess.run([sys.executable, str(ROOT / "tools" / "check_s11_consistency.py")],
                         capture_output=True).returncode == 0)

    print("\nE. OBSOLETE FILENAMES AND SCIENTIFIC STATE")
    doc_names = listdir_exact(_paths.DOC)
    check("forward_citation_stage1_raw.csv is gone",
          "forward_citation_stage1_raw.csv" not in doc_names)
    rows = list(csv.DictReader(open(_paths.DECISIONS, encoding="utf-8")))
    s2 = [r for r in rows if r["stage2_system_paper"] == "yes"]
    fams = {r["version_family"] for r in s2}
    check("retired F-ANJ-C / F-ANJ-J split absent",
          not ({"F-ANJ-C", "F-ANJ-J"} & fams))
    check("F-ANJ-DL present", "F-ANJ-DL" in fams)
    check("retired 'counterexample' role absent from the decision table",
          not any(r["final_role"] == "counterexample" for r in s2))
    # Behavioural, not textual: the only scientific content any tool can emit now comes
    # from the manual-decision table, so that is what must be clean. The builder carries
    # its own guards and exits non-zero if a retired family or role ever reappears.
    man = _paths.DOC / "s11_manual_decisions.csv"
    check("manual-decision table exists (science separated from code)", man.is_file())
    if man.is_file():
        mrows = list(csv.DictReader(open(man, encoding="utf-8")))
        mfam = {r["version_family"] for r in mrows if r["stage2_system_paper"] == "yes"}
        mrole = {r["final_role"] for r in mrows if r["stage2_system_paper"] == "yes"}
        check("manual-decision table carries no retired family",
              not ({"F-ANJ-C", "F-ANJ-J"} & mfam))
        check("manual-decision table carries no retired role",
              "counterexample" not in mrole, str(sorted(mrole)))
    check("no shipped tool embeds a version-family assignment table",
          not any(re.search(r'^\s*["\']F-[A-Z-]+["\']\s*:', t2.read_text(encoding="utf-8"), re.M)
                  for t2 in (ROOT / "tools").glob("*.py")))

    print("\nF. RELATIVE MARKDOWN LINKS")
    lc = ROOT / "tools" / "check_mirror_links.py"
    if lc.is_file():
        r = subprocess.run([sys.executable, str(lc), str(ROOT)], capture_output=True, text=True)
        check("zero broken relative links", r.returncode == 0,
              (r.stdout.strip().splitlines() or [""])[-1][:90])

    print("\nG. MANIFEST")
    man = ROOT / "review" / "REVIEW_MANIFEST.md"
    if man.is_file():
        paths = [m.group(1) for m in
                 re.finditer(r"^\| `([^`]+)` \|", man.read_text(encoding="utf-8"), re.M)]
        dupes = sorted({p for p in paths if paths.count(p) > 1})
        check("manifest paths are unique", not dupes, str(dupes))
        missing = [p for p in paths if not (ROOT / p).exists()]
        check("every manifest path exists", not missing, str(missing[:5]))
    else:
        print("  (no manifest in this tree — mirror-only check)")

    if a.network:
        print("\nH. LIVE RETRIEVAL (network)")
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "retrieve_306_records.py")],
                           capture_output=True, text=True)
        check("live retrieval reproduces 306 records / 262 works",
              "Matches the recorded snapshot exactly" in r.stdout,
              (r.stdout.strip().splitlines() or [""])[-1][:90])

    print(f"\n{'='*60}\n{len(OK)} passed, {len(FAIL)} failed")
    if FAIL:
        for f in FAIL:
            print(f"  FAILED: {f}")
        return 1
    print("PUBLIC SNAPSHOT VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())

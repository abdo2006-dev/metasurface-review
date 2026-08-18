#!/usr/bin/env python3
"""
Reproduce search S11 -- the forward citation search behind manuscript contribution C3.

WHAT THIS SCRIPT DOES REPRODUCE, AUTOMATICALLY AND EXACTLY
    1. Retrieval of every work citing the three primary hardware sources, from the
       OpenAlex citation graph.
    2. Deduplication to unique works.
    3. Stage-1 title+abstract screening against an EXACT regular expression, given
       in full below with no elision.

WHAT THIS SCRIPT CANNOT REPRODUCE
    4. Stage-2 manual screening (wireless-relevant -> flexible-metasurface or
       reconfigurable-surface *system* paper). This is a human judgement.
    5. Full-text extraction, which requires the full texts. Seven of the twenty
       stage-2 papers are behind publisher paywalls and were never read; no
       paywall was circumvented, and every count is therefore a LOWER BOUND.

    Decisions 4 and 5 are not hidden inside this script. They are recorded, one row
    per work, in `Documentation/forward_citation_search_results.csv`, which this
    script reads back and joins against the live API result so that any divergence
    between the recorded screening and a fresh retrieval is reported rather than
    silently absorbed.

USAGE
    python3 tools/reproduce_forward_citation_search.py                # retrieve + screen + compare
    python3 tools/reproduce_forward_citation_search.py --write-csv OUT # emit a fresh stage-1 CSV skeleton

NOTE ON DRIFT
    The citation graph grows. Re-running this later will return MORE citing works
    than the 18 August 2026 run. That is expected and is not an error; the script
    reports the delta explicitly. The recorded CSV is a snapshot of the screened
    set as of the stated date.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import ROOT, DOC, MANUSCRIPT, DECISIONS, WORKS, RECORDS, REGISTER, MATRIX
import argparse
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CSV_PATH = DECISIONS

SEARCH_DATE = "2026-08-18"
OPENALEX = "https://api.openalex.org/works"
# OpenAlex asks for a contact address in the polite pool. Replace with your own.
MAILTO = "metasurface-review@example.org"

# ---------------------------------------------------------------------------
# EXACT seed set. These are the three primary hardware sources whose forward
# citations are traced. Keys are the project's internal source keys.
# ---------------------------------------------------------------------------
SEEDS = {
    "BAI": {
        "openalex": "W4296552404",
        "doi": "10.1038/s41586-022-05061-w",
        "cite": "Bai et al., Nature 609(7928):701-708, 2022",
    },
    "NI": {
        "openalex": "W4297022396",
        "doi": "10.1038/s41467-022-31092-y",
        "cite": "Ni et al., Nature Communications 13:5576, 2022",
    },
    "LI": {
        "openalex": "W4409148742",
        "doi": "10.1038/s41467-025-58249-9",
        "cite": "Li et al., Nature Communications 16:3161, 2025",
    },
}

# ---------------------------------------------------------------------------
# EXACT stage-1 screening regular expression. NO ELLIPSIS.
#
# Applied case-insensitively to (title + " " + reconstructed abstract).
# A work passes stage 1 if AT LEAST ONE alternative matches.
#
# This is a deliberately RECALL-ORIENTED screen: it is meant to over-include, so
# that the precision step is the human one recorded in the CSV. A term is in this
# list if it would appear in the title or abstract of a wireless/communications
# paper that might cite mechanical-metasurface hardware.
# ---------------------------------------------------------------------------
WIRELESS_TERMS = [
    r"reconfigurable intelligent surface(?:s)?",
    r"intelligent reflecting surface(?:s)?",
    r"intelligent omni-?surface(?:s)?",
    r"\bRIS\b",
    r"\bIRS\b",
    r"metasurface(?:s)?",
    r"meta-?atom(?:s)?",
    r"reflectarray(?:s)?",
    r"transmitarray(?:s)?",
    r"\bMIMO\b",
    r"\bMISO\b",
    r"\bSISO\b",
    r"beamforming",
    r"beam-?steering",
    r"beam-?forming",
    r"precoding",
    r"\bISAC\b",
    r"integrated sensing and communication(?:s)?",
    r"joint communication and sensing",
    r"channel estimation",
    r"channel state information",
    r"\bCSI\b",
    r"movable antenna(?:s)?",
    r"fluid antenna(?:s)?",
    r"flexible intelligent metasurface(?:s)?",
    r"\bFIM\b",
    r"wireless communication(?:s)?",
    r"wireless network(?:s)?",
    r"wireless channel(?:s)?",
    r"millimet(?:er|re)[- ]wave",
    r"\bmmWave\b",
    r"terahertz communication(?:s)?",
    r"\b6G\b",
    r"\b5G\b",
    r"antenna array(?:s)?",
    r"phased array(?:s)?",
    r"base station(?:s)?",
    r"spectral efficiency",
    r"sum[- ]rate",
    r"achievable rate",
    r"\bDoppler\b",
    r"coherence time",
    r"coherence block(?:s)?",
    r"path loss",
    r"signal[- ]to[- ]noise ratio",
    r"\bSNR\b",
]
WIRELESS_RE = re.compile("|".join(WIRELESS_TERMS), re.IGNORECASE)

# ---------------------------------------------------------------------------
# EXACT timing-terminology extraction expression, applied to FULL TEXT (not to
# abstracts -- an abstract-level scan of all stage-1 survivors returned ZERO
# timing mentions, which is precisely why full-text access bounds this search).
#
# Full texts are NOT retrieved by this script. The expression is recorded here so
# that the extraction step is reproducible by anyone who has the texts.
#
# Before matching, full text MUST be normalised:
#   - ligatures:  ﬁ -> "fi",  ﬂ -> "fl"   (PDF extraction emits these as
#     single glyphs, which silently defeats a naive search for "fi"/"fl")
#   - hyphenated line breaks:  "-\n" -> ""
# ---------------------------------------------------------------------------
TIMING_TERMS = [
    r"morphing period",
    r"morphing time",
    r"morphing speed",
    r"switching speed",
    r"switching time",
    r"response time",
    r"reconfiguration time",
    r"deformation response",
    r"reconfigurability rate",
    r"millisecond(?:s)?",
    r"\d+(?:\.\d+)?\s*ms\b",
    r"\d+(?:\.\d+)?\s*milliseconds?\b",
    r"0\.\d+\s*s\b",
]
TIMING_RE = re.compile("|".join(TIMING_TERMS), re.IGNORECASE)

LIGATURES = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff",
             "ﬃ": "ffi", "ﬄ": "ffl"}


def normalise(text: str) -> str:
    """Mandatory normalisation before any full-text term search."""
    for lig, repl in LIGATURES.items():
        text = text.replace(lig, repl)
    return text.replace("-\n", "")


def fetch_json(url: str, tries: int = 4):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": f"metasurface-review ({MAILTO})"})
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except Exception as exc:  # noqa: BLE001
            if attempt == tries - 1:
                raise
            print(f"  retry {attempt + 1} after {exc}", file=sys.stderr)
            time.sleep(2 * (attempt + 1))
    return None


def reconstruct_abstract(inv_index):
    """OpenAlex stores abstracts as an inverted index. Rebuild the word order."""
    if not inv_index:
        return ""
    positions = []
    for word, idxs in inv_index.items():
        for i in idxs:
            positions.append((i, word))
    positions.sort()
    return " ".join(w for _, w in positions)


def retrieve_citing(seed_id: str):
    """EXACT query: GET /works?filter=cites:{ID}&per-page=200&cursor=* , paginated."""
    out, cursor = [], "*"
    while cursor:
        params = urllib.parse.urlencode({
            "filter": f"cites:{seed_id}",
            "per-page": "200",
            "cursor": cursor,
            "mailto": MAILTO,
            "select": "id,doi,title,publication_year,authorships,primary_location,ids",
        })
        data = fetch_json(f"{OPENALEX}?{params}")
        out.extend(data.get("results", []))
        cursor = data.get("meta", {}).get("next_cursor")
        if not data.get("results"):
            break
    return out


def retrieve_abstracts(work_ids):
    """Second pass for abstracts (kept separate so the id/title pass stays small)."""
    abstracts = {}
    ids = list(work_ids)
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        params = urllib.parse.urlencode({
            "filter": "openalex_id:" + "|".join(chunk),
            "per-page": "50",
            "mailto": MAILTO,
            "select": "id,abstract_inverted_index",
        })
        data = fetch_json(f"{OPENALEX}?{params}")
        for w in data.get("results", []):
            abstracts[w["id"].rsplit("/", 1)[-1]] = reconstruct_abstract(
                w.get("abstract_inverted_index"))
    return abstracts


def short_id(work):
    return work["id"].rsplit("/", 1)[-1]


def run():
    print(f"Forward citation search S11 -- live retrieval (recorded run: {SEARCH_DATE})\n")

    # ---- 1. retrieval -----------------------------------------------------
    by_id, seeds_for = {}, {}
    for key, seed in SEEDS.items():
        works = retrieve_citing(seed["openalex"])
        print(f"  seed {key} ({seed['openalex']}, {seed['doi']}): {len(works)} citing records")
        for w in works:
            wid = short_id(w)
            by_id[wid] = w
            seeds_for.setdefault(wid, set()).add(key)

    total_records = sum(len(seeds_for[w]) for w in seeds_for)
    print(f"\n  total citing records (with duplicates): {total_records}")
    print(f"  unique works after deduplication by OpenAlex ID: {len(by_id)}")

    # ---- 2. stage-1 screening --------------------------------------------
    abstracts = retrieve_abstracts(by_id.keys())
    passed = []
    for wid, w in by_id.items():
        blob = f"{w.get('title') or ''} {abstracts.get(wid, '')}"
        if WIRELESS_RE.search(blob):
            passed.append(wid)
    print(f"  stage-1 (regex on title+abstract) wireless-relevant: {len(passed)}")

    # ---- 3. compare against the recorded snapshot -------------------------
    if not CSV_PATH.exists():
        print(f"\n  no recorded CSV at {CSV_PATH}; run with --write-csv to create a skeleton.")
        return by_id, seeds_for, abstracts, passed

    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        recorded = list(csv.DictReader(fh))
    rec_ids = {r["openalex_id"] for r in recorded}
    rec_stage1 = {r["openalex_id"] for r in recorded if r["stage1_regex_pass"] == "yes"}
    rec_stage2 = {r["openalex_id"] for r in recorded if r["stage2_system_paper"] == "yes"}
    rec_full = {r["openalex_id"] for r in recorded if r["full_text_inspected"] == "yes"}
    rec_prop = {r["openalex_id"] for r in recorded if r["final_role"] == "propagation"}

    print(f"\n  recorded snapshot ({SEARCH_DATE}): {len(recorded)} unique works, "
          f"{len(rec_stage1)} stage-1, {len(rec_stage2)} stage-2 system papers, "
          f"{len(rec_full)} full texts inspected, {len(rec_prop)} propagation cases")

    new_works = set(by_id) - rec_ids
    gone = rec_ids - set(by_id)
    print(f"\n  DRIFT vs recorded snapshot:")
    print(f"    works present now but not in the snapshot: {len(new_works)}")
    print(f"    works in the snapshot but not returned now: {len(gone)}")
    if new_works:
        print("    (expected -- the citation graph grows. Re-screening these is the"
              "\n     natural way to extend the audit; every recorded count is a lower bound.)")
    return by_id, seeds_for, abstracts, passed


def write_csv(path, by_id, seeds_for, abstracts, passed):
    passed_set = set(passed)
    fields = ["openalex_id", "doi", "arxiv_id", "title", "year", "cited_seeds",
              "stage1_regex_pass", "stage2_system_paper", "exclusion_reason",
              "full_text_inspected", "full_text_source", "timing_terminology_hit",
              "propagation_case_id", "author_network_status", "final_role"]
    with Path(path).open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for wid, work in sorted(by_id.items()):
            doi = (work.get("doi") or "").replace("https://doi.org/", "")
            w.writerow({
                "openalex_id": wid,
                "doi": doi,
                "arxiv_id": "",
                "title": (work.get("title") or "").replace("\n", " "),
                "year": work.get("publication_year") or "",
                "cited_seeds": "|".join(sorted(seeds_for.get(wid, []))),
                "stage1_regex_pass": "yes" if wid in passed_set else "no",
                "stage2_system_paper": "", "exclusion_reason": "",
                "full_text_inspected": "", "full_text_source": "",
                "timing_terminology_hit": "", "propagation_case_id": "",
                "author_network_status": "", "final_role": "",
            })
    print(f"\n  wrote stage-1 skeleton to {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-csv", metavar="OUT", default=None)
    args = ap.parse_args()
    result = run()
    if args.write_csv and result:
        write_csv(args.write_csv, *result)

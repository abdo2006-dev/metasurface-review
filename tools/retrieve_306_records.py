#!/usr/bin/env python3
"""Retrieve the PRE-DEDUPLICATION seed-wise citing-record set (the "306 records").

Distinction this script exists to make explicit:

  * a RECORD is one (seed, citing work) pair. A work citing two of the three
    seeds contributes two records. This is the raw retrieval.
  * a WORK is one OpenAlex work id. Collapsing records by work id gives the
    deduplicated work-level set that stage-1 screening is applied to.

Output: Documentation/forward_citation_records_raw.csv, one row per record,
in retrieval order, with no screening columns. This is the artifact the
manuscript's "306 records" refers to.
"""
import csv, json, sys, time, urllib.parse, urllib.request
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "Documentation"
OPENALEX = "https://api.openalex.org/works"
MAILTO = "abdo.studyy@gmail.com"

SEEDS = {
    "BAI": {"openalex": "W4296552404", "doi": "10.1038/s41586-022-05061-w"},
    "NI":  {"openalex": "W4297022396", "doi": "10.1038/s41467-022-31092-y"},
    "LI":  {"openalex": "W4409148742", "doi": "10.1038/s41467-025-58249-9"},
}


def fetch_json(url, tries=4):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": f"metasurface-review (mailto:{MAILTO})"})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            if a == tries - 1:
                raise
            time.sleep(2 * (a + 1))


def retrieve_citing(seed_id):
    """EXACT query: GET /works?filter=cites:{ID}&per-page=200&cursor=* , paginated."""
    out, cursor = [], "*"
    while cursor:
        q = urllib.parse.urlencode({"filter": f"cites:{seed_id}", "per-page": "200",
                                    "cursor": cursor, "mailto": MAILTO})
        data = fetch_json(f"{OPENALEX}?{q}")
        out.extend(data.get("results", []))
        cursor = data.get("meta", {}).get("next_cursor")
        time.sleep(0.2)
    return out


def main():
    records = []
    per_seed = {}
    for key, seed in SEEDS.items():
        works = retrieve_citing(seed["openalex"])
        per_seed[key] = len(works)
        print(f"  seed {key} ({seed['openalex']}): {len(works)} citing records")
        for w in works:
            wid = (w.get("id") or "").rsplit("/", 1)[-1]
            records.append({
                "record_seed": key,
                "seed_openalex_id": seed["openalex"],
                "seed_doi": seed["doi"],
                "openalex_id": wid,
                "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
                "title": (w.get("title") or "").replace("\n", " "),
                "year": w.get("publication_year") or "",
                "publication_date": w.get("publication_date") or "",
                "type": w.get("type") or "",
            })
    n_records = len(records)
    n_works = len({r["openalex_id"] for r in records})
    print(f"\nRECORDS (pre-deduplication, seed-wise): {n_records}")
    print(f"WORKS   (deduplicated by OpenAlex id)  : {n_works}")
    print(f"per-seed: {per_seed}")

    out = DOC / "forward_citation_records_raw.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(records[0].keys()))
        w.writeheader()
        w.writerows(records)
    print(f"wrote {out.name}: {n_records} rows")

    # drift report against the figures the manuscript records
    RECORDED_RECORDS, RECORDED_WORKS = 306, 262
    if n_records != RECORDED_RECORDS or n_works != RECORDED_WORKS:
        print(f"\n*** DRIFT vs recorded snapshot: records {RECORDED_RECORDS}->{n_records}, "
              f"works {RECORDED_WORKS}->{n_works}. The recorded snapshot is NOT overwritten; "
              f"report the drift.")
    else:
        print(f"\nMatches the recorded snapshot exactly: {RECORDED_RECORDS} records / {RECORDED_WORKS} works.")


if __name__ == "__main__":
    main()

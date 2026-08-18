# Reproducibility scripts

These are the scripts the manuscript refers to. They are published so that the
forward citation search (Section 2.3, Section 8.5) can be re-executed, and so that
every S11 and C1 count can be re-derived rather than taken on trust.

Python 3.9+. Only the standard library is required — no third-party packages, no
API key, no authentication. Network access to `api.openalex.org` is needed for the
two retrieval scripts; the rest work offline against the committed CSVs.

## What is exactly reproducible, and what is not

| Stage | Script | Status |
|---|---|---|
| Seed-wise citing-record retrieval (306 records) | `retrieve_306_records.py` | **automatic and exact** |
| Deduplication to works (262) and stage-1 screening (65) | `reproduce_forward_citation_search.py` | **automatic and exact** — the 47-alternative expression is written out in full, with no ellipsis |
| Stage-2 system-study screening (24 records) | — | **manual**, recorded per work in the CSV with a reason; auditable, not re-derivable |
| Version-family collapse (20 studies) | `repair_study_families.py` | **recorded judgement with its evidence** — every merge and every examined-but-rejected pair is listed with authors, venue and dates |
| Full-text timing extraction | — | **manual**, bounded by access: 13 of 20 studies were readable |
| Author-network resolution | `resolve_author_network.py` | **automatic from published metadata** |
| Study-level register and counts | `build_s11_study_register.py`, `s11_counts.py` | **generated** from the CSVs |
| C1 per-source stage counts | `c1_stage_counts.py` | **generated** by parsing `documentation/adaptation_chain_matrix.md` |
| Stale-count guard | `check_s11_consistency.py` | fails if any active document disagrees with the authoritative counts |

Both retrieval scripts **report drift** against the recorded snapshot rather than
overwriting it. If OpenAlex has changed since 18 August 2026, you will see the
difference printed; the committed CSVs remain the snapshot the manuscript describes.

## Data files

| File | Contents |
|---|---|
| `documentation/forward_citation_records_raw.csv` | **306 rows** — one per (seed, citing work) pair, pre-deduplication, no screening columns |
| `documentation/forward_citation_works_deduplicated.csv` | **262 rows** — one per unique OpenAlex work, with stage-1 result |
| `documentation/forward_citation_search_results.csv` | **262 rows** — the full decision table: stage-1, stage-2, exclusion reason, full-text status and source, timing hit, Table 7 row, author-network status, record role, version family, study role |
| `documentation/s11_study_register.md` | generated study-level view: the 20 studies, their roles, and the version families |

No third-party full text is included in this repository. Titles, DOIs and author
lists are bibliographic metadata.

## Run

```
python3 tools/retrieve_306_records.py
python3 tools/reproduce_forward_citation_search.py
python3 tools/c1_stage_counts.py
python3 tools/s11_counts.py
```

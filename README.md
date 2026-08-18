# FIM High-Mobility ISAC — Public Review Mirror

This repository is a **sanitized, read-only mirror** of the supporting documentation and manuscript drafts for a structured critical review:

> *Flexible Intelligent Metasurfaces for High-Mobility ISAC: Hardware Evidence, Adaptation Timescales, and Validation Gaps*

It exists **only** so that an independent reviewer can inspect the manuscript, its tables, figures, bibliography, and the full evidence-audit trail behind it, without needing local filesystem access to the author's working repository.

## What this is not

- **Not the working repository.** The authoritative repository — including the full downloaded literature corpus (journal and conference PDFs) — is private and stays private. This mirror is regenerated from it by a one-way, whitelist-based sync script; nothing flows back.
- **Not a publication.** This is an unpublished draft under active revision. See `manuscript/00_front_matter.md` for the current version and freeze status, and `documentation/draft_status.md` for exactly what is and is not done.
- **Not the CST/full-wave companion project.** That project is explicitly out of scope for this manuscript and is not mirrored here.

## Start here

Read **[`REVIEW_INDEX.md`](REVIEW_INDEX.md)** first. It gives the reading order, links every supporting record, states the manuscript's load-bearing claims and their current evidence classification without strengthening them, and lists known limitations.

For a single-file read of the whole manuscript, see **[`manuscript/COMPLETE_MANUSCRIPT.md`](manuscript/COMPLETE_MANUSCRIPT.md)** (auto-generated — do not edit directly; edit the section files in `manuscript/` instead).

## Contents

```
manuscript/       — front matter, twelve numbered sections, references, figures
documentation/     — evidence matrices, source inventory, search log, audits
review/            — REVIEW_MANIFEST.md (file-by-file provenance) and SOURCE_VERSION_MAP.md
CURRENT_VERSION.md — which snapshot this is, and what private commit it corresponds to
CHANGELOG.md       — dated, attributed change history
LICENSE_OR_NOTICE.md — copyright status of this repository and of the works it cites
```

## What is deliberately excluded

No journal or conference PDFs, no publisher supplementary files, no API keys, credentials, or private correspondence are present in this repository or its history. See `LICENSE_OR_NOTICE.md` and `review/REVIEW_MANIFEST.md` for the exclusion policy and the safety checks applied before each publish.

## Synchronization

This repository is regenerated from the private working repository by `tools/sync_review_repo.py` (kept in the private repository, not here). Each sync corresponds to exactly one private-repository commit, recorded in `CURRENT_VERSION.md`.

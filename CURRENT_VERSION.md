# Current Review Snapshot

Manuscript: v0.22
Documentation: v1.9

Private source repository commit:
`87114766f9d1d0f72445a3817068d01b3fbc0ff7`

Public review repository commit:
`this commit` (see `git log -1` in this repository)

Generated:
`2026-08-18 22:34 UTC`

Scientific freeze status:
`Evidence base frozen at documentation v1.6. Manuscript v0.22 / documentation v1.9. The v0.21 pass recoded the adaptation chain on two axes and re-executed the forward citation search against an explicit published query; the v0.22 pass repaired the C1 stage count, collapsed a conference/journal pair the dataset had counted as two studies, and published the reproducibility scripts. Current S11 flow: 306 records -> 262 works -> 65 stage-1 -> 24 records -> 20 studies -> 13 read / 7 unread. See CHANGELOG.md v1.9.`

Known unresolved blockers:
- no domain-expert review has occurred; extraction and classification were performed by a single reviewer and were not independently duplicated or adjudicated
- no *headline* response, morphing or adaptation interval in the manuscript carries an uncertainty, because no reviewed source reports repetitions or dispersion for one -- this is not universal across the register: Table 5 row 28 carries 0.35 +/- 0.15 s
- 7 of the 20 identified system studies are behind publisher paywalls and unread -- every forward-citation count is a lower bound. Exactly one of them is author-disjoint from both the FIM lineage and all three primary hardware sources, so that single study is the whole residual risk to the independence finding
- stage-2 screening and full-text extraction remain single-reader judgements; retrieval and stage-1 screening are exactly reproducible from tools/ but stages 2-3 are auditable per work rather than re-derivable
- no reviewed source fully delimits more than 5 of the ten adaptation stages, and the one that reaches that number has no radio-frequency layer; stages S8, S9 and S10 remain untimed on any radiating, shape-commanding platform
- one version-of-record check remains open (ALE-26) and is peripheral: cited once for class membership, with no quantitative claim drawn from it

Files synchronized from private source:
- `CHANGELOG.md`
- `documentation/absence_claims.md`
- `documentation/adaptation_chain_matrix.md`
- `documentation/architecture_taxonomy.md`
- `documentation/article_type_assessment.md`
- `documentation/audits/architecture_audit.md`
- `documentation/audits/citation_audit.md`
- `documentation/audits/evidence_audit.md`
- `documentation/audits/independence_audit.md`
- `documentation/audits/latency_definition_audit.md`
- `documentation/audits/redundancy_audit.md`
- `documentation/audits/terminology_audit.md`
- `documentation/draft_status.md`
- `documentation/evidence_matrix.md`
- `documentation/evidence_strength_matrix.md`
- `documentation/forward_citation_records_raw.csv`
- `documentation/forward_citation_search_results.csv`
- `documentation/forward_citation_works_deduplicated.csv`
- `documentation/literature_search_log.md`
- `documentation/manuscript_argument_map.md`
- `documentation/novelty_boundary.md`
- `documentation/s11_study_register.md`
- `documentation/s11_study_register.md`
- `documentation/source_inventory.md`
- `documentation/timescale_matrix.md`
- `documentation/unresolved_questions.md`
- `manuscript/00_front_matter.md`
- `manuscript/01_introduction.md`
- `manuscript/02_scope_and_method.md`
- `manuscript/03_architectures.md`
- `manuscript/04_demand_side.md`
- `manuscript/05_adaptation_chain.md`
- `manuscript/06_hardware_evidence.md`
- `manuscript/07_synthesis.md`
- `manuscript/08_traceability.md`
- `manuscript/09_validation_gap.md`
- `manuscript/10_reporting_framework.md`
- `manuscript/11_discussion.md`
- `manuscript/12_conclusion.md`
- `manuscript/99_references.md`
- `manuscript/figures/fig1_architecture_evidence_map.pdf`
- `manuscript/figures/fig1_architecture_evidence_map.png`
- `manuscript/figures/fig2_adaptation_chain.pdf`
- `manuscript/figures/fig2_adaptation_chain.png`
- `manuscript/figures/fig3_timing_landscape.pdf`
- `manuscript/figures/fig3_timing_landscape.png`
- `manuscript/figures/fig4_assumption_evidence_map.pdf`
- `manuscript/figures/fig4_assumption_evidence_map.png`
- `manuscript/figures/make_figures.py`
- `tools/README.md`
- `tools/build_forward_citation_csv.py`
- `tools/build_s11_study_register.py`
- `tools/c1_stage_counts.py`
- `tools/check_s11_consistency.py`
- `tools/repair_study_families.py`
- `tools/reproduce_forward_citation_search.py`
- `tools/resolve_author_network.py`
- `tools/retrieve_306_records.py`
- `tools/s11_counts.py`

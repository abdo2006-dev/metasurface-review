# Current Review Snapshot

Manuscript: v0.28a
Documentation: v1.12

Private source repository commit:
`39c3139c629ff83d71704589d087bdf42a908772` (private working tree was NOT clean at sync time -- see below)

Public review repository commit:
`this commit` (see `git log -1` in this repository)

Generated:
`2026-08-22 10:48 UTC`

Scientific freeze status:
`Manuscript v0.28a / documentation v1.12. Seven numbered sections. The v0.24 pass rebuilt the timing taxonomy on two axes, which is where the measured-duration maximum became 4; v0.28 restructured the article from twelve sections to seven and moved the audit machinery to the supplementary material; v0.28a renumbered the figures into order of appearance and corrected the object attributed to one cited control-path bound after re-reading the primary source. Current C1 maxima: quantitatively evidenced stages 6; measured stage durations 4; stages carrying any duration information 6. Current S11 flow: 306 records -> 262 works -> 65 stage-1 -> 24 records -> 20 studies -> 13 read / 7 unread. See CHANGELOG.md v1.12.`

Known unresolved blockers:
- no domain-expert review has occurred; extraction and classification were performed by a single reviewer and were not independently duplicated or adjudicated
- no *headline* response, morphing or adaptation interval in the manuscript carries an uncertainty, because no reviewed source reports repetitions or dispersion for one -- this is not universal across the register: Table 5 row 28 carries 0.35 +/- 0.15 s
- 7 of the 20 identified system studies are behind publisher paywalls and unread -- every forward-citation count is a lower bound. Exactly one of them is author-disjoint from both the FIM lineage and all three primary hardware sources, so that single study is the whole residual risk to the independence finding
- stage-2 screening and full-text extraction remain single-reader judgements; retrieval and stage-1 screening are exactly reproducible from tools/ but stages 2-3 are auditable per work rather than re-derivable
- no reviewed source fully delimits more than 4 of the ten adaptation stages, and the one that reaches that number has no radio-frequency layer; stages S8, S9 and S10 remain untimed on any radiating, shape-commanding platform
- one version-of-record check remains open (ALE-26) and is peripheral: cited once for class membership, with no quantitative claim drawn from it

Files synchronized from private source:
- `.github/workflows/validate.yml`
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
- `documentation/journalization_v0.28.md`
- `documentation/literature_search_log.md`
- `documentation/manuscript_argument_map.md`
- `documentation/novelty_boundary.md`
- `documentation/professor_brief.md`
- `documentation/professor_readiness_v0.28a.md`
- `documentation/s11_manual_decisions.csv`
- `documentation/s11_study_citations.csv`
- `documentation/s11_study_register.md`
- `documentation/source_inventory.md`
- `documentation/supplement_coding_scheme.md`
- `documentation/supplement_combined.md`
- `documentation/supplement_extraction_notes.md`
- `documentation/supplement_forward_citation.md`
- `documentation/supplement_propagation.md`
- `documentation/supplement_quantity_taxonomy.md`
- `documentation/supplement_reporting_motivation.md`
- `documentation/supplement_states.md`
- `documentation/supplement_timing_register.md`
- `documentation/timescale_matrix.md`
- `documentation/unresolved_questions.md`
- `manuscript/00_front_matter.md`
- `manuscript/01_introduction.md`
- `manuscript/02_scope_and_method.md`
- `manuscript/03_architectures.md`
- `manuscript/04_hardware_evidence.md`
- `manuscript/05_validation_gap.md`
- `manuscript/06_implications.md`
- `manuscript/07_conclusion.md`
- `manuscript/99_references.md`
- `manuscript/figures/fig1_architecture_evidence_map.pdf`
- `manuscript/figures/fig1_architecture_evidence_map.png`
- `manuscript/figures/fig2_timing_landscape.pdf`
- `manuscript/figures/fig2_timing_landscape.png`
- `manuscript/figures/fig3_adaptation_chain.pdf`
- `manuscript/figures/fig3_adaptation_chain.png`
- `manuscript/figures/fig4_assumption_evidence_map.pdf`
- `manuscript/figures/fig4_assumption_evidence_map.png`
- `manuscript/figures/make_figures.py`
- `tools/README.md`
- `tools/_paths.py`
- `tools/build_forward_citation_csv.py`
- `tools/build_s11_study_register.py`
- `tools/c1_stage_counts.py`
- `tools/check_mirror_links.py`
- `tools/check_s11_consistency.py`
- `tools/export_manual_decisions.py`
- `tools/reproduce_forward_citation_search.py`
- `tools/retrieve_306_records.py`
- `tools/s11_counts.py`
- `tools/validate_public_snapshot.py`

#!/usr/bin/env python3
"""Merge the live stage-1 retrieval with the recorded manual screening decisions."""
import csv, sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "Documentation" / "forward_citation_stage1_raw.csv"
OUT = Path(__file__).resolve().parent.parent / "Documentation" / "forward_citation_search_results.csv"

# Manual stage-2 decisions, keyed by a distinctive title fragment (lowercase).
# fields: stage2, exclusion_reason, full_text, source, timing_hit, case_id, network, role
D = {
 "channel estimation for flexible intelligent metasurfaces": ("yes","","yes","arXiv:2508.00268v4","yes","P3","shares author (Yuen) with FIM lineage","propagation"),
 "flexible intelligent metasurfaces in high-mobility": ("yes","","yes","corpus: IEEE TWC version of record","yes","P5","FIM lineage (An, Yuen)","propagation"),
 "weighted sum-rate enhancement for flexible intelligent metasurface-assisted multicell": ("yes","","yes","arXiv:2606.06845","yes","P1;P2","shares author (An) with FIM lineage","propagation"),
 "weighted sum-rate maximization for flexible intelligent metasurface aided multicell": ("yes","earlier conference version of the arXiv work read","no","paywalled (GLOBECOM 2025)","unknown","","shares author (An) with FIM lineage","unread"),
 "flexible intelligent metasurfaces for downlink multiuser miso": ("yes","","yes","open institutional repository (Southampton ePrints 496956)","yes","P4","FIM lineage (An, Yuen)","propagation"),
 "downlink multiuser communications relying on flexible intelligent metasurfaces": ("yes","","yes","corpus: GLOBECOM 2024 author version","no","","FIM lineage (An, Yuen)","no timing value"),
 "flexible intelligent metasurface-aided wireless communications": ("yes","","yes","corpus: IEEE TWC version of record","no","","FIM lineage (Yuen)","no timing value"),
 "flexible intelligent metasurfaces for enhancing mimo communications": ("yes","","yes","arXiv:2502.16478","no","N2","FIM lineage (An, Yuen)","counterexample"),
 "flexible intelligent metasurface for downlink communications under statistical csi": ("yes","","yes","arXiv:2512.23045","no","N1","AUTHOR-DISJOINT from FIM lineage and from all three seeds","counterexample"),
 "flexible intelligent metasurface for enhancing multi-target wireless sensing": ("yes","","yes","arXiv:2506.23052","no","","shares author with FIM lineage","no timing value"),
 "optimal morphing metasurface lens": ("yes","","yes","figshare open access (EuCAP 2024)","no","N3","AUTHOR-DISJOINT from FIM lineage and from all three seeds","counterexample"),
 "flexible reconfigurable intelligent surface-aided covert communications": ("yes","","no","paywalled (IEEE JSAC); Crossref author metadata only","unknown","","disjoint from FIM lineage; shares author (T. Pan) with seed LI","unread"),
 "emerging technologies in intelligent metasurfaces": ("yes","","no","paywalled (IEEE TAP)","unknown","","unresolved","unread"),
 "flexible intelligent metasurface for mitigating beam squint": ("yes","","no","paywalled (IEEE TVT)","unknown","","unresolved","unread"),
 "harmonizing flexibility and intelligence": ("yes","","no","paywalled (PIMRC 2025)","unknown","","unresolved","unread"),
 "sum-rate maximization for flexible intelligent metasurface enhanced multiuser miso": ("yes","","no","paywalled (ICC)","unknown","","unresolved","unread"),
 "drl-based joint beamforming and surface shape optimization": ("yes","","no","paywalled (ICC)","unknown","","unresolved","unread"),
 "near-field equivalent modeling and efficient analysis": ("yes","","no","not retrieved (Acta Physica Sinica)","unknown","","unresolved","unread"),
 "flexible intelligent metasurfaces for enhancing mimo integrated sensing": ("yes","","yes","arXiv author version","no","","FIM lineage (An, Yuen)","no timing value"),
 "flexible antenna arrays for wireless communications": ("yes","","yes","arXiv author version","no","","disjoint from FIM lineage","no timing value"),
 "flexible cylindrical arrays with movable antennas": ("yes","","yes","arXiv author version","no","","disjoint from FIM lineage","no timing value"),
 "t3dris": ("yes","","yes","arXiv:2404.05261 / HAL open access","no","","shares author (Di Renzo) with FIM lineage","no timing value"),
}

EXCL = "not a flexible-metasurface or reconfigurable-surface wireless *system* paper (optics, photonics, materials, mechanics, imaging, or non-system metasurface design)"

# Deduplication by OpenAlex ID does NOT collapse preprint/version-of-record pairs.
# The project's independence rule does: two versions of one study are one study.
# version_family groups stage-2 records into studies.
FAMILY = {
 "channel estimation for flexible intelligent metasurfaces": "F-XIA",
 "flexible intelligent metasurfaces in high-mobility": "F-RAN",
 "weighted sum-rate enhancement for flexible intelligent metasurface-assisted multicell": "F-HU",
 "weighted sum-rate maximization for flexible intelligent metasurface aided multicell": "F-HU",
 "flexible intelligent metasurfaces for downlink multiuser miso": "F-ANJ-J",
 "downlink multiuser communications relying on flexible intelligent metasurfaces": "F-ANJ-C",
 "flexible intelligent metasurface-aided wireless communications": "F-YAN",
 "flexible intelligent metasurfaces for enhancing mimo communications": "F-ANJ-MIMO",
 "flexible intelligent metasurface for downlink communications under statistical csi": "F-KUM",
 "flexible intelligent metasurface for enhancing multi-target wireless sensing": "F-SENS",
 "optimal morphing metasurface lens": "F-BAN",
 "flexible reconfigurable intelligent surface-aided covert communications": "F-HUA",
 "emerging technologies in intelligent metasurfaces": "F-TAP",
 "flexible intelligent metasurface for mitigating beam squint": "F-MING",
 "harmonizing flexibility and intelligence": "F-ZAR",
 "sum-rate maximization for flexible intelligent metasurface enhanced multiuser miso": "F-SRM",
 "drl-based joint beamforming and surface shape optimization": "F-DRL",
 "near-field equivalent modeling and efficient analysis": "F-APS",
 "flexible intelligent metasurfaces for enhancing mimo integrated sensing": "F-MIMO-ISAC",
 "flexible antenna arrays for wireless communications": "F-FAA",
 "flexible cylindrical arrays with movable antennas": "F-FCA",
 "t3dris": "F-T3D",
}

rows = list(csv.DictReader(SRC.open(encoding="utf-8")))
matched = set()
for r in rows:
    t = (r["title"] or "").lower()
    if r["stage1_regex_pass"] != "yes":
        r["stage2_system_paper"] = "no"
        r["exclusion_reason"] = "did not pass stage-1 title/abstract screen"
        r["full_text_inspected"] = "no"; r["final_role"] = "excluded"
        r["version_family"] = ""
        continue
    hit = next((k for k in D if k in t), None)
    if hit:
        matched.add(hit)
        s2, exc, ft, src, th, cid, net, role = D[hit]
        r.update(stage2_system_paper=s2, exclusion_reason=exc, full_text_inspected=ft,
                 full_text_source=src, timing_terminology_hit=th,
                 propagation_case_id=cid, author_network_status=net, final_role=role,
                 version_family=FAMILY.get(hit, ""))
    else:
        r.update(stage2_system_paper="no", exclusion_reason=EXCL,
                 full_text_inspected="no", final_role="excluded", version_family="")

missing = set(D) - matched
if missing:
    print("WARNING: decision-table keys that matched nothing:", missing, file=sys.stderr)

for r in rows: r.setdefault("version_family","")
fields = list(rows[0].keys())
if "version_family" not in fields: fields.append("version_family")
with OUT.open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(rows)

s1 = sum(r["stage1_regex_pass"] == "yes" for r in rows)
s2 = sum(r["stage2_system_paper"] == "yes" for r in rows)
ft = sum(r["full_text_inspected"] == "yes" for r in rows)
prop = sum(r["final_role"] == "propagation" for r in rows)
cex = sum(r["final_role"] == "counterexample" for r in rows)
nov = sum(r["final_role"] == "no timing value" for r in rows)
unread = sum(r["final_role"] == "unread" for r in rows)
print(f"unique works {len(rows)} | stage-1 {s1} | stage-2 records {s2} | full text {ft}")
fam_all={r["version_family"] for r in rows if r["stage2_system_paper"]=="yes"}
fam_read={r["version_family"] for r in rows if r["full_text_inspected"]=="yes"}
print(f"roles: propagation {prop} | counterexample {cex} | no-timing {nov} | unread {unread}")
print(f"STUDIES after version-family collapse: {len(fam_all)} total | {len(fam_read)} read in full | {len(fam_all-fam_read)} not read")
print("  not read:", sorted(fam_all-fam_read))

# Source Inventory

**Version:** 1.1 · **Compiled:** 17 August 2026 · **Amended:** 18 August 2026 (freeze consistency gate) · **Compiler:** Claude (Opus 5), acting as research/evidence-audit agent
**Scope:** every file physically present in `Metasurfaces/` as of the compilation date, plus sources identified through the documented external search (see `literature_search_log.md`).

---

## 0. How to read this file

Three evidence sets are kept strictly separate throughout all project documentation:

| Set | Meaning |
|---|---|
| **PROJECT CORPUS** | Full-text PDF physically present in `Metasurfaces/`. Verified by direct text extraction or page rendering. |
| **VERIFIED EXTERNAL** | Located through the documented external search and inspected (abstract page, HTML full text, or targeted extraction). Full PDF not necessarily archived locally. |
| **IDENTIFIED — FULL TEXT MISSING** | Known to exist; not inspected. No claim may rest on it. |

Citation keys used across all documentation are of the form `AUTHOR-YY`. **These keys, not filenames, are canonical.** Filenames in this corpus have a documented history of being wrong (see §4).

Independence groups (`IG-n`) mark publications that are *not* mutually independent evidence — same prototype, same author team reporting the same result, or conference/journal versions of one study.

---

## 1. PROJECT CORPUS — core review sources

### RAN-25 · Ranasinghe et al.
- **Title:** Flexible Intelligent Metasurfaces in High-Mobility MIMO Integrated Sensing and Communications
- **Authors:** K. R. R. Ranasinghe, J. An, I. A. Morales Sandoval, H. S. Rou, G. T. F. de Abreu, C. Yuen, M. Debbah
- **Year / status:** copy held is arXiv:2507.18793v1 [eess.SP], 24 Jul 2025 (12 pp.). ✅ **Version of record confirmed 17 Aug 2026** from the publisher-deposited Crossref record: *IEEE Trans. Wireless Commun.*, vol. 25, pp. 13319–13335, 2026, **DOI 10.1109/TWC.2026.3668992**. This confirms MOR-26's statement that an extended version exists. **Use the journal version in the bibliography.**
  - ✅ **Published full text obtained and inspected 17 Aug 2026.** Archived as `01V_Ranasinghe_High_Mobility_FIM_ISAC_IEEE_TWC_2026_VERSION_OF_RECORD.pdf` (17 pp., 13319–13335). Received 24 Jul 2025; revised 3 Nov and 30 Dec 2025; accepted 25 Feb 2026; published 6 Mar 2026. **All load-bearing quantities survive**, at new locators:
    - old **Table II** → published **Table III, p. 13327**, retaining f_c = 28 GHz, λ = 0.0107 m, B = 20 MHz, N_T = N_R = 4 (2 × 2), V_max = 208 m/s, y_max = λ, y_min = −λ (verified against the rendered table).
    - old **footnote 8** → published **footnote 10, p. 13327**, retaining verbatim: *"…after the surface shapes y_T and y_R have been computed for a distinct realization, the optimized surface shapes can be used irrespective to changes in delays, Doppler shifts and waveform."*
    - system-parameter and shape-reuse discussion: **p. 13327**; Figure 2 communications discussion continues on **p. 13328**.
    - FIM geometry constraint, shape vector and array response: Eqs. (1c), (2), (3), **p. 13321**.
  - ‼ **Material addition in the version of record — absent from the held preprint.** A **Remark** spanning pp. 13321–13322 states that distributed Lorentz forces *"enable rapid reconfiguration of the FIM surface shape within millisecond switching speeds [36], comparable to typical channel coherence times in high-mobility wireless scenarios"*, and then that *"in practical implementations, the FIM surface shape can also be morphed once over several channel coherence intervals to achieve statistically optimal performance, thus offering a flexible trade-off between achievable performance gains and morphing speed requirements."* Reference **[36] is BAI-22** (*Nature* **609**(7928):701–708, Sep 2022). See `evidence_matrix.md` E-03b/E-03c and `unresolved_questions.md` U6.
- **File (preprint, retained as an earlier version of the same study — IG-1):** `01_Ranasinghe_High_Mobility_FIM_ISAC.pdf` (12 pp.) · full text available
- **File (version of record):** `01V_Ranasinghe_High_Mobility_FIM_ISAC_IEEE_TWC_2026_VERSION_OF_RECORD.pdf` (17 pp.) · full text available
- **Architecture class:** A1 — theoretical FIM array, elements movable along surface normal (TX and RX)
- **Evidence level:** analytical model + communication-system simulation. **No hardware.**
- **Role in review:** central high-mobility FIM–ISAC system anchor; source of the two key modelling assumptions audited in §5 of the manuscript.
- **Key quantitative evidence:** 28 GHz, λ = 0.0107 m, B = 20 MHz, F_S = 20 MHz, N = 16/64 subcarriers, N_T = N_R = 4 (2×2), d_s = 4, P = 2/5 scatterers, R_max = 120 m, **V_max = 208 m/s**, morphing range y ∈ [−λ, +λ] (**Table III, p. 13327**; preprint Table II, p. 8). Gains: ≈2.5 dB (no FIM → random FIM) and ≈2 dB further (random → optimised), **p. 13328** (preprint p. 8).
- **Timing evidence:** none measured. **Footnote 10, p. 13327** (preprint footnote 8, p. 8) is a *qualitative* shape-reuse assertion — see `timescale_matrix.md` T-ASM-01. The version of record additionally asserts *"millisecond switching speeds"* for the cited filamentary platform in a Remark on pp. 13321–13322; this is an **assertion about another paper's hardware, not a measurement**, and is registered as such.
- **Independence group:** **IG-1** (with MOR-26). The held arXiv preprint and the archived version of record are **two versions of one study**, not two sources; the preprint is retained as the earlier version and is never counted as independent evidence.
- **Unresolved:** none arising from the version check. The bibliography must use *IEEE Trans. Wireless Commun.* **25**, 13319–13335, **2026**.

### ANJ-25 · An et al.
- **Title:** Downlink Multiuser Communications Relying on Flexible Intelligent Metasurfaces
- **Year / status:** ✅ **Resolved 17 Aug 2026, and the previous entry was wrong in one respect.** The held copy (arXiv:2502.16472v1, 6 pp.) is not an unpublished 2025 manuscript: it is the **GLOBECOM 2024** paper *"Downlink Multiuser Communications Relying on Flexible Intelligent Metasurfaces"*, pp. 4932–4937, 8 Dec 2024, **DOI 10.1109/GLOBECOM52923.2024.10901792**. The related journal article is also confirmed: *"Flexible Intelligent Metasurfaces for Downlink Multiuser MISO Communications," IEEE Trans. Wireless Commun.*, vol. 24, no. 4, pp. 2940–2955, April 2025, **DOI 10.1109/TWC.2025.3526843** — the paper RAN-25 cites as [31]. These are **two separate publications by the same team**, a conference paper and a journal paper, not a preprint and its version of record.
  - **Bibliography action:** cite the held copy as the GLOBECOM 2024 conference paper. The internal key `ANJ-25` is retained to avoid re-keying the whole documentation set, but **the version-of-record year is 2024**, and every quantitative claim in this review keyed to ANJ-25 was extracted from that 6-page conference paper, not from the TWC article.
  - ✅ **Version check completed 18 Aug 2026 — all five load-bearing claims survive.** The IEEE published record is paywalled, but (i) Semantic Scholar confirms `arXiv:2502.16472` **is** DOI `10.1109/GLOBECOM52923.2024.10901792`, so the held copy is the author version of the published conference paper; and (ii) the team's extended journal article — *"Flexible Intelligent Metasurfaces for Downlink Multiuser MISO Communications," IEEE Trans. Wireless Commun.* **24**(4):2940–2955, 2025, DOI `10.1109/TWC.2025.3526843` — was obtained in full from an open institutional repository (University of Southampton ePrints 496956) and read. Verified present in **both** versions: the **10.8 mm at 28 GHz** statement; **≈3 dB**; the **100-iteration cap with the −30 dB fractional-decrease rule** and 100-realisation averaging; **"quasi-static flat fading"**; and **"perfect knowledge of the CSI"** (the journal adds an acquisition route — probing predesigned shapes plus interpolation — that the conference paper does not give).
  - ‼ **One addition in the journal version, absent from the held conference paper.** Remark 4 states that *"With advanced EM actuation technology, it is possible to achieve dynamic surface-shape morphing in just a few milliseconds"*, citing BAI-22 as its reference [36]. The held conference copy contains **no occurrence of "millisecond" or of any `<number> ms` value**. This is the same add-on-at-journal-stage pattern found in RAN-25 and is registered as **E-FP-04**.
- **File:** `03_An_Downlink_Multiuser_FIM.pdf` (6 pp.) · full text available
- **Architecture class:** A1 — active FIM transmit array at a base station, normal-direction element movement
- **Evidence level:** analytical + communication-system simulation. No hardware.
- **Role:** foundational FIM shape-optimisation formulation; the clearest statement of the optimistic assumption set.
- **Key quantitative evidence:** 28 GHz, 100 MHz bandwidth, path-loss exponent 2.2, noise density −174 dBm/Hz; ≈3 dB transmit-power reduction at ζ = λ (p. 5 and conclusion p. 6); **the paper itself states λ = 10.8 mm at 28 GHz** (p. 6, conclusion). Max 100 alternating-optimisation iterations, convergence at −30 dB fractional decrease, averaged over 100 channel realisations (p. 5).
- **Stated assumptions (verified verbatim):** "we assume that all channels experience quasi-static flat fading" (p. 2); "We assume that both the BS and users have the perfect knowledge of the CSI for all the channels" (p. 3).
- **Independence group:** IG-2
- **Unresolved:** none blocking.

### YAN-25 · Yang et al.
- **Title:** Flexible Intelligent Metasurface-Aided Wireless Communications: Architecture and Performance
- **Year / status:** copy held is arXiv:2503.11112v1, 14 Mar 2025 (13 pp.). ✅ **Version of record confirmed 17 Aug 2026** from the publisher-deposited Crossref record: *IEEE Trans. Wireless Commun.*, vol. 25, pp. 6823–6836, 2026, **DOI 10.1109/TWC.2025.3627095**. **Use the journal version in the bibliography.**
  - ✅ **Published full text obtained and inspected 17 Aug 2026.** Archived as `04V_Yang_FIM_Architecture_and_Performance_IEEE_TWC_2026_VERSION_OF_RECORD.pdf` (14 pp., 6823–6836). **Both load-bearing items survive**, at new locators: the two-rate protocol statement is on **p. 6829** (preprint pp. 7–8), and the **Fig. 8 running-time experiment is on p. 6833** (preprint p. 11), retaining the 13th-Gen Intel Core i7-13650HX CPU, the 400-iteration maximum and the 10⁻⁸ stopping tolerance. **E-12 / T-YA-01 are version-of-record verified.**
  - ‼ **A quantitative claim was REMOVED between the preprint and the version of record (found 18 Aug 2026).** The preprint abstract states: *"In a multi-element, multi-path scenario, the EM-only mode improves the received signal power by 125% compared to the PBF-only mode."* **That sentence is absent from the published abstract**, which retains only the qualitative comparison — PBF-only *"shows less effective than the EM-only mode in enhancing received signal strength"*, and EM-PBF *"further enhances performance"* (p. 6823). A full-document scan of the version of record finds **no percentage figure anywhere in its technical text**. The manuscript's §1.1 previously cited the 125 % figure to YAN-25; it now uses the version of record's qualitative statement only. See `evidence_matrix.md` **E-13**, which is reclassified **superseded-by-version-of-record**. **Do not re-derive the figure from a published plot** — that would be an upgrade of evidence.
- **File (preprint, retained as an earlier version — IG-3):** `04_Yang_FIM_Architecture_and_Performance.pdf` · full text available (extraction required UTF-8 error handling)
- **File (version of record):** `04V_Yang_FIM_Architecture_and_Performance_IEEE_TWC_2026_VERSION_OF_RECORD.pdf` (14 pp.) · full text available
- **Architecture class:** A1 — reflecting FIM, elements movable in a plane **plus** independent passive phase shift
- **Evidence level:** analytical + simulation. No hardware.
- **Role:** the only corpus source that *schedules* element movement and phase update on different protocol levels; and the only FIM source reporting wall-clock computation time.
- **Key quantitative evidence:** 10 GHz; N = 4×4 movable elements; L = P = 4 paths; 12×12 angular grid; T₂ = 9 EM slots so that 4×4 elements form a 12×12 virtual array; Q = 2…16 subframes; max 400 iterations, tolerance 10⁻⁸ (**pp. 6832–6833**; preprint p. 11). ‼ **The preprint abstract's "125 %" figure does not appear in the version of record** — see below.
- **Timing evidence:** **Fig. 8, p. 6833 (preprint p. 11) — "Running time [Second]" versus virtual array size (36–324), on a 13th-Gen Intel Core i7-13650HX CPU**, Q = 12, SNR = 20 dB, 400-iteration maximum, 10⁻⁸ tolerance. Proposed CMFV-SBL spans roughly 4 × 10⁻³ s to ≈10⁻¹ s; the slowest benchmark reaches ≈1.2 s. Axis units read directly from the rendered figure.
- **Protocol structure (verified against the version of record):** "Assuming Q subframes with T₂ time slots in each subframe, the element moves once per subframe, and the FIM adjusts the phase once per time slot" (**p. 6829**; preprint pp. 7–8).
- **Independence group:** IG-3. The held preprint and the archived version of record are **two versions of one study**, not two sources.

### MOR-26 · Morales Sandoval et al.
- **Title:** Bistatic Integrated Sensing and Communications with Flexible Intelligent Metasurfaces
- **Year / status:** 2026 · arXiv:2607.29137, short paper (6 pp.)
- **File:** `11_Morales_Bistatic_FIM_ISAC.pdf` · full text available
- **Architecture class:** A1
- **Evidence level:** analytical + simulation. No hardware.
- **Independence group:** **IG-1 — NOT INDEPENDENT of RAN-25.** Verbatim, p. 1: *"An extended version of this work has been published in the Transactions on Wireless Communications [1]."* Do not count RAN-25 and MOR-26 as two confirmations of any result.
- **Role:** publication-lineage record; concise restatement of the same DD-FIM model. Footnote 1 repeats the movement-perturbation assumption; projected-gradient method "empirically converges within ∼10 iterations" (p. 3).

### XU-22 · Xu et al.
- **Title:** Channel Estimation for Reconfigurable Intelligent Surface Assisted High-Mobility Wireless Systems
- **Year / status:** copy held is marked DRAFT (16 pp.). ✅ **Version of record confirmed 17 Aug 2026** from the publisher-deposited Crossref record: *IEEE Trans. Veh. Technol.*, vol. 72, no. 1, pp. 718–734, **January 2023**, **DOI 10.1109/TVT.2022.3203818**.
  - ⚠ **The year in the internal key is wrong for the version of record.** The key `XU-22` reflects the 2022 draft and the 2022 DOI stem; the article is a **2023** publication. The key is retained internally, but **the bibliography must give 2023**, and no sentence in the manuscript should describe this as a 2022 paper.
  - ✅ **Published full text obtained and inspected 17 Aug 2026.** Archived as `07V_Xu_High_Mobility_RIS_Channel_Estimation_IEEE_TVT_2023_VERSION_OF_RECORD.pdf` (17 pp., 718–734). **All load-bearing items survive**, at new locators: 2.6 GHz, 100 kHz, 90 mph and the **51-symbol >0.5-correlation window on p. 721** (draft p. 4); the **20-symbol @ 0.95 and 40-symbol @ 0.82 illustrative cases in Fig. 4(b), p. 728** (draft p. 9, verified from the rendered figure legend); the **(1 + M) ON/OFF estimation slots on pp. 720 and 722**; the simulation parameter table on **p. 727**.
  - ‼ **A statement in our own earlier record was wrong.** The version of record **explicitly defines and uses f_s = 100 kHz as the symbol rate** in the system model (p. 721: *"…which is reasonable for a C&C link of f_s = 100 kHz over a coverage distance on the order of hundreds of meters"*), and f_d = v f_c / (c f_s) throughout. The claim that converting 51 symbols to wall-clock time "requires an assumption the source does not state" is therefore **false for the version of record — and, on re-checking, false for the held draft too**, which carries the same sentence on its p. 4. The ≈0.51 ms figure is a derivation from a source-stated quantity, not a conditional one. It has nonetheless been **deleted from the manuscript** by decision (U5): the 51-symbol figure carries the argument, and the derived millisecond value invites decontextualised quotation. It is retained in `evidence_matrix.md` E-DR-02 and `timescale_matrix.md` as a derived value, annotated *"derived from the source-stated f_s = 100 kHz; not required by the manuscript argument."*
- **File (draft, retained as an earlier version — IG-4):** `07_Xu_High_Mobility_RIS_Channel_Estimation.pdf` · full text available
- **File (version of record):** `07V_Xu_High_Mobility_RIS_Channel_Estimation_IEEE_TVT_2023_VERSION_OF_RECORD.pdf` (17 pp.) · full text available
- **Architecture class:** A5 — conventional electronically reconfigurable RIS, fixed geometry
- **Evidence level:** analytical + simulation. No hardware.
- **Role:** the corpus's only quantified statement of how fast a high-mobility channel actually decorrelates. Supplies the fast-timescale reference against which all hardware evidence is compared.
- **Key quantitative evidence:** carrier 2.6 GHz, bandwidth 100 kHz, **symbol rate f_s = 100 kHz**, M = 16 RIS elements, v = 90 mph; source–RIS–destination geometry given in the simulation table (**p. 727**; draft p. 10). **Verbatim, p. 721 (draft p. 4): "If the user moves at 90 mph, the coherence time over which the time correlation function is higher than 0.5 is estimated to cover only 51 symbols, which significantly differs from the idealistic assumption, namely that channel remains 100 % constant over an entire frame of signal transmission."** **Fig. 4(b), p. 728** additionally uses 20 symbol periods at 0.95 correlation and 40 symbol periods at 0.82 correlation (M = 16, 16QAM, v = 90 mph).
- **Protocol overhead:** ON/OFF scheme requires 1 + M time slots (**pp. 720, 722**).
- **Independence group:** IG-4. The held draft and the archived version of record are **two versions of one study**, not two sources.

---

## 2. PROJECT CORPUS — hardware evidence

### LI-25 · Fan Li et al.  ★ strongest hardware source in the corpus
- **Title:** Flexible intelligent microwave metasurface with shape-guided adaptive programming
- **Venue:** *Nature Communications* **16**:3161 (2025) · DOI `10.1038/s41467-025-58249-9`
- **File:** `02_FanLi_Flexible_Microwave_Metasurface_FISP.pdf` (11 pp.) · full text available
- **Architecture class:** **A3 — externally deformed, shape-aware, electronically programmable flexible reflective metasurface.** Not A4 (self-morphing): the surface does not command its own geometry.
- **Evidence level:** prototype RF measurement + application-level demonstration (highest in corpus for a flexible reflective surface)
- **Key quantitative evidence:** flexible RM 480 × 240 mm, 32 × 16 meta-atoms, 15 mm period, column-shared bias (32 independent channels), varactor 0–30 V, PI/PDMS/serpentine-mesh ground; 3.0–3.4 GHz; up to ≈270° reflection-phase tuning over 0–45° incidence; 32-sensor conformal strain array with RMSD as low as 2.36 mm at 45 mm maximum displacement; video-link demonstration with EVM ≈ −20 dB.
- **Timing evidence (verified verbatim, p. 4):** data preparation for ANN inputs **4 ms** (≈2 ms reception at ≈1200 Hz per channel + ≈2 ms processing); ANN inference for 32 channels **≈2 ms**; power-supply module response **5.25 ms**; varactor switching "negligibly short"; **"the measured response time for the entire process of our FISP system is 16.76 ms, which is approximately 5.5 ms slower than the response time obtained from theoretical analysis."** Fig. 3g annotates **16.76 ms** (measured) and **11.25 ms** (= 4 + 2 + 5.25, the component sum). The interval is explicitly defined as **"from shape acquisition to bias voltage supply."**
- **★★ Supplementary information retrieved 17 August 2026** (`23_FanLi_FISP_Supplementary_Information.pdf`, 33 pp.; `23B_…Peer_Review_File.pdf`, 49 pp.) — **this is the file recorded as missing in `Metasurface_Literature_Review_Context_v2.1.md` §5 and as workbook item M06; M06 is now resolved.** Supplementary Note 6 establishes:
  - **Method per component:** T1 (4 ms) and T2 (≈2 ms) are **thread-timing averages** inside the control program; T3 (5.25 ms) is an **oscilloscope measurement** of the supply module's output voltage after a control signal is issued over RS-232. The three are not the same kind of measurement.
  - **Why 16.76 ms exceeds 11.25 ms:** *"full-cycle control of all 32 channels via the RS-232 protocol (115200 bps baud rate) extends the total to 16.76 ms due to serial communication bottleneck."*
  - **Rate limit:** deformation intervals must exceed 16.76 ms, giving reliable operation *"at deformation frequencies up to 60 Hz."*
  - **★ A second, independent end-to-end experiment** (SI Fig. 13): a finger-triggered sensor, a dual-channel oscilloscope, and an AD8317 logarithmic detector linear over −10 to −60 dBm at 3.1 GHz. *"The measured delay between sensor triggering and stabilized RF output is 16.7 ms."* **This is the only interval in the corpus whose end event is stabilised radiation.** Geometry is static throughout — the trigger is a sensor press, not a shape change.
  - **Projection, not measurement:** response time *"expected to be reduced to less than 10 ms"* with faster acquisition circuits and a different protocol.
  - **Note 7 confirms the A3 classification:** the mechanical platform is a PMMA frame with two telescopic links and three movable fulcrums, adjusted to set curvature. No actuation timing, no closed loop on shape. Geometry is an imposed disturbance.
  - **Note 4:** strain sensors → ADC → MCU; bending radius from a two-term exponential fit calibrated against standard cylinders; **3 000 bending cycles** with negligible drift; shape RMSD computed against a binocular stereo-camera reference.
  - **Not reported anywhere in the supplement:** repetition counts, sample sizes, dispersion or uncertainty for 16.76 ms or 16.7 ms.
- **What it does NOT establish:** commanded mechanical actuation, mechanical settling, post-command RF stabilisation, fatigue, or high-mobility operation.
- **Independence group:** IG-5
- **✅ Supplement status — RESOLVED 17 August 2026.** Supplementary Notes 4, 5, 6 and 7 (strain-sensor calibration; BSM design; **assessment of response time**; mechanical loading platform) were retrieved from the publisher's open-access endpoint and archived as `23_FanLi_FISP_Supplementary_Information.pdf` (33 pp.), with `23B_FanLi_FISP_Peer_Review_File.pdf` (49 pp.). All notes referenced by the main text are present and have been read. This entry previously read "NOT in the corpus"; that state no longer holds.

### NEU-24 · Neuder et al.
- **Title:** Architecture for sub-100 ms liquid crystal reconfigurable intelligent surface based on defected delay lines
- **Venue:** *Communications Engineering* (2024) · DOI `10.1038/s44172-024-00214-3`
- **File:** `08_Neuder_Liquid_Crystal_RIS_Response_Time.pdf` (10 pp.) · full text available
- **Architecture class:** A5 — fixed-geometry electronically/materially tuned RIS
- **Evidence level:** component + prototype RF measurement
- **Key quantitative evidence (verified):** 4.6 μm LC layer; 12 × 10 unit cells; 62 GHz; 6.8 GHz (10.9 %) bandwidth; insertion loss < 7 dB (abstract) / 6.6 dB (conclusion); beam steering −50° to +50°. **τ_on ≈ 15 ms, τ_off = 72 ms** (p. 5, Fig. 4a), with **10 % / 90 % threshold markers shown in Fig. 4a**. Comparator: reflectarray-type LC-RIS implementations are stated to have τ_on of "few seconds" and τ_off of "10s of seconds" (p. 7). Projection only: **< 2 ms for t_LC = 1 μm** (p. 7) — modelled, not measured.
- **Independence group:** IG-6

### AKR-26 · Akram et al.
- **Title:** A Scalable and Integrated Reconfigurable Intelligent Surface
- **Venue:** *Advanced Electronic Materials* (2026) · DOI `10.1002/aelm.202500674`
- **File:** `09_Akram_Scalable_and_Integrated_RIS.pdf` (10 pp.) · full text available
- **Architecture class:** A5 — fixed-geometry one-bit PIN-diode RIS with integrated FPGA
- **Evidence level:** prototype RF measurement + measured control power
- **Key quantitative evidence (verified):** 9–10 GHz, 180° ± 20°; 16 × 16 tile, four-tile 32 × 32; Xilinx XC7A100T (Artix-7); UART/USB, Wi-Fi, LAN. Gain 20.2 dBi broadside / 18.2 dBi at ±50° (16 × 16, p. 8); 20.5 / 18.6 dBi (conclusion, p. 9 — quote per section, do not merge). Power for 32 × 32: **8.25 W all OFF, 13 W all ON, 11.25–11.60 W during beam steering** (p. 9).
- **Timing evidence (verified, two distinct quantities):** per-element FPGA **update time below 0.1 ms** (abstract, p. 1); **tile ON/OFF configuration updated in less than 10 ms** (p. 8 and conclusion p. 9). Control architecture note (p. 6): time-multiplexing "reduces the effective update rate to one quarter of the raw parallel speed."
- **Independence group:** IG-7

### BAI-22 · Bai et al.
- **Title:** A dynamically reprogrammable surface with self-evolving shape morphing
- **Venue:** *Nature* **609**(7928), 701–708 (2022) · DOI `10.1038/s41586-022-05061-w`
- **File:** `19_Bai_Dynamically_Reprogrammable_Shape_Morphing_Surface.pdf` (19 pp.) · full text available
- **Architecture class:** **A4 — actively self-morphing mechanical surface with closed-loop shape feedback.** Not an RF metasurface.
- **Evidence level:** measured mechanical hardware + closed-loop control demonstration
- **Key quantitative evidence (verified, p. 2):** 4 × 4 mesh of filamentary metal/polyimide traces; sample L = W = **18.0 mm**; serpentine beam length 3.60 mm; out-of-plane deformation **u/L ≈ 30 %** (⇒ ≈5.4 mm on an 18 mm sample); in-plane deformation < 0.01 L; **element response time < 0.07 s**; current I < 27.5 mA; static field B = 224 ± 16 mT. Abstract: "dynamic morphing capabilities with response times within 0.1 second."
- **★ Closed-loop timing (p. 4, previously unrecorded in the project workbook):** *"Each feedback control cycle in the current setup takes around 0.25 s due mainly to the time overhead from the image processing algorithm but this time is ultimately limited by the mechanical response time (which is less than 0.1 s)"*, and the optimisation "takes 5–15 iterations."
- **★★ Supplementary information retrieved 17 August 2026** (`19S_Bai_…pdf`, 71 pp.; `19SB_…Peer_Review_File.pdf`, 28 pp.). Note S5.3: single beam reaches steady state within 0.07 s, monitored by a **60 fps** Canon EOS R — the instrument's frame period (≈16.7 ms) bounds what this figure could resolve. Note S5.4: **1 000 reversible actuation cycles** at 1 Hz, u = 1.55 ± 0.02 mm at ±10 mA. Note S6 + Table 1: one function evaluation costs **0.35 ± 0.15 s** (update 0.06, settle pause 0.1, stereo imaging 0.08, template matching 0.11, reprojection ≈0, optimisation ≈0); each optimiser iteration requires **4(N+M)+2 = 34** function evaluations; Extended Data Fig. 4 gives **170–510 function evaluations (5–15 iterations)**; and the paper states directly: *"a 4×4 sample takes an average of ~2.5 min to morph a shape from the zero-actuation initial state."* Video legends: open-loop replay of known voltages at **10 fps**.
- **⚠ This retrieval retracted one of our own derived values.** The previous entry here recorded convergence as ≈1.25–3.75 s (5–15 × 0.25 s). That is **wrong** — an iteration is 34 cycles, not one. See `audits/citation_audit.md` C5 and evidence-matrix rows T-BA-03/04/05.
- **Full-package search for the tabulated 10 ms:** no occurrence of "10 ms", "0.01 s" (except as a ± dispersion), "sub-element", "filament", "transient" or "rise time"; the unit "ms" does not appear in the SI at all.
- **Independence group:** IG-8
- **✅ Supplement status — RESOLVED 17 August 2026.** The complete published package is now held: main text, Extended Data, the 71-page supplementary information (`19S_Bai_Shape_Morphing_Supplementary_Information.pdf`) and the peer-review file (`19SB_…`, 28 pp.). Notes S5.3, S5.4, S6 and Table 1 have been read directly. This entry previously read "not in the corpus"; that state no longer holds, and no audit finding may continue to rest on the supplement being unavailable.

### NI-22 · Ni et al.
- **Title:** Soft shape-programmable surfaces by fast electromagnetic actuation of liquid metal networks
- **Venue:** *Nature Communications* **13**:5576 (2022) · DOI `10.1038/s41467-022-31092-y`
- **File:** `20_Ni_Soft_Shape_Programmable_Liquid_Metal_Surface.pdf` (9 pp.) · full text available
- **Architecture class:** A4 — actively morphing soft surface (liquid-metal microfluidic ribbons, Lorentz force). Not an RF metasurface.
- **Evidence level:** measured mechanical hardware + FEA
- **★ Timing evidence (verified, pp. 3–4) — three distinct quantities that must never be merged:**
  1. **isolated ribbon:** measured ≈**30 ms** to stable deformation (FEA ≈50 ms);
  2. **full surface from flat:** measured total ≈**300 ms**, "dominated by the viscoelastic response of the membrane (~250 ms for the membrane to reach maximum deformation)";
  3. **shape-to-shape switching:** ≈300 ms + ≈**50 ms script processing** + ≈300 ms ⇒ ≈**650 ms**.
- **Independence group:** IG-9

### GAL-22 · Gal-Katziri, Fikes & Hajimiri
- **Title:** Flexible active antenna arrays
- **Venue:** *npj Flexible Electronics* **6**:85 (2022) · DOI `10.1038/s41528-022-00218-z`
- **File:** `18_GalKatziri_Flexible_Active_Antenna_Arrays.pdf` (11 pp.) · full text available
- **Architecture class:** **A7 — flexible *active transmitter* array.** Architecturally distinct from a passive reflective FIM/RIS: it has per-element RFICs, PLLs, on-chip sensors and self-sensing receivers.
- **Evidence level:** measured hardware system + application demonstration
- **Key quantitative evidence (verified):** two 256-element, 30 × 30 cm arrays; ≈0.1 g cm⁻² mass; concave and convex bend radii **< 23 cm** remaining "fully functional and programmable"; ≈**80 mW** DC delivered wirelessly to a 6.7 × 11 cm receiver at ≈1 m; maximum demonstrated steering ±10° and focusing range 1.6 m, both stated to be limited by the antenna range, not the array; closed-loop focusing using feedback from a remote receiver; calibration explicitly targets phase offsets from "manufacturing variations, shape deformations, or environmental changes."
- **Timing evidence:** **none reported for calibration or refocusing.** This is a significant gap — the corpus's most capable deformation-aware RF platform does not report how long its calibration takes.
- **Independence group:** IG-10

---

## 3. PROJECT CORPUS — reviews, conformal prior art, CST-project sources

| Key | Short title | Year / venue | Class | Evidence level | Role | IG |
|---|---|---|---|---|---|---|
| **MA-26** | A Survey on Reconfigurable and Movable Antennas for Wireless Communications and Sensing | 2026 · arXiv:2602.17977 (39 pp.). **Checked 17 Aug 2026: no journal version of record found.** The only publisher-deposited record is a TechRxiv preprint, DOI 10.36227/techrxiv.176857884.40392967/v1, 16 Jan 2026. **Cite as a preprint**; U11's caveat on the zero-occurrence "FIM" search stands, since it is a property of the copy held | A6 review | review synthesis | closest conceptual review; source of the instantaneous-vs-statistical-CSI and hierarchical-control positions | IG-11 |
| **SAI-22** | Recent Progress in Reconfigurable and Intelligent Metasurfaces (tuning mechanisms) | 2022 · *Adv. Sci.* `10.1002/advs.202203747` (35 pp.) | mechanism review | review synthesis | tuning-mechanism taxonomy and qualitative speed ranking | IG-12 |
| **TIS-25** | The Emergence of Multi-Functional and Hybrid RIS for ISAC — A Survey | 2025 · *IEEE COMST* `10.1109/COMST.2024.3519785` (44 pp.) | RIS/ISAC review | review synthesis | broad RIS–ISAC context and controller-latency framing | IG-13 |
| **TIS-25-AAM** | *(same paper, accepted-manuscript version)* | 42 pp. | — | — | **duplicate of TIS-25 — not independent** | IG-13 |
| **BUD-22** | Design of Planar and Conformal, Passive, Lossless Metasurfaces that Beamform | ‼ **DOI CORRECTED 18 Aug 2026.** This entry previously gave `10.1109/MAP.2022.3169344`; **that DOI belongs to a different paper** (Bodehou *et al.*, "Direct Numerical Inversion Methods for the Design of Surface Wave-Based Metasurface Antennas", *IEEE Antennas Propag. Mag.* **64**(4):24–36) and must not be used. The correct record, verified from Crossref: J. Budhu, L. Szymanski and A. Grbic, *IEEE J. Microw.* **2**(3):401–418, Jul. 2022, **DOI `10.1109/JMW.2022.3181719`** (16 pp.) | A-conformal (fixed) | full-wave simulation | conformal synthesis prior art; model-fidelity caveats | IG-14 |
| **LIH-19** | Wide-Angle Beam Steering Based on an Active Conformal Metasurface Lens | 2019 · *IEEE Access* `10.1109/ACCESS.2019.2960639` (9 pp.) | A-conformal transmissive, fixed curvature | prototype RF measurement | active conformal steering prior art (≈195° phase range; ±60° coverage) | IG-15 |
| **TAG-20** | Scalability Analysis of Programmable Metasurfaces for Beam Steering | 2020 · arXiv:2004.06917 (12 pp.) | A5 planar | semi-analytical model | phase-quantisation / aperture / angle scaling — **CST project** | IG-16 |
| **GUO-25** | Beam Steering Flexible Transparent Metasurfaces Based on Multi-Bit Phase Gradient Variations | 2025 · *Sci. Rep.* `10.1038/s41598-025-99768-1` (11 pp.) | A2 flexible passive (PB phase) | full-wave + fabricated array | flexible multi-bit prior art — **CST project fallback cell** | IG-17 |
| **ALE-26** | Feasibility Study of Curvature Effect in Flexible Antenna Arrays for 2-Dimensional Beam Alignment of 6G Wireless Systems | copy held is arXiv:2409.09590 (5 pp.). ✅ **Version of record confirmed 17 Aug 2026:** *2025 IEEE AP-S/CNC-USNC-URSI*, pp. 1–4, 13 July 2025, DOI 10.1109/AP-S/CNC-USNC-URSI55537.2025.11265965. **The version-of-record year is 2025, not 2026** — the key is retained internally but the bibliography must give 2025. Metadata only; full text not retrieved | A7 flexible active array | analytical + HFSS | curvature-aware array modelling precedent | IG-18 |
| **YOO-21** | Design of Conformal Array of Rectangular Waveguide-fed Metasurfaces | 2021 · arXiv:2109.09450 (6 pp.) | A-conformal fed antenna | reduced-order + CST | conformal reduced-order modelling precedent | IG-19 |
| **HAR-20** | Design of a continuously tunable reflectarray element for 5G metrology in the k-band | 2020 · *Adv. Radio Sci.* **18**, 1–5 · `10.5194/ars-18-1-2020` | A5 unit cell | full-wave (CST) + component measurement | **CST project preferred baseline — now PRESENT (was listed missing)** | IG-20 |
| **HAR-22** | Measurement and optimization of a continuously tunable 10 × 10 reflectarray antenna for 5G metrology in the K-band | 2022 · *Adv. Radio Sci.* **19**, 215–220 · `10.5194/ars-19-215-2022` | A5 array | prototype RF measurement | **NEWLY IDENTIFIED in corpus** (file `ars-19-215-2022.pdf`, previously unlabelled); array-level follow-up to HAR-20 | **IG-20 — same group, same design lineage; not independent of HAR-20** |
| **PEP-26** | Conformal Reconfigurable Intelligent Surfaces: A Cylindrical Geometry Perspective | 2026 · *Adv. Electron. Mater.* e00550 · `10.1002/aelm.202500550` (11 pp.) | A-conformal RIS, fixed cylindrical geometry, one-bit meta-atoms | analytical + semi-analytical + full-wave | closest competitor to the **CST project**; taxonomy entry for fixed-curvature conformal RIS | IG-21 |
| **LU-25** | A Versatile Design Method Applied to Conformal Metasurface Array Antenna | 2025 · *Microw. Opt. Technol. Lett.* **67**:e70134 · `10.1002/mop.70134` (6 pp.) | A2 flexible passive conformal reflectarray | full-wave + fabricated/measured | 15 × 15 liquid-metal-on-PDMS, 10 GHz dual beam, 1-bit coding, 17.9 dBi, stable over ±25 % bending | **IG-22** |
| **LU-26** | Design of Conformal Reconfigurable Reflectarray Antenna Based on Flexible Material | 2026 · *IEEE AWPL* **25**(5), 2265 · `10.1109/LAWP.2026.3676871` (5 pp.) | **A3 — flexible + electronically reconfigurable, externally bent** | full-wave + fabricated/measured | 10 × 10, 9 GHz, PIN diodes, ±45° scanning, PDMS + printed liquid metal, measured on acrylic supports at several fixed bending degrees, peak gain 16.13 dBi | **IG-22 — same group as LU-25 (Nanjing Univ. Posts & Telecom, Y. Yu corresponding); not independent** |
| **CHE-26** | Wide-Angle Conformal Active Metasurface for Dynamic Beam Steering and OAM Generation | 2026 · *Laser Photonics Rev.* **20**:e01500 · `10.1002/lpor.202501500` (13 pp.) | A-conformal, fixed 3D-printed curvature + voltage-programmable 2-bit coding | full-wave + measurement | 9.3–10.5 GHz, 0°–50° deflection, pointing accuracy better than ±2°, RCS −10 dB / +8.9 dB | IG-23 |

**Extraction note.** `22_Pepe…pdf`, `A Versatile Design Method….pdf` and `Wide-Angle Conformal Active Metasurface….pdf` contain **no extractable text layer** (rasterised Wiley downloads). Their metadata and abstracts above were read from rendered page images at 140 dpi. Deeper claims from these three require page-by-page image reading and are **not yet performed**. ✅ **Author lists for all three were read from rendered title pages on 18 Aug 2026** during bibliographic completion and are in `manuscript/99_references.md`.

---

## 3b. Bibliographic completion pass — 18 August 2026

Performed during the publication-oriented authoring pass, to produce a numbered reference list without inventing any field. **Author lists were extracted from the held PDFs' title pages** (rendered as images for the three rasterised files); **every DOI was then resolved against the publisher-deposited Crossref record**, and the arXiv metadata endpoint was queried for the preprints. Findings:

| Key | What changed | Basis |
|---|---|---|
| **BUD-22** | ‼ **DOI was wrong** — see the corrected row above. This is the only outright bibliographic error found. | Crossref resolution of the recorded DOI returned an unrelated paper; a title query returned the correct record |
| **AKR-26** | ‼ **corrected again 18 Aug 2026.** The v1.7 entry combined "vol. 12, no. 1" with "Dec. 2025" — internally inconsistent. Crossref gives `published-online` **12 Dec 2025** and `published-print` **January 2026**; volume 12, issue 1 **is** the 2026 issue. Cite as *Adv. Electron. Mater.* **12**(1), art. **e00674**, **Jan 2026**, noting the online-first date separately. The internal key's "26" turns out to match the issue year after all | Crossref `published-print` vs `published-online` |
| **CHE-26** | ‼ **same defect, same correction.** Crossref gives `published-online` **28 Sep 2025**, `published-print` **February 2026**. Cite as *Laser Photon. Rev.* **20**(3), art. e01500, **Feb 2026** | Crossref |
| **SAI-22** | art. 2203747 added; issue date is **Nov 2022** (online 18 Sep 2022) | Crossref |
| **LU-25** | issue date is **Mar 2025** (online 24 Feb 2025) | Crossref |
| **NEU-24** | art. 70 added; no print issue, so the May 2024 online date is the correct one | Crossref |
| **TIS-25** | **27**(5):2895–2936, Oct 2025 — no longer "Early Access" | Crossref |
| **LU-26** | pp. **2265–2269** (the entry gave only the first page) | Crossref |
| **LIH-19** | pp. **185264–185272** added | Crossref |
| **LU-25** | **67**(3), art. e70134 | Crossref |
| **SAI-22** | **9**(33) | Crossref |
| **NEU-24** | *Commun. Eng.* **3**(1) | Crossref |
| All other DOIs | ✅ resolve to the expected record, with the expected authors, volume and pages | Crossref |

**Standing rule reaffirmed.** The internal keys `AKR-26`, `CHE-26`, `XU-22`, `ANJ-25`, `ALE-26` and `PEP-26` carry years that differ from their versions of record. **The bibliography uses the version-of-record year; the keys are internal only and are never a citation.**

**External sources verified for the bibliography** (identity and full author list, from Crossref or the arXiv metadata endpoint): `HU-26` = Hu, An, Gan, H. Li, Al-Dhahir, Karagiannidis, Nallanathan, *IEEE TWC* **25**:18579–18595, 2026; `XIA-26` = Xiao, J. Wang, Cui, Y. Yang, X. Li, Niyato, Yuen, *IEEE TWC* **25**:10684–10701, 2026; `ANJ-25J` = An, Yuen, Di Renzo, Debbah, Poor, Hanzo, *IEEE TWC* **24**(4):2940–2955, 2025; `ANJ-MIMO` = An, Han, Niyato, Debbah, Yuen, Hanzo, arXiv:2502.16478; `KUM-25` = Kumar, Papazafeiropoulos, Kourtessis, Senior, Chafii, Kaklamani, Venieris, *IEEE WCL* **15**:1150–1154, 2026; `HUA-25` = Huang, G. Chen, Z. Xu, Zhu, **T. Pan**, Tafazolli, W. Huang, *IEEE JSAC* **44**:1577–1588, 2026; `LFIM-26` = He, Kumar, Papazafeiropoulos, Wen, Tran, Chafii, arXiv:2601.15471; `FAS-26` = Zhu, Wong, H. Xu, Rao, Shin, arXiv:2605.06275.

‼ **Two independence facts surfaced by this pass, both recorded in `evidence_matrix.md`:**
1. **`HUA-25` shares an author (Taisong Pan) with `LI-25`.** It is disjoint from the FIM system-paper lineage, which is what the S11 independence test measured, but it is **not** disjoint from the cited hardware sources. The counterexample row E-FP-C1 previously said "no author overlap" without that qualification, and has been corrected. `KUM-25` remains fully author-disjoint from both the lineage and all three primary hardware sources.
2. **`LFIM-26` shares three authors with `KUM-25`** (Kumar, Papazafeiropoulos, Chafii). They are two publications from one line of work and must never be presented as two independent confirmations that statistical-CSI FIM optimisation exists. No claim in the manuscript depends on their being independent — both are cited only for the *existence* of the published approach.

---

## 4. Filename audit and duplicate mapping

**Rule: filenames are not evidence of identity.** The following is the reconciliation between current filenames, the older workbook `S-IDs`, and the canonical keys used here.

| Current filename | Workbook S-ID | Canonical key | Note |
|---|---|---|---|
| `01_Ranasinghe_…` | S01 | RAN-25 | ok |
| `02_FanLi_…` | S02 | LI-25 | ok |
| `03_An_Downlink_Multiuser_FIM.pdf` | **S07** | ANJ-25 | ⚠ workbook S-numbering is *offset* from the current file numbering |
| `04_Yang_…` | **S06** | YAN-25 | ⚠ offset |
| `05_Ma_…` | S05 | MA-26 | ok |
| `06_Saifullah_…` | **S04** | SAI-22 | ⚠ offset |
| `07_Xu_…` | **S03** | XU-22 | ⚠ offset |
| `08_Neuder_…` | S08 | NEU-24 | ok |
| `09_Akram_…` | S09 | AKR-26 | ok |
| `10_Tishchenko_…_Published.pdf` | S15 | TIS-25 | ok |
| `10B_Tishchenko_…_DUPLICATE_VERSION.pdf` | S15-DUP | TIS-25-AAM | **duplicate — cite once** |
| `11_Morales_…` | S10 | MOR-26 | ok |
| `12`–`18`, `19`, `20` | S11–S14, S16–S18, S19, S20 | BUD-22, LIH-19, TAG-20, GUO-25, ALE-26, YOO-21, GAL-22, BAI-22, NI-22 | ok |
| `21_Harz_Continuously_Tunable_Reflectarray_Element.pdf` | (M01, "missing") | **HAR-20** | ✅ **now present**; workbook's `12_Missing_Sources` entry M01 is resolved |
| `ars-19-215-2022.pdf` | — | **HAR-22** | ⚠ **previously unlabelled and unrecorded.** Different paper from HAR-20 (vol. 19, 2022, array-level). Suggested rename: `21B_Harz_10x10_Tunable_Reflectarray_Measurement.pdf` |
| `A Versatile Design Method….pdf` | (M03, "missing") | **LU-25** | ✅ now present |
| `Design_of_Conformal_Reconfigurable_Reflectarray….pdf` | (M04, "missing") | **LU-26** | ✅ now present |
| `Wide-Angle Conformal Active Metasurface….pdf` | (M05, "missing") | **CHE-26** | ✅ now present |
| `22_Pepe_…` | (M02, "missing") | **PEP-26** | ✅ now present |

| `23_FanLi_FISP_Supplementary_Information.pdf` | (M06, "missing") | **LI-25-SI** | ✅ **retrieved 17 Aug 2026**; belongs to LI-25, **not an independent study** |
| `23B_FanLi_FISP_Peer_Review_File.pdf` | — | **LI-25-PR** | ✅ retrieved 17 Aug 2026; belongs to LI-25 |
| `19S_Bai_Shape_Morphing_Supplementary_Information.pdf` | — | **BAI-22-SI** | ✅ retrieved 17 Aug 2026; belongs to BAI-22 |
| `19SB_Bai_Shape_Morphing_Peer_Review_File.pdf` | — | **BAI-22-PR** | ✅ retrieved 17 Aug 2026; belongs to BAI-22 |

**Corpus totals (revised 17 August 2026):** **31 PDF files** → **26 unique documents** → **24 distinct research contributions** (distinct, not independent: several share authors — see §4 and `audits/independence_audit.md`).

The file count rose by four and **the contribution count did not change.** Supplementary information and peer-review files belong to their parent papers and are not independent studies; this is the project brief's independence rule and it applies to material this review retrieved just as it applies to material it found. The four new files are evidence *about* LI-25 and BAI-22, not evidence alongside them, and they are assigned to independence groups IG-5 and IG-8 accordingly.

---

## 5. ⚠ MISSING SOURCES — flagged for the user

### ✅ M-A. `23_FanLi_FISP_Supplementary_Information.pdf` — **RESOLVED 17 August 2026**
Previously recorded as absent from the corpus despite being listed as item #23 in `Metasurface_Literature_Review_Context_v2.1.md` §5 (= workbook `12_Missing_Sources` item M06).

**Retrieved** from the publisher's open-access supplementary endpoint and archived as `23_FanLi_FISP_Supplementary_Information.pdf` (33 pp.), together with `23B_FanLi_FISP_Peer_Review_File.pdf` (49 pp.). Identity confirmed from the title page. Supplementary Note 6 is present and has been read in full; its contents are recorded in §2 of this inventory under LI-25 and in evidence-matrix rows T-LI-04 and T-LI-06…T-LI-09. **Workbook item M06 should be marked resolved.**

### ✅ M-B. BAI-22 Extended Data / Supplementary Information — **RESOLVED 17 August 2026**
**Retrieved** and archived as `19S_Bai_Shape_Morphing_Supplementary_Information.pdf` (71 pp.) and `19SB_Bai_Shape_Morphing_Peer_Review_File.pdf` (28 pp.). The Extended Data figures were already present in the main-text PDF held in the corpus. The package was searched for any sub-element or faster response figure: **none exists.** See `audits/citation_audit.md` CA-02 for the full search result, and §2 under BAI-22 for the timing contents — including the ≈2.5 min closed-loop convergence figure that **retracted a derived value of our own**.

### M-C. Version-of-record status — **rebuilt 18 August 2026 from the actual present state**

‼ **The previous text of this item was stale and self-contradictory.** It listed RAN-25, ANJ-25, YAN-25, MA-26, XU-22 and ALE-26 under the heading "Journal versions not inspected", while §1 of this same file recorded that the versions of record for RAN-25, YAN-25 and XU-22 had been **obtained, archived and inspected**, and that the An journal article had been read in full from an open repository. The heading is withdrawn and replaced by a per-source status table. No blocker language survives that the evidence does not support.

| Key | VoR exists? | VoR obtained? | Full text inspected? | Quantitative claims verified against it? | Bibliography cites | Unresolved |
|---|---|---|---|---|---|---|
| **RAN-25** | ✅ *IEEE TWC* **25**:13319–13335, 2026, DOI 10.1109/TWC.2026.3668992 | ✅ archived `01V_…` | ✅ **yes**, 17 Aug 2026 | ✅ **all load-bearing timing and parameter quantities survive**, at VoR locators; one **material addition** found (the Remark, pp. 13321–13322, E-03b/E-03c) | version of record | **none** |
| **YAN-25** | ✅ *IEEE TWC* **25**:6823–6836, 2026, DOI 10.1109/TWC.2025.3627095 | ✅ archived `04V_…` | ✅ **yes**, 17 Aug 2026 | ✅ E-12 and T-YA-01 verified at VoR locators. ‼ **One non-timing claim did NOT survive** — the preprint abstract's 125 % figure is absent from the VoR and has been withdrawn (E-13) | version of record | **none** |
| **XU-22** | ✅ *IEEE TVT* **72**(1):718–734, **Jan 2023**, DOI 10.1109/TVT.2022.3203818 | ✅ archived `07V_…` | ✅ **yes**, 17 Aug 2026 | ✅ all load-bearing items survive at VoR locators; the f_s = 100 kHz correction was found here | version of record, **year 2023** | **none** — the internal key's "22" is an artefact and is never a citation |
| **ANJ-25** | ✅ two separate publications: GLOBECOM 2024 (the held copy) and the *IEEE TWC* **24**(4) journal article | conference: ✅ held; journal: ✅ read, not archived locally | ✅ **both**, 18 Aug 2026 | ✅ all five load-bearing claims verified present in **both** versions. ‼ **One addition in the journal version** — Remark 4's "a few milliseconds", absent from the conference copy (E-FP-04, propagation case P4) | the conference paper as [2]; the journal article separately as [32] | **none** |
| **MA-26** | ✗ **no journal version of record located** (checked 17 Aug 2026); only a TechRxiv preprint deposit, DOI 10.36227/techrxiv.176857884.40392967/v1 | n/a | ✅ held preprint read in full | ✅ E-40…E-43 verified in the held copy | **as a preprint**, explicitly | the zero-occurrence "FIM" search is a property of **the copy held**; U11's caveat stands |
| **ALE-26** | ✅ *IEEE AP-S/CNC-USNC-URSI* 2025, pp. 1–4, DOI 10.1109/AP-S/CNC-USNC-URSI55537.2025.11265965 | ✗ **metadata only; full text not retrieved** (paywalled) | ✗ — the held copy is arXiv:2409.09590 | ⚠ **not re-verified against the VoR** | the VoR, **year 2025**, marked in bold in `manuscript/99_references.md` as carrying an access caveat | ⚠ **the one genuinely open item in this table.** No load-bearing quantitative claim rests on it — it is cited once, in §3.5, as a curvature-aware array-modelling precedent (identity-level, class A7). Classified **peripheral** in the 18 Aug bibliographic-only audit; see §5b |

## 5b. Load-bearing audit of bibliographic-only and unread sources — 18 August 2026

Every manuscript claim resting on a source **not read in full** was located and classified. **A = load-bearing** (a quantitative value, a verdict, an absence claim or a contribution depends on it). **B = contextual/peripheral** (identity-level citation: the source is cited for existing, for being an example of a class, or for a position stated in its abstract).

| Ref | Key | Access status | Claims it supports | Class | Action taken |
|---|---|---|---|---|---|
| [11] | MA-26 | preprint held and **read in full**; no version of record exists to compare against | the instantaneous-vs-statistical-CSI position, hierarchical control, the "mechanical is slower" dichotomy, the movement-time modelling recommendation | **A** | **No action needed.** The full text *is* held and read; the caveat is only that no VoR exists. Cited explicitly as a preprint |
| [13] | LFIM-26 | **identified bibliographically only** | cited twice, jointly with [12], solely for the *existence* of published statistical-CSI FIM optimisation | **B** | **Retained, with the evidence level made explicit.** [12] was read in full and independently supports the same existence claim, so no claim rests on [13] alone. Note that [12] and [13] share three authors and are one line of work — recorded, and never presented as two confirmations |
| [14] | FAS-26 | **identified bibliographically only** | cited once, for the existence of delay-aware modelling in the adjacent fluid-antenna field | **B** | **Retained.** Used to *limit* this manuscript's novelty claim, not to support a finding. A citation that only ever weakens our own claim cannot inflate it |
| [21] | ALE-26 | VoR paywalled; **arXiv preprint held**, metadata verified | one row of Table 1 (A7 class membership) and one clause in §3.5 | **B** | **Retained.** Identity-level and class-level only; no quantity is drawn from it |
| [29] | ANJ-MIMO | author version **read in full** | Premise 2 (the coherence-block assumption), Table 5 row 35, Table 8 row 2, counterexample N2 | **A** | **No action needed** — the author version was read; only the *IEEE Trans. Commun.* record was not retrieved. Marked accordingly |
| [33] | HUA-25 | **paywalled; full text never read.** Crossref author metadata verified | ‼ **previously supported a claim it could not support** | **A → downgraded** | ‼ **Corrected.** v0.20 §8.5 and Table 7 row N1 listed it among papers that "attach no timing value at all" — a statement requiring full text we do not have. **Removed from the counterexample count**, which falls from a set including it to two fully author-disjoint cases. It is now cited only for its verified authorship, and §8.5 states explicitly that whether it attaches a timing value is unknown to us. See `CHANGELOG.md` CH-103 |

**Result.** One genuine over-reach was found and corrected ([33]). Two sources classified **A** turned out to have been read in full, their caveats being about version status rather than access ([11], [29]) — the bold marks in the reference list were doing double duty and are now worded precisely. The three remaining bibliographic-only sources are all **B**, each cited for existence or class membership, and one of them exists only to bound our own novelty claim.

**Standing rule.** No source that has not been read in full may support a statement about what that source does *not* contain. Absence claims require presence of the text.

### M-D. External FIM sources located but full text not archived (see `literature_search_log.md`)
Notably arXiv:2606.06845 (Hu et al., multicell FIM — source of the Table I feasibility claim audited in this review), arXiv:2512.23045 (Kumar et al., statistical-CSI FIM), arXiv:2502.16478 (An et al., FIM MIMO, IEEE TCOM), arXiv:2510.07466, arXiv:2601.15471, arXiv:2508.00268, arXiv:2605.29227, arXiv:2506.23052, arXiv:2511.00878, arXiv:2510.24190. **These were inspected online only.** Any claim resting on them is marked `[EXTERNAL — ABSTRACT/HTML INSPECTED, PDF NOT ARCHIVED]`.

# Ransomware detection, prevention, and incident response: a systematic literature review (2022–2026)

**Review type:** Systematic literature review (PRISMA 2020-style)
**Review protocol:** Not registered (no PROSPERO/OSF entry; PROSPERO does not accept non-health reviews of this design)
**PRISMA compliance:** Partial — see the transparency note in §2.3 and the checklist in Appendix B
**Review window:** 2022–2026 · **Eligibility:** journal papers, Q1/Q2 (Scimago SJR) · **Retained papers: 25** across 12 review items
**Date of review-catalog rewrite:** 2026-10-24
**Methodology note:** This document follows the structure of the literature-review skill template (structured abstract, documented methodology, PRISMA-style flow, thematic synthesis, full reference list, appendices). The full per-study extraction catalog produced by the deep-research phase is preserved unchanged as Supplementary file S1 (`extraction_catalog.md`); every field statement below is traceable to S1 or to the JSON extraction records in `results/`.

---

## Abstract

**Background:** Ransomware has shifted from commodity file-encrypting malware toward industrialized Ransomware-as-a-Service (RaaS) operations with double extortion, platform diversification (Windows, Linux/NAS, Android, IIoT/ICS, hypervisors), and emerging AI-generated offensive tooling. Defenders face a fragmented evidence base: detection research is dominated by laboratory ML prototypes with ad-hoc datasets, while causal evidence on organizational and clinical impact has only recently appeared.

**Objectives:** To systematically identify, verify, and synthesize peer-reviewed journal literature (2022–2026, Scimago SJR Q1/Q2) spanning ransomware detection methods, prevention and resilience engineering, AI-era threat modeling, threat-actor economics, incident response and forensic readiness, victimology, and quantified sectoral impact.

**Methods:** Twelve review items (A–L) were searched across six allowed sources (Google Scholar, IEEE Xplore, ScienceDirect, Scopus, Scimago SJR for quartile verification, and the PRISMA statement as methodological anchor) for journal papers published 2022–2026. Records were screened at candidate level against year, quartile, source, and topical criteria; exclusion and pruning decisions were documented per cluster; structured extraction recorded methodology, findings, limitations, research gaps, platform/kill-chain stratification, dataset and metric disclosure, reproducibility, and threat-intelligence coverage, with unverified values flagged `[uncertain]` rather than filled in.

**Results:** 25 papers were retained (23 Q1, 2 Q2). Detection research (12 papers) remains predominantly reactive and laboratory-bound: host/ML approaches struggle with evasion and non-standardized datasets; hardware/SSD- and deception-based designs achieve high detection at low overhead; network/federated designs extend coverage to propagation and unknown variants. Explainability work shows XAI can be layered onto detectors but exposes dataset-availability as the field's central replication bottleneck. Threat-modelling papers provide empirical proof that LLMs can generate full attack chains including encryption/extortion impact. Prevention/resilience work links backup and OS-level access-control design to realized recovery. On the economics side, on-chain tracing (13,497 payments, USD 101M, 87 actors) and game-theoretic analysis of double extortion (452 attacks; 27.8% payment rate) now exist alongside causal clinical evidence: hospital ransomware attacks reduced volume by 17–24% and increased in-hospital mortality by 34–38% among already-admitted patients.

**Conclusions:** The strongest current evidence sits at the extremes — technical detection prototypes (largely sandbox-validated; moderate-to-low external validity) and econometric/epidemiological impact studies (high methodological rigor). Cross-cutting gaps are dataset standardization, pre-encryption early detection, real-environment evaluation, IIoT/NAS-specific defense, and reproducibility of ML claims.

**Keywords:** ransomware; ransomware detection; systematic literature review; PRISMA; machine learning; Ransomware-as-a-Service; double extortion; incident response; reproducibility; hospital cybersecurity

---

## 1. Introduction

### 1.1 Background and context

Ransomware is the dominant financially motivated threat to organizations. The 2022–2026 window covers the industrialization of the criminal ecosystem — RaaS affiliates, data-exfiltration-before-encryption extortion (double extortion), leak-site victim exposure, NAS/consumer-appliance and IIoT targeting, and, at the frontier, LLM-assisted attack-code generation (e.g., the PromptLock proof-of-concept work). The deep-research literature used as the co-citation baseline (Oz et al. [25]; Albshaier et al. [24]) documents that detection research long over-indexed on Windows workstations, retrospective accuracy claims, and self-built datasets — conditions that motivated clustering this review around *reproducibility, early detection, platform expansion, and impact evidence* in addition to method categories.

### 1.2 Scope and objectives

This review covers journal literature on: (A) AI/ML-based detection; (B) behavioural, content and deception-based detection; (C) traffic and network-based detection; (D) explainability, reproducibility and benchmark validity; (E) AI-era threat models (LLM/GenAI ransomware); (F) prevention and resilience engineering; (G) platform expansion (OT/IoT/ICS, cloud/hypervisor, cross-platform, NAS); (H) RaaS, double extortion and payment tracing; (I) incident response, playbooks and forensic readiness; (J) victimology, economics and regulatory response; (K) sectoral empirical impact studies; (L) taxonomies and prior systematic reviews as baseline.

**Research questions:**

1. **RQ1 (Detection):** What detection method families exist in verified Q1/Q2 journal literature (2022–2026), at which kill-chain stage do they act, and what is known about their real-world effectiveness?
2. **RQ2 (Adversarial shift):** What does empirical evidence say about offensive AI/LLM automation of the ransomware attack lifecycle?
3. **RQ3 (Prevention and response):** What designs and organizational instruments link prevention, resilience, and incident response to realized outcomes?
4. **RQ4 (Threat-actor economy and victims):** What is known about RaaS economics, payment tracing, deception in extortion, and victim-side decision-making?
5. **RQ5 (Impact):** What is the causal, quantified impact of ransomware attacks on service delivery (especially healthcare)?
6. **RQ6 (Reproducibility):** How reproducible is the field's evidence, and what dataset/benchmark gaps dominate?

### 1.3 Significance

Prior reviews stop at 2020/2024 and are detection-centric ([25], [24]). The present review adds, within one verified protocol: the AI-offense strand (E), causal human-impact economics (K), NAS/IIoT victimology (G, J), on-chain payment tracing (H) and a reproducibility-first extraction schema (D) — enabling comparison of what can be *replicated* versus merely *reported*.

---

## 2. Methodology

### 2.1 Protocol and registration

Not registered. The review was executed as a scripted multi-agent pipeline: a candidate registry (`outline.yaml`), per-cluster extraction JSONs (`results/`), a field schema (`fields.yaml`), and pruning (`prune_results.py`). **Deviations from PRISMA 2020 during execution:** no per-database query logs were recorded; screening was automated/single-reviewer; see §2.5 and §4.3.

### 2.2 Search strategy

**Sources (allowed by protocol):** Google Scholar (discovery and citation chaining), IEEE Xplore, ScienceDirect, Scopus (record verification), Scimago Journal & Country Rank (quartile verification), plus the PRISMA statement as methodological anchor. Every retained record is traceable to one of these sources (column "Source" in Table 1; field `source_database` in S1).

**Eligibility window:** 2022–2026 (journal-issue year; online-first dates recorded in S1).
**Quality bound:** Scimago SJR Q1/Q2 at publication year. Conference papers, workshop proceedings, and arXiv/grey literature were out of scope by protocol but are referenced inside S1 where they are the provenance lead for a retained paper (e.g., the *Ransomware 3.0* preprint for the PromptLock narrative).

**Documentation limitation (explicit):** search strings, per-database execution dates, and raw hit counts were **not recorded** during the deep-research phase and therefore are not reproducible at query granularity. This review reports record-level provenance instead of query-level logs; the consequence for validity is discussed in §4.3. This is the review's largest deviation from PRISMA 2020 item 7 and is flagged in Appendix B.

### 2.3 Screening and selection

**Process:** candidates were registered per review item, then verified against: (i) publication year; (ii) Scimago SJR quartile at publication year; (iii) allowed-source traceability; (iv) topical fit. Retained records were afterwards pruned for redundancy ("record-overlap prune"), broken disclosure ("validity prune"), or recency overlap with an equivalent newer record — decisions transcribed verbatim in S1 and summarized in Appendix A. Where a candidate was miscited in the registry (e.g., Albshaier et al. registered as "Applied Sciences 2024" but actually published in *Information* [24]; Chaieb et al. registered as a 2023 IEEE Access article but actually an ESL/ESAI conference paper), the corrected record is documented in S1.

**PRISMA-style flow (with explicit gaps):**

```
Records identified by database searching ......... not recorded (no query-level logs)
Duplicates/records removed before screening ...... not recorded
Records screened at title/abstract level ......... not recorded
Records assessed at eligibility (candidate +
  provenance-leads evaluated in full) ............ 41 = 25 retained + 16 records
                                                   excluded/pruned with documented reasons
Reports not retrieved ............................ 0 reported (per-record rationale in S1)
Included studies (retained papers) ............... 25
```

An exclusion/prune log exists for every decision taken at the eligibility stage (16 entries across clusters A3, B4, C3, D1, E1, F1, I2, K1). Two of these entries in cluster B are retained-verification decisions recorded inside the same transcript block (see Appendix A); this bookkeeping ambiguity is itself recorded as a reconciliation limitation (see Appendix A). Cluster-level counter totals as reported by the pipeline: A 3, B 4, C 3, D 1, E 1, F 1, G 0, H 0, I 2, J 0, K 1, L 0 = 16.

**Selection bias by design (declared):** the protocol restricts inclusion to SJR Q1/Q2 *journals*. This excludes influential conference work (e.g., IEEE EuroS&PW reproducibility systematization — pruned from cluster D for quartile failure [S1]) and preprints (e.g., *Ransomware 3.0*). The 25-paper set therefore under-represents exactly the reproducibility-methods literature it measures — see §4.3.

### 2.4 Data extraction

Structured extraction followed the schema in `fields.yaml`: bibliographic (title, authors, year, journal, SJR quartile, source database, DOI); content (study type, methodology, key findings, limitations, research gaps); PRISMA (stage, inclusion rationale); stratification (platform/environment, kill-chain stage, dataset/benchmark disclosure, evaluation metrics); reproducibility; and threat-intelligence coverage (RaaS-group naming, leak-site evidence, wallet tracing). Values that failed verification were flagged `[uncertain]` and are shown in S1 as `*[uncertain]*` rather than invented (25 `study_type` flags, 25 `evaluation_metrics` flags, and 28 cluster-level uncertainty entries as booked by the pipeline; see Appendix C).

**Quality assessment:** no formal risk-of-bias instrument (RoB 2 / ROBINS-I / AMSTAR 2) was applied; no validated tool exists for security-ML and econometric designs of this profile. Quality proxy evidence is extracted instead: per-study limitations (acknowledged vs. observed), dataset/benchmark disclosure, evaluation balance, and real-environment vs. sandbox designation. This proxy approach is reported with its own limitation: it is not tool-calibrated and cannot support GRADE-style certainty statements.

**Synthesis approach:** narrative thematic synthesis across the 12 items; no meta-analysis (detection metrics from heterogeneous sandboxes/datasets are not combinable; econometric and clinical designs have incompatible effect measures).

### 2.5 Citation verification

All 25 reference DOIs plus the referenced replication-data DOI were checked against the Crossref Works API (2026-10-24). All 25 article DOIs are registered; returned metadata (title, journal, year) matches every reference entry. The ICPSR replication-package DOI `10.3886/E235483V1` (infra-tier data repository) is **not registered in Crossref** (HTTP 404) — its handle/provider is outside Crossref's coverage; per skill guidance the reference is retained with this limitation stated rather than deleted. The skill's DOI-registration pass via the doi.org Handle API (`verify_citations.py`) could not execute from this environment: local TLS interception (self-signed certificate in the chain for doi.org) broke the connection; Crossref metadata verification was run as substitute evidence, and claim-support checking was done manually during synthesis (any claim below maps to a study whose full-text extract is in S1).

---

## 3. Results

### 3.1 Study selection (25 retained papers)

Cluster yields: A 2, B 2, C 2, D 2, E 2, F 2, G 2, H 3, I 2, J 2, K 2, L 2. Year distribution: 2022 (4), 2023 (6), 2024 (7), 2025 (5), 2026 (3). Venues: Computers & Security (8), IEEE Access (3), IEEE/ACM (4), IEEE/ACM (4), MDPI (3), one each Communications of the ACM, ACM Computing Surveys, AEJ: Economic Policy, JAMA, European Journal of Criminology, Global Crime, Journal of Cybersecurity, Journal of Network and Computer Applications. 23 papers retained at Q1; 2 retained at Q2 (Future Internet 2023 [14]; Information 2024 [24]).

### 3.2 Study characteristics

Study types in Table 1 are the reviewer's categorization from methodology text (the extracted `study_type` field was flagged uncertain across all 25 papers — trust the description, not the type labels when in doubt).

Table 1. Included studies (n=25)

| # | Study (authors, year) | Theme | Venue (SJR quartile, source) | Study type | Design highlights |
|---|------------------------|-------|------------------------------|------------|-------------------|
| 1 | Ispahany et al. 2024 [1] | A | IEEE Access 12 (Q1; IEEE Xplore) | SLR | ML-detection review mapped to Cyber-Kill Chain; finds most systems reactive, late-detecting |
| 2 | Alzahrani et al. 2025 [2] | A | IEEE Access 13 (Q1; IEEE Xplore) | Survey | 135→45 papers (Windows/Android) 2019–2025; ML vs non-ML strengths; RaaS framing |
| 3 | Min et al. 2022 [3] | B | IEEE TCAD 41(7) (Q1; IEEE Xplore) | System design | AMOEBA: SSD-controller content detector + intra-device backup; beats FlashGuard |
| 4 | Gómez-Hernández & García-Teodoro 2024 [4] | B | Sensors 24(9) (Q1; PMC/MDPI) | Empirical experiment | Android honeyfiles + FileObserver; 1–700 ms notification latency vs 10–70 ms encryption |
| 5 | Almashhadani et al. 2022 [5] | C | Computers & Security (Q1 1.605; ScienceDirect) | Empirical experiment | MFMCNS: session- + time-based flows; WannaCry/NotPetya propagation detection |
| 6 | Lan et al. 2025 [6] | C | IEEE TNSM (Q1 1.389; IEEE Xplore) | System design | HFL-RD: heterogeneous federated learning over C&C traffic + API calls; >95% accuracy |
| 7 | Gulmez et al. 2024 [7] | D | Computers & Security 139 (Q1 1.445; ScienceDirect) | Empirical experiment | XRan: Cuckoo API/DLL/mutex sequences + 2-layer CNN; LIME/SHAP; up to 99.4% TPR |
| 8 | Galli et al. 2024 [8] | D | Computers & Security 141 (Q1 1.445; ScienceDirect) | Empirical experiment | SHAP/LIME/LRP/Attention comparison on LSTM/GRU behavioral detectors; proprietary data |
| 9 | Iturbe et al. 2024 [9] | E | Computers & Security (Q1 1.445; ScienceDirect) | System design / experiment | LLM-generated attack-technique code incl. encryption/extortion impact actions |
| 10 | Gupta et al. 2023 [10] | E | IEEE Access 11 (Q1 0.960; IEEE Xplore) | Threat modeling + PoC | GenAI dual-use: jailbreak/prompt-injection; polymorphic malware generation |
| 11 | Ilau et al. 2025 [11] | F | Journal of Cybersecurity (Q1 0.938; Oxford) | Modelling/simulation | Compositional model of organizational ransomware recovery; 9,000 configurations |
| 12 | McIntosh et al. 2023 [12] | F | Computers & Security 128 (Q1 1.566; ScienceDirect) | System design | SEDAC staged access control (PCAC/UCAC); blocks direct encryption + MBR tampering |
| 13 | Al-Hawawreh et al. 2024 [13] | G | J. Network & Computer Applications 223 (Q1 2.417; ScienceDirect) | Narrative review | IIoT ransomware landscape; IT-platform detectors have unvalidated IIoT transferability |
| 14 | Gazzan & Sheldon 2023 [14] | G | Future Internet 15(4) (Q2 0.808; MDPI/Scopus) | Non-systematic review | ICS/SCADA ransomware *prediction* literature is thin; GAN-experiment tabulation |
| 15 | Oosthoek et al. 2023 [15] | H | Communications of the ACM 66(8) (Q1; Scopus) | Empirical (on-chain) | Ransomwhere: 13,497 payments, 7,321 BTC addresses, 87 actors, >USD 101M |
| 16 | Meurs et al. 2024 [16] | H | Computers & Security 138 (Q1; ScienceDirect) | Game theory + empirics | Signaling game of double extortion; 452 attacks, 119 payments (27.8%) |
| 17 | Phipps & Nurse 2026 [17] | H | Computers & Security 160 (Q1 1.598; ScienceDirect) | PRISMA qualitative | Conti, LockBit, BlackCat/ALPHV: structure, retaliation, RaaS economics; >500 sources |
| 18 | Huck & Breitinger 2022 [18] | I | IEEE Security & Privacy 20(4) (Q1; IEEE Xplore) | Position/best practice | Forensic readiness neglected vs technical countermeasures |
| 19 | Shaked et al. 2023 [19] | I | Computers & Security 134 (Q1; ScienceDirect) | Conceptual + tool | Operations-informed playbooks embed dependency models; open-source artifact |
| 20 | Matthijsse et al. 2025 [20] | J | European J. Criminology 22(4) (Q1 1.029; Scopus/SAGE) | Empirical survey (n=445) | SMEs: low stated payment likelihood; expert advice ↑, backup absence ↑ willingness |
| 21 | Meurs et al. 2026 [21] | J | Global Crime 27(2-3) (Q1 0.609; Scopus) | Empirical register (n=502) | Dutch police data: 104/502 (20.7%) NAS attacks; DeadBolt key-recovery operation |
| 22 | Neprash et al. 2026 [22] | K | AEJ: Economic Policy 18(1) (Q1 7.737; Scopus/AEA) | Econometric (DiD) | −17–24% hospital volume wk1; +34–38% in-hospital mortality among admitted patients |
| 23 | Abouk & Powell 2024 [23] | K | JAMA 331(24) (Q1 5.843; PubMed) | Econometric (Research Letter) | ED visits −8.10% wk1, −16.21% wk2; recovery ≤ ~8 weeks; spillovers to nearby hospitals |
| 24 | Albshaier et al. 2024 [24] | L | Information 15(8) (Q2 0.805; MDPI) | PRISMA SLR | Early-detection approaches categorized; datasets/standardization gaps |
| 25 | Oz et al. 2022 [25] | L | ACM Computing Surveys 54(11s) (Q1 4.457; ACM) | Survey (n=137, 1989–2020) | Evolution + taxonomy + defense across PC/mobile/IoT; pre-RaaS-era canon |

### 3.3 Thematic synthesis

#### 3.3.1 Theme 1 — Detection at the host: ML promise, practicality deficit (RQ1, RQ6)

ML-based detection reviews converge on the same gap diagnosis. Ispahany et al. [1], reviewing ML approaches against the Cyber-Kill Chain, find most proposed systems are *reactive* (detect during or after mass encryption) and that early-detection potential is under-exploited because studies rarely map detectors to kill-chain stages; the same review reports dataset heterogeneity (ad-hoc VirusTotal-derived corpora) as the dominant reproducibility obstacle. Alzahrani et al. [2] independently reach the complementary conclusion from a 2019–2025 sweep: ML and non-ML method families each cover different zero-day/variant gaps, and 135→45 (Windows/Android) filtering left only papers whose datasets are fragmented and often unavailable.

The experimental end of host detection supports accuracy claims but exposes their fragility. XRan [7] reaches 99.4% TPR by fusing API/DLL/mutex sequences from Cuckoo sandbox runs with a two-layer CNN, and LIME/SHAP explanations "consistently identify the dynamic features driving ransomware behaviour" — yet its own limitations note runtime overhead, sandbox detectability/evadability, and Windows-centrism. Galli et al. [8] extend explainability to sequence models (SHAP/LIME/LRP/Attention over LSTM/GRU) and show *no single XAI method dominates* across dataset size/length/classes — i.e., explanation choice is itself an open methodological decision — while their datasets are proprietary ("authors do not have permission to share"), making the exact reproducibility bottleneck that Theme 1 reports a lived one.

**Consensus:** detection accuracy is largely a laboratory property; ML detectors remain reactive; dataset standardization is the field's binding constraint. **Controversy:** none on diagnosis, but no retained study offers a validated host-based early (pre-encryption) detector at production readiness.

#### 3.3.2 Theme 2 — Non-classical detection planes: storage, deception, and network (RQ1)

Two studies move detection below/outside the host. At the storage layer, AMOEBA [3] embeds content-based entropy/inspection in the SSD controller at NAND speed plus intra-device backup; it outperforms FlashGuard on performance/space, and device-level placement survives host-side evasion — limited however to simulator + OpenSSD prototype workloads and to content-level confounders (encrypted/compressed writes). At the deception layer, Android honeyfile monitoring [4] achieves near-zero steady-state cost (1–700 ms alert latency under 1–9 running apps, versus 10–70 ms for 8–60 KB encryption) with code open-sourced (FileMonitor), but patterns are hard-coded and the malware sample set is not a public dataset.

Network-plane detection splits by target: *ransomworm propagation* (MFMCNS [5]: fused session/time flow classifiers on WannaCry/NotPetya captures; pre-execution early warning, but worms only) versus *federated hybrid endpoint+network learning* (HFL-RD [6]: >95% accuracy on a 300-sample/30-family corpus assembled from public sources; superior unknown-variant detection time). The two network studies presuppose different deployment realities (enterprise PCAP sensors vs. multi-client federation) and were not compared head-to-head on shared data.

**Consensus:** each non-classical plane increases the kill-chain coverage window (pre-encryption or pre-execution). **Methodological note:** none releases the exact attack traffic/sample corpus as a packaged dataset — a Theme 1 weakness that propagates across planes.

#### 3.3.3 Theme 3 — Offensive AI: the threat side is now empirical (RQ2)

The retained literature crosses from speculation to empirical demonstration. Iturbe et al. [9] show an LLM-driven mechanism generating functional attack-technique code "from initial access vectors through impact actions (including encryption and extortion-related impact)", with multiple variants per technique and simulation-only validation; their framing (scoping simplicity, BAS integration) centres on the defender consequence: attack space drifts from fixed playbooks to generated variants. Gupta et al. [10] contribute the GenAI jailbreak/abuse evidence (social-engineering content, payload/polymorphic malware PoCs) and, importantly, parallel defensive uses. Neither paper associates AI-generated attacks with named RaaS operators or observed in-the-wild campaigns; the PromptLock narrative enters this literature only via a non-eligible preprint referenced as provenance lead in S1 — the strongest AI-era claims therefore rest on a weaker evidence tier than the rest of this review (see §4.3).

#### 3.3.4 Theme 4 — Prevention, resilience, and response machinery (RQ3)

Prevention work targets the two standard weaknesses: host containment and recovery. SEDAC [12] chains program-centric and user-centric access control as three stages and reports the prototype "intercepted more types of ransomware attack vectors than existing proposals" — all direct file-encryption activity blocked (File Warden), all unsafe MBR writes blocked (MBR Guard) — while indirect vectors (PowerShell/VM) and Microsoft's explicitly trusted directories formed the residual gap; Windows-only, and dependent on industry cooperation assumptions. On the resilience side, Ilau et al. [11] model organizational recovery compositionally (process-algebra; 9,000-config/450k-iteration simulation) demonstrating that recovery-mix choices can be quantified *before* deployment — situating the 21%-of-55-attacks empirical recovery context from prior case research.

Response-side, Huck & Breitinger [18] document systemic neglect of procedural/forensic countermeasures, and Shaked et al. [19] close a specific operational gap: playbooks that do not model organizational dependencies cannot communicate incident/response impact; their operations-informed playbook artifact is open-source. **Consensus:** prevention and response designs exist and are evaluated, but only against prototype/Windows or single-case deployments; organizational-scale validation is absent throughout.

#### 3.3.5 Theme 5 — RaaS economy, double extortion, and money (RQ4)

The threat-economy cluster contains the review's largest datasets. Oosthoek et al. [15] operated the Ransomwhere crowdsourced tracker and verify, on Bitcoin's public ledger, 13,497 payments across 7,321 addresses and 87 criminal actors (>$101M, ~5 years), separating commodity vs RaaS markets by on-chain behaviour: commodity market activity has actionable transaction choke points, while RaaS-linked tracing is the harder open problem. Meurs et al. [16] model double extortion as a signaling game calibrated with 452 real attacks (130 negotiations, 119 payments = 27.8%); exfiltration signaling raises requests to ~€3M (~€1.7M post-negotiation) and yields more profit — i.e., deception itself is a revenue strategy. Phipps & Nurse [17] combine a PRISMA protocol with >500 dispersed sources (leaked chats, court documents, vendor reports, leak sites) to characterize Conti, LockBit, and BlackCat/ALPHV operationally (business-like, brand-building, retaliation against victimizing retailers, RaaS affiliate enablement, multi-tier extortion, and retaliation dynamics against victims who publicize negotiations); the source catalog also records internal payment/economic behaviour of BlackCat/ALPHV, details of which are truncated in S1 and therefore not restated here.

On the victim side of the same market, Matthijsse et al. [20]'s vignette experiment on 445 Dutch SME owners finds low stated payment likelihood; willingness rises if a cybersecurity company advises paying or a backup is absent, and — counter-intuitively — is *not* significantly related to ransom affordability. Meurs et al. [21] show from 502 police-reported attacks (2019–2022) that 104 (20.7%) hit NAS devices (QNAP-appliance class), a consumer-grade platform largely absent from the ransomware literature, and document the 2022 DeadBolt operation in which Dutch police induced key release via on-chain communication.

**Consensus:** double extortion is operating successfully as a deception/profit strategy; payment-side intuition (affordability) is not supported as a driver; consumer NAS is a materially under-studied victim population. **Tension:** both coverage sources are subject to under-reporting — crowdsourced payment trackers capture only victim-reported payments [15], and police registers miss unreported incidents [21]; inferred payment/prevalence rates should both be read as lower bounds.

#### 3.3.6 Theme 6 — Quantified impact: the causal evidence arrives (RQ5)

The strongest methodological evidence in the review is clinical-econometric. Neprash et al. [22] link a constructed US hospital attack database to 100% Medicare FFS claims (event-study/continuous-treatment DiD): volume falls 17–24% in the attack week with ~3-week recovery, while in-hospital mortality among already-admitted patients rises 34–38% — the first estimates directly tying hospital ransomware to excess mortality; replication data/code are openly deposited (ICPSR). Abouk & Powell [23] independently quantify California hospital disruption (8 attacks, 15 hospitals): ED visits −8.10% (95% CI −14.40 to −1.80) week 1 and −16.21% (−26.58 to −5.84) week 2; inpatient admissions −8.16% and −16.62% with recovery within ~8 weeks, plus evidence of spillover to *unattacked* hospitals (displaced demand). Retained despite its Research Letter format, with that caveat recorded ([23]; S1). **Consensus:** ransomware's patient-care harms are now causal, not anecdotal. **Limitation carried over from both studies:** small attack samples, US/state single-geography, pre-2021 windows in [23].

#### 3.3.7 Theme 7 — Baseline SLRs and how position changed (RQ1/RQ6, comparison anchor)

Oz et al. [25] (137 studies, 1989–2020) established the dual canon: platform-diversified evolution narrative + defense taxonomy, with detection research workstation-dominant and evaluation-uniformity named an open issue. Albshaier et al. [24] (PRISMA SLR, 2020–2024, *early* detection focus) conclude that pre-encryption detection "is feasible only by combining warning signs, frameworks and proactive techniques" and rate ML/behavioural approaches the strongest proactive direction, again constrained by benchmarks. Relative to these baselines, the 2022–2026 verified journal record completes three shifts: (i) explanation layers are now being *measured* ([7], [8]), (ii) impact evidence moved from reported counts to causal estimation ([22], [23]), (iii) the threat-actor economy (leak-site operation, payment tracing, affiliate structure) acquired primary datasets ([15]–[17]) — while unchanged is the universal dataset/standardization complaint.

#### 3.3.8 Knowledge gaps (cross-theme)

- **Datasets:** ad-hoc, unshared, or proprietary corpora recur in every detection theme ([1]–[8]); no retained study validates on a common, public benchmark. This is the field's single loudest failure signal.
- **Early (pre-encryption) detection:** reviews demand it ([2], [24]); the closest realized implementations are deception/storage-plane ([3], [4]) and worm-propagation ([5]) designs with narrow applicable attacks.
- **Real-environment evaluation:** sandbox/simulator-based validation dominates detection studies; federated and on-chain studies depart from this but assume deployment contexts that nobody measured.
- **IIoT/ICS/NAS defense:** platform-expansion reviews (G [13], [14]) find no validated IIoT-specific detector; NAS victimology [21] documents an attack share (20.7%) without parallel defense literature.
- **AI-offense response surface:** [9], [10] demonstrate capability, but no retained study evaluates a *defense* against AI-generated polymorphic ransomware.
- **Integrated economics-defense evidence:** payment tracing [15] and victim decision modeling [20] exist without linkage to prevention/resilience effectiveness [11], [12].

---

## 4. Discussion

### 4.1 Principal findings

1. **Reactivity persists.** Both independent reviews and the experimental record agree that most published detection engages at/after the encryption stage; early-detection designs (honeyfiles, storage-level, propagation analysis) are the credible exceptions but are narrowly evaluated ([1], [2], [4], [5]).
2. **Explainability is measurable; datasets are not shareable.** XAI layers on ransomware/malware detectors can be benchmarked ([7], [8]) — yet the same cluster's dataset restrictions make replication of the *models* impossible for third parties, a structural (not incidental) reproducibility failure.
3. **Offensive AI is empirically demonstrated, defensively unaddressed.** LLM-generated attack chains including extortion-level impact exist as peer-reviewed evidence [9]; no equivalent *countermeasure validation* appears in the eligible record.
4. **The threat-actor economy has primary data.** On-chain verification [15], calibration on real negotiations [16], and PRISMA-structured actor analysis [17] jointly replace vendor-report reliance.
5. **Impact is causal and severe.** Hospital volume and mortality effects [22], ED disruption/spillovers [23] materially raise the stakes for prevention/resilience investment decisions ([11], [12], [19]).

### 4.2 Interpretation and implications

**For practice:** the evidence supports a layered posture: OS-level access control (SEDAC-style) to stop direct encryption vectors [12]; deception or storage-plane tripwires for evasion-prone hosts [3], [4]; network monitoring for campaign-level behavior [5], [6]; embedded in operations-aware playbooks [19]. Complementing these are economic instruments — attention to ransom-payment advice channels [20], consumer NAS hygiene/patching [21] — and the demonstrated value of open replication packages [22] when hosting new studies.

**For policy:** the finding that "advised to pay" and "no backup" increase payment willingness [20] supports regulator attention to ransom-payment advice channels and backup-adequacy requirements (NIS2-style); the NAS result [21] implies consumer-device security regulation (currently unregulated surfaces), and causal clinical impact [22], [23] strengthens healthcare-specific incident mandates.

**For research:** the priorities implied by §3.3.8 are clear: public standardized ransomware benchmarks; kill-chain-mapped early detection with public corpora; defense evaluations against AI-generated attack variants; and integration of payment-economy observability into detection/response testing.

### 4.3 Strengths and limitations of this review

**Strengths:** record-level provenance (every paper traceable to one of six allowed sources; quartiles verified via Scimago); verbatim documentation of exclusion and pruning decisions; explicit handling of registry citing errors (two corrected candidate registrations); extraction with uncertainty flagging rather than silent filling; Crossref verification of all 25 article DOIs; a strict eligibility bound that precludes ad-hoc relaxation.

**Limitations (by severity):**
- **Search-documentation failure (major).** Query strings, dates, and per-database result counts were not recorded; the search is not reproducible at query granularity. PRISMA 2020 items 7/8 are therefore only partially satisfiable, and coverage risks (keyword omission, date-bounded database snapshots) cannot be quantified.
- **Selection by design (major, declared).** Q1/Q2-journal-only inclusion removed conference-track reproducibility work (e.g., the ML-ransomware replicability systematization) — a relevance bias *against* the very Theme 1 dimension it measures — and excluded preprints for AI-offense claims.
- **Single pipeline/reviewer (moderate).** No independent second screening; ambiguity between "retained decisions" and "excluded records" in cluster-level bookkeeping (§2.5, Appendix A).
- **Uncertainty flags (moderate).** 25 `study_type` and 25 `evaluation_metrics` values failed verification and remain unconfirmed; thematic claims do not rest on these, but metric-level meta-synthesis is blocked (see §2.4, synthesis approach).
- **Language/geography (minor).** English-language academic sources dominate the allowed databases; the victimology records draw heavily on Dutch data.
- **Currency (minor).** The record closes at the 2026-10-24 verification date; AI-era claims may have moved.

**Impact of limitations on conclusions:** RQ1–RQ5 conclusions rest on retained full-texts and are robust to the search-log gap *only where confirmed evidence exists in ≥2 independent studies* (dataset fragmentation: [1], [2], [7], [8], [24]; causal impact: [22], [23]). RQ2 (AI offense) carries the weakest evidence tier of the review and should be read as "demonstrated capability", not prevalence.

### 4.4 Comparison with previous reviews

Against Oz et al. [25] (≈500-cited anchor, pre-2020 corpus): the present verified record extends the taxonomy through the RaaS/leak-site era, adds NAS [21] and IIoT landscape work [13] alongside the platform-uniformity complaint's answer (defense for those platforms remains a gap); and adds the patient-outcome layer [22], [23] — which did not exist pre-2020 — plus the threat-actor economic layer [15]–[17]. Against Albshaier et al. [24]: this review's addition is the constraint of quartile-verified *journals-within-window* screening with a documented decision log — while explicitly acknowledging the its own absence of query-level protocol documentation, which the PRISMA flow of [24] does provide. Neither prior review contains a defensible answer to ChatGPT/LLM-era offense; [9] and [10] shown here represent the first peer-reviewed empirical tier of that question.

### 4.5 Future research

1. **Standardized, public ransomware benchmarks** with kill-chain and platform stratification as a first-class artifact (addresses the dataset failure signal confirmed across 10+ studies in Themes 1–2).
2. **Pre-encryption detection validated on shared corpora**, not single-force paper corpora — combining deception, storage-plane, and network signals ([3]–[5]).
3. **Defense evaluation against AI-generated attack variants**, mirroring [9] as red-team input.
4. **Integrated decision models** joining payment economics (tracing [15]; victim factors [20]) with resilience investment [11].
5. **Independent rigorous re-screening of excluded conference/preprint literature** (e.g., EuroS&PW reproducibility work; PromptLock) to raise confidence beyond the journal-only bound.

---

## 5. Conclusions

1. For RQ1, verified 2022–2026 journal evidence describes a detection landscape that is broad but laboratory-bound: accurate classifiers, three non-classical planes (storage, deception, network), and no shared benchmark; results are best read as capability statements, not deployment evidence.
2. For RQ2–RQ4, ransomware's criminal structure now has primary-data publication: generated attack code [9], actor economics [15]–[17], real-payment/deception dynamics [16], [20], [21] — the strongest AI-offense *capability* evidence sits at preprint level and must be treated as provisional.
3. For RQ5, causal patient-harm evidence (mortality +34–38% [22]; ED care disruption and spillovers [23]) makes ransomware a quantifiable health threat, not only an IT one.
4. For RQ6, the field's dominant methodological failure is dataset unavailability and non-standardized evaluation — cutting across detection themes — and this review itself demonstrates the fix: record-level provenance, verbatim exclusion logs, and uncertainty flags over invented values.

**Evidence certainty:** moderate-high for impact/economic themes (multiple large datasets or causal designs); moderate for detection themes (high internal validity of prototypes, low external validity); low for AI-era preprint-driven claims.
**Translation readiness:** prevention/resilience designs are near deployment-ready on their target platforms (Windows/SSD); AI-offense defense is preliminary.

---

## 6. Declarations

**Funding:** none.
**Conflicts of interest:** none.
**Registration:** not registered (not eligible for PROSPERO; not yet on OSF).
**Author contributions:** catalog produced by a scripted multi-agent deep-research pipeline (per-item agents A–L); PRISMA-style restructuring, thematic synthesis, and verification performed in the present revision; single-reviewer limitations documented in §4.3.
**Data availability:** per-paper structured extractions: `results/*.json`; full per-study catalog: Supplementary S1 `extraction_catalog.md`; prune logic: `prune_results.py`; schema: `fields.yaml`; citation-verification results: this §2.5 and the Crossref log retained in the workspace.

---

## 7. References

*(IEEE-style numeric, listed in thematic order of Table 1; every entry Crossref-verified 2026-10-24, per §2.5)*

1. Ispahany, J.; Islam, M.R.; Islam, M.Z.; Khan, M.A. Ransomware Detection Using Machine Learning: A Review, Research Limitations and Future Directions. *IEEE Access* **12** (2024). doi:10.1109/access.2024.3397921
2. Alzahrani, S.; Xiao, Y.; Asiri, S.; Zheng, J.; Li, T. A Survey of Ransomware Detection Methods. *IEEE Access* **13**, 57943–57982 (2025). doi:10.1109/access.2025.3556187
3. Min, D.; Ko, Y.; Walker, R.; Lee, J.; Kim, Y. A Content-Based Ransomware Detection and Backup Solid-State Drive for Ransomware Defense. *IEEE Trans. Computer-Aided Design of Integrated Circuits and Systems* **41**, 7, 2038–2051 (2022). doi:10.1109/tcad.2021.3099084
4. Gómez-Hernández, J.A.; García-Teodoro, P. Lightweight Crypto-Ransomware Detection in Android Based on Reactive Honeyfile Monitoring. *Sensors* **24**, 9, 2679 (2024). doi:10.3390/s24092679
5. Almashhadani, A.O.; Carlin, D.; Kaiiali, M.; Sezer, S. MFMCNS: a multi-feature and multi-classifier network-based system for ransomworm detection. *Computers & Security* **119**, 102860 (2022). doi:10.1016/j.cose.2022.102860
6. Lan, K.; Li, G.; Huang, W.; Li, J. HFL-RD: Heterogeneous Federated Learning-Empowered Ransomware Detection via APIs and Traffic Features. *IEEE Trans. Network and Service Management* (2025). doi:10.1109/tnsm.2025.3574716
7. Gulmez, S.; Gorgulu Kakisim, A.; Sogukpinar, I. XRan: Explainable deep learning-based ransomware detection using dynamic analysis. *Computers & Security* **139**, 103703 (2024). doi:10.1016/j.cose.2024.103703
8. Galli, A.; La Gatta, V.; Moscato, V.; Postiglione, M.; Sperli, G. Explainability in AI-based behavioral malware detection systems. *Computers & Security* **141**, 103842 (2024). doi:10.1016/j.cose.2024.103842
9. Iturbe, E.; Llorente-Vazquez, O.; Rego, A.; Rios, E.; Toledo, N. Unleashing offensive artificial intelligence: Automated attack technique code generation. *Computers & Security* **148**, 104077 (2024). doi:10.1016/j.cose.2024.104077
10. Gupta, M.; Akiri, C.; Aryal, K.; Parker, E.; Praharaj, L. From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy. *IEEE Access* **11** (2023). doi:10.1109/access.2023.3300381
11. Ilau, M.-C.; Baldwin, A.; Caulfield, T.; Pym, D. Modelling and simulating organizational ransomware recovery: structure, methodology, and decisions. *Journal of Cybersecurity* **11**, tyaf035 (2025). doi:10.1093/cybsec/tyaf035
12. McIntosh, T.; Kayes, A.S.M.; Chen, Y.-P.P.; Ng, A.; Watters, P. Applying staged event-driven access control to combat ransomware. *Computers & Security* **128**, 103160 (2023). doi:10.1016/j.cose.2023.103160
13. Al-Hawawreh, M.; Alazab, M.; Ferrag, M.A.; Hossain, M.S. Securing the Industrial Internet of Things against ransomware attacks: a comprehensive analysis of the emerging threat landscape and detection mechanisms. *Journal of Network and Computer Applications* **223**, 103809 (2024). doi:10.1016/j.jnca.2023.103809
14. Gazzan, M.; Sheldon, F.T. Opportunities for Early Detection and Prediction of Ransomware Attacks against Industrial Control Systems. *Future Internet* **15**, 4, 144 (2023). doi:10.3390/fi15040144
15. Oosthoek, K.; Cable, J.; Smaragdakis, G. A Tale of Two Markets: Investigating the Ransomware Payments Economy. *Communications of the ACM* **66**, 8, 74–83 (2023). doi:10.1145/3582489
16. Meurs, T.; Cartwright, E.; Cartwright, A.; Junger, M.; Abhishta, A. Deception in double extortion ransomware attacks: an analysis of profitability and credibility. *Computers & Security* **138**, 103670 (2024). doi:10.1016/j.cose.2023.103670
17. Phipps, A.; Nurse, J.R.C. Inside ransomware groups: an analysis of their origins, structures, and dynamics. *Computers & Security* **160**, 104705 (2026). doi:10.1016/j.cose.2025.104705
18. Huck, J.; Breitinger, F. Wake Up Digital Forensics' Community and Help Combat Ransomware. *IEEE Security & Privacy* **20**, 4, 61–70 (2022). doi:10.1109/msec.2021.3137018
19. Shaked, A.; Cherdantseva, Y.; Burnap, P.; Maynard, P. Operations-informed incident response playbooks. *Computers & Security* **134**, 103454 (2023). doi:10.1016/j.cose.2023.103454
20. Matthijsse, S.R.; Moneva, A.; van 't Hoff-de Goede, M.S.; Leukfeldt, E.R. Examining ransomware payment decision-making among small- and medium-sized enterprises. *European Journal of Criminology* **22**, 4, 625–645 (2025; online first 2024). doi:10.1177/14773708241285671
21. Meurs, T.; Hoheisel, R.; Junger, M.; Abhishta, A. NAS ransomware: ransomware targeting NAS devices. *Global Crime* **27**, 2–3, 135–158 (2026; online first 2025). doi:10.1080/17440572.2025.2591628
22. Neprash, H.; McGlave, C.; Nikpay, S. Hacked to Pieces? The Effects of Ransomware Attacks on Hospitals and Patients. *American Economic Journal: Economic Policy* **18**, 1, 256–281 (2026). doi:10.1257/pol.20240594 — replication package: https://doi.org/10.3886/E235483V1 (ICPSR; not Crossref-registered, see §2.5)
23. Abouk, R.; Powell, D. Ransomware Attacks, ED Visits and Inpatient Admissions in Targeted and Nearby Hospitals. *JAMA* **331**, 24, 2129–2131 (2024). doi:10.1001/jama.2024.7752
24. Albshaier, L.; Almarri, S.; Rahman, M.M.H. Earlier Decision on Detection of Ransomware Identification: A Comprehensive Systematic Literature Review. *Information* **15**, 8, 484 (2024). doi:10.3390/info15080484
25. Oz, H.; Aris, A.; Levi, A.; Uluagac, A.S. A Survey on Ransomware: Evolution, Taxonomy, and Defense Solutions. *ACM Computing Surveys* **54**, 11s, 238 (2022). doi:10.1145/3514229

---

## 8. Appendices

### Appendix A — Excluded/pruned record log (summary; verbatim decisions in S1)

| Cluster | Record | Decision | Reason (category) |
|---|---|---|---|
| A | Chaieb et al., "ESAI 2024" conference paper | EXCLUDED | Venue (conference, not SJR-indexed journal); also mis-dated in registry |
| A | "AI-Based Ransomware Detection: A Comprehensive Review" (2024) | PRUNED | Overlap with [1], [2] |
| A | "The Age of Ransomware" survey (2023) | PRUNED | Overlap with [1], [2]; earliest of three overlapping records |
| B | Honeyfile-based Android detection — *Sensors* | RETAINED (verified) | Candidate accurate |
| B | Min et al. *IEEE TCAD* 2022 | RETAINED (verified) | Candidate accurate |
| B | Fang et al., R-Locker honeyfiles, *Mathematics* 2025 | Added, then PRUNED | Dataset disclosure unresolvable; overlap with [4] |
| C | 3-paper cluster (Berrueta/Almashhadani/Lan) | RETAINED/PRUNED | Berrueta pruned as oldest overlapping traffic-detection record |
| C | HyperVision (IEEE/ACM ToN 2024) | EXCLUDED | General encrypted-malware-traffic detector without ransomware-specific evaluation |
| D | Pereira et al., EuroS&PW 2026 | PRUNED | Workshop proceedings, no SJR quartile |
| E | "Ransomware 3.0" arXiv preprint | PRUNED | No peer-reviewed version as of 2026-10-21; retained as provenance lead only |
| F | Zhang et al. 2023, game theory | PRUNED | Scope (most tangential prevention model) |
| I | Bajpai & Enbody 2023, Digital Threats | PRUNED | Q2 misquoted as Q1; overlaps [19] |
| I | Kara & Aydos 2022, ESWA | PRUNED | Overlaps [18] forensic-readiness scope |
| K | JAMA Network Open 2025 breach-trend paper | PRUNED | Overlap; causal evidence retained via [22], [23] |

Summary: venue/design-level failures (n=3), record-overlap prunes (n=9), scope prune (n=1), preprint eligibility (n=1), dataset-disclosure prune (n=1), plus 2 retained-verification entries recorded inside cluster transcripts (bookkeeping ambiguity noted in §2.5).

### Appendix B — PRISMA 2020 checklist (summary; full checklist to be attached at manuscript submission)

| Section | Item | Reported? | Where |
|---|---|---|---|
| Title/Abstract | Identify as systematic review; structured abstract | Yes | Title; Abstract |
| Introduction | Rationale, objectives | Yes | §1 |
| Methods (eligibility) | Criteria defined with reason | Yes | §2.2, §2.4 |
| Methods (sources) | All databases with dates searched | **Partial** — sources listed; dates/strings not recorded | §2.2 + limitation §4.3 |
| Methods (search) | Full electronic/search strategies | **No** | §2.2 limitation |
| Methods (selection) | Process for selecting studies | Yes (record level) | §2.3 |
| Methods (data) | Data extraction method | Yes | §2.4 |
| Methods (risk of bias) | Tool used | **No formal tool** — proxy documented | §2.4, §4.3 |
| Methods (synthesis) | Approach | Yes | §2.4 |
| Results (selection flow) | PRISMA flow with counts | Partial (counts at eligibility stage; upstream counts not recorded) | §2.3 |
| Results (characteristics) | Study characteristics | Yes | §3.2 |
| Results (synthesis) | Thematic synthesis with sources | Yes | §3.3 |
| Discussion | Evidence, limitations, conclusions | Yes | §4, §5 |
| Other | Funding, COI, data availability | Yes | §6 |

### Appendix C — Uncertainty register (as recorded in S1)

- Inline `[uncertain]` fields failing verification and shown as `*[uncertain]*`: **study_type × 25 (all studies)**; **evaluation_metrics × 25**.
- Cluster-level uncertainty entries (pipeline-booked 28): dataset_benchmark (B, D, E, F, I, J, L, K, S1 fragments), platform_environment (D, E, F), quartile_sjr (D, E), journal (E), reproducibility (D, E, F, J, K, L), threat_actor_fields (G, I), evaluation_metrics (F, G, H, I, L).
- Consequence: study-type counts in Table 1 use reviewer categorization (declared); no metric-level meta-analysis was possible (§2.4); all thematic conclusions avoid unsupported metric-specific claims.

### Appendix D — Supplementary files and resources

- **S1 — `extraction_catalog.md`:** the original per-study extraction catalog (12 clusters, fields per study, verbatim exclusion transcripts), preserved unchanged.
- **S2 — `results/*.json`:** structured per-cluster extraction data validated during the pipeline.
- **S3 — Guidelines:** PRISMA 2020 (prisma-statement.org), Cochrane Handbook (training.cochrane.org/handbook), Scimago (scimagojr.com), PRISMA 2020 flow diagram (prisma-statement.org/prisma-2020-flow-diagram).
- **Skill attribution:** review restructured and verified following a literature-review methodology skill; search/citation phases documented per skill's reproducibility requirements.

---

*Verification log (2026-10-24): Crossref metadata check returned REGISTERED + title-match for all 25 article DOIs (70 titles, venues, years matched as listed in §7); `10.3886/E235483V1` unresolved in Crossref (ICPSR handle provider outside Crossref coverage) and retained with documentation (§2.5); doi.org Handle-API pass unavailable in this environment (TLS interception), documented in §2.5. PDF generation via skill tooling was skipped: pandoc/xelatex are not installed on this machine; the docx deliverables (generated by `generate_docx.py` from `results/`) remain unchanged.*

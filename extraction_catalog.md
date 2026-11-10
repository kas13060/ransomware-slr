# Ransomware detection, prevention, and incident response — systematic literature review (PRISMA-style)

> **Source constraint:** Google Scholar · IEEE Xplore · ScienceDirect · Scimago SJR · Scopus · PRISMA statement
> **Eligibility:** 2022–2026 · Q1/Q2 (Scimago SJR) · papers retained: **25**

## Table of contents

1. [A. AI/ML-based ransomware detection](#a-aiml-based-ransomware-detection) — Papers: 2 | Years: 2024–2025 | Best quartile: Q1 | Journals: IEEE Access (Vol. 12, IEEE Access (Vol. 13
2. [B. Behavioural, content & deception-based detection](#b-behavioural-content--deception-based-detection) — Papers: 2 | Years: 2022–2024 | Best quartile: Q1 | Journals: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (Vol. 41, Sensors (MDPI)
3. [C. Traffic & network-based detection](#c-traffic--network-based-detection) — Papers: 2 | Years: 2022–2025 | Best quartile: Q1 | Journals: Computers & Security (Elsevier), IEEE Transactions on Network and Service Management
4. [D. Explainability, reproducibility & benchmark validity](#d-explainability-reproducibility--benchmark-validity) — Papers: 2 | Years: 2024–2024 | Best quartile: Q1 | Journals: Computers & Security
5. [E. AI-era threat models (LLM/GenAI ransomware)](#e-ai-era-threat-models-llmgenai-ransomware) — Papers: 2 | Years: 2023–2024 | Best quartile: Q1 | Journals: Computers & Security (Elsevier), IEEE Access
6. [F. Prevention & resilience engineering](#f-prevention--resilience-engineering) — Papers: 2 | Years: 2023–2025 | Best quartile: Q1 | Journals: Computers & Security, Journal of Cybersecurity (Oxford University Press)
7. [G. Platform expansion (OT/IoT/ICS, cloud/hypervisor, cross-platform)](#g-platform-expansion-otiotics-cloudhypervisor-cross-platform) — Papers: 2 | Years: 2023–2024 | Best quartile: Q1 | Journals: Future Internet (MDPI), Journal of Network and Computer Applications (Elsevier)
8. [H. RaaS, double extortion & payment tracing](#h-raas-double-extortion--payment-tracing) — Papers: 3 | Years: 2023–2026 | Best quartile: Q1 | Journals: Communications of the ACM, Computers & Security (Elsevier)
9. [I. Incident response, playbooks & forensic readiness](#i-incident-response-playbooks--forensic-readiness) — Papers: 2 | Years: 2022–2023 | Best quartile: Q1 | Journals: Computers & Security (Elsevier), IEEE Security & Privacy
10. [J. Victimology, economics & regulatory response](#j-victimology-economics--regulatory-response) — Papers: 2 | Years: 2025–2026 | Best quartile: Q1 | Journals: European Journal of Criminology (SAGE, Global Crime (Taylor & Francis / Routledge; ISSN 1744-0572)
11. [K. Sectoral empirical impact studies](#k-sectoral-empirical-impact-studies) — Papers: 2 | Years: 2024–2026 | Best quartile: Q1 | Journals: American Economic Journal: Economic Policy (American Economic Association; ISSN 1945-7731), JAMA (American Medical Association; ISSN 0098-7484) - Research Letter
12. [L. Taxonomies & prior systematic reviews (co-citation baseline)](#l-taxonomies--prior-systematic-reviews-co-citation-baseline) — Papers: 2 | Years: 2022–2024 | Best quartile: Q1 | Journals: ACM Computing Surveys (CSUR) (Association for Computing Machinery; ISSN 0360-0300), Information (MDPI; ISSN 2078-2489). CORRECTION of candidate-registry entry: the candidate paper was registered as 'Albshaier et al. 2024 Applied Sciences'
## 1. A. AI/ML-based ransomware detection

**Papers retained: 2** · Excluded records: 3 · Uncertain fields: 0

<details><summary>Excluded records (PRISMA transparency)</summary>

- candidate_as_cited=Chaieb et al. 2023 IEEE Access (AI ransomware detection taxonomy); actual_record=Chaieb, O.; Kannouf, N.; Benabdellah, M. 'A Systematic Review and Taxonomy of Ransomware Detection Based on Artificial Intelligence Algorithms', 2024 3rd International Conference on Embedded Systems and Artificial Intelligence (ESAI), IEEE Xplore record 10913856, DOI 10.1109/ESAI62891.2024.10913856; decision=EXCLUDED; reason=Conference proceeding (ESAI 2024), not a Scimago SJR-indexed Q1/Q2 journal; also published 2024/2025, not 2023 as cited. Replaced in the cluster by Razaulla et al. 2023 IEEE Access survey (Q1), which provides the equivalent AI-ransomware-detection taxonomy anchor.
- paper_ref=ferdous2024; decision=PRUNED; title=AI-Based Ransomware Detection: A Comprehensive Review; reason=Record-overlap prune: AI-detection scope redundant with isphany2024_ml_review and alzahrani2025_survey_detection_methods
- paper_ref=razaulla2023; decision=PRUNED; title=The Age of Ransomware: A Survey on the Evolution, Taxonomy, and Research Directions; reason=Record-overlap prune: coverage of ransomware evolution/taxonomy redundant with alzahrani2025 (2019-2025 survey) and isphany2024; earliest of three overlapping IEEE Access reviews

</details>

### 1.1 Ransomware Detection Using Machine Learning: A Review, Research Limitations and Future Directions

*Ispahany, J.; Islam, M.R.; Islam, M.Z.; Khan, M.A. (2024). IEEE Access (Vol. 12, published 7 May 2024). Q1 (Scimago SJR 2024, Computer Science (miscellaneous): SJR 0.849, Q1). [https://doi.org/10.1109/ACCESS.2024.3397921](https://doi.org/10.1109/ACCESS.2024.3397921) `retained-included` · `IEEE Xplore (record 10521643)`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Structured review of ML-based ransomware detection literature. Search terms: 'ransomware', 'detection', 'machine learning', 'deep learning' across academic archives. Proposes a taxonomy of detection phases, ML techniques and system designs; maps studies onto the Cyber-Kill Chain (CKC) to determine t …
- **key_findings:** Most proposed ML detection systems lack practicality for real-world attacks and are reactive with delayed detection; early-detection potential is under-exploited because studies are rarely mapped to CKC stages; dataset heterogeneity (most studies build ad-hoc datasets from VirusTotal etc.) impedes c …
- **limitations:** Acknowledged: prior surveys neglect system design and real-time/early detection practicality; most reviewed studies rely on non-standardised, self-built datasets; many reviewed systems are reactive and cannot handle modern evasion. Observed: the review itself does not empirically validate any detect …
- **research_gaps:** Gap in practical, real-time and early (CKC-aligned) detection designs; need for standardised benchmark datasets; need for systems robust to evasion techniques used by modern ransomware families; gap between laboratory accuracy and real-world deployability.

**prisma**

- **inclusion_rationale:** Passes: published May 2024, IEEE Access SJR Q1 (0.849, 2024), IEEE Xplore record 10521643 verified; directly relevant as a review of ML-based ransomware detection with CKC-aligned early-detection taxonomy.

**stratification**

- **platform_environment:** Multi-platform review; Windows endpoints emphasised (Sysmon/log-based detection designs), Android also covered
- **kill_chain_stage:** Explicitly maps detection studies to Cyber-Kill Chain stages; advocates pre-encryption/early detection before T1485 (Data Encrypted for Impact); distinguishes early vs real-time detection
- **dataset_benchmark:** Collates a list of ransomware detection datasets used in the literature (section IV-B2), including VirusTotal-derived self-built corpora; notes most are not open-sourced and non-standardised
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate risk: review includes dataset catalogue enabling partial replication of reviewed settings; notes most primary studies use self-built datasets and sandbox-only evaluation, limiting external validation of the field's claims

**threat_intel**

- **threat_actor_fields:** Partially applicable: reviews recent ransomware families, attack trends and TTPs observed in the wild, and government responses; no leak-site or payment-wallet tracing analysis

---

### 1.2 A Survey of Ransomware Detection Methods

*Alzahrani, S.; Xiao, Y.; Asiri, S.; Zheng, J.; Li, T. (2025). IEEE Access (Vol. 13, pp. 57943-57982, published 1 April 2025). Q1 (Scimago SJR 2025, Computer Science (miscellaneous): SJR 0.884, Q1). [https://doi.org/10.1109/ACCESS.2025.3556187](https://doi.org/10.1109/ACCESS.2025.3556187) `retained-included` · `IEEE Xplore (record 10945868); cross-verified via DOAJ record 655bae4ce3c4475d9e4fa3f3471db122`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Survey of detection literature 2019-2025: 135 papers initially reviewed and filtered by scope and venue; 45 papers focused on Windows or Android detection selected for in-depth analysis. Methods categorised into ML-based and non-ML-based with advantages/drawbacks of each; dedicated analysis of Ranso …
- **key_findings:** ML-based and non-ML-based detection methods each have complementary strengths and weaknesses for zero-day/unknown variants; RaaS lowers the entry barrier for attackers and drives attack growth; reviewed datasets are fragmented and often unavailable, limiting reproducibility; identifies gaps and futu …
- **limitations:** Acknowledged: reviewed datasets have structural limitations and restricted availability; detection methods struggle with zero-day and unknown variants. Observed: in-depth analysis restricted to Windows and Android only (other platforms excluded from the 45-paper core set); selection criteria ('filte …
- **research_gaps:** Need for more effective and dynamic detection of zero-day/unknown variants; dataset availability and standardisation gaps; understanding of RaaS-driven threat landscape needs to be integrated into detection research; robustness of current methods across OS platforms.

**prisma**

- **inclusion_rationale:** Passes: published April 2025, IEEE Access SJR Q1 (0.884, 2025), IEEE Xplore record 10945868 verified; covers detection methods 2019-2025 including RaaS, extending the cluster's temporal coverage.

**stratification**

- **platform_environment:** Windows and Android operating systems (45 in-depth papers restricted to these two platforms)
- **kill_chain_stage:** Detection methods reviewed span pre-encryption (early/behavioural indicators) through during-encryption (T1485); encryption-stage focus dominates
- **dataset_benchmark:** Catalogues datasets used in the 45 reviewed papers with their structures and limitations; notes availability/reproducibility limitations; no new dataset released
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate risk: 135->45 paper filtering is described but not formalised (no PRISMA flow diagram); dataset catalogue supports reproducibility of reviewed experiments where datasets are public; no new empirical evaluation

**threat_intel**

- **threat_actor_fields:** Applicable: dedicated section on Ransomware-as-a-Service (RaaS) explaining its operation and its effect on the increase in ransomware attacks; no leak-site evidence or payment-wallet tracing coverage

---

## 2. B. Behavioural, content & deception-based detection

**Papers retained: 2** · Excluded records: 4 · Uncertain fields: 1

<details><summary>Excluded records (PRISMA transparency)</summary>

- candidate_as_cited=Min et al. 2022 IEEE TCAD; actual_record=Min, D.; Ko, Y.; Walker, R.; Lee, J.; Kim, Y. 'A Content-Based Ransomware Detection and Backup Solid-State Drive for Ransomware Defense', IEEE TCAD 41(7):2038-2051, July 2022; decision=RETAINED; reason=Candidate description verified accurate; online-first 2021 but issue year 2022, SJR Q1 2022.
- candidate_as_cited=Honeyfile-based Android ransomware detection - Sensors 2024 (PMC11085278); actual_record=Gómez-Hernández, J.A.; García-Teodoro, P. 'Lightweight Crypto-Ransomware Detection in Android Based on Reactive Honeyfile Monitoring', Sensors 24(9):2679, 2024; decision=RETAINED; reason=Candidate description verified accurate; Sensors SJR Q1 (Instrumentation) in 2024.
- candidate_as_cited=None (supplementary search hit); actual_record=Fang, X.; Song, E.; Ning, C.; Huseynov, H.; Saadawi, T. 'Crypto-Ransomware Detection Through a Honeyfile-Based Approach with R-Locker', Mathematics 13(12):1933, 2025; decision=RETAINED; reason=Added via DOAJ/MDPI search to give the deception pillar a third 2022-2026 record; Mathematics is SJR Q2 in 2025.
- paper_ref=fang2025; decision=PRUNED; title=Crypto-Ransomware Detection Through a Honeyfile-Based Approach with R-Locker; reason=Validity prune: dataset_benchmark unidentifiable (uncertain), and honeyfile approach overlaps gomezhernandez2024_honeyfile_android which has full parameter disclosure

</details>

<details><summary>Uncertain fields in this cluster</summary>

- dataset_benchmark

</details>

### 2.1 A Content-Based Ransomware Detection and Backup Solid-State Drive for Ransomware Defense

*Min, D.; Ko, Y.; Walker, R.; Lee, J.; Kim, Y. (2022). IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (Vol. 41, No. 7, July 2022, pp. 2038-2051; first published online 26 July 2021). Q1 (Scimago SJR 2022: SJR 0.971; Q1 in Computer Graphics and Computer-Aided Design and in Electrical and Electronic Engineering, Q2 in Software). [https://doi.org/10.1109/TCAD.2021.3099084](https://doi.org/10.1109/TCAD.2021.3099084) `retained-included` · `IEEE Xplore (record 9493745); cross-verified via dblp (TCAD Vol. 41) and Korea University Pure repository`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Device-level defense inside the SSD controller: (1) a hardware accelerator runs content-based detection algorithms at NAND-flash speed to identify ransomware-encrypted pages (entropy/content analysis of page data inside the FTL), and (2) a fine-grained backup control mechanism maintains intra-device …
- **key_findings:** AMOEBA achieves high ransomware detection accuracy with negligible performance overhead, and outperforms FlashGuard in performance and space efficiency for intra-device backup; the hardware-accelerated content-based detector catches encryption activity even when host-level detection is evaded, and t …
- **limitations:** Acknowledged/observed: detection relies on content-level indicators of encryption, so encryption-at-rest or compressed/already-encrypted writes may confound it; evaluation is simulator-based (Microsoft SSD simulator) plus an OpenSSD prototype rather than mass-market SSD hardware; device-level backup …
- **research_gaps:** Gap addressed: ransomware that evades host-level behavioural detection and destroys software backups - solved by moving detection and backup into the storage device itself. Remaining gaps: scaling hardware content-inspection to modern SSD workloads, defending against ransomware-aware storage attacks …

**prisma**

- **inclusion_rationale:** Passes: journal issue dated July 2022 (within 2022-2026; online-first July 2021), IEEE TCAD is SJR Q1 in 2022 (SJR 0.971), sourced from IEEE Xplore (record 9493745 verified via dblp). Core content-based detection + backup-SSD candidate as nominated.

**stratification**

- **platform_environment:** Storage-device level (SSD controller/FTL); evaluated on Microsoft SSD simulator and OpenSSD platform with host workloads from Windows ransomware execution
- **kill_chain_stage:** During-encryption detection (content inspection of pages as they are written, T1485) plus post-encryption recovery via intra-SSD backup restore
- **dataset_benchmark:** Real ransomware workloads: block-level I/O traces collected while running actual ransomware against the Microsoft SSD simulator and OpenSSD prototype; benchmarked against FlashGuard SSD; traces not stated to be publicly open-sourced
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate risk: real-environment grounding via OpenSSD hardware prototype and real ransomware traces strengthens validity, but the simulator setup and trace datasets are not clearly released, limiting independent replication; baseline comparison to FlashGuard provided

**threat_intel**

- **threat_actor_fields:** Not applicable: no RaaS group naming, leak-site evidence or payment-wallet tracing

---

### 2.2 Lightweight Crypto-Ransomware Detection in Android Based on Reactive Honeyfile Monitoring

*Gómez-Hernández, J.A.; García-Teodoro, P. (2024). Sensors (MDPI), Vol. 24, Issue 9, Article 2679, published 23 April 2024; PMID 38732785, PMCID PMC11085278. Q1 (Scimago SJR 2024: SJR 0.764; Q1 in Instrumentation and Analytical Chemistry, Q2 in Information Systems and Electrical and Electronic Engineering). [https://doi.org/10.3390/s24092679](https://doi.org/10.3390/s24092679) `retained-included` · `PubMed Central (PMC11085278); cross-verified via MDPI (doi.org/10.3390/s24092679) and DOAJ`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Deception + reactive monitoring: honeyfiles (hidden, attractively named trap files) are deployed across the external-storage directory tree; Android's FileObserver service (wrapping Linux inotify) raises kernel-driven alerts when trap files are accessed in suspicious sequences, without continuous po …
- **key_findings:** Reactive honeyfile monitoring achieves high detection accuracy at near-zero steady-state resource cost: notifying 200 monitored events took 1-200 ms with 1 running app, 1-450 ms with 4 apps, and 1-700 ms with 9 apps; encrypting a file takes 10 ms (8 KB) or 70 ms (60 KB), so with distributed 60 KB de …
- **limitations:** Acknowledged: evaluation must be extended with more crypto-ransomware and other file-targeting malware samples (limited by dataset resources); detection depends on correct characterisation of file-access sequences, else false alerts occur. Observed: detection patterns are hard-coded in the app (no c …
- **research_gaps:** Gap addressed: ML-based ransomware detectors are too computationally heavy for resource-limited mobile/IoT devices - solved with lightweight reactive deception. Remaining gaps: larger-scale malware evaluation, configurable detection patterns, and integration with broader mobile security frameworks ( …

**prisma**

- **inclusion_rationale:** Passes: published April 2024, Sensors is SJR Q1 in 2024 (Instrumentation; SJR 0.764), verified via PMC11085278 / DOI 10.3390/s24092679. Nominated candidate confirmed accurate (honeyfile-based Android ransomware detection, Sensors 2024).

**stratification**

- **platform_environment:** Android (external storage; FileObserver/inotify); builds on the authors' prior Linux and Windows R-Locker deployments
- **kill_chain_stage:** Pre-encryption / early detection: traps are accessed during the ransomware's file-scanning/encryption ramp-up (T1485), before mass encryption completes
- **dataset_benchmark:** Real crypto-ransomware samples executed on Android test devices; the FileMonitor monitoring app is open-sourced on GitHub (github.com/JA-Gomez-Hernandez/FileMonitor); the ransomware sample set itself is not released as a named public dataset
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Good: FileMonitor app code is publicly available on GitHub and evaluation used real Android devices with real samples; the exact ransomware sample list and versions are described in the paper but not packaged as a public dataset

**threat_intel**

- **threat_actor_fields:** Not applicable: no RaaS group naming, leak-site evidence or payment-wallet tracing

---

## 3. C. Traffic & network-based detection

**Papers retained: 2** · Excluded records: 3 · Uncertain fields: 0

<details><summary>Excluded records (PRISMA transparency)</summary>

- candidate_as_cited=Suggested venues: Expert Systems with Applications / Computers & Security / IEEE Access 2022-2026; actual_record=Three papers retained: Berrueta et al. (ESWA 2022), Almashhadani et al. (C&S 2022), Lan et al. (IEEE TNSM 2025); decision=RETAINED (3 papers); reason=All three are SJR Q1 journal papers from allowed databases (ScienceDirect, IEEE Xplore), within 2022-2026, and squarely on encrypted-traffic analysis / network IDS for ransomware. No candidate in this cluster required exclusion; conference papers encountered during search (e.g., IEEE CNS 2024 contex …
- candidate_as_cited=HyperVision - Flow Interaction Graph Analysis (IEEE/ACM Transactions on Networking 2024); actual_record=Fu, C.; Li, Q.; Xu, K. IEEE/ACM ToN 32(4):2972-2987, 2024; decision=EXCLUDED from cluster C; reason=Q1 journal and methodologically relevant to encrypted malicious traffic, but it is a general encrypted-malware-traffic detector (140 generic attacks) with no ransomware-specific evaluation, so it was deprioritised in favour of ransomware-specific network detection papers to keep cluster C on-topic.
- paper_ref=berrueta2022; decision=PRUNED; title=Crypto-ransomware detection using machine learning models in file-sharing network scenarios with encrypted traffic; reason=Recency/overlap prune: oldest traffic-based record (2022); encrypted-traffic detection scope covered by almashhadani2022 (in-network) and lan2025 (federated, current)

</details>

### 3.1 MFMCNS: a multi-feature and multi-classifier network-based system for ransomworm detection

*Almashhadani, A.O.; Carlin, D.; Kaiiali, M.; Sezer, S. (2022). Computers & Security (Elsevier), Article 102860, published online 28 July 2022. Q1 (Scimago SJR 2022: SJR 1.605; Q1 in Computer Science (miscellaneous) and Law). [https://doi.org/10.1016/j.cose.2022.102860](https://doi.org/10.1016/j.cose.2022.102860) `retained-included` · `ScienceDirect (Elsevier); DOI 10.1016/j.cose.2022.102860; cross-verified via Scopus-indexed citation records`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Comprehensive behavioural analysis of ransomworm (self-propagating ransomware) network traffic using WannaCry and NotPetya as case studies. Two independent feature sets are extracted at two flow levels: session-based and time-based; an independent classifier is built on each set; MFMCNS runs the cla …
- **key_findings:** MFMCNS proved reliable with high detection accuracy against ransomworm propagation traffic (WannaCry, NotPetya); combining session-based and time-based flow classifiers through a fusion rule improves reliability over single-view network detection; network-based detection can catch ransomworm activit …
- **limitations:** Acknowledged/observed: evaluation limited to two worm-propagating campaigns (WannaCry, NotPetya); method targets propagation-phase traffic, so ransomware without self-spreading behaviour (classic crypto-lockers) is not the detection target; specific accuracy figures vary by flow level and are report …
- **research_gaps:** Gap addressed: host-based methods only detect after infection and payload execution, whereas network-based analysis of ransomworm propagation enables pre-execution early warning. Remaining gaps: generalisation beyond WannaCry/NotPetya-style worms, robustness to encryption of propagation traffic, and …

**prisma**

- **inclusion_rationale:** Passes: published 2022, Computers & Security is SJR Q1 (1.605, 2022), sourced from ScienceDirect (allowed database); anchors the network IDS pillar for ransomware campaign (ransomworm propagation) detection.

**stratification**

- **platform_environment:** Network-level (enterprise/campus networks); campaign targets are Windows systems (WannaCry, NotPetya)
- **kill_chain_stage:** Pre-encryption / pre-execution: detects ransomworm propagation traffic as it spreads to infect other hosts, before payload (encryption) runs on new victims
- **dataset_benchmark:** Own PCAP-based traffic captures of WannaCry and NotPetya propagation plus benign background traffic; not stated to be publicly open-sourced
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate risk: methodology (feature sets, classifier fusion) is described in reproducible detail, but the WannaCry/NotPetya capture corpus is not clearly published; comparison baselines are the component classifiers rather than external state-of-the-art systems

**threat_intel**

- **threat_actor_fields:** Partially applicable: analyses WannaCry and NotPetya campaign traffic as case studies (well-known campaign malware), but performs no actor attribution, leak-site analysis or wallet tracing

---

### 3.2 HFL-RD: Heterogeneous Federated Learning-Empowered Ransomware Detection via APIs and Traffic Features

*Lan, K.; Li, G.; Huang, W.; Li, J. (2025). IEEE Transactions on Network and Service Management, published online 29 May 2025. Q1 (Scimago SJR 2025: SJR 1.389; Q1 in Computer Networks and Communications and Electrical and Electronic Engineering). [https://doi.org/10.1109/TNSM.2025.3574716](https://doi.org/10.1109/TNSM.2025.3574716) `retained-included` · `IEEE Xplore; DOI 10.1109/TNSM.2025.3574716`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Heterogeneous federated learning scheme (HFL-RD) integrating (a) Command-and-Control (C&C) traffic behaviour analysis and (b) local API call operation analysis to capture concealed ransomware characteristics; one-dimensional convolution pre-processing of raw traffic preserves structural network feat …
- **key_findings:** HFL-RD obtained accuracy over 95% and outperformed existing methods; for unknown ransomware variants it demonstrated superior detection capability in terms of detection time and number of file corruptions; the combination of C&C traffic analysis with API call analysis captures covert evolution chara …
- **limitations:** Acknowledged/observed: federated architecture introduces communication/training overhead and assumes multiple participating clients; requires joint deployment of endpoint API telemetry and network monitoring; evaluation uses publicly downloadable samples rather than live enterprise campaigns; exact  …
- **research_gaps:** Gap addressed: traditional methods treat external (network) and internal (endpoint) ransomware behaviours separately, missing covert evolution of advanced ransomware; federated learning enables privacy-preserving collaborative detection across clients with non-IID ransomware data. Remaining gaps: sc …

**prisma**

- **inclusion_rationale:** Passes: published 2025, IEEE Transactions on Network and Service Management is SJR Q1 (1.389, 2025), sourced from IEEE Xplore (allowed database); provides the most recent network+endpoint hybrid detection record, extending the cluster's temporal coverage to 2025.

**stratification**

- **platform_environment:** Network + endpoint hybrid: C&C traffic monitoring at network level plus local API call analysis on endpoints (Windows-oriented ransomware samples)
- **kill_chain_stage:** Pre-encryption (C&C communication stage, T1486-adjacent command channel) combined with during-encryption detection via local API call sequences (T1485)
- **dataset_benchmark:** Dataset assembled from three public websites: 300 runnable ransomware samples from 30 families and 200 benign samples from 7 categories; constituent sources are public but the assembled corpus is not stated to be released as a unified open dataset
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate risk: sample counts (300 ransomware / 30 families / 200 benign) and federated design are documented and constituent sources are public, but the assembled dataset, federated client configuration and code are not stated to be released; comparisons against existing methods are reported without …

**threat_intel**

- **threat_actor_fields:** Not applicable: no RaaS group naming, leak-site evidence or payment-wallet tracing; 30 ransomware families used as detection targets without actor attribution

---

## 4. D. Explainability, reproducibility & benchmark validity

**Papers retained: 2** · Excluded records: 1 · Uncertain fields: 5

<details><summary>Excluded records (PRISMA transparency)</summary>

- paper_ref=Pereira et al. 2026; decision=PRUNED; title=It Works on My Machine: A Systematization of Knowledge on Reproducibility and Replicability in ML-Based Ransomware Detection; reason=Eligibility prune: IEEE EuroS&PW workshop proceedings carry no Scimago SJR quartile; fails strict Q1/Q2 journal criterion

</details>

<details><summary>Uncertain fields in this cluster</summary>

- quartile_sjr
- platform_environment
- dataset_benchmark
- evaluation_metrics
- reproducibility

</details>

### 4.1 XRan: Explainable deep learning-based ransomware detection using dynamic analysis

*Gulmez, S.; Gorgulu Kakisim, A.; Sogukpinar, I. (2024). Computers & Security, vol. 139, art. 103703 (Elsevier). Q1 (Scimago SJR 2024 = 1.445; Computer Science (miscellaneous) and Law; ISSN 0167-4048). [https://doi.org/10.1016/j.cose.2024.103703](https://doi.org/10.1016/j.cose.2024.103703) `retained-included` · `ScienceDirect`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Dynamic analysis in Cuckoo Sandbox extracting API-call sequences, DLL sequences, and mutex (mutual-exclusion) sequences combined into a multi-view feature space; two-layer CNN classifier; LIME (local) and SHAP (global) explanations of detection outcomes; five datasets: RD1 (VirusShare, 6,263 ransomw …
- **key_findings:** XRan attains up to 99.4% True Positive Rate and outperforms baseline and state-of-the-art ransomware detectors; combining API/DLL/mutex sequence views preserves sequence relationships that frequency-domain-only features lose; LIME and SHAP consistently identify the dynamic features driving ransomwar …
- **limitations:** Dynamic feature extraction incurs high runtime overhead; detection requires executing the binary in a Cuckoo sandbox, so fast or environment-sensitive ransomware activity may complete before capture; evaluation is Windows-centric; sandbox-based dynamic analysis is itself detectable and evadable by s …
- **research_gaps:** Addresses the explainability gap of black-box detectors for security analysts; notes that feature-extraction overhead and sandbox dependence remain unresolved for production deployment, and that XAI-guided insight into ransomware behavior (beyond accuracy) is an emerging requirement

**prisma**

- **inclusion_rationale:** 2024 publication in Computers & Security (SJR 2024 = 1.445, Q1) indexed in ScienceDirect and Scopus; squarely in scope as an XAI (LIME/SHAP) ransomware detection study; no eligibility criterion failed.

**stratification**

- **platform_environment:** Windows (PE executables; benign set built from Windows system files)
- **kill_chain_stage:** During-encryption (behavioral detection at the onset of T1485 file-modification behavior to stop encryption in progress)
- **dataset_benchmark:** *[uncertain]*
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** *[uncertain]*

**threat_intel**

- **threat_actor_fields:** Not applicable (no RaaS group attribution, leak-site evidence, or wallet tracing content)

---

### 4.2 Explainability in AI-based behavioral malware detection systems

*Galli, A.; La Gatta, V.; Moscato, V.; Postiglione, M.; Sperli, G. (2024). Computers & Security, vol. 141, art. 103842 (Elsevier, open access). Q1 (Scimago SJR 2024 = 1.445; Computer Science (miscellaneous) and Law; ISSN 0167-4048). [https://doi.org/10.1016/j.cose.2024.103842](https://doi.org/10.1016/j.cose.2024.103842) `retained-included` · `ScienceDirect`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** XAI framework for API-call-sequence behavioral malware detection; evaluates four XAI methods (SHAP, LIME, LRP, and Attention mechanism) as explanatory layers for recurrent deep detectors (LSTM and GRU) across three API-call benchmark datasets differing in size, sequence length, and number of classes …
- **key_findings:** Each of SHAP, LIME, LRP, and Attention exhibits distinct effectiveness/efficiency trade-offs that vary with dataset size, sequence length, and class count; no single XAI method dominates across all behavioral malware detection formulations; embedding XAI makes AI-based behavioral detection more acti …
- **limitations:** Scope is generic malware rather than ransomware-specific; the datasets are proprietary and the authors state they do not have permission to share data, which blocks third-party replication and typifies the dataset-limitation problem this review item targets; explanation quality is sensitive to datas …
- **research_gaps:** Identifies the gap of choosing among XAI methods for security pipelines: no uniform guidance on which explanation method suits which data profile; future work on explanation faithfulness/fidelity validation and on larger, shareable datasets to support XAI evaluation at scale

**prisma**

- **inclusion_rationale:** 2024 publication in Computers & Security (SJR 2024 = 1.445, Q1) indexed in ScienceDirect and Scopus; in scope for item D as a rigorous XAI-method comparison (SHAP/LIME/LRP/Attention) that directly informs explainability and dataset-limitation analysis of behavioral detection; noted scope deviation:  …

**stratification**

- **platform_environment:** *[uncertain]*
- **kill_chain_stage:** Pre-encryption (host-level classification of malicious binaries at execution time, before data impact; not ransomware-stage-specific)
- **dataset_benchmark:** Three API-call sequence datasets differing in size, sequence length, and number of classes; explicitly NOT shared (ScienceDirect data-availability statement: 'the authors do not have permission to share data')
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Open-access (CC license) and methodologically detailed, but datasets are proprietary and not shared, so full third-party replication of the pipeline is not currently possible; compares model variants internally rather than against real-environment deployments

**threat_intel**

- **threat_actor_fields:** Not applicable (no RaaS group attribution, leak-site evidence, or wallet tracing content)

---

## 5. E. AI-era threat models (LLM/GenAI ransomware)

**Papers retained: 2** · Excluded records: 1 · Uncertain fields: 5

<details><summary>Excluded records (PRISMA transparency)</summary>

- paper_ref=arXiv preprint; decision=PRUNED; title=Ransomware 3.0: Self-Composing and LLM-Orchestrated; reason=Eligibility prune: arXiv:2508.20444 (Ransomware 3.0) has no peer-reviewed journal/conference version as of 2026-10-21; retained only as provenance lead for PromptLock

</details>

<details><summary>Uncertain fields in this cluster</summary>

- journal
- quartile_sjr
- platform_environment
- dataset_benchmark
- reproducibility

</details>

### 5.1 Unleashing offensive artificial intelligence: Automated attack technique code generation

*Iturbe, E.; Llorente-Vazquez, O.; Rego, A.; Rios, E.; Toledo, N. (2024). Computers & Security (Elsevier), art. 104077. Q1 (Computers & Security, Scimago SJR 2024 = 1.445, Computer Science (miscellaneous) and Law). [https://doi.org/10.1016/j.cose.2024.104077](https://doi.org/10.1016/j.cose.2024.104077) `retained-included` · `ScienceDirect`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Builds an AI-powered mechanism for the automatic generation of attack technique code, spanning initial access vectors through impact actions (including encryption and extortion-related impact), driven by Large Language Model technology; comprehensive analysis of simulated attacks identifies which MI …
- **key_findings:** Empirically demonstrates that LLM technology can be easily used for attack execution: multiple attack tactics and techniques (from initial vectors to impact actions) are consistently generated in code form; single attack techniques can be produced in multiple variants, enabling AI-enhanced attack si …
- **limitations:** Focus is on automated generation of aircraft-/system-level attack techniques rather than a complete autonomous attack campaign; generation depends on current LLM capability and prompt engineering; evaluation is simulation-based in controlled scenarios rather than in-the-wild attestation
- **research_gaps:** Identifies the gap of scalable, automated red-teaming: BAS platforms lack automatic generation of multiple, varied attack techniques; AI-generated attack variants imply defenders must test against a widened attack space rather than fixed playbooks

**prisma**

- **inclusion_rationale:** Peer-reviewed journal article, 2024 (within 2022-2026), Computers & Security (SJR Q1), indexed in ScienceDirect/Scopus; directly serves the item-E adversarial pillar (attacker-side AI) with LLM-generated attack techniques up to encryption/extortion-level impact actions; no eligibility criterion fail …

**stratification**

- **platform_environment:** *[uncertain]*
- **kill_chain_stage:** Full kill chain from initial access through post-encryption impact (covers generation of techniques mapping to encryption/extortion impact, i.e., MITRE T1485/T1471 impact stage among others)
- **dataset_benchmark:** *[uncertain]*
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** *[uncertain]*

**threat_intel**

- **threat_actor_fields:** Not applicable (study models cybercriminal capability expansion in general - e.g., hacker-as-a-service - without naming a specific RaaS group)

---

### 5.2 From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy

*Gupta, M.; Akiri, C.; Aryal, K.; Parker, E.; Praharaj, L. (2023). IEEE Access, vol. 11 (IEEE). Q1 (IEEE Access, Scimago SJR 2023 = 0.960). [https://doi.org/10.1109/ACCESS.2023.3300381](https://doi.org/10.1109/ACCESS.2023.3300381) `retained-included` · `IEEE Xplore`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Analyzes generative-AI (ChatGPT-class) vulnerabilities and their dual use: demonstrates jailbreak, reverse-psychology, and prompt-injection attacks that bypass model ethical constraints; examines offensive scenarios (social engineering, phishing, automated hacking, attack payload generation, malware …
- **key_findings:** Successful proof-of-concept attacks show GenAI tools can be misused by adversaries to create social-engineering content, phishing lures, attack payloads, malicious code snippets, and polymorphic malware despite OpenAI's ethical policies; the paper frames parallel defensive uses (automated threat int …
- **limitations:** Conceptual threat modeling with selected proof-of-concept demonstrations rather than a systematic measurement of real attack prevalence; ransomware covered as one offensive scenario within broader GenAI misuse; technical detail is fast-dated given rapid model evolution
- **research_gaps:** Highlights open challenges of both offensive and defensive GenAI: model jailbreaking and prompt injection, lack of uniform guidance for AI-assisted incident response, need for secure-by-default model deployment, and social/legal/ethical implications of GenAI misuse

**prisma**

- **inclusion_rationale:** Peer-reviewed journal article, 2023 (within 2022-2026), IEEE Access (SJR 2023 = 0.960, Q1), indexed in IEEE Xplore; in scope for GenAI-generated polymorphic malware threat modeling; noted deviation: ransomware is treated within the broader GenAI misuse threat landscape rather than as the sole focus.

**stratification**

- **platform_environment:** *[uncertain]*
- **kill_chain_stage:** Pre-encryption and full-chain conceptual coverage (payload generation, phishing/social engineering as delivery; malware creation through impact)
- **dataset_benchmark:** No named benchmark dataset (demonstration-driven study)
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** *[uncertain]*

**threat_intel**

- **threat_actor_fields:** Not applicable (no RaaS group attribution or leak-site evidence; discusses generic cyber offenders)

---

## 6. F. Prevention & resilience engineering

**Papers retained: 2** · Excluded records: 1 · Uncertain fields: 4

<details><summary>Excluded records (PRISMA transparency)</summary>

- paper_ref=Zhang et al. 2023; decision=PRUNED; title=Multistage Game Theoretical Approach for Ransomware Attack and Defense; reason=Scope prune: formal game-theoretic modeling most tangential to the review's prevention-engineering focus; empirical/simulation (Ilau2025) and system-design (McIntosh2023/SEDAC) evidence retained

</details>

<details><summary>Uncertain fields in this cluster</summary>

- platform_environment
- dataset_benchmark
- evaluation_metrics
- reproducibility

</details>

### 6.1 Modelling and simulating organizational ransomware recovery: structure, methodology, and decisions

*Ilau, M.-C.; Baldwin, A.; Caulfield, T.; Pym, D. (2025). Journal of Cybersecurity (Oxford University Press), open access. Q1 (Scimago SJR 2024 = 0.938, Q1 in Computer Networks and Communications, Computer Science Applications, Computer Science (miscellaneous), Information Systems, Software, Law, and further categories; SJR 2025 = 0.818; ISSN 2057-2093). [https://doi.org/10.1093/cybsec/tyaf035](https://doi.org/10.1093/cybsec/tyaf035) `retained-included` · `Google Scholar (lead) / verified against Oxford Academic publisher page (record indexed in Scopus/ScienceDirect-family sources via Oxford)`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Semantically justified, mathematically compositional co-design system-modelling approach (process-algebra grounded): ransomware behaviour, organizational structure, IT infrastructure, and recovery options conceptualized from literature surveys and expert knowledge; model built as composition of four …
- **key_findings:** Demonstrates that a compositional simulation model can quantify the organizational consequences of recovery-solution choices (recovery time, cost, and resilience trade-offs) before deployment; situates the decision problem in empirical context (prior work reports 21% of 55 studied ransomware attacks …
- **limitations:** Model is only partially generic and parametrized from literature/expert judgement rather than validated against real recovered organizations; focus is endpoint device recovery rather than enterprise-wide (cloud, hypervisor, supply-chain) recovery; outcome realism depends on fidelity of the conceptua …
- **research_gaps:** Addresses the resilience-engineering gap: organizations lack evidence-based understanding of how backup/recovery mixes (technology + policy + employee factors) affect time-to-recover and cost; positions compositional modelling and sensitivity analysis as a decision-support instrument for ransomware  …

**prisma**

- **inclusion_rationale:** Named candidate for item F (organizational ransomware recovery modelling). Published online 21 Nov 2025 (year 2025, within 2022-2026); open-access article in Journal of Cybersecurity (Scimago Q1, SJR 2024 = 0.938); verified via DOI 10.1093/cybsec/tyaf035 and Oxford Academic/Google Scholar records; n …

**stratification**

- **platform_environment:** *[uncertain]*
- **kill_chain_stage:** Post-encryption (organizational recovery after the T1485 encryption impact; restores integrity/availability)
- **dataset_benchmark:** No external dataset; simulation over a synthetic parameter space (9,000 configurations, 450,000 iterations) grounded in literature-derived conceptualizations
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** *[uncertain]*

**threat_intel**

- **threat_actor_fields:** Not applicable (no RaaS group named; references empirical incident context from prior studies, e.g., Connolly et al., without group attribution)

---

### 6.2 Applying staged event-driven access control to combat ransomware

*McIntosh, T.; Kayes, A. S. M.; Chen, Y.-P. P.; Ng, A.; Watters, P. (2023). Computers & Security, vol. 128, art. 103160, May 2023 (Elsevier). Q1 (Scimago SJR 2023 = 1.566, SJR 2024 = 1.445, Computer Science (miscellaneous) and Law; ISSN 0167-4048). [https://doi.org/10.1016/j.cose.2023.103160](https://doi.org/10.1016/j.cose.2023.103160) `retained-included` · `ScienceDirect`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Staged Event-Driven Access Control (SEDAC) architecture combining program-centric access control (PCAC) and user-centric access control (UCAC), chained as three stages: pre-UCAC PCAC (OS integrity, MBR Guard), UCAC (user consent/intention), post-UCAC PCAC (user file integrity, File Warden minifilter …
- **key_findings:** The Sedaco prototype intercepted more types of ransomware attack vectors than existing proposals: File Warden blocked all directly initiated file-encryption activities (user-level PCAC); MBR Guard blocked all unsafe MBR modifications (OS-level PCAC); indirect encryptions (PowerShell/Command Line, VM …
- **limitations:** Prototype limited to Windows OS; UCAC inference of user intention/consent trades accuracy vs alarm fatigue, and human-presence heuristics can mis-fire; PCAC depends on software-industry cooperation on coding standards and file-type integrity enforcement that does not currently exist; explicit securi …
- **research_gaps:** Fills the gap of OS-native prevention: existing anti-ransomware studies ignore novel vectors (fileless scripts, partial encryption, exfiltration, human-operated ransomware); advocates embedding SEDAC-style access control into OS/architecture design and calls for research on non-negotiable vs user-de …

**prisma**

- **inclusion_rationale:** Named candidate for item F (staged event-driven access control vs ransomware). Computers & Security, vol. 128, art. 103160, May 2023, Scimago Q1 (SJR 2023 = 1.566); indexed in ScienceDirect/Scopus; directly in scope for prevention engineering; no eligibility criterion failed.

**stratification**

- **platform_environment:** Windows OS (Sedaco prototype augmented into Windows 10; kernel-mode file-system minifilter)
- **kill_chain_stage:** Pre-encryption through during-encryption prevention (OS-integrity and MBR guard stages precede damage; file-system and exfiltration interception at the T1485/T1441-file-modification and data-theft stages)
- **dataset_benchmark:** *[uncertain]*
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** *[uncertain]*

**threat_intel**

- **threat_actor_fields:** Not applicable (defensive perspective; test samples from named historical families WannaCry/Petya and the LockFile variant, without group-level intelligence or wallet tracing)

---

## 7. G. Platform expansion (OT/IoT/ICS, cloud/hypervisor, cross-platform)

**Papers retained: 2** · Excluded records: 0 · Uncertain fields: 2

<details><summary>Uncertain fields in this cluster</summary>

- evaluation_metrics
- threat_actor_fields

</details>

### 7.1 Securing the Industrial Internet of Things against ransomware attacks: A comprehensive analysis of the emerging threat landscape and detection mechanisms

*Al-Hawawreh, M.; Alazab, M.; Ferrag, M. A.; Hossain, M. S. (2024). Journal of Network and Computer Applications (Elsevier), vol. 223, article 103809. Q1 (SJR 2023 = 2.417; Q1 in Computer Networks and Communications, Computer Science Applications, and Hardware and Architecture per SCImago). [https://doi.org/10.1016/j.jnca.2023.103809 (ScienceDirect PII: S108480452300228X)](https://doi.org/10.1016/j.jnca.2023.103809 (ScienceDirect PII: S108480452300228X)) `retained-included` · `ScienceDirect (Elsevier); also indexed in Scopus (AN: SCOPUS:85181092350)`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Comprehensive thematic review: analyzes IIoT system evolution and common architecture, ransomware evolution/types (mass-distribution vs targeted), attack stages, extortion strategies (single vs multiple extortion, malware and non-malware tactics, employment of non-ransomware malware and on-premises, …
- **key_findings:** Sophisticated ransomware will likely target heterogeneous, legacy-connected IIoT systems; detection methods validated on IT platforms (entropy, honeypots, anti-virus, AI) have uncertain applicability to IIoT; existing studies do not yet cover new IIoT devices/CPS platforms (authors state they have n …
- **limitations:** Narrative review without systematic PRISMA-style protocol or reported search/screening counts; no empirical evaluation of the surveyed detection methods on IIoT testbeds or real deployments; no quantitative meta-analysis of detection effectiveness; as acknowledged, no real-world ransomware incidents …
- **research_gaps:** Addresses the gap that no prior study comprehensively analyzed new ransomware tactics/techniques and detection research for IIoT; identifies open issues requiring further research: lack of validated IIoT-specific detection models, absence of IIoT-targeted datasets/benchmarking, and the need for offe …

**prisma**

- **inclusion_rationale:** Passes eligibility: published 2024 (within 2022-2026), journal at SJR Q1 in 2023-2024 rankings, indexed in Scopus and hosted on ScienceDirect (one of the six allowed source databases); directly fits Item G as the designated candidate paper for OT/IIoT platform ransomware protection and platform-depe …

**stratification**

- **platform_environment:** IIoT-SCADA (IIoT edge systems, IT/OT convergence, CPS); covers ransomware across Windows, Linux, Android, iOS and cross-platform variants as part of the reviewed landscape
- **kill_chain_stage:** Pre-encryption through post-encryption (full kill-chain landscape: tactics, stages, extortion - MITRE T1485 Data Encrypted for Impact context); detection research emphasis is on detecting at/before encryption onset
- **dataset_benchmark:** No experimental benchmark of its own; review synthesizes existing detection research (entropy, honeypot, anti-virus, AI-based); no named open dataset introduced
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Low reproducibility relevance: qualitative review with no baseline comparisons, experiments, or test environments; conclusions depend on the (unreported) search strategy; useful as scoping/background source rather than a reproducible benchmark

**threat_intel**

- **threat_actor_fields:** *[uncertain]*

---

### 7.2 Opportunities for Early Detection and Prediction of Ransomware Attacks against Industrial Control Systems

*Gazzan, M.; Sheldon, F. T. (2023). Future Internet (MDPI), vol. 15, issue 4, article 144. Q2 (SJR 2023 = 0.808; Q2 in Computer Networks and Communications per SCImago; Q1 only in the 2025 ranking). [https://doi.org/10.3390/fi15040144](https://doi.org/10.3390/fi15040144) `retained-included` · `MDPI/Scopus-indexed journal record verified via DOI landing page and Google Scholar/Scopus metadata`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Authors state they conducted a non-systematic literature review limited to articles specifically addressing ransomware prediction for ICS/SCADA; reviews SCADA architecture, vulnerabilities, attacks, intruspoon-detection techniques and testbeds, tabulates ransomware prediction studies (methods, tools …
- **key_findings:** ICS/SCADA characteristics (outdated proprietary software, limited visibility, legacy infrastructure, remote-access needs) make ransomware prediction difficult; ransomware attacks on ICS are growing and pose a significant challenge to predictive prohibition; reviewed prediction literature is thin - a …
- **limitations:** Explicit self-described non-systematic review with a deliberately narrowed article set; non-empirical research synthesis with no new data, model or testbed; prediction-oriented evidence base is sparse (the paper itself notes large gaps); limited discussion of detection-only techniques for ICS beyond …
- **research_gaps:** Identifies the specific gap that prior surveys covered only ransomware detection/prevention, not early prediction of attack likelihood against ICS; enumerates future research opportunities: threat-intelligence-enabled ransomware prediction in ICS, expanding the narrow prediction literature, and shar …

**prisma**

- **inclusion_rationale:** Passes eligibility: published 2023 (within 2022-2026) in Future Internet, which held SJR Q2 in 2023 (verified on SCImago quartile table; Q1 only in 2025), an allowed source; retained as the designated ICS ransomware early-detection candidate paper for Item G despite being Q2 (Q1/Q2 threshold met); d …

**stratification**

- **platform_environment:** IIoT-SCADA (industrial control systems and SCADA, including power plants and water treatment facilities)
- **kill_chain_stage:** Pre-encryption (early detection and attack-likelihood prediction, aiming to act before data encryption, MITRE T1471/T1485 prevention context)
- **dataset_benchmark:** No dataset built or benchmarked; reviews prediction studies and their tools (e.g., GAN experiments) rather than evaluating datasets; no open-source artifact introduced
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Low reproducibility: narrative synthesis without a systematic search protocol; reviewed studies summarized in tables but none re-evaluated in a controlled environment; no sandbox/real-environment testing reported

**threat_intel**

- **threat_actor_fields:** *[uncertain]*

---

## 8. H. RaaS, double extortion & payment tracing

**Papers retained: 3** · Excluded records: 0 · Uncertain fields: 1

<details><summary>Uncertain fields in this cluster</summary>

- evaluation_metrics

</details>

### 8.1 A Tale of Two Markets: Investigating the Ransomware Payments Economy

*Oosthoek, K.; Cable, J.; Smaragdakis, G. (2023). Communications of the ACM, vol. 66, no. 8, pp. 74-83. Q1 (Communications of the ACM held SCImago Q1 in Computer Science (miscellaneous) continuously 1999-2025, including 2023). [https://doi.org/10.1145/3582489](https://doi.org/10.1145/3582489) `retained-included` · `Scopus-indexed journal; record verified via ACM Digital Library publisher metadata and Google Scholar`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Operated Ransomwhere, an open crowdsourced ransomware payment tracker; compiled 7,321 Bitcoin addresses reported by victims of ransomware; verified on-chain via Bitcoin's transparent ledger; conducted follow-the-money analysis of 13,497 ransom payments to 87 criminal actors over five years (worth mo …
- **key_findings:** Two parallel ransomware criminal markets exist: commodity ransomware and Ransomware-as-a-Service; striking differences between markets in cryptocurrency resource utilization, revenue per transaction, and ransom laundering efficiency; identifying choke points in commodity ransomware payment activity  …
- **limitations:** Payments data rely on voluntary victim reports to a crowdsourced aggregator, so the dataset captures only reported payments and may under-represent the true population; payment addresses restricted to Bitcoin (non-Bitcoin payment channels excluded); actor classification into commodity vs RaaS depend …
- **research_gaps:** Identifies the open problem of tracing RaaS-linked cryptocurrency (harder choke points than commodity ransomware) and proposes follow-up work on tracing RaaS on-chain activity; highlights the need for larger, systematically collected ransomware payment datasets beyond crowdsourced self-reports

**prisma**

- **inclusion_rationale:** Passes eligibility: 2023 publication (2022-2026 window); Communications of the ACM is SCImago Q1 in 2023; Scopus-indexed and retrievable via Google Scholar; core Item H paper covering RaaS economics and crypto payment tracing via the Ransomwhere dataset

**stratification**

- **platform_environment:** Windows/enterprise IT platforms and cross-platform payment ecosystems (Bitcoin on-chain layer); platform focus is the payments/laundering infrastructure rather than infection hosts
- **kill_chain_stage:** Post-encryption (payment, laundering, cash-out, traceability - supporting MITRE T1485/T1471 impact-stage intelligence)
- **dataset_benchmark:** Ransomwhere crowdsourced ransomware payment dataset in study period: 13,497 payments to 87 criminal actors, over $101 million, 7,321 Bitcoin addresses, spanning roughly five years; described as the largest public dataset of ransomware activity at the time; Ransomwhere is an open crowdsourced tracker …
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate-to-high: reproducible on-chain verification because Bitcoin state is public and the Ransomwhere aggregator was operated openly; manual actor classification reduces exact replication fidelity; real on-chain environment rather than sandbox

**threat_intel**

- **threat_actor_fields:** 87 ransomware criminal actors named/classified in the study; RaaS ecosystem emphasized with Conti's leaked playbook cited as exemplar of affiliate enablement; leak-site/double-extortion behavior described as RaaS pricing feature; full wallet-level tracing of 7,321 Bitcoin addresses covering commodit …

---

### 8.2 Deception in double extortion ransomware attacks: An analysis of profitability and credibility

*Meurs, T.; Cartwright, E.; Cartwright, A.; Junger, M.; Abhishta, A. (2024). Computers & Security (Elsevier), vol. 138, article 103670. Q1 (Computers & Security held SCImago Q1 in Computer Science (miscellaneous) and Law in 2022-2025, including 2024). [https://doi.org/10.1016/j.cose.2023.103670](https://doi.org/10.1016/j.cose.2023.103670) `retained-included` · `ScienceDirect (Elsevier); also indexed in Scopus`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Models double-extortion ransomware as a signaling game between criminals and victims under information asymmetry; derives five distinct equilibria characterizing criminals' approaches to signaling data exfiltration; calibrates game parameters with real-world-like values; empirically grounds the mode …
- **key_findings:** Double extortion leads to a larger proportion of victims paying (119 of 452 paid, 27.8%) and larger ransoms - roughly 3 million euro requested when data exfiltration is signaled and roughly 1.7 million euro after negotiation - yielding more profit for criminals; five equilibria characterize exfiltra …
- **limitations:** Game-theoretic equilibria are simplifications of real negotiations; empirical calibration uses like-for-like real-world values but parameter estimation is sensitive to assumptions; ground truth on whether data was truly exfiltrated is often unknowable even in hindsight; the 452-attack dataset, while …
- **research_gaps:** Addresses the gap between ransomware economics literature (which treated exfiltration claims as credible) and observed deception dynamics; identifies the need to model information asymmetry, signal credibility, and victim epistemics in double extortion, and to establish whether exfiltration claims c …

**prisma**

- **inclusion_rationale:** Passes eligibility: 2024 publication (2022-2026 window); Computers & Security held SCImago Q1 in 2024; hosted on ScienceDirect (allowed source); core Item H paper quantifying double-extortion profitability and credibility

**stratification**

- **platform_environment:** Windows/enterprise IT platforms (platform-agnostic economic analysis of double-extortion attacks and leak/publication outcomes)
- **kill_chain_stage:** Post-encryption (extortion and negotiation phase, including leak-site publication decisions after non-payment)
- **dataset_benchmark:** Empirical dataset of 452 real-world ransomware attacks (130 negotiations, 119 payments) used to calibrate and validate the signaling game; no publicly released open dataset confirmed
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate: model derivation is reproducible, but empirical calibration depends on a described-but-not-publicly-confirmed negotiation dataset; no external benchmark or test environment involved

**threat_intel**

- **threat_actor_fields:** Naming anchored on the Maze group as initiator of the double-extortion scheme (leak-site exposure of non-paying victims since November 2019); leak-site publication evidence used to evaluate criminal credibility claims; no full RaaS roster attribution; no wallet tracing

---

### 8.3 Inside ransomware groups: An analysis of their origins, structures, and dynamics

*Phipps, A.; Nurse, J. R. C. (2026). Computers & Security (Elsevier), vol. 160, article 104705. Q1 (Computers & Security held SCImago Q1 in Computer Science (miscellaneous) and Law through 2025; SJR 2025 = 1.598). [https://doi.org/10.1016/j.cose.2025.104705](https://doi.org/10.1016/j.cose.2025.104705) `retained-included` · `ScienceDirect (Elsevier); also indexed in Scopus`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** PRISMA systematic review approach combined with critical analysis of over 500 dispersed sources, including ransomware group communications (leaked chat messages), court documents, security-vendor reports, and ransomware leak sites; thematic examination of the origins, structure, organisation, dynami …
- **key_findings:** Conti, LockBit, and BlackCat/ALPHV share noteworthy similarities: Russian origins, business-like operations, emphasis on brand-building, strong leadership structures, propensity for retaliation against victims who publicize negotiations, use of RaaS models, and multi-level extortion; BlackCat paid a …
- **limitations:** Evidence base mixes systematic review sources with leaked group chats and vendor reporting whose veracity varies; analysis limited to three prominent (Western/Dutch-law enforcement-documented) groups and may not generalize to smaller or non-English groups; qualitative synthesis cannot quantify causa …
- **research_gaps:** Explicitly addresses the research gap of scarce academic, evidence-grounded knowledge on the internal origins, structures, and dynamics of ransomware threat actors, proposing that systematic academic analysis of group communications can provide a foundation for disrupting ransomware groups and their …

**prisma**

- **inclusion_rationale:** Passes eligibility: 2026 publication (2022-2026 window); Computers & Security is SCImago Q1 (latest available SJR 2025 = 1.598, Q1); hosted on ScienceDirect (allowed source); named RaaS groups and leak-site evidence directly satisfy the Item H threat-actor intelligence requirement

**stratification**

- **platform_environment:** Cross-platform enterprise threat-actor operations (Windows-dominant strains; focuses on organizational infrastructure - leak sites, Tor payment portals, chat communications - rather than endpoint platforms)
- **kill_chain_stage:** Post-encryption (extortion economics; also covers pre-encryption operational planning such as initial access broker work by affiliates)
- **dataset_benchmark:** No experimental dataset; evidence corpus of over 500 dispersed sources (group communications/leaked chats, vendor reports, court records, leak sites) synthesized qualitatively; not released as a machine-readable artifact
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate: PRISMA protocol improves auditability of source selection, but reliance on ephemeral sources (leak sites, leaked chats) makes systematic re-collection impossible after takedowns/shutdowns; no quantitative baseline comparisons

**threat_intel**

- **threat_actor_fields:** Three RaaS groups studied in depth: Conti (successor to Ryuk/TrickBot/Emotet lineage), LockBit (and LockBit 3.0/3.0 Green variants), and BlackCat/ALPHV (successor to DarkSide/BlackMatter/REvil lineage); leak-site evidence central (victim counts, inflated LockBit postings, BlackCat SEC-reporting exto …

---

## 9. I. Incident response, playbooks & forensic readiness

**Papers retained: 2** · Excluded records: 2 · Uncertain fields: 3

<details><summary>Excluded records (PRISMA transparency)</summary>

- paper_ref=1; decision=PRUNED; title=Know Thy Ransomware Response: A Detailed Framework for Devising Effective Ransomware Response Strategies; reason=Validity prune: Bajpai & Enbody 2023 recorded as Q2 (2023 SJR 0.595) but commonly misquoted as Q1; weakest quartile evidence in cluster, overlaps Shaked2023 playbook framework
- paper_ref=4; decision=PRUNED; title=The rise of ransomware: Forensic analysis for windows based ransomware attacks; reason=Overlap prune: Kara & Aydos 2022 single-OS (Windows) forensic analysis overlaps forensic-readiness scope of Huck & Breitinger 2022; methodological redundancy

</details>

<details><summary>Uncertain fields in this cluster</summary>

- evaluation_metrics
- dataset_benchmark
- threat_actor_fields

</details>

### 9.1 Wake Up Digital Forensics' Community and Help Combat Ransomware

*Huck, J.; Breitinger, F. (2022). IEEE Security & Privacy, vol. 20, issue 4, pp. 61-70 (Jul.-Aug. 2022). Q1 (best quartile in Law per SCImago 2022, SJR 2022 = 0.684) - venue met the Q1/Q2 eligibility threshold at publication year. [https://doi.org/10.1109/MSEC.2021.3137018](https://doi.org/10.1109/MSEC.2021.3137018) `retained-included` · `IEEE Xplore; verified via IEEE Computer Society Digital Library metadata`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Argumentative best-practice synthesis supported by a comparative analysis of implemented ransomware strategies of companies (extended Rhine valley region, first author's related thesis work); examines technical vs procedural countermeasures and the role of digital forensics in ransomware investigati …
- **key_findings:** Organizations, literature, and research efforts focus on technical measures and neglect procedural countermeasures against ransomware; detailed case studies and shared best practices are needed so companies can adapt strategies and be better prepared; the digital forensics community has an underused …
- **limitations:** Position-style article with claims grounded in a regional (extended Rhine valley) comparative analysis of limited scope; no systematic evaluation of countermeasure effectiveness; recommendations are qualitative and practitioner-oriented
- **research_gaps:** Identifies the neglect of procedural countermeasures and of digital-forensic readiness in the ransomware defense literature; highlights the absence of shared, detailed incident case studies and best practices that organizations can adopt

**prisma**

- **inclusion_rationale:** Passes eligibility: published July-August 2022 (2022-2026 window); IEEE Security & Privacy held SCImago Q1 (best quartile, Law) with SJR 0.684 in 2022; indexed on IEEE Xplore (allowed source); retained as the designated forensic-readiness candidate paper

**stratification**

- **platform_environment:** Windows/enterprise IT (organizational forensic readiness across company environments)
- **kill_chain_stage:** Pre-encryption (forensic readiness and procedural preparation) and post-encryption (forensic investigation after impact)
- **dataset_benchmark:** No dataset; draws on comparative analysis of companies' implemented countermeasures and public case sources; no open dataset
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Low: argumentative synthesis without controlled experiments or benchmark environments

**threat_intel**

- **threat_actor_fields:** *[uncertain]*

---

### 9.2 Operations-informed incident response playbooks

*Shaked, A.; Cherdantseva, Y.; Burnap, P.; Maynard, P. (2023). Computers & Security (Elsevier), vol. 134, article 103454. Q1 (SCImago 2023: Q1 in Computer Science (miscellaneous) and Law). [https://doi.org/10.1016/j.cose.2023.103454](https://doi.org/10.1016/j.cose.2023.103454) `retained-included` · `ScienceDirect (Elsevier); also indexed in Scopus`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Identifies the conceptual gap that current playbook research/practice represent playbooks as process models that cannot communicate operational impact of an incident or of the response; proposes operations-informed playbooks by embedding a model of operations (dependency map) into the playbook's pro …
- **key_findings:** Playbook design currently lacks the ability to communicate operational impact of an incident and of incident response on the organization; embedding an operations model into playbooks reflects interdependencies and mutual influences of IR activities and operations in an accurate, systematic way; a n …
- **limitations:** Conceptual approach demonstrated in a single ransomware case study; no enterprise field deployment or multi-organization evaluation; adoption effort/costs of modeling operations itself are acknowledged as a practical consideration
- **research_gaps:** Identifies a significant conceptual gap in cybersecurity playbook design research and practice: inability to communicate operational impact of incidents and of incident response; proposes closing it via operations-informed playbooks that link process models to models of operations

**prisma**

- **inclusion_rationale:** Passes eligibility: published November 2023 (2022-2026 window); Computers & Security at SCImago Q1 in 2023; hosted on ScienceDirect (allowed source); retained as the designated operations-informed playbook candidate paper

**stratification**

- **platform_environment:** Windows/enterprise IT with critical national infrastructure framing (operations dependency context; Colonial Pipeline-style fuel-supply impact scenario discussed)
- **kill_chain_stage:** Pre-encryption (playbook preparation stage) and post-encryption (response decision-making amid operational degradation)
- **dataset_benchmark:** No empirical dataset; artifact is a newly developed open-source tool implementing the operations-informed playbook approach, demonstrated on a ransomware IR playbook case study
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate-to-good conceptually: open-source tool supports replication of the case-study demonstration, but metric validation is qualitative and there is no external sandbox/production comparison

**threat_intel**

- **threat_actor_fields:** *[uncertain]*

---

## 10. J. Victimology, economics & regulatory response

**Papers retained: 2** · Excluded records: 0 · Uncertain fields: 2

<details><summary>Uncertain fields in this cluster</summary>

- dataset_benchmark (open-sourced status of both datasets)
- reproducibility (public data-release confirmations)

</details>

### 10.1 Examining ransomware payment decision-making among small- and medium-sized enterprises

*Matthijsse, S. R.; Moneva, A.; van 't Hoff-de Goede, M. S.; Leukfeldt, E. R. (2025 (issue year, European Journal of Criminology vol. 22, issue 4, pp. 625-645; first published online 14 November 2024)). European Journal of Criminology (SAGE, journal of the European Society of Criminology; ISSN 1477-3708). Q1 per Scimago SJR - Law category, Q1 continuously 2005-2025; SJR 2025 = 1.029 (also ranked in Sociology and Political Science). [https://doi.org/10.1177/14773708241285671](https://doi.org/10.1177/14773708241285671) `retained-included` · `Scopus (journal-indexed record) and Google Scholar; DOI metadata cross-verified via publisher (SAGE Journals)`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Online survey with a vignette experiment administered via the I&O Research entrepreneurs' panel to 445 owners/managers of Dutch small- and medium-sized enterprises (EU Recommendation 2003/361/EC SME definition). Respondents rated inclination to pay under systematically varied scenario factors (ranso …
- **key_findings:** The stated likelihood of paying the ransom is low among Dutch SME decision-makers. Being advised to pay by a cybersecurity company significantly increases the likelihood of paying, as does not having a backup. Unexpectedly, the affordability of the ransom demand is not significantly related to the p …
- **limitations:** Stated payment intentions in hypothetical vignettes may not equal real payment behaviour (social desirability/hypothetical bias); single-country (Dutch) sample limits external validity; survey sampling via a commercial panel may skew towards more cyber-aware entrepreneurs; inability vs willingness t …
- **research_gaps:** Addresses the gap that little is known about how SMEs respond to ransomware victimization and which factors drive the payment decision - prior ransomware victim studies concentrated on prevalence and large enterprises. Leaves open real-payment validation, cross-jurisdiction replication, and study of …

**prisma**

- **inclusion_rationale:** PASS. Source: Scopus/Google Scholar-indexed journal. Year: 2025 print issue (online-first 2024), within 2022-2026 window. Quartile: Q1 by Scimago SJR (Law, SJR 2025 = 1.029). Topical fit: ransom payment decision factors in the victim-side/economic pillar of the review.

**stratification**

- **platform_environment:** Platform-agnostic: the study concerns SME organizational IT environments and victim decision context; no specific OS/device (Windows/Android/NAS etc.) is the unit of analysis
- **kill_chain_stage:** Post-encryption (victim-facing response and ransom payment decision after data encrypted; maps to the impact/response side of T1486/T1489 rather than T1485/T1471)
- **dataset_benchmark:** *[uncertain]*
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** *[uncertain]*

**threat_intel**

- **threat_actor_fields:** Not applicable: no RaaS group named, no leak-site evidence, no payment wallet/tracing coverage; the paper studies victim-side decisions rather than actor attribution

---

### 10.2 NAS ransomware: ransomware targeting NAS devices

*Meurs, T.; Hoheisel, R.; Junger, M.; Abhishta, A. (2026 (print issue year, Global Crime vol. 27, issue 2-3, pp. 135-158; first published online 26 November 2025)). Global Crime (Taylor & Francis / Routledge; ISSN 1744-0572). Q1 per Scimago SJR - Sociology and Political Science, 2025; SJR 2025 = 0.609 (CiteScore 2024 Q1 per Scopus). [https://doi.org/10.1080/17440572.2025.2591628](https://doi.org/10.1080/17440572.2025.2591628) `retained-included` · `Scopus (record SCOPUS:105023059210 confirmed via University of Twente Pure profile) and Google Scholar`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Quantitative analysis of 502 ransomware attacks reported to the Dutch national police between 2019 and 2022, of which 104 (20.7%) targeted Network Attached Storage (NAS) devices such as QNAP units, spanning both households and organisations. Victim characteristics, attack characteristics and financi …
- **key_findings:** NAS devices account for a substantial minority of reported attacks: 104 of 502 police-reported ransomware attacks (20.7%) targeted NAS devices, affecting both individuals and companies. Financial impact of an attack on an individual NAS owner is relatively low compared with organisational attacks, b …
- **limitations:** Data derive from police reports with possible low willingness to report (both individuals and SMEs under-report), so the 20.7% NAS share may not generalise to the true attack population; single-country (Netherlands) register; attack reports include incomplete or victim-supplied details; the law-enfo …
- **research_gaps:** Addresses the gap that ransomware research overwhelmingly focuses on Windows endpoints and enterprise double-extortion campaigns, largely ignoring consumer/SOHO NAS appliances as a distinct victim population. Highlights that NAS ransomware needs inclusion in the public debate and in victimology/cybe …

**prisma**

- **inclusion_rationale:** PASS. Source: Scopus-indexed journal (record confirmed). Year: published online November 2025, print issue 2026, within 2022-2026 window. Quartile: Q1 by Scimago SJR (Sociology and Political Science, 2025; SJR 0.609). Topical fit: victimology of a non-Windows platform (NAS), victim-side and economic …

**stratification**

- **platform_environment:** NAS (QNAP NAS appliances running QTS; embedded Linux-based network-attached storage devices), including non-NAS comparison cases
- **kill_chain_stage:** Pre-encryption through post-encryption: police-reported incidents cover exploitation of NAS web exposure (pre-encryption), encryption/compression of files (during-encryption, T1471/T1486), and post-encryption payment, decryption and law-enforcement response
- **dataset_benchmark:** *[uncertain]*
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Low-to-moderate: analysis of a privileged police dataset that cannot be redistributed; strings/coding scheme and the October 2022 DeadBolt intervention (Chainalysis/Censys/BleepingComputer evidence) are traceable via open sources, but external researchers cannot re-run the exact register analysis; n …

**threat_intel**

- **threat_actor_fields:** Partial coverage: names consumer-NAS ransomware strains/campaigns (DeadBolt, ech0raix, Qlocker targeting QNAP devices) rather than RaaS groups; documents the October 2022 law-enforcement action where the Dutch police tricked the DeadBolt actor into releasing decryption keys (bitcoin-trick key recove …

---

## 11. K. Sectoral empirical impact studies

**Papers retained: 2** · Excluded records: 1 · Uncertain fields: 2

<details><summary>Excluded records (PRISMA transparency)</summary>

- paper_ref=K_impackt_paper3; decision=PRUNED; title=Ransomware Attacks and Data Breaches in US Health Care Systems; reason=Overlap prune: JAMA Network Open 2025 descriptive breach-trend analysis; causal DiD evidence retained in Neprash2026 (AEJ) and Abouk-Powell2024 (JAMA)

</details>

<details><summary>Uncertain fields in this cluster</summary>

- dataset_benchmark (redistribution status of California state data; SAS code availability for Jiang et al.)
- reproducibility (code deposit confirmations for Abouk-Powell and Jiang et al.)

</details>

### 11.1 Hacked to Pieces? The Effects of Ransomware Attacks on Hospitals and Patients

*Neprash, H.; McGlave, C.; Nikpay, S. (2026 (American Economic Journal: Economic Policy, vol. 18, no. 1, February 2026, pp. 256-281)). American Economic Journal: Economic Policy (American Economic Association; ISSN 1945-7731). Q1 per Scimago SJR - Economics, Econometrics and Finance (miscellaneous), Q1 every year 2010-2025; SJR 2025 = 7.737; also Q1 by Scopus CiteScore (9.4, 2025). [https://doi.org/10.1257/pol.20240594 (replication data and code: https://doi.org/10.3886/E235483V1)](https://doi.org/10.1257/pol.20240594 (replication data and code: https://doi.org/10.3886/E235483V1)) `retained-included` · `Google Scholar and Scopus (Scopus Q1-indexed journal, coverage 2009-present); DOI record verified via Crossref and the AEA publisher page`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Authors constructed a database of US hospital ransomware attacks and linked it to 100% Medicare fee-for-service claims data; impacts on hospital operations and patient outcomes are quantified with event-study / continuous-treatment difference-in-differences estimators (Callaway-Goodman-Bacon-Sant'An …
- **key_findings:** Ransomware attacks reduce hospital volume by 17-24% during the initial attack week, with recovery within 3 weeks. Among patients already admitted when an attack begins, in-hospital mortality increases by 34-38%. These are among the first causal estimates directly tying hospital ransomware to excess  …
- **limitations:** Medicare claims cover predominantly elderly fee-for-service patients, limiting generalisation to younger/commercial populations; attack list depends on public reporting (underreporting of unreported attacks); attacks may be correlated with unobserved hospital characteristics, mitigated but not elimi …
- **research_gaps:** Extends the literature from descriptive attack counts and ED-volume disruption to causal patient-outcome impacts (mortality); remaining gaps include non-Medicare populations, community/ambulatory clinics, cost-of-incident response, and mechanisms (e.g., delayed procedures) through which attacks rais …

**prisma**

- **inclusion_rationale:** PASS. Source: Scopus/Google Scholar-indexed journal. Year: February 2026, within 2022-2026 window. Quartile: Q1 by Scimago SJR (7.737). Topical fit: quantified hospital consequences - core outcome-metrics pillar justifying incident-response investment.

**stratification**

- **platform_environment:** Not device-specific: hospital enterprise IT/clinical systems environment (US inpatient settings); no endpoint OS is the unit of analysis
- **kill_chain_stage:** Post-encryption: quantifies post-attack operational disruption (volume loss, T1486 impact side) and patient outcomes; not about attacker technique execution
- **dataset_benchmark:** Hospital ransomware-attack database constructed by the authors, linked to 100% Medicare FFS claims; replication data and code openly deposited at ICPSR (doi 10.3886/E235483V1, AEA publisher-hosted) - open-sourced (restricted-use Medicare data accessed through CMS/ResDAC channels)
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** High: AEA requires deposit of data and code - both publicly archived (ICPSR doi 10.3886/E235483V1); Medicare claims access requires CMS approval, but analysis recipes, event windows and identification strategy are externally auditable

**threat_intel**

- **threat_actor_fields:** Marginal: references the TrickBot/Conti ecosystem in background sourcing only; no RaaS group named as analytic subject, no leak-site or wallet-tracing analysis

---

### 11.2 Ransomware Attacks, ED Visits and Inpatient Admissions in Targeted and Nearby Hospitals

*Abouk, R.; Powell, D. (2024 (JAMA, vol. 331, no. 24, June 25 2024, pp. 2129-2131; published online May 29, 2024)). JAMA (American Medical Association; ISSN 0098-7484) - Research Letter. Q1 per Scimago SJR - Medicine (miscellaneous), Q1 every year 1999-2025; SJR 2025 = 5.843. [https://doi.org/10.1001/jama.2024.7752](https://doi.org/10.1001/jama.2024.7752) `retained-included` · `Google Scholar and Scopus (journal indexed via PubMed/MEDLINE and Scopus); verified against the JAMA article page and PubMed record PMID 38809568 (PMC11137657)`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Attacks identified from the HHS OCR breach portal cross-checked with online media coverage, restricted to attacks disruptive to care delivery. California hospital panel 2014-2020 (82,359,450 ED visits; 23,475,497 inpatient admissions): 8 disruptive ransomware attacks affecting 15 hospitals vs 355 un …
- **key_findings:** In attacked hospitals, weekly ED visits fell 8.10% (95% CI -14.40 to -1.80) in week 1 and 16.21% (95% CI -26.58 to -5.84) in week 2; inpatient admissions fell 8.16% (95% CI -19.92 to 3.60) in week 1 and 16.62% (95% CI -31.28 to -2.00) in week 2, returning to pre-attack levels within about 8 weeks. E …
- **limitations:** Only 8 attacks/15 hospitals (small treatment count, wide CIs); single US state (California), 2014-2020 window predating the 2021-2023 attack surge; outcome restricted to ED visits and inpatient admissions (no clinical complication or mortality outcomes); attack identification relies on HHS portal pl …
- **research_gaps:** Identifies inter-hospital spillover effects as an under-measured dimension of ransomware harm; gaps remain in clinical outcomes of displaced patients (e.g., longer treatment times found in adjacent ED studies), multi-state replication, and post-2020 attack-wave evidence.

**prisma**

- **inclusion_rationale:** PASS. Source: Scopus/PubMed-indexed journal. Year: 2024, within window. Quartile: Q1 by Scimago SJR (5.843). Topical fit: ED-visit disruption metrics sectoral impact study. Note: research-letter format - retained for quantified outcome evidence, not as a methodological exemplar.

**stratification**

- **platform_environment:** Not device-specific: hospital enterprise IT environment (electronic medical record servers of attacked hospitals); platform-level, no named OS
- **kill_chain_stage:** Post-encryption: measures service disruption in the weeks following destructive attacks (impact on care delivery); secondary spillover effects on unattacked hospitals
- **dataset_benchmark:** *[uncertain]*
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** *[uncertain]*

**threat_intel**

- **threat_actor_fields:** Not applicable: attack actors unknown; no RaaS group, leak-site or wallet evidence analysed

---

## 12. L. Taxonomies & prior systematic reviews (co-citation baseline)

**Papers retained: 2** · Excluded records: 0 · Uncertain fields: 3

<details><summary>Uncertain fields in this cluster</summary>

- dataset_benchmark (final included-paper count for Albshaier et al. 2024 SLR)
- evaluation_metrics (exact per-method quantitative figures quoted by Albshaier et al. 2024)
- reproducibility (protocol-documentation detail of Albshaier et al. 2024 search)

</details>

### 12.1 Earlier Decision on Detection of Ransomware Identification: A Comprehensive Systematic Literature Review

*Albshaier, L.; Almarri, S.; Rahman, M. M. H. (2024 (Information, vol. 15, issue 8, article 484; published 14 August 2024)). Information (MDPI; ISSN 2078-2489). CORRECTION of candidate-registry entry: the candidate paper was registered as 'Albshaier et al. 2024 Applied Sciences', but verification confirmed the SLR was published in MDPI Information, not Applied Sciences; authors and SLR identity match. Q2 per Scimago SJR - Information Systems (MDPI Information), Q2 continuously 2021-2025; SJR 2025 = 0.805; JCR category rank Q2 (Computer Science, Information Systems). [https://doi.org/10.3390/info15080484](https://doi.org/10.3390/info15080484) `retained-included` · `Google Scholar and Scopus (MDPI Information is Scopus-indexed, coverage 2010-present); verified against the MDPI article page and Semantic Scholar record (gold open access, CC-BY)`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** PRISMA-guided study selection (flow diagram in Section 2) filtering systematic-search results from academic databases plus industry reports and case studies, restricted to 2020-2024 publications. Contribution: categorisation of early-ransomware-detection approaches into signature-based, behaviour-pa …
- **key_findings:** Early detection before encryption is feasible only by combining warning signs, frameworks and proactive techniques; signature-only approaches fail against ever-changing samples while behaviour- and ML-based approaches offer the strongest proactive direction as long as features (API calls, file I/O a …
- **limitations:** Restricted time window (2020-2024) and English-language emphasis limits coverage of the long pre-2020 detection canon and non-English literature; qualitative assessment of effectiveness - no standardised quantitative re-benchmarking of the surveyed detectors; MDPI special-issue review so inclusion c …
- **research_gaps:** Explicitly points out gaps in current early-detection research: insufficient benchmark datasets and standardised evaluation; weak pre-encryption behaviour coverage; limited integration of ML with frameworks and industry indicators; calls for strong, proactive, continuously updated detection systems  …

**prisma**

- **inclusion_rationale:** PASS. Source: Scopus/Google Scholar-indexed journal. Year: 2024, within 2022-2026 window. Quartile: Q2 by Scimago SJR (Information Systems, SJR 2025 = 0.805) - meets the Q1/Q2 eligibility criterion. Topical fit: baseline pillar - existing PRISMA-style ransomware SLR used for comparison and as a PRIS …

**stratification**

- **platform_environment:** Framework-level review is platform-agnostic; the reviewed early-detection studies predominantly concern Windows endpoint environments, with partial coverage of mobile/Android detection work
- **kill_chain_stage:** Pre-encryption (early detection of ransomware before harm; the review's stated objective) - maps to pre-execution/pre-impact monitoring equivalent of pre-T1486 stages
- **dataset_benchmark:** *[uncertain]*
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** *[uncertain]*

**threat_intel**

- **threat_actor_fields:** Not a threat-intelligence source: no RaaS group named, no leak-site or wallet-tracing analysis; only generic ransomware strain examples as context

---

### 12.2 A Survey on Ransomware: Evolution, Taxonomy, and Defense Solutions

*Oz, H.; Aris, A.; Levi, A.; Uluagac, A. S. (2022 (ACM Computing Surveys, vol. 54, issue 11s, article 238, pp. 1-37; published online 9 September 2022)). ACM Computing Surveys (CSUR) (Association for Computing Machinery; ISSN 0360-0300). Q1 per Scimago SJR - Computer Science (miscellaneous), Q1 continuously 2000-2025; SJR 2022 = 4.457 and SJR 2025 = 5.985; Theoretical Computer Science Q1 2023-2025. [https://doi.org/10.1145/3514229](https://doi.org/10.1145/3514229) `retained-included` · `Google Scholar (cited by ~500) and Scopus (ACM Computing Surveys Scopus-indexed); verified against the ACM Digital Library record and the arXiv preprint (arXiv:2102.06249v2) with related DOI 10.1145/3514229`

**bibliographic**


**content**

- **study_type:** *[uncertain]*
- **methodology:** Structured literature synthesis of 137 studies (1989-2020) across three target platforms (PCs/workstations, mobile devices, IoT/CPS). Contributions: detailed ransomware evolution narrative from early disk-encryptingPoC families to modern double-extortion campaigns; analysis of key ransomware buildin …
- **key_findings:** First survey to jointly cover evolution, taxonomy and defense across workstation, mobile and IoT/CPS platforms: documents the shift from simple locker/crypto families toward target-of-choice, double-extortion and platform-diversified operations; shows detection research is dominated by workstation-f …
- **limitations:** Coverage stops at studies published through 2020, pre-dating the 2021-2024 surge in double-extortion RaaS, leak sites and healthcare-focused campaigns; narrative (non-PRISMA) search process limits reproducibility of the corpus; no quantitative meta-comparison of reported detection accuracies across  …
- **research_gaps:** Provides the extensive open-issues list used as the comparison baseline for the present review: no study existed giving a complete platform-diverse picture of ransomware and defenses; gaps include IoT/CPS defense research, recovery research, evaluation-uniformity, evading/anti-analysis countermeasur …

**prisma**

- **inclusion_rationale:** PASS. Source: Scopus/Google Scholar-indexed journal (ACM CSUR). Year: 2022, within 2022-2026 window. Quartile: Q1 by Scimago SJR (4.457 in 2022; 5.985 in 2025). Topical fit: baseline pillar - the highest-cited ransomware taxonomy/defense survey of the window, used to position the new review against  …

**stratification**

- **platform_environment:** Explicitly stratified by platform: PCs/workstations (Windows-dominant), mobile devices (Android/iOS), and IoT/CPS environments
- **kill_chain_stage:** Full chain: pre-encryption (infection vectors, C&C, anti-analysis analysis), during/post-encryption (system and file-level detection, T1471/T1486 impact side) and post-encryption recovery
- **dataset_benchmark:** Corpus = 137 primary studies (1989-2020) from journals and conferences, plus notable ransomware family samples discussed; corpus itself not open-sourced but fully enumerated in the paper's reference list
- **evaluation_metrics:** *[uncertain]*

**reproducibility_risk**

- **reproducibility:** Moderate: complete 137-study coverage list and taxonomy enable locating all primary works, but the survey uses a narrative (non-PRISMA) method with no documented search protocol; free-access ACM version plus arXiv version ease verification

**threat_intel**

- **threat_actor_fields:** Partial: taxonomy of notable ransomware families (e.g., CryptoLocker, WannaCry, Locky, Cerber, Android/Linux locker families) by behaviour and platform, and documented operational activities (e.g., Tesla insider-bribe incident, double-extortion evolution); no RaaS-group attribution, leak-site teleme …

---

## Uncertainty summary
- Clusters: 12 · Retained papers: 25 · Uncertain fields flagged: 28

## Methodology note
Fields produced by the deep-research phase were validated with validate_json.py (12/12 pass, 100% coverage). Values failing verification were marked [uncertain] and are shown as `*[uncertain]*` rather than omitted, per PRISMA transparency practice.
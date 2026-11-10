#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prune SLR results to the ~25-paper target, preserving PRISMA transparency.

Moved records go to excluded_records with rationale; nothing is silently deleted.
"""
import json
import pathlib

RESULTS = pathlib.Path(r"C:\Users\Albert Wesley\Desktop\researchRansomware\ransomware-slr\results")

ID_KEYS = ("paper_id", "paper")

# file -> (drop spec list).  pid-substr match or numeric pin index.
PRUNE = {
    "A_AI_ML_detection": [
        ("pid_substr", "razaulla2023", "Record-overlap prune: coverage of ransomware evolution/taxonomy redundant with alzahrani2025 (2019-2025 survey) and isphany2024; earliest of three overlapping IEEE Access reviews"),
        ("pid_substr", "ferdous2024", "Record-overlap prune: AI-detection scope redundant with isphany2024_ml_review and alzahrani2025_survey_detection_methods"),
    ],
    "B_behavioural_deception_detection": [
        ("pid_substr", "fang2025", "Validity prune: dataset_benchmark unidentifiable (uncertain), and honeyfile approach overlaps gomezhernandez2024_honeyfile_android which has full parameter disclosure"),
    ],
    "C_traffic_network_detection": [
        ("pid_substr", "berrueta2022", "Recency/overlap prune: oldest traffic-based record (2022); encrypted-traffic detection scope covered by almashhadani2022 (in-network) and lan2025 (federated, current)"),
    ],
    "D_XAI_reproducibility": [
        ("pid_substr", "Pereira et al. 2026", "Eligibility prune: IEEE EuroS&PW workshop proceedings carry no Scimago SJR quartile; fails strict Q1/Q2 journal criterion"),
    ],
    "E_AI_era_threats": [
        ("pid_substr", "arXiv preprint", "Eligibility prune: arXiv:2508.20444 (Ransomware 3.0) has no peer-reviewed journal/conference version as of 2026-10-21; retained only as provenance lead for PromptLock"),
    ],
    "F_prevention_resilience": [
        ("pid_substr", "Zhang et al. 2023", "Scope prune: formal game-theoretic modeling most tangential to the review's prevention-engineering focus; empirical/simulation (Ilau2025) and system-design (McIntosh2023/SEDAC) evidence retained"),
    ],
    "I_incident_response_forensics": [
        ("pin", 1, "Validity prune: Bajpai & Enbody 2023 recorded as Q2 (2023 SJR 0.595) but commonly misquoted as Q1; weakest quartile evidence in cluster, overlaps Shaked2023 playbook framework"),
        ("pin", 4, "Overlap prune: Kara & Aydos 2022 single-OS (Windows) forensic analysis overlaps forensic-readiness scope of Huck & Breitinger 2022; methodological redundancy"),
    ],
    "K_sectoral_impact": [
        ("pin", 3, "Overlap prune: JAMA Network Open 2025 descriptive breach-trend analysis; causal/design-based evidence retained in Neprash2026 (DiD, outcomes) and Abouk-Powell2024 (DiD, ED spillovers)"),
    ],
}


def pid_of(e):
    for k in ID_KEYS:
        if k in e:
            v = e[k]
            return v if isinstance(v, str) else f"paper_{v}"
    return None


def prune():
    for f in sorted(RESULTS.glob("*.json")):
        spec = PRUNE.get(f.stem)
        if not spec:
            print(f"keep all: {f.stem}")
            continue
        data = json.loads(f.read_text(encoding="utf-8"))

        def to_drop(e):
            for mode, needle, reason in spec:
                if mode == "pin":
                    if pid_of(e) == f"paper_{needle}":
                        return reason
                else:
                    if str(pid_of(e)).lower().find(needle.lower()) != -1:
                        return reason
            return None

        dropped, missing = {}, list(spec)
        for field, entries in data.items():
            if field in ("uncertain", "excluded_records") or not isinstance(entries, list):
                continue
            keep = []
            for e in entries:
                r = to_drop(e)
                if r:
                    tag = next(s[1] for s in spec if (s[0] == "pin" and f"paper_{s[1]}" == str(pid_of(e)))
                               or (s[0] != "pin" and str(pid_of(e)).lower().find(s[1].lower()) != -1))
                    dropped.setdefault(tag, (e["value"], r))
                    for m in missing:
                        if m[1] == tag:
                            missing.remove(m)
                    continue
                keep.append(e)
            data[field] = keep

        recs = data.setdefault("excluded_records", [])
        for r in missing:
            recs.append({"paper_ref": r[1], "decision": "PRUNE-UNRESOLVED",
                         "reason": f"Spec pattern not found in field data: {r[0]} match '{r[1]}' - {r[2]}"})
        for tag, (title, reason) in sorted(dropped.items()):
            recs.append({"paper_ref": tag, "decision": "PRUNED",
                         "title": title, "reason": reason})

        # strip uncertain refs to pruned papers (titles only reference cluster ids)
        f.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"pruned {len(dropped):2d} (unresolved {len(missing)}): {f.stem}")


if __name__ == "__main__":
    prune()

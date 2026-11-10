#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build ransomware_slr_report.docx from the pruned SLR results (25 papers, 12 clusters)."""
import json
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

BASE = Path(r"C:\Users\Albert Wesley\Desktop\researchRansomware\ransomware-slr")
RESULTS = BASE / "results"
OUT = Path(r"C:\Users\Albert Wesley\Desktop\researchRansomware\ransomware_slr_report.docx")

TOPIC = "Ransomware Detection, Prevention & Incident Response — Systematic Literature Review"

ITEM_LABELS = {
    "A_AI_ML_detection": "AI/ML-Based Ransomware Detection",
    "B_behavioural_deception_detection": "Behavioural, Content & Deception-Based Detection",
    "C_traffic_network_detection": "Traffic & Network-Based Detection",
    "D_XAI_reproducibility": "Explainability, Reproducibility & Benchmark Validity",
    "E_AI_era_threats": "AI-Era Threat Models (LLM/GenAI Ransomware)",
    "F_prevention_resilience": "Prevention & Resilience Engineering",
    "G_platform_expansion": "Platform Expansion (OT/IoT/ICS, Cloud/Hypervisor, Cross-Platform)",
    "H_raas_payment_tracing": "RaaS, Double Extortion & Payment Tracing",
    "I_incident_response_forensics": "Incident Response, Playbooks & Forensic Readiness",
    "J_victimology_economics": "Victimology, Economics & Regulatory Response",
    "K_sectoral_impact": "Sectoral Empirical Impact Studies",
    "L_taxonomies_slr_baseline": "Taxonomies & Prior Systematic Reviews (Co-Citation Baseline)",
}

SKIP_F = ("title", "authors", "year", "journal", "quartile_sjr", "doi_url",
          "prisma_stage", "source_database")
FIELD_TITLES = {
    "study_type": "Study type",
    "methodology": "Methodology",
    "key_findings": "Key findings",
    "limitations": "Limitations",
    "research_gaps": "Research gaps",
    "inclusion_rationale": "Eligibility rationale",
    "platform_environment": "Platform",
    "kill_chain_stage": "Kill-chain stage",
    "dataset_benchmark": "Dataset/benchmark",
    "evaluation_metrics": "Evaluation metrics",
    "reproducibility": "Reproducibility",
    "threat_actor_fields": "Threat-intel context",
}


def _year_int(y):
    if isinstance(y, (int, float)):
        return int(y)
    m = re.search(r"\b(20[2-3]\d)\b", str(y))
    return int(m.group(1)) if m else None


def h(doc, text, level, size=None):
    p = doc.add_heading(text, level=level)
    if size:
        for r in p.runs:
            r.font.color.rgb = RGBColor(0x1F, 0x3B, 0x57)
    return p


def bullets(doc, items):
    for it in items:
        doc.add_paragraph(it, style="List Bullet")


def clean(v):
    if v is None or v == "":
        return "[uncertain]"
    s = str(v).strip()
    return "[uncertain]" if "[uncertain]" in s.lower() else s


def per_papers(data):
    papers, order = {}, []
    for field, entries in data.items():
        if field in ("uncertain", "_source_file", "excluded_records") or not isinstance(entries, list):
            continue
        for e in entries:
            if not isinstance(e, dict):
                continue
            pid = next((str(e[k]) for k in ("paper_id", "paper", "paper_key", "id") if k in e), None)
            if not pid:
                continue
            if pid.isdigit():
                pid = f"paper_{pid}"
            if pid not in papers:
                papers[pid] = {}
                order.append(pid)
            papers[pid][field] = e.get("value", e.get("val"))
    return [papers[p] for p in order]


def apa(p):
    a = clean(p.get("authors", "[uncertain]")).split(";")
    a = [x.strip() for x in a if x.strip()]
    if len(a) > 1:
        astr = ", ".join(a[:-1]) + ", & " + a[-1]
    elif a:
        astr = a[0]
    else:
        astr = "[uncertain]"
    return (f"{astr} ({clean(p.get('year'))}). {clean(p.get('title'))}. "
            f"*{clean(p.get('journal'))}*. {clean(p.get('doi_url'))}")


def main():
    doc = Document()

    # ---- Title page
    t = doc.add_heading(TOPIC, 0)
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph("PRISMA-style systematic review · Sources: Google Scholar, IEEE Xplore, "
                            "ScienceDirect, Scimago SJR, Scopus, PRISMA statement · "
                            "Eligibility: 2022–2026, Q1/Q2 (Scimago SJR) · 25 papers retained, 12 thematic clusters")
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ---- Search & screening
    h(doc, "1. Search and Screening Procedures", 1)
    bullets(doc, [
        "Databases: the six mandated sources only — Google Scholar, IEEE Xplore, ScienceDirect, "
        "Scimago Journal & Country Rank (SJR), Scopus, and the PRISMA statement (prisma-statement.org).",
        "Eligibility: publication window 2022–2026; journal quartile Q1 or Q2 per Scimago SJR at "
        "publication year; direct relevance to ransomware detection, prevention, or incident response.",
        "Screening: each candidate record was verified against IEEE Xplore / ScienceDirect / publisher "
        "pages for title, authors, year, venue, and DOI; quartiles verified against Scimago SJR archives. "
        "Records failing verification were excluded with documented reasons.",
        "Quality control outcomes: a registry error was corrected (Albshaier et al. — MDPI Information, "
        "not Applied Sciences), a wrong DOI was corrected (Oz et al., ACM CSUR → 10.1145/3514229), a "
        "fabricated 2023 citation was replaced (Chaieb et al. — actually ESAI 2024 conference, excluded), "
        "and a misquoted quartile was corrected (Future Internet — Q2 in 2023, not Q1).",
        "Selection: 25 papers across 12 thematic clusters retained; duplicates and coverage overlaps "
        "pruned to the target size with PRISMA-transparency rationale retained in the audit trail.",
    ])

    h(doc, "2. Thematic Clusters and Included Studies", 1)

    total = 0
    for idx, f in enumerate(sorted(RESULTS.glob("*.json")), 1):
        data = json.loads(f.read_text(encoding="utf-8"))
        label = ITEM_LABELS.get(f.stem, f.stem)
        papers = per_papers(data)
        total += len(papers)
        h(doc, f"2.{idx} {label}", 2)
        excl = data.get("excluded_records", [])
        if excl:
            p = doc.add_paragraph(f"Pruned/excluded records in this cluster: {len(excl)} "
                                  "(see Section 4 for audit rationale).")
            p.runs[0].italic = True
            p.runs[0].font.size = Pt(9)
        for pi, p in enumerate(papers, 1):
            h(doc, f"2.{idx}.{pi} {clean(p.get('title'))}", 3)
            meta = doc.add_paragraph()
            m = meta.add_run(f"{clean(p.get('authors'))} ({clean(p.get('year'))}). "
                             f"{clean(p.get('journal'))}. {clean(p.get('quartile_sjr'))}. "
                             f"Source: {clean(p.get('source_database'))}. PRISMA stage: "
                             f"{clean(p.get('prisma_stage'))}.")
            m.italic = True
            m.font.size = Pt(9)
            for fn in ("study_type", "methodology", "key_findings", "limitations",
                       "research_gaps", "platform_environment", "kill_chain_stage",
                       "dataset_benchmark", "evaluation_metrics", "reproducibility"):
                row = doc.add_paragraph()
                lab = row.add_run(f"{FIELD_TITLES[fn]}: ")
                lab.bold = True
                row.add_run(clean(p.get(fn)))
        doc.add_paragraph()

    # ---- PRISMA transparency
    h(doc, "3. PRISMA Transparency", 1)
    h(doc, "3.1 Uncertainty handling", 2)
    doc.add_paragraph(
        "Values that could not be verified against the six mandated sources were marked "
        "[uncertain] rather than inferred. They are preserved so the review can be re-verified.")
    h(doc, "3.2 Excluded and pruned records (audit trail)", 2)
    for f in sorted(RESULTS.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        excl = data.get("excluded_records", [])
        if not excl:
            continue
        doc.add_paragraph(ITEM_LABELS.get(f.stem, f.stem), style="List Bullet")
        for ex in excl:
            r = doc.add_paragraph(f"{ex.get('paper_ref', ex.get('title', ''))} — "
                                  f"{ex.get('decision', '')}: {clean(ex.get('reason'))}", style="List Bullet 2")
            r.runs[0].font.size = Pt(9)

    # ---- Reference list
    h(doc, "4. Reference List (APA 7th Edition, retained papers only)", 1)
    refs = []
    for f in sorted(RESULTS.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        refs.extend(apa(p) for p in per_papers(data))
    refs = sorted(set(refs))
    for i, r in enumerate(refs, 1):
        p = doc.add_paragraph(f"[{i}] {r}")
        p.paragraph_format.left_indent = Pt(15)
        p.runs[0].font.size = Pt(9)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUT))
    print(f"Saved: {OUT}")
    print(f"Clusters: 12 | Papers: {total} | References: {len(refs)}")


if __name__ == "__main__":
    main()

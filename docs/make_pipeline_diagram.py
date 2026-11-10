"""Render the ransomware-slr review pipeline as a dark, PRISMA-style flow diagram.

Output: docs/pipeline.png
Palette matches the portfolio site (dark surface + neon cyan/green/purple accents).
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

BG = "#05080d"
SURFACE = "#0d141d"
BORDER = "#182433"
TEXT = "#dde8f0"
MUTED = "#8fa5b5"
CYAN = "#2ad4e8"
GREEN = "#34d399"
PURPLE = "#a78bfa"
PINK = "#f472b6"

fig, ax = plt.subplots(figsize=(15.5, 9.2), dpi=150)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")


def box(x, y, w, h, title, body="", accent=CYAN, title_size=10, body_size=7.2, body_gap=4.2):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.5,rounding_size=1.2",
            facecolor=SURFACE, edgecolor=accent, linewidth=1.4,
        )
    )
    ax.text(x + w / 2, y + h - 2.3, title, ha="center", va="top",
            color=TEXT, fontsize=title_size, fontweight="bold")
    if body:
        ax.text(x + w / 2, y + h - 2.3 - body_gap, body, ha="center", va="top",
                color=MUTED, fontsize=body_size, linespacing=1.5)


def arrow(p1, p2, color=CYAN, conn="arc3,rad=0"):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=14,
                                 linewidth=1.3, color=color, connectionstyle=conn,
                                 shrinkA=1, shrinkB=1))


def seg(p1, p2, color=MUTED):
    ax.add_line(Line2D([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=1.2))


# ---------------- Title ----------------
ax.text(50, 98, "RANSOMWARE DETECTION, PREVENTION & INCIDENT RESPONSE — SLR 2022–2026",
        ha="center", va="top", color=TEXT, fontsize=13.5, fontweight="bold")
ax.text(50, 94.2, "review pipeline  ·  PRISMA 2020-style  ·  protocol: outline.yaml + fields.yaml + results/*.json",
        ha="center", va="top", color=MUTED, fontsize=8.5)

# ---------------- Row 1: sources ----------------
src = ["Google Scholar", "IEEE Xplore", "ScienceDirect", "Scopus",
       "Scimago SJR\n(quartile check)", "PRISMA 2020\n(method anchor)"]
w1, gap = 14.4, 1.62
xs = [3 + i * (w1 + gap) for i in range(6)]
for s, x in zip(src, xs):
    box(x, 80.5, w1, 8.5, s, accent=BORDER, title_size=8.2)
    seg((x + w1 / 2, 80.5), (x + w1 / 2, 78.2))

seg((xs[0] + w1 / 2, 78.2), (xs[-1] + w1 / 2, 78.2))
arrow((50, 78.2), (50, 76.8))
ax.text(50, 76.4, "eligibility: journal papers, 2022–2026, Scimago Q1/Q2 at publication year",
        ha="center", va="top", color=MUTED, fontsize=7.6, style="italic")

# ---------------- Row 2: clusters ----------------
box(23, 61, 54, 12.5, "12 REVIEW CLUSTERS (A–L)",
    "detection · deception · network · XAI / reproducibility · AI-era threats · prevention\n"
    "platforms (OT/IoT, NAS, hypervisor) · RaaS & payment tracing · IR & forensics\n"
    "victimology & economics · sectoral impact · taxonomies & prior reviews",
    accent=CYAN, title_size=10.5, body_gap=4.6)

arrow((36, 61), (17.5, 58.2), color=GREEN, conn="arc3,rad=0.10")
arrow((61, 61), (50, 58.2), color=PINK, conn="arc3,rad=-0.10")

# ---------------- Row 3: screening / prune / retained ----------------
box(3, 45.5, 29, 12.5, "CANDIDATE SCREENING",
    "year · SJR quartile · allowed source ·\ntopical fit  →  41 records assessed\nat eligibility",
    accent=GREEN)
box(35.5, 45.5, 29, 12.5, "PRUNE / EXCLUDE LOG",
    "16 decisions with reasons\ntranscribed verbatim in S1\n(summary in Appendix A)",
    accent=PINK)
box(68, 45.5, 29, 12.5, "25 RETAINED PAPERS",
    "23 × Q1   ·   2 × Q2\n2022:4  2023:6  2024:7  2025:5  2026:3\nComputers & Security: 8 (most common)",
    accent=GREEN)

# screening -> prune (short side arrow)
arrow((32.4, 52), (35.1, 52), color=PINK)

# screening -> retained, routed through the corridor between rows 3 and 4
seg((17.5, 45.5), (17.5, 43.6), color=GREEN)
seg((17.5, 43.6), (82.5, 43.6), color=GREEN)
arrow((82.5, 43.6), (82.5, 45.3), color=GREEN)

# ---------------- Row 4: extraction / verification ----------------
arrow((12, 45.5), (12, 42.9), color=PURPLE)
arrow((88, 45.5), (88, 42.9), color=PURPLE)

box(2, 30, 45, 12.6, "STRUCTURED EXTRACTION  (S1, S2)",
    "bibliographic · SJR quartile · methodology · findings · limitations · gaps\n"
    "platform / kill-chain stage · dataset & metric disclosure · reproducibility\n"
    "threat-intelligence coverage — unverified values flagged [uncertain]",
    accent=PURPLE)
box(53, 30, 45, 12.6, "CITATION VERIFICATION",
    "25 / 25 reference DOIs verified against the\n"
    "Crossref Works API (2026-10-24): titles,\n"
    "journals and years all match",
    accent=PURPLE)

# ---------------- Row 5: synthesis ----------------
arrow((30, 30), (40, 28.3), color=CYAN)
arrow((68, 30), (60, 28.3), color=CYAN)

box(20, 17, 60, 11, "THEMATIC SYNTHESIS  →  report.md",
    "6 research questions (RQ1–RQ6) · narrative synthesis, no meta-analysis\n"
    "(incompatible effect measures) · every claim traceable to an S1 extract",
    accent=CYAN, body_gap=4.6)

# ---------------- Row 6: outputs ----------------
arrow((38, 17), (18, 12.7), color=CYAN, conn="arc3,rad=0.08")
arrow((50, 17), (50, 12.7), color=CYAN)
arrow((62, 17), (82, 12.7), color=CYAN, conn="arc3,rad=-0.08")

box(4, 4.5, 28, 8, "DOCX MANUSCRIPT", "report-ready literature review",
    accent=CYAN, title_size=8.8, body_gap=3.4)
box(36, 4.5, 28, 8, "REPRODUCIBILITY KIT", "fields.yaml · prune_results.py · generate_docx.py",
    accent=CYAN, title_size=8.8, body_gap=3.4, body_size=6.9)
box(68, 4.5, 28, 8, "TRANSPARENCY ARTIFACTS", "PRISMA checklist (App. B) · uncertainty register (App. C)",
    accent=CYAN, title_size=8.8, body_gap=3.4, body_size=6.9)

fig.savefig("docs/pipeline.png", facecolor=BG, bbox_inches="tight")
print("wrote docs/pipeline.png")

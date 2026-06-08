"""Genere le chart slide 10 : projection 2 scenarios sur 12 mois (Velura).

Voie 3 (matplotlib PNG sans texte + JSON overlays pour PptxGenJS).

Scenario inaction (orange) : cumul perte jusqu'a ~88 k€ a m+12
Scenario plan 90j (bleu) : stable 3 mois puis remontee jusqu'a +12 k€

Conformement a CLAUDE.md §6.6 / Erreur #11 :
- PNG ne contient AUCUN texte (lignes + grille + zone ombree seulement)
- JSON sidecar donne les coordonnees relatives ou placer les textes via
  PptxGenJS slide.addText() en superposition (editable).
"""

import json
import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Palette Empirik
ORANGE = "#E9540D"
BLUE = "#0A3856"
GREY = "#B0B0B0"
BG = "#FFFFFF"

# Donnees : 12 mois (m+0 = jun 2026 -> m+12 = juin 2027 = 13 points)
months = np.arange(0, 13)

# Scenario inaction : courbe accelerative jusqu'a -88 k€ cumules
# 43 k€/an = ~3.6 k€/mois en moyenne, mais perte qui s'accelere
# m+0=0, m+12=-88. Profil accelere puis plateau leger.
inaction = -1 * np.array(
    [0, 3, 7, 13, 20, 28, 37, 47, 57, 67, 76, 83, 88], dtype=float
)

# Scenario plan 90j : descend legerement les 3 premiers mois (decaissement),
# stabilise m+3-m+5, remonte progressivement pour finir a +12 k€ a m+12.
plan = np.array(
    [0, -3, -5, -6, -6, -5, -2, 1, 4, 7, 9, 11, 12], dtype=float
)

fig, ax = plt.subplots(figsize=(11, 5.2), dpi=160)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

# Zone ombree entre les 2 courbes (ecart manque a gagner)
ax.fill_between(
    months, inaction, plan, where=(plan >= inaction),
    color=ORANGE, alpha=0.10, interpolate=True
)

# Ligne baseline 0
ax.axhline(0, color=GREY, linewidth=0.8, linestyle="--", alpha=0.6, zorder=1)

# Courbe inaction (orange epaisse)
ax.plot(months, inaction, color=ORANGE, linewidth=3.5, zorder=3, solid_capstyle="round")
# Point final inaction (marker)
ax.plot([months[-1]], [inaction[-1]], "o", color=ORANGE, markersize=10, zorder=5)

# Courbe plan (bleu Empirik epaisse)
ax.plot(months, plan, color=BLUE, linewidth=3.5, zorder=3, solid_capstyle="round")
# Point final plan (marker)
ax.plot([months[-1]], [plan[-1]], "o", color=BLUE, markersize=10, zorder=5)

# Decombrer : pas de bordure, pas de gridlines majeures, fond blanc
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_color(GREY)
ax.spines["left"].set_color(GREY)
ax.spines["bottom"].set_linewidth(0.6)
ax.spines["left"].set_linewidth(0.6)

# AUCUN texte sur les axes (regle Voie 3 / Erreur #11)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-0.2, 13.2)
ax.set_ylim(-100, 25)

# Marges
plt.subplots_adjust(left=0.04, right=0.96, top=0.96, bottom=0.06)

output_png = "assets/charts/slide10-projection.png"
output_json = "assets/charts/slide10-projection.overlays.json"
os.makedirs("assets/charts", exist_ok=True)
plt.savefig(output_png, dpi=160, facecolor=BG, edgecolor="none", bbox_inches=None, pad_inches=0)
plt.close()

# Generer le JSON overlays
# Coordonnees en % du PNG. Le PNG fait 11 x 5.2 inches = 1760 x 832 px
# Axe X : month 0 a 12 mapped sur xlim -0.2 a 13.2 => ratio
xlim_min, xlim_max = -0.2, 13.2
ylim_min, ylim_max = -100, 25
plot_left_pct = 0.04
plot_right_pct = 0.96
plot_top_pct = 0.04  # 1 - 0.96
plot_bottom_pct = 0.94  # 1 - 0.06

def x_to_pct(x):
    rel = (x - xlim_min) / (xlim_max - xlim_min)
    return plot_left_pct + rel * (plot_right_pct - plot_left_pct)


def y_to_pct(y):
    rel = (y - ylim_min) / (ylim_max - ylim_min)
    # Y inverse : top=1
    return plot_bottom_pct - rel * (plot_bottom_pct - plot_top_pct)


overlays = [
    # X axis labels (mois)
    {"type": "x_label", "x_pct": x_to_pct(0), "y_pct": 0.96, "text": "Juin 2026", "align": "center", "color": "0A3856", "bold": False, "size": 10},
    {"type": "x_label", "x_pct": x_to_pct(6), "y_pct": 0.96, "text": "Dec. 2026", "align": "center", "color": "0A3856", "bold": False, "size": 10},
    {"type": "x_label", "x_pct": x_to_pct(12), "y_pct": 0.96, "text": "Juin 2027", "align": "center", "color": "0A3856", "bold": False, "size": 10},

    # Annotation finale inaction (orange)
    {"type": "annotation_inaction", "x_pct": x_to_pct(12) + 0.005, "y_pct": y_to_pct(-88) - 0.04, "text": "~88 k€ cumules perdus", "align": "right", "color": "E9540D", "bold": True, "size": 12},
    {"type": "label_inaction", "x_pct": x_to_pct(7), "y_pct": y_to_pct(-47) + 0.06, "text": "Scenario inaction", "align": "left", "color": "E9540D", "bold": True, "size": 11},

    # Annotation finale plan (bleu)
    {"type": "annotation_plan", "x_pct": x_to_pct(12) + 0.005, "y_pct": y_to_pct(12) - 0.04, "text": "~+12 k€ a m+12", "align": "right", "color": "0A3856", "bold": True, "size": 12},
    {"type": "label_plan", "x_pct": x_to_pct(6), "y_pct": y_to_pct(0) - 0.06, "text": "Scenario plan 90j", "align": "left", "color": "0A3856", "bold": True, "size": 11},

    # Y axis label (gauche, fin gris)
    {"type": "y_label", "x_pct": 0.005, "y_pct": y_to_pct(-50), "text": "k€ cumules", "align": "left", "color": "B0B0B0", "bold": False, "size": 9},
    {"type": "y_zero", "x_pct": 0.005, "y_pct": y_to_pct(0) - 0.025, "text": "0", "align": "left", "color": "B0B0B0", "bold": False, "size": 9},
]

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(overlays, f, ensure_ascii=False, indent=2)

print(f"OK chart -> {output_png} ({os.path.getsize(output_png)} bytes)")
print(f"OK overlays -> {output_json} ({len(overlays)} entries)")

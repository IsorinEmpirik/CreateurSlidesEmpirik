#!/usr/bin/env python3
"""
generate_chart.py · Generer un graphique a la charte Empirik.

Voie 3 du choix de generation de graphes (CLAUDE.md §6.6) : Python matplotlib
genere SEULEMENT le visuel (lignes, points, barres, gradients) dans un PNG
transparent, ET un fichier JSON sidecar avec les coordonnees des textes a
superposer via PptxGenJS.

Pourquoi cette separation : un texte hard-code dans un PNG est pixelise et
non-editable une fois importe dans Google Slides / PowerPoint. Les libelles
doivent rester des elements PptxGenJS editables (cf PROCESS-ANTI-ERREURS
Erreur #11).

Usage :
  python scripts/generate_chart.py --type slope \\
    --data data.json --output assets/charts/slope-evolution.png --highlight Barillet

Sorties :
  - assets/charts/slope-evolution.png  (visuel pur, sans texte)
  - assets/charts/slope-evolution.overlays.json  (positions des textes en % du PNG)

Format JSON attendu pour --data (exemple slope) :
  {
    "periods": ["Mars 2026", "Mai 2026"],
    "series": {
      "Barillet": [3.2, 4.5],
      "Dispano": [18.2, 24.3],
      "Point P": [10.1, 12.5]
    }
  }

Format JSON overlays produit :
  [
    {"type": "x_label_left",  "x_pct": 0.18, "y_pct": 0.05, "text": "Mars 2026",
     "align": "center", "color": "0A3856", "bold": true, "size": 12},
    {"type": "series_left", "x_pct": 0.05, "y_pct": 0.82, "text": "Barillet  3.2",
     "align": "right", "color": "E9540D", "bold": true, "size": 11},
    ...
  ]

Le script build_xxx.js lit le JSON et place les textes via addText() en
superposition de l'image, calculant les coordonnees relatives a la position
de l'addImage().

Types supportes : slope, line, dot, heatmap, waterfall, bar, dumbbell
"""
import argparse
import json
import sys
from pathlib import Path

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except ImportError:
    print("Erreur : matplotlib non installe. Installer avec :")
    print("  pip install matplotlib")
    sys.exit(1)

# === Charte Empirik ======================================================
BLUE = '#0A3856'
ORANGE = '#E9540D'
YELLOW = '#FCC02D'
GREY = '#B0B0B0'
LIGHT_GREY = '#E5E5E5'

# Couleurs sans # pour PptxGenJS
BLUE_HEX = '0A3856'
ORANGE_HEX = 'E9540D'
GREY_HEX = 'B0B0B0'
TEXT_GREY_HEX = '6B7280'

# === Helpers =============================================================

def setup_clean_axes(ax):
    """Cadre minimal : pas de spines, pas de ticks, fond transparent."""
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('none')


def save_png_and_overlays(fig, png_path, overlays):
    """Sauvegarde le PNG transparent + le JSON overlays sidecar."""
    png_path = Path(png_path)
    png_path.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(png_path, format='png', transparent=True, dpi=200,
                bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)

    overlays_path = png_path.with_suffix('').with_name(png_path.stem + '.overlays.json')
    with open(overlays_path, 'w', encoding='utf-8') as f:
        json.dump(overlays, f, indent=2, ensure_ascii=False)

    print(f"  ok    {png_path.name}  ({png_path.stat().st_size} bytes)")
    print(f"  ok    {overlays_path.name}  ({len(overlays)} text overlays)")


# === Generateurs =========================================================

def gen_slope(data, png_path, highlight=None):
    """Slope graph 2 periodes x N categories.
    PNG = lignes seules. JSON = labels periodes + labels series."""
    periods = data['periods']
    series = data['series']

    fig, ax = plt.subplots(figsize=(10, 5), dpi=200, facecolor='none')
    fig.patch.set_alpha(0)

    # Marges symetriques pour le centrage
    ax.set_xlim(-0.05, 1.05)

    overlays = []

    # Tracer les lignes
    n_series = len(series)
    for name, values in series.items():
        is_vedette = (name == highlight)
        color = ORANGE if is_vedette else GREY
        lw = 3 if is_vedette else 1.5
        alpha = 1.0 if is_vedette else 0.6
        ms = 9 if is_vedette else 5

        ax.plot([0, 1], values, color=color, linewidth=lw, alpha=alpha,
                marker='o', markersize=ms,
                zorder=10 if is_vedette else 5)

    # Calculer la plage Y pour normaliser les overlays
    all_vals = [v for vals in series.values() for v in vals]
    y_min = min(all_vals)
    y_max = max(all_vals)
    y_range = y_max - y_min if y_max != y_min else 1
    ax.set_ylim(y_min - y_range * 0.15, y_max + y_range * 0.15)

    setup_clean_axes(ax)

    # === Overlays : labels periodes en haut + labels series en bouts de ligne ===
    # Calculer les positions Y en % du PNG (haut = 0, bas = 1)
    def y_to_pct(val):
        # Inverse car axe matplotlib Y va de bas en haut
        ax_y_min, ax_y_max = ax.get_ylim()
        return 1.0 - (val - ax_y_min) / (ax_y_max - ax_y_min)

    # Labels periodes (au-dessus du graphe)
    overlays.append({
        "type": "x_label",
        "x_pct": 0.05, "y_pct": -0.08,
        "w_pct": 0.20, "h_pct": 0.06,
        "text": periods[0], "align": "center",
        "color": BLUE_HEX, "bold": True, "size": 12
    })
    overlays.append({
        "type": "x_label",
        "x_pct": 0.75, "y_pct": -0.08,
        "w_pct": 0.20, "h_pct": 0.06,
        "text": periods[1], "align": "center",
        "color": BLUE_HEX, "bold": True, "size": 12
    })

    # Labels series gauche + droite (en bouts de ligne)
    for name, values in series.items():
        is_vedette = (name == highlight)
        color_hex = ORANGE_HEX if is_vedette else TEXT_GREY_HEX

        overlays.append({
            "type": "series_left",
            "x_pct": -0.02, "y_pct": y_to_pct(values[0]) - 0.025,
            "w_pct": 0.18, "h_pct": 0.05,
            "text": f"{name}  {values[0]}", "align": "right",
            "color": color_hex, "bold": is_vedette, "size": 11
        })
        overlays.append({
            "type": "series_right",
            "x_pct": 0.84, "y_pct": y_to_pct(values[1]) - 0.025,
            "w_pct": 0.18, "h_pct": 0.05,
            "text": f"{values[1]}  {name}", "align": "left",
            "color": color_hex, "bold": is_vedette, "size": 11
        })

    save_png_and_overlays(fig, png_path, overlays)


def gen_line(data, png_path, highlight=None):
    """Line chart avec une serie eventuellement mise en vedette.
    PNG = lignes seules. JSON = labels x + labels series."""
    x_labels = data['x']
    series = data['series']
    n = len(x_labels)

    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=200, facecolor='none')
    fig.patch.set_alpha(0)

    for name, values in series.items():
        is_vedette = (name == highlight)
        color = ORANGE if is_vedette else GREY
        lw = 3 if is_vedette else 1.5
        ax.plot(range(n), values, color=color, linewidth=lw,
                marker='o' if is_vedette else None,
                markersize=7, zorder=10 if is_vedette else 5)

    # Y range
    all_vals = [v for vals in series.values() for v in vals]
    y_min = min(all_vals)
    y_max = max(all_vals)
    y_range = y_max - y_min if y_max != y_min else 1
    ax.set_ylim(y_min - y_range * 0.1, y_max + y_range * 0.1)
    ax.set_xlim(-0.5, n - 0.5)

    setup_clean_axes(ax)

    overlays = []

    # Labels X (sous le graphe)
    for i, lbl in enumerate(x_labels):
        x_pct = (i + 0.5) / n
        overlays.append({
            "type": "x_label",
            "x_pct": x_pct - 0.05, "y_pct": 1.02,
            "w_pct": 0.10, "h_pct": 0.06,
            "text": lbl, "align": "center",
            "color": BLUE_HEX, "bold": False, "size": 10
        })

    # Labels series en bout de ligne
    def y_to_pct(val):
        ax_y_min, ax_y_max = ax.get_ylim()
        return 1.0 - (val - ax_y_min) / (ax_y_max - ax_y_min)

    for name, values in series.items():
        is_vedette = (name == highlight)
        color_hex = ORANGE_HEX if is_vedette else TEXT_GREY_HEX
        overlays.append({
            "type": "series_right",
            "x_pct": (n - 0.5) / n + 0.01, "y_pct": y_to_pct(values[-1]) - 0.025,
            "w_pct": 0.18, "h_pct": 0.05,
            "text": name, "align": "left",
            "color": color_hex, "bold": is_vedette, "size": 11
        })

    save_png_and_overlays(fig, png_path, overlays)


def gen_dot(data, png_path, highlight=None):
    """Dot plot horizontal. PNG = points et lignes. JSON = labels categories + valeurs."""
    categories = data['categories']
    values = data['values']
    n = len(categories)

    fig, ax = plt.subplots(figsize=(10, max(3, n * 0.5)), dpi=200, facecolor='none')
    fig.patch.set_alpha(0)

    x_max = max(values) * 1.15

    for i, val in enumerate(values):
        cat = categories[i]
        is_vedette = (cat == highlight) if highlight else False
        color = ORANGE if is_vedette else BLUE
        # Ligne de fond
        ax.plot([0, x_max * 0.95], [n - 1 - i, n - 1 - i],
                color=LIGHT_GREY, linewidth=0.8, zorder=1)
        # Point
        ax.scatter([val], [n - 1 - i],
                   s=140 if is_vedette else 90, color=color, zorder=10)

    ax.set_xlim(-x_max * 0.15, x_max)
    ax.set_ylim(-0.5, n - 0.5)

    setup_clean_axes(ax)

    overlays = []

    # Labels categories a gauche + valeurs a droite
    for i, (cat, val) in enumerate(zip(categories, values)):
        is_vedette = (cat == highlight) if highlight else False
        color_hex = ORANGE_HEX if is_vedette else BLUE_HEX
        y_pct = (i + 0.5) / n - 0.025

        # Label categorie a gauche
        overlays.append({
            "type": "category_label",
            "x_pct": 0, "y_pct": y_pct,
            "w_pct": 0.20, "h_pct": 0.05,
            "text": cat, "align": "right",
            "color": BLUE_HEX, "bold": False, "size": 10
        })
        # Valeur a droite du point
        val_x_pct = 0.22 + (val / x_max) * 0.75
        overlays.append({
            "type": "value_label",
            "x_pct": val_x_pct + 0.01, "y_pct": y_pct,
            "w_pct": 0.08, "h_pct": 0.05,
            "text": str(val), "align": "left",
            "color": color_hex, "bold": is_vedette, "size": 10
        })

    save_png_and_overlays(fig, png_path, overlays)


def gen_bar(data, png_path, highlight=None, orientation='vertical'):
    """Bar chart. PNG = barres seules. JSON = labels categories + valeurs."""
    categories = data['categories']
    values = data['values']
    n = len(categories)

    if orientation == 'horizontal':
        fig, ax = plt.subplots(figsize=(10, max(3, n * 0.6)), dpi=200, facecolor='none')
        for i, val in enumerate(values):
            cat = categories[i]
            is_vedette = (cat == highlight) if highlight else False
            color = ORANGE if is_vedette else BLUE
            ax.barh(n - 1 - i, val, color=color, height=0.65)
        ax.set_xlim(0, max(values) * 1.15)
        ax.set_ylim(-0.5, n - 0.5)
    else:
        fig, ax = plt.subplots(figsize=(10, 4.5), dpi=200, facecolor='none')
        for i, val in enumerate(values):
            cat = categories[i]
            is_vedette = (cat == highlight) if highlight else False
            color = ORANGE if is_vedette else BLUE
            ax.bar(i, val, color=color, width=0.65)
        ax.set_ylim(0, max(values) * 1.15)
        ax.set_xlim(-0.5, n - 0.5)

    fig.patch.set_alpha(0)
    setup_clean_axes(ax)

    overlays = []
    for i, (cat, val) in enumerate(zip(categories, values)):
        is_vedette = (cat == highlight) if highlight else False
        color_hex = ORANGE_HEX if is_vedette else BLUE_HEX

        if orientation == 'horizontal':
            y_pct = (i + 0.5) / n - 0.025
            # label cat a gauche
            overlays.append({
                "type": "category_label",
                "x_pct": 0, "y_pct": y_pct,
                "w_pct": 0.18, "h_pct": 0.05,
                "text": cat, "align": "right",
                "color": BLUE_HEX, "bold": False, "size": 11
            })
            # valeur en bout de barre
            val_x = 0.20 + (val / (max(values) * 1.15)) * 0.78
            overlays.append({
                "type": "value_label",
                "x_pct": val_x + 0.01, "y_pct": y_pct,
                "w_pct": 0.08, "h_pct": 0.05,
                "text": str(val), "align": "left",
                "color": color_hex, "bold": is_vedette, "size": 11
            })
        else:
            x_pct = (i + 0.5) / n
            # label cat sous l'axe
            overlays.append({
                "type": "category_label",
                "x_pct": x_pct - 0.08, "y_pct": 1.02,
                "w_pct": 0.16, "h_pct": 0.05,
                "text": cat, "align": "center",
                "color": BLUE_HEX, "bold": False, "size": 10
            })
            # valeur au-dessus de la barre
            y_pct = 1.0 - val / (max(values) * 1.15) - 0.05
            overlays.append({
                "type": "value_label",
                "x_pct": x_pct - 0.08, "y_pct": y_pct,
                "w_pct": 0.16, "h_pct": 0.05,
                "text": str(val), "align": "center",
                "color": color_hex, "bold": is_vedette, "size": 11
            })

    save_png_and_overlays(fig, png_path, overlays)


def gen_dumbbell(data, png_path, highlight=None):
    """Dumbbell horizontal : 2 valeurs par categorie, reliees par une ligne.
    ATTENTION : a eviter si une des deux valeurs est ~0 (cf CLAUDE.md §4.10).
    PNG = points et lignes. JSON = labels categories + valeurs + labels series."""
    categories = data['categories']
    series_names = list(data['series'].keys())  # 2 series attendues
    s1, s2 = series_names[0], series_names[1]
    vals1 = data['series'][s1]
    vals2 = data['series'][s2]
    n = len(categories)

    # Garde-fou : warning si valeurs degenerees
    for i, (v1, v2) in enumerate(zip(vals1, vals2)):
        if v1 == 0 or v2 == 0:
            print(f"  WARN  Categorie '{categories[i]}': valeur 0 detectee ({s1}={v1}, {s2}={v2})")
            print(f"        Dumbbell sera degenere sur cette categorie. Voir CLAUDE.md §4.10.")

    fig, ax = plt.subplots(figsize=(10, max(3, n * 0.6)), dpi=200, facecolor='none')
    fig.patch.set_alpha(0)

    max_val = max(max(vals1), max(vals2)) * 1.15

    for i, (v1, v2) in enumerate(zip(vals1, vals2)):
        y = n - 1 - i
        # Ligne reliant les 2 points
        ax.plot([v1, v2], [y, y], color=LIGHT_GREY, linewidth=2, zorder=1)
        # Point s1
        c1 = ORANGE if (highlight == s1) else BLUE
        ax.scatter([v1], [y], s=120, color=c1, zorder=10)
        # Point s2
        c2 = ORANGE if (highlight == s2) else BLUE
        ax.scatter([v2], [y], s=120, color=c2, zorder=10)

    ax.set_xlim(-max_val * 0.15, max_val)
    ax.set_ylim(-0.5, n - 0.5)
    setup_clean_axes(ax)

    overlays = []
    # Labels categories a gauche
    for i, cat in enumerate(categories):
        y_pct = (i + 0.5) / n - 0.025
        overlays.append({
            "type": "category_label",
            "x_pct": 0, "y_pct": y_pct,
            "w_pct": 0.20, "h_pct": 0.05,
            "text": cat, "align": "right",
            "color": BLUE_HEX, "bold": False, "size": 10
        })

    save_png_and_overlays(fig, png_path, overlays)


def gen_heatmap(data, png_path):
    """Heatmap avec degrade UNE seule couleur. PNG = cellules colorees."""
    rows = data['rows']
    cols = data['cols']
    values = data['values']

    fig, ax = plt.subplots(figsize=(max(6, len(cols) * 1.2), max(4, len(rows) * 0.6)),
                           dpi=200, facecolor='none')
    fig.patch.set_alpha(0)

    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('empirik_blue', ['#FFFFFF', BLUE], N=256)

    ax.imshow(values, cmap=cmap, aspect='auto')
    setup_clean_axes(ax)

    # Reactivate ticks pour positionner les overlays correctement
    ax.set_xticks(range(len(cols)))
    ax.set_yticks(range(len(rows)))
    ax.set_xticklabels([''] * len(cols))
    ax.set_yticklabels([''] * len(rows))

    overlays = []
    n_rows, n_cols = len(rows), len(cols)
    max_val = max(max(row) for row in values)

    # Labels colonnes en haut
    for j, col in enumerate(cols):
        x_pct = (j + 0.5) / n_cols
        overlays.append({
            "type": "col_label",
            "x_pct": x_pct - 0.08, "y_pct": -0.06,
            "w_pct": 0.16, "h_pct": 0.05,
            "text": col, "align": "center",
            "color": BLUE_HEX, "bold": False, "size": 10
        })

    # Labels lignes a gauche
    for i, row in enumerate(rows):
        y_pct = (i + 0.5) / n_rows - 0.025
        overlays.append({
            "type": "row_label",
            "x_pct": -0.15, "y_pct": y_pct,
            "w_pct": 0.13, "h_pct": 0.05,
            "text": row, "align": "right",
            "color": BLUE_HEX, "bold": False, "size": 10
        })

    # Valeurs dans chaque cellule
    for i in range(n_rows):
        for j in range(n_cols):
            v = values[i][j]
            x_pct = (j + 0.5) / n_cols
            y_pct = (i + 0.5) / n_rows
            text_color = "FFFFFF" if v > max_val * 0.6 else BLUE_HEX
            overlays.append({
                "type": "cell_value",
                "x_pct": x_pct - 0.05, "y_pct": y_pct - 0.025,
                "w_pct": 0.10, "h_pct": 0.05,
                "text": str(v), "align": "center",
                "color": text_color, "bold": False, "size": 10
            })

    save_png_and_overlays(fig, png_path, overlays)


def gen_waterfall(data, png_path):
    """Waterfall chart. PNG = barres. JSON = labels + valeurs."""
    labels = data['labels']
    values = data['values']
    is_total_flags = data.get('is_total', [False] * len(labels))
    n = len(labels)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=200, facecolor='none')
    fig.patch.set_alpha(0)

    cumul = 0
    bar_tops = []  # pour positionner les overlays au-dessus
    for i, (lbl, v, is_tot) in enumerate(zip(labels, values, is_total_flags)):
        if is_tot:
            color = BLUE
            ax.bar(i, v, color=color, width=0.6)
            bar_tops.append(v)
            cumul = v
        else:
            color = ORANGE if v > 0 else GREY
            bottom = cumul if v > 0 else cumul + v
            ax.bar(i, abs(v), bottom=bottom, color=color, width=0.6)
            bar_tops.append(bottom + abs(v))
            cumul += v

    max_y = max(bar_tops) * 1.15
    ax.set_ylim(0, max_y)
    ax.set_xlim(-0.5, n - 0.5)
    setup_clean_axes(ax)

    overlays = []
    for i, (lbl, v, is_tot, top) in enumerate(zip(labels, values, is_total_flags, bar_tops)):
        x_pct = (i + 0.5) / n
        # Label en dessous
        overlays.append({
            "type": "category_label",
            "x_pct": x_pct - 0.08, "y_pct": 1.02,
            "w_pct": 0.16, "h_pct": 0.05,
            "text": lbl, "align": "center",
            "color": BLUE_HEX, "bold": False, "size": 10
        })
        # Valeur au-dessus
        color_hex = BLUE_HEX if is_tot else (ORANGE_HEX if v > 0 else GREY_HEX)
        sign = '+' if (v > 0 and not is_tot) else ''
        y_pct = 1.0 - top / max_y - 0.05
        overlays.append({
            "type": "value_label",
            "x_pct": x_pct - 0.08, "y_pct": y_pct,
            "w_pct": 0.16, "h_pct": 0.05,
            "text": f"{sign}{v}", "align": "center",
            "color": color_hex, "bold": True, "size": 11
        })

    save_png_and_overlays(fig, png_path, overlays)


# === CLI =================================================================

GENERATORS = {
    'slope': gen_slope,
    'line': gen_line,
    'dot': gen_dot,
    'bar': gen_bar,
    'dumbbell': gen_dumbbell,
    'heatmap': gen_heatmap,
    'waterfall': gen_waterfall,
}


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--type', required=True, choices=list(GENERATORS.keys()),
        help="Type de graphique a generer")
    parser.add_argument('--data', required=True,
        help="Fichier JSON contenant les donnees du graphe")
    parser.add_argument('--output', required=True,
        help="Chemin de sortie du PNG (ex : assets/charts/slope-evolution.png)")
    parser.add_argument('--highlight', default=None,
        help="Nom de la serie/categorie a mettre en orange Empirik (vedette)")
    parser.add_argument('--orientation', default='vertical', choices=['vertical', 'horizontal'],
        help="Orientation des barres (pour --type bar uniquement)")
    args = parser.parse_args()

    with open(args.data, encoding='utf-8') as f:
        data = json.load(f)

    fn = GENERATORS[args.type]
    if args.type == 'bar':
        fn(data, args.output, highlight=args.highlight, orientation=args.orientation)
    elif args.type in ('slope', 'line', 'dot', 'dumbbell'):
        fn(data, args.output, highlight=args.highlight)
    else:
        fn(data, args.output)

    print(f"\nIntegration PptxGenJS :")
    print(f'  slide.addImage({{ path: "{args.output}", x: 0.5, y: 1.4, w: 9, h: 3.6 }});')
    print(f'  // Lire {Path(args.output).stem}.overlays.json et placer chaque texte via addText()')


if __name__ == '__main__':
    main()

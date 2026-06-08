"""Genere les images de cover/closing pour la pres Velura, sans IA externe.

Style scandinave epure : palette beige/blanc/bois clair, formes geometriques
douces, evocation editoriale e-commerce deco.
"""

from PIL import Image, ImageDraw, ImageFilter
import os
import math
import random

random.seed(42)

W, H = 1408, 1600  # portrait pour cover gauche

# Palettes Velura scandinave
CREAM = (245, 240, 232)
BEIGE = (228, 215, 196)
WOOD_LIGHT = (210, 188, 158)
WOOD_MID = (175, 145, 110)
WARM_GREY = (190, 180, 170)
SAGE = (175, 185, 165)
TERRACOTTA = (200, 130, 100)
WHITE = (252, 250, 246)


def add_grain(img, intensity=8):
    pixels = img.load()
    w, h = img.size
    for _ in range(w * h // 20):
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)
        r, g, b = pixels[x, y][:3]
        delta = random.randint(-intensity, intensity)
        pixels[x, y] = (
            max(0, min(255, r + delta)),
            max(0, min(255, g + delta)),
            max(0, min(255, b + delta)),
        )
    return img


def cover_velura(output):
    """Cover style scandinave: fond beige, courbe sage, formes geometriques douces."""
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # Grand cercle terracotta en haut a droite (soleil doux)
    cx, cy, r = W * 0.78, H * 0.18, 220
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TERRACOTTA + (0,))
    # Halo
    for i in range(40, 0, -2):
        alpha = int(40 - i)
        col = tuple(
            int(TERRACOTTA[k] * (alpha / 50) + CREAM[k] * (1 - alpha / 50))
            for k in range(3)
        )
        d.ellipse([cx - r - i, cy - r - i, cx + r + i, cy + r + i], outline=col)

    # Cercle principal
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TERRACOTTA)

    # Bande horizontale wood-light (etagere/table)
    band_y = int(H * 0.55)
    d.rectangle([0, band_y, W, band_y + 8], fill=WOOD_MID)
    d.rectangle([0, band_y + 8, W, H], fill=WOOD_LIGHT)

    # Pots / vases stylises en bas (rectangles arrondis)
    pots = [
        (W * 0.15, band_y, 180, 220, SAGE),
        (W * 0.40, band_y, 140, 280, BEIGE),
        (W * 0.62, band_y, 200, 180, WARM_GREY),
        (W * 0.82, band_y, 110, 240, WOOD_MID),
    ]
    for px, py, pw, ph, col in pots:
        d.rounded_rectangle(
            [px, py - ph, px + pw, py], radius=20, fill=col
        )

    # Lignes verticales fines (texture brins/tiges) sortant des pots
    for px, py, pw, ph, col in pots[:3]:
        for i in range(3):
            sx = px + pw * 0.3 + i * pw * 0.15
            d.line(
                [(sx, py - ph), (sx + (i - 1) * 4, py - ph - 80 - i * 20)],
                fill=tuple(max(0, c - 30) for c in col),
                width=3,
            )

    # Tres legere grille de carres jaune-creme en bas (motif decoratif Empirik)
    for i in range(8):
        sx = 30 + i * 12
        sy = H - 60
        d.rectangle([sx, sy, sx + 8, sy + 8], fill=(252, 192, 45))

    img = add_grain(img, intensity=6)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.8))
    img.save(output, "PNG", optimize=True)
    print(f"OK cover -> {output} ({os.path.getsize(output)} bytes)")


def closing_velura(output):
    """Closing : ambiance board apaisee, palette claire, courbe verte stylisee."""
    Wc, Hc = 1408, 768
    img = Image.new("RGB", (Wc, Hc), CREAM)
    d = ImageDraw.Draw(img)

    # Fond degrade tres doux beige -> blanc cassé
    for y in range(Hc):
        ratio = y / Hc
        col = tuple(
            int(CREAM[k] * (1 - ratio * 0.3) + WHITE[k] * ratio * 0.3) for k in range(3)
        )
        d.line([(0, y), (Wc, y)], fill=col)

    # Grande fenêtre rectangulaire à droite (lumière naturelle)
    fx1, fy1, fx2, fy2 = int(Wc * 0.62), int(Hc * 0.08), int(Wc * 0.94), int(Hc * 0.62)
    # Cadre bois
    d.rounded_rectangle([fx1 - 8, fy1 - 8, fx2 + 8, fy2 + 8], radius=4, fill=WOOD_MID)
    # Vitre claire (gradient)
    for y in range(fy1, fy2):
        ratio = (y - fy1) / (fy2 - fy1)
        col = tuple(
            int(WHITE[k] * (1 - ratio * 0.15) + WOOD_LIGHT[k] * ratio * 0.15)
            for k in range(3)
        )
        d.line([(fx1, y), (fx2, y)], fill=col)
    # Croix de la fenetre
    midx = (fx1 + fx2) // 2
    midy = (fy1 + fy2) // 2
    d.line([(midx, fy1), (midx, fy2)], fill=WOOD_MID, width=4)
    d.line([(fx1, midy), (fx2, midy)], fill=WOOD_MID, width=4)

    # Table en bois clair en bas
    table_y = int(Hc * 0.68)
    d.rectangle([0, table_y, Wc, table_y + 4], fill=WOOD_MID)
    d.rectangle([0, table_y + 4, Wc, Hc], fill=WOOD_LIGHT)

    # MacBook stylise au centre
    laptop_w, laptop_h = 320, 180
    lx = (Wc - laptop_w) // 2
    ly = table_y - laptop_h - 10
    # Ecran
    d.rounded_rectangle(
        [lx, ly, lx + laptop_w, ly + laptop_h], radius=8, fill=(40, 50, 65)
    )
    # Bord
    d.rounded_rectangle(
        [lx + 6, ly + 6, lx + laptop_w - 6, ly + laptop_h - 6], radius=4, fill=(20, 28, 38)
    )
    # Courbe verte montante (croissance) dans l'ecran
    pts = []
    for i in range(11):
        x = lx + 20 + i * (laptop_w - 40) / 10
        # Croissance accélérée vers le haut
        progress = (i / 10) ** 1.6
        y = ly + laptop_h - 30 - progress * (laptop_h - 60)
        pts.append((x, y))
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=(80, 180, 120), width=4)
    for x, y in pts[-3:]:
        d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(80, 180, 120))

    # Trackpad/base
    d.rectangle(
        [lx - 10, ly + laptop_h, lx + laptop_w + 10, ly + laptop_h + 8],
        fill=(180, 180, 180),
    )

    # Petite tasse a cafe a droite du laptop
    cup_x = lx + laptop_w + 80
    cup_y = table_y - 50
    d.ellipse([cup_x, cup_y, cup_x + 50, cup_y + 60], fill=WHITE)
    d.ellipse([cup_x + 4, cup_y + 4, cup_x + 46, cup_y + 56], fill=(110, 80, 55))

    # Plante stylisee a gauche
    pot_x = lx - 200
    pot_y = table_y - 80
    d.rounded_rectangle(
        [pot_x, pot_y, pot_x + 80, pot_y + 80], radius=8, fill=SAGE
    )
    for i in range(5):
        d.line(
            [
                (pot_x + 40 + (i - 2) * 8, pot_y),
                (pot_x + 40 + (i - 2) * 16, pot_y - 80 - i * 5),
            ],
            fill=(110, 130, 100),
            width=4,
        )

    img = add_grain(img, intensity=5)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    img.save(output, "PNG", optimize=True)
    print(f"OK closing -> {output} ({os.path.getsize(output)} bytes)")


def velura_wordmark(output):
    """Logo wordmark Velura simple en serif."""
    from PIL import ImageFont
    img = Image.new("RGBA", (600, 160), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    # Try serif fonts
    font = None
    for f in [
        "C:/Windows/Fonts/georgia.ttf",
        "C:/Windows/Fonts/times.ttf",
        "C:/Windows/Fonts/timesbd.ttf",
    ]:
        if os.path.exists(f):
            try:
                font = ImageFont.truetype(f, 90)
                break
            except Exception:
                pass
    if font is None:
        font = ImageFont.load_default()
    text = "VELURA"
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (600 - tw) // 2 - bbox[0]
    y = (160 - th) // 2 - bbox[1]
    d.text((x, y), text, fill=(40, 56, 86, 255), font=font)
    # Petite ligne sous le mot
    d.rectangle([(600 - tw) // 2, y + th + 8, (600 - tw) // 2 + tw, y + th + 12], fill=(200, 130, 100, 255))
    img.save(output, "PNG", optimize=True)
    print(f"OK velura logo -> {output} ({os.path.getsize(output)} bytes)")


if __name__ == "__main__":
    cover_velura("assets/cover-velura.png")
    closing_velura("assets/closing-velura.png")
    velura_wordmark("assets/logos/velura.png")

#!/usr/bin/env python3
"""
generate_image.py — Génération d'images pour slides Empirik via Gemini

Modèles disponibles :
  - gemini-3-pro-image-preview     : qualité max, infographies pro (défaut)
  - gemini-3.1-flash-image-preview : production rapide, haut volume
  - gemini-2.5-flash-image         : workflows créatifs rapides

Usage :
  python scripts/generate_image.py --type concept --prompt "data funnel showing user journey" --output assets/slide3-visual.png
  python scripts/generate_image.py --type cover --output assets/cover.png
  python scripts/generate_image.py --prompt "custom prompt here" --output assets/custom.png --model gemini-3.1-flash-image-preview
"""

import argparse
import base64
import os
import sys
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Erreur : installe google-genai d'abord :")
    print("  pip install google-genai")
    sys.exit(1)

# --- Configuration ---
# La clé API est lue depuis clé-api-gemini.md à la racine du projet (gitignored).
# Ce fichier n'est JAMAIS pushé sur GitHub. Chaque utilisateur met sa propre clé.
# Voir SETUP.html § 3 étape 7 pour les instructions.

def _load_api_key():
    """Charge la clé Gemini depuis clé-api-gemini.md à la racine du projet."""
    import re
    from pathlib import Path
    key_file = Path(__file__).resolve().parent.parent / "clé-api-gemini.md"
    if not key_file.exists():
        print("Erreur : clé-api-gemini.md introuvable à la racine du projet.")
        print("Crée ce fichier avec ta clé Gemini (voir SETUP.html § 3 étape 7).")
        print("Tu peux en créer une sur https://aistudio.google.com/apikey")
        sys.exit(1)
    content = key_file.read_text(encoding='utf-8').strip()
    # Pattern Google API key (AIza...)
    m = re.search(r'(AIza[A-Za-z0-9_-]{30,})', content)
    if m:
        return m.group(1)
    # Fallback : première ligne non-vide non-commentaire
    for line in content.splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            return line
    print("Erreur : aucune clé valide trouvée dans clé-api-gemini.md")
    sys.exit(1)

API_KEY = _load_api_key()

MODELS = {
    "pro": "gemini-3-pro-image-preview",
    "flash": "gemini-3.1-flash-image-preview",
    "nano": "gemini-2.5-flash-image",
}
DEFAULT_MODEL = "pro"

# Prompts de base par type d'asset (depuis DESIGN_EMPIRIK.md)
ASSET_PROMPTS = {
    "cover": (
        "Abstract dark blue professional cover visual for a corporate presentation. "
        "Geometric data streams and network nodes. Deep #0A3856 navy background. "
        "Sharp orange accent points and lines #E9540D. "
        "Editorial poster style, clean and authoritative. "
        "25% clear negative space on the right for text overlay. "
        "16:9 format, 2K resolution, no text, no logo."
    ),
    "section": (
        "Minimal dark blue section divider background for a corporate slide. "
        "Single bold orange geometric element. "
        "Clean negative space for large text overlay. "
        "#0A3856 dominant, #E9540D accent. "
        "Professional, no text, no logo, 16:9."
    ),
    "concept": (
        "Clean concept visualization diagram for a business presentation slide. "
        "Geometric shapes, clean arrows, flow illustration. "
        "#0A3856 blue and #E9540D orange on white background. "
        "Data flow or process concept, editorial style. "
        "No text labels, no logo, 16:9."
    ),
    "comparison": (
        "Side-by-side comparison visual for a slide. "
        "Left panel dark #0A3856 navy, right panel warm #E9540D orange. "
        "Clean vertical dividing line. Professional corporate style. "
        "No text, no logo, 16:9."
    ),
    "data-backdrop": (
        "Subtle data visualization backdrop for a KPI slide. "
        "Faint grid lines and chart outlines in #0A3856 palette. "
        "Very low contrast, professional background. "
        "No visible text, no logo, 16:9."
    ),
    "workflow": (
        "Clean workflow diagram background for a slide. "
        "Connected nodes with arrows, left-to-right reading flow. "
        "#0A3856 navy and #E9540D orange color scheme. "
        "Minimal design, geometric shapes. "
        "No text labels, no logo, 16:9."
    ),
    "closing": (
        "Powerful closing visual for a corporate presentation. "
        "Dark #0A3856 background, strong central #E9540D orange geometric element. "
        "Editorial poster energy, professional confidence. "
        "25-30% clear space for text overlay. "
        "No text, no logo, 16:9."
    ),
}

EMPIRIK_STYLE_SUFFIX = (
    " Style: professional corporate, data-driven, editorial. "
    "Color palette: #0A3856 navy, #E9540D orange, #FCC02D gold, white. "
    "Poppins-compatible clean geometric aesthetic. "
    "No stock photography, no clipart, no 3D effects."
)


def generate_image(prompt: str, output_path: str, model_key: str = DEFAULT_MODEL) -> None:
    model_id = MODELS.get(model_key, MODELS[DEFAULT_MODEL])
    print(f"Modele : {model_id}")
    print(f"Output : {output_path}")
    print(f"Prompt : {prompt[:80]}...")

    client = genai.Client(api_key=API_KEY)

    full_prompt = prompt + EMPIRIK_STYLE_SUFFIX

    response = client.models.generate_content(
        model=model_id,
        contents=full_prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        ),
    )

    # Extraire l'image de la réponse
    image_data = None
    for part in response.candidates[0].content.parts:
        if hasattr(part, "inline_data") and part.inline_data is not None:
            image_data = part.inline_data.data
            break

    if image_data is None:
        print("Erreur : aucune image dans la réponse.")
        print("Réponse brute :", response)
        sys.exit(1)

    # Sauvegarder
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "wb") as f:
        f.write(base64.b64decode(image_data) if isinstance(image_data, str) else image_data)

    print(f"Image sauvegardee : {output}")


def main():
    parser = argparse.ArgumentParser(description="Generateur d'images Empirik via Gemini")
    parser.add_argument(
        "--type",
        choices=list(ASSET_PROMPTS.keys()),
        help="Type d'asset visuel (utilise le prompt predefined)",
    )
    parser.add_argument(
        "--prompt",
        type=str,
        help="Prompt personnalise (remplace ou complète --type)",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Chemin de sortie de l'image (ex: assets/cover.png)",
    )
    parser.add_argument(
        "--model",
        choices=list(MODELS.keys()),
        default=DEFAULT_MODEL,
        help=f"Modele Gemini a utiliser (defaut: {DEFAULT_MODEL})",
    )

    args = parser.parse_args()

    if not args.type and not args.prompt:
        print("Erreur : fournir --type ou --prompt")
        parser.print_help()
        sys.exit(1)

    # Construire le prompt final
    if args.type and args.prompt:
        # Combiner le prompt de base du type + le prompt custom
        final_prompt = ASSET_PROMPTS[args.type] + " Additional context: " + args.prompt
    elif args.type:
        final_prompt = ASSET_PROMPTS[args.type]
    else:
        final_prompt = args.prompt

    generate_image(final_prompt, args.output, args.model)


if __name__ == "__main__":
    main()

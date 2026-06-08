# DESIGN_EMPIRIK.md — Guide de génération d'images pour slides Empirik

> Inspiré du format PPT-Design-Prompt. Ce fichier est passé en contexte à chaque génération d'image avec Gemini.
> Objectif : produire des visuels d'assets pour slides — PAS des slides complètes, PAS des captures d'écran.

---

## Philosophie centrale

**Une image = une thèse.**
L'image doit communiquer l'idée principale de la slide en moins d'une seconde.
Style éditorial professionnel, pas de photo stock, pas d'illustration SaaS générique.

---

## Charte graphique Empirik

### Palette officielle
- **Bleu principal** : #0A3856 — couleur dominante, fond sombre, éléments structurants
- **Orange accent** : #E9540D — points de tension, CTA, éléments à retenir
- **Jaune accent** : #FCC02D — highlights, icônes secondaires, éclairage chaud
- **Blanc** : #FFFFFF — espace négatif, respiration, fond de slides

### Typographie
- Police : Poppins (sans-serif géométrique, moderne, professionnel)
- Le texte dans les images doit être **minimal** : pas de titre, pas de bullets dans l'image
- Maximum : un court label ou un marqueur de section

### Style visuel
- Ambiance : data-driven, sérieux mais accessible, "better with data"
- Pas de dégradés complexes
- Préférer les formes géométriques nettes (rectangles, cercles, lignes)
- Ombres légères, coins arrondis (8px équivalent)
- **JAMAIS** de logo Empirik dans les images

---

## Zone de sécurité texte

- Conserver **25 à 35 % d'espace vide** pour permettre la superposition du texte de la slide
- Contenu critique dans les **80 % centraux** du cadre (survie au recadrage et projection)
- Prévoir de l'espace à gauche ou en bas pour les titres et bullets PptxGenJS

---

## 7 types d'assets visuels

### 1. Cover / Opening Hero
**Usage** : slide de titre, première impression
**Composition** : scène conceptuelle forte, fond bleu #0A3856 dominant, touche orange #E9540D
**Prompt type** : `"Abstract dark blue professional cover visual, geometric data streams, deep #0A3856 background, orange accent points #E9540D, editorial poster style, 16:9, no text"`

### 2. Section Divider
**Usage** : slide de transition entre parties
**Composition** : fond plein #0A3856, forme graphique simple, bande ou diagonale orange
**Prompt type** : `"Minimal dark blue section divider, single orange geometric element, clean negative space, professional, 16:9, no text"`

### 3. Concept Visualization
**Usage** : expliquer un concept abstrait (funnel, cycle, IA, données)
**Composition** : schéma épuré, flèches nettes, icônes géométriques sur fond blanc ou bleu clair
**Règle** : montrer le concept avec des formes, pas de mots dans l'image
**Prompt type** : `"Clean concept diagram visualization, geometric shapes and arrows, #0A3856 blue and #E9540D orange on white background, data flow or process illustration, no text labels, 16:9"`

### 4. Comparison Plate
**Usage** : avant/après, option A vs B, deux colonnes
**Composition** : séparation visuelle nette, couleurs opposées (bleu / orange-jaune)
**Prompt type** : `"Side-by-side comparison visual, left panel dark #0A3856, right panel warm orange #E9540D, clean dividing line, professional, no text, 16:9"`

### 5. Data Backdrop
**Usage** : fond pour slides de chiffres clés, KPIs, métriques
**Composition** : graphes, courbes, grilles en filigrane, très épuré
**Règle** : l'image doit rester en arrière-plan — contraste faible, pas de formes agressives
**Prompt type** : `"Subtle data visualization backdrop, faint grid lines and chart outlines, #0A3856 palette, very low contrast, professional background for data slides, 16:9, no visible text"`

### 6. System / Workflow Plate
**Usage** : process en étapes, architecture, schéma technique simplifié
**Composition** : noeuds reliés par flèches, lecture de gauche à droite, palette Empirik
**Prompt type** : `"Clean workflow diagram, connected nodes with arrows, left-to-right flow, #0A3856 and #E9540D colors, minimal design, no text labels, 16:9"`

### 7. Closing Poster
**Usage** : slide de conclusion, CTA, call-to-action final
**Composition** : impactant, bleu foncé dominant, élément orange fort en centre
**Prompt type** : `"Powerful closing visual, dark #0A3856 background, strong central #E9540D orange element, editorial poster energy, professional confidence, 16:9, no text"`

---

## Spécifications techniques

| Paramètre | Valeur |
|-----------|--------|
| Format | 16:9 horizontal |
| Résolution | 2K minimum (via Gemini Pro) |
| Modèle recommandé | `gemini-3-pro-image-preview` |
| Modèle rapide | `gemini-3.1-flash-image-preview` |
| Style global | éditorial, professionnel, data-driven |

---

## Ce qu'il NE FAUT PAS générer

- Texte intégré dans l'image (titres, bullets, chiffres) — c'est PptxGenJS qui s'en charge
- Photos réalistes de personnes
- Logo Empirik
- Effets 3D tape-à-l'oeil
- Dégradés arc-en-ciel ou palettes non conformes
- Icônes clipart ou style flat design générique

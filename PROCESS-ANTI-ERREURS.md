# PROCESS ANTI-ERREURS — Création de slides Empirik
> **Ce fichier est OBLIGATOIRE à lire AVANT toute génération de slides.**
> Il consolide les règles non-évidentes qui ont déjà causé des erreurs.
> Si tu ne respectes pas une règle ici, le livrable est à refaire.

---

## ⛔ PRE-FLIGHT CHECKLIST — À COCHER MENTALEMENT AVANT LA 1RE LIGNE DE CODE

Avant d'écrire le moindre script PptxGenJS, tu DOIS pouvoir répondre OUI à toutes ces questions :

```
[ ] J'ai lu CLAUDE.md + PROCESS-ANTI-ERREURS.md + MASTER-CHECKLIST.md + guide_design_slides.md + guide-slides-data-storytelling.md + guide_storytelling_presentations.md + dataviz-guide.md + DESIGN_EMPIRIK.md (les 8 guides, dans cet ordre)
[ ] J'ai produit le rapport de lecture en ACTIONS CONCRÈTES (CLAUDE.md §0 étape 1), pas en bullets théoriques
[ ] J'ai listé TOUTES les marques/outils/sites mentionnés et planifié leurs LOGOS officiels
[ ] J'ai identifié les chiffres clés du brief / PDF source à intégrer SANS exception
[ ] J'ai planifié les tableaux source en intégralité (pas de troncage)
[ ] J'ai noté les "À vérifier" et "À confirmer" pour les signaler explicitement au client
[ ] J'ai détecté si le brouillon est à risque "Pathos faible" (data-driven, zéro personnage humain) et planifié la compensation
[ ] J'ai produit les 6 artifacts de l'étape 4 (couverture brouillon, avocat du diable, slides récap, voies dataviz, slides question, plan émotionnel Duarte)
[ ] Si pas de plan validé par user → STOP, demander validation (sauf instruction explicite "skip")
```

---

## 🚨 MÉTA-RÈGLE — Anti-angle-mort de checklist

> **Une checklist incomplète crée un angle mort qui devient structurel.** C'est le bug de fond du process : quand un référentiel comme MASTER-CHECKLIST est posé comme "source de vérité opérationnelle", **tout ce qui n'y est PAS devient invisible**. Et tout ce qui est dans les guides mais absent de la checklist disparaît silencieusement à chaque génération.

**Exemple historique** : les principes Duarte (S.T.A.R., humanisation, sparkline, nouvelle félicité, Pathos) étaient dans `guide_storytelling_presentations.md` mais absents de MASTER-CHECKLIST. Résultat : la pres "Angora vs Sphinx v1" a obtenu 100% sur la checklist factuelle et 55% sur Duarte. La rigueur procédurale s'est retournée contre la qualité du livrable.

**Action obligatoire avant CHAQUE génération** : faire un audit explicite à voix mentale (et si possible documenté dans le rapport de lecture) :

```
Pour chaque guide externe (guide_design_slides, guide-slides-data-storytelling,
guide_storytelling_presentations, dataviz-guide, DESIGN_EMPIRIK) :
  → Liste les règles/principes/concepts importants du guide
  → Pour CHAQUE règle, vérifier : est-elle dans MASTER-CHECKLIST ?
  → Si NON et que la règle est importante pour cette pres → l'AJOUTER
    temporairement à mon rapport de lecture comme action concrète à appliquer
  → Si NON et que la règle n'est pas pertinente pour cette pres → la documenter
    comme dérogation consciente
```

**Pourquoi cette règle est ici et pas implicite** : le réflexe par défaut d'un Claude rigoureux est d'appliquer parfaitement la checklist qu'on lui donne. Sans cette méta-règle qui force à challenger l'exhaustivité de la checklist, l'angle mort est garanti structurellement.

> Si tu repères pendant la génération une règle importante d'un guide externe qui n'est pas dans MASTER-CHECKLIST → **propose à l'utilisateur de l'y ajouter en fin de pres**. C'est ainsi que le process s'améliore : chaque génération est une opportunité de détecter un angle mort résiduel.

---

## 🔥 LES 7 ERREURS RÉCURRENTES À NE PLUS JAMAIS COMMETTRE

### Erreur #1 — Sur-titres en MAJUSCULES avec charSpacing

**❌ INTERDIT (a déjà causé une refonte) :**
```js
slide.addText(section.toUpperCase(), {
  fontFace: "Poppins", fontSize: 12, color: ORANGE,
  charSpacing: 4,  // ⛔ JAMAIS
});
```

**✅ BON :**
```js
slide.addText(section, {                       // ← Casse normale, pas de toUpperCase
  fontFace: "Poppins ExtraLight",              // ← Police explicite ExtraLight
  fontSize: 12, color: ORANGE,
  // ← Pas de charSpacing
});
```

Exemple de bon sur-titre : `"Phase 1 · Présence dans les LLMs"` (pas `"PHASE 1 · PRÉSENCE DANS LES LLMS"`).

### Erreur #2 — Titre principal qui rend en Regular au lieu de SemiBold

**❌ INTERDIT — `fontWeight` est silencieusement ignoré par PptxGenJS :**
```js
slide.addText(title, {
  fontFace: "Poppins", fontSize: 22, color: BLUE,
  fontWeight: 600,    // ⛔ N'EXISTE PAS dans PptxGenJS — rend en Regular
  bold: false,
});
```

**✅ BON — utiliser le nom de police variant :**
```js
slide.addText(title, {
  fontFace: "Poppins SemiBold",  // ← Le nom de la police inclut le weight
  fontSize: 22, color: BLUE,
  bold: false,                    // ← Pas de bold: true (qui ferait Bold, pas SemiBold)
});
```

Idem pour Bold (chiffres clés, slide de cover) : `fontFace: "Poppins Bold"`.

### Erreur #3 — Texte ou chiffre en JAUNE (#FCC02D) sur fond blanc

**❌ INTERDIT — contraste insuffisant, illisible :**
```js
slide.addText("À vérifier", { color: YELLOW, ... });  // ⛔ sur fond blanc
slide.addText("93,8%", { color: YELLOW, ... });        // ⛔
slide.addText("Haute", { color: YELLOW, ... });        // ⛔ (label de priorité)
```

**✅ BON — utiliser le jaune SEULEMENT en accent décoratif (barres, fonds, icônes), jamais comme couleur de texte sur blanc :**
- Texte sur blanc → BLUE (#0A3856) ou ORANGE (#E9540D)
- Si label "warning" → fond ORANGE/CREAM + texte BLUE/WHITE
- Si chiffre clé → ORANGE (jamais YELLOW)

Le jaune est OK :
- En accent de bord supérieur d'une carte
- En fond pour un badge avec texte BLUE par-dessus
- En icône décorative
- Comme couleur de barre de séparation

#### Corollaire : contraste stratégique (UN seul élément ressort)

Au-delà du contraste de lisibilité, il faut un **contraste sémantique** : sur un graphique ou une visualisation, **un seul élément doit attirer l'œil**.

- **Élément vedette** (client, donnée à montrer, perte, pic, cible) → **ORANGE Empirik `#E9540D`**
- **Tout le reste** (concurrents, contexte, baseline, autres catégories) → **gris `#B0B0B0`** ou bleu Empirik atténué

**Anti-pattern fréquent** : palette multicolore par défaut sur les graphiques (orange + jaune + bleu + vert sans rôle narratif) → aucun élément ne ressort, le message est dilué.

**Test rapide** : avant de coder le graphique, formuler en une phrase ce que l'audience doit voir en 2 secondes. C'est ça, et ça seul, qui passe en orange. Voir `CLAUDE.md §4.5` pour les patterns détaillés par type de viz.

### Erreur #4 — Tirets cadratin (—) dans les titres ou contenus

**❌ INTERDIT (règle Empirik) :**
```js
title: "Très faible — vs 24,3% concurrent"
body: "Action prioritaire — équipe technique"
```

**✅ BON — remplacer par : virgule, deux-points, parenthèses, point médian :**
```js
title: "Très faible (vs 24,3% concurrent)"
body: "Action prioritaire : équipe technique"
"Démarrage · segments accessibles"
```

**🛠️ Fix de masse à appliquer SYSTÉMATIQUEMENT avant chaque génération :**
```bash
python -c "
with open('build_xxx.js', encoding='utf-8') as f: c = f.read()
c = c.replace(' — ', ' · ').replace('—', '·')
with open('build_xxx.js', 'w', encoding='utf-8') as f: f.write(c)
"
```

### Erreur #5 — Logos officiels OUBLIÉS pour les outils/marques connus

**Memory rule** : *"Logos officiels obligatoires — quand on mentionne un outil/marque connu (ChatGPT, Gemini, Wikipedia, concurrents…), intégrer son logo officiel via simple-icons / Wikimedia / sites officiels."*

**Réflexe à avoir AVANT la génération :** lister TOUS les noms propres mentionnés dans le contenu, et pour chacun :
1. Vérifier dans `assets/logos/` si on a déjà le PNG
2. Si manquant, le télécharger AVANT de coder les slides

**🛠️ MÉTHODE FIABLE EN 4 COUCHES (script `scripts/fetch_logos.py`)**

Au lieu de chercher à la main, utiliser le script de récupération automatique. **Mode auto recommandé pour les marques inconnues** : il essaie les 4 couches en cascade jusqu'à trouver.

```bash
# Mode auto (cascade des 4 couches) — le plus simple, à utiliser par défaut
python scripts/fetch_logos.py --auto "lemoniteur=lemoniteur" "dispano=dispano" "pointp=pointp"

# Ou couche par couche si on sait ce qu'on cherche :

# Layer 1 (rapide, marques tech connues) : simpleicons CDN
python scripts/fetch_logos.py --simpleicons cloudflare perplexity googleanalytics googlegemini

# Layer 2 (PNG haute résolution) : Wikipedia Commons API
python scripts/fetch_logos.py --wikipedia \
  "ChatGPT-Logo.svg=openai" \
  "Bing_Fluent_Logo_Text.svg=bing" \
  "Microsoft_logo_(2012).svg=microsoft"

# Layer 3 (multi-pages : home + /press + /brand + /media + /about) : scraping HTML
python scripts/fetch_logos.py --scrape \
  "https://www.polyrey.com/=polyrey" \
  "https://www.fundermax.com/=fundermax" \
  "https://www.lairdubois.fr/=lairdubois"

# Layer 4 (fallback puissant : sites Cloudflare / 403 persistant) : brandfetch.com API
python scripts/fetch_logos.py --brandfetch \
  "lemoniteur.fr=lemoniteur" \
  "dispano.fr=dispano" \
  "pointp.fr=pointp"
```

**Comment ça marche (fallback en cascade automatique) :**

| Couche | Méthode | Format | Idéal pour |
|--------|---------|--------|-----------|
| 1 | simpleicons.org CDN (`cdn.simpleicons.org/SLUG/HEX`) | SVG monochrome | Tech brands populaires (Cloudflare, GA, Perplexity, Gemini) |
| 2 | Wikipedia Commons API (`iiurlwidth=400` → PNG serveur-rendu) | PNG HD multicolore | Marques connues avec entrée Wikipedia (ChatGPT, Bing, Microsoft) |
| 3 | **Scraping HTML multi-pages** : home + `/press` + `/press-kit` + `/media` + `/brand` + `/about` + `/qui-sommes-nous`. Sur chaque page : `apple-touch-icon`, `og:image`, `<link rel="icon">`, `<img class="logo">`, `<svg id="logo">`, `<a class="logo"><img>`, liens `/logo.png`. Rotation User-Agent (Chrome → Firefox+Referer → Safari+Referer) si 403. | PNG/JPG/SVG | Marques de niche sans Wikipedia (forums sectoriels, médias spécialisés B2B) |
| 4 | **brandfetch.com API publique** (search puis téléchargement icon) | PNG/WebP HD | Sites résistants au scraping (Cloudflare, JS challenge, 403 persistant). Couvre la plupart des marques B2B reconnues qui résistent aux Layer 1-3. |

**Cas limites & fallbacks (si les 4 couches échouent) :**
- ❌ **403 Forbidden persistant** : le script tente déjà rotation User-Agent et 10 pages. Layer 4 (brandfetch) résout 90% des cas restants.
- ❌ **SSL certificate verify failed** : ajouter `ssl._create_unverified_context()` dans le script pour ce domaine.
- ❌ **Brand introuvable sur brandfetch** : passer aux méthodes manuelles d'escalade ci-dessous.
- ✅ **Persistance manuelle obligatoire** : voir bloc "Persistance obligatoire" ci-dessus (10 méthodes : Wikipedia EN, Wayback Machine, Google Images, agrégateurs tiers logo.wine / 1000logos.net / worldvectorlogo.com).

**Conversion SVG → PNG** :
- `cairosvg` et `svglib+reportlab` nécessitent libcairo natif (souvent absent Windows)
- Préférer obtenir directement du PNG via Layer 2 (Wikipedia rend côté serveur) ou Layer 3
- Si vraiment besoin d'une conversion locale : ImageMagick (`magick convert in.svg -resize 400x out.png`) ou Inkscape headless


- Bots / moteurs LLM cités (Google, Bing, OpenAI/ChatGPT, Anthropic/Claude, Perplexity, Gemini, Mistral…)
- Outils mesure cités (GA4, GSC, Cloudflare, Clarity, Hotjar, dashboards…)
- Concurrents directs nommés dans le brief
- Marques produits / fournisseurs cités
- Forums / communautés sectorielles évoqués
- Médias / publications sectorielles citées
- Plateformes / canaux nommés (LinkedIn, Instagram, TikTok…)

Le réflexe est **catégoriel** : à chaque type de nom propre rencontré dans le brief, lister puis chercher les logos. Le fait que la pres précédente concernait un secteur X (bois/BTP, cuisine, e-commerce, etc.) n'est PAS pertinent — chaque pres a sa propre liste à reconstruire from scratch.

#### ⛔ Persistance obligatoire — interdiction d'abandonner

> **Un logo existe TOUJOURS quelque part.** Si tu n'arrives pas à le récupérer, c'est que tu n'as pas essayé assez de méthodes. Écrire "logo introuvable" ou "le script n'a pas marché donc j'ai laissé tomber" est un **défaut bloquant**, pas une issue acceptable.

**Si les 3 couches automatiques échouent sur une marque, escalader avec ces 10 méthodes AVANT d'abandonner** :

1. **Crawler le site officiel en profondeur** (pas juste la home) : `/press`, `/press-kit`, `/media`, `/media-kit`, `/brand`, `/brand-assets`, `/about`, `/about-us`, `/qui-sommes-nous`. Ces pages contiennent souvent un kit logo téléchargeable en haute résolution.
2. **Inspecter le HTML de la home au-delà des meta** : balises `<img>` avec `class`/`alt` contenant "logo" ou "brand", `<svg>` inline avec id/class "logo", contenu de `<header>`/`<nav>`/`<footer>`.
3. **CSS background-image** : parser les `style="background-image:url(...)"` et les classes CSS qui référencent des images "logo".
4. **Wikipedia avec variantes du nom** : nom officiel (Le Moniteur → Groupe Moniteur), avec/sans suffixe SA/magazine/fr…, page de la marque parente si filiale (Point P → Saint-Gobain).
5. **Wikipedia EN** si la version FR ne donne rien (`en.wikipedia.org`).
6. **Agrégateurs tiers** : `brandfetch.com` (API JSON), `logo.wine`, `1000logos.net`, `worldvectorlogo.com`.
7. **Google Images / DuckDuckGo Images** : recherche `<marque> logo png transparent`, récupérer la 1ère image carrée propre.
8. **Bypass 403 Forbidden** : changer le User-Agent (`Mozilla/5.0 ... Firefox/121.0`), ajouter `Referer: https://google.com`, retenter.
9. **Bypass SSL fail** : `urllib.request` avec `ssl._create_unverified_context()` pour sites avec cert auto-signé.
10. **Wayback Machine** : `https://web.archive.org/web/<date>/<url>` retrouve une version récente si le site officiel est mort/bloqué.

**Règle d'arbitrage** : tu n'as le droit d'écrire "logo introuvable" dans le rapport QA QUE si tu as documenté les 10 méthodes ci-dessus essayées et leur échec respectif. Sinon, **continue jusqu'à trouver**.

**Astuce pratique** : pour le scraping site officiel, télécharger le HTML complet (`curl -L --user-agent "Mozilla/5.0"`) et chercher avec `grep -oE 'src="[^"]*logo[^"]*\.(svg|png)"'`. La balise `<img>` qui affiche le logo dans le header de la home **existe presque toujours** — il suffit de l'extraire correctement.

### Erreur #6 — Tableaux du PDF source TRONQUÉS dans les slides

**❌ Erreur commise** : PDF source avec 30 prompts → slide avec seulement 15 prompts visibles.

**✅ Règle** : si le client demande l'exhaustivité (la plupart du temps), TOUS les éléments des tableaux source doivent être restitués. Si volume trop important pour une slide :
- Réduire fontSize (jusqu'à 7.5pt pour les tableaux denses, 12pt min pour le texte courant standard)
- Utiliser 2 colonnes côte à côte
- Splitter sur 2 slides si nécessaire (jamais squeezer)

**Avant validation finale** : faire un mapping section par section PDF source ↔ slides générées, et lister explicitement ce qui a été omis (s'il y a vraiment besoin d'omettre, c'est justifiable, mais à signaler).

### Erreur #7 — Pas de QA visuel sur la totalité des slides

**Process obligatoire APRÈS génération :**
1. `node build_xxx.js` → PPTX
2. `soffice --headless --convert-to pdf` → PDF
3. PDF → JPG via PyMuPDF (`fitz`)
4. **Lire CHAQUE slide en image** (pas juste 2-3)
5. Vérifier chaque slide contre la checklist (typo, couleurs, em dashes, débordements de cadres)
6. Lancer un agent de vérification d'exhaustivité contre le PDF source

### Erreur #8 — Choisir un type de graphe sans tester l'adéquation aux valeurs réelles

**❌ Symptôme** : on choisit dumbbell / slope / dot plot parce que le plan le dit, sans vérifier si les valeurs réelles rendent le format pertinent. Cas typique : dumbbell pour comparer "30 vs 140" où l'une des deux valeurs est ~0 → les points s'agglutinent et le format perd son sens.

**Cas réel commis** : dumbbell pour Angora vs Sphinx en temps de toilettage (0,0,5,5,20 vs 30,15,20,15,60). Les points Angora s'agglutinent à gauche, format dégénéré.

**✅ Test obligatoire AVANT de coder chaque graphe (à faire dès l'étape 4 du plan, pas en QA)** :

1. **Écrire les valeurs numériques réelles**, pas "comparaison X vs Y" mais "30 vs 140" / "12-18 vs 9-15" / "4,5% vs 24,3%"
2. **Calculer le ratio** entre les valeurs. Si ratio > 3 ou si une des valeurs est ~0 → certains formats deviennent inadaptés :
   - **Dumbbell** : exige 2 valeurs non triviales sur chaque catégorie
   - **Slope graph** : exige des valeurs comparables aux deux périodes (pas une qui plonge à 0)
   - **Dot plot avec fourchettes** : exige des fourchettes qui ne se chevauchent pas trop
3. **Test "qu'est-ce que l'audience voit en 3 secondes"** au FORMAT lui-même, dès l'étape 4 :
   > "Sur ce graphe, sans aucune annotation textuelle, l'audience verra-t-elle le message principal en 3 secondes ?"

   Si non → changer de format AVANT de coder. C'est le format qui doit porter le message, pas une annotation béquille.

**Garde-fou : le test "si je retire les annotations textuelles"**
Si en imaginant le graphe sans ses labels/légendes/titres textuels, il ne dit plus rien → le format est mauvais, c'est l'annotation qui fait tout le travail. Changer de format (souvent : revenir à 2 chiffres-clés).

### Erreur #9 — Confondre fourchettes (variabilité) et écarts (différences)

**❌ Symptôme** : utiliser un dot plot avec fourchettes pour montrer un écart entre 2 entités. L'œil voit le chevauchement des fourchettes, pas l'écart entre les médianes.

**Cas réel commis** : dot plot "Angora vit 12-18 ans vs Sphinx 9-15 ans" pour faire passer "+3 ans". Les deux lignes ont la même longueur (6 ans de fourchette) → ratio visuel identique → message inverse de celui voulu.

**✅ Règle de séparation des dimensions** :

| Ce qu'on veut montrer | Format adapté |
|----------------------|---------------|
| **Écart entre 2 entités** (différence de moyennes / médianes) | 2 chiffres-clés + écart en orange, OU bar chart vertical à 2 barres |
| **Variabilité individuelle** (distribution interne d'une entité) | Dot plot / boxplot (mais c'est de l'exploratoire §4.15, à éviter en explicatif) |
| **Les deux à la fois** | 2 slides séparées : slide 1 = écart, slide 2 = variabilité (si vraiment utile) |

Ne jamais mélanger les deux dimensions sur le même graphe explicatif : l'audience ne sait pas où regarder.

### Erreur #10 — Importer un PNG matplotlib non centré

**❌ Symptôme** : labels asymétriques en matplotlib (légendes plus longues à gauche qu'à droite) → padding asymétrique du PNG → contenu utile visuellement décalé une fois importé dans la slide.

**✅ Workflow obligatoire après génération d'un PNG :**

1. Générer le PNG via `scripts/generate_chart.py`
2. **Ouvrir le PNG dans le Read tool** (analyse visuelle multimodale)
3. Vérifier visuellement le centrage : tracer mentalement les axes du PNG, le contenu utile (lignes, points, barres) doit être centré
4. **Si décalé**, 3 solutions :
   - Ajuster `xlim` / `ylim` matplotlib pour symétriser les marges
   - Cropper proprement avec PIL (`Image.crop(box)`)
   - Compenser le décalage dans `addImage()` PptxGenJS en jouant sur `x` et `w`

### Erreur #11 — Texte hard-codé dans le PNG matplotlib (non modifiable)

**❌ Symptôme** : générer un PNG matplotlib avec tous les textes (titres, axes, étiquettes de séries, annotations) directement intégrés dans l'image. Une fois importé dans PowerPoint / Google Slides, ces textes sont **pixelisés et non éditables**.

**Pourquoi c'est un problème** : l'utilisateur (ou un collègue) ouvre le PPTX dans Google Slides pour corriger une coquille ou ajuster un libellé → impossible, c'est un screenshot du graphe.

**✅ Règle : séparer le visuel du texte**

Le PNG matplotlib doit contenir UNIQUEMENT les éléments visuels qui ne peuvent pas être faits en PptxGenJS : lignes, points, barres, gradients, courbes, zones colorées. **Aucun texte dans le PNG.**

Tous les textes (axes, étiquettes de séries, annotations, valeurs en bout de ligne) sont ajoutés ensuite via PptxGenJS `slide.addText()` en superposition, positionnés relativement au PNG importé.

**Procédure** :
1. `generate_chart.py` génère le PNG **sans texte** + un fichier JSON sidecar avec les coordonnées (en % du PNG) où chaque texte doit être placé
2. Le script `build_xxx.js` :
   - Importe le PNG via `addImage()`
   - Lit le JSON sidecar
   - Place chaque texte via `addText()` aux coordonnées calculées (en fonction de `x/y/w/h` de l'image)
3. Résultat : tous les libellés sont des `<txBody>` PptxGenJS = éditables dans PowerPoint / Google Slides

---

## 📋 CHECKLIST QA FINALE (à exécuter avant de livrer)

```
TYPOGRAPHIE
[ ] Sur-titres : Poppins ExtraLight 12pt orange #E9540D, CASSE NORMALE, sans charSpacing
[ ] Titres : Poppins SemiBold 22pt bleu #0A3856 (utiliser fontFace, pas fontWeight)
[ ] Aucun .toUpperCase() dans le script
[ ] Aucun charSpacing > 0 sur les eyebrows / sur-titres
[ ] Aucun texte < 12pt visible (sauf footer notes 9-10pt OK)

CONTRASTE — LISIBILITÉ
[ ] grep "color: YELLOW" → vérifier chaque occurrence (jaune sur blanc INTERDIT pour texte)
[ ] Texte courant en BLUE (#0A3856)
[ ] Chiffres clés en ORANGE (#E9540D), JAMAIS en YELLOW

CONTRASTE — STRATÉGIQUE (un seul élément ressort)
[ ] Sur chaque graphique : un seul élément en ORANGE, le reste en gris/bleu atténué
[ ] Sur chaque slide à N cartes/KPIs : UN seul en ORANGE qui appuie le titre, les autres en BLUE
[ ] Pas de palette multicolore "décorative" sans rôle narratif explicite
[ ] Test : "qu'est-ce que l'audience doit voir en 2s ?" → c'est ça, et ça seul, qui ressort

HIÉRARCHIE TYPO (texte dense, paragraphes, bullets longues)
[ ] Gras posé sur 2-4 mots porteurs de sens par bloc (max 25-30% du bloc en gras)
[ ] Orange sur 1 à 3 mots/chiffres-clés max par bloc (jamais sur tout)
[ ] Italique uniquement pour citations, sources, termes étrangers (jamais déco)
[ ] Souligné uniquement pour liens cliquables réels (jamais pour mettre en avant)
[ ] Test scan : lire uniquement le gras + orange → le message principal doit ressortir

COULEUR — OUTIL STRATÉGIQUE (jamais décoratif)
[ ] Compter les couleurs vives sur chaque slide : si > 3 sans rôle narratif, réduire
[ ] Pour chaque couleur : "quelle info elle véhicule ? si je la retire, le message perd-il du sens ?"
[ ] Heatmaps / dégradés : UNE seule couleur en intensité, jamais une couleur par valeur (anti-rainbow)
[ ] Échelle divergente (+/-) : bleu Empirik → blanc → orange Empirik (pas rouge/vert)
[ ] Test noir & blanc : le message principal doit survivre sans la couleur (sinon redoubler position/taille/étiquette)

TEST DES 3 SECONDES (pour chaque slide image générée)
[ ] Regarder l'image SANS lire le contenu : sur quel élément l'œil se pose en premier ?
    (le plus saturé / le plus gros / le plus contrasté / position dominante)
[ ] Identifier l'élément vedette voulu (celui qui appuie le titre de la slide)
[ ] Match entre les deux ? Si OUI → hiérarchie OK. Si NON → corriger :
    - Atténuer / retirer l'élément décoratif qui capte l'œil à tort
    - Agrandir / mettre en gras / isoler l'élément vedette
    - Griser tout sauf l'élément vedette
    - Repositionner l'élément vedette dans la zone dominante (centre / haut)
[ ] Pour slides multi-éléments (tableau de bord) : définir un ordre de lecture intentionnel (1→2→3...),
    élément #1 le plus saillant, intensité dégressive ensuite

ÉLIMINER LES DISTRACTIONS — test "Et si je l'enlevais ?"
[ ] Pour chaque élément visible (chiffre, ligne, label, cadre, icône, légende, axe, sous-titre, note) :
    "Si je retire ça, l'audience perd-elle de l'info pour comprendre le message ?"
    → NON = supprimer purement. OUI = garder en arrière-plan (gris atténué, taille réduite).
[ ] Hiérarchiser en 3 niveaux :
    1. Essentiel = appuie le message du titre → pleine intensité orange/bleu
    2. Nécessaire mais secondaire = contexte (axes, sources, baseline) → gris #B0B0B0, taille réduite
    3. Non essentiel = déco, redondance, "bon à savoir" → SUPPRIMER
[ ] Cibler les distractions classiques : bordures inutiles, lignes de grille superflues,
    légendes remplaçables par étiquettes directes, icônes déco, sous-titres redondants,
    colonnes "info contextuelle" rarement regardées, ticks d'axes intermédiaires.
[ ] Après nettoyage, refaire le test des 3 secondes : l'œil va-t-il droit sur l'essentiel ?

PONCTUATION
[ ] grep -c "—" → DOIT renvoyer 0 (aucun tiret cadratin)
[ ] Accents diacritiques tous en place (relecture orthographique)

LOGOS
[ ] Logo Empirik UNIQUEMENT sur slide cover (jamais ailleurs)
[ ] Pour chaque marque/outil cité, logo officiel intégré quand pertinent

CONTENU
[ ] Voix "vous" partout, jamais "nous"
[ ] Chaque slide data a une mention "Source : ... · Période : ..."
[ ] URLs externes cliquables (hyperlink dans PptxGenJS)
[ ] Exhaustivité PDF source vs slides vérifiée par agent

VISUEL
[ ] Aucun débordement de cadre (texte qui dépasse)
[ ] Aucun chevauchement entre éléments
[ ] Footer + numéro de page sur chaque slide standard
[ ] Slide cover et CTA en exception (pas de footer/sur-titre)

ALIGNEMENT STRICT (CLAUDE.md §3.7)
[ ] Tous les éléments d'une rangée partagent la même coordonnée Y
[ ] Tous les éléments d'une colonne partagent la même coordonnée X
[ ] Cartes côte à côte : même largeur, même hauteur, mêmes espacements (calculés, pas "à l'œil")
[ ] Texte aligné à gauche par défaut (sauf titres centrés et chiffres alignés droite)
[ ] Nombres dans tableau : alignés à droite, même nombre de décimales sur grandeurs comparables
[ ] Icônes / numéros / badges centrés dans leur conteneur et alignés avec le texte associé
[ ] Sources / footnotes en bas de slide, même position Y partout dans le deck
[ ] Sur graphes : labels d'axes alignés sur les ticks, étiquettes de barres au même niveau
[ ] Test : tracer mentalement des lignes verticales/horizontales — tout doit toucher la grille invisible

CHOIX DU GRAPHE (CLAUDE.md §4.10)
[ ] Type de graphe dans la liste des 6 par défaut (barre horiz/vert/empilée, ligne, slope, dot plot)
    — sinon justification écrite explicite
[ ] Pas de 3D (jamais), pas de radar / sankey / treemap / gauge sur audience non spécialiste
[ ] Pas de pie chart > 3 parts → barre horizontale triée
[ ] Pas de 2 pies côte à côte → slope graph à la place
[ ] Pas de tableau de chiffres sauf si la valeur exacte est le livrable
[ ] Évolution temporelle ≥ 4 points → ligne. 2 périodes → slope. 3 points → barres verticales possible.

DÉCOMBRER LES GRAPHES (CLAUDE.md §4.11)
[ ] Pas de bordure, pas de gridlines (ou très atténuées), fond blanc
[ ] Pas de trailing zeros (1000.0 → 1000, 10.00% → 10%)
[ ] Pas de texte diagonal sur axe X (abréger les labels pour rester horizontal)
[ ] Axe Y OU data labels (pas les deux en même temps)
[ ] Pas de décimales inutiles (47,3% → 47% si la précision ne porte pas le message)
[ ] Barres épaisses (espace blanc entre barres ≤ largeur de barre)
[ ] Tri par valeur sur barres horizontales (sauf ordre sémantique : jours, étapes, classes d'âge)
[ ] Pas de re-titrage interne du graphe (le titre de slide centré porte le takeaway)

COHÉRENCE DES FORMATS DANS LE DECK (CLAUDE.md §4.12)
[ ] Même police, mêmes tailles par rôle (titre/axe/label/footer) sur tout le deck
[ ] Même casing des titres (Sentence case partout)
[ ] Même format de date partout (`Mai 2026` ou `05/2026`, pas alternance)
[ ] Mêmes noms de métriques / séries (jamais `Citations` puis `Mentions` pour la même chose)
[ ] Même palette de couleurs cohérente sur tout le deck
[ ] Mêmes unités et précisions sur grandeurs comparables

LEVIERS DE CONTRASTE (CLAUDE.md §4.13)
[ ] Couleur (orange vs bleu/gris) appliquée sur élément vedette UNIQUEMENT
[ ] 2-3 leviers empilés sur l'élément vedette (couleur + épaisseur + label)
[ ] Pointillé STRICTEMENT réservé à l'incertitude (forecast/cible/projection), JAMAIS pour focaliser
[ ] Pas de marker visible sur tous les points : juste 1-2 points stratégiques

ANNOTATIONS + RENOMMAGE BUSINESS (CLAUDE.md §4.14)
[ ] Annotations courtes (2-3 points stratégiques max) sur le graphe — pas tous les points
[ ] Catégories techniques renommées en termes business (pas `Treatment_1`, pas `Q1_2025_var_pct`)
[ ] Footnote sous graphe pour définir métriques techniques si nécessaire (1 ligne, gris atténué)

EXPLORATOIRE ≠ EXPLICATIF (CLAUDE.md §4.15)
[ ] Aucun box plot / scatter / courbe de survie / matrice de corrélation dans le deck final
[ ] Si un visuel exploratoire est tentant : remplacer par un visuel des 6 types par défaut
    OU par 2-3 chiffres-clés en bloc qui transportent le même insight

ESPACE BLANC / RESPIRATION (CLAUDE.md §4.16)
[ ] Marges 60px respectées (non négociable)
[ ] Densité de la slide ≤ 60-70% de la surface utile (tableaux denses = exception explicite)
[ ] Si débordement ou étouffement → splitter en 2 slides, jamais réduire marges/police
[ ] Test rapide : si on retire 20% du contenu, la slide devient-elle plus claire ? Si oui → nettoyer.

BUILD SEQUENCE (CLAUDE.md §4.17) — anti spaghetti chart
[ ] Identifier si le graphe est saturé (6+ lignes/séries qui se croisent, toutes importantes)
    → C'est le piège du "spaghetti chart" : 1 ligne en avant à la fois sur N slides successives
[ ] Si oui : créer N slides successives avec le MÊME graphe (mêmes axes, mêmes positions, même taille)
[ ] Sur chaque slide, un seul élément en orange Empirik (le reste en gris #B0B0B0)
[ ] Annotation courte (1 ligne) à côté de l'élément vedette de chaque slide
[ ] Titre takeaway dédié à l'élément vedette de chaque slide (pas un titre générique répété)
[ ] Cohérence visuelle absolue entre les N slides : l'œil doit suivre les éléments d'une slide à l'autre
[ ] Slide finale optionnelle : tous les éléments en couleur OU récap "Ce qu'il faut retenir"
[ ] Ne pas utiliser pour graphes simples (2-3 catégories) : artillerie pour visus riches uniquement

TITRES (CLAUDE.md §2.7)
[ ] Test narratif : lire UNIQUEMENT les titres dans l'ordre → l'histoire doit s'enchaîner sans contenu
[ ] Test bi-directionnel sur chaque slide :
    - Le contenu renforce-t-il la pertinence du titre ? (preuves qui font tenir le titre)
    - Le titre renforce-t-il la pertinence du contenu ? (sans le titre, l'audience ne saurait pas où regarder)
[ ] Titres takeaway (verdict / constat), jamais descriptifs (sujet)

RECOMMANDATION FINALE OBLIGATOIRE (CLAUDE.md §2.1)
[ ] Le deck se termine par une action recommandée explicite : `Nous recommandons de <verbe> pour <résultat>`
[ ] Si pas de reco formulable après l'analyse → c'est de la donnée brute, pas une présentation
    (livrer en rapport markdown plutôt qu'en deck)
```

---

## 🧰 PATTERNS DE CODE PPTXGENJS — RÉFÉRENCE

### Le helper `addSurTitleAndTitle` officiel

```js
function addSurTitleAndTitle(slide, section, title) {
  // Sur-titre orange Poppins ExtraLight 12pt centré, casse normale
  slide.addText(section, {
    x: 0.5, y: 0.30, w: 9, h: 0.28,
    fontFace: "Poppins ExtraLight", fontSize: 12, color: "E9540D",
    bold: false, align: "center", valign: "middle", margin: 0,
  });
  // Titre principal Poppins SemiBold 22pt bleu centré, collé au sur-titre
  slide.addText(title, {
    x: 0.4, y: 0.60, w: 9.2, h: 0.7,
    fontFace: "Poppins SemiBold", fontSize: 22, color: "0A3856",
    bold: false,
    align: "center", valign: "middle", margin: 0,
  });
}
```

### Mappings de couleurs par type d'élément

| Élément | Couleur fond | Couleur texte |
|---------|--------------|---------------|
| Texte courant sur blanc | BLANC | BLUE #0A3856 |
| Chiffre clé sur blanc | BLANC | ORANGE #E9540D |
| Badge "Critique" | ORANGE | BLANC |
| Badge "Haute" | BLUE | BLANC |
| Badge "Normale" | TEXT_GREY | BLANC |
| Cellule statut "Oui/OK" | LIGHT/transparent | VERT #10A050 |
| Cellule statut "Non/Absent" | LIGHT/transparent | ORANGE |
| Cellule statut "À confirmer" | LIGHT/transparent | TEXT_GREY (pas YELLOW) |
| Accent bord supérieur de carte | ORANGE ou YELLOW | — |

### Commande de QA visuel

```bash
# Génération + conversion + extraction images en une seule chaîne
NODE_PATH="$NPM_GLOBAL/node_modules" node build_xxx.js && \
"C:\\Program Files\\LibreOffice\\program\\soffice.exe" --headless --convert-to pdf build_xxx.pptx && \
python -c "
import fitz
doc = fitz.open('build_xxx.pdf')
for i, p in enumerate(doc):
    p.get_pixmap(dpi=110).save(f'qa-slides/slide-{i+1:02d}.jpg')
print(f'{doc.page_count} pages générées dans qa-slides/')
"
```

---

## 🧠 RÉORGANISATION DE TON PROCESS MENTAL

Quand on te demande de transformer un document en slides :

1. **LIRE EN ENTIER** le PDF source AVANT d'ouvrir le moindre fichier de design
2. **EXTRAIRE** les éléments structurés (chiffres, tableaux, listes, citations) dans une note mentale
3. **LISTER** les marques/outils → planifier les logos
4. **LIRE** CLAUDE.md + ce PROCESS-ANTI-ERREURS.md + memory rules
5. **STRUCTURE** : Acte 1 / Acte 2 / Acte 3 (Nancy Duarte) avec big idea formulée
6. **CODER** : utiliser le helper `addSurTitleAndTitle` officiel, palette stricte, fontFace explicite pour les variants
7. **PRÉ-COMMIT FIX** : python script pour replace em dashes
8. **GÉNÉRER** : PPTX → PDF → images JPG
9. **QA EXHAUSTIF** : lire CHAQUE slide image + vérifier contre PDF source
10. **DOC FINALE** : checklist remplie + signalement explicite des "À vérifier"

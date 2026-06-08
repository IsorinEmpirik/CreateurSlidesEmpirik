# Contexte condensé pour sous-agents Empirik

> **À injecter en contexte de chaque sous-agent du workflow `/empirik-slides`** au lieu de leur faire relire `CLAUDE.md` (1700+ lignes) à chaque invocation.
>
> Gain de perf attendu : ~3 min × 6 sous-agents = ~18 min par génération.
>
> Si un sous-agent rencontre une règle ambiguë ou un cas non couvert ici → autorisation de consulter `CLAUDE.md`, `PROCESS-ANTI-ERREURS.md` ou `MASTER-CHECKLIST.md` à la section pointée. Sinon, ce fichier suffit.

---

## 1. CHARTE EMPIRIK — RÈGLES NON NÉGOCIABLES

### Palette (4 couleurs strictes)
- **Bleu Empirik** `#0A3856` : titres, texte courant, structure, baseline (joue le rôle du "gris dominant" Knaflic)
- **Orange Empirik** `#E9540D` : accent narratif vedette (joue aussi le rôle du "rouge alerte" Knaflic, pas de rouge en charte)
- **Jaune** `#FCC02D` : accent décoratif uniquement (bordures, badges, icônes), JAMAIS texte sur blanc
- **Gris** `#B0B0B0` : contexte secondaire, éléments atténués
- **Vert ad-hoc** `#10A050` : autorisé uniquement KPI atteint explicitement (cible vs réalisé)

### Typo Poppins (variants obligatoires via `fontFace`)
- Titre principal : `fontFace: "Poppins SemiBold"`, 22pt, bleu `0A3856`, centré
- Sur-titre : `fontFace: "Poppins ExtraLight"`, 12pt, orange `E9540D`, centré, **casse normale** (pas `.toUpperCase()`, pas `charSpacing`)
- Texte courant : `fontFace: "Poppins"`, 14pt, bleu, gauche
- Chiffre clé : `fontFace: "Poppins Bold"`, 48-72pt, orange, centré
- Sur-titre y=0.30, titre y=0.60 (collés en haut)
- **JAMAIS `fontWeight`** (silencieusement ignoré par PptxGenJS) → toujours `fontFace` variant

### Mise en page
- LAYOUT_16x9 (10" × 5.625")
- Marges minimum 0.6"
- Densité max 60-70% surface utile (sauf tableaux denses exceptionnels)
- Alignement strict : éléments d'une rangée même Y, éléments d'une colonne même X
- Max 6 bullets par slide

### Cover (TOUJOURS template Empirik, jamais demander si perso)
Logo Empirik haut-gauche + logo client haut-droite si client + ligne séparation + image gauche 50% + titre orange Poppins Bold 48-60pt droite + trait orange + sous-titre + date + motif jaune décoratif bas.
Logo Empirik UNIQUEMENT sur cover, INTERDIT ailleurs.

---

## 2. RÈGLES DE FOND

### 2.1 Top-down McKinsey
- Slide 2 = synthèse/reco systématique après cover
- Chaque section = slide "Ce qu'il faut retenir" en ouverture
- Recommandation finale obligatoire (`Nous recommandons de <verbe> pour <résultat>`)
- Si aucune action formulable → rapport markdown, pas un deck

### 2.2 Voix "vous" QUANTIFIÉE
- ≥ 70% des slides standard (hors cover/dividers/CTA) contiennent `vous` / `votre` / `vos`
- Auto-test obligatoire : `grep -ciE "\b(vous|votre|vos)\b" build_xxx.js` puis comparer
- "Nous" INTERDIT sauf "Nous recommandons" sur slide reco finale (préférer "Adoptez...")

### 2.4 Source obligatoire sur slide data
- Mention `Source : <outil> · Période : <dates>` en footer 10-11pt gris
- Multi-sources toutes listées
- URLs externes cliquables (PptxGenJS `hyperlink`)

### 2.6 Logos officiels
- Chaque marque/outil/site cité = logo intégré
- Workflow : `python scripts/fetch_logos.py --auto "marque=dest"` (4 couches : simpleicons → Wikipedia → scraping → brandfetch)
- **QA visuelle pre-flight OBLIGATOIRE** : ouvrir chaque PNG avec Read tool pour vérifier marque + version + format avant `addImage()`
- **Refresh forcé LLM en début de session** : ChatGPT, Claude, Gemini, Perplexity, Mistral, Copilot, Grok, DeepSeek (cache > 3 mois = probablement obsolète)
- Persistance OBLIGATOIRE : 10 méthodes d'escalade documentées (voir PROCESS-ANTI-ERREURS Erreur #5) avant d'écrire "logo introuvable"

### 2.7 Titres
- TAKEAWAY (verdict), pas descriptif (sujet)
- "Le T3 dépasse la cible pour la 1re fois en 4 ans" pas "Ventes T3"
- Test narratif : lire les titres seuls → l'histoire doit s'enchaîner
- Test bi-directionnel : titre ↔ contenu se renforcent

### 2.8 Pas de tiret cadratin (—)
- Remplacer par virgule, deux-points, parenthèses, point médian (·)
- Auto-test : `grep -c "—" build_xxx.js` → DOIT = 0

### 2.9 Accents diacritiques UTF-8
- Écrire `chiffrées`, `généré`, `défense`, `cœur`, `très`, `dès` directement
- AUCUNE substitution préventive par ASCII (`chiffrees`, `genere`)
- L'environnement est UTF-8 garanti, point.
- Cf `PROCESS-ANTI-ERREURS Erreur #12`

---

## 3. DATAVIZ — RÈGLES CRITIQUES

### Choix du graphe (6 par défaut)
Barre horiz / barre vert / barre empilée / ligne (≥4 points) / slope (2 périodes) / dot plot. Au-delà, justifier.

### Test d'adéquation aux valeurs réelles (CLAUDE.md §4.10)
Avant chaque graphe : écrire valeurs exactes (pas "X vs Y" mais "30 vs 140"). Si ratio ≥ 3 ou une valeur ~0 → dumbbell / slope / dot plot inadaptés → **Voie 4 chiffres-clés**.

### Test "sans annotation"
Si le graphe ne dit rien quand on retire les libellés textuels → mauvais format.

### Interdits
3D · radar · sankey · pie > 3 parts · 2 pies côte à côte · tableau dense de chiffres · double axe Y · rainbow.

### Contraste stratégique
**Un seul élément vedette** par graphique → orange Empirik. Tout le reste en gris/bleu atténué. Test 3 secondes : l'œil va sur l'élément vedette voulu ?

### Heatmaps / dégradés
UNE seule couleur en intensité. Jamais une couleur par valeur (anti-rainbow).

### 4 voies de génération
1. **Shapes PptxGenJS** : barres simples, KPI cards
2. **Charts natifs** : line chart simple, doughnut
3. **Python matplotlib → PNG** : slope, dot, heatmap, waterfall, line annoté. **PNG SANS texte** + JSON overlays sidecar, textes ajoutés en superposition via PptxGenJS (éditables Google Slides)
4. **Chiffres-clés seuls** : pour ratios ≥ 3, écarts simples. Souvent supérieur à un graphe.

### Cohérence du deck
Même police / casing / palette / format date / noms de séries / unités sur tout le deck.

### Build sequence (anti spaghetti chart)
Si line chart à 6+ lignes toutes importantes → répéter même graphe sur N slides, une seule ligne en orange à la fois, autres en gris.

---

## 4. STORYTELLING

### Acte 1 / 2 / 3 (Duarte) ~10/80/10%
Setup (what is) → Confrontation (alternance what is ↔ what could be) → Nouvelle félicité + CTA.

### Plot / Twist / Ending (Knaflic)
Contexte → moment de bascule → action recommandée.

### Big idea complète
Point de vue + ENJEUX (gain ET perte évitée). Pas juste verdict sec.

### Audience-héros
Profil incarné (rôle, âge, peur, désir), pas "les stakeholders".

### S.T.A.R. moment (Something They'll Always Remember)
Au moins 1 : sound bite ciselé, stat choquante humanisée, visuel évocateur, dramatisation, mini-histoire.

### Humanisation des chiffres
Top 3 chiffres-clés ont une analogie familière (ex : "11 700 €" → "voyage aux Maldives").

### Sparkline
4 alternances minimum "ce qui est" ↔ "ce qui pourrait être".

### Nouvelle félicité (§5.6)
Slide entre reco et CTA. Projection narrative du futur. **JAMAIS pavé > 60 mots monobloc** → 3 moments visuels (ouverture / pivot ancré chiffré / résolution).

### Équilibre Logos/Pathos/Ethos
Logos 50-65% / **Pathos ≥ 20% obligatoire** / Ethos 10-15%. Si < 20% sur sujet narratif → défaut bloquant.

### Métaphore filée
Une seule, mentionnée dès cover, rappelée 2-3 fois.

---

## 5. STACK TECHNIQUE

### Pièges PptxGenJS connus
- `fontWeight` silencieusement ignoré → utiliser `fontFace` variant
- Réutiliser un objet d'options entre `addText`/`addShape` → PptxGenJS le mute, créer un nouvel objet à chaque appel
- `barDir: "bar"` rend labels comme indices numériques en LibreOffice → construire les barres manuellement
- Ombres : pas de valeur négative pour `offset`, pas de couleur 8-char hex

### Pipeline génération
```bash
NODE_PATH="$NPM_GLOBAL/node_modules" node build_xxx.js
"C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf build_xxx.pptx
python -c "import fitz; doc=fitz.open('build_xxx.pdf'); [p.get_pixmap(dpi=110).save(f'qa-slides/slide-{i+1:02d}.jpg') for i,p in enumerate(doc)]"
python -m markitdown build_xxx.pptx
```

### Helpers
- `scripts/fetch_logos.py --auto "marque=dest"` (4 couches)
- `scripts/generate_chart.py --type [slope|line|dot|bar|dumbbell|heatmap|waterfall] --data data.json --output assets/charts/X.png --highlight VEDETTE`
- `scripts/generate_image.py --type [cover|section|concept|workflow|comparison|data-backdrop|closing]` (Gemini)

---

## 6. QA — RÈGLES DE PROCÉDURE (pour sous-agents auditeurs)

### Preuves atomiques obligatoires
Une preuve = citation directe + référence (slide N, ligne L du script, sortie de commande). **Preuves circulaires INTERDITES** (pointer vers un autre ✅ = nulle).

### Comptages chiffrés pour règles quantifiables
Voix vous, em-dashes, ratio dataviz, proportions actes Duarte, exhaustivité brouillon, % Pathos. Toujours donner le chiffre, pas "règle respectée".

### Mandat devil's advocate
Par défaut chaque bloc est ❌. Le producteur doit prouver atomiquement chaque ✅.

### Si > 3 ✅ sans preuve atomique → rapport rejeté
Recommencer la QA, ce n'est pas fini.

---

## 7. RÈGLES TRANSVERSALES

- **Pas d'invention de data** : signaler échec/ambiguïté explicitement, jamais combler. Distinguer DATA SOURCÉE / CALCUL RECONSTRUIT (~préfixe + footnote) / ESTIMATION FRAGILE (badge orange "à reconfirmer").
- **Avocat du diable** sur chaque reco/chiffre du brouillon : preuve / limites / robustesse.
- **Pas de conclusions interprétatives** dans les rapports markdown d'analyse.
- **Voix "vous"** quantifiée ≥ 70% (cf §2.2).
- **Format dates** : `Mai 2026` partout, pas `05/2026` un slide sur deux.

---

## 8. CAS D'AMBIGUÏTÉ — où chercher

Ce fichier suffit pour 95% des décisions. Pour le reste :

| Sujet | Source |
|-------|--------|
| Détails dataviz Knaflic (slopegraph, waterfall, ordre catégories) | `CLAUDE.md §4.3` + `guide-slides-data-storytelling.md` |
| Pièges PptxGenJS spécifiques + 13 erreurs récurrentes | `PROCESS-ANTI-ERREURS.md` |
| Items checklist QA exhaustive | `MASTER-CHECKLIST.md` |
| Templates slides | `CLAUDE.md §3.5-§3.7` + `guide_design_slides.md` |
| Prompts Gemini par type d'asset | `DESIGN_EMPIRIK.md` |
| Méthode Nancy Duarte intégrale | `guide_storytelling_presentations.md` |

Hiérarchie de priorité en cas de conflit : **CLAUDE.md > PROCESS-ANTI-ERREURS.md > guides externes**.

---

*Ce fichier est versionné. Si une règle évolue dans CLAUDE.md ou ailleurs, mettre à jour ce fichier en miroir.*

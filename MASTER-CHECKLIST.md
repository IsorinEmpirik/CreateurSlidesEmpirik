# MASTER CHECKLIST — Rapport QA obligatoire pour chaque présentation

> **OBLIGATOIRE après chaque génération de slides.**
> À produire en markdown comme rapport de livraison à côté du `.pptx`.
> Pas de livraison sans ce rapport rempli avec preuves atomiques point par point.

---

## ⛔ RÈGLE FONDAMENTALE — Le rapport est rempli par un sous-agent INDÉPENDANT

**L'agent producteur n'a PAS LE DROIT de cocher ✅ lui-même.** L'auto-évaluation est structurellement compromise : sur l'audit "Angora vs Sphinx v2", l'agent producteur avait coché 17/17 blocs ✅ alors que 3 méritaient ❌.

**Procédure correcte** :
1. L'agent producteur livre : .pptx + script source + PDF de QA visuelle + brouillon source
2. **Un sous-agent QA indépendant** lance cette checklist en mode "devil's advocate" : par défaut chaque bloc est ❌, il faut une PREUVE ATOMIQUE pour passer en ✅
3. L'agent producteur lit le rapport, propose des corrections sur les ❌, le sous-agent re-statue
4. **Un 3ème sous-agent (Devil's advocate)** challenge le rapport final : il retraite en ❌ tout ✅ dont la preuve est circulaire, absente, ou non quantifiée

Voir CLAUDE.md §0 Étape 8 et Étape 8.5 pour les mandats détaillés des sous-agents.

---

## ⛔ ANTI-CASCADE — Format des preuves atomiques obligatoire

Toute case ✅ doit s'accompagner d'une **preuve atomique** : citation directe + référence à un élément CONCRET et VÉRIFIABLE du livrable.

| ✅ PREUVE ATOMIQUE (accepté) | ❌ PREUVE CIRCULAIRE (refusé, retraite en ❌) |
|------------------------------|------------------------------------------------|
| "vérifié slide 7 : '4,5%' bien en orange #E9540D, gras (capture qa-slides/slide-07.jpg)" | "preuve = confirmé bloc F" |
| "ligne 234 du script : `fontFace: 'Poppins SemiBold'`" | "preuve = voir bloc T sur voix vous" |
| `grep -c "—" build.js` → 0 | "preuve = règle §2.2 appliquée" |
| "comptage : 12 slides standard sur 17 contiennent 'vous' = 70,6% (seuil 70% respecté)" | "preuve = voix vous OK partout" |

**Règle de quantification** : pour toute règle quantifiable (voix "vous", em-dashes, ratio dataviz, couverture brouillon, proportions actes Duarte), exiger un **comptage chiffré explicite** dans la preuve. Pas de "✅ règle respectée" sans chiffre.

---

## Comment utiliser cette checklist

1. **À chaque génération**, créer un fichier `qa-rapport-<nom-pres>.md` à côté du `.pptx`
2. **Copier-coller cette checklist** dans le rapport
3. **Lancer le sous-agent QA indépendant** avec le mandat de CLAUDE.md §0 Étape 8
4. Le sous-agent statue `✅` ou `❌` avec preuve atomique pour chaque ✅
5. **Lancer le sous-agent Devil's advocate** (Étape 8.5) qui challenge toutes les preuves
6. **Joindre les 2 rapports** (sous-agent QA + Devil's advocate) à la livraison du `.pptx`

Score cible : **100% ✅** sur les blocs "non négociable" (incluant Y, Z, AA, BB, CC), **≥ 90% ✅** sur les blocs "qualité".

---

## A. PRE-FLIGHT (avant 1ère ligne de code) — non négociable

```
[ ] J'ai lu CLAUDE.md en entier (1028+ lignes)
[ ] J'ai lu PROCESS-ANTI-ERREURS.md en entier (442+ lignes)
[ ] J'ai lu guide_design_slides.md, guide_storytelling_presentations.md, dataviz-guide.md, guide-slides-data-storytelling.md
[ ] J'ai compris la hiérarchie : CLAUDE.md > PROCESS > guides externes
[ ] J'ai listé TOUS les noms propres (marques/outils/concurrents/médias) à intégrer en logos
[ ] J'ai téléchargé les logos manquants via scripts/fetch_logos.py AVANT de coder
[ ] J'ai identifié les chiffres-clés du brief / PDF source à intégrer SANS exception
[ ] J'ai planifié les tableaux source en intégralité (pas de troncage prévu)
[ ] J'ai validé un plan détaillé avec l'utilisateur (sauf instruction explicite "skip")
[ ] Pour chaque slide data du plan : type de graphique justifié selon CLAUDE.md §4.10
[ ] Pour chaque section : mécanique storytelling explicitée (what is → what could be → bascule → preuve)
```

## B. STRUCTURE NARRATIVE — non négociable

```
[ ] Slide cover conforme au template Empirik (logo + image + titre orange + motif jaune)
[ ] Slide synthèse/recommandation présente JUSTE après la cover (CLAUDE.md §2.1)
[ ] Pour chaque section : slide "ce qu'il faut retenir" en ouverture
[ ] Recommandation finale explicite en dernière slide (CLAUDE.md §2.1)
    → Sinon : présentation impossible (donnée brute, pas de pres)
[ ] Test narratif : lire UNIQUEMENT les titres dans l'ordre → l'histoire s'enchaîne
[ ] Test bi-directionnel sur chaque slide : titre ↔ contenu se renforcent mutuellement
[ ] Structure Acte 1/2/3 (Duarte) ou Plot/Twist/Ending (Knaflic) respectée
[ ] Préambule "volatilité GEO" présent si pres GEO/LLM (CLAUDE.md règle de fond)
[ ] 1 graphe = 1 slide (pas de bloc de 4 graphes côte à côte)
```

## C. TITRES DE SLIDES — non négociable

```
[ ] Chaque titre est un CONSTAT CONCRET, pas une étiquette / catégorie
[ ] Chaque titre est un TAKEAWAY (verdict), pas un descriptif (sujet)
    Exemple ❌ "Ventes par trimestre" / ✅ "Le T3 dépasse la cible pour la 1re fois en 4 ans"
[ ] Connecteurs entre slides d'une même section : "Ainsi que…", "Autre point…", "Enfin…"
[ ] Pas de jargon anglais en position de label de titre
[ ] Slides de reco : titre = constat + direction de solution
[ ] Aucun titre en MAJUSCULES (sauf acronymes ROI, KPI, IA…)
[ ] Aucun tiret cadratin (—) dans aucun titre
```

## D. TYPOGRAPHIE — non négociable (CLAUDE.md §3.2)

```
[ ] Police Poppins partout (jamais d'autre police)
[ ] Variantes Poppins installées sur la machine (ExtraLight, Regular, Medium, SemiBold, Bold)
[ ] Titre principal : Poppins SemiBold 22pt centré bleu Empirik
    → Code : fontFace: "Poppins SemiBold", PAS fontWeight: 600 (PptxGenJS ignore)
[ ] Sur-titre : Poppins ExtraLight 12pt centré orange Empirik
    → Casse normale, PAS de toUpperCase(), PAS de charSpacing
[ ] Sur-titre + titre rapprochés du haut : sur-titre y=0.30, titre y=0.60 (espacement ~10pt)
[ ] Texte courant : Poppins Regular 14pt aligné gauche bleu Empirik
[ ] Chiffres clés : Poppins Bold 48-72pt centré orange Empirik
[ ] Aucun texte < 12pt (sauf footer notes 9-10pt tolérées)

[ ] ENCODAGE UTF-8 strict : accents écrits directement, aucune substitution par ASCII
    → Auto-test : `python -m markitdown build_xxx.pptx | grep -cE "[éèêàùôîûœç]"` doit être > 0
    → Si = 0 sur pres française → l'agent a substitué "chiffrées" par "chiffrees", défaut bloquant
    → Cf PROCESS-ANTI-ERREURS Erreur #12
```

## E. PALETTE COULEURS — non négociable (CLAUDE.md §3.1, §4.8)

```
[ ] 4-5 couleurs Empirik uniquement (bleu #0A3856 / orange #E9540D / jaune #FCC02D / blanc / gris #B0B0B0)
[ ] Vert ad-hoc #10A050 autorisé UNIQUEMENT pour KPI atteint (jamais autre usage)
[ ] AUCUN texte/chiffre en jaune #FCC02D sur fond blanc (contraste insuffisant)
[ ] Jaune utilisé uniquement en accent décoratif (bord de carte, badge avec texte bleu, icône)
[ ] Bleu Empirik joue le rôle de la couleur neutre dominante (équivalent du gris Knaflic)
[ ] Orange Empirik joue le rôle du rouge alerte (pas de rouge en charte)
[ ] Aucune couleur hors charte introduite sans justification écrite
```

## F. CONTRASTE STRATÉGIQUE — non négociable (CLAUDE.md §4.5)

```
[ ] Sur chaque graphique : UN seul élément en orange, le reste en gris/bleu atténué
[ ] Sur chaque slide à N cartes/KPIs : UN seul en orange qui appuie le titre
[ ] Pas de palette multicolore "décorative" sans rôle narratif
[ ] Heatmaps/dégradés : UNE seule couleur en intensité, pas une couleur par valeur (anti-rainbow)
[ ] Test des 3 secondes appliqué slide par slide (CLAUDE.md §4.7) : l'œil va sur l'élément vedette voulu ?
[ ] Test noir & blanc mental : le message principal survit-il sans la couleur ?
```

## G. HIÉRARCHIE TYPOGRAPHIQUE — qualité (CLAUDE.md §4.6)

```
[ ] Gras posé sur 2-4 mots porteurs par bloc (max 25-30% du texte du bloc)
[ ] Orange sur 1-3 mots/chiffres-clés max par bloc
[ ] Italique uniquement pour citations / sources / termes étrangers (jamais déco)
[ ] Souligné uniquement pour liens cliquables réels
[ ] Test scan : lire uniquement le gras + orange → le message principal ressort
```

## H. CHOIX DU GRAPHE — non négociable (CLAUDE.md §4.10)

```
[ ] Chaque graphique est dans la liste des 6 types par défaut (barre horiz/vert/empilée, ligne, slope, dot plot)
    → Sinon : justification écrite dans le rapport
[ ] Aucun graphique 3D (jamais)
[ ] Aucun radar / sankey / treemap / gauge / ribbon (sauf audience spécialiste justifiée)
[ ] Aucun pie chart > 3 parts → remplacé par barre horizontale triée
[ ] Aucun couple de pies côte à côte → remplacé par slope graph
[ ] Aucun tableau dense de chiffres (sauf rapport financier où la valeur exacte est le livrable)
[ ] Évolution temporelle ≥ 4 points → ligne. 2 périodes → slope graph. 3 points → barres verticales.
```

## I. DÉCOMBRER LES GRAPHES — qualité (CLAUDE.md §4.11)

```
[ ] Pas de bordure de graphe, pas de gridlines (ou très atténuées), fond blanc
[ ] Pas de trailing zeros (1000.0 → 1000, 10.00% → 10%)
[ ] Pas de texte diagonal sur axe X (abréger pour rester horizontal)
[ ] Axe Y OU data labels (pas les deux en même temps)
[ ] Pas de décimales inutiles (47,3% → 47% si la précision ne porte pas le message)
[ ] Barres épaisses (espace blanc entre barres ≤ largeur de barre)
[ ] Tri par valeur sur barres horizontales (sauf ordre sémantique)
[ ] Pas de re-titrage interne du graphe (titre de slide centré porte le takeaway)
```

## J. COHÉRENCE DU DECK — non négociable (CLAUDE.md §4.12)

```
[ ] Même police, mêmes tailles par rôle (titre/axe/label/footer) sur TOUT le deck
[ ] Même casing des titres (Sentence case partout)
[ ] Même format de date partout (`Mai 2026` ou `05/2026`, pas alternance)
[ ] Mêmes noms de métriques (jamais "Citations" puis "Mentions" pour la même chose)
[ ] Même palette de couleurs cohérente sur tout le deck
[ ] Mêmes unités et précisions sur grandeurs comparables
[ ] Sur-titre/footer/numéro de page à la même position partout
```

## K. ALIGNEMENT STRICT — non négociable (CLAUDE.md §3.7)

```
[ ] Tous les éléments d'une rangée partagent la même coordonnée Y
[ ] Tous les éléments d'une colonne partagent la même coordonnée X
[ ] Cartes côte à côte : même largeur, hauteur, espacements (calculés, pas "à l'œil")
[ ] Texte aligné à gauche par défaut (titres centrés + chiffres alignés droite OK)
[ ] Nombres dans tableau : alignés à droite, même nombre de décimales sur grandeurs comparables
[ ] Icônes/numéros/badges centrés dans leur conteneur, alignés avec le texte associé
[ ] Sources/footnotes en bas de slide, même position Y partout
```

## L. ESPACE BLANC ET RESPIRATION — non négociable (CLAUDE.md §4.16)

```
[ ] Marges 60px respectées sur toutes les slides (non négociable)
[ ] Densité ≤ 60-70% de la surface utile (tableaux denses = exception explicite documentée)
[ ] Pas plus de 6 bullets par slide
[ ] Si débordement/étouffement → split en 2 slides, jamais réduire marges/police
[ ] Test "retire 20% du contenu" : la slide devient-elle plus claire ?
```

## M. ÉLIMINER LES DISTRACTIONS — qualité (CLAUDE.md §4.9)

```
[ ] Test "et si je l'enlevais ?" passé sur chaque élément visible
[ ] Hiérarchie 3 niveaux respectée : essentiel (orange) / secondaire (gris) / supprimé
[ ] Bordures inutiles supprimées
[ ] Légendes remplaçables par étiquettes directes → remplacées
[ ] Icônes décoratives sans rôle sémantique → supprimées
[ ] Sous-titres redondants avec le titre → supprimés
[ ] Colonnes "info contextuelle" rarement regardées → supprimées
[ ] Ticks d'axes intermédiaires non porteurs → supprimés
```

## N. LEVIERS DE CONTRASTE — qualité (CLAUDE.md §4.13)

```
[ ] Couleur orange sur l'élément vedette uniquement
[ ] 2-3 leviers empilés sur l'élément vedette (couleur + épaisseur + label)
[ ] Pointillé STRICTEMENT réservé à l'incertitude (forecast/cible/projection), JAMAIS pour focaliser
[ ] Marker visible uniquement sur 1-2 points stratégiques (pas tous)
```

## O. ANNOTATIONS / RENOMMAGE BUSINESS — qualité (CLAUDE.md §4.14)

```
[ ] Annotations courtes (2-3 points stratégiques max) sur graphe, pas tous les points
[ ] Catégories techniques renommées en termes business (pas `Treatment_1`, pas `Q1_2025_var_pct`)
[ ] Footnote sous graphe pour définir métriques techniques si nécessaire (1 ligne, gris atténué)
```

## P. EXPLORATOIRE ≠ EXPLICATIF — non négociable (CLAUDE.md §4.15)

```
[ ] Aucun box plot / scatter / courbe de survie / matrice de corrélation dans le livrable final
[ ] Si l'analyse a produit un visu exploratoire → traduit en visuel des 6 types par défaut
    OU remplacé par 2-3 chiffres-clés en bloc qui transportent le même insight
```

## Q. BUILD SEQUENCE — qualité (CLAUDE.md §4.17)

```
[ ] Si graphe à 6+ séries/lignes qui se croisent (spaghetti chart) → build sequence appliquée
[ ] Sur chaque slide de la séquence : UNE série en orange, autres en gris
[ ] Annotation courte (1 ligne) à côté de la série vedette de chaque slide
[ ] Titre takeaway dédié à la série vedette (pas un titre générique répété)
[ ] Cohérence visuelle absolue entre les N slides (mêmes axes/positions/échelles)
```

## R. LOGOS — non négociable (CLAUDE.md §2.6)

```
[ ] Identification pre-flight : TOUTES les marques/outils/sites/concurrents/médias/plateformes cités dans le brief listés
[ ] Pour chaque entrée de la liste, logo officiel récupéré et intégré dans le deck
[ ] Logo Empirik UNIQUEMENT sur slide cover (jamais ailleurs)
[ ] Logos téléchargés via scripts/fetch_logos.py (4 couches : simpleicons → Wikipedia → scraping HTML multi-pages → brandfetch.com)
    → Mode --auto recommandé : essaie les 4 couches en cascade jusqu'à trouver
[ ] PNG transparents 30-60px de haut, version adaptée au fond (couleur sur blanc, blanc sur bleu Empirik)

[ ] QA VISUELLE PRE-FLIGHT de chaque logo avant intégration via slide.addImage()
    → Ouvrir CHAQUE PNG dans le Read tool (Claude multimodal)
    → Vérifier (a) marque correcte (pas placeholder texte / pas autre marque)
                (b) version actuelle (pas obsolète)
                (c) format exploitable (vrai PNG ≥ 1 KB, fond transparent)
    → Si échec sur un critère → re-fetch AVANT première ligne addImage()
    → Cf PROCESS-ANTI-ERREURS Erreur #13

[ ] REFRESH FORCÉ des logos LLM en début de session (PNG cache > 3 mois souvent obsolète)
    → ChatGPT/OpenAI, Claude/Anthropic, Gemini/Google AI, Perplexity, Mistral, Copilot, Grok, DeepSeek, Llama, Cohere
    → Commande type : `python scripts/fetch_logos.py --auto "openai=chatgpt" "anthropic=claude" "googlegemini=gemini" ...`
    → Suivi de la QA visuelle pre-flight ci-dessus
[ ] Aucun logo abandonné silencieusement
    → Si une marque a posé problème, les 10 méthodes d'escalade documentées ci-dessous ont été tentées
    avant d'envisager une absence de logo (et l'absence est documentée dans le rapport, pas omise)
[ ] Pour les marques résistantes, méthodes tentées documentées :
    [ ] (1) Crawl pages /press, /press-kit, /media, /brand, /brand-assets, /about du site officiel
    [ ] (2) Inspection HTML home : <img class="logo">, <svg id="logo">, contenu <header>/<nav>/<footer>
    [ ] (3) CSS background-image (parsing des url(...) dans les feuilles de style)
    [ ] (4) Wikipedia avec variantes de nom (officiel, sans suffixe, marque parente si filiale)
    [ ] (5) Wikipedia EN si la version FR n'a rien
    [ ] (6) Agrégateurs tiers : brandfetch.com, logo.wine, 1000logos.net, worldvectorlogo.com
    [ ] (7) Google Images / DuckDuckGo Images avec recherche "marque logo png transparent"
    [ ] (8) Bypass 403 Forbidden : User-Agent Mozilla Firefox + Referer google
    [ ] (9) Bypass SSL fail : ssl._create_unverified_context()
    [ ] (10) Wayback Machine si site mort/bloqué
[ ] Rappel : "logo introuvable" n'est PAS une issue acceptable sans documentation des 10 méthodes ci-dessus
```

## S. SOURCES ET RÉFÉRENCES — non négociable (CLAUDE.md §2.4, §2.5)

```
[ ] Chaque slide data : mention "Source : <outil> · Période : <dates>" en footer
[ ] Multi-sources : toutes listées
[ ] URLs externes cliquables (hyperlink dans PptxGenJS, pas juste texte)
[ ] Sources externes (Wikipedia, dashboards, articles) avec lien cliquable
```

## T. CONTENU — non négociable (CLAUDE.md §2.2, §2.3, §2.8, §2.9)

```
[ ] Voix "vous" (client) partout, jamais "nous" (agence)
[ ] Concepts techniques expliqués visuellement (pas de jargon supposé acquis)
[ ] Aucun tiret cadratin — dans aucun titre/contenu (vérifier grep -c "—" → 0)
[ ] Accents diacritiques tous en place (relecture orthographique systématique)
[ ] Aucune invention de data (en cas d'erreur, signaler explicitement)
[ ] Si pres GEO : préambule volatilité posé
```

## U. EXHAUSTIVITÉ vs SOURCE — non négociable

```
[ ] Mapping section par section : PDF source ↔ slides générées documenté
[ ] Tous les chiffres-clés du source intégrés (aucune omission silencieuse)
[ ] Tous les tableaux source restitués (au besoin sur plusieurs slides, jamais tronqués)
[ ] Si une omission est faite → justification écrite dans le rapport (raison + arbitrage)
[ ] Vérification d'exhaustivité lancée par sous-agent indépendant
```

## V. PptxGenJS — pièges techniques (PROCESS-ANTI-ERREURS Erreurs #1-7)

```
[ ] Aucun .toUpperCase() dans le script de génération
[ ] Aucun charSpacing > 0 sur les eyebrows / sur-titres
[ ] fontFace explicite pour les variants ("Poppins SemiBold", "Poppins ExtraLight", "Poppins Bold")
    → Jamais fontWeight: N (silencieusement ignoré par PptxGenJS)
[ ] grep "color: YELLOW" sur le script → vérifier chaque occurrence (jaune sur blanc INTERDIT pour texte)
[ ] grep -c "—" sur le script → DOIT renvoyer 0 (aucun tiret cadratin)
[ ] Aucune réutilisation d'objet d'options entre plusieurs addText / addShape (PptxGenJS les mute)
[ ] Pas d'ombres avec offset négatif ni couleur 8-char hex
```

## W. QA VISUELLE — non négociable

```
[ ] PPTX généré → converti en PDF (LibreOffice)
[ ] PDF → JPG via PyMuPDF (1 image par slide)
[ ] CHAQUE slide JPG inspectée visuellement (pas seulement 2-3)
[ ] Test des 3 secondes effectué slide par slide
[ ] Test bi-directionnel titre ↔ contenu effectué slide par slide
[ ] Aucun débordement de cadre / chevauchement
[ ] Footer + numéro de page sur chaque slide standard (sauf cover et CTA)
[ ] Slide cover et CTA exempts de sur-titre / footer (exception)
```

## Y. ANTI-FAILLES HISTORIQUES — non négociable (17 failles documentées sur générations précédentes)

```
[ ] Étape 1 — Rapport de lecture des guides produit (3-5 bullets par fichier) AVANT étape 2
[ ] Tous les chiffres / sources du brouillon listés dans Artifact 1 (tableau couverture)
[ ] Si > 20% des chiffres omis : alerte explicite à l'utilisateur AVANT validation (pas après)
[ ] Étape 4 — Avocat du diable §1.3 appliqué : tableau "preuve / limites / robustesse" produit
[ ] Chiffres "à vérifier" du brouillon JAMAIS utilisés comme verdict, signalés à l'utilisateur
[ ] N sections détectées → N slides "Ce qu'il faut retenir" planifiées (1 par section)
[ ] Cartographie des voies dataviz produite (Artifact 4) : type + voie + justification par graphe
[ ] Pas plus de 70% du même type de graphe dans le deck (sinon alerte rouge, repenser ≥ 30%)
[ ] Au moins 1 slide question client par section (ou justification écrite si pas pertinent)
[ ] Test §2.7 narratif explicitement fait : lire les titres dans l'ordre, écrire le verdict
[ ] Test §2.7 bi-directionnel fait slide par slide, résultat écrit
[ ] Test §4.7 des 3 secondes fait slide par slide, élément vedette identifié pour chaque
[ ] Voix "vous" appliquée 100% (pas 50%, pas "le propriétaire" / "le client")
[ ] Slide cover conforme au template §3.5 (logo Empirik + logo client si pres client + ligne + image + titre orange + motif jaune)
    → Logo Empirik OBLIGATOIRE par défaut, jamais demander "perso ou Empirik" à l'utilisateur
    → Suppression du logo uniquement si l'utilisateur l'a explicitement demandé, sinon = appliquer le template intégral
[ ] Bullets niveau 1 en orange #E9540D (cercles pleins), pas en bleu (couleur héritée du texte)
[ ] Build sequence §4.17 envisagée pour chaque viz multi-catégories (3+) avant de figer un seul graphe
[ ] URLs sources cliquables dans le PPTX (hyperlink, pas juste texte)
[ ] Logos d'institutions / journaux / études cités intégrés (pas seulement marques tech)
[ ] markitdown exécuté sur le .pptx final pour vérifier le texte extrait
[ ] Sous-agent d'exhaustivité §7.3 lancé OBLIGATOIREMENT (pas optionnel) avec verdict joint
[ ] Slides chapitres / section dividers enrichies visuellement (pas juste fond bleu + texte)
[ ] Slides chiffre clé seul (sans graphe) : ajouter au moins un élément visuel d'accompagnement
    (icône, mini-visualisation, image conceptuelle)

POUR CHAQUE GRAPHE — Test d'adéquation aux valeurs réelles (CLAUDE.md §4.10, Erreur #8)
[ ] Valeurs numériques exactes écrites (pas "comparaison X vs Y" mais "30 vs 140")
[ ] Ratio calculé : si > 3 ou si une valeur ~0 → format dumbbell/slope/dot inadapté, repenser
[ ] Test "sans annotation textuelle" : le graphe transmet-il encore le message principal ?
    Si NON → format mauvais, changer (probablement vers Voie 4 chiffres-clés)
[ ] Test "3 secondes au format" appliqué au plan (étape 4), pas seulement à la QA finale

POUR CHAQUE GRAPHE — Fourchettes ≠ écarts (CLAUDE.md §4.10, Erreur #9)
[ ] Ne pas utiliser dot plot avec fourchettes pour montrer un écart entre 2 entités
[ ] Écart entre 2 entités → 2 chiffres-clés + écart en orange, OU bar chart à 2 barres
[ ] Variabilité individuelle ≠ écart entre entités, ne JAMAIS mélanger sur le même graphe

VOIE 3 (Python matplotlib → PNG) — règles spécifiques
[ ] Le PNG ne contient AUCUN texte (juste lignes, points, barres, gradients)
    → Tous les libellés ajoutés via PptxGenJS addText() en superposition (sinon non éditables dans Google Slides)
[ ] Fichier JSON sidecar (overlays.json) avec coordonnées % et textes produit par generate_chart.py
[ ] PNG ouvert dans le Read tool après génération pour QA de centrage (Erreur #10)
[ ] Si décalage : ajustement xlim/ylim matplotlib OU crop PIL OU compensation x dans addImage()
```

## Z. CONFORMITÉ DUARTE — non négociable (anti-pres-100%-Logos)

> Bloc créé suite à l'audit "Angora vs Sphinx v1" qui a obtenu 100% sur la rigueur factuelle mais 55% sur Duarte (zéro S.T.A.R., chiffres froids, structure 100% piliers sans sparkline, big idea sèche). Tant que ce bloc est respecté, la pres résonne au-delà du rapport d'audit.

```
[ ] Artifact 6 "Plan émotionnel" produit à l'étape 4 (les 6 éléments documentés AVANT le go final)

[ ] S.T.A.R. moment(s) identifiable(s) dans le deck
    → Cite la ou les slide(s) précises
    → Type : sound bite / stat choquante humanisée / visuel évocateur / dramatisation / mini-histoire
    → Au moins 1 S.T.A.R. obligatoire (idéalement 2-3 sur le deck)

[ ] Humanisation des chiffres-clés (top 3 chiffres principaux du deck)
    → Au moins 2 chiffres sur 3 ont une analogie familière
    → Ex : "11 700 €" → "le prix d'un voyage de noces aux Maldives"
    → Ex : "33-50% HCM" → "1 Sphinx sur 3 minimum aura un trouble cardiaque"
    → Ex : "+37% cortisol" → "l'équivalent stress d'une séance de yoga"

[ ] Sparkline (alternance "ce qui est" ↔ "ce qui pourrait être")
    → 4 alternances minimum dans le deck (pas de structure 100% blocs thématiques)
    → Liste explicite des slides "ce qui est" vs "ce qui pourrait être"

[ ] Slide "nouvelle félicité" présente entre la reco et le CTA final
    → Projection narrative du futur transformé (pas une liste de bénéfices en cartes)
    → Ex : "Imaginez, dans X mois, votre [audience]..."

[ ] Slide nouvelle félicité (et tout paragraphe narratif) STRUCTURÉE en 3 moments visuels si > 60 mots
    → Pas de pavé monobloc indifférencié (ton oraliste mal traduit à l'écrit)
    → Structure : moment 1 ouverture (1 phrase) + moment 2 pivot avec ancrage chiffré (1 phrase + 3-4 bullets)
                  + moment 3 résolution émotionnelle (1 phrase)
    → Espaces blancs entre les moments, lisible en 5 secondes
    → Cf CLAUDE.md §5.6

[ ] Big idea formulée avec ENJEUX gain ET perte (pas juste verdict sec)
    → ❌ "L'Angora l'emporte sur le Sphinx"
    → ✅ "Choisir l'Angora, c'est gagner 3 ans de vie animale ET économiser 7 000 €, en évitant 50% de risque cardiaque"

[ ] Métaphore / analogie centrale présente et filée dans le deck
    → Une seule métaphore, mentionnée dès la cover ou la synthèse, rappelée 2-3 fois

[ ] Ratio Logos / Pathos / Ethos respecte la cible §5.5
    → Logos 50-65% / Pathos 20-30% min / Ethos 10-15%
    → Pas 95% Logos comme défaut "rapport McKinsey"

[ ] Audience-héros nommée précisément et incarnée
    → Pas "les stakeholders" mais "le futur propriétaire qui hésite", "le décideur marketing qui doit choisir entre…"
    → L'audience-héros doit être présente dans le texte du deck (pronoms "vous", projection à sa place)

[ ] Proportions actes Duarte respectées : ~10/80/10% (±10pts tolérance)
    → Acte 1 (setup, what is) : ~10%
    → Acte 2 (contraste, sparkline) : ~80%
    → Acte 3 (nouvelle félicité + CTA) : ~10%
    → Si Acte 1 > 25% ou Acte 2 < 60% → déséquilibre à corriger

[ ] Sous-agent #2 "Audit Duarte" lancé en étape 7 (non optionnel, distinct du sous-agent factuel)
    → Verdict Duarte X/9 documenté dans le rapport QA
```

## AA. SLIDE COVER §3.5 — non négociable (décomposé item par item)

> Bloc créé suite à l'audit "Angora vs Sphinx v2" : la cover ne respectait que partiellement le template §3.5 (logo Empirik supprimé unilatéralement par l'agent, sans demande utilisateur). Chaque élément du template est désormais un item séparé pour empêcher la suppression silencieuse.

```
[ ] Logo Empirik présent en haut à gauche (taille ~1.5" × 0.5", obligatoire et non négociable
    → Preuve : "slide 1, coin haut-gauche, x=0.4 y=0.3 w=1.5 h=0.5"
[ ] Logo client présent en haut à droite SI pres pour un client (sinon laisser vide à droite)
    → Preuve : "slide 1, coin haut-droit"
[ ] Ligne horizontale fine de séparation sous les logos (gris #E5E5E5, hauteur ~0.015")
    → Preuve : "slide 1, y=0.95"
[ ] Image d'ambiance côté gauche (~50% largeur, hauteur pleine, bords carrés)
    → Preuve : "addImage path=assets/cover-xxx.png x=0.4 y=1.15 w=4.6 h=4.0"
[ ] Titre principal côté droit : Poppins Bold 48-60pt, orange #E9540D, aligné gauche, 1-2 lignes
    → Preuve : "ligne L du script : fontSize 48-60, color E9540D, fontFace 'Poppins Bold'"
[ ] Petit trait orange horizontal sous le titre (largeur ~0.6", épaisseur ~0.05")
    → Preuve : "ligne L : shape rect orange sous titre"
[ ] Sous-titre Poppins Regular ~20pt, bleu #0A3856
    → Preuve : "ligne L : fontSize 20, color 0A3856, fontFace 'Poppins'"
[ ] Date Poppins Bold ~20pt, bleu #0A3856 (format "Mai 2026", pas "05/2026")
    → Preuve : "ligne L : fontSize 20, bold true, format date conforme"
[ ] Motif décoratif jaune #FCC02D en bas (petite grille de carrés, entre image et bloc texte)
    → Preuve : "boucle for shapes jaune visible slide 1"
```

## BB. VOIX "VOUS" QUANTIFIÉE — non négociable (≥ 70% des slides standard)

> Bloc créé suite au bug "Angora v2" : 4 slides sur 24 contenaient "vous" mais coché ✅ "voix vous appliquée partout". Sans seuil chiffré + auto-test, la règle est qualitative et permet le glissement silencieux.

```
[ ] Comptage explicite des slides standard (hors cover, section dividers, citation pure, CTA)
    → Preuve : "Total slides standard = X (= total slides - cover - N dividers - CTA)"

[ ] Pour chaque slide standard, présence d'au moins UNE occurrence de "vous" / "votre" / "vos"
    dans le titre OU le corps
    → Preuve : tableau exhaustif slide N → contient "vous" ? oui/non

[ ] Comptage final : N slides avec "vous" / Total slides standard = X%
    → Preuve atomique attendue : "grep -ciE '\\b(vous|votre|vos)\\b' build_xxx.js → résultat"
    → Comparer au nombre de slides standard

[ ] Seuil minimal respecté : X% ≥ 70%
    → Si < 70% → ❌ obligatoire, à corriger AVANT livraison
    → Reformulation de la 3e personne ("le client", "le propriétaire") vers la 2e ("vous")

[ ] Aucune occurrence de "nous" en dehors de "Nous recommandons" sur la slide reco unique finale
    → Preuve : grep -ciE '\\bnous\\b' build_xxx.js → comptage
    → Préférer "Adoptez..." / "Choisissez..." même sur la slide reco

[ ] L'audience-héros est nommée dans la pres (cf §3.5 Artifact 6 g)
    → Preuve : citation slide précise qui nomme la persona
```

## CC. ASSETS VISUELS DESIGN_EMPIRIK — non négociable (cover, sections, closing)

> Bloc créé suite au bug "Angora v2" : section dividers limités à "fond bleu + texte" sans image conceptuelle. DESIGN_EMPIRIK.md liste 7 types d'assets visuels obligatoires — sans bloc dédié, ils étaient zappés silencieusement.

```
[ ] Slide cover : image générée via scripts/generate_image.py --type cover OU image fournie
    → Preuve : "addImage path=assets/cover-xxx.png présent slide 1"
    → ❌ si pas d'image (juste shapes / fond uni)

[ ] Slide(s) de section divider : image conceptuelle OU élément visuel fort (pas juste fond bleu + texte)
    → Preuve : pour chaque divider, citer l'élément visuel ou l'image utilisée
    → ❌ si tous les dividers sont fond bleu + texte uniquement

[ ] Slide CTA / closing : élément visuel fort (poster pattern, fond gradient, image conceptuelle)
    → Preuve : description visuelle de la slide finale
    → ❌ si juste texte + bouton sans élément visuel marquant

[ ] Slides "chiffre clé seul" enrichies (cf bloc Y) : icône / mini-viz / image conceptuelle
    en accompagnement du chiffre
    → Preuve : pour chaque slide chiffre clé, citer l'élément d'accompagnement

[ ] Aucune slide texte-only (règle §3.6) : chaque slide a au moins UN élément visuel
    → Preuve : tableau exhaustif slide N → élément visuel présent ? quel type ?

[ ] Couleurs des assets respectent palette Empirik (cf §3.1) — pas de couleur hors charte
    sans justification métier écrite
    → Preuve : palette utilisée listée par asset
```

## X. LIVRAISON

```
[ ] Fichier .pptx final dans le dossier projet
[ ] Rapport QA (ce fichier) rempli et joint
[ ] PDF de QA généré et joint
[ ] Score global : __% ✅
[ ] Liste des ❌ avec justification : <ci-dessous>
[ ] Arbitrage utilisateur sur les ❌ restants : <demandé / validé / en attente>
```

---

## Rapport des défauts résiduels (à remplir)

| # | Catégorie | Item | Pourquoi non appliqué | Impact | Arbitrage utilisateur |
|---|-----------|------|----------------------|--------|----------------------|
|   |           |      |                      |        |                      |

---

## Score final

- Blocs non négociables (A, B, C, D, E, F, H, J, K, L, P, R, S, T, U, W, Y, Z, AA, BB, CC) : **__ / __ ✅**
- Blocs qualité (G, I, M, N, O, Q, V) : **__ / __ ✅**
- Nombre de ✅ avec preuve concrète : **__ / __ ✅** (cibler 100%)
- Nombre de ❓ "non vérifié" : **__** (cibler 0)
- **Score global** : **__%**

**Livraison validée** : ☐ Oui · ☐ Non (raison : ____________)

---

*Ce rapport est obligatoire. Pas de livraison sans rapport rempli. L'objectif n'est pas le 100% systématique, mais la **traçabilité explicite** de l'application de chaque règle. Un ❌ documenté et arbitré vaut mieux qu'un ❌ silencieux.*

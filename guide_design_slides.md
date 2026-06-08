# Guide de Design des Slides
## Règles Visuelles et Spécifications Techniques

> Ce guide définit les règles strictes de design à appliquer pour toutes les slides générées. Respecter ces spécifications garantit une cohérence visuelle professionnelle.

---

## 🎨 PALETTE DE COULEURS

### Couleurs Principales

```
┌─────────────────────────────────────────────────────────────┐
│                    PALETTE OFFICIELLE                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ██████████  BLEU PRINCIPAL          #0A3856                │
│              → Titres                                        │
│              → Texte courant                                 │
│              → Éléments importants                           │
│                                                              │
│  ██████████  ORANGE ACCENT           #E9540D                │
│              → Mise en valeur                                │
│              → Call-to-action                                │
│              → Points clés                                   │
│                                                              │
│  ██████████  JAUNE ACCENT            #FCC02D                │
│              → Highlights                                    │
│              → Éléments secondaires                          │
│              → Icônes et décorations                         │
│                                                              │
│  ██████████  BLANC FOND              #FFFFFF                │
│              → Arrière-plan de toutes les slides             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Utilisation des Couleurs

```yaml
HIÉRARCHIE VISUELLE:

Niveau 1 - Information Principale:
  couleur: "#0A3856"
  usage: "Titres, texte principal, messages clés"

Niveau 2 - Accent Fort:
  couleur: "#E9540D"
  usage: "Mots à souligner, CTA, chiffres importants, alertes"

Niveau 3 - Accent Léger:
  couleur: "#FCC02D"
  usage: "Sous-catégories, icônes, séparateurs, fonds légers"

Niveau 4 - Fond:
  couleur: "#FFFFFF"
  usage: "Arrière-plan uniquement, jamais de texte blanc"
```

### Règles de Combinaison

```
COMBINAISONS AUTORISÉES:
✅ Texte #0A3856 sur fond #FFFFFF (standard)
✅ Texte #FFFFFF sur fond #0A3856 (inversé pour accent)
✅ Texte #FFFFFF sur fond #E9540D (CTA, boutons)
✅ Texte #0A3856 sur fond #FCC02D (highlight léger)
✅ Icône #E9540D sur fond #FFFFFF
✅ Icône #FCC02D sur fond #0A3856

COMBINAISONS INTERDITES:
❌ Texte #FCC02D sur fond #FFFFFF (contraste insuffisant)
❌ Texte #E9540D sur fond #FCC02D (conflit de couleurs)
❌ Texte #0A3856 sur fond #E9540D (lisibilité réduite)
```

---

## 📝 TYPOGRAPHIE

### Police Principale : Poppins

```
┌─────────────────────────────────────────────────────────────┐
│                     SYSTÈME TYPOGRAPHIQUE                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  TITRE DE SLIDE                                              │
│  ─────────────────────────────────────────────────          │
│  Police    : Poppins                                         │
│  Taille    : 22pt                                            │
│  Graisse   : SemiBold (600) UNIQUEMENT, jamais Bold         │
│  Couleur   : #0A3856                                         │
│  Alignement: Centré                                          │
│  Casse     : Première lettre en majuscule                    │
│                                                              │
│  TEXTE COURANT                                               │
│  ─────────────────────────────────────────────────          │
│  Police    : Poppins                                         │
│  Taille    : 14pt                                            │
│  Graisse   : Regular (400)                                   │
│  Couleur   : #0A3856                                         │
│  Alignement: Gauche (par défaut) ou Centré                   │
│  Interligne: 1.5                                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Hiérarchie Typographique Complète

| Élément | Police | Taille | Graisse | Couleur | Alignement |
|---------|--------|--------|---------|---------|------------|
| **Sur-titre de section** | Poppins | **12pt** | **ExtraLight (200)** | **#E9540D** | aligné avec le titre |
| Titre principal | Poppins | 22pt | **SemiBold (600) uniquement — JAMAIS Bold** | #0A3856 | Centré |
| Sous-titre | Poppins | 18pt | Medium (500) | #0A3856 | Centré |
| Texte courant | Poppins | 14pt | Regular (400) | #0A3856 | Gauche |
| Légende/Note | Poppins | 12pt | Regular (400) | #0A3856 | Gauche |
| Chiffre clé | Poppins | 48-72pt | Bold (700) | #E9540D | Centré |
| Citation | Poppins | 16pt | Italic | #0A3856 | Centré |
| Label bouton | Poppins | 14pt | SemiBold (600) | #FFFFFF | Centré |

> **🔒 RÈGLE TITRE PRINCIPAL — STRICT** : Poppins SemiBold uniquement. NE PAS appliquer `bold: true` en plus dans PptxGenJS. Le Bold est réservé aux chiffres clés et au titre de la slide de couverture.

> **🔒 RÈGLE SUR-TITRE — STRICT** : Sur **toutes les slides standard** (sauf slide de couverture, slides chapitre/section et slide CTA finale), ajouter au-dessus du titre principal un **sur-titre = nom de la section/chapitre courant**. Style : Poppins ExtraLight 12pt orange #E9540D (fallback : Poppins Light / Poppins Thin si ExtraLight indisponible), **CENTRÉ horizontalement**, **directement collé au titre principal (espacement court, ~6-10pt)**. Sur-titre + titre forment un ensemble visuel compact et centré.
>
> **Layout de référence (screen utilisateur 2026-05-11) :**
> ```
>                  [sur-titre orange ExtraLight 12pt — CENTRÉ]
>             [TITRE PRINCIPAL bleu SemiBold 22pt — CENTRÉ]
> ```
> Objectif : permettre au lecteur de toujours savoir dans quelle section il se trouve.

### Règles Typographiques

```yaml
ESPACEMENT:
  entre_titre_et_contenu: "40px minimum"
  entre_paragraphes: "20px"
  entre_bullet_points: "12px"
  marge_laterale: "60px minimum de chaque côté"

LONGUEUR DE LIGNE:
  maximum: "65-75 caractères par ligne"
  regle: "Si plus long, diviser en plusieurs lignes ou réduire le texte"

MAJUSCULES:
  titres: "Première lettre uniquement"
  jamais: "Tout en majuscules pour du texte long"
  exception: "Acronymes (ROI, KPI, etc.)"

PONCTUATION:
  bullet_points: "Pas de point final si phrase incomplète"
  titres: "Pas de point final"
```

---

## 📐 MISE EN PAGE

### Grille de Base

```
┌─────────────────────────────────────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│ ░  ┌─────────────────────────────────────────────────┐  ░░ │
│ ░  │                                                 │  ░░ │
│ ░  │              ZONE DE TITRE                      │  ░░ │
│ ░  │              (Centré, 22pt)                     │  ░░ │
│ ░  │                                                 │  ░░ │
│ ░  ├─────────────────────────────────────────────────┤  ░░ │
│ ░  │                                                 │  ░░ │
│ ░  │                                                 │  ░░ │
│ ░  │              ZONE DE CONTENU                    │  ░░ │
│ ░  │              (14pt, flexible)                   │  ░░ │
│ ░  │                                                 │  ░░ │
│ ░  │                                                 │  ░░ │
│ ░  │                                                 │  ░░ │
│ ░  └─────────────────────────────────────────────────┘  ░░ │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
└─────────────────────────────────────────────────────────────┘
  ░ = Marges (minimum 60px)
```

### Zones et Marges

```yaml
MARGES OBLIGATOIRES:
  haut: "60px"
  bas: "60px"
  gauche: "60px"
  droite: "60px"
  note: "Aucun élément ne doit toucher les bords"

ZONE DE TITRE:
  position: "Haut de la slide"
  hauteur: "15-20% de la slide"
  centrage: "Horizontal et vertical dans sa zone"

ZONE DE CONTENU:
  position: "Sous le titre"
  hauteur: "70-75% de la slide"
  padding_interne: "20px minimum"
```

### Alignements

```
RÈGLES D'ALIGNEMENT:

┌─ TITRES ──────────────────────────────────────────┐
│  Toujours centré horizontalement                  │
│  Position verticale: haut de slide                │
└───────────────────────────────────────────────────┘

┌─ TEXTE COURANT ───────────────────────────────────┐
│  Par défaut: aligné à gauche                      │
│  Exception: texte court centré si seul            │
└───────────────────────────────────────────────────┘

┌─ IMAGES ──────────────────────────────────────────┐
│  Centrées si seules                               │
│  Alignées avec le texte si accompagnées           │
└───────────────────────────────────────────────────┘

┌─ ÉLÉMENTS MULTIPLES ──────────────────────────────┐
│  Distribués uniformément                          │
│  Espacements égaux entre éléments                 │
└───────────────────────────────────────────────────┘
```

---

## 🏷️ TITRES DE SLIDES — RÈGLES DE RÉDACTION (CRITIQUE)

> **Le titre est la phrase la plus importante de chaque slide.** Lu seul, il doit suffire à comprendre l'argument. Lus en séquence, les titres doivent raconter toute l'histoire de la présentation.

### Principe fondamental : CONSTAT CONCRET, PAS ÉTIQUETTE

Chaque titre doit être une **phrase complète qui pose un diagnostic, une conviction ou une recommandation** — jamais un simple label de catégorie.

```
MAUVAIS (label / étiquette) :
❌ "Score de qualité de la page"
❌ "Score sémantique : un déficit de couverture"
❌ "Intentions de recherche : 1 seule complétée sur 7"
❌ "Les 3 critères les plus faibles : actions prioritaires"
❌ "Above-the-fold : le premier écran est décisif"

BON (constat / conviction / recommandation) :
✅ "Un score insuffisant pour atteindre une top position & satisfaire son lecteur"
✅ "Le champ lexical attendu par Google n'est pas suffisamment présent, la page n'est pas 'optimisée sémantiquement'"
✅ "Le contenu répond à une seule intention de recherche sur les 7 recommandées"
✅ "L'expertise, l'originalité et l'effort de valeur ajoutée doivent être retravaillés en priorité"
✅ "Le premier écran est décisif, un résumé permet tout de suite de capter le lecteur"
```

### Règle des connecteurs : créer un fil narratif entre slides

Au sein d'une même section, les titres doivent s'enchaîner avec des **mots de liaison** qui créent une progression fluide :

```
CONNECTEURS À UTILISER :
→ "Ainsi que..."     — pour ajouter un point lié au précédent
→ "Autre point, ..." — pour signaler un constat supplémentaire
→ "Enfin, ..."       — pour signaler le dernier point d'une section
→ "De plus, ..."     — pour renforcer l'argument
→ "En conséquence, ..." — pour tirer une conclusion

EXEMPLE D'ENCHAÎNEMENT :
  Slide 5 : "L'expertise, l'originalité et l'effort de valeur ajoutée doivent être retravaillés en priorité"
  Slide 6 : "Ainsi que la qualité rédactionnelle qui doit être améliorée"
  Slide 7 : "Proposer du contenu unique non copiable fera la différence à l'ère du contenu IA en masse"
```

### Nommer les choses concrètement

Ne jamais utiliser de catégories vagues quand on peut nommer les éléments précis :

```
MAUVAIS :
❌ "Les 3 critères les plus faibles"
❌ "2 critères à améliorer"
❌ "Plusieurs problèmes identifiés"

BON :
✅ "L'expertise, l'originalité et l'effort de valeur ajoutée doivent être retravaillés"
✅ "La qualité rédactionnelle doit être améliorée"
✅ "Le score sémantique est à 32%, les intentions couvertes à 1 sur 7"
```

### Pas de jargon anglais en position de label

Le client ne connaît pas le vocabulaire technique anglais. Le jargon peut apparaître entre guillemets dans le corps du titre, mais jamais comme label d'accroche :

```
MAUVAIS :
❌ "Above-the-fold : le premier écran est décisif"
❌ "E-E-A-T : incarner l'expertise"
❌ "Information Gain : se différencier"

BON :
✅ "Le premier écran est décisif, un résumé permet tout de suite de capter le lecteur"
✅ "Signature de l'auteur, pour incarner l'expertise et renforcer l'E-E-A-T"
✅ "Proposer du contenu unique non copiable fera la différence à l'ère du contenu IA en masse"
```

### Titre = constat + solution (pour les slides de recommandation)

Sur les slides qui proposent une action, le titre doit idéalement contenir à la fois le constat et la direction de la solution :

```
EXEMPLES :
✅ "Le premier écran est décisif, un résumé permet tout de suite de capter le lecteur"
     [constat]                     [solution]

✅ "Corps de l'article, casser la monotonie en intégrant des blocs, infographies..."
     [zone concernée]              [action concrète]

✅ "Appels à l'action, à adapter au stade (funnel) du lecteur"
     [élément]                     [recommandation]
```

### Types de titres selon le type de slide

```yaml
SLIDE DE DIAGNOSTIC:
  format: "Constat négatif concret"
  exemple: "Un score insuffisant pour atteindre une top position & satisfaire son lecteur"

SLIDE D'ANALYSE:
  format: "Ce qui ne va pas + pourquoi c'est un problème"
  exemple: "Le champ lexical attendu par Google n'est pas suffisamment présent"

SLIDE DE RECOMMANDATION:
  format: "Action à mener + bénéfice attendu"
  exemple: "Proposer du contenu unique non copiable fera la différence à l'ère du contenu IA en masse"

SLIDE PÉDAGOGIQUE:
  format: "Question que se pose naturellement l'audience"
  exemple: "Qu'entend-t-on par page 'optimisée sémantiquement' ?"

SLIDE AVANT/APRÈS (UX):
  format: "Zone + recommandation d'amélioration"
  exemple: "Signature de l'auteur, pour incarner l'expertise et renforcer l'E-E-A-T"

SLIDE DE SYNTHÈSE:
  format: "Synthèse : [nombre] + [nature des actions] + [objectif]"
  exemple: "Synthèse : 3 types d'optimisations pour un contenu qui performe"
```

### Test de validation des titres

Avant de finaliser, vérifier :

```
□ Si je lis UNIQUEMENT les titres dans l'ordre, est-ce que je comprends tout l'argumentaire ?
□ Chaque titre fait-il un constat concret (pas un label générique) ?
□ Les titres au sein d'une section s'enchaînent-ils avec des connecteurs ?
□ Les termes techniques anglais sont-ils évités en position de label ?
□ Les éléments sont-ils nommés précisément (pas "3 critères" mais lesquels) ?
□ Les slides de recommandation combinent-elles constat + solution dans le titre ?
```

---

## 🖼️ TYPES DE SLIDES

### 1. Slide de Titre

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                    TITRE PRINCIPAL                          │
│                    (Poppins 22pt SemiBold #0A3856)          │
│                                                             │
│                    Sous-titre optionnel                     │
│                    (Poppins 18pt Medium #0A3856)            │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
Fond: #FFFFFF
```

### 2. Slide de Contenu Standard

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    Titre de la slide                        │
│                    ─────────────────                        │
│                                                             │
│    • Premier point à développer                             │
│                                                             │
│    • Deuxième point à développer                            │
│                                                             │
│    • Troisième point à développer                           │
│                                                             │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
Titre: Poppins 22pt SemiBold #0A3856 centré
Bullets: Poppins 14pt Regular #0A3856
Puce: ● en #E9540D ou #FCC02D
```

### 3. Slide Chiffre Clé

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    Titre contextuel                         │
│                                                             │
│                                                             │
│                         73%                                 │
│                    (Poppins 72pt Bold #E9540D)              │
│                                                             │
│                 des entreprises concernées                  │
│                    (Poppins 14pt #0A3856)                   │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 4. Slide Citation

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                          ❝                                  │
│                                                             │
│              "La citation va ici, elle est                  │
│               centrée et en italique."                      │
│                                                             │
│                          ❞                                  │
│                                                             │
│                    — Auteur de la citation                  │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
Citation: Poppins 16pt Italic #0A3856
Auteur: Poppins 14pt Regular #0A3856
Guillemets: #FCC02D ou #E9540D
```

### 5. Slide Deux Colonnes

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    Titre de la slide                        │
│                                                             │
│    ┌───────────────────┐    ┌───────────────────┐          │
│    │                   │    │                   │          │
│    │   COLONNE 1       │    │   COLONNE 2       │          │
│    │                   │    │                   │          │
│    │   Contenu ici     │    │   Contenu ici     │          │
│    │                   │    │                   │          │
│    │                   │    │                   │          │
│    └───────────────────┘    └───────────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
Gouttière entre colonnes: 40px minimum
Colonnes: largeur égale
```

### 6. Slide Image + Texte

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                    Titre de la slide                        │
│                                                             │
│    ┌───────────────────┐                                   │
│    │                   │    Texte explicatif               │
│    │                   │    qui accompagne                 │
│    │     IMAGE         │    l'image et donne               │
│    │                   │    du contexte.                   │
│    │                   │                                   │
│    └───────────────────┘                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
Ratio image: max 50% de la largeur
Image: coins arrondis optionnels (8px)
```

### 7. Slide Call-to-Action

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                    Titre engageant                          │
│                                                             │
│                                                             │
│              ┌─────────────────────────┐                   │
│              │   VOTRE ACTION ICI      │                   │
│              │   (Bouton #E9540D)      │                   │
│              └─────────────────────────┘                   │
│                                                             │
│                    Texte de support                         │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
Bouton: fond #E9540D, texte #FFFFFF, Poppins 14pt SemiBold
Coins du bouton: arrondis 8px
```

---

## ✨ ÉLÉMENTS VISUELS

### Puces et Listes

```yaml
STYLE DES PUCES:

Niveau 1:
  symbole: "●" (cercle plein)
  couleur: "#E9540D"
  taille: "Proportionnelle au texte"
  indentation: "20px"

Niveau 2:
  symbole: "○" (cercle vide) ou "–"
  couleur: "#0A3856"
  indentation: "40px depuis la marge"

Niveau 3:
  symbole: "·" (petit point)
  couleur: "#0A3856"
  indentation: "60px depuis la marge"

RÈGLE IMPORTANTE:
  maximum_niveaux: 2
  note: "Éviter plus de 2 niveaux d'imbrication"
```

### Icônes

```yaml
UTILISATION DES ICÔNES:

Style:
  type: "Linéaire ou filled, cohérent dans la présentation"
  épaisseur_trait: "2px"
  couleur_primaire: "#0A3856"
  couleur_accent: "#E9540D" ou "#FCC02D"

Taille:
  petite: "24px"
  moyenne: "48px"
  grande: "72px"

Placement:
  - À côté des titres de section
  - En illustration de concepts
  - Dans les bullet points (remplace la puce)
```

### Formes et Cadres

```yaml
RECTANGLES/CARRÉS:
  coins: "Arrondis 8px"
  bordure: "Optionnelle, 2px #0A3856"
  fond: "#FFFFFF ou couleur d'accent léger"

CERCLES:
  usage: "Icônes, numéros, photos de profil"
  bordure: "Optionnelle"

LIGNES DE SÉPARATION:
  épaisseur: "2px"
  couleur: "#0A3856 ou #FCC02D"
  style: "Solide"
  longueur: "40-60% de la largeur, centrée"

OMBRES:
  utilisation: "Minimale"
  si_utilisée: "Légère, 0 4px 8px rgba(10,56,86,0.1)"
```

---

## ⚠️ RÈGLES STRICTES

### À Faire (DO)

```
✅ Utiliser uniquement la palette définie (#0A3856, #E9540D, #FCC02D, #FFFFFF)
✅ Respecter les tailles de police (22pt titre, 14pt texte)
✅ Centrer tous les titres
✅ Garder un fond blanc pour toutes les slides
✅ Maintenir des marges généreuses (60px minimum)
✅ Utiliser Poppins exclusivement
✅ Limiter à 6 bullet points maximum par slide
✅ Garder un seul message par slide
✅ Assurer un contraste suffisant pour la lisibilité
✅ Aligner les éléments sur une grille invisible
```

### À Ne Pas Faire (DON'T)

```
❌ Utiliser d'autres couleurs que la palette définie
❌ Mettre du texte plus petit que 12pt
❌ Surcharger une slide avec trop d'informations
❌ Utiliser des fonds colorés ou dégradés
❌ Mélanger plusieurs polices
❌ Centrer du texte long (paragraphes)
❌ Utiliser des animations gratuites
❌ Placer des éléments trop près des bords
❌ Utiliser du texte en #FCC02D sur fond blanc
❌ Créer des slides "murailles de texte"
```

---

## 📊 GRAPHIQUES ET DONNÉES

### Style des Graphiques

```yaml
COULEURS DES GRAPHIQUES:

Serie_principale: "#0A3856"
Serie_secondaire: "#E9540D"
Serie_tertiaire: "#FCC02D"
Fond_graphique: "#FFFFFF"
Lignes_grille: "#E5E5E5" (gris très léger)
Axes: "#0A3856"

TYPOGRAPHIE DES GRAPHIQUES:

Titre_graphique: "Poppins 16pt SemiBold #0A3856"
Labels_axes: "Poppins 12pt Regular #0A3856"
Valeurs: "Poppins 12pt Regular #0A3856"
Légende: "Poppins 12pt Regular #0A3856"
```

### Bonnes Pratiques Graphiques

```
1. UN SEUL MESSAGE PAR GRAPHIQUE
   → Le titre du graphique doit énoncer l'insight

2. SIMPLIFIER AU MAXIMUM
   → Retirer les éléments non essentiels
   → Pas de grille 3D
   → Pas d'effets de volume

3. METTRE EN ÉVIDENCE
   → Utiliser #E9540D pour la donnée clé
   → Griser les données de contexte

4. ÉTIQUETER DIRECTEMENT
   → Labels sur les barres/lignes plutôt que légende séparée
```

---

## 🔄 TRANSITIONS ET COHÉRENCE

### Slides de Transition

```
UTILISATION:
→ Entre les grandes sections de la présentation
→ Pour marquer un changement de sujet

DESIGN:
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                                                             │
│                    SECTION 2                                │
│                    ─────────                                │
│                    Titre de la section                      │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Option: Fond #0A3856 avec texte #FFFFFF pour contraste fort
```

### Cohérence Globale

```yaml
ÉLÉMENTS RÉCURRENTS:

Position_du_titre:
  toujours: "En haut, centré"
  meme_position: "Sur toutes les slides"

Marges:
  identiques: "Sur toutes les slides"

Style_des_puces:
  uniforme: "Même couleur, même taille"

PROGRESSION VISUELLE:

Début_de_présentation:
  style: "Plus sobre, établit le contexte"

Milieu:
  style: "Plus dynamique, utilise les accents"

Fin:
  style: "Call-to-action fort, couleurs d'accent"
```

---

## 📋 CHECKLIST DE DESIGN

### Avant de Valider une Slide

```
□ Le titre est en Poppins 22pt SemiBold centré #0A3856
□ Le texte est en Poppins 14pt Regular #0A3856
□ Le fond est blanc (#FFFFFF)
□ Les marges de 60px sont respectées
□ Il n'y a qu'un seul message principal
□ Maximum 6 bullet points
□ Les couleurs utilisées sont dans la palette
□ Le contraste est suffisant pour la lisibilité
□ Les éléments sont alignés
□ Aucun élément ne touche les bords
```

### Cohérence de la Présentation

```
□ Tous les titres sont à la même position
□ La typographie est cohérente partout
□ Les couleurs sont utilisées de façon cohérente
□ Les espacements sont uniformes
□ Le style des puces est identique
□ Les graphiques suivent la même charte
```

---

## 📏 SPÉCIFICATIONS TECHNIQUES RÉSUMÉES

```
┌─────────────────────────────────────────────────────────────┐
│                  RÉCAPITULATIF TECHNIQUE                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  TYPOGRAPHIE                                                 │
│  ───────────                                                 │
│  Police unique      : Poppins                                │
│  Titre              : 22pt SemiBold uniquement, centré       │
│  Texte              : 14pt, Regular, gauche                  │
│  Interligne         : 1.5                                    │
│                                                              │
│  COULEURS                                                    │
│  ────────                                                    │
│  Principal          : #0A3856 (bleu foncé)                   │
│  Accent 1           : #E9540D (orange)                       │
│  Accent 2           : #FCC02D (jaune)                        │
│  Fond               : #FFFFFF (blanc)                        │
│                                                              │
│  MISE EN PAGE                                                │
│  ────────────                                                │
│  Marges             : 60px minimum                           │
│  Titre              : Centré, haut de slide                  │
│  Coins arrondis     : 8px (éléments)                         │
│  Espacement titre   : 40px avant contenu                     │
│                                                              │
│  LIMITES                                                     │
│  ───────                                                     │
│  Bullet points      : 6 maximum par slide                    │
│  Niveaux de puces   : 2 maximum                              │
│  Caractères/ligne   : 65-75 maximum                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

*Ce guide de design doit être appliqué systématiquement pour garantir des slides professionnelles et cohérentes.*

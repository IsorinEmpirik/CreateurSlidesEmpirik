# Guide opérationnel — Slides avec data

> Manuel à donner à un agent IA pour qu'il crée ou audite des slides contenant de la data.
> Règles **concrètes et actionnables**, pas de conseils génériques. Chaque règle dit **quoi faire** et **quoi ne pas faire**.
>
> Source : 4 vidéos YouTube — *Storytelling with Data* (Cole Nussbaumer Knaflic + Mike Cisneros + Alex Velez), résumé Luke Barousse. Méthode validée sur 10+ ans de workshops.

> ⚠️ **EN CAS DE CONFLIT, `CLAUDE.md §4` PRIME SUR CE GUIDE.**
> Ce guide est la source de référence académique Knaflic. CLAUDE.md a déjà intégré l'essentiel et fait les adaptations Empirik nécessaires.
> Adaptations connues qui priment sur ce guide :
> - **Couleur rouge alerte** : pas de rouge dans la charte Empirik, **l'orange #E9540D joue ce rôle** (CLAUDE.md §4.8)
> - **Titre du graphe en haut à gauche** : chez Empirik, **1 graphe = 1 slide**, le titre de slide centré porte le takeaway. Pas de re-titrage interne (CLAUDE.md §4.11)
> - **"Tout en gris par défaut"** : chez Empirik, **bleu Empirik #0A3856 joue le rôle de la couleur neutre dominante** (CLAUDE.md §4.8)
> - **Production de 2 versions (live + leave-behind)** : non requis, les pres Empirik sont par défaut "leave-behind" (lues seules en PDF)
>
> Lire ce guide pour la méthode SWD complète, mais appliquer CLAUDE.md §4 en pratique.

---

## 0. Méthode obligatoire avant d'ouvrir PowerPoint

1. **Papier + post-it**. 20 min minimum. Ne **pas** ouvrir l'outil tant que ces 3 lignes ne sont pas écrites :
   - Audience : `<personne précise>` (pas "les stakeholders")
   - Action voulue : `<verbe + objet>` (ex. "approuver budget 2026", "réduire churn de 10 %")
   - Insight central : 1 phrase max
2. **Dire l'histoire à voix haute** avant de la dessiner. Si on bute sur les mots, le slide ne marchera pas.
3. **Storyboarder** : 1 post-it = 1 slide. Réorganiser, supprimer, déplacer la CTA. Feedback sur le storyboard, **pas** sur le design.

---

## 1. Choix du graphe — 6 types par défaut, point.

Cole utilise ces 6 graphes pour 95 % des cas (méthode SWD) :

| Type | Quand l'utiliser |
|---|---|
| **Barre horizontale** | Catégories longues, ranking, comparaisons (le défaut le plus sûr) |
| **Barre verticale** | Quelques catégories courtes, valeurs absolues |
| **Barre empilée (stacked)** | Décomposition d'un total en 2-3 sous-parts |
| **Ligne** | Évolution temporelle continue (≥ 4 points) |
| **Slope graph** | Comparaison 2 périodes (avant/après, 2019 vs 2025) sur plusieurs catégories |
| **Dot plot** | Comparaison de valeurs ponctuelles, alternative à la barre horizontale |

### Interdits par défaut (sauf raison forte écrite)

- ❌ **3D** (jamais, tout court)
- ❌ **Ribbon chart, radar, treemap, sankey, gauge** sur audience non-spécialiste → courbe d'apprentissage = audience perdue
- ❌ **Camembert (pie)** : tolérable seulement si **2-3 parts max** ET la relation **part/tout** est *exactement* le message. Au-delà de 3 parts → barre horizontale.
- ❌ **Deux camemberts côte à côte pour comparer** : c'est le pire cas. Remplacer par slope graph.
- ❌ **Tableau de chiffres** : sauf si la valeur numérique exacte est le livrable (rapport financier). Le cerveau scanne ligne par ligne et mémorise → coût cognitif énorme.

### Règle de remplacement rapide

- "J'ai un tableau" → essayer barre horizontale ou slope graph
- "J'ai un pie chart avec 5+ parts" → barre horizontale triée
- "J'ai des barres groupées 2 années" → slope graph
- "J'ai une heatmap fancy" → réfléchir si une barre triée ne suffirait pas

---

## 2. Décombrer — checklist à appliquer en bloc

Pour **chaque graphe**, supprimer dans l'ordre :

1. ❌ **Bordure du graphe** (cadre noir autour)
2. ❌ **Gridlines** (lignes horizontales/verticales du fond)
3. ❌ **Background coloré** (fond bleu, gris dégradé → blanc)
4. ❌ **Trailing zeros** sur axe Y : `1000.0` → `1000` ; `10.00%` → `10%`
5. ❌ **Texte diagonal sur axe X** (50 % plus lent à lire) → abréger les mois (`Jan, Fév, Mar`) pour les passer en horizontal
6. ❌ **Légende séparée** quand on peut **étiqueter la donnée directement** (label de la même couleur que la ligne, en bout de ligne)
7. ❌ **Tous les data labels** quand il y a déjà un axe Y. Choisir l'un OU l'autre :
   - Valeur numérique précise critique → labels, supprimer l'axe Y
   - Forme/comparaison priorisée → garder l'axe, supprimer les labels
8. ❌ **Décimales inutiles** : `47,3 %` si la précision décimale n'est pas le message → `47 %`

### Mise en page de chaque graphe

- ✅ **Titre du graphe en haut à gauche** (pas centré). L'œil scanne en Z, il rencontre le titre avant la data.
- ✅ **Sous-titre/axe Y nommé** en haut à gauche aussi, pas en rotation verticale à gauche du graphe.
- ✅ **Barres épaisses** : si l'espace blanc entre les barres est plus large que les barres elles-mêmes → épaissir les barres.
- ✅ Sur barre horizontale → **trier par valeur** (sauf si l'ordre est sémantique : jours de la semaine, étapes).

---

## 3. Cohérence du deck (souvent négligé)

Toute incohérence visuelle force le cerveau à se demander "pourquoi est-ce différent ?". À unifier sur **l'intégralité du deck** :

- ✅ Même police, même tailles pour titres / axes / labels
- ✅ Même casing des titres (tout en Sentence case par défaut)
- ✅ Même position de la légende (idéalement : pas de légende, label direct)
- ✅ Même palette de couleurs (jamais "rouge slide 3, rouge slide 5" mais 2 nuances différentes)
- ✅ Mêmes formats de date (`Jan 2025` partout, pas `01/2025` un slide sur deux)
- ✅ Mêmes noms de séries (`Revenue` partout, pas `CA` un slide sur deux)

---

## 4. Couleur — règles strictes

> **Principe fondateur** : la couleur n'est **pas décorative**. C'est un **outil stratégique** au service du message. Chaque tache de couleur sur le slide doit répondre à la question : *"qu'est-ce que je veux que l'audience regarde ?"*. Si la réponse est "rien de particulier" → gris.

### Règles générales

- ✅ **Par défaut : tout en gris**. Puis 1 couleur d'accent pour ce qui compte.
- ✅ **Bleu** = neutre / positif / institutionnel (couleur la plus safe)
- ✅ **Rouge** = alerte, perte, problème. Ne **jamais** mettre la série principale en rouge si le message est positif.
- ✅ **Gris #B0B0B0** pour les séries de contexte (années précédentes, autres segments)
- ❌ **Jamais plus de 2 couleurs d'accent** dans un graphe (hors gris)
- ❌ **Jamais 5 lignes de 5 couleurs vives qui se croisent** → 1 couleur, le reste gris
- ❌ **Jamais rouge/vert seuls** comme code (~10 % de daltoniens). Doubler avec texte ou icône.
- ✅ **Brand colors** : OK, mais 1-2 max. Le reste en gris.
- ✅ **Couleur du label de série = couleur de la série** (renforce le lien visuel)

### Limiter le nombre de couleurs distinctes

Plus on multiplie les couleurs, plus on **dilue** la hiérarchie visuelle. Si tout est différent, **rien ne ressort**.

- ❌ "Une couleur par catégorie" → l'œil se perd, plus rien n'est prioritaire
- ✅ Une seule couleur, déclinée en **intensités/contrastes** pour traduire la valeur

### Heatmaps, gradients, encodage par valeur

Quand le message porte sur une **échelle de valeurs** (température, intensité, fréquence, %) :

- ✅ **Une seule teinte** (ex. bleu) **avec dégradé d'intensité** : clair = valeurs basses, foncé = valeurs hautes
- ✅ Si vraiment besoin de bipolarité (négatif/positif autour d'un zéro) → **gradient divergent à 2 teintes max** (ex. rouge → blanc → bleu), pas un arc-en-ciel
- ❌ **Échelle arc-en-ciel** (rouge → orange → jaune → vert → bleu) : illisible, trompeuse pour le cerveau (la perception de luminosité n'est pas linéaire), et catastrophique pour les daltoniens
- ❌ Une couleur catégorielle différente par cellule de heatmap → impossible à interpréter comme une échelle

---

## 5. Mots — utiliser le titre comme arme

### Le titre prioritaire = le takeaway, pas le sujet

| ❌ Titre descriptif | ✅ Titre takeaway |
|---|---|
| `Ventes par trimestre 2025` | `Le T3 dépasse la cible pour la 1re fois en 4 ans` |
| `Tickets reçus vs traités` | `L'écart de tickets non traités a doublé depuis mai` |
| `Évolution NPS` | `Le NPS chute de 12 points après le pricing change` |
| `Skip days par groupe` | `Les notifications réduisent le skip… mais seulement 24 h` |

Étude citée par Cole : avec un titre takeaway, **l'audience retient mieux le message**.

### Annotations sur le graphe

- ✅ Texte court directement **à côté** du point d'intérêt (flèche fine ou label)
- ✅ **Étiqueter 2-3 points stratégiques** seulement (pics, vallées, début/fin) — pas tous
- ✅ **Renommer les catégories techniques** en termes business :
  - `Treatment 1` → `Groupe Awareness`
  - `Treatment 2` → `Groupe Goal-oriented`
  - `Q1_2025_var_pct` → `Variation T1 2025`
- ✅ **Footnote** sous le graphe pour définir métriques techniques

---

## 6. Contraste pour pointer LA chose à regarder

Quand tout est gris, n'importe quoi devient saillant. Leviers, par ordre de force :

| Levier | Effet | Quand |
|---|---|---|
| **Couleur** vs gris | Très fort | Toujours en premier |
| **Épaisseur** ligne/barre | Fort | Compléter la couleur |
| **Intensité** (foncé vs clair) | Moyen | Si la couleur est déjà prise |
| **Taille du texte / label** | Fort sur les labels | Pour les annotations clés |
| **Position 1er plan** | Moyen | Si une ligne passe derrière une autre |
| **Marker + label ponctuel** | Fort | Sur 1-2 points (forcer la comparaison) |
| **Apparition animée** | Très fort en live | Le reste apparaît, puis la série clé arrive |
| **Pointillé** | Fort mais ATTENTION | **Réservé à l'incertitude** (cible, forecast). Pas pour focaliser. |

**Empiler 2-3 leviers** : couleur + épaisseur + label, c'est OK et même conseillé.

---

## 7. Live vs document : ne pas mélanger

| Cas | Règle |
|---|---|
| **Slide présentée en live (réunion/webinar)** | Slides épurées, peu de texte, l'orateur fournit le contexte. **Animer** la révélation des éléments. |
| **Slide envoyée en PDF/lien** | Tout doit se lire seul. **Annoter** chaque graphe : titre takeaway + encadré explicatif + recommandation. |
| **Le slidement (slide + document mixte)** | ❌ À éviter : trop dense pour le live, pas assez détaillé pour le standalone. |

> Idéalement : produire **2 versions** du même contenu (live + leave-behind).

---

## 8. Structure du deck — Plot / Twist / Ending

### Story Mountain (minimum vital)

1. **Plot** : contexte que l'audience doit avoir pour être réceptive
2. **Twist** : ce qui est nouveau / inattendu / qui change la donne
3. **Ending** : action recommandée

### Le piège du "presentation typique"

❌ Background → Problem → Data → Méthodologie → Findings → ~~(stop ici)~~

→ L'audience dit "intéressant" et passe. Ajouter **Recommandation** (étape 8 ci-dessous).

### Tisser plusieurs graphes ensemble (pas en bloc côte à côte)

- ❌ 4 graphes sur 1 slide "vue d'ensemble"
- ✅ 1 graphe par slide, qui construit progressivement le récit : hausses → baisses → conclusion → recommandation

---

## 9. Recommandation finale obligatoire

Chaque deck data finit par **une action recommandée explicite**.

Si l'orateur ne peut formuler aucune action après l'analyse → **ne pas faire la présentation**.

### Formuler la recommandation

- ✅ `Je recommande qu'on <verbe action> pour <résultat attendu>`
- ✅ Donner même une option imparfaite : l'audience aura quelque chose à amender, redirige la discussion vers "comment agir" plutôt que "donnez plus de data"
- ❌ "Voici les données, à vous de décider" (= occasion ratée)

### Exemples concrets de fin de deck

- "Je recommande d'ajouter un 2e cycle de promotion en avril pour réduire les exits."
- "Je recommande de targeter les véhicules 5 places similaires plutôt que toutes les CSUV pour la campagne marketing."
- "Je sollicite l'approbation du budget pour 2 ETP supplémentaires sur le service desk."

---

## 10. Exploratoire ≠ Explicatif (erreur la plus fréquente)

| Phase | Visuels | Public |
|---|---|---|
| **Exploratoire** | Box plot, histogramme, scatter, courbe de survie, heatmap, matrices | **Soi-même uniquement**. Tools par défaut, pas de mise en forme. |
| **Explicatif** | Les 6 types par défaut (§1), épurés et titrés | Audience finale |

**Règle d'or** : ne jamais partager un graphe exploratoire à l'audience finale. Le retravailler entièrement OU le remplacer par un visuel plus simple qui transporte le même insight.

Exemple du livre : une **courbe de survie** (skip days study) → remplacée par **3 square area charts** côte à côte (32 % vs 16 % vs 12 %) → compréhensible en 5 sec par un comex.

---

## Checklist finale agent IA — avant de livrer un slide

Pour chaque slide du deck :

- [ ] **Audience nommée** précisément (pas "stakeholders", pas "le client")
- [ ] **Titre = takeaway** en phrase complète, pas le sujet
- [ ] **Type de graphe** dans la liste des 6 (§1) — sinon justification écrite
- [ ] **Pas de** : bordure, gridlines, fond coloré, texte diagonal, trailing zeros
- [ ] **Choix axe Y OU labels**, pas les deux
- [ ] **Légende remplacée** par labels directs en bout de série, même couleur
- [ ] **Tout gris sauf 1 série** d'accent (couleur)
- [ ] **Contraste empilé** sur la série clé (couleur + épaisseur + label ponctuel)
- [ ] **Cohérence** police/casing/palette/format date avec le reste du deck
- [ ] **Catégories renommées** en business (pas `treatment_1`)
- [ ] **Recommandation explicite** présente au moins dans le slide final
- [ ] **Version live ET version annotée** si le deck circule en async

---

## Outils utilisés par les auteurs

- **PowerPoint + Excel uniquement** pour tous les exemples des livres (méthode délibérément tool-agnostic). Tableau / Power BI / Python / D3 fonctionnent pareil, les principes ne changent pas.
- Tutoriels Excel/PPT officiels SWD : `storytellingwithdata.com/excel-tutorials`
- Guide de choix du graphe : `storytellingwithdata.com/chart-guide`

---

## Sources

| # | Vidéo | Auteur | Apport principal |
|---|---|---|---|
| 1 | [How to turn data into stories](https://www.youtube.com/watch?v=Hfx1X9WSGYQ) | storytelling with data | Workshop : disperate data → good → great → story (HR/sales managers) |
| 2 | [Storytelling with Data: Before and After (audiobook preview)](https://www.youtube.com/watch?v=2h81XPgtHnM) | Cole + Cisneros + Velez | Méthode complète + ch. 1 mindful eats (square area charts) |
| 3 | [The book every Data Analyst should read](https://www.youtube.com/watch?v=09JnFEdZe2A) | Luke Barousse | Synthèse pratique en 5 étapes (Power BI) |
| 4 | [Celebrating a decade — 10 lessons](https://www.youtube.com/watch?v=99zlHv1fNdw) | storytelling with data | 10 lessons + slope graph + narrative arc |

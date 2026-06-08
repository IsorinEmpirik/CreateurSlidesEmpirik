# Guide Expert Data Visualization pour IA

> Source: "Fundamentals of Data Visualization" - Claus O. Wilke
> Usage: Aide-mémoire pour générer des graphiques professionnels dans des slides/audits

> ⚠️ **EN CAS DE CONFLIT, `CLAUDE.md §4` PRIME SUR CE GUIDE.**
> CLAUDE.md adapte les règles Wilke à la charte Empirik et aux principes Knaflic (plus stricts).
> Exemples de divergences connues à respecter :
> - **Pie chart** : Wilke tolère, **CLAUDE.md §4.10 interdit** (sauf 2-3 parts max ET part/tout = exactement le message)
> - **Area chart** : Wilke tolère si axe Y = 0, **CLAUDE.md §4.10 préfère ligne** sauf cas spécifiques
> - **Palette** : Wilke n'impose pas, **CLAUDE.md §4.8 = 4 couleurs Empirik strictement** (bleu / orange / jaune décoratif / gris)
> - **Rainbow / arc-en-ciel** : interdit dans les deux ✓ (cohérent)
>
> Lire ce guide comme une référence académique, mais appliquer CLAUDE.md en pratique.

---

## 1. SÉLECTION DU TYPE DE GRAPHIQUE

### Montants (valeurs numériques par catégorie)
| Objectif | Graphique recommandé |
|----------|---------------------|
| Comparaison simple | Barres verticales/horizontales |
| Valeurs loin de zéro | Dot plot (points) |
| Multi-catégories croisées | Heatmap |
| Catégories ordonnées | Conserver l'ordre naturel |
| Catégories non-ordonnées | Trier par valeur décroissante |

### Distributions
| Objectif | Graphique recommandé |
|----------|---------------------|
| Une distribution | Histogramme, density plot |
| Comparer 2-3 distributions | Density plots superposés (transparents) |
| Comparer 5-20 distributions | Boxplots, violin plots |
| Comparer 20+ distributions | Ridgeline plots |
| Données éparses | Strip charts avec jitter |

### Proportions (parts d'un tout)
| Objectif | Graphique recommandé |
|----------|---------------------|
| Fractions simples (1/2, 1/4) | Pie chart acceptable |
| Comparaison entre groupes | Barres côte-à-côte |
| Évolution temporelle | Barres empilées (max 2-3 segments) |
| Proportions imbriquées | Treemap, mosaic plot |

### Relations X-Y
| Objectif | Graphique recommandé |
|----------|---------------------|
| 2 variables continues | Scatter plot |
| Scatter + 3ème variable | Couleur ou taille des points |
| Forte densité de points | Hexbin, contours de densité |
| Corrélations multiples | Matrice de corrélation (correlogram) |

### Séries temporelles
| Objectif | Graphique recommandé |
|----------|---------------------|
| Tendance générale | Ligne continue |
| Points espacés | Ligne + points visibles |
| Cumul depuis zéro | Area chart (axe Y doit partir de 0) |
| Multiples séries | Lignes avec étiquettes directes |

### Incertitude
| Objectif | Graphique recommandé |
|----------|---------------------|
| Estimation ponctuelle | Barres d'erreur (spécifier IC) |
| Distribution complète | Violin plot, gradient de confiance |
| Probabilités | Quantile dot plot (20-50 points) |

---

## 2. RÈGLES DES COULEURS

### Types d'échelles de couleur
| Type | Usage | Exemple |
|------|-------|---------|
| **Qualitative** | Catégories sans ordre | Pays, types de produits |
| **Séquentielle** | Valeurs continues ordonnées | Revenus, températures |
| **Divergente** | Valeurs avec point médian significatif | Écarts +/-, % autour de 50% |
| **Accent** | Mise en évidence | 1-2 éléments clés à souligner |

### Règles strictes
- **Maximum 5-8 couleurs distinctes** pour les échelles qualitatives
- **Jamais de rainbow/arc-en-ciel** : non-monotonique, trompeuse
- **Tester l'accessibilité daltoniens** : éviter rouge-vert seuls
- **Palette recommandée CVD-safe** : Okabe-Ito, ColorBrewer
- **Couleurs moins saturées** pour grandes surfaces
- **Chaque couleur doit avoir un but** : pas de décoration gratuite

### Codage redondant obligatoire
Ne jamais se fier uniquement à la couleur. Combiner :
- Couleur + forme des points
- Couleur + motif de ligne
- Couleur + étiquettes directes

---

## 3. AXES ET ÉCHELLES

### Échelle linéaire vs logarithmique
| Situation | Échelle |
|-----------|---------|
| Données standard | Linéaire |
| Données sur plusieurs ordres de grandeur | Logarithmique |
| Ratios et taux de croissance | Logarithmique |
| Données incluant zéro | Linéaire (log impossible) |

### Règles critiques
- **Barres = toujours partir de zéro** sur échelle linéaire
- **Échelle log = partir de 1** (pas de zéro)
- **Spécifier la base** du logarithme
- **Mêmes unités X et Y** = grille carrée obligatoire
- **Unités différentes** = ratio ajustable selon message

### Formatage
- Labels d'axes **suffisamment grands** (erreur #1 : trop petits)
- Nommer la **variable**, pas sa transformation
- Inclure les **unités** pour toute variable numérique

---

## 4. PRINCIPES DE DESIGN

### Principe de l'encre proportionnelle
> "La taille des éléments visuels doit être proportionnelle aux valeurs qu'ils représentent"

- Barres coupées = **INTERDIT** (exagère les différences)
- Area charts avec Y ≠ 0 = **INTERDIT**
- Pie charts = mathématiquement corrects mais perceptuellement faibles

### Gérer le chevauchement de points
| Niveau | Solution |
|--------|----------|
| Léger | Transparence (alpha) |
| Modéré | Transparence + jitter |
| Intense | Hexbin ou 2D histogram |
| Très dense | Contours de densité |

### Éviter les dessins au trait
- **Préférer les formes pleines** aux contours vides
- Barres pleines > barres vides
- Points pleins > cercles vides
- Remplissage semi-transparent pour densités superposées

### JAMAIS de 3D gratuite
- La projection 3D **déforme systématiquement** les données
- Pie 3D : tranches avant paraissent plus grandes
- Barres 3D : hauteurs impossibles à comparer
- **Alternative** : small multiples, couleur, taille

---

## 5. FIGURES MULTI-PANNEAUX

### Small multiples
- Même type de graphique pour chaque sous-ensemble
- **Axes identiques** entre tous les panneaux
- Ordre logique : temporel, hiérarchique ou par magnitude

### Figures composées
- Étiqueter **a, b, c...** discrètement
- **Même code couleur** = même signification partout
- **Même ordre** des catégories entre panneaux
- Alignement précis des axes

---

## 6. TITRES ET LÉGENDES

### Règles des titres
- Un graphique = **un seul titre**
- Le titre doit énoncer le **message**, pas décrire le contenu
- Slide/infographie : titre intégré au graphique
- Article/rapport : titre en début de légende sous le graphique

### Règles des tableaux
- **Jamais de lignes verticales**
- Lignes horizontales minimales (en-tête seulement)
- Texte : aligné à gauche
- Nombres : alignés à droite, décimales uniformes
- Légende du tableau : **au-dessus** (pas en-dessous)

---

## 7. ÉQUILIBRE DATA / CONTEXTE

### Ratio data-ink (Tufte)
Maximiser l'encre consacrée aux données, **dans la raison**.

| Trop de contexte | Trop peu de contexte |
|------------------|----------------------|
| Cadres inutiles | Points flottant dans le vide |
| Grilles denses | Pas de repères visuels |
| Annotations excessives | Impossible de lire les valeurs |

### Recommandations grilles
- Grilles légères, gris clair
- Lignes perpendiculaires à la variable d'intérêt principal
- Scatter plots denses : garder la grille
- Line charts : lignes horizontales suffisent

---

## 8. STORYTELLING DATA

### Principes narratifs
- **Simple > Complexe** : ne pas tout montrer en une figure
- **3-6 figures** par histoire/analyse
- **Progression** : données brutes → dérivées → conclusions
- **Varier les types** de graphiques pour maintenir l'attention

### Pour présentations
1. Montrer version simplifiée d'abord
2. Révéler la complexité progressivement
3. Un message clé par slide
4. Public pressé = clarté immédiate obligatoire

### Mémorabilité
- Figures uniques et visuellement distinctes = plus mémorables
- Isotypes (pictogrammes) augmentent la rétention
- Ne pas sacrifier la clarté pour l'originalité

---

## 9. CHECKLIST AVANT GÉNÉRATION

```
[ ] Type de graphique adapté à l'objectif ?
[ ] Axes partent de zéro si barres/areas ?
[ ] Échelle (lin/log) appropriée ?
[ ] Max 5-8 couleurs qualitatives ?
[ ] Palette accessible daltoniens ?
[ ] Codage redondant (pas couleur seule) ?
[ ] Labels d'axes lisibles et avec unités ?
[ ] Titre = message, pas description ?
[ ] Pas de 3D gratuite ?
[ ] Grille minimale mais suffisante ?
[ ] Ordre des catégories logique ?
```

---

## 10. ANTI-PATTERNS À ÉVITER

| Anti-pattern | Problème | Solution |
|--------------|----------|----------|
| Barres tronquées | Exagère différences | Partir de zéro |
| Rainbow colormap | Non-monotonique | Séquentielle monotone |
| Pie chart 3D | Distorsion | Pie 2D ou barres |
| Légende avec 10+ items | Illisible | Étiquettes directes |
| Histogrammes empilés | Comparaison impossible | Density superposés |
| Axes sans unités | Ambigu | Toujours spécifier |
| Double axe Y | Trompeur | Deux graphiques séparés |
| Trop de décimales | Fausse précision | Arrondir raisonnablement |

---

## QUICK REFERENCE : CHOIX RAPIDE

```
Comparer des quantités    → Barres (triées si non-ordonnées)
Montrer une distribution  → Histogramme / Density
Comparer distributions    → Boxplot / Violin
Relation 2 variables      → Scatter plot
Évolution temporelle      → Line chart
Parts d'un tout          → Barres empilées ou Pie (simple)
Données géographiques    → Carte choroplèthe
Incertitude              → Barres d'erreur + spécifier CI
```

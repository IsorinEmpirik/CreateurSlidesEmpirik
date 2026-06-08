# Instructions Empirik — Création de Slides x Storytelling

> **Source unique de vérité.** Tous les retours utilisateurs ont été consolidés ici.
> Quatre fichiers compagnons à lire en parallèle : `guide_design_slides.md`, `guide_storytelling_presentations.md`, `dataviz-guide.md`, `guide-slides-data-storytelling.md`.
> Référence anti-régression : `PROCESS-ANTI-ERREURS.md` (checklist tactique + 7 erreurs récurrentes + helpers PptxGenJS).

---

## ⚠️ HIÉRARCHIE DES SOURCES (priorité décroissante)

En cas de divergence entre fichiers, appliquer dans cet ordre strict :

1. **`CLAUDE.md`** (ce fichier) — règles de fond + adaptations Empirik. **Prime sur tout.**
2. **`PROCESS-ANTI-ERREURS.md`** — règles tactiques + helpers code + checklist QA. Prime sur les guides externes pour la mise en œuvre concrète.
3. **`guide_design_slides.md`**, **`guide_storytelling_presentations.md`**, **`dataviz-guide.md`**, **`guide-slides-data-storytelling.md`** — sources académiques de référence (Knaflic, Wilke, Duarte). À lire pour la culture, mais leurs règles peuvent être surchargées par les §1-§2 ci-dessus (qui ont adapté à la charte Empirik).
4. **Mémoire utilisateur (`MEMORY.md`)** — notes ponctuelles uniquement. Ne contient plus de règles.

Si un guide externe dit X et CLAUDE.md dit Y → appliquer Y.

---

## 0. WORKFLOW OBLIGATOIRE (8 étapes)

> **REGLE ABSOLUE** : ne JAMAIS commencer à générer des slides sans avoir fait valider un plan par l'utilisateur.
> **REGLE ABSOLUE 2** : ne JAMAIS livrer un .pptx sans avoir produit le rapport QA exhaustif de l'étape 8.

### Étape 1 — Lecture des guides (avec preuve obligatoire)
Avant toute réflexion : lire **dans l'ordre, intégralement** :
1. `CLAUDE.md` (ce fichier) — règles de fond Empirik
2. `PROCESS-ANTI-ERREURS.md` — checklist tactique + erreurs récurrentes
3. `MASTER-CHECKLIST.md` — instrument du rapport QA final
4. `guide_design_slides.md` — détails design
5. `guide-slides-data-storytelling.md` — méthode Knaflic intégrale (référence académique principale pour les slides data)
6. `guide_storytelling_presentations.md` — méthode Nancy Duarte
7. `dataviz-guide.md` — référence Wilke
8. `DESIGN_EMPIRIK.md` — assets visuels Gemini

Garder en tête la **hiérarchie des sources** (encart ci-dessus) : CLAUDE.md + PROCESS-ANTI-ERREURS.md priment.

#### ⛔ Artifact obligatoire — Rapport de lecture EN ACTIONS CONCRÈTES (anti-triche + anti-théorie)

**Avant de passer à l'étape 2**, produire un mini-rapport qui liste **5 ACTIONS TACTIQUES PRÉCISES** par fichier — pas 5 bullets théoriques. Chaque action doit être :
- Tactique (un verbe concret : "je placerai", "je vérifierai", "je créerai")
- Vérifiable plus tard dans le deck (on doit pouvoir cocher ✅/❌ à la fin)
- Spécifique à CETTE pres (pas une généralité réutilisable)

**Pourquoi cette nuance "actions concrètes vs bullets théoriques"** : un Claude qui résume Duarte en 5 bullets ("3 actes", "audience est le héros", "big idea", "S.T.A.R.", "Logos/Pathos/Ethos") repart sans plan d'application. Il appliquera ce qui a un équivalent tactique évident (top-down, voix "vous") et oubliera le reste. La conversion **lecture → actions** force le passage du conceptuel au tactique.

Format attendu :

```
## Rapport de lecture des guides — Actions concrètes pour cette pres

### CLAUDE.md (règles de fond)
1. J'appliquerai la slide synthèse/reco en slide 2 (top-down McKinsey §2.1)
2. J'utiliserai fontFace: "Poppins SemiBold" pour les titres, jamais fontWeight (§3.2)
3. ...

### PROCESS-ANTI-ERREURS.md (tactique)
1. J'exécuterai grep -c "—" sur le script de génération avant export (Erreur #4)
2. ...

### guide-slides-data-storytelling.md (Knaflic)
1. Je vérifierai pour chaque graphe le test d'adéquation aux valeurs réelles §4.10
2. Je préfèrerai chiffres-clés à dot plot si ratio > 3 (§6.6 Voie 4)
3. ...

### guide_storytelling_presentations.md (Duarte)
1. Je placerai un S.T.A.R. moment slide X (type : stat choquante humanisée / sound bite / visuel évocateur)
2. J'humaniserai les 3 chiffres-clés principaux avec une analogie familière (ex : "11 700 € = un voyage aux Maldives")
3. Je peindrai la nouvelle félicité slide Y entre la reco et le CTA final
4. Je formulerai la big idea avec enjeux gain ET perte (pas juste le verdict)
5. Je vérifierai l'alternance "ce qui est" / "ce qui pourrait être" — 4 minimum sur le deck

### guide_design_slides.md
1. ...
```

**Pourquoi cette contrainte** : sans actions tactiques, la lecture des guides reste théorique. Particulièrement vrai pour Duarte (Pathos, S.T.A.R., humanisation, nouvelle félicité) dont les principes sont **conceptuels** alors que ceux de Knaflic/Wilke sont **tactiques** (helpers code, palette, types de graphes). Sans conversion explicite en actions, le Pathos devient un angle mort silencieux. **Pas de rapport en actions concrètes = pas de progression vers l'étape 2.**

### Étape 2 — Proposer 2 à 3 angles narratifs distincts

#### ⚠️ Drapeau rouge "Pathos faible" — à lever explicitement sur sujets data-driven

Avant de formuler les angles, **détecter si le brouillon est à risque Pathos faible** :
- Le brouillon est 100% chiffres / sources / études / faits ?
- Pas de personnage humain incarné, pas d'anecdote, pas de témoignage, pas de citation propriétaire ?
- Sujet "comparatif rationnel" / "audit" / "restitution data" pure ?

Si OUI à l'un de ces critères, ajouter **explicitement** dans chaque angle proposé une mention du type :

```
⚠️ RISQUE PATHOS FAIBLE détecté.
Compensation prévue dans cet angle :
 - 1 personnage incarné (qui ? le futur propriétaire / l'utilisateur final / le décideur cible)
 - 1 anecdote ou témoignage placé en slide N
 - 1 métaphore filée tout au long du deck (le sujet "est comme...")
 - Au moins 1 S.T.A.R. moment (stat choquante humanisée, sound bite, ou visuel évocateur)
```

L'utilisateur valide en connaissance de cause au lieu de découvrir le manque de Pathos à la fin du deck. **Le défaut par défaut sur sujet data-driven est le format McKinsey "rapport d'audit" qui maximise Logos et tue le Pathos** — c'est ce que la pres "Angora vs Sphinx" v1 a illustré (score Duarte 55-60% au lieu de 85%).

**⛔ Validation explicite OBLIGATOIRE de l'utilisateur sur le contre-poison choisi AVANT de passer à l'étape 3.5**

Le sujet est data-driven (zéro personnage humain, zéro anecdote dans le brouillon) ? Tu dois proposer **3 contre-poisons** explicitement à l'utilisateur, et attendre qu'il choisisse :

```
⚠️ Risque Pathos faible détecté. Pour que la pres résonne, choisis l'un des
3 contre-poisons (obligatoire avant étape 3.5) :

(a) Personnage incarné fil rouge — la pres parle À une persona précise
    (Marc et Sophie, 32 et 28 ans, premiers acquéreurs d'un chat...) et
    elle apparaît dans plusieurs slides
(b) Anecdote d'ouverture — slide 1 ou 2 = mini-histoire vraie (1-2 phrases)
    qui plante le décor émotionnel
(c) Métaphore filée tout au long du deck — un parallèle filé du début à
    la fin ("Choisir un chat = choisir un véhicule pour 15 ans...")

Quel contre-poison veux-tu pour cette pres ? (a / b / c / les trois)
```

**Pas de "go" à l'étape 3.5 tant que l'utilisateur n'a pas choisi.** Sans contre-poison explicitement validé, la pres glisse mécaniquement vers le format audit McKinsey factuel.

#### Format des angles



Format :
```
OPTION A : [Nom de l'angle]
Fil conducteur : ...
Structure :
  1. [Section] — X slides — types : ...
  2. [Section] — X slides — types : ...
Total : ~XX slides

OPTION B : [Nom de l'angle]
...
```

### Étape 3 — ATTENDRE la validation explicite
Pas de génération sans validation. Si l'utilisateur dit juste "ok" ou "go", reconfirmer quelle option est retenue.

### Étape 3.5 — Audience + Action + Insight central (Knaflic §0 obligatoire)

**Avant de détailler le plan slide par slide, produire 3 lignes qui ancrent la pres** :

```
ÉTAPE 3.5 — Triplet Audience / Action / Insight (obligatoire, anti-pres-vague)

AUDIENCE : <personne PRÉCISE>
  → Pas "le client", pas "le lecteur", pas "les stakeholders"
  → Format attendu : rôle, contexte, peur principale, désir principal
  → Ex : "Le futur propriétaire entre 30 et 45 ans, qui hésite entre 2 races
          de chat, a peur des frais véto, désire un animal calme et durable"

ACTION VOULUE : <verbe + objet concret>
  → Ce que l'audience doit FAIRE concrètement après la pres
  → Ex : "Choisir l'Angora plutôt que le Sphinx pour son premier chat"
  → ❌ "Comprendre les différences" (passif) / ✅ "Choisir l'Angora" (actif)

INSIGHT CENTRAL : 1 phrase max
  → La chose nouvelle / contre-intuitive que la pres révèle
  → Ex : "Le Sphinx a un coût de vie 2x supérieur ET une espérance de vie
         3 ans inférieure à l'Angora — la séduction esthétique cache un
         deal défavorable"
```

**Test obligatoire** : si tu ne peux pas raconter l'histoire à voix haute en 90 secondes à partir de ces 3 lignes, NE PASSE PAS à l'étape 4. Reviens travailler le triplet.

**Pourquoi cette étape** : Knaflic §0 ("papier + post-it 20 min") insiste sur le fait que le détail slide par slide AVANT l'ancrage Audience/Action/Insight produit une pres techniquement riche mais sans direction claire. Le triplet est la boussole du deck — sans lui, chaque slide est une décision isolée.

### Étape 4 — Détailler le plan retenu slide par slide (avec 6 artifacts obligatoires)

Numéro + titre + type de slide + contenu principal + élément visuel prévu.

**Pour chaque slide contenant de la data** : annoncer le **type de graphique justifié** ET la **voie de génération choisie** (cf §6.6) :
> "Slide N : objectif = comparer X entités sur Y critères → selon §4.10 = slope graph (pas barres horizontales). Voie : Python matplotlib → PNG (Voie 3) car slope graph en shapes PptxGenJS trop lourd."

**Pour chaque section** : annoncer la **mécanique storytelling** :
> "Section 2 : what is (constat actuel client) → what could be (potentiel) → point de bascule (insight) → preuve (data)."

#### ⛔ 6 artifacts obligatoires à produire dans le plan détaillé (anti-omission)

Ces 5 artifacts forcent l'application de règles que les agents IA ont tendance à zapper silencieusement. **Sans ces 5 artifacts dans le plan, pas de "go" à donner.**

**Artifact 1 — Tableau de couverture du brouillon (anti-troncage)**

Pour CHAQUE chiffre, fait, citation ou source dans le brouillon / brief / PDF source : ligne dans un tableau qui indique sur quelle slide il sera utilisé.

| # | Chiffre / fait / source | Brouillon réf | Slide cible | Statut |
|---|--------------------------|---------------|-------------|--------|
| 1 | 67% câlins · Vienna 2012 | brouillon p.2 | Slide 7 | utilisé |
| 2 | 54% pref poil long · Ipsos 2019 | brouillon p.2 | Slide 7 | utilisé |
| 3 | 3x consult dermato · RVC 2017 | brouillon p.3 | — | **OMIS → justification : redondant avec ligne 4** |
| ... | ... | ... | ... | ... |

Si > 20% des chiffres sont en "OMIS" → alerte obligatoire à l'utilisateur avant validation. L'exhaustivité est la règle, l'omission est l'exception et doit être documentée.

**Artifact 2 — Avocat du diable §1.3 (anti-validation aveugle)**

Pour chaque chiffre clé / reco / source du brouillon : passer au crible avec une note de robustesse.

| # | Chiffre / reco | Preuve | Limites / biais | Robustesse | Action |
|---|----------------|--------|-----------------|-----------|--------|
| 1 | "67% câlins · Vienna 2012" | étude n=300 | perception subjective, n=300 modeste, ancienneté (13 ans) | 🟡 moyenne | utiliser avec mention "perception déclarée" |
| 2 | "+40% frais véto" | annoncé "à vérifier" dans brouillon | source non confirmée | 🔴 faible | **NE PAS utiliser comme verdict, signaler à l'utilisateur** |
| 3 | "HCM 33-50% Sphinx vs 7% Angora" | journals vétérinaires | panels différents, biais d'échantillonnage | 🟠 modérée | utiliser avec fourchette explicite, ne pas généraliser "1 sur 2" |
| ... | ... | ... | ... | ... | ... |

À la fin du tableau : note "qualité globale des sources : X chiffres robustes, Y modérés, Z fragiles → recommandation utilisateur".

**Artifact 3 — Liste explicite des slides "Ce qu'il faut retenir" (anti-trou narratif)**

Le top-down McKinsey §2.1 exige une slide synthèse de section après CHAQUE chapitre. Lister explicitement :

```
Section 1 (chapeau) — 3 slides → slide récap section 1 = slide 5 "Ce qu'il faut retenir : ..."
Section 2 (chapeau) — 4 slides → slide récap section 2 = slide 10 "Ce qu'il faut retenir : ..."
Section 3 (chapeau) — 3 slides → slide récap section 3 = slide 14 "Ce qu'il faut retenir : ..."
```

Si une section n'a pas de slide récap planifiée → c'est un défaut, l'ajouter ou justifier explicitement.

**Artifact 4 — Cartographie des voies dataviz (anti-monotonie)**

Pour TOUS les graphes du deck, lister par type et voie de génération :

| Slide | Type de graphe | Voie | Justification |
|-------|----------------|------|---------------|
| 8 | Barre horizontale 5 catégories | Voie 1 (shapes) | Comparaison simple, 5 entités |
| 10 | Slope graph multi-critères | Voie 3 (matplotlib → PNG) | Comparaison Angora vs Sphinx sur 5 critères = cas d'usage canonique slope |
| 13 | Chiffre clé (pas graphe) | — | — |
| 15 | Waterfall coût Sphinx 15 ans | Voie 3 (matplotlib → PNG) | Décomposition séquentielle d'un total |

**Règle de variété** : si > 70% des graphes du deck sont du même type (typiquement barres horizontales), c'est une alerte rouge. Repenser au moins 30% des graphes pour utiliser slope/dot plot/line/waterfall selon le cas. Voir §4.2 (variété obligatoire) et §6.6 (3 voies de génération).

**Artifact 5 — Slides question client planifiées (anti-pres monolithique)**

§3.6 demande d'intégrer régulièrement des slides question client (fond crème, icône `?` orange, question centrée 24pt bold) pour créer interaction. Rythme cible : au moins 1 par section, ou 1 toutes les 5-7 slides.

```
Slide 6 : Question client après section 1 ("Quel critère pèse le plus pour vous : santé ou esthétique ?")
Slide 11 : Question client après section 2 ("Êtes-vous prêt à investir 2 000€ + chauffage continu sur 15 ans ?")
Slide 15 : Question client de transition vers reco ("Que voulez-vous prioriser : la facilité quotidienne ou l'animal de compagnie qui vit longtemps ?")
```

Si aucune slide question planifiée → c'est un défaut, en ajouter au minimum 2-3 ou justifier explicitement.

**Artifact 6 — Plan émotionnel (anti-pres-100%-Logos, Duarte/Resonate)**

Le guide Duarte/Resonate exige une dimension émotionnelle (Pathos) pour qu'une pres "résonne". Sans ce plan explicite, le réflexe Empirik par défaut sur sujet data-driven est un rapport d'audit factuel à 95% Logos — techniquement excellent mais qui ne marque pas l'audience.

Le plan émotionnel doit être documenté **avant le go final**, avec ces 6 éléments :

```
ARTIFACT 6 — Plan émotionnel

a) S.T.A.R. MOMENT PRINCIPAL ("Something They'll Always Remember")
   → Slide N : type = [sound bite ciselé / stat choquante humanisée /
                        visuel évocateur / dramatisation / mini-histoire]
   → Contenu précis : "..."

b) HUMANISATION DES CHIFFRES (top 3 chiffres-clés du deck)
   → Chiffre 1 : "[valeur brute]" → traduction familière "[analogie]"
     Ex : "11 700 € sur 15 ans" → "le prix d'un voyage de noces aux Maldives"
   → Chiffre 2 : ...
   → Chiffre 3 : ...

c) SPARKLINE (alternance "ce qui est" ↔ "ce qui pourrait être")
   → Liste explicite de 4 alternances minimum sur le deck
   → Slide 3 : ce qui est (constat actuel)
   → Slide 5 : ce qui pourrait être (potentiel atteignable)
   → Slide 7 : ce qui est (obstacle 2)
   → Slide 9 : ce qui pourrait être (solution 2)
   → ...

d) NOUVELLE FÉLICITÉ (peinture du futur transformé)
   → Slide située entre la reco et le CTA final
   → Projection narrative : "Imaginez, dans 12 mois, votre [audience]..."
   → Pas une liste de bénéfices en carte, une VISION racontée

e) BIG IDEA COMPLÈTE avec ENJEUX (gain ET perte)
   → ❌ Big idea incomplète : "L'Angora turc l'emporte sur le Sphinx"
   → ✅ Big idea complète : "Choisir l'Angora vs Sphinx, c'est gagner 3 ans
       de vie animale ET économiser 7 000 €, en évitant 50% de risque cardiaque"
   → Le gain ET la perte évitée doivent être dans la phrase

f) MÉTAPHORE / ANALOGIE CENTRALE (le sujet "est comme...")
   → Une seule métaphore filée, mentionnée dès la cover et rappelée 2-3 fois
   → Ex : "Choisir un chat, c'est comme choisir un véhicule pour 15 ans :
       le Sphinx est une voiture de course (séduisant, exigeant, coûteux),
       l'Angora est un break familial (fiable, économique, durable)"

g) AUDIENCE HÉROÏSÉE (profil incarné, pas une étiquette)
   → Identité précise du "héros" de la pres : rôle, âge, contexte, peur,
     désir. La pres doit lui parler à LUI, pas à "les stakeholders".
   → Doit reprendre / approfondir l'AUDIENCE de l'Étape 3.5
   → Ex : "Marc et Sophie, 32 et 28 ans, premiers acquéreurs d'un chat,
          en appartement T3, peur 1 : finir avec des frais véto chroniques,
          peur 2 : choisir un animal qui ne s'adapte pas à leur rythme,
          désir : un compagnon calme pour 15+ ans"
   → L'audience est NOMMÉE quand pertinent (pas obligatoire mais
     puissant) et présente dans le texte du deck via "vous" et projections.
```

**Pourquoi cet artifact est obligatoire** : la conception initiale du process Empirik a privilégié la rigueur factuelle (top-down, dataviz, exhaustivité, sources, charte). C'est puissant mais déséquilibré : sans plan émotionnel explicite, le Claude exécute par défaut un format McKinsey audit où Pathos = 0%. Ce manquement est **structurel**, pas accidentel. La pres v1 "Angora vs Sphinx" a obtenu 100% sur la checklist factuelle mais 55% sur Duarte — preuve que l'angle mort est dans le process lui-même.

Si l'utilisateur a explicitement demandé un **rapport d'analyse** plutôt qu'une **présentation** (cas rare : audit interne, restitution data pure pour comité technique), on peut documenter "Pathos volontairement minimal — usage rapport, pas présentation" comme arbitrage explicite. Sinon, les 6 éléments ci-dessus sont obligatoires.

### Étape 5 — Validation finale avant génération
Présenter le plan détaillé et attendre un "go" explicite.

### Étape 6 — Génération en appliquant STRICTEMENT les guides
Charte design, dataviz, storytelling. Helpers PptxGenJS officiels (voir `PROCESS-ANTI-ERREURS.md`).

### Étape 7 — QA structurée obligatoire + sous-agent exhaustivité OBLIGATOIRE
Après génération : pour CHAQUE slide, dérouler la checklist complète de `PROCESS-ANTI-ERREURS.md` + dataviz §9. Si une case n'est pas cochée → corriger avant de dire "fini". Pas de "ça a l'air OK".

#### Sous-agent #1 — Exhaustivité factuelle (non optionnel)

Au sein de cette étape, lancer **obligatoirement** un sous-agent `general-purpose` avec mission précise :
> "Compare le brouillon source (chiffres, sources, citations, recos) avec les slides générées. Liste TOUT ce qui est dans le brouillon mais absent des slides. Liste TOUT ce qui est dans les slides mais absent du brouillon (= inventé ou supposé). Verdict factuel : score d'exhaustivité X/N."

Un agent qui s'auto-audite a un biais : il valide ses propres choix. Le sous-agent avec fresh eyes rattrape les omissions silencieuses (Artifact 1 de l'étape 4 sert de base). **Pas de sous-agent lancé = étape 7 incomplète.**

#### Sous-agent #2 — Audit Duarte / résonance émotionnelle (non optionnel)

Le sous-agent #1 ne couvre QUE les faits. Il est aveugle au Pathos / Duarte / résonance. Lancer un **2ème sous-agent** avec mission distincte :

> "Tu es un expert Nancy Duarte / Resonate. Audite cette présentation (slides en JPG fournis) pour vérifier sa résonance émotionnelle. Pour chaque point, donne un verdict + une preuve :
>
> 1. **S.T.A.R. moment** : identifie le ou les S.T.A.R. de la pres (sound bite, stat choquante humanisée, visuel évocateur, dramatisation, mini-histoire). Si zéro S.T.A.R. → défaut.
> 2. **Humanisation des chiffres** : liste les chiffres-clés du deck. Lesquels ont une analogie familière (ex : '11 700 €' → 'voyage aux Maldives') ? Lesquels restent froids ? Score : X/Y humanisés.
> 3. **Sparkline (alternance ce qui est ↔ ce qui pourrait être)** : compte combien d'alternances dans le deck. Cible : 4 minimum. Si structure 100% blocs thématiques (Santé / Coût / etc.) sans alternance → défaut Duarte.
> 4. **Nouvelle félicité** : la pres peint-elle le futur transformé entre la reco et le CTA ? Cite la slide précise ou conclus 'absent'.
> 5. **Big idea complète** : la slide synthèse formule-t-elle le point de vue + le gain + la perte évitée ? Ou juste le verdict sec ?
> 6. **Métaphore / analogie centrale** : présente ou absente ? Filée tout au long ?
> 7. **Ratio Logos / Pathos / Ethos** : estime le pourcentage de chaque dimension dans le deck. Si Pathos < 20% sur sujet narratif → défaut.
> 8. **Audience-héros** : est-elle nommée précisément (le futur propriétaire, le décideur cible…) ou en arrière-plan ?
> 9. **Proportions actes** : compte les slides par acte (1 = setup, 2 = contraste, 3 = nouvelle félicité + CTA). Cible Duarte : ~10/80/10%. Tolérance ±10pts.
>
> Verdict final : score Duarte X/9 + liste des défauts à corriger avant livraison."

**Pourquoi 2 sous-agents distincts** : la mission de l'agent factuel et celle de l'agent émotionnel sont **antagonistes** dans leur méthode (l'un compte les chiffres, l'autre évalue la résonance). Les fusionner produit un agent moyen sur les deux. Garder 2 agents séparés = chaque dimension est auditée sérieusement.

**Pas de 2e sous-agent lancé = étape 7 incomplète.** Le Pathos n'est plus un angle mort silencieux.

#### markitdown obligatoire (vérification du texte exporté)

```bash
python -m markitdown <fichier.pptx>
```

Cela affiche le texte tel qu'extrait du PPTX. Sert à :
- Vérifier qu'aucun em-dash n'est resté
- Vérifier les accents diacritiques
- Détecter les erreurs d'encodage
- Comparer rapidement à la version planifiée

### Étape 8 — Rapport QA exhaustif obligatoire (MASTER-CHECKLIST.md)

**Sans ce rapport, pas de livraison.** L'objectif est la **traçabilité explicite** de l'application de chaque règle Empirik à cette présentation, point par point.

#### ⛔ RÈGLE STRUCTURELLE : sous-agent QA INDÉPENDANT (jamais l'agent producteur)

**Le rapport QA est rempli par un sous-agent `general-purpose` indépendant, JAMAIS par l'agent producteur.** L'agent producteur a un biais d'auto-validation systématique : il a coché 17/17 blocs ✅ alors que 3 méritaient ❌ (audit "Angora vs Sphinx v2"). L'auto-évaluation est structurellement compromise.

**Principe d'inversion de la charge de la preuve** : par défaut, le travail a un défaut. C'est à l'agent producteur de fournir des preuves atomiques, le sous-agent QA tranche.

**Mission du sous-agent QA** (à lancer en début d'étape 8) :
> "Tu es l'auditeur indépendant du livrable. Voici MASTER-CHECKLIST.md (~170 items) et le PPTX généré + son script source + le PDF de QA visuelle.
>
> **Mandat strict** : remplis le rapport QA à la place de l'agent producteur. Mode 'devil's advocate' : par défaut chaque bloc est en ❌, c'est à toi de trouver les preuves atomiques qui justifient un ✅. Sans preuve atomique, c'est ❌.
>
> **Règles** :
> - Une preuve atomique = citation directe + référence (slide N, ligne L du script, sortie de commande)
> - Une preuve qui pointe vers un autre ✅ d'un autre bloc est NULLE (anti-cascade)
> - Pour les règles quantifiables (ex : voix vous, em-dashes, ratio dataviz), exiger un comptage explicite
> - Verdict final : score global + liste des blocs ❌ avec justification factuelle"

**Pourquoi cette règle absolue** : l'agent producteur optimise la métrique mesurée (✅ cochés), pas la métrique voulue (qualité réelle). Si on lui demande de remplir la checklist, il maximise les ✅. Le sous-agent QA indépendant ne partage pas ce biais — sa réussite c'est de TROUVER les défauts, pas de valider le travail.

#### Procédure étape 8

1. Créer un fichier `qa-rapport-<nom-pres>.md` à côté du `.pptx` final
2. Copier-coller intégralement le contenu de `MASTER-CHECKLIST.md` dans ce fichier
3. **Lancer le sous-agent QA indépendant** avec le mandat ci-dessus + les fichiers
4. Le sous-agent statue `✅` ou `❌` pour chaque item (~170 au total), avec **preuve atomique pour chaque ✅**
5. L'agent producteur récupère le rapport, lit les ❌, propose des corrections au cas par cas
6. **Pas de cycle infini** : 2 itérations max producteur ↔ auditeur. Si après 2 tours il reste des ❌ sur des blocs non-négociables, signaler explicitement à l'utilisateur pour arbitrage

**Score cible** : 100% ✅ sur les blocs "non négociable" (A, B, C, D, E, F, H, J, K, L, P, R, S, T, U, W, Y, **Z**, **AA**, **BB**, **CC**), ≥ 90% ✅ sur les blocs "qualité" (G, I, M, N, O, Q, V).

#### Format des preuves atomiques (anti-cascade)

| ✅ ATOMIQUE (accepté) | ❌ CIRCULAIRE (refusé) |
|------------------------|--------------------------|
| "vérifié sur slide 7 : '4,5%' bien en orange #E9540D, gras (image qa-slides/slide-07.jpg)" | "preuve = confirmé bloc F" |
| "ligne 234 du script : `fontFace: 'Poppins SemiBold'` confirmé" | "preuve = voir bloc T sur la voix vous" |
| "grep -c '—' build.js → 0" | "preuve = score global 98% donc OK" |
| "comptage manuel : 12 slides sur 24 contiennent 'vous' = 50%, donc ❌ (seuil 70%)" | "preuve = règle §2.2 appliquée" |

Une preuve qui renvoie à un autre ✅ est NULLE. Une preuve doit être traçable à un élément CONCRET du livrable (slide précise, ligne précise, sortie de commande précise).

#### ⛔ Anti-tricherie : ✅ sans preuve atomique = ❌ par défaut

Pour les règles quantifiables (voix "vous", em-dashes, ratio dataviz, exhaustivité brouillon, proportions actes Duarte), exiger un **comptage explicite** dans la preuve :
- ✅ "12 slides standard sur 17 contiennent 'vous'/'votre' = 70,6% → OK (seuil 70%)"
- ❌ "voix vous appliquée partout — ✅"

### Étape 8.5 — Auto-test fidélité (sous-agent Devil's advocate, post-rapport QA)

**Pourquoi cette étape** : même un sous-agent QA indépendant peut laisser passer des preuves circulaires ou superficielles. Une 2ème passe spécifiquement orientée "challenge des preuves" attrape les défauts résiduels.

**Mission du 3ème sous-agent (Devil's advocate)** :
> "Voici le rapport QA produit par le sous-agent QA. Ton mandat unique : challenger TOUTES les preuves des blocs cochés ✅.
>
> Pour chaque ✅ :
> - La preuve est-elle atomique (citation directe + référence fichier:ligne ou slide N) ? Si non → retraite en ❌
> - La preuve est-elle circulaire (pointe vers un autre ✅) ? Si oui → retraite en ❌
> - La preuve est-elle quantifiée pour les règles quantifiables ? Si non → retraite en ❌
> - La preuve est-elle contradictoire avec un fait vérifiable du livrable ? Si oui → retraite en ❌
>
> Focus prioritaire (blocs historiquement laxistes) : voix 'vous' (Bloc BB), couverture brouillon (Artifact 1), contraste stratégique (Bloc F), exhaustivité PDF source (Bloc U), conformité Duarte (Bloc Z).
>
> Verdict final attendu : nombre de ✅ retraités en ❌. Si > 3 retraitements, le rapport QA initial est REJETÉ, l'agent producteur doit recommencer avec corrections."

**Pas de livraison sans Étape 8.5 passée.** Cette étape attrape les "✅ déclaratifs" que le sous-agent QA aurait laissé filer.

---

## 1. RÈGLES DE PROCESS (workflow général)

### 1.1 Workflow fichiers de data
Quand l'utilisateur fournit un fichier de data : ranger dans `data-brute/` du projet, consigner le contexte, **attendre** la demande d'analyse. Ne pas lancer d'exploration automatique.

### 1.2 Pas d'invention de data + distinction DATA vs CALCUL vs ESTIMATION

Échec API, extraction incomplète, donnée ambiguë → **signaler explicitement**, jamais combler par de l'inventé. Préférer "X/N réussis, Y erreurs" à un résultat propre fabriqué.

#### Convention typographique obligatoire : 3 catégories de valeurs

Toute valeur numérique affichée sur une slide doit appartenir à l'une de ces 3 catégories, **visuellement distinguées** :

| Catégorie | Définition | Format slide | Footnote requise |
|-----------|------------|--------------|------------------|
| **1. DATA SOURCÉE** | Valeur directement issue du brouillon ou d'une source citée | Format normal : `4,5%` | Mention de la source en footer (`Source : LLM Brand Tracker · Mai 2026`) |
| **2. CALCUL RECONSTRUIT** | Valeur obtenue par addition/multiplication/extrapolation d'hypothèses | Préfixe `~` : `~11 700 €` | Footnote obligatoire : `*estimation calculée à partir de [hypothèses A + B + C]` |
| **3. ESTIMATION FRAGILE** | Valeur marquée "à vérifier" ou "à confirmer" dans le brouillon, ou source non vérifiée | Badge orange `à reconfirmer` visible sur la slide | Mention explicite du caractère non confirmé |

**❌ Interdiction** : présenter une valeur de catégorie 2 ou 3 comme si c'était une catégorie 1 (sans marquage visuel). Bug commis sur "Angora vs Sphinx" : "11 700 € sur 15 ans" présenté comme un total ferme alors que c'était un calcul reconstruit à partir de 5 hypothèses non sourcées.

**✅ Exemple correct** :
- DATA : `4,5%` + footer `Source : Brand Tracker · Mai 2026`
- CALCUL : `~11 700 €*` + footnote `*estimation = 500€/an chauffage + 320€/an véto + 150€/an soins × 15 ans, hypothèses non sourcées`
- ESTIMATION : `+40% frais véto` + badge `à reconfirmer` (annoncé "à vérifier" dans le brouillon)

**Pourquoi cette règle** : sans distinction visuelle, l'audience traite un calcul reconstruit comme un fait établi. C'est de la fausse précision qui se retourne contre la crédibilité de l'agence quand le client challenge la valeur.

### 1.3 Challenger chaque reco (avant validation du plan)
Pour chaque reco que l'utilisateur formule ou que je propose, mode brainstorming avocat du diable :
- **Pourquoi** cette reco ? (objectif business / GEO)
- **Quelle preuve** qu'elle marchera ? (étude externe, observation interne, retour d'XP, hypothèse)
- **Impact attendu** mesurable ou qualitatif ?
- **ROI estimé** vs effort / coût ?
- **Limites / risques** ?
- **Comment l'expliquer au client** simplement ?

Identifier les recos faibles (pas de preuve, ROI flou) et le signaler explicitement. Identifier les **contradictions** avec d'autres données du projet. À faire **avant** validation du plan storytelling, pas pendant la génération PPTX.

### 1.4 Pas de conclusions dans les rapports markdown
Dans les fichiers d'analyse type `analyse-resultats.md` : data brute uniquement (tableaux, chiffres, qualité de données). **Pas** de sections "Lecture / Insight / Implications / Pistes d'action / TL;DR interprétatif". Formulations à virer : "domination écrasante", "convergence", "levier clé". L'utilisateur tire ses propres conclusions.

> Cette règle concerne les **fichiers de restitution d'analyse**, pas les slides. Les slides ont besoin de titres-constats (voir §2.7).

### 1.5 Audit GEO — fact-check focalisé client
Quand on audite les connaissances LLM sur une marque :
- Fact-checker **uniquement le client**, pas les concurrents. Ce qui intéresse le client : "le LLM dit-il du faux sur moi ?"
- Le fact-check se fait par **lecture des outputs**, pas par heuristique de termes ou regex
- Citer le verbatim exact du LLM dans le livrable
- Conclure clairement : "✅ confirmé", "❌ faux : la réalité est …", "⚠️ partiellement faux : …"
- Ne pas fact-checker les dates/lieux qui bougent souvent

### 1.6 Validation pertinence métier des concurrents
Ne pas inclure un acteur dans une liste de concurrents juste parce qu'il apparaît dans le secteur ou dans le top of mind LLM. Critère : "même type de produit/salon, même cible". Si un nom remonte d'un Brand Tracker, c'est un signal "présence catégorielle" pas "concurrence directe". En cas de doute, demander.

---

## 2. RÈGLES DE FOND (contenu / structure)

### 2.1 Communication top-down (pyramide McKinsey)
Toute pres commence par la **conclusion/recommandation** avant le détail. À 3 niveaux :

1. **Pres globale** : slide "Synthèse / Recommandation" **systématique** juste après la slide de couverture. Format : 1 phrase de reco complète + 3 piliers max. Variantes :
   - Pitch / avant-vente : "Notre recommandation pour [client] : [action concrète]"
   - Audit / bilan : "Ce que révèle l'audit : [constat principal]"
   - Restitution data : "Le résultat clé : [chiffre + interprétation]"
   - Présentation stratégique : "Notre conviction : [thèse]"

2. **Chaque section** : slide "Ce qu'il faut retenir de cette section" juste après la slide chapitre. Format : constat principal + conséquence (1 phrase chacun).

3. **Chaque slide** : titre porte la conclusion, contenu apporte les preuves. Voir §2.7 titres-constats.

**Slides de recommandation** : plutôt qu'une slide "Nos recommandations" en liste, **une slide par reco** avec TITRE = phrase d'action complète + CONTENU = pourquoi / comment / impact.

**Test de validation** : lire uniquement la slide synthèse + les slides "ce qu'il faut retenir" + les titres → l'argumentaire complet doit ressortir. L'audience doit pouvoir quitter la pres après la slide 2 et avoir le message principal.

**Recommandation finale OBLIGATOIRE** : chaque deck data se termine par une action recommandée explicite. Formule type : `Nous recommandons de <verbe action> pour <résultat attendu>`. Donner une option imparfaite vaut mieux que "voici les données, à vous de décider" — cela recentre la discussion sur "comment agir" plutôt que "donnez plus de data". **Si après l'analyse aucune action n'est formulable** (pas de leviers, pas de hypothèse à tester) → ce n'est pas une présentation, c'est de la donnée brute : la livrer en rapport markdown, pas en deck. Source : Knaflic / Storytelling with Data.

### 2.2 Perspective "vous" (client) — quantifiée et auto-vérifiable

- ❌ "Nous allons faire", "notre équipe"
- ✅ "Vous allez bénéficier", "votre marque", "vos consommateurs"

La présentation parle AU client, pas DE ce que fait l'agence.

#### Seuil quantifié obligatoire (anti-règle-floue)

La règle "voix vous partout" est qualitative et permet le glissement silencieux ("4 slides sur 24 contiennent vous" → coché ✅ à tort dans l'audit Angora v2). **Règle quantifiée stricte** :

- **Toute slide standard** (hors cover, section dividers, citation pure, CTA) **DOIT contenir au moins UNE occurrence** de `vous` / `votre` / `vos` dans le titre OU dans le corps.
- **Seuil minimal acceptable au niveau du deck** : 70% des slides standard contiennent au moins une occurrence "vous".
- **Si < 70% → défaut bloquant**, à corriger en reformulant les titres et contenus à la 3e personne (le client / le propriétaire / le décideur) vers la 2e personne (vous / votre).
- **"Nous" est INTERDIT** sauf dans "Nous recommandons" en titre d'une slide reco unique finale (et même là, préférer "Adoptez..." / "Choisissez..." pour rester en "vous").

#### Auto-test grep obligatoire avant livraison

```bash
# Compter les occurrences "vous/votre/vos" dans le script :
grep -ciE "\\b(vous|votre|vos)\\b" build_xxx.js

# Comparer au nombre de slides standard (= total slides - cover - dividers - CTA)
# Si ratio < 70% → corriger AVANT export
```

Ce test doit apparaître explicitement dans le rapport QA (Bloc BB de MASTER-CHECKLIST), avec le comptage chiffré comme preuve atomique.

### 2.3 Expliquer les concepts techniques visuellement
- Ne jamais supposer que le client connaît les termes (queries fan out, Common Crawl, GEO…)
- Toujours rappeler "GEO = optimisation pour les IA génératives"
- Schémas plutôt que définitions textuelles

### 2.4 Légende source obligatoire sur chaque slide de data
Chaque slide qui présente un chiffre, un graphique ou un tableau doit afficher :
- **D'où vient la data** : GA4, Google Search Console, LLM Brand Tracker, DataForSEO, étude qualitative Empirik, audit interne…
- **Quelle période** : "avril 2026 vs mars 2026", "mars-mai 2026", "18/03 → 06/05/2026"…
- **Propriété/périmètre** quand pertinent : "[Marque client], segment LLM", "N villes franchisées", "N mots-clés [marché]"

**Format** : légende discrète en bas de slide, 10-11pt, gris foncé ou bleu Empirik atténué. Type : *"Source : GA4, [Nom client], segment Traffic LLM, [période vs période]"*.

Si plusieurs sources : les lister toutes. Pour les slides constat / question / reco sans data : pas de légende.

**Mise en page stats** : prioriser visuellement le chiffre brut (gros, dominant), évolution vs mois précédent en petit en dessous. Ex : `119` en gros, `+58,7% vs mars` en petit.

### 2.5 URL cliquables sur sources externes
Quand une slide mentionne une fiche Wikipedia, Wikidata, un site source, un article, un dashboard → l'URL doit être **cliquable** (`{ hyperlink: { url: "..." } }` dans PptxGenJS), pas juste une référence textuelle. À vérifier en QA en ouvrant le PPTX.

### 2.6 Logos officiels obligatoires
Quand une slide mentionne un outil/marque/service connu (LLMs, navigateurs, plateformes, concurrents, médias, forums sectoriels…), intégrer son logo officiel.

**Workflow pre-flight obligatoire** (AVANT la 1ère ligne de code PptxGenJS) :
1. Lister TOUS les noms propres dans le contenu (marques, outils, sites, médias, concurrents)
2. Vérifier ce qui existe déjà dans `assets/logos/`
3. Pour les manquants → lancer le script de récupération automatique :
   ```bash
   python scripts/fetch_logos.py --simpleicons <slugs> --wikipedia "<File.svg>=<dest>" --scrape "<https://...>=<dest>"
   ```
4. Tester chaque PNG résultant (vrai PNG ≥ 1KB, pas un SVG ni un fichier corrompu)

**Le script `scripts/fetch_logos.py`** implémente une méthode **4 couches** en cascade automatique :
- **Layer 1 — simpleicons.org CDN** (SVG monochrome, format vectoriel) : pour tech brands populaires (cloudflare, perplexity, googleanalytics, googlegemini…)
- **Layer 2 — Wikipedia Commons API** (`iiurlwidth=400` → PNG serveur-rendu HD) : pour marques connues avec entrée Wikipedia (ChatGPT, Bing, Microsoft…)
- **Layer 3 — Scraping HTML multi-pages** : home + `/press` + `/press-kit` + `/media` + `/brand` + `/brand-assets` + `/about` + `/qui-sommes-nous`. Sur chaque page : `apple-touch-icon`, `og:image`, `<link rel="icon">`, `<img class="logo">`, `<svg id="logo">`, `<a class="logo"><img>`, liens de téléchargement explicites (`/logo.png`, `/brand.svg`). Avec rotation automatique de User-Agent (Chrome / Firefox+Referer Google / Safari+Referer DuckDuckGo) en cas de 403/429.
- **Layer 4 — brandfetch.com API publique** (fallback puissant) : pour les sites résistants au scraping (Cloudflare, JS challenge, 403 persistant). Couvre la plupart des marques B2B reconnues qui résistent aux Layer 1-3.

**Mode auto recommandé** quand on n'est pas sûr de la couche qui marchera :
```bash
python scripts/fetch_logos.py --auto "lemoniteur=lemoniteur" "dispano=dispano" "pointp=pointp"
```
Le mode `--auto` essaie les 4 couches en cascade jusqu'à trouver. Si les 4 échouent, on passe aux méthodes manuelles d'escalade ci-dessous.

Détails complets et cas limites (403 Forbidden persistant, SSL fail, slugs introuvables, fallback manuel) dans `PROCESS-ANTI-ERREURS.md` Erreur #5.

**Format à intégrer** : PNG transparent (PptxGenJS gère mieux que SVG), 30-60px de haut, version colorée sur fond blanc / monochrome blanche sur fond bleu Empirik.

**Ne JAMAIS attendre la QA finale pour intégrer les logos** — c'est une erreur fréquente : on découvre tard que 8 logos manquent, alors qu'on aurait pu les fetcher en 5 min en pre-flight.

#### Persistance obligatoire — ne JAMAIS abandonner sur un logo

> Un logo existe toujours quelque part. Si tu n'arrives pas à le récupérer, c'est que tu n'as pas essayé assez de méthodes. Abandonner avec un message "logo introuvable" est un défaut bloquant, pas une issue acceptable.

**Si les 3 couches automatiques échouent sur une marque, escalader avec ces méthodes manuelles AVANT d'abandonner** :

1. **Crawler le site officiel en profondeur** (pas juste la home) :
   - `/press`, `/press-kit`, `/media`, `/media-kit`, `/brand`, `/brand-assets`, `/about`, `/about-us`, `/qui-sommes-nous`, `/identité-visuelle`
   - Ces pages contiennent souvent un kit logo téléchargeable (PNG/SVG en haute résolution)
2. **Inspecter le HTML de la home** au-delà des balises meta :
   - `<img>` avec attributs `class` ou `alt` contenant "logo", "brand"
   - `<svg>` inline avec id/class contenant "logo"
   - `<header>`, `<nav>`, `<footer>` — c'est presque toujours là que se trouve le logo principal
3. **CSS background-image** dans les feuilles de style :
   - Récupérer le HTML, parser les `style="background-image:url(...)"` et les classes CSS qui font référence à des images "logo"
4. **Wikipedia chercher avec variantes du nom** :
   - Nom officiel (`Le Moniteur` → `Groupe Moniteur`), avec/sans suffixe SA, magazine, fr…
   - Page de la marque parente si filiale (`Point P` → `Saint-Gobain Distribution Bâtiment France`)
5. **Wikipedia EN** : si la version FR n'a rien, tester en anglais (`fr.wikipedia.org` → `en.wikipedia.org`)
6. **Brandfetch.com / logo.wine / 1000logos.net** : agrégateurs tiers gratuits, à interroger en fallback (`https://api.brandfetch.io/v2/brands/<domain>` retourne un JSON avec URLs des logos)
7. **Google Images / DuckDuckGo Images** : recherche `<marque> logo png transparent` → récupérer la 1ère image carrée propre
8. **Bypass 403 Forbidden** : changer le User-Agent (`Mozilla/5.0 ... Firefox/121.0`), ajouter `Referer: https://google.com`, retenter
9. **Bypass SSL fail** : `urllib.request` avec `ssl._create_unverified_context()` (sites avec cert auto-signé)
10. **Wayback Machine** : si le site officiel est mort ou bloqué, `https://web.archive.org/web/<date>/<url>` retrouve une version récente

**Règle d'arbitrage** : tu n'as le droit d'écrire "logo introuvable" dans le rapport QA QUE si tu as documenté les 10 méthodes ci-dessus essayées et leur échec. Sinon, continue jusqu'à trouver.

**Astuce pratique** : pour le scraping du site officiel, télécharger le HTML complet (`curl -L`) et chercher avec `grep -oE 'src="[^"]*logo[^"]*\.(svg|png)"'` ou inspecter visuellement avec un agent multimodal. La balise `<img>` qui affiche le logo dans le header de la home **existe presque toujours**.

#### ⛔ QA visuelle pre-flight OBLIGATOIRE de chaque logo avant intégration

Avant d'intégrer un logo via `slide.addImage()`, **ouvrir le PNG dans le Read tool** (Claude est multimodal) et confirmer visuellement les 3 critères :

1. **Identité correcte** : le logo correspond bien à la marque réelle (pas un placeholder texte, pas une autre marque par confusion de slug)
2. **Version actuelle** : c'est la version actuelle du logo (pas une version retirée par la marque depuis)
3. **Format exploitable** : vrai PNG ≥ 1 KB, fond transparent, pas un fichier corrompu

Si l'un des 3 critères échoue → **relancer `fetch_logos.py --auto`** ou les méthodes manuelles d'escalade ci-dessus sur cette marque, AVANT la première ligne de code PptxGenJS qui l'utilise. Ne JAMAIS intégrer un logo "à l'aveugle" parce que le fichier existe dans `assets/logos/` — un fichier en cache d'une session précédente peut être un placeholder oublié ou une version obsolète.

#### Refresh forcé des logos LLM / IA en début de session

Les marques d'IA génératives évoluent vite (Claude a eu 3 versions de logo en 18 mois, Gemini en a eu 2, ChatGPT en a eu 2). Un PNG en cache de plus de 3 mois est probablement obsolète.

**Règle automatique** : pour chacune des marques de la liste ci-dessous, **toujours regénérer le logo en début de session** (même si le cache `assets/logos/` existe), puis appliquer la QA visuelle pre-flight ci-dessus :

```
ChatGPT / OpenAI · Claude / Anthropic · Gemini / Bard / Google AI ·
Perplexity · Mistral · Copilot / Microsoft Copilot · Grok / xAI ·
DeepSeek · Llama / Meta AI · Cohere · Pi / Inflection
```

Commande type à lancer en pre-flight si une pres cite des LLMs :
```bash
python scripts/fetch_logos.py --auto \
  "openai=chatgpt" "anthropic=claude" "googlegemini=gemini" \
  "perplexity=perplexity" "mistral=mistral"
```

Pour les marques B2B classiques (concurrents sectoriels, médias, plateformes établies), le cache est généralement OK mais la QA visuelle reste obligatoire.

### 2.7 Titres de slides — constats concrets, pas étiquettes
- **Constat, pas étiquette** : "Un score insuffisant pour atteindre une top position" au lieu de "Score de qualité de la page"
- **Nommer précisément** : "L'expertise, l'originalité et l'effort doivent être retravaillés" au lieu de "Les 3 critères les plus faibles"
- **Connecteurs entre slides** d'une même section : "Ainsi que…", "Autre point,…", "Enfin,…"
- **Pas de jargon EN en label** : "Le premier écran est décisif" au lieu de "Above-the-fold : le premier écran est décisif"
- **Reco = constat + action** : "Corps de l'article : casser la monotonie en intégrant des blocs, infographies…"
- **Test ultime** : lire UNIQUEMENT les titres dans l'ordre → on doit comprendre tout l'argumentaire

**Titre takeaway, pas titre descriptif** (source Knaflic) : le titre porte le message que l'audience doit retenir, pas le sujet du graphe.

| ❌ Titre descriptif (sujet) | ✅ Titre takeaway (message) |
|------------------------------|------------------------------|
| Ventes par trimestre 2025 | Le T3 dépasse la cible pour la 1re fois en 4 ans |
| Tickets reçus vs traités | L'écart de tickets non traités a doublé depuis mai |
| Évolution NPS | Le NPS chute de 12 points après le pricing change |
| Part de voix LLM par concurrent | Vous êtes cité dans 4,5% des réponses LLM, contre 24,3% pour Dispano |
| Analyse des fan-out queries | Vous êtes invisible sur les queries commerciales à plus forte intention d'achat |

Étude Knaflic : avec un titre takeaway, l'audience retient mieux le message. Sur une slide data, le titre = le verdict, pas l'en-tête de tableau.

**Deux tests de relecture à faire systématiquement avant de livrer** :

1. **Test narratif (sur l'ensemble du deck)** : lire UNIQUEMENT les titres dans l'ordre. L'histoire doit être compréhensible et s'enchaîner sans contenu. Si un titre rompt le fil ou semble hors-sujet → revoir le titre ou la position de la slide.

2. **Test de fit bi-directionnel (sur chaque slide individuellement)** :
   - Le **contenu de la slide renforce-t-il la pertinence du titre** ? (le contenu apporte les preuves / le détail qui font tenir le titre)
   - Le **titre renforce-t-il la pertinence du contenu** ? (le titre éclaire ce que l'audience doit retenir du contenu, sans le titre on ne saurait pas où regarder)

   Si l'un des deux côtés ne tient pas (titre générique qui ne colle pas à la spécificité du contenu, ou contenu qui dit autre chose que le titre) → la slide est cassée, il faut soit retitrer, soit retravailler le contenu, soit splitter en deux slides.

### 2.8 Pas de tiret cadratin (—) dans les slides
Jamais de — dans les titres ou contenus. Remplacer par : virgule, deux-points, point-virgule, parenthèses, point médian (·), ou point. À vérifier avant export :
```bash
grep -c "—" build_xxx.js  # DOIT renvoyer 0
```

### 2.9 Vigilance accents / diacritiques
Aucun mot français ne doit perdre ses accents. Mots à surveiller : `à` vs `a`, participes passés (`-é -és -ée -ées`), `où` vs `ou`, `dû/sûr/là/déjà/c'est-à-dire/très/après/dès/près/succès/accès`. Caractères spéciaux : `œ` (cœur, œuvre, sœur), `Ç/ç`, apostrophes typographiques.

**Ne JAMAIS** substituer un accent par ASCII pour "simplifier" un script. Encodage UTF-8 obligatoire de bout en bout.

---

## 3. RÈGLES DE FORME (charte Empirik)

### 3.1 Couleurs
- **Bleu principal** : `#0A3856` — Titres, texte courant, éléments importants
- **Orange accent** : `#E9540D` — Mise en valeur, CTA, chiffres clés, élément vedette dans un graphique
- **Jaune accent** : `#FCC02D` — Highlights décoratifs, icônes
- **Blanc fond** : `#FFFFFF` — Arrière-plan de TOUTES les slides (sauf sections et CTA)

**INTERDIT** : texte ou chiffre en jaune `#FCC02D` sur fond blanc (contraste insuffisant). Le jaune est OK seulement en accent décoratif (bord de carte, fond de badge avec texte bleu/blanc par-dessus, icône).

En PptxGenJS : couleurs SANS `#` → `"0A3856"`, `"E9540D"`, `"FCC02D"`, `"FFFFFF"`.

### 3.2 Typographie Poppins
| Élément | Taille | fontFace | Couleur | Alignement |
|---------|--------|----------|---------|------------|
| Sur-titre de section | 12pt | `"Poppins ExtraLight"` | #E9540D | Centré |
| Titre principal | 22pt | `"Poppins SemiBold"` | #0A3856 | Centré |
| Sous-titre | 18pt | `"Poppins Medium"` | #0A3856 | Centré |
| Texte courant | 14pt | `"Poppins"` (Regular) | #0A3856 | Gauche |
| Légende / Source | 10-11pt | `"Poppins"` | gris ou bleu atténué | Gauche |
| Chiffre clé | 48-72pt | `"Poppins Bold"` | #E9540D | Centré |

**REGLE TECHNIQUE CRITIQUE PptxGenJS** : utiliser le **nom de police variant** dans `fontFace`, JAMAIS `fontWeight` (silencieusement ignoré → rend en Regular).

- ❌ `fontFace: "Poppins", fontWeight: 600` → rend Regular
- ❌ `fontFace: "Poppins", bold: true` → rend Bold (pas SemiBold)
- ✅ `fontFace: "Poppins SemiBold", bold: false` → rend SemiBold

### 3.3 Mise en page
- Marges : 60px minimum de chaque côté (0.6" en PptxGenJS, `LAYOUT_16x9`)
- Espacement titre/contenu : 40px minimum
- Maximum 6 bullet points par slide
- Maximum 2 niveaux d'imbrication
- Coins arrondis : 8px
- Texte ≥ 12pt (sauf footer/légende 10-11pt OK)
- Bullets niveau 1 : cercle plein #E9540D
- Bullets niveau 2 : cercle vide ou tiret #0A3856

### 3.4 Sur-titre + titre — positionnement précis

**Layout** :
```
              [sur-titre orange ExtraLight 12pt, CENTRÉ]
         [TITRE PRINCIPAL bleu SemiBold 22pt, CENTRÉ]
```

Les deux blocs forment un ensemble compact, centré, **proche du haut de la slide** (pas au tiers supérieur).

**Valeurs PptxGenJS** (slide 10" × 5.625") :
- Sur-titre : `y = 0.30`, `h = 0.28`
- Titre principal : `y = 0.60`, `h = 0.7` (juste sous le sur-titre)
- Ou variante compacte du helper officiel : sur-titre `y=0.18`, titre `y=0.46`

**Sur-titre = nom de la section/chapitre courant**. Sur TOUTES les slides standard. **Sauf** : slide de couverture, slides chapitres/sections, slide CTA finale.

**Écriture du sur-titre** : casse normale (1ère lettre cap), pas de `charSpacing`, pas de `.toUpperCase()`.
- ❌ `M I S S I O N`, `C Ô T É   F I D U C I A L`, `CAS 1`, `OPTION 1`
- ✅ `Mission`, `Côté client`, `Cas 1`, `Option 1`

Acronymes courants en MAJ OK : SEO, GEO, CTA, KPI, TPE, CMS…

### 3.5 Slide de couverture — template strict (TOUJOURS appliqué, pas de question à poser)

**Principe** : toute pres générée via ce système est par défaut une pres Empirik, livrée sous l'identité de l'agence. Le template cover est **systématiquement appliqué**, logo Empirik inclus. **Ne JAMAIS demander à l'utilisateur "est-ce une pres perso ou Empirik ?"** — par défaut c'est Empirik.

Si l'utilisateur veut explicitement une cover sans logo Empirik (cas vraiment exceptionnel, ex : test personnel), il doit le dire de lui-même de manière explicite. En l'absence d'instruction contraire, appliquer le template Empirik intégral.

**Template intégral (à appliquer systématiquement)** :
1. **En haut** : logo Empirik (gauche, obligatoire) + logo client (droite, si pres pour un client) alignés verticalement
2. **Ligne horizontale fine** de séparation sous les logos
3. **Côté gauche (~50%)** : grande image d'ambiance liée au sujet de la pres, bords carrés, hauteur pleine
4. **Côté droit (~45%)** :
   - **Titre principal** ~48-60pt, Poppins **Bold**, orange `#E9540D`, aligné gauche, 1-2 lignes
   - Petit trait orange horizontal sous le titre
   - **Sous-titre** ~20pt Poppins Regular, bleu `#0A3856`
   - **Date** ~20pt Poppins Bold, bleu `#0A3856`
5. **Motif décoratif** : petite grille de carrés jaunes `#FCC02D` en bas, entre l'image et le bloc texte

**Image** : si non fournie → `python scripts/generate_image.py --type cover --output assets/cover.png`.

**Logo Empirik** : AUTORISÉ uniquement sur la slide cover. INTERDIT sur toutes les autres slides (chapitres, contenu, CTA, fin). Mais sur la cover, il est OBLIGATOIRE — sa présence n'est jamais une question optionnelle.

### 3.6 Types de slides à varier
- Slide section (fond bleu foncé) — introduire une nouvelle partie
- Slide transition numérotée — gros numéro + titre pour étapes
- Slide 2 cartes — comparaison côte à côte
- Slide 3 cartes — options/personas/étapes
- Slide avec placeholder image — `[SCREENSHOT : description]` rectangle gris arrondi
- Slide schéma/concept — étapes visuelles avec flèches
- Slide question client (fond crème `#FDF8F0`, icône `?` orange, question centrée) — à intégrer régulièrement pour créer interaction
- Slide CTA (fond bleu, bouton orange)

**Règle visuelle non négociable** : jamais de slide texte-only. Chaque slide a un élément visuel central.

### 3.7 Alignement strict de tous les éléments

**Principe** : tous les éléments d'une slide (et d'un graphique) doivent être alignés sur une grille invisible. L'alignement strict est une part majeure de l'esthétique professionnelle. Un seul élément désaligné se voit immédiatement et fait passer la slide pour "amateur".

**Règles concrètes** :

- ✅ **Alignement horizontal** : tous les éléments d'une même rangée partagent la **même coordonnée Y** (haut, centre, ou bas — au choix mais cohérent)
- ✅ **Alignement vertical** : tous les éléments d'une même colonne partagent la **même coordonnée X** (gauche, centre, ou droite — cohérent)
- ✅ **Bords de cartes côte à côte** : exactement même largeur, même hauteur, mêmes espacements entre elles (calculer mathématiquement, pas "à l'œil")
- ✅ **Texte dans une carte / une cellule** : aligné gauche par défaut, à l'exception des titres centrés et des chiffres alignés droite
- ✅ **Nombres dans un tableau** : alignés à droite, avec **même nombre de décimales** (`4,5%` et `24,3%` ensemble, pas `4,5%` et `24%`)
- ✅ **Texte dans un tableau** : aligné à gauche
- ✅ **Icônes / numéros / badges** : centrés dans leur conteneur, alignés horizontalement avec le texte qu'ils accompagnent (baseline ou centre selon le cas)
- ✅ **Sources / footnotes** : alignées à gauche en bas de slide, même position Y partout dans le deck
- ✅ **Sur graphes** : labels d'axes alignés sur les ticks, étiquettes de barres horizontales toutes au même niveau, légendes (si présentes) à position cohérente entre slides

**Test rapide** : tracer mentalement des lignes verticales et horizontales sur la slide. Tous les éléments doivent toucher ces lignes. Si un élément "flotte" à 5px du bord de son voisin, c'est une faute d'alignement.

**En PptxGenJS** : utiliser des constantes pour les coordonnées (`const COL_X = 0.55;` réutilisée sur 3 colonnes). Ne jamais "ajuster à l'œil" de 0.02" en plus ou en moins, car cela casse l'alignement de la slide suivante qui réutilise le même layout. Calculer les positions à partir d'une grille (largeur slide - 2×marge) / N colonnes.

---

## 4. RÈGLES DATAVIZ (ajout process)

### 4.1 Type de graphique justifié explicitement
Pour chaque slide contenant de la data, au moment du plan détaillé (étape 4), j'écris explicitement :
> "Slide N : objectif = [comparer / distribuer / corréler / évoluer] → selon `dataviz-guide §1` = [type X]. Pourquoi pas barres : [raison]."

L'utilisateur valide la pioche **avant** que je code.

### 4.2 Variété obligatoire — éviter le réflexe barres
Mon biais par défaut est "barres horizontales + gros chiffre orange". Le `dataviz-guide.md §1` propose 7 familles de visualisation à mobiliser selon l'objectif :
- **Montants** : barres, dot plot, heatmap
- **Distributions** : histogramme, density, boxplot, violin, ridgeline
- **Proportions** : barres empilées, treemap, mosaic, pie (si simple)
- **Relations X-Y** : scatter, hexbin, contours de densité, matrice de corrélation
- **Séries temporelles** : ligne, area, multi-lignes étiquetées, **slopegraph**
- **Incertitude** : barres d'erreur, violin, quantile dot plot
- **Small multiples** : sous-ensembles avec axes identiques

### 4.3 Patterns spécifiques — Storytelling with Data (Knaflic)

#### Slopegraph — comparer 2 périodes × N catégories
Source : Cole Nussbaumer Knaflic, *Storytelling with Data*.

**Quand l'utiliser** :
- Deux périodes (ex : mars vs avril, 2024 vs 2025) et N catégories
- Objectif : montrer rapidement **les augmentations, baisses et différences relatives** entre catégories
- Plus puissant que des barres groupées pour faire ressortir une trajectoire individuelle

**Comment le construire dans la charte Empirik** :
- Axe gauche = période 1, axe droite = période 2, lignes reliant chaque catégorie
- Étiquettes directes en bout de ligne (nom de catégorie + valeur), pas de légende
- **Si beaucoup de lignes → griser les secondaires** (couleur gris clair `#BFBFBF` ou bleu atténué) et **mettre la ligne vedette en orange Empirik `#E9540D`** + épaissir le trait
- L'élément vedette = le client, le segment qu'on veut faire ressortir, ou la variation la plus marquante
- Annotation textuelle courte près de la ligne orange pour expliquer le constat (ex : "+58,7%, plus forte hausse du panel")
- Pas de grille verticale, pas de cadre, juste les deux étiquettes d'axe en haut (les noms des périodes)

**Erreur à éviter** : montrer 15 lignes toutes en couleur → illisible. Le slopegraph ne marche qu'avec un focus narratif clair.

#### Waterfall chart — décomposer une variation ou un cumul
Source : Cole Nussbaumer Knaflic, *Storytelling with Data*.

**Quand l'utiliser** :
- Décomposer un stacked bar chart pour montrer **une pièce à la fois** et la focaliser
- Montrer un **point de départ + une série d'augmentations et de baisses + le résultat final** (variation budgétaire, évolution de trafic, décomposition de chiffre d'affaires, etc.)
- Plus narratif qu'un stacked bar : l'audience suit la logique pas à pas

**Comment le construire dans la charte Empirik** :
- Barre de départ en bleu Empirik `#0A3856`
- Barres d'augmentation en orange `#E9540D` (ou vert `#10A050` si la convention "positif = vert" doit primer)
- Barres de diminution en gris atténué (jamais rouge agressif, garder la palette charte)
- Barre finale en bleu Empirik, soulignée par un trait orange dessous pour marquer le résultat
- Étiquettes directes au-dessus de chaque barre (valeur + signe), pas de légende
- Axe Y : optionnel, peut être supprimé si les étiquettes directes suffisent
- Titre = message qui annonce le constat ("De 100 visiteurs LLM à 142 en 3 mois : voici comment")

**Erreur à éviter** : utiliser un waterfall quand il n'y a pas de logique séquentielle. Si les composantes n'ont pas d'ordre causal ou temporel, préférer un stacked bar simple.

#### Ordre logique des catégories
Source : Cole Nussbaumer Knaflic, *Storytelling with Data*.

Sur tout graphique présentant des données catégorielles (barres, dot plot, heatmap, slopegraph…), réfléchir explicitement à **l'ordre des catégories**. Ce n'est jamais neutre.

**Si l'ordre est naturel → le respecter** :
- Tranches d'âge : 0-10, 11-20, 21-30…
- Mois / trimestres / années : ordre chronologique
- Étapes d'un funnel / parcours : suivre la séquence
- Échelles ordinales : très faible → faible → moyen → fort → très fort
- Notes / niveaux : F → A, ou 1 → 5

**S'il n'y a pas d'ordre naturel → choisir un ordre qui sert le message** :
- Par défaut : trier par valeur **décroissante** (catégorie la plus grande en haut/gauche, l'œil va du plus important au moins)
- Si on veut mettre en avant la catégorie la plus faible : trier par valeur **croissante** + accent orange sur le bas
- Si on veut grouper par similarité : ordonner par cluster (mais étiqueter clairement les groupes)
- Alphabétique : seulement si l'audience cherche un nom précis (annuaire), jamais par défaut

**Erreur à éviter** : laisser l'ordre que retourne l'outil par défaut (souvent alphabétique ou ordre d'insertion). Toujours **choisir** consciemment l'ordre selon le message à porter.

#### Stacked horizontal bar chart — totaux + sous-composantes
Source : Cole Nussbaumer Knaflic, *Storytelling with Data*.

**Quand l'utiliser** :
- Montrer le **total** par catégorie ET donner une idée des **sous-composantes** qui le composent
- Deux structures possibles :
  - **Valeurs absolues** : longueur de chaque barre = total de la catégorie (utile quand les totaux varient et qu'on veut les comparer)
  - **Sum to 100%** : toutes les barres ont la même longueur, chaque segment représente une part en pourcentage (utile pour comparer la composition entre catégories indépendamment du volume)

**Pourquoi horizontal plutôt que vertical** :
- Les labels de catégories tiennent mieux à l'horizontale (pas d'inclinaison)
- L'œil compare plus naturellement les longueurs horizontales
- Sur slide 16:9, plus de place pour les labels à gauche

**Comment le construire dans la charte Empirik** :
- Catégories à gauche, axe en bas (ou supprimé si étiquettes directes sur les segments)
- Max 5-6 segments par barre (au-delà, illisible)
- Couleurs : utiliser la palette charte avec un dégradé maîtrisé (bleu Empirik en variantes d'intensité, ou bleu/orange/jaune si segments très différents)
- Étiquettes directes dans chaque segment quand la largeur le permet (valeur + %)
- L'élément vedette en orange `#E9540D`, les autres en bleu Empirik atténué
- Ordre des segments **cohérent entre les barres** (même séquence de catégories partout)
- Ordre des barres : selon §4.3 "Ordre logique des catégories"

**Erreur à éviter** : empiler 8+ catégories qui deviennent illisibles. Si trop de segments, en regrouper certains dans "Autres" (avec note explicative).

#### Éviter les area graphs
Source : Cole Nussbaumer Knaflic, *Storytelling with Data*.

Les **area charts** (graphiques en aires, qu'ils soient simples ou empilés) sont à **éviter** dans les pres Empirik :
- L'œil estime mal les surfaces (encore moins bien que les longueurs)
- Avec des aires empilées, seule la couche du bas a sa base sur l'axe ; les autres "flottent" et leur hauteur réelle devient difficile à lire
- Le chevauchement masque les variations individuelles

**Alternatives à privilégier selon l'objectif** :
- Évolution temporelle d'une seule série → ligne simple
- Évolution comparée de plusieurs séries → multi-lignes avec étiquettes directes (et focus narratif : orange sur la série vedette, gris sur les secondaires)
- Décomposition d'un total dans le temps → small multiples (une mini-ligne par composante côte à côte) ou stacked bar par période
- Variation entre 2 points → slopegraph (voir §4.3)
- Décomposition d'un cumul → waterfall (voir §4.3)

Cette règle prime sur la mention "Area chart" du `dataviz-guide.md §1` (Wilke autorise les area charts avec Y=0, Knaflic les déconseille même dans ce cas — on suit Knaflic).

#### Charts à proscrire totalement
Source : Cole Nussbaumer Knaflic, *Storytelling with Data*.

**Jamais utiliser** :
- **Pie chart** (en 2D ou 3D). L'œil compare mal les angles et les surfaces. Toujours remplaçable par un barres triées ou un dot plot.
- **Donut chart**. Variante "tendance" du pie chart, même problème en pire (l'épaisseur de l'anneau ajoute une distorsion). À bannir.
- **3D** sur n'importe quel type de graphique (pie 3D, barres 3D, lignes 3D, area 3D…). La projection déforme systématiquement les valeurs : les tranches/barres en avant paraissent plus grandes, celles en arrière plus petites. **Aucun cas où la 3D apporte quoi que ce soit** à part de la décoration trompeuse.

**Alternatives à privilégier** :
- À la place d'un pie/donut → barres horizontales triées par valeur décroissante avec étiquettes directes (% ou valeur absolue), éventuellement avec un trait fin pour montrer le 100%.
- À la place d'un bar chart 3D → bar chart 2D propre, point.
- Si on veut absolument une représentation circulaire (rare) → préférer un waffle chart (grille de 10×10 carrés colorés selon la part).

Cette règle prime sur la mention "Pie chart acceptable pour fractions simples (1/2, 1/4)" du `dataviz-guide.md §1`. On suit Knaflic : zéro pie chart, zéro donut, zéro 3D dans les pres Empirik.

#### Pas de double axe Y (secondary Y axis)
Source : Cole Nussbaumer Knaflic, *Storytelling with Data*.

L'ajout d'un **second axe Y** sur le côté droit pour superposer deux séries d'unités différentes est trompeur :
- L'œil compare implicitement la hauteur des points/lignes, alors que les deux axes ont des échelles indépendantes
- L'auteur peut **manipuler la corrélation visuelle** en jouant sur les échelles (deux séries non corrélées peuvent sembler suivre la même tendance)
- Le lecteur doit faire un effort cognitif pour distinguer quelle série appartient à quel axe

**Deux alternatives propres** :

1. **Étiqueter directement les data points** qui appartiendraient au second axe, et supprimer cet axe. Les valeurs sont alors lues sans ambiguïté.

2. **Séparer le graphique verticalement** en deux sous-graphiques empilés :
   - Le graphique du haut a son propre axe Y (à gauche)
   - Le graphique du bas a son propre axe Y (à gauche aussi)
   - Les deux **partagent le même axe X** (temps, catégorie…)
   - On peut comparer visuellement les tendances sans superposition trompeuse

**Erreur à éviter** : utiliser le second axe Y "par paresse" pour caser deux séries sur un seul graphique. Toujours splitter ou étiqueter directement. Cette règle prime sur le `dataviz-guide.md §10` qui mentionnait déjà "Double axe Y : trompeur, deux graphiques séparés" — on confirme et on détaille.

### 4.4 Règles non négociables (extraits clés du guide)
- **Barres** : toujours partir de zéro (échelle linéaire)
- **Max 5-8 couleurs** distinctes en qualitatif
- **Jamais de 3D** gratuite (déforme systématiquement)
- **Jamais rainbow** (non-monotonique, trompeur)
- **Étiquettes directes** plutôt qu'une légende avec 10+ items
- **Titre = message**, pas description
- **Codage redondant** : couleur + forme ou couleur + étiquette
- **Tableaux** : pas de lignes verticales, légende AU-DESSUS, texte aligné gauche / nombres alignés droite
- **Focus narratif par contraste** : élément vedette en orange Empirik, secondaires grisés (voir §4.5)

Checklist complète : `dataviz-guide.md §9`.

### 4.5 Contraste stratégique — UN seul élément qui ressort, le reste grisé

**Principe central** : sur tout graphique ou visualisation, **un seul élément doit attirer l'œil**. Plus on multiplie les couleurs vives, moins chaque élément ressort. Le contraste est un budget limité qu'on dépense sur l'insight, pas sur la décoration.

**Règle de coloration par défaut** :
- **Élément vedette** (la donnée qu'on veut montrer, le client, la perte, le pic, la cible…) → **orange Empirik `#E9540D`**
- **Éléments de contexte** (concurrents, autres périodes, autres catégories, baseline…) → **gris `#B0B0B0`** ou **bleu Empirik atténué** (opacité 30-40%)
- **Aucun élément décoratif coloré** sans rôle narratif

**Exemples concrets** :

| Type de viz | Élément à mettre en orange | Reste grisé |
|------------|----------------------------|-------------|
| Barres concurrents | Barre du client | Barres concurrents |
| Évolution mensuelle | Mois cible / mois de perte | Autres mois |
| Slopegraph | Ligne du client / ligne avec la plus forte variation | Toutes les autres lignes |
| Funnel de conversion | Étape qui drop | Étapes normales |
| Top 10 thématique | La ligne du client | Les 9 autres |
| Carte de chaleur | Cellule la plus chaude (ou cliquée) | Le reste en dégradé gris-bleu |

**Anti-pattern à proscrire** : palette multicolore "pour faire joli" (orange + jaune + bleu + vert sur le même graphique sans raison narrative). Si chaque élément a sa couleur vive, **aucun ne ressort**.

**Test de validation** : avant de coder le graphique, formuler en une phrase **ce que l'audience doit voir en 2 secondes**. Cet élément précis doit être le seul en couleur vive. Si plusieurs éléments doivent ressortir, c'est probablement plusieurs graphiques.

**Application aux slides hors graphiques** : la règle vaut aussi pour les chiffres clés, les cartes, les tableaux. Sur une slide à 6 KPIs, si tous sont en orange, aucun ne ressort. Mettre en orange UNIQUEMENT le KPI qui appuie le titre, les autres en bleu Empirik ou texte gris.

### 4.6 Hiérarchie visuelle dans le texte — gras, couleur, italique, souligné

Quand une slide est dense en texte (paragraphe, bullets longues, citation, légende détaillée), la couleur seule ne suffit pas. **Les attributs typographiques sont des outils d'attention** qu'il faut utiliser pour créer un parcours de lecture.

**Les 4 attributs et leur rôle** :

| Attribut | Usage | Quand |
|----------|-------|-------|
| **Gras** | Mots ou groupes de mots qui portent le sens principal | Chiffres-clés in-line, verbes d'action, nom du client, conclusion d'un paragraphe |
| **Couleur orange** | Le terme/chiffre/mot le plus important du bloc | 1 à 3 éléments max par bloc — toujours en complément, jamais à la place du sens |
| *Italique* | Citations, termes étrangers, sources, mentions méta | Verbatim d'un client/LLM, références bibliographiques, *fan-out queries*, *AI Overviews* |
| Souligné | Liens cliquables uniquement | Jamais pour décorer. Souligner = signal d'action (URL, navigation) |

**Comment construire la hiérarchie sur un paragraphe** :

1. **Lire le bloc en entier** et identifier les 2-4 mots qui portent l'argument
2. **Mettre ces mots en gras** (Poppins SemiBold inline) — c'est le squelette de la lecture rapide
3. **Mettre en orange** UN seul élément central (le chiffre-clé, le nom du client, le verdict)
4. **Italiquer** les termes techniques ou les citations
5. **Vérifier le test scan** : en parcourant uniquement le gras + l'orange, est-ce que le message principal ressort ?

**Exemples** :

✅ Bonne hiérarchie :
> Barillet est cité dans **seulement 4,5%** des réponses LLM (vs **24,3% pour Dispano**) : c'est un manque de **contenu ciblant les sujets que les IA cherchent à citer**, pas un simple déficit de notoriété, donc **actionnable**.

(le squelette en gras se lit seul → "seulement 4,5% / 24,3% pour Dispano / contenu ciblant les sujets que les IA cherchent à citer / actionnable" = l'argument complet)

❌ Mauvaise hiérarchie (rien ou trop ressort) :
> Barillet est cité dans seulement 4,5% des réponses LLM (vs 24,3% pour Dispano) : c'est un manque de contenu ciblant les sujets que les IA cherchent à citer, pas un simple déficit de notoriété, donc actionnable.

(tout au même niveau → l'œil ne sait pas où aller)

❌ Mauvaise hiérarchie (trop de gras) :
> **Barillet est cité dans seulement 4,5%** des **réponses LLM** (vs **24,3% pour Dispano**) : **c'est un manque de contenu ciblant les sujets que les IA cherchent à citer**, pas un simple **déficit de notoriété**, donc **actionnable**.

(50% du texte en gras = aucune hiérarchie, le gras ne signifie plus rien)

**Règles strictes** :
- **Max 25-30% du texte** d'un bloc peut être en gras (sinon dilution)
- **Max 1-3 mots ou chiffres en orange** par bloc texte (sinon dilution)
- **Pas d'italique pour décorer**, uniquement pour les usages typographiques réels (citations, sources, termes étrangers)
- **Pas de souligné** sauf liens cliquables réels (jamais pour mettre en avant)
- **Jamais combiner gras + italique + orange + souligné** sur le même mot — c'est de la sur-emphase, l'effet s'annule
- **En PptxGenJS** : utiliser le format rich text array avec `{ text: "...", options: { bold: true } }` pour créer des sous-segments dans un même bloc

### 4.7 Test des 3 secondes — où va l'œil en premier ?

**Principe** : test classique de Cole Knaflic / UX. Une slide est réussie quand le premier élément que voit l'audience en 3 secondes est l'élément qu'on voulait qu'elle voie. Si l'œil va ailleurs, la hiérarchie visuelle est cassée.

**Comment l'appliquer en tant qu'agent IA multimodal** :

Pour chaque slide générée (image JPG après conversion PDF), exécuter mentalement cette analyse en 4 étapes :

1. **Première impression sans lire le contenu** : sur quoi se pose l'œil immédiatement ?
   - L'élément le plus saturé en couleur (typiquement l'orange)
   - L'élément le plus gros (chiffre clé, titre)
   - L'élément le plus contrasté avec son fond
   - L'élément en position dominante (centre, haut-gauche par convention de lecture)

2. **Identifier l'élément vedette voulu** : quel est le message de la slide ? Quel élément doit porter ce message ?
   - Lire le titre de la slide
   - Identifier le chiffre / mot / donnée qui appuie ce titre

3. **Comparer les deux** :
   - ✅ **Match** : le premier élément vu = l'élément vedette → hiérarchie OK
   - ❌ **Mismatch** : l'œil va sur autre chose (un élément décoratif, un chiffre secondaire, un bord coloré) → corriger

4. **Corrections classiques en cas de mismatch** :
   - L'élément décoratif (bord jaune, icône colorée) est trop saillant → l'atténuer ou le retirer
   - L'élément vedette est trop petit / trop fin → l'agrandir, le mettre en gras, l'isoler
   - Plusieurs éléments à intensité égale → griser tout sauf l'élément vedette (voir §4.5)
   - Le titre est centré mais l'œil va sur un chiffre en haut à droite → repositionner l'élément vedette plus haut/centré

**Pour les slides à plusieurs éléments importants** (ex : tableau de bord à 6 KPIs) :
- Définir un **parcours de lecture intentionnel** (ordre : 1 → 2 → 3 → 4 → 5 → 6)
- L'élément #1 doit être celui qui ressort le plus, les suivants en intensité dégressive
- Si tous au même niveau visuel → l'audience ne sait pas par où commencer

**Application dans la QA** : voir `PROCESS-ANTI-ERREURS.md` checklist "TEST DES 3 SECONDES".

### 4.8 Couleur — outil stratégique, pas décoration

**Principe central** : la couleur n'est jamais "pour faire joli". Chaque couleur sur une slide doit porter une intention narrative précise. Si une couleur n'a pas de rôle, elle dilue les couleurs qui en ont un.

**Les 3 questions à se poser avant d'ajouter une couleur** :
1. Quelle **information** cette couleur véhicule-t-elle ? (catégorie, intensité, état, accent, niveau d'importance)
2. Cette information ne pourrait-elle pas passer par un **autre canal** ? (taille, position, étiquette directe, gras)
3. Si je retire cette couleur, le message **devient-il moins clair** ? Si non → la retirer

**Règle d'économie chromatique (adaptation Empirik de la règle "tout en gris" de Knaflic)** :
- **Par défaut** : bleu Empirik `#0A3856` pour tout (texte, structure, baseline). Le bleu Empirik est suffisamment foncé pour jouer le rôle du gris neutre dominant de Knaflic : c'est la couleur stable de la charte qui ne demande pas d'attention.
- **Accent narratif** : orange Empirik `#E9540D` pour ce qui doit ressortir (voir §4.5). **L'orange joue aussi le rôle du "rouge alerte" de Knaflic** (perte, problème, point de tension) car la charte Empirik n'inclut pas de rouge. Pas d'ambiguïté : l'audience l'interprète comme "ici se trouve l'élément critique", que ce soit un succès, un risque ou une opportunité.
- **Contexte secondaire** : gris `#B0B0B0` pour les éléments contextuels (baseline, périodes précédentes, catégories non vedettes)
- **Jaune `#FCC02D`** : uniquement en accents décoratifs (bordures de cartes, badges avec texte bleu, icônes), JAMAIS comme couleur de texte sur blanc
- **Vert ad-hoc `#10A050`** : autorisé uniquement pour les KPI atteints explicitement (cible vs réalisé, signal "go") en doublure d'un libellé. Hors de cet usage métier précis : ne pas introduire.
- **Au-delà de ces 5 couleurs** : ne pas introduire de nouvelle couleur sans justification métier écrite (ex : convention sectorielle).

**Anti-pattern à proscrire** : palette multicolore où chaque catégorie a sa couleur vive (jaune + orange + bleu + vert + violet…) sans rôle narratif. L'œil saute partout, aucun élément ne ressort.

**Cas des heatmaps, choroplèthes, dégradés d'intensité** :

❌ **MAUVAIS** : utiliser une **couleur différente par valeur** (jaune pour 0-20%, vert pour 20-40%, bleu pour 40-60%, orange pour 60-80%, rouge pour 80-100%). C'est l'effet "arc-en-ciel" — l'œil ne perçoit pas l'ordre, les comparaisons sont impossibles.

✅ **BON** : utiliser **une seule couleur en dégradé d'intensité** (luminosité). C'est l'échelle séquentielle :
- Faible valeur → couleur très claire (presque blanc)
- Valeur médiane → couleur intermédiaire
- Valeur élevée → couleur saturée pleine

| Type d'échelle | Quand l'utiliser | Couleurs Empirik |
|----------------|------------------|------------------|
| **Séquentielle** | Valeurs ordonnées de faible à élevé (revenus, scores, fréquences) | Dégradé d'opacité sur le bleu `#0A3856` ou l'orange `#E9540D` |
| **Divergente** | Valeurs autour d'un point pivot (écarts +/-, % autour de 50%, satisfaction négative/neutre/positive) | Bleu Empirik d'un côté → blanc/neutre au centre → orange Empirik de l'autre |
| **Qualitative** | Catégories sans ordre (max 5-6 catégories) | Bleu + orange + 1-2 nuances atténuées, max — au-delà = repenser la viz |

**Test de validation** :
- **Compte les couleurs vives** sur la slide. Si > 3 (hors charte technique), réduire.
- **Imagine la slide en noir & blanc** : le message principal doit-il survivre ? Si oui → la couleur est bien un accent, pas le seul porteur de sens. Si le message disparaît → la couleur fait trop de travail, redoubler avec position/taille/étiquettes.
- **Daltonisme** : éviter rouge + vert seuls comme distinction (10% des hommes ne distinguent pas). Préférer bleu + orange (palette CVD-safe).

### 4.9 Éliminer les distractions — supprimer ou pousser en arrière-plan

**Principe central** : toutes les données ne sont pas égales en importance. Une slide réussie n'est pas une slide qui contient *tout*, c'est une slide où seul ce qui est essentiel reste, et où ce qui est secondaire-mais-nécessaire est visuellement reculé. Le bruit visuel masque le signal.

**Hiérarchie en 3 niveaux à appliquer sur chaque slide** :

| Niveau | Statut | Traitement visuel |
|--------|--------|-------------------|
| **1. Essentiel** | Donnée qui porte le message du titre | Pleine intensité : orange Empirik, taille forte, gras, position dominante |
| **2. Nécessaire mais secondaire** | Contexte qui aide à comprendre (axes, baseline, labels, sources) | **Reculé visuellement** : gris `#B0B0B0`, taille réduite, opacité 60-70%, en bord de slide |
| **3. Non essentiel** | Détails, redondances, déco, info "bonne à savoir" | **Supprimé purement** |

**Le test "Et si je l'enlevais ?"** — à appliquer sur chaque élément visible d'une slide :

```
Pour chaque élément (chiffre, ligne, label, cadre, icône, légende, sous-titre, note…) :

  → Si je le retire, l'audience perd-elle de l'information importante pour comprendre le message ?

    ✅ OUI, c'est essentiel ou contextuel obligatoire → garder (niveau 1 ou 2)
    ❌ NON, ça ne change rien à la compréhension → SUPPRIMER (niveau 3)
```

**Catégories de distractions fréquentes à challenger systématiquement** :

| Type de distraction | Question à se poser | Action si non essentiel |
|---------------------|---------------------|------------------------|
| Bordures, cadres autour des éléments | Sépare-t-il vraiment 2 zones différentes ? | Supprimer la bordure |
| Lignes de grille sur un graphique | Aident-elles à lire des valeurs précises ? | Atténuer ou supprimer |
| Légendes avec couleurs | Y a-t-il une alternative directe (étiquettes sur les barres) ? | Remplacer par étiquettes directes |
| Icônes décoratives sans rôle sémantique | Apporte-t-elle de l'info ? | Supprimer |
| Sous-titres redondants | Répète-t-il le titre / le contenu ? | Supprimer |
| Tableaux avec colonnes "info contextuelle" | Sont-elles regardées dans 80% des cas ? | Retirer la colonne, mettre l'info en footnote si critique |
| Axes / ticks / labels d'axe | Le lecteur a-t-il besoin des valeurs intermédiaires ? | Garder uniquement min/max ou supprimer l'axe au profit d'étiquettes directes |
| "Source : ..." très long | Toute la phrase est-elle nécessaire ? | Garder l'essentiel (nom outil + période), retirer le reste |
| Plusieurs sources sur une slide | Sont-elles toutes citées dans la slide ? | Garder uniquement les sources actives |
| Numéros de pages, footers de marque | Apportent-ils de l'info à chaque slide ? | OK pour numéro de page seul, footer minimal |

**Reculer en arrière-plan (niveau 2)** :
- **Atténuer la couleur** : gris `#B0B0B0` au lieu du bleu Empirik plein, ou opacité 60-70% sur les éléments contextuels
- **Réduire la taille** : passer un sous-label de 12pt à 10pt, une note de 11pt à 9pt
- **Décaler en bord de slide** : footer en bas pour les sources/notes, axes minimalistes en bord de graphique
- **Retirer le gras** : tout texte secondaire en Regular, jamais en SemiBold/Bold
- **Supprimer l'encadrement** : pas de bordure sur les éléments secondaires (seule la zone vedette peut être cadrée)

**Test final** : après nettoyage, refaire le **test des 3 secondes (§4.7)** :
- L'œil va-t-il directement sur l'essentiel (niveau 1) ?
- Si oui → la suppression et la mise en arrière ont fonctionné
- Si l'œil hésite encore → il reste du bruit à éliminer ou à reculer

**Garde-fou** : ne pas supprimer pour le seul plaisir de minimiser. Le but n'est pas "moins" mais "ce qui est essentiel" — la suppression doit toujours servir la lisibilité du message principal, pas un dogme esthétique.

### 4.10 Les 6 types de graphes par défaut + interdits (Knaflic)

Pour 95% des cas, on choisit dans cette liste fermée. Au-delà, justifier explicitement.

| Type | Quand l'utiliser |
|------|------------------|
| **Barre horizontale** | Catégories longues, ranking, comparaisons. **Le défaut le plus sûr** quand on hésite. |
| **Barre verticale** | Quelques catégories courtes (3-6), valeurs absolues. |
| **Barre empilée (stacked)** | Décomposition d'un total en **2 à 3 sous-parts max** (au-delà : illisible). |
| **Ligne (line chart)** | **Évolution temporelle continue** (≥ 4 points). **C'est le défaut pour montrer une tendance dans le temps.** Pour 2 périodes → slope graph. Pour 3 points → barre verticale possible. |
| **Slope graph** | Comparaison **2 périodes** (avant/après, 2024 vs 2025) sur plusieurs catégories. Plus puissant que des barres groupées. |
| **Dot plot** | Comparaison de valeurs ponctuelles, alternative à la barre horizontale quand les valeurs sont éloignées de zéro. |

**Interdits par défaut (sauf justification écrite)** :
- ❌ **3D** (toujours, pas de cas valable)
- ❌ **Ribbon chart, radar, treemap, sankey, gauge** sur audience non-spécialiste — courbe d'apprentissage = audience perdue
- ❌ **Camembert (pie)** : tolérable seulement si **2-3 parts max ET** la relation part/tout est exactement le message. Au-delà de 3 parts → barre horizontale triée.
- ❌ **Deux camemberts côte à côte pour comparer** (le pire cas) : remplacer par slope graph
- ❌ **Tableau de chiffres** : sauf si la valeur numérique exacte est le livrable (rapport financier, bilan). Le cerveau scanne ligne par ligne et mémorise mal → coût cognitif énorme

**Règle de remplacement rapide** :
- "J'ai un tableau" → essayer barre horizontale ou slope graph
- "J'ai un pie chart avec 5+ parts" → barre horizontale triée par valeur
- "J'ai des barres groupées 2 années" → slope graph
- "J'ai une heatmap fancy" → vérifier si une barre triée + couleur d'accent ne suffirait pas

#### ⛔ Test d'adéquation aux valeurs réelles (à faire à l'étape 4, pas en QA)

C'est le **plus gros angle mort** des générations IA : on choisit un format de graphe parce que le plan le dit, sans vérifier que les valeurs réelles le justifient. Le format théoriquement adapté à un *type* de comparaison peut être totalement inadapté aux *valeurs spécifiques* qu'on doit afficher.

**Avant de coder CHAQUE graphe, à l'étape 4**, dérouler ce test obligatoire :

1. **Écrire les valeurs numériques exactes** que le graphe doit porter (pas "Angora vs Sphinx" mais "30 vs 140 / 12-18 vs 9-15 / 4,5% vs 24,3%")
2. **Calculer le ratio** : si l'un des deux côtés est ~0 ou si ratio > 3 sur tous les axes →
   - Dumbbell devient une colonne d'un seul côté (inadapté)
   - Slope graph devient une ligne quasi-horizontale (inadapté)
   - Dot plot avec fourchettes devient illisible si les fourchettes ne se chevauchent pas (ou trop)
3. **Test "qu'est-ce que l'audience voit en 3 secondes"** appliqué AU FORMAT :
   > "Sur ce graphe, sans aucune annotation textuelle, l'audience verra-t-elle le message principal en 3 secondes ?"

   Si la réponse est non → changer de format AVANT de coder.

4. **Test de la béquille annotation** : si on retire mentalement les annotations textuelles (titre, valeurs, séries), le graphe transmet-il encore le message ? Si non → c'est l'annotation qui fait tout le travail, le format est mauvais.

**Cas typiques où il faut renoncer au graphe sophistiqué et passer à "Voie 4 — chiffres-clés"** :
- Comparatif 2 valeurs avec ratio ≥ 3 (`30 vs 140`, `4,5% vs 24,3%`) → 2 gros chiffres + écart en orange
- Écart de moyennes / médianes avec faible variabilité comparée à l'écart (`15 ans vs 12 ans avec fourchettes 12-18 vs 9-15`) → 2 chiffres + l'écart "+3 ans" en orange géant
- Tout cas où "l'audience doit comprendre en 5 secondes" et où le ratio est extrême

**Knaflic l'affirme explicitement** : un graphe sophistiqué qui demande un effort de lecture est INFÉRIEUR à 2 chiffres-clés clairs. La sophistication n'est pas un signal de pro — c'est souvent un signal de "j'ai voulu utiliser un format technique parce que je l'avais en tête, pas parce qu'il sert le message".

#### Fourchettes (variabilité) ≠ Écarts (différences) — ne pas mélanger

**Erreur fréquente** : utiliser un dot plot avec fourchettes pour montrer un écart entre 2 entités.

| Ce qu'on veut montrer | Format adapté | Format à éviter |
|----------------------|---------------|-----------------|
| **Écart entre 2 entités** (différence de moyennes ou médianes) | 2 chiffres-clés + écart en orange · bar chart à 2 barres | Dot plot avec fourchettes |
| **Variabilité individuelle** (distribution d'une entité) | Boxplot · dot plot · histogramme | (réservé à l'exploratoire §4.15) |
| **Les deux à la fois** | 2 slides séparées (slide écart, slide variabilité si vraiment utile) | Un seul graphe qui mélange |

Le mélange des deux dimensions sur un même graphe brouille le message : l'œil voit le chevauchement des fourchettes, pas l'écart des médianes.

### 4.11 Décombrer en bloc — checklist tactique sur chaque graphe (Knaflic)

À appliquer dans cet ordre sur tout graphique :

1. ❌ **Bordure du graphe** (cadre noir autour) → supprimer
2. ❌ **Gridlines** (lignes horizontales/verticales du fond) → supprimer ou atténuer fortement
3. ❌ **Background coloré** → fond blanc
4. ❌ **Trailing zeros** sur axe Y : `1000.0` → `1000`, `10.00%` → `10%`
5. ❌ **Texte diagonal sur axe X** (50% plus lent à lire) → abréger les labels pour les passer en horizontal (`Janvier` → `Jan`, `Septembre` → `Sep`)
6. ❌ **Légende séparée** quand on peut **étiqueter la donnée directement** (label de la même couleur que la ligne/barre, en bout de série)
7. ❌ **Axe Y + data labels en même temps** → choisir l'un OU l'autre :
   - Valeur numérique précise critique → data labels, supprimer l'axe Y
   - Forme / comparaison priorisée → garder l'axe, supprimer les labels
8. ❌ **Décimales inutiles** : `47,3%` si la précision décimale n'est pas le message → `47%`. Garder les décimales uniquement quand elles font partie du verdict (`4,5% vs 24,3%` : oui, c'est l'argument).

**Mise en page de chaque graphe (charte Empirik)** :
- ✅ **Pas de re-titrage interne du graphe** : chez Empirik, 1 graphe = 1 slide, le titre de slide centré porte le takeaway. Pas de "titre du graphe en haut à gauche" en plus.
- ✅ **Axes nommés en clair** (`Volume de citations`, pas `vol_cit_n`), pas en rotation verticale à gauche.
- ✅ **Barres épaisses** : si l'espace blanc entre les barres est plus large que les barres elles-mêmes → épaissir les barres.
- ✅ **Tri par valeur** sur barre horizontale (sauf ordre sémantique : jours de la semaine, étapes d'un funnel, classes d'âge).

### 4.12 Cohérence des formats à travers tout le deck (Knaflic)

Toute incohérence visuelle force le cerveau à se demander "pourquoi est-ce différent ?". À unifier sur **tout le deck** :

- ✅ Même police (Poppins partout) et mêmes tailles par rôle (titres / axes / labels / footers)
- ✅ Même casing des titres (Sentence case par défaut, première lettre uniquement)
- ✅ Même position des légendes (idéalement : pas de légende, label direct)
- ✅ Même palette de couleurs sur tout le deck (jamais "orange slide 3, orange slide 5" mais 2 nuances différentes)
- ✅ Mêmes formats de date partout (`Mai 2026` partout, pas `05/2026` un slide sur deux)
- ✅ Mêmes noms de séries / métriques partout (`Mentions LLM` partout, pas `Citations LLM` un slide sur deux)
- ✅ Mêmes unités et précisions (`%` vs `pts` cohérent, mêmes décimales pour des grandeurs comparables)

### 4.13 Leviers de contraste — par ordre de force (Knaflic)

Quand la slide ou le graphe est dans la palette neutre (bleu Empirik + gris), faire ressortir UN élément avec les leviers suivants. **Empiler 2-3 leviers** sur l'élément vedette est conseillé (couleur + épaisseur + label).

| Levier | Effet | Quand l'utiliser |
|--------|-------|------------------|
| **Couleur** (orange Empirik vs bleu/gris) | Très fort | Toujours en premier, sur l'élément vedette |
| **Épaisseur** ligne/barre | Fort | En complément de la couleur (ligne client = orange + épaisse) |
| **Intensité** (foncé vs clair) | Moyen | Si la couleur est déjà prise par une autre série |
| **Taille du texte / label** | Fort | Pour les annotations clés (chiffre vedette plus gros) |
| **Position 1er plan** | Moyen | Si une ligne passe derrière une autre, l'amener au premier plan |
| **Marker + label ponctuel** | Fort | Sur 1-2 points stratégiques (pic, vallée, point de bascule) |
| **Apparition animée (en live)** | Très fort | Le contexte gris apparaît, puis la série vedette arrive ensuite |
| **Pointillé** | Fort, mais **STRICTEMENT réservé à l'incertitude** : forecast, cible, projection. **Ne JAMAIS utiliser le pointillé juste pour focaliser** — l'audience l'interprétera comme "donnée hypothétique". |

### 4.14 Annotations et renommage business sur les graphes (Knaflic)

- ✅ **Annotations courtes directement sur le graphe** : texte court avec flèche fine ou label à côté du point d'intérêt (ex : "+58,7%, plus forte hausse du panel")
- ✅ **Étiqueter 2-3 points stratégiques seulement** (pics, vallées, début/fin, point de bascule) — pas tous les points
- ✅ **Renommer les catégories techniques en termes business** :
  - `Treatment_1` → `Groupe Awareness`
  - `Q1_2025_var_pct` → `Variation T1 2025`
  - `prompt_id_07` → `Requête fournisseur menuiserie pro`
  - `LCP_p75` → `Temps de chargement (75ᵉ percentile)`
- ✅ **Footnote sous le graphe** pour définir les métriques techniques si nécessaire (1 ligne max, gris atténué)

### 4.15 Exploratoire ≠ Explicatif (l'erreur la plus fréquente, Knaflic)

| Phase | Visuels typiques | Public |
|-------|------------------|--------|
| **Exploratoire** (analyse) | Box plot, histogramme, scatter, courbe de survie, heatmap, matrices de corrélation | **Soi-même uniquement**. Outils par défaut, pas de mise en forme. |
| **Explicatif** (livrable) | Les 6 types par défaut de §4.10, épurés et titrés en takeaway | **Audience finale** (client, comité, direction) |

**Règle d'or** : ne JAMAIS partager un visuel exploratoire à l'audience finale. Le retravailler entièrement OU le remplacer par un visuel plus simple qui transporte le même insight.

Exemple Knaflic : une courbe de survie complexe (étude sur le "skip" de pubs) → remplacée par 3 chiffres-clés en bloc (`32% vs 16% vs 12%`) → compréhensible en 5 secondes par un comex.

Si un agent IA produit une heatmap, un scatter ou une matrice : faire l'étape de traduction explicite en visuel explicatif avant de mettre dans le deck.

### 4.16 Espace blanc et respiration — règle anti-saturation

Ne pas chercher à remplir la slide. L'espace blanc autour des éléments leur donne du poids visuel et permet à l'œil de respirer. Une slide aérée se lit beaucoup plus vite qu'une slide dense.

**Règles concrètes** :
- ✅ **Marges 60px minimum** (déjà charte) — non négociable, même pour gagner de la place
- ✅ **Densité maximum recommandée** : ~60-70% de la surface utile (marges exclues). Au-delà → la slide étouffe.
- ✅ **Espacement entre éléments** : 20-30px entre cartes, 40px entre titre et contenu (déjà charte)
- ✅ **Pas plus de 6 bullets** par slide (déjà charte). Si plus → splitter.
- ✅ **Si un élément déborde ou s'étouffe** → splitter en 2 slides plutôt que réduire les marges ou la taille de police
- ✅ **Exception explicite tolérée** : tableaux denses (vue d'ensemble, ranking complet). Dans ce cas, justifier que la densité sert la lisibilité (comparaisons rapides ligne à ligne) et non l'inverse.

**Test rapide** : si on retire 20% du contenu de la slide, est-ce qu'elle devient plus claire ? Si oui → c'était trop dense, splitter ou nettoyer.

### 4.17 Build sequence — le même graphe répété sur N slides, un élément vedette à la fois

**Quand l'utiliser** : un graphique est intrinsèquement chargé (beaucoup de données, plusieurs lignes / segments / catégories), et **toutes les données sont importantes** au final. Mais les présenter d'un coup sature visuellement : trop de couleurs, l'œil ne sait pas où regarder, le message se dilue.

**Le piège du graphique "spaghetti"** : un line chart avec 6, 8, 10 lignes de 10 couleurs différentes qui se croisent partout. Personne ne comprend rien, chaque ligne a sa couleur vive donc aucune ne ressort, et l'audience décroche en 3 secondes. C'est un anti-pattern fréquent quand on essaie de "tout montrer en même temps". **La build sequence est la solution canonique au spaghetti chart** : on garde toutes les lignes, mais on n'en met qu'une en avant à la fois sur chaque slide.

**Alternative au "tout sur une slide"** : présenter le **même graphique sur N slides successives**, en mettant en avant un élément différent à chaque slide. L'audience voit progressivement émerger l'image complète, avec un insight ciblé à chaque étape.

**Comment l'implémenter** :

1. **Construire le graphe de référence** (épuré, sans focus) : toutes les séries en gris atténué `#B0B0B0` ou bleu Empirik clair. Aucune couleur vive. C'est l'état "neutre" du graphe.

2. **Pour chaque insight à révéler, créer une slide** :
   - **Réutiliser exactement le même graphe** (même axes, mêmes échelles, même position, même taille). Cohérence absolue : c'est CE point qui permet à l'œil de suivre la progression.
   - **Passer un seul élément en orange Empirik** `#E9540D` (la série / la barre / le point qu'on met en avant à cette étape). Tout le reste reste gris.
   - **Annoter cet élément** : flèche fine + texte court (1 ligne max) à côté.
   - **Titre de slide ciblé** sur cet élément (takeaway dédié à ce point précis, voir §2.7).

3. **Enchaîner les slides** dans un ordre narratif :
   - Slide 1 : point de départ / baseline → "Voici la situation en avril 2024"
   - Slide 2 : nouveau focus → "En septembre, l'écart se creuse sur [segment X]"
   - Slide 3 : autre focus → "Mais [segment Y] continue de progresser malgré le contexte"
   - Slide N : synthèse finale → afficher tous les éléments en couleur ou récap (optionnel)

4. **Variante "synthèse finale"** : après la build sequence, possible d'ajouter une dernière slide avec **tous les éléments en couleur en même temps** (mais l'audience est désormais préparée à les lire), accompagnée d'une slide "Ce qu'il faut retenir" qui condense les N insights.

**Pourquoi ça marche** :
- Chaque slide respecte le principe **§4.5 (un seul élément vedette)** et **§4.7 (test des 3 secondes)** — l'œil va droit au bon endroit
- L'audience n'est jamais saturée visuellement, le rythme est posé
- Les N annotations construites slide après slide accumulent l'histoire sans la dévoiler d'un coup
- L'effet "tisser les graphes" (§5.4) est appliqué *au sein du même graphique* : le récit se construit par étapes

**Cas typiques où l'utiliser** :
- **Line chart "spaghetti"** (6-10 lignes qui se croisent, toutes importantes) : 1 slide par ligne vedette à commenter, les autres en gris
- Slopegraph avec 10+ catégories : 1 slide par catégorie clé à commenter
- Évolution multi-segments sur 12 mois : 1 slide par segment vedette
- Tableau ranking complet : 1 slide pour la tête du classement, 1 pour le milieu, 1 pour la queue
- Funnel de conversion détaillé : 1 slide par étape critique

**Anti-pattern à proscrire** : 1 slide unique avec 8 lignes de 8 couleurs vives, légende dans le coin, et 5 annotations qui se chevauchent. Si ça vous tente → c'est exactement le cas où une build sequence s'impose.

**Garde-fou** : la build sequence consomme N slides. Ne pas l'utiliser pour un graphe simple (2-3 catégories), c'est une artillerie réservée aux visualisations vraiment riches. Et : la cohérence visuelle entre les N slides est non négociable (mêmes axes, mêmes positions) — sinon l'œil de l'audience perd le fil.

---

## 5. RÈGLES STORYTELLING (ajout process)

### 5.1 Tension narrative explicite par section
Au plan détaillé (étape 4), pour chaque section j'explicite la mécanique :
> "Section 2 — Constat actuel : what is (état du client aujourd'hui) → what could be (potentiel atteignable) → point de bascule (l'insight qui révèle l'écart) → preuve (data/exemple)."

Permet à l'utilisateur de voir si l'histoire **monte** ou si elle est plate.

### 5.2 Structure Acte 1 / Acte 2 / Acte 3 (Nancy Duarte)
- **Acte 1 — Setup** : situation actuelle (what is), enjeu, public concerné
- **Acte 2 — Confrontation** : tension entre what is et what could be, obstacles, choix
- **Acte 3 — Résolution** : action recommandée (what could be → comment l'atteindre), bénéfices

La "big idea" en une phrase doit être formulable avant de coder.

### 5.3 Alternance dans le rythme
Constat → solution → exemple → question. Chaque section doit avoir un "et alors ?" clair.

### 5.4 Story Mountain — Plot / Twist / Ending (Knaflic)

Structure narrative minimum pour tout deck data, complémentaire à Acte 1 / 2 / 3 de Duarte (§5.2) :

1. **Plot (contexte)** — ce que l'audience doit savoir pour être réceptive : situation actuelle, métrique de référence, période, périmètre. C'est l'établi commun.
2. **Twist (le moment de bascule)** — ce qui est nouveau, inattendu, ou qui change la donne : un chiffre marquant, une corrélation découverte, une rupture de tendance. C'est l'insight qui justifie la pres.
3. **Ending (action recommandée)** — qu'est-ce qu'on fait à partir de là ? Voir §2.1 reco obligatoire.

**Piège classique à éviter** : la structure "rapport d'analyse" — Background → Problem → Data → Méthodologie → Findings → ~~(stop)~~. L'audience dit "intéressant" et passe à autre chose. Sans **Ending explicite**, la pres rate son objectif.

**Anti-pattern visuel** : 4 graphes côte à côte sur 1 slide "vue d'ensemble" → l'audience ne sait pas par où commencer.

**Pattern Empirik (déjà charte)** : 1 graphe = 1 slide. Les graphes se **tissent** sur plusieurs slides successives qui construisent progressivement le récit (hausse → baisse → conclusion → recommandation), pas en bloc parallèle. Le rythme du deck = succession de slides qui s'enchaînent narrativement, jamais un dashboard plat.

### 5.5 Équilibre Logos / Pathos / Ethos — obligatoire, jamais 100% Logos

**Règle de fond** : toute présentation doit équilibrer les 3 modes de persuasion d'Aristote (repris par Duarte) :

| Mode | Définition | Outils Empirik |
|------|------------|----------------|
| **Logos** (rationnel) | Faits, chiffres, démonstration logique, sources | Graphes, tableaux, KPIs, légendes sources, Brand Tracker |
| **Pathos** (émotionnel) | Histoire, anecdote, projection, métaphore, S.T.A.R. | Slides "nouvelle félicité", humanisation des chiffres, citation propriétaire, visuel évocateur |
| **Ethos** (crédibilité) | Sources fiables, méthodologie transparente, expertise | Citations Wilke/Knaflic/Duarte, logos d'études, mention agence, périmètre méthodologique |

**Le défaut par défaut du process Empirik est de saturer Logos** (rigueur factuelle = priorité de la charte) et de **négliger Pathos** (S.T.A.R., humanisation, métaphore, nouvelle félicité). C'est un déséquilibre structurel à corriger à chaque pres.

**Cible** :
- Logos : 50-65% du deck (preuves, data, démonstration)
- Pathos : 20-30% minimum (sans descendre en dessous)
- Ethos : 10-15% (sources, méthodologie, crédibilité)

**Si Pathos < 20% sur sujet narratif (pres client, pitch, présentation stratégique)** → **défaut bloquant**. Compenser via Artifact 6 (§0 étape 4) :
- S.T.A.R. moment ajouté
- Chiffres-clés humanisés (au moins 3)
- Slide "nouvelle félicité" entre reco et CTA
- Métaphore filée

**Exception** : rapport d'analyse pure pour comité technique interne (audit, restitution data brute). Dans ce cas, Pathos peut être < 20% — mais l'utilisateur doit l'avoir explicitement demandé en mode "rapport" et non "présentation".

**Pourquoi cette règle est ici et pas implicite** : la pres "Angora vs Sphinx" v1 a obtenu 100% sur la checklist factuelle Empirik (charte, dataviz, exhaustivité, sources) mais 55% sur Duarte (zéro S.T.A.R., chiffres froids, structure 100% piliers sans sparkline, big idea sèche). Preuve que **sans règle explicite Pathos**, le Claude exécute par défaut un audit McKinsey rigoureux mais émotionnellement plat.

### 5.6 Nouvelle félicité (et tout paragraphe narratif) — règle de mise en forme

**Principe** : un paragraphe narratif Duarte (slide "nouvelle félicité", anecdote d'ouverture, projection émotionnelle) doit rester **narratif** dans le ton, mais sa **mise en page reste éditoriale** — pas un bloc oraliste indifférencié.

**Règle quantifiée** : tout paragraphe narratif sur une slide ne doit JAMAIS être un pavé > 60 mots monobloc. Au-delà, le ton oral mal transposé à l'écrit étouffe le message. Un lecteur scanne, il ne lit pas un monologue.

**Si le paragraphe dépasse 60 mots, le découper en 3 moments visuels** (structure ouverture / pivot / résolution) :

1. **Moment 1 — Ouverture (le décor)** : 1 phrase qui plante le contexte ou le dialogue d'entrée
2. **Moment 2 — Pivot (la révélation factuelle)** : 1 phrase + 3-4 chiffres-ancres en bullet ou liste compacte
3. **Moment 3 — Résolution (le verdict émotionnel)** : 1 phrase qui scelle le futur transformé

Chaque moment occupe son propre bloc visuel sur la slide, avec espace blanc entre eux. Le ton reste narratif (tu peux garder dialogues, métaphores, projections), la mise en page devient lisible en 5 secondes au lieu de 30.

**Exemple générique de structure** :

```
[ Slide nouvelle félicité ]

Moment 1 (ouverture) :
  Septembre prochain, salle de réunion.
  [Le décideur] : "Et nos chiffres clés ?"

Moment 2 (pivot avec ancrage chiffré) :
  Cette fois, [le héros de la pres] ne montre plus une courbe rouge.
  Il montre :
   ▸ [chiffre 1]
   ▸ [chiffre 2]
   ▸ [chiffre 3]
   ▸ [chiffre 4]

Moment 3 (résolution émotionnelle) :
  [Le décideur] ne demande plus pourquoi.
  Il demande comment scaler.
```

**Anti-pattern à proscrire** : "Imaginez, dans X mois, votre [audience] [verbe] [bénéfice 1], [verbe] [bénéfice 2], [verbe] [bénéfice 3], et grâce à ça [conclusion]…" en un seul bloc italique centré. C'est le ton d'un oral mal traduit en slide. Le lecteur écrit décroche.

**Règle d'or** : si tu hésites à structurer ou pas, structure. Une narration en 3 moments visuels reste émotionnelle ET devient scannable. Une narration monobloc perd les deux.

---

## 6. STACK TECHNIQUE PptxGenJS

### 6.1 Conventions de base
- Couleurs sans `#` : `"0A3856"`, `"E9540D"`, `"FCC02D"`, `"FFFFFF"`
- `LAYOUT_16x9` (10" × 5.625")
- Marges ≥ 0.6"
- Police : utiliser le nom complet variant dans `fontFace` (voir §3.2)

### 6.2 Bullets et listes
- `bullet: true` (JAMAIS de caractères unicode "•")
- `breakLine: true` entre les items multi-lignes

### 6.3 Pièges connus
- **Ne JAMAIS réutiliser un objet d'options** entre plusieurs appels — PptxGenJS le mute en place
- **Ombres** : jamais de valeur négative pour `offset`, jamais de couleur 8-char hex
- **`fontWeight`** : n'existe pas, utiliser `fontFace` variant
- **`charSpacing`** : ne pas utiliser sur les sur-titres / eyebrows
- **`.toUpperCase()`** : à proscrire dans le script

### 6.4 Génération d'images Gemini
- Modèle pro (défaut) : `gemini-3-pro-image-preview` (Nano Banana Pro Preview) — qualité max, infographies
- Modèle flash : `gemini-3.1-flash-image-preview` — production rapide
- Script : `python scripts/generate_image.py --type [cover|concept|workflow|section|comparison|data-backdrop|closing] --output assets/nom.png`
- 7 types d'assets définis dans `DESIGN_EMPIRIK.md`
- Workflow : générer images → `assets/` → intégrer via `slide.addImage()`

### 6.5 Charts horizontaux — bug LibreOffice
PptxGenJS `barDir: "bar"` rend les labels catégories comme des index numériques (1, 2, 3…) en LibreOffice. **Fix** : construire les barres manuellement avec rectangles + text labels.

### 6.6 Quatre voies de génération de graphes — choisir la bonne selon le type ET les valeurs

**Constat important** : par défaut, construire les graphes en `shapes` PptxGenJS (rectangles + textes) est très simple pour des barres horizontales/verticales mais devient **vite limitant** pour les types complexes (slopegraph multi-catégories, line chart avec courbure, scatter, heatmap, density). Cette limite n'est pas inhérente à PptxGenJS — c'est juste qu'on n'utilise pas la bonne voie.

**Règle de choix double** : au plan détaillé (étape 4), pour CHAQUE graphique, statuer explicitement :
1. **Quelle voie de génération** (1, 2, 3 ou 4)
2. **Pourquoi cette voie est adaptée AUX VALEURS RÉELLES** (cf §4.10 test d'adéquation)

| Type de graphe / message | Voie recommandée | Quand l'éviter |
|---------------------------|------------------|----------------|
| **2 valeurs avec ratio ≥ 3** (ex : 30 vs 140, 4,5% vs 24,3%) | **Voie 4 : chiffres-clés seuls** | Jamais — c'est le format canonique pour cet usage |
| **Barre horizontale / verticale** (1-5 catégories, valeurs comparables) | Voie 1 : shapes PptxGenJS | Si une valeur est ~0 (la barre disparaît) |
| **Barre empilée** (2-3 segments) | Voie 1 : shapes PptxGenJS | Si > 3 segments (illisible) |
| **Slope graph** (2 périodes × N catégories non-extrêmes) | Voie 3 : Python matplotlib → PNG | Si une valeur est ~0 ou si ratio extrême : préférer Voie 4 |
| **Dumbbell** (2 valeurs côte à côte × N catégories non-triviales) | Voie 3 : Python matplotlib → PNG | Si l'une des 2 valeurs est ~0 sur la majorité des catégories : préférer Voie 4 ou bar chart groupé |
| **Line chart** (≥ 4 points) | Voie 2 (PptxGenJS natif simple) OU Voie 3 (annoté) | Si < 4 points → barres verticales |
| **Dot plot avec fourchettes** | Voie 3 (matplotlib) | Si on veut montrer un ÉCART (pas une variabilité) : préférer Voie 4 (cf §4.10) |
| **Scatter** | Voie 2 ou 3 | Si < 5 points → préférer un format plus simple |
| **Heatmap** | Voie 3 : matplotlib/seaborn | Si tableau trop petit (< 4×4) : tableau simple suffit |
| **Waterfall** | Voie 3 : matplotlib | Si pas de logique séquentielle réelle : stacked bar |
| **Build sequence** (§4.17) | Voie cohérente entre les N slides | — |

#### Voie 1 — Shapes PptxGenJS (rectangles + textes)
Avantages : contrôle pixel-perfect, pas de dépendance externe, idéal pour barres et tableaux.
Limites : devient vite lourd au-delà de barres simples.
Quand : barres horizontales/verticales, barres empilées simples, comparaisons côte à côte, tags / pills / KPI cards.

#### Voie 2 — Charts natifs PptxGenJS (`pres.addChart()`)
Avantages : rapide, supporte line / bar / pie / doughnut / scatter / radar / bubble / area.
Limites : moins de contrôle stylistique, certains rendus diffèrent entre PowerPoint et LibreOffice (cf §6.5 sur `barDir: "bar"`).
Quand : line chart simple (évolution temporelle classique), doughnut pour ratio 1-2 segments.
Code de base :
```js
slide.addChart(pres.charts.LINE, [
  { name: "Barillet", labels: ["Mars", "Avril", "Mai"], values: [3.2, 4.1, 4.5] },
  { name: "Dispano", labels: ["Mars", "Avril", "Mai"], values: [18.2, 21.5, 24.3] },
], { x: 0.5, y: 1.5, w: 9, h: 3.5,
     showLegend: false, chartColors: ["E9540D", "B0B0B0"],
     catAxisLabelFontFace: "Poppins", catAxisLabelFontSize: 10,
     valAxisLabelFontFace: "Poppins", valAxisLabelFontSize: 10 });
```

#### Voie 3 — Python matplotlib/plotly → PNG → importé (pour la variété)
Avantages : flexibilité maximale, tous les types de graphes accessibles, contrôle stylistique total, palette Empirik facile à appliquer.
Limites : étape supplémentaire (générer le PNG puis l'importer), texte du PNG non éditable une fois importé (cf règle ci-dessous).
Quand : slope graph, dot plot, heatmap, waterfall, density plot, scatter dense, line chart annoté, tout graphique au-delà des barres simples — **À CONDITION que le test d'adéquation aux valeurs §4.10 valide le format**.

Helper disponible : `scripts/generate_chart.py`. Il prend en entrée le type de graphe + les données, génère un PNG transparent à la charte Empirik (palette bleu/orange/gris) + un fichier JSON sidecar avec les coordonnées des textes à superposer.

##### ⛔ Règle critique pour Voie 3 : PNG sans texte, texte ajouté en superposition PptxGenJS

Le PNG matplotlib doit contenir **uniquement les éléments visuels** qui ne peuvent pas être faits en PptxGenJS : lignes, points, barres, gradients, courbes, zones colorées. **Aucun texte dans le PNG.**

Tous les textes (axes, étiquettes de séries, annotations, valeurs en bout de ligne, titres) sont ajoutés ensuite via PptxGenJS `slide.addText()` en superposition au-dessus du PNG importé.

**Pourquoi cette règle** : un texte hard-codé dans le PNG est **pixelisé et non éditable** une fois le PPTX ouvert dans PowerPoint / Google Slides. Si l'utilisateur veut corriger une coquille ou ajuster un libellé, il ne peut pas. Tous les libellés doivent rester des `<txBody>` PptxGenJS éditables.

**Workflow** :
1. `generate_chart.py` génère `assets/charts/chart-name.png` (visuel seul) + `assets/charts/chart-name.overlays.json` (coordonnées et textes)
2. Le script `build_xxx.js` :
   ```js
   slide.addImage({ path: "assets/charts/chart-name.png", x: 0.5, y: 1.4, w: 9, h: 3.6 });
   const overlays = JSON.parse(fs.readFileSync("assets/charts/chart-name.overlays.json"));
   overlays.forEach(o => {
     // Convertir % du PNG → coordonnées slide
     const x_slide = 0.5 + o.x_pct * 9;
     const y_slide = 1.4 + o.y_pct * 3.6;
     slide.addText(o.text, {
       x: x_slide, y: y_slide, w: o.w || 1.5, h: o.h || 0.3,
       fontFace: o.bold ? "Poppins SemiBold" : "Poppins",
       fontSize: o.size || 11, color: o.color || "0A3856",
       align: o.align || "left", valign: "middle", margin: 0,
     });
   });
   ```

##### ⛔ QA de centrage du PNG (Erreur #10 du process anti-erreurs)

Après génération d'un PNG via Voie 3, ouvrir l'image dans le Read tool et **vérifier visuellement** que le contenu utile (lignes, points, barres) est centré dans le PNG. Si décalage (typique avec des labels asymétriques) : ajuster matplotlib (`xlim`/`ylim`) ou cropper avec PIL.

**Règle d'or** : si une slide planifiée à l'étape 4 demande autre chose qu'une barre simple ET que le test §4.10 valide le format, ne pas se rabattre par défaut sur des shapes — passer par Voie 3 (Python). **Un deck Empirik réussi mélange plusieurs types de graphes au fil des slides**, pas 30 slides de barres horizontales. **MAIS** la variété ne se valorise jamais elle-même : un graphe sophistiqué inadapté aux valeurs est INFÉRIEUR à 2 chiffres-clés bien posés (Voie 4).

#### Voie 4 — Chiffres-clés seuls (souvent supérieur à un graphe)

**Format canonique** pour les comparatifs simples avec ratio extrême ou écart simple à raconter.

**Quand l'utiliser (souvent c'est la BONNE réponse, pas un fallback)** :
- Comparatif 2 valeurs avec ratio ≥ 3 (`30 vs 140 min`, `4,5% vs 24,3%`, `1 jour vs 1 an`)
- Écart de moyennes / médianes simple à raconter (`15 ans vs 12 ans = +3 ans`)
- KPI unique avec contexte (`73% des entreprises concernées · +12 pts depuis 2023`)
- Tout cas où "l'audience doit comprendre en 5 secondes"

**Format type sur une slide** :
- 2 gros chiffres centrés en Poppins Bold 60-72pt
- L'un en bleu Empirik (référence), l'autre en orange Empirik (vedette)
- Sous chaque chiffre : label court 14pt Poppins Medium ("Angora · 30 min/sem")
- Au centre ou en bas : l'écart en orange (`×4`, `+3 ans`, `+19,8 pts`)
- Optionnel : ventilation textuelle des composantes en dessous (5 lignes max)

**Pourquoi c'est souvent supérieur à un graphe** : moins de friction cognitive, message immédiat, pas de risque d'inadéquation format/valeurs. Knaflic souligne que la sophistication graphique n'est PAS un signal de qualité — souvent l'inverse. Un comex / un client préfère 2 chiffres clairs à un dot plot complexe.

#### Voie alternative — Images IA pour concepts (PAS pour data)
Gemini / OpenAI image generation est **réservé aux illustrations conceptuelles narratives** (cover, sections, schémas pédagogiques, ambiances) et **strictement interdit pour les graphes data** : impossible de garantir l'exactitude des valeurs, peu reproductible, pas de contrôle de palette.
Modèles à utiliser (toujours les derniers en vigueur) :
- Gemini : `gemini-3-pro-image-preview` (Nano Banana Pro Preview) pour qualité max, `gemini-3.1-flash-image-preview` pour rapide
- OpenAI : `gpt-image-1` ou son successeur si publié
- **Vérifier en début de session quel est le modèle d'image le plus récent** (les noms changent fréquemment) et ne pas hardcoder un modèle obsolète. Si en doute, faire une recherche rapide ou tester l'appel API.

---

## 7. QA POST-GÉNÉRATION (ajout process)

### 7.1 Pipeline obligatoire
```bash
# 1. Génération
NODE_PATH="$NPM_GLOBAL/node_modules" node build_xxx.js

# 2. Conversion PDF
"C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf build_xxx.pptx

# 3. PDF → images JPG (PyMuPDF, PAS pdftoppm)
python -c "import fitz; doc=fitz.open('build_xxx.pdf'); [p.get_pixmap(dpi=150).save(f'qa-slides/slide-{i+1:02d}.jpg') for i,p in enumerate(doc)]"

# 4. Vérification texte
python -m markitdown build_xxx.pptx
```

### 7.2 QA structurée — checklist par slide
Pour CHAQUE slide image, je coche explicitement :

**Typographie**
- [ ] Sur-titre Poppins ExtraLight 12pt orange, casse normale, sans `charSpacing`
- [ ] Titre Poppins SemiBold 22pt bleu (fontFace variant utilisé)
- [ ] Aucun texte < 12pt (sauf footer 10-11pt OK)

**Contraste**
- [ ] Aucun texte jaune sur blanc
- [ ] Texte courant bleu, chiffres clés orange

**Ponctuation / accents**
- [ ] `grep -c "—"` = 0 (aucun tiret cadratin)
- [ ] Accents diacritiques tous en place

**Logos**
- [ ] Logo Empirik uniquement sur cover
- [ ] Chaque marque/outil cité a son logo officiel

**Contenu**
- [ ] Voix "vous" partout
- [ ] Slide data → mention "Source : … · Période : …"
- [ ] URLs externes cliquables
- [ ] Exhaustivité PDF source vérifiée

**Visuel**
- [ ] Aucun débordement de cadre
- [ ] Aucun chevauchement
- [ ] Footer + n° page sur slides standard

Si une case n'est pas cochée → corriger avant "fini". **Pas de "ça a l'air OK"**.

### 7.3 Vérification d'exhaustivité par sous-agent
Lancer un sous-agent (general-purpose) avec mission : "Comparer les slides images aux sections du PDF/brief source, lister ce qui a été omis, ce qui a été tronqué". Fresh eyes pour rattraper les angles morts.

---

## 8. CHECKLIST CHARTE (rappel synthétique)

### Design
- [ ] Poppins partout (avec fontFace variants explicites)
- [ ] Tailles conformes (22pt titre, 14pt texte)
- [ ] Palette stricte (#0A3856 / #E9540D / #FCC02D / #FFFFFF)
- [ ] Fond blanc partout (sauf section/CTA)
- [ ] Marges 60px, max 6 bullets/slide
- [ ] Contraste lisible (pas de jaune sur blanc)

### Visuel
- [ ] Une seule idée par slide
- [ ] Élément visuel central sur chaque slide
- [ ] Placeholders prévus pour screenshots/images
- [ ] Slides transition entre sections
- [ ] Variété des types de slides

### Contenu
- [ ] Voix "vous" partout
- [ ] Concepts techniques expliqués visuellement
- [ ] Questions client intégrées régulièrement
- [ ] Storytelling cohérent (Acte 1/2/3)
- [ ] Top-down McKinsey (synthèse + "ce qu'il faut retenir" par section)

---

## 9. RESSOURCES PROJET

### Fichiers de référence
| Fichier | Rôle |
|---------|------|
| `CLAUDE.md` | Source unique de vérité (ce fichier) |
| `guide_design_slides.md` | Détails design exhaustifs |
| `guide_storytelling_presentations.md` | Méthode Nancy Duarte détaillée |
| `dataviz-guide.md` | Référence Wilke pour les graphiques |
| `DESIGN_EMPIRIK.md` | 7 types d'assets visuels + prompts Gemini |
| `PROCESS-ANTI-ERREURS.md` | Checklist tactique + 7 erreurs récurrentes + helpers code |

### Outils installés
| Outil | Commande |
|-------|----------|
| Extraction texte PPTX | `python -m markitdown fichier.pptx` |
| Aperçu visuel | `python scripts/thumbnail.py fichier.pptx` |
| Conversion PDF | `"C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf fichier.pptx` |
| PDF → images | PyMuPDF (`fitz`) — voir §7.1 |
| Génération image | `python scripts/generate_image.py --type [type] --output assets/nom.png` |

### Clés API
- `clé-api-gemini.md` — Gemini (génération images)
- `clé-api-openai.md` — OpenAI (analyses entité de marque LLM)
- `clé-api-dataforseo.md` — DataForSEO (SEO data)

### Dépendances système
Voir `SETUP.html` pour la procédure d'installation complète. Stack :
- npm global : `pptxgenjs`, `react-icons`, `react`, `react-dom`, `sharp`
- pip : `markitdown[pptx]`, `Pillow`, `PyMuPDF`, `google-generativeai`
- LibreOffice (chemin codé en dur pour Windows)
- `NODE_PATH="C:\Users\spare\AppData\Roaming\npm\node_modules"` pour trouver pptxgenjs

### Agence
- **Empirik** — agence du user ("better with data")
- Logo Empirik : uniquement sur slide de couverture, jamais ailleurs

---

## 10. RAPPEL CRITIQUE — PROCESS-ANTI-ERREURS.md

`PROCESS-ANTI-ERREURS.md` est le **fichier anti-régression**. À lire **AVANT toute génération**. Il contient :
- Pre-flight checklist (cocher mentalement avant 1ère ligne de code)
- Les 7 erreurs récurrentes (sur-titres MAJ, fontFace ignoré, jaune sur blanc, em dashes, logos oubliés, tableaux tronqués, QA partiel)
- Helper `addSurTitleAndTitle()` officiel
- Mapping couleurs par type d'élément
- Commande QA visuel one-liner

Si une instruction de `CLAUDE.md` semble en conflit avec `PROCESS-ANTI-ERREURS.md`, `PROCESS-ANTI-ERREURS.md` prime sur la tactique (helpers code, valeurs précises), `CLAUDE.md` prime sur la stratégie (workflow, règles de fond).

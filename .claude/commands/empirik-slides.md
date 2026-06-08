---
description: Génère une présentation Empirik via workflow dynamique multi-agents (orchestration des 8 étapes + sous-agents QA indépendants + Devil's advocate)
---

# Commande : Générer une présentation Empirik via workflow dynamique

Tu vas générer une présentation Empirik en utilisant un **workflow dynamique** (feature Claude Code ≥ v2.1.154 — toggle "Dynamic workflows" dans `/config` doit être activé).

L'objectif du workflow : garantir mécaniquement (pas par interprétation textuelle) que les 170+ règles Empirik sont appliquées à chaque génération, en éliminant les 3 bugs structurels observés sur les générations précédentes :
- **Agentic laziness** : l'agent producteur s'arrêtait avant la fin (Pathos zappé, exhaustivité partielle)
- **Self-preferential bias** : l'agent producteur s'auto-validait (17/17 ✅ alors que 3 méritaient ❌)
- **Goal drift** : règles non quantifiées appliquées de plus en plus laxement au fil du contexte

## Briefing utilisateur attendu (à demander si manquant)

Avant de lancer le workflow, tu DOIS avoir reçu de l'utilisateur :
- **Client / sujet** de la présentation
- **Public cible** (rôle, contexte)
- **Objectif** (pitch / audit / bilan / restitution data / autre)
- **Inputs disponibles** (brouillon, brief, PDF source, data, références)

Si ces 4 infos ne sont pas dans le message courant, **demande-les explicitement avant de lancer le workflow**. Pas de génération sans briefing complet.

## Workflow dynamique à créer et exécuter

Crée et lance un workflow dynamique (`ultracode`) qui orchestre les phases suivantes. **Le workflow doit générer des sous-agents avec contextes isolés** pour empêcher l'auto-validation.

### Phase 1 — Lecture allégée des guides + Rapport d'actions tactiques (1 sous-agent)

**Optimisation perf** : ce sous-agent (et tous ceux des phases suivantes) reçoit en contexte injecté le fichier **`CONTEXTE-SOUS-AGENTS.md`** (~500 lignes, vs 1700+ pour CLAUDE.md). Ce contexte condensé couvre 95% des décisions. Le sous-agent ne consulte les guides complets QUE si une règle floue ou non couverte le bloque (auto-référence dans CONTEXTE-SOUS-AGENTS.md §8).

Sous-agent qui :
- Lit `CONTEXTE-SOUS-AGENTS.md` (référence opérationnelle condensée)
- Lit `MASTER-CHECKLIST.md` (instrument du rapport QA final)
- Consulte ponctuellement les guides complets uniquement si nécessaire (`CLAUDE.md`, `PROCESS-ANTI-ERREURS.md`, `guide_design_slides.md`, `guide-slides-data-storytelling.md`, `guide_storytelling_presentations.md`, `dataviz-guide.md`, `DESIGN_EMPIRIK.md`)
- Produit le **rapport de lecture en 5 ACTIONS TACTIQUES par fichier consulté** (format CLAUDE.md §0 Étape 1, pas un résumé théorique)
- Détecte si le sujet est data-driven → drapeau Pathos + propose 3 contre-poisons (CLAUDE.md §0 Étape 2)
- **Refresh logos LLM en pre-flight** : si la pres cite des LLMs/IA (ChatGPT, Claude, Gemini, Perplexity, Mistral, Copilot, Grok, DeepSeek, Llama, Cohere), lance `scripts/fetch_logos.py --auto` sur ces marques même si le cache existe (cf CLAUDE.md §2.6)
- Retourne : rapport actions + drapeau Pathos + contre-poison proposé + logos LLM rafraîchis

### Phase 2 — Validation utilisateur (humain dans la boucle)
Affiche le rapport de Phase 1 + 2-3 angles narratifs proposés (CLAUDE.md §0 Étape 2). **Attend la validation explicite de l'utilisateur** sur (a) l'angle choisi (b) le contre-poison Pathos. Pas de progression sans validation.

### Phase 3 — Triplet Audience/Action/Insight (Knaflic §0, CLAUDE.md §0 Étape 3.5)
Sous-agent qui produit les 3 lignes obligatoires :
- Audience précise (rôle, contexte, peur, désir — pas "les stakeholders")
- Action voulue (verbe + objet concret)
- Insight central (1 phrase max)

Test 90 secondes obligatoire : si on ne peut pas raconter l'histoire à voix haute en 90s, recommencer.

### Phase 4 — Plan détaillé + 6 artifacts obligatoires (1 sous-agent)
Sous-agent qui produit le plan slide par slide ET les 6 artifacts (CLAUDE.md §0 Étape 4) :
1. Tableau couverture du brouillon (chiffre source → slide cible)
2. Avocat du diable §1.3 (preuve / limites / robustesse pour chaque chiffre)
3. Liste explicite des slides "Ce qu'il faut retenir" (1 par section)
4. Cartographie des voies dataviz (type + voie + justification par graphe)
5. Slides question client planifiées (1 par section minimum)
6. Plan émotionnel Duarte (S.T.A.R., humanisation 3 chiffres, sparkline, nouvelle félicité, big idea complète, métaphore, audience héroïsée)

### Phase 5 — Validation finale utilisateur
Affiche le plan + les 6 artifacts. **Attend "go" explicite de l'utilisateur**. Pas de génération sans validation.

### Phase 6 — Génération PPTX (1 agent producteur)
Agent qui :
- Pre-flight 1 : liste les marques/outils → lance `scripts/fetch_logos.py --auto` pour les manquants
- Pre-flight 2 : **QA visuelle de chaque logo** via Read tool (vérifier marque réelle + version actuelle + format exploitable, cf CLAUDE.md §2.6 + PROCESS-ANTI-ERREURS Erreur #13). Si placeholder / obsolète / erroné détecté → re-fetch avant intégration
- Génère le script `build_<nom-pres>.js` selon la charte (CLAUDE.md §3 et §6)
- Pour chaque graphe Voie 3 : lance `scripts/generate_chart.py` (PNG sans texte + JSON overlays)
- **Encodage UTF-8 strict** : écrire les accents directement (`chiffrées`, `généré`, `défense`). AUCUNE substitution préventive par ASCII. L'environnement est UTF-8 garanti (cf PROCESS-ANTI-ERREURS Erreur #12). La "fix-up post-génération" des accents est interdite et signale une erreur d'amont.
- Compile en `.pptx` via `node build_<nom-pres>.js`
- Convertit en PDF via LibreOffice puis en JPG via PyMuPDF (1 par slide)
- Test final : `python -m markitdown build_<nom-pres>.pptx | grep -cE "[éèêàùôîûœç]"` doit être > 0 (sinon l'agent a substitué les accents)

### Phase 7 — Panel parallèle de 3 sous-agents indépendants
**Lancer en PARALLÈLE** (pattern fan-out-and-synthesize) :

**Sous-agent A — Exhaustivité factuelle**
Mission : compare le brouillon source vs slides générées. Liste tout ce qui est dans le brouillon mais absent des slides. Liste tout ce qui est dans les slides mais absent du brouillon (= inventé/supposé). Verdict factuel : score X/N. Mandat strict : par défaut chaque omission est ❌, c'est au producteur de justifier.

**Sous-agent B — Audit Duarte / résonance émotionnelle**
Mission : audite la pres sur les 9 critères Duarte (S.T.A.R., humanisation chiffres, sparkline, nouvelle félicité, big idea complète, métaphore, ratio Logos/Pathos, audience-héros, proportions actes). Verdict X/9.

**Sous-agent C — Conformité technique PptxGenJS**
Mission : vérifie le script source. fontFace variant (pas fontWeight), aucun `toUpperCase()`, aucun `charSpacing` sur eyebrows, `grep -c "—"` = 0, aucun jaune sur blanc, alignement strict, marges 60px, PNG sans texte pour graphes Voie 3.

### Phase 8 — Rapport QA double-passe par sous-agent QA INDÉPENDANT (fusion 8 + 8.5)

**Sous-agent QA unique avec mandat double-passe interne** (gain perf : ~4 min vs 2 sous-agents séquentiels) :

> "Tu es l'auditeur indépendant du livrable. Voici MASTER-CHECKLIST.md (~170 items) et tous les outputs des Phases 1-7.
>
> **Passe 1 — Audit initial** : par défaut chaque bloc est ❌. Pour passer en ✅, il faut une PREUVE ATOMIQUE (citation directe + référence slide N ou ligne L du script). Pour règles quantifiables (voix vous, em-dashes, ratio dataviz, proportions actes), exiger comptage chiffré dans la preuve.
>
> **Passe 2 — Devil's advocate interne** (immédiatement après la passe 1, dans le même contexte) : reprends chaque ✅ que tu viens d'attribuer et challenge-le. Si la preuve est circulaire (pointe vers un autre ✅), absente, ou non quantifiée sur règle quantifiable → retraite en ❌. Focus prioritaire sur les blocs historiquement laxistes : BB (voix vous), Artifact 1 (couverture brouillon), F (contraste stratégique), U (exhaustivité), Z (Duarte).
>
> **Verdict final** : pour chaque ✅, double validation (passe 1 atomique + passe 2 challengée). Pour chaque ❌, justification + impact + correction proposée.
>
> Si > 3 ✅ retraités en ❌ lors de la passe 2 → le rapport QA est REJETÉ, retour à Phase 6 avec corrections obligatoires (max 2 itérations producteur ↔ auditeur)."

L'agent producteur n'a PAS le droit de cocher ✅ lui-même.

**Pourquoi fusion** : 2 sous-agents séquentiels (audit puis devil's advocate) consommaient ~14 min cumulés alors que la passe 2 est essentiellement une relecture critique du résultat de la passe 1. Un seul sous-agent avec mandat double-passe explicite obtient le même niveau de rigueur en ~10 min, avec le bénéfice supplémentaire d'un contexte continu (la passe 2 connaît directement les preuves de la passe 1, sans re-relecture).

### Phase 9 — Livraison
Produire :
- `<nom-pres>.pptx` (le livrable)
- `qa-rapport-<nom-pres>.md` (MASTER-CHECKLIST rempli par sous-agent G + verdict sous-agent H)
- `<nom-pres>.pdf` (export PDF)
- Dossier `qa-slides-<nom-pres>/` (1 JPG par slide)

## Méta-règle absolue

**L'agent producteur ne calcule JAMAIS sa propre métrique finale.** Toute métrique de qualité (score MASTER-CHECKLIST, verdict Duarte, exhaustivité) est calculée par un sous-agent indépendant avec mandat explicite "trouve les défauts, sois critique, par défaut le travail est en échec sauf preuve atomique du contraire".

## Sauvegarde du workflow après 1ère exécution réussie

Une fois le workflow exécuté avec succès, presser **`s`** dans le menu `/workflows` pour le sauvegarder localement. À partir de là, les exécutions suivantes lancent directement `/empirik-slides` sans re-générer le workflow.

## Prérequis utilisateur

- Claude Code ≥ **v2.1.154** (Settings → About)
- Toggle "Dynamic workflows" activé dans `/config`
- Tous les setup de SETUP.html validés (Node, Python, LibreOffice, npm globaux, pip, Poppins, clés API)

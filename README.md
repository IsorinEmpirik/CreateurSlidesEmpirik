# Empirik — Créateur de Slides x Storytelling

Système de génération de slides PowerPoint à la charte Empirik, piloté par Claude Code (extension VS Code) + PptxGenJS + Python. Toutes les règles de design, dataviz et storytelling sont appliquées automatiquement et tracées dans un rapport QA exhaustif à chaque livraison.

---

## 🚀 Installation sur ta machine — copie-colle les prompts dans Claude Code

> **Prérequis** : tu as déjà Claude Code (extension VS Code) installé et authentifié sur ton compte Anthropic.

---

### Prompt 1 — Cloner le repo en local

Ouvre Claude Code (Cmd/Ctrl + Shift + P → "Claude Code: Start chat") et colle ce prompt :

```
Clone le repo https://github.com/IsorinEmpirik/CreateurSlidesEmpirik.git
dans mon dossier Desktop (ou Documents si c'est plus logique pour moi).
Une fois cloné, ouvre le nouveau dossier dans VS Code via une nouvelle
fenêtre VS Code. Vérifie que CLAUDE.md est bien à la racine et confirme-moi
que c'est prêt avant la suite.
```

Claude clone le repo, ouvre le dossier dans une nouvelle fenêtre VS Code, et te confirme. Continue dans cette nouvelle fenêtre pour les prompts suivants.

---

### Prompt 2 — Installer toutes les dépendances en une commande

Dans la nouvelle fenêtre VS Code (celle du repo cloné), ouvre Claude Code et colle ce prompt :

```
Setup environnement complet pour ce projet Empirik. Étape par étape, vérifie et
installe si manquant :
(1) Node.js LTS ≥ 20 et npm (via winget sous Windows, brew sous macOS, package
    manager natif sous Linux),
(2) Python 3.10+ et pip (idem),
(3) LibreOffice (idem ; sous Windows confirme le chemin
    C:\Program Files\LibreOffice\program\soffice.exe),
(4) packages npm globaux : pptxgenjs, react-icons, react, react-dom, sharp ;
    sous Windows configure aussi NODE_PATH=%APPDATA%\npm\node_modules,
(5) packages Python pip : markitdown[pptx], Pillow, PyMuPDF, google-generativeai,
    matplotlib,
(6) famille Poppins (ExtraLight 200, Light 300, Regular 400, Medium 500,
    SemiBold 600, Bold 700) — si manquante, télécharge depuis Google Fonts
    (https://fonts.google.com/specimen/Poppins) et installe les .ttf : Windows
    dans %LOCALAPPDATA%\Microsoft\Windows\Fonts (pas d'admin requis), macOS
    dans ~/Library/Fonts, Linux dans ~/.local/share/fonts puis fc-cache -fv.

À la fin, génère un rapport checklist ✅/❌ avec actions correctives pour chaque ❌.
Demande-moi confirmation avant toute installation qui pourrait demander
mon mot de passe ou un accès admin.
```

Claude exécute tout. Tu valides les éventuelles demandes d'autorisation système. Ça prend 5-10 minutes selon ce qui est déjà installé.

---

### Prompt 3 — Configurer tes clés API personnelles

Les clés API ne sont pas dans le repo (gitignored pour éviter les fuites). Tu dois les renseigner localement.

> **⚠ IMPORTANT** : utilise tes **propres** clés Gemini et OpenAI, OU demande des clés personnelles à Yannick. **Ne demande pas les clés d'un collègue**, ça perturbe le suivi des dépenses agence.
> - Créer une clé Gemini : https://aistudio.google.com/apikey (gratuit, quota généreux)
> - Créer une clé OpenAI : https://platform.openai.com/api-keys
> - DataForSEO : demande à Yannick

Une fois tes 3 clés en main, colle ce prompt dans Claude Code :

```
Crée 3 fichiers à la racine du projet pour mes clés API :
- clé-api-gemini.md contenant ma clé Gemini : [COLLE TA CLÉ ICI]
- clé-api-openai.md contenant ma clé OpenAI : [COLLE TA CLÉ ICI]
- clé-api-dataforseo.md contenant mes identifiants DataForSEO : [COLLE TES IDENTIFIANTS]

Ensuite teste les 3 clés avec un appel ping minimal (auth uniquement, pas de
génération volumineuse) pour confirmer qu'elles sont valides.

Rappel : ces 3 fichiers sont dans le .gitignore, donc ils ne seront jamais
pushés sur GitHub — ils restent strictement locaux.
```

> Si tu n'as qu'une seule clé pour démarrer (typiquement Gemini), mets-la et indique à Claude que les 2 autres seront ajoutées plus tard. Le système fonctionne dès que Gemini est disponible.

---

### Prompt 4 — Vérification finale de l'environnement

Avant de te lancer dans ta première présentation, vérifie que tout est bien en place :

```
Fais un audit complet de mon environnement pour ce projet Empirik. Vérifie :
(1) versions Node.js et npm, (2) Python ≥ 3.10 et pip, (3) chemin LibreOffice
et qu'il convertit bien un .pptx test en PDF, (4) packages npm globaux
(pptxgenjs, react-icons, react, react-dom, sharp), (5) packages Python
(markitdown, Pillow, PyMuPDF/fitz, google-generativeai, matplotlib),
(6) variable NODE_PATH sous Windows, (7) toutes les variantes Poppins
installées (ExtraLight, Light, Regular, Medium, SemiBold, Bold), (8) validité
des 3 clés API. Génère un rapport synthétique en checklist avec ✅ ou ❌
devant chaque point, et donne-moi un prompt prêt à coller pour corriger
chaque ❌.
```

Tu dois voir tous les points en ✅. Si ❌, copie le prompt correctif que Claude te propose.

---

### Prompt 5 — Démarrer ta première présentation

Quand tout est ✅, lance la création de ta première pres :

```
Je veux créer une nouvelle présentation pour [NOM DU CLIENT].
Le sujet est : [SUJET].
Le public cible est : [DIRECTION MARKETING / COMITÉ DE DIRECTION / ÉQUIPE TECHNIQUE / ETC.].
L'objectif est : [PITCH / AUDIT / BILAN / RESTITUTION DATA / ETC.].
Voici les inputs disponibles : [LISTE DES FICHIERS / DATA / BRIEF].

Applique strictement le workflow CLAUDE.md en 8 étapes : (1) lis CLAUDE.md +
PROCESS-ANTI-ERREURS.md + MASTER-CHECKLIST.md + guide_design_slides.md +
guide-slides-data-storytelling.md + guide_storytelling_presentations.md +
dataviz-guide.md, (2) propose-moi 2 à 3 angles narratifs distincts avec
structure et nombre de slides estimé, (3) attends ma validation, (4) détaille
le plan slide par slide avec type de graphique justifié pour chaque slide
data, (5) attends mon go final, (6) génère le .pptx, (7) lance la QA structurée,
(8) PRODUIS LE RAPPORT QA EXHAUSTIF en remplissant MASTER-CHECKLIST.md
(~170 items, ✅/❌ avec preuves point par point, score global, défauts
résiduels arbitrés). N'engage AUCUNE génération avant ma validation explicite
du plan, et ne livre AUCUN .pptx sans le rapport QA. En pre-flight : liste
les marques/outils à intégrer en logos, lance scripts/fetch_logos.py pour
les manquants.
```

Remplace les `[PLACEHOLDERS]` par les infos réelles de ton projet. Plus tu donnes de contexte, meilleurs sont les angles narratifs proposés.

---

## 🔄 Recevoir les mises à jour du process

Le système évolue régulièrement (nouvelles règles, helpers, corrections). Quand tu veux récupérer les dernières versions, colle ce prompt :

```
Mets à jour ce repo Empirik avec les dernières évolutions du process. Fais
un git pull sur la branche main, résume-moi en 3-5 bullets les changements
notables depuis ma dernière sync (compare avec git log --since), et signale
si une nouvelle dépendance est requise.
```

Tes clés API et tes présentations en cours restent intactes (elles sont gitignorées).

---

## 🤝 Proposer une amélioration au process

Si tu repères une faille ou que tu as une bonne pratique à codifier :

```
J'ai repéré [PROBLÈME / IDÉE D'AMÉLIORATION]. Voici le détail : [EXPLICATION].

Crée une branche dédiée, ajoute la règle au bon endroit dans CLAUDE.md ou
PROCESS-ANTI-ERREURS.md ou MASTER-CHECKLIST.md selon le type de règle
(de fond / tactique / vérification). Commit avec un message clair, push
la branche sur GitHub, et ouvre une Pull Request avec une description qui
explique le pourquoi de la règle et l'incident qui l'a motivée.
```

Claude fait le commit, push, et ouvre la PR. Yannick review et merge.

---

## 📂 Ce que contient ce repo

| Fichier | Rôle |
|---------|------|
| `SETUP.html` | Guide détaillé d'installation + premier lancement (équivalent visuel des prompts ci-dessus) |
| `CLAUDE.md` | Source unique de vérité : workflow 8 étapes + toutes les règles |
| `PROCESS-ANTI-ERREURS.md` | 11 erreurs récurrentes documentées + helpers code |
| `MASTER-CHECKLIST.md` | Rapport QA obligatoire à produire à chaque pres (~170 items) |
| `guide_design_slides.md` | Charte design détaillée |
| `guide-slides-data-storytelling.md` | Méthode Knaflic (Storytelling with Data) |
| `guide_storytelling_presentations.md` | Méthode Nancy Duarte |
| `dataviz-guide.md` | Référence Wilke pour les graphiques |
| `DESIGN_EMPIRIK.md` | 7 types d'assets visuels + prompts Gemini |
| `scripts/fetch_logos.py` | Récupération auto de logos officiels (4 couches) |
| `scripts/generate_image.py` | Génération d'images Gemini |
| `scripts/generate_chart.py` | Génération de graphes Python → PNG sans texte + JSON overlays |
| `assets/logos/` | Logos officiels génériques prêts à l'emploi |
| `Logos-Empirik.png` | Logo agence (slide cover uniquement) |

---

*Empirik · better with data*

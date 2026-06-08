# -*- coding: utf-8 -*-
"""Restaure les accents diacritiques français dans build_audit-perf-site-velura.js."""

import re
import sys
import os

BUILD_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "build_audit-perf-site-velura.js",
)

with open(BUILD_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Mots ASCII à remplacer par leur version accentuée — word-boundary appliqué.
# PRUDENCE : "à" vs "a", "ou" vs "où" sont gérés en cas spéciaux après (trop risqués en regex aveugle).
replacements = [
    # --- Mots fréquents prioritaires
    (r"\bequipe\b", "équipe"),
    (r"\bequipes\b", "équipes"),
    (r"\betape\b", "étape"),
    (r"\betapes\b", "étapes"),
    (r"\bdonnees\b", "données"),
    (r"\bdonnee\b", "donnée"),
    (r"\bchiffrees\b", "chiffrées"),
    (r"\bchiffree\b", "chiffrée"),
    (r"\breponse\b", "réponse"),
    (r"\breponses\b", "réponses"),
    (r"\bpresenter\b", "présenter"),
    (r"\bpresentez\b", "présentez"),
    (r"\bpresente\b", "présente"),
    (r"\bpresentes\b", "présentes"),
    (r"\bpresentee\b", "présentée"),
    (r"\bpresentees\b", "présentées"),
    (r"\bpresentation\b", "présentation"),
    (r"\bpresentations\b", "présentations"),
    (r"\bpresence\b", "présence"),
    (r"\bpresences\b", "présences"),
    (r"\bpresent\b", "présent"),
    # --- pre- → pré-
    (r"\bprealable\b", "préalable"),
    (r"\bprecis\b", "précis"),
    (r"\bprecise\b", "précise"),
    (r"\bprecisement\b", "précisément"),
    (r"\bprecisons\b", "précisons"),
    (r"\bprefere\b", "préfère"),
    (r"\bpreferer\b", "préférer"),
    (r"\bprepare\b", "prépare"),
    (r"\bpreparer\b", "préparer"),
    (r"\bpreserve\b", "préserve"),
    (r"\bpreserver\b", "préserver"),
    # --- re- → ré-
    (r"\brecuperer\b", "récupérer"),
    (r"\brecupere\b", "récupère"),
    (r"\brecupere?es?\b", "récupérées"),
    (r"\brecuperees\b", "récupérées"),
    (r"\brecuperee\b", "récupérée"),
    (r"\bresultat\b", "résultat"),
    (r"\bresultats\b", "résultats"),
    (r"\bresume\b", "résumé"),
    (r"\bregle\b", "règle"),
    (r"\bregles\b", "règles"),
    (r"\brealise\b", "réalisé"),
    (r"\brealiser\b", "réaliser"),
    (r"\brealiste\b", "réaliste"),
    (r"\brealite\b", "réalité"),
    (r"\bredige\b", "rédigé"),
    (r"\bredaction\b", "rédaction"),
    (r"\breduire\b", "réduire"),
    (r"\brepondre\b", "répondre"),
    (r"\brepondu\b", "répondu"),
    (r"\brevise\b", "révisé"),
    # --- e- en début de mot → é-
    (r"\beconomie\b", "économie"),
    (r"\beconomiser\b", "économiser"),
    (r"\beconomique\b", "économique"),
    (r"\beconomiques\b", "économiques"),
    (r"\becart\b", "écart"),
    (r"\becarts\b", "écarts"),
    (r"\bechantillon\b", "échantillon"),
    (r"\becole\b", "école"),
    (r"\beleve\b", "élevé"),
    (r"\belevee\b", "élevée"),
    (r"\beleves\b", "élevés"),
    (r"\belevees\b", "élevées"),
    (r"\belegant\b", "élégant"),
    (r"\belement\b", "élément"),
    (r"\belements\b", "éléments"),
    (r"\benergie\b", "énergie"),
    (r"\benergies\b", "énergies"),
    (r"\benerve\b", "énervé"),
    (r"\bentite\b", "entité"),
    (r"\bentites\b", "entités"),
    (r"\bequipement\b", "équipement"),
    (r"\bequivalent\b", "équivalent"),
    (r"\bequivalents\b", "équivalents"),
    (r"\bequivalence\b", "équivalence"),
    (r"\bevidemment\b", "évidemment"),
    (r"\bevident\b", "évident"),
    (r"\bevidence\b", "évidence"),
    (r"\bevolue\b", "évolue"),
    (r"\bevoluer\b", "évoluer"),
    (r"\bevolution\b", "évolution"),
    (r"\bevolutions\b", "évolutions"),
    # --- de- → dé-
    (r"\bdecouvert\b", "découvert"),
    (r"\bdecouverte\b", "découverte"),
    (r"\bdecouvertes\b", "découvertes"),
    (r"\bdecide\b", "décidé"),
    (r"\bdecider\b", "décider"),
    (r"\bdecideur\b", "décideur"),
    (r"\bdecideurs\b", "décideurs"),
    (r"\bdedie\b", "dédié"),
    (r"\bdediee\b", "dédiée"),
    (r"\bdefaut\b", "défaut"),
    (r"\bdefauts\b", "défauts"),
    (r"\bdefinir\b", "définir"),
    (r"\bdefinition\b", "définition"),
    (r"\bdefinitions\b", "définitions"),
    (r"\bdelai\b", "délai"),
    (r"\bdelais\b", "délais"),
    (r"\bdemarrer\b", "démarrer"),
    (r"\bdemarre\b", "démarre"),
    (r"\bdemarrage\b", "démarrage"),
    (r"\bdesavouer\b", "désavouer"),
    (r"\bdesaveu\b", "désaveu"),
    (r"\bdetail\b", "détail"),
    (r"\bdetails\b", "détails"),
    (r"\bdetaille\b", "détaillé"),
    (r"\bdetailler\b", "détailler"),
    (r"\bdetaillee\b", "détaillée"),
    (r"\bdeveloppe\b", "développé"),
    (r"\bdevelopper\b", "développer"),
    (r"\bdeveloppement\b", "développement"),
    # --- a- → â- ou à-
    (r"\bage\b", "âge"),
    (r"\bages\b", "âges"),
    (r"\bagee\b", "âgée"),
    (r"\baine\b", "aîné"),
    # --- Mots fréquents
    (r"\btres\b", "très"),
    (r"\bapres\b", "après"),
    (r"\bdes lors\b", "dès lors"),
    (r"\bsucces\b", "succès"),
    (r"\bacces\b", "accès"),
    (r"\bproces\b", "procès"),
    (r"\bcle\b", "clé"),
    (r"\bcles\b", "clés"),
    (r"\bcoute\b", "coûte"),
    (r"\bcouter\b", "coûter"),
    (r"\bcoutent\b", "coûtent"),
    (r"\bpremiere\b", "première"),
    (r"\bpremieres\b", "premières"),
    (r"\bderniere\b", "dernière"),
    (r"\bdernieres\b", "dernières"),
    (r"\bmaniere\b", "manière"),
    (r"\bmanieres\b", "manières"),
    (r"\bidee\b", "idée"),
    (r"\bidees\b", "idées"),
    (r"\bmeme\b", "même"),
    (r"\bmemes\b", "mêmes"),
    (r"\bcoeur\b", "cœur"),
    (r"\boeuvre\b", "œuvre"),
    (r"\boeuvres\b", "œuvres"),
    (r"\bnumero\b", "numéro"),
    (r"\bnumeros\b", "numéros"),
    (r"\bperiode\b", "période"),
    (r"\bperiodes\b", "périodes"),
    (r"\bmetier\b", "métier"),
    (r"\bmetiers\b", "métiers"),
    (r"\bbenefice\b", "bénéfice"),
    (r"\bbenefices\b", "bénéfices"),
    (r"\bbeneficier\b", "bénéficier"),
    (r"\bdeja\b", "déjà"),
    (r"\bvoila\b", "voilà"),
    (r"\bla-bas\b", "là-bas"),
    (r"\bcompare\b", "comparé"),
    (r"\bcomparees\b", "comparées"),
    (r"\bvalidees\b", "validées"),
    (r"\bvalidee\b", "validée"),
    (r"\blancees\b", "lancées"),
    (r"\blancee\b", "lancée"),
    (r"\bgenere\b", "généré"),
    (r"\bgenerer\b", "générer"),
    (r"\bgenerale\b", "générale"),
    (r"\bgeneral\b", "général"),
    (r"\bgenerique\b", "générique"),
    (r"\bgeneration\b", "génération"),
    # --- Spécifiques métier / charte
    (r"\bcategorisation\b", "catégorisation"),
    (r"\bcategorie\b", "catégorie"),
    (r"\bcategories\b", "catégories"),
    (r"\bquotidien\b", "quotidien"),
    (r"\bambition\b", "ambition"),
    (r"\bmediocre\b", "médiocre"),
    (r"\bspecifique\b", "spécifique"),
    (r"\bspecifiques\b", "spécifiques"),
    (r"\bspecificite\b", "spécificité"),
    (r"\bidentite\b", "identité"),
    (r"\bidentifie\b", "identifié"),
    (r"\bidentifier\b", "identifier"),
    (r"\bclientele\b", "clientèle"),
    (r"\bsalarie\b", "salarié"),
    (r"\bsalaries\b", "salariés"),
    (r"\bcree\b", "créé"),
    (r"\bcreer\b", "créer"),
    (r"\bcreee\b", "créée"),
    (r"\bcrees\b", "créés"),
    (r"\bcreees\b", "créées"),
    (r"\bcreatif\b", "créatif"),
    (r"\bcreative\b", "créative"),
    (r"\bcreatifs\b", "créatifs"),
    (r"\bcreatives\b", "créatives"),
    (r"\bcreation\b", "création"),
    (r"\bcreations\b", "créations"),
    (r"\bcontenue?s?\b", "contenu"),
    (r"\bcommentes?\b", "commenté"),
    (r"\bvalide\b", "validé"),
    (r"\bvalider\b", "valider"),
    (r"\bvalidation\b", "validation"),
    (r"\bevalue\b", "évalué"),
    (r"\bevaluer\b", "évaluer"),
    (r"\bevaluation\b", "évaluation"),
    (r"\bevaluations\b", "évaluations"),
    # --- Mots dépendant du contexte (à appliquer prudemment)
    # "Côté" en début de phrase ou après ponctuation
    (r"\bCote\b", "Côté"),
    (r"\bcote(?=[,\.\:\s])", "côté"),
    (r"\bDes\b", "Dès"),  # ATTENTION : peut conflicter avec "Des" article. Désactivé.
    (r"\bperformantes\b", "performantes"),  # déjà OK, garde
    (r"\bla\s+seconde\b", "la seconde"),  # déjà OK
    # Ponctuels métier de la pres Velura
    (r"\baudite\b", "audité"),
    (r"\bauditer\b", "auditer"),
    (r"\bmesure\b", "mesuré"),
    (r"\bmesurer\b", "mesurer"),
    (r"\bmesurees\b", "mesurées"),
    (r"\bmesuree\b", "mesurée"),
    (r"\bmodifie\b", "modifié"),
    (r"\bmodifier\b", "modifier"),
    (r"\borganise\b", "organisé"),
    (r"\borganiser\b", "organiser"),
    (r"\bpilote\b", "pilote"),  # ne pas modifier, c'est un nom
    (r"\bcamille\b", "camille"),  # déjà OK
    (r"\bantoine\b", "antoine"),  # déjà OK
    (r"\boptimise\b", "optimisé"),
    (r"\boptimiser\b", "optimiser"),
    (r"\boptimisation\b", "optimisation"),
    (r"\bcorrige\b", "corrigé"),
    (r"\bcorriger\b", "corriger"),
    (r"\bsecurise\b", "sécurisé"),
    (r"\bsecuriser\b", "sécuriser"),
    (r"\bsecurite\b", "sécurité"),
    (r"\bsemaine\b", "semaine"),  # OK
    (r"\bcalcule\b", "calculé"),
    (r"\bcalculer\b", "calculer"),
    (r"\bestime\b", "estimé"),
    (r"\bestimee\b", "estimée"),
    (r"\bestimer\b", "estimer"),
    (r"\bestimation\b", "estimation"),
    (r"\bestimations\b", "estimations"),
    (r"\bexploite\b", "exploité"),
    (r"\bexploiter\b", "exploiter"),
    (r"\baccompagne\b", "accompagné"),
    (r"\baccompagner\b", "accompagner"),
    (r"\bdiagnostic\b", "diagnostic"),  # OK
    (r"\bameliore\b", "amélioré"),
    (r"\bameliorer\b", "améliorer"),
    (r"\bamelioration\b", "amélioration"),
    (r"\bameliorations\b", "améliorations"),
    (r"\bautorise\b", "autorisé"),
    (r"\bautoriser\b", "autoriser"),
    (r"\bautorite\b", "autorité"),
    (r"\binclus\b", "inclus"),  # OK
    (r"\binclueese?\b", "incluse"),
    (r"\bincluse\b", "incluse"),
    (r"\bincluses\b", "incluses"),
]

# Désactiver les patterns problématiques par sécurité (peuvent toucher des mots anglais ou des noms propres)
SAFE_REPLACEMENTS = [pair for pair in replacements if pair[0] not in [r"\bDes\b", r"\bcompare\b"]]

original = content
total = 0
log_lines = []
for pattern, replacement in SAFE_REPLACEMENTS:
    matches = re.findall(pattern, content)
    if matches:
        n = len(matches)
        content = re.sub(pattern, replacement, content)
        total += n
        log_lines.append(f"  {pattern!r:40s} -> {replacement!r:25s}: {n}")

print(f"Total remplacements appliqués: {total}")
for line in log_lines:
    print(line)

# Sauvegarde en UTF-8 sans BOM
with open(BUILD_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print()
print("Fichier sauvegarde en UTF-8 sans BOM:", BUILD_PATH)

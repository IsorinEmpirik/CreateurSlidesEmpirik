# -*- coding: utf-8 -*-
"""2e passe correction accents — patterns supplémentaires identifiés au check."""

import re
import os

BUILD_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "build_audit-perf-site-velura.js",
)

with open(BUILD_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Patterns supplémentaires identifiés
extra_replacements = [
    # Identifiés par grep direct
    (r"\bReponses\b", "Réponses"),
    (r"\bBenefice\b", "Bénéfice"),
    (r"\bBenefices\b", "Bénéfices"),
    (r"\bdedies\b", "dédiés"),
    (r"\bdedie\b", "dédié"),
    (r"\bdediee\b", "dédiée"),
    (r"\bdediees\b", "dédiées"),
    (r"\bAcces\b", "Accès"),
    (r"\bDecoration\b", "Décoration"),
    (r"\bdecoration\b", "décoration"),
    (r"\btestes\b", "testés"),
    (r"\bteste\b", "testé"),
    (r"\btestee\b", "testée"),
    (r"\btestees\b", "testées"),
    (r"\bzero\b", "zéro"),
    (r"\bZero\b", "Zéro"),
    (r"\bEtre\b", "Être"),
    (r"\betes\b", "êtes"),
    (r"\bgeneratifs?\b", "génératif"),
    (r"\bgenerative\b", "générative"),
    (r"\bgeneratives\b", "génératives"),
    (r"\bgeneration\b", "génération"),
    (r"\bgenerations\b", "générations"),
    (r"\bgenerateur\b", "générateur"),
    (r"\bgenerateurs\b", "générateurs"),
    (r"\bconfigure\b", "configuré"),
    (r"\bconfigurer\b", "configurer"),
    (r"\bconfiguree\b", "configurée"),
    (r"\bstructurees\b", "structurées"),
    (r"\bstructuree\b", "structurée"),
    (r"\bstructures\b", "structures"),  # OK pas d'accent
    (r"\bstructurer\b", "structurer"),  # OK
    (r"\bcitees\b", "citées"),
    (r"\bcitee\b", "citée"),
    (r"\bcites\b", "cités"),
    # cite tout seul : à vérifier contexte. Sécurisé : ne le touche que quand suivi par "par" ou "dans" (= participe passé)
    (r"\bcite\b(?=\s+(par|dans|comme|au))", "cité"),
    # Autres
    (r"\bcategorise\b", "catégorisé"),
    (r"\bcategoriser\b", "catégoriser"),
    (r"\bcategorisation\b", "catégorisation"),
    (r"\bperdues?\b", "perdue"),
    (r"\bperdues\b", "perdues"),
    (r"\bperdues\b", "perdues"),
    (r"\bligne\s+de\s+seuil\b", "ligne de seuil"),  # OK
    (r"\bnumerotation\b", "numérotation"),
    (r"\bdesactive\b", "désactivé"),
    (r"\bdesactiver\b", "désactiver"),
    (r"\bdesactivee\b", "désactivée"),
    (r"\baltere\b", "altéré"),
    (r"\balterer\b", "altérer"),
    (r"\balterees\b", "altérées"),
    (r"\bameliore\b", "amélioré"),
    (r"\bamelioree\b", "améliorée"),
    (r"\bameliorees\b", "améliorées"),
    (r"\bamelioration\b", "amélioration"),
    (r"\bameliorations\b", "améliorations"),
    (r"\bgenericite\b", "généricité"),
    (r"\bspecifie\b", "spécifié"),
    (r"\bspecifier\b", "spécifier"),
    (r"\bspecifiee?\b", "spécifiée"),
    # Ponctuels métier de la pres
    (r"\bcanonique\b", "canonique"),  # OK
    (r"\bcanoniques\b", "canoniques"),  # OK
    (r"\benvergure\b", "envergure"),  # OK
    (r"\beditorial\b", "éditorial"),
    (r"\beditoriaux\b", "éditoriaux"),
    (r"\beditoriale\b", "éditoriale"),
    (r"\bemplaces?\b", "emplacés"),
    (r"\bemplacement\b", "emplacement"),  # OK
    (r"\bemplacements\b", "emplacements"),  # OK
    (r"\bsupprime\b", "supprimé"),
    (r"\bsupprimer\b", "supprimer"),
    (r"\bsupprimee\b", "supprimée"),
    (r"\bsupprimees\b", "supprimées"),
    (r"\bcorrige\b", "corrigé"),
    (r"\bcorriger\b", "corriger"),
    (r"\bcorrigee\b", "corrigée"),
    (r"\bcorrigees\b", "corrigées"),
    (r"\bameliore\b", "amélioré"),
    (r"\bameliorer\b", "améliorer"),
    (r"\bproblematique\b", "problématique"),
    (r"\bproblematiques\b", "problématiques"),
    (r"\bcaracterise\b", "caractérisé"),
    (r"\bcaracteristique\b", "caractéristique"),
    (r"\bcaracteristiques\b", "caractéristiques"),
    (r"\binterieur\b", "intérieur"),
    (r"\bexterieur\b", "extérieur"),
    (r"\bperiph\w+", "périphérique"),  # ATTENTION : trop large, désactivé sauf si besoin
    # Mots fréquents oubliés
    (r"\bdepart\b", "départ"),
    (r"\bdepenses?\b", "dépenses"),
    (r"\bdepense\b", "dépense"),
    (r"\bdepenser\b", "dépenser"),
    (r"\bdepasse\b", "dépassé"),
    (r"\bdepasser\b", "dépasser"),
    (r"\bdepense?e?s?\b", "dépensé"),
    (r"\bdeposer\b", "déposer"),
    (r"\bdepose\b", "déposé"),
    (r"\bproposer\b", "proposer"),  # OK
    (r"\bpropose\b", "propose"),  # OK
    (r"\bdisponibilite\b", "disponibilité"),
    (r"\bdiffere\b", "diffère"),
    (r"\bdifferent\b", "différent"),
    (r"\bdifferents\b", "différents"),
    (r"\bdifferente\b", "différente"),
    (r"\bdifferentes\b", "différentes"),
    (r"\bdifference\b", "différence"),
    (r"\bdifferences\b", "différences"),
    (r"\bcorroberer\b", "corroborer"),
    (r"\bevoque\b", "évoqué"),
    (r"\bevoquer\b", "évoquer"),
    (r"\bevolution\b", "évolution"),
    (r"\bbarillet\b", "barillet"),  # OK nom propre
    (r"\bvelura\b", "velura"),  # OK nom propre, déjà OK
    (r"\bmenace\b", "menace"),  # OK
    (r"\bmenacees\b", "menacées"),
    (r"\bvise\b", "visé"),
    (r"\bviser\b", "viser"),
    (r"\bvisez\b", "visez"),
    (r"\binvite\b", "invité"),
    (r"\binvitee?s?\b", "invitée"),
    (r"\binvitation\b", "invitation"),  # OK
    (r"\bidentifies?\b", "identifié"),
    (r"\binvers\w*", "inverse"),  # heuristique
    (r"\boppose\b", "opposé"),
    (r"\bopposer\b", "opposer"),
    (r"\boppositions\b", "oppositions"),  # OK
    (r"\bdedier\b", "dédier"),
    (r"\bdeleguer\b", "déléguer"),
    (r"\bdelegue\b", "délégué"),
    (r"\bdeleguee\b", "déléguée"),
    (r"\bderoulement\b", "déroulement"),
    (r"\bderoulen?t?\b", "déroule"),
    (r"\bderouler\b", "dérouler"),
    (r"\bdetermine\b", "déterminé"),
    (r"\bdetermines?\b", "déterminé"),
    (r"\bdeterminer\b", "déterminer"),
    (r"\bdetermination\b", "détermination"),
    # Le plus important : nouveaux mots du brouillon Velura
    (r"\bagee?\b", "âgée"),
    (r"\baines?\b", "aînés"),
    (r"\bdeception\b", "déception"),
    (r"\bdeceptif\b", "déceptif"),
    (r"\bdeceptive\b", "déceptive"),
    (r"\bdrole\b", "drôle"),
    (r"\bfacile\b", "facile"),  # OK
    (r"\bfreine\b", "freine"),  # OK
    (r"\bgele\b", "gelé"),
    (r"\bgerer\b", "gérer"),
    (r"\bgere\b", "gère"),  # ATTENTION : peut être "il gère" (à corriger) ou "gere" inexistant ; ici OK
    (r"\bcouvre\b", "couvre"),  # OK
    (r"\binnombrable\b", "innombrable"),  # OK
    (r"\bcontrolee\b", "contrôlée"),
    (r"\bcontroler\b", "contrôler"),
    (r"\bcontrole\b", "contrôle"),
    # Spéciaux Q1, Q2, etc. - sigles avec accents
    (r"\b1\)\s*Pourquoi\b", "1) Pourquoi"),
    (r"\b2\)\s*Combien\b", "2) Combien"),
    # Maintenant : "à" isolé vs "a" isolé. PRUDENCE ABSOLUE.
    # "a" verbe avoir : "il a" — pas d'accent
    # "à" préposition : "à 3 semaines", "à 30 jours", "à votre" — accent
    # Pas faisable avec regex aveugle. Cas spéciaux :
    (r"(\d+)\s+a\s+(\d+)", r"\1 à \2"),  # "30 a 60" → "30 à 60"
    (r"(\d+)\s+a\s+([JMAS])", r"\1 à \2"),  # "30 a J+60"
    (r"\ba\s+(\d+)\s*(k€|€|%)", r"à \1\2"),  # "a 25 k€" → "à 25 k€"
    (r"\ba\s+ces\b", "à ces"),
    (r"\ba\s+leur\b", "à leur"),
    (r"\ba\s+leurs\b", "à leurs"),
    (r"\ba\s+votre\b", "à votre"),
    (r"\ba\s+vos\b", "à vos"),
    (r"\ba\s+nos\b", "à nos"),
    (r"\ba\s+notre\b", "à notre"),
    (r"\ba\s+son\b", "à son"),
    (r"\ba\s+sa\b", "à sa"),
    (r"\ba\s+ses\b", "à ses"),
    (r"\ba\s+l'\b", "à l'"),
    (r"\ba\s+la\b", "à la"),
    (r"\ba\s+le\b", "au "),  # "a le" → "au"
    (r"\ba\s+les\b", "aux "),
    (r"\ba\s+m\+\b", "à m+"),  # "a m+12"
    (r"\bjusqu'a\b", "jusqu'à"),
    (r"\bjusque-la\b", "jusque-là"),
    (r"\bdes\s+m\+", "dès m+"),
    (r"\bdes\s+J\+", "dès J+"),
    (r"\bdes\s+lundi\b", "dès lundi"),
    (r"\bdes\s+demain\b", "dès demain"),
    (r"\bdes\s+que\b", "dès que"),
    # "ou" → "où" UNIQUEMENT dans "où en est"
    (r"\bou\s+en\s+est\b", "où en est"),
    (r"\bou\s+en\s+sommes\b", "où en sommes"),
    (r"\bou\s+vous\s+en\b", "où vous en"),
    # "déjà" — au cas où
    (r"\bdeja\b", "déjà"),
]

# Désactiver les patterns trop larges
SAFE = [pair for pair in extra_replacements if pair[0] not in [r"\bperiph\w+"]]

total = 0
log_lines = []
for pattern, replacement in SAFE:
    matches = re.findall(pattern, content)
    if matches:
        n = len(matches)
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0 and new_content != content:
            content = new_content
            total += count
            log_lines.append(f"  {pattern!r:50s} -> {replacement!r:30s}: {count}")

print(f"Total remplacements (pass 2): {total}")
for line in log_lines:
    print(line)

with open(BUILD_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print()
print("Sauvegardé:", BUILD_PATH)

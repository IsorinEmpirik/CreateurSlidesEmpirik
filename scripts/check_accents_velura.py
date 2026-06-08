# -*- coding: utf-8 -*-
"""Scanne build_audit-perf-site-velura.js et liste les mots français sans accent suspects."""

import re
import os

BUILD_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "build_audit-perf-site-velura.js",
)

with open(BUILD_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Extraire uniquement les chaînes de caractères entre guillemets simples ou doubles
# Patterns simplifiés (n'attrape pas tout mais l'essentiel)
strings = []
for match in re.finditer(r'"([^"\\]*(?:\\.[^"\\]*)*)"', content):
    strings.append(match.group(1))
for match in re.finditer(r"'([^'\\]*(?:\\.[^'\\]*)*)'", content):
    strings.append(match.group(1))

all_strings_text = "\n".join(strings)

# Mots français sans accent suspects (à vérifier manuellement)
suspect_patterns = [
    r"\bequip\w*",
    r"\bdonnees?\b",
    r"\bchiffrees?\b",
    r"\breponses?\b",
    r"\bpresent\w*",
    r"\bpresence\w*",
    r"\bsecurise\w*",
    r"\bsecurite\b",
    r"\bameliore\w*",
    r"\bperiodes?\b",
    r"\bderniere?s?\b",
    r"\bpremieres?\b",
    r"\bmaniere?s?\b",
    r"\bidee?s?\b",
    r"\bmemes?\b",
    r"\bcoute\w*",
    r"\bcafe\w*",
    r"\bcle\b",
    r"\bcles\b",
    r"\bcoeur\b",
    r"\boeuvre\w*",
    r"\bagee?\b",
    r"\bage\b",
    r"\bsysteme?s?\b",
    r"\bmetiers?\b",
    r"\bsalaries?\b",
    r"\bbenefices?\b",
    r"\bbeneficier\b",
    r"\bcategorie?s?\b",
    r"\bspecifique?s?\b",
    r"\bidentite\b",
    r"\bdetails?\b",
    r"\bdetaillee?s?\b",
    r"\bdefauts?\b",
    r"\bdedie\w*",
    r"\bdelai?s?\b",
    r"\bdesaveu\b",
    r"\bdesavouer\b",
    r"\bdecouvert\w*",
    r"\bdetaille\w*",
    r"\bevolution\w*",
    r"\beconomique?s?\b",
    r"\beconomie\b",
    r"\beconomiser\b",
    r"\becart\w*",
    r"\beleve?e?s?\b",
    r"\belegant\b",
    r"\belements?\b",
    r"\benergie\w*",
    r"\bentite?s?\b",
    r"\bequivalent\b",
    r"\bevident\w*",
    r"\bevoluer\b",
    r"\bautorite\b",
    r"\bautorise\w*",
    r"\bderniere\w*",
    r"\bclientele\b",
    r"\boptimise\w*",
    r"\borganise\w*",
    r"\bvalide\w*",
    r"\bevalue\w*",
    r"\bestimee?s?\b",
    r"\bgenere?e?s?\b",
    r"\bgenerale\b",
    r"\bgeneration\b",
    r"\bappuye\w*",
    r"\baudite\w*",
    r"\bnumero\w*",
    r"\bdeja\b",
    r"\bvoila\b",
    r"\btres\b",
    r"\bapres\b",
    r"\bsucces\b",
    r"\bacces\b",
    r"\bcote\b",
    r"\bCote\b",
    r"\bDes\s+lors\b",
    r"\bces\s+\w+\s+lors\b",
    # mots se terminant par -e qui pourraient être -é
    r"\bvalide\b",
    r"\bnomme\b",
    r"\bappele\b",
    r"\bappelee\b",
    r"\bcite\b",
    r"\bcitees?\b",
    r"\bcitee\b",
    r"\bcoincide\b",
    r"\bcompose\b",
    r"\bcomposee?s?\b",
    r"\bresume\b",
    r"\bdemarre\b",
    r"\baxe\b",
    r"\baxes\b",
    r"\bgere\b",
    r"\bgerer\b",
    r"\bcombine\b",
    r"\bcombiner\b",
]

print("=== Mots français sans accent suspects encore présents ===\n")

found_count = 0
for pattern in suspect_patterns:
    matches = re.findall(pattern, all_strings_text, re.IGNORECASE)
    if matches:
        unique = list(set(matches))
        found_count += len(matches)
        print(f"  {pattern:30s} : {len(matches)} occurrences, unique: {unique}")

print()
print(f"Total mots suspects : {found_count}")

# Échantillon des chaînes contenant peut-être encore des problèmes
print("\n=== Chaînes potentiellement non accentuées (échantillon, recherche de patterns) ===\n")
suspect_strings = []
for s in strings:
    if len(s) < 10:
        continue
    # Recherche très simple : présence de mots français sans aucun accent dans une chaîne longue
    # Heuristique : si une chaîne fait > 30 chars sans aucun caractère accentué, c'est suspect
    if len(s) > 30 and not re.search(r"[éèêëàâäùûüôöîïÿçœÉÈÊËÀÂÄÙÛÜÔÖÎÏŸÇŒ]", s):
        # Filter out URLs, paths, code-looking strings
        if any(ch in s for ch in ["/", "://", "#", "@", "px", "{", "}"]):
            continue
        # Filter out pure-English strings (basic)
        english_indicators = ["the ", "and ", "of ", "for ", "with ", "on ", "in "]
        if sum(1 for ind in english_indicators if ind in s.lower()) >= 2:
            continue
        suspect_strings.append(s)

for s in suspect_strings[:30]:
    print(f"  - {s!r}")

if len(suspect_strings) > 30:
    print(f"  ... et {len(suspect_strings) - 30} autres")

print(f"\nTotal chaînes longues sans aucun accent : {len(suspect_strings)}")

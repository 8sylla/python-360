"""Outils de persistance du carnet d'opportunités (lecture/écriture JSON)."""

import json
from pathlib import Path

# Path() est la façon moderne de désigner un fichier : elle fonctionne
# à l'identique sur Windows, macOS et Linux (fini les problèmes de \ et /).
FICHIER = Path("donnees.json")


def charger() -> list:
    """Renvoie la liste des opportunités enregistrées.

    Renvoie une liste vide si aucun fichier n'existe encore
    (cas du tout premier lancement).
    """
    if not FICHIER.exists():
        return []  # sortie anticipée : plus lisible qu'un gros if/else

    # encoding="utf-8" est OBLIGATOIRE : sans lui, les accents et les caractères
    # non latins peuvent être illisibles selon la machine.
    with FICHIER.open("r", encoding="utf-8") as f:
        return json.load(f)


def sauvegarder(opportunites: list) -> None:
    """Écrit la liste complète dans le fichier JSON (écrase le contenu)."""
    with FICHIER.open("w", encoding="utf-8") as f:
        # indent=2 -> lisible par un humain
        # ensure_ascii=False -> conserve les accents tels quels
        json.dump(opportunites, f, indent=2, ensure_ascii=False)

"""Outils de persistance du carnet de dépenses (lecture / écriture JSON).

Ce module ne fait qu'une chose : lire et écrire le fichier `depenses.json`.
Il ne connaît rien du menu ni de l'affichage — c'est un tiroir d'outils, on
l'importe depuis tracker.py.
"""

import json
from pathlib import Path

# Path() : la façon moderne de désigner un fichier, identique sur Windows,
# macOS et Linux (fini les soucis de \ contre /). Le fichier est cherché
# à côté de ce module, pas dans le dossier courant du terminal.
FICHIER = Path(__file__).parent / "depenses.json"


def charger() -> list:
    """Renvoie la liste des dépenses enregistrées.

    Renvoie une liste vide si aucun fichier n'existe encore (cas du tout
    premier lancement) : on évite ainsi une FileNotFoundError.
    """
    if not FICHIER.exists():
        return []                       # sortie anticipée, plus lisible
    with FICHIER.open(encoding="utf-8") as f:
        return json.load(f)             # texte JSON -> objets Python


def sauvegarder(depenses: list) -> None:
    """Écrit la liste complète dans le fichier JSON (écrase le contenu)."""
    with FICHIER.open("w", encoding="utf-8") as f:
        # indent=2         -> le fichier reste lisible par un humain
        # ensure_ascii=False -> conserve les accents ("é", "à"...)
        json.dump(depenses, f, indent=2, ensure_ascii=False)

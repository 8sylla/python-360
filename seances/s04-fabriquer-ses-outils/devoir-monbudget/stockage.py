"""Outils de persistance du carnet de dépenses (lecture / écriture JSON).

SQUELETTE À COMPLÉTER — remplis les deux `# TODO`.
Ce module ne fait qu'une chose : lire et écrire `depenses.json`. Il ne connaît
ni le menu ni l'affichage. tracker.py l'importera.
"""

import json
from pathlib import Path

# Déjà fait pour toi : le fichier est cherché à côté de ce module.
FICHIER = Path(__file__).parent / "depenses.json"


def charger() -> list:
    """Renvoie la liste des dépenses enregistrées, ou [] si le fichier
    n'existe pas encore (tout premier lancement)."""
    # TODO :
    #   - si FICHIER n'existe pas (FICHIER.exists() est False) -> return []
    #   - sinon, ouvre-le en lecture avec `with FICHIER.open(encoding="utf-8") as f:`
    #     et renvoie json.load(f)
    return []  # <- remplace


def sauvegarder(depenses: list) -> None:
    """Écrit la liste complète dans le fichier JSON (écrase le contenu)."""
    # TODO :
    #   - ouvre FICHIER en écriture : `with FICHIER.open("w", encoding="utf-8") as f:`
    #   - json.dump(depenses, f, indent=2, ensure_ascii=False)
    pass  # <- remplace

"""03 — CORRIGÉ. Fichiers (pathlib + JSON) et erreurs (try / except)."""

import json
from pathlib import Path

FICHIER = Path(__file__).parent / "carnet_demo.json"


def sauvegarder(depenses):
    """Écrit la liste de dépenses dans le fichier JSON."""
    with FICHIER.open("w", encoding="utf-8") as f:
        json.dump(depenses, f, indent=2, ensure_ascii=False)


def charger():
    """Rend les dépenses du fichier, ou [] si le fichier n'existe pas encore."""
    if not FICHIER.exists():
        return []
    with FICHIER.open(encoding="utf-8") as f:
        return json.load(f)


def ajouter(titre, categorie, montant):
    """Charge le carnet, ajoute une dépense, puis sauvegarde. Ne rend rien."""
    depenses = charger()
    depenses.append({"titre": titre, "categorie": categorie, "montant": montant})
    sauvegarder(depenses)


depart = [
    {"titre": "Café", "categorie": "Alimentation", "montant": 2.50},
    {"titre": "Bus", "categorie": "Transport", "montant": 1.90},
]
sauvegarder(depart)
ajouter("Livre", "Loisirs", 18.90)
print("Carnet après ajout :", charger())

# TODO 2 — les exceptions attendues :
#   int("douze")                       -> ValueError
#   charger()[99]                      -> IndexError
#   depart[0]["justificatif"]          -> KeyError
#   json.loads("{ pas du json }")      -> json.JSONDecodeError

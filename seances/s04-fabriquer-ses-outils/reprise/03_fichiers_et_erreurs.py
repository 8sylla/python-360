# """03 — Fichiers (pathlib + JSON) et erreurs (try / except).

# On donne enfin une mémoire longue à nos données : on les écrit sur le disque,
# puis on les relit. Et on met la ceinture de sécurité autour des saisies.
# """

# import json
# from pathlib import Path

# # Path() désigne un fichier de façon portable (Windows / macOS / Linux).
# # Le fichier sera créé À CÔTÉ de ce script, quel que soit le dossier courant.
# FICHIER = Path(__file__).parent / "carnet_demo.json"


# # ── On regarde ensemble : écrire puis relire ─────────────────────────────
# def sauvegarder(depenses):
#     """Écrit la liste de dépenses dans le fichier JSON."""
#     with FICHIER.open("w", encoding="utf-8") as f:
#         json.dump(depenses, f, indent=2, ensure_ascii=False)


# def charger():
#     """Rend les dépenses du fichier, ou [] si le fichier n'existe pas encore."""
#     if not FICHIER.exists():
#         return []
#     with FICHIER.open(encoding="utf-8") as f:
#         return json.load(f)


# depart = [
#     {"titre": "Café", "categorie": "Alimentation", "montant": 2.50},
#     {"titre": "Bus", "categorie": "Transport", "montant": 1.90},
# ]
# sauvegarder(depart)
# print("Écrit dans :", FICHIER.name)
# print("Relu depuis le disque :", charger())
# print("(Ouvre carnet_demo.json dans VS Code : tu vois tes données.)\n")


# # ── On regarde ensemble : la ceinture de sécurité ────────────────────────
# def demander_montant(question):
#     """Redemande tant que ce n'est pas un nombre valide (ne plante jamais)."""
#     while True:
#         reponse = input(question)
#         try:
#             return float(reponse.replace(",", "."))   # accepte 12,50
#         except ValueError:
#             print("  Attention : ce n'est pas un montant. Réessaie (ex : 12.50).")


# # Décommente pour tester la saisie robuste dans le terminal :
# montant = demander_montant("Montant de la dépense : ")
# print("Tu as saisi :", montant)


# # ── À toi de jouer ───────────────────────────────────────────────────────
# # TODO 1 : écris ajouter(titre, categorie, montant) qui CHARGE le carnet,
# #          ajoute la nouvelle dépense, puis SAUVEGARDE. Elle ne rend rien.
# def ajouter(titre, categorie, montant):
#     """Ajoute une dépense au carnet (charge puis sauvegarde)."""
#     depenses = charger()
#     depenses.append({"titre": titre, "categorie": categorie, "montant": montant})
#     sauvegarder(depenses)

# ajouter("Pizza", "Alimentation", 12.50)
# print("Après ajout :", charger())

# TODO 2 : prédis quelle exception lève chacune de ces lignes, puis vérifie
#          en les décommentant UNE PAR UNE (lis la dernière ligne du traceback) :
int("douze")
charger()[99]
depart[0]["justificatif"]
json.loads("{ ceci n'est pas du json }")
#
# Réponses attendues : ValueError · IndexError · KeyError · JSONDecodeError

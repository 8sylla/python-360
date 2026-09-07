"""04 — Gestionnaires de contexte et `match` structurel.

DEUX ANALOGIES :
  - le `with`, c'est la **ceinture de sécurité** : quoi qu'il arrive, on
    referme. Même si le bloc explose.
  - le `match` structurel, c'est le **gabarit de tri à formes** : le cube ne
    passe pas dans le trou rond. On filtre par la FORME, pas par la valeur.
"""

from contextlib import contextmanager

# ══════════════════════════════════════════════════════════════════════
#  1. Le with que tu connais déjà
# ══════════════════════════════════════════════════════════════════════
# with open(...) as f:  ->  ouvre, travaille, REFERME quoi qu'il arrive.
# Derrière, deux méthodes : __enter__ et __exit__. Écrivons-les.


class Chronometre:
    """Mesure la durée d'un bloc `with`."""

    def __init__(self, nom):
        self.nom = nom

    def __enter__(self):
        import time
        self.depart = time.perf_counter()
        return self          # SANS ce return, `as chrono` vaudrait None

    def __exit__(self, type_exc, valeur, trace):
        import time
        duree = (time.perf_counter() - self.depart) * 1000
        print(f"  [{self.nom}] {duree:.1f} ms")
        return False         # False = on NE masque PAS l'exception


with Chronometre("boucle") as chrono:
    total = sum(range(500_000))
print("Résultat :", total)


# ══════════════════════════════════════════════════════════════════════
#  2. La version courte : @contextmanager
# ══════════════════════════════════════════════════════════════════════
@contextmanager
def section(nom):
    """Six lignes remplacent __enter__ / __exit__.

    Avant le yield = l'entrée. Après (dans le finally) = la sortie.
    Le `finally` est OBLIGATOIRE : sans lui, une erreur dans le bloc
    sauterait la fermeture — précisément ce qu'on voulait éviter.
    """
    print(f"--- début {nom} ---")
    try:
        yield
    finally:
        print(f"--- fin {nom} ---")


with section("traitement"):
    print("  je travaille")

# La preuve que ça referme même en cas d'erreur :
try:
    with section("qui plante"):
        raise ValueError("boum")
except ValueError as erreur:
    print("Erreur bien propagée :", erreur)


# ══════════════════════════════════════════════════════════════════════
#  3. Le match STRUCTUREL (PEP 636) — au-delà du menu
# ══════════════════════════════════════════════════════════════════════
def decrire(donnee):
    """Filtre par la FORME de la donnée, pas par sa valeur."""
    match donnee:
        # motif de dictionnaire (matche si AU MOINS ces clés existent)
        case {"titre": str(titre), "montant": (int() | float()) as m} if m >= 100:
            return f"grosse dépense : {titre} ({m})"

        case {"titre": str(titre), "montant": (int() | float())}:
            return f"petite dépense : {titre}"

        # motif de séquence (matche exactement 2 éléments)
        case [titre, montant]:
            return f"ligne CSV : {titre} = {montant}"

        # motif de séquence avec reste
        case [titre, *reste]:
            return f"ligne longue : {titre} (+{len(reste)} colonnes)"

        case _:                       # le joker, TOUJOURS en dernier
            return "forme inconnue"


exemples = [
    {"titre": "Loyer", "montant": 850.0},
    {"titre": "Café", "montant": 2.5},
    ["Bus", 1.9],
    ["Courses", 54.2, "Alimentation", "carte"],
    42,
]
print()
for exemple in exemples:
    print(" ", decrire(exemple))


# ══════════════════════════════════════════════════════════════════════
#  À toi de jouer
# ══════════════════════════════════════════════════════════════════════
# TODO 1 : écris un context manager  @contextmanager  nommé  fichier_temporaire
#          qui crée un fichier, le rend (yield), puis le SUPPRIME dans le
#          finally. Vérifie qu'il disparaît même si le bloc lève une erreur.

# TODO 2 : écris une classe  Voiture  utilisable en `with` : __enter__ affiche
#          « moteur démarré » et __exit__ « moteur coupé ». Vérifie que le
#          moteur est coupé même si le bloc plante.

# TODO 3 : complète `decrire` avec un cas pour un remboursement
#          ({"titre": ..., "montant": m} avec m < 0) qui renvoie
#          « remboursement : ... ». Attention à le placer AVANT les cas
#          plus généraux.

# TODO 4 (piège) : que se passe-t-il si tu mets  case _:  en PREMIER ?
#          Essaie, et lis l'erreur.

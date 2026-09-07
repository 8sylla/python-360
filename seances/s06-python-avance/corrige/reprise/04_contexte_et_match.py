"""04 — CORRIGÉ. Contextes et match structurel."""

from contextlib import contextmanager
from pathlib import Path
from tempfile import gettempdir


# TODO 1
@contextmanager
def fichier_temporaire(nom="essai.txt"):
    """Crée un fichier, le rend, puis le SUPPRIME quoi qu'il arrive."""
    chemin = Path(gettempdir()) / nom
    chemin.write_text("contenu de test", encoding="utf-8")
    try:
        yield chemin
    finally:
        chemin.unlink(missing_ok=True)      # le finally garantit le ménage


with fichier_temporaire() as f:
    print("dans le with, le fichier existe :", f.exists())
print("après le with, il a disparu       :", not f.exists())

# Et même si le bloc plante :
try:
    with fichier_temporaire() as f2:
        raise ValueError("boum")
except ValueError:
    pass
print("supprimé même après une erreur    :", not f2.exists())


# TODO 2
class Voiture:
    """Utilisable en `with` : le moteur se coupe quoi qu'il arrive."""

    def __enter__(self):
        print("  moteur démarré")
        return self                 # sans ce return, `as v` vaudrait None

    def __exit__(self, type_exc, valeur, trace):
        print("  moteur coupé")
        return False                # False = on ne masque pas l'exception


print("\nTrajet normal :")
with Voiture():
    print("  je roule")

print("Trajet qui plante :")
try:
    with Voiture():
        raise RuntimeError("panne")
except RuntimeError as erreur:
    print("  erreur propagée :", erreur)


# TODO 3
def decrire(donnee):
    """Le cas 'remboursement' doit passer AVANT les cas plus généraux."""
    match donnee:
        # remboursement : le plus spécifique, donc en premier
        case {"titre": str(titre), "montant": (int() | float()) as m} if m < 0:
            return f"remboursement : {titre} ({m})"

        case {"titre": str(titre), "montant": (int() | float()) as m} if m >= 100:
            return f"grosse dépense : {titre} ({m})"

        case {"titre": str(titre), "montant": (int() | float())}:
            return f"petite dépense : {titre}"

        case [titre, montant]:
            return f"ligne CSV : {titre} = {montant}"

        case [titre, *reste]:
            return f"ligne longue : {titre} (+{len(reste)} colonnes)"

        case _:
            return "forme inconnue"


print()
for exemple in [
    {"titre": "Remboursement", "montant": -20.0},
    {"titre": "Loyer", "montant": 850.0},
    {"titre": "Café", "montant": 2.5},
    ["Bus", 1.9],
    42,
]:
    print(" ", decrire(exemple))


# TODO 4 — le piège du joker en premier
# Mettre  case _:  en PREMIER provoque une SyntaxError :
#     SyntaxError: wildcard makes remaining patterns unreachable
# Python REFUSE de compiler : le joker rend tous les cas suivants morts.
# Le joker se met TOUJOURS en dernier.

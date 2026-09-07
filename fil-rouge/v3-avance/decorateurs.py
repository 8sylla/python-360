"""Décorateurs de MonBudget v3.

Un décorateur, c'est **l'emballage cadeau** : le contenu ne change pas, mais
on ajoute une couche autour (mesurer, journaliser, réessayer). La fonction
décorée garde son code — on ne le touche jamais.

Les trois règles d'or d'une enveloppe :
  1. `@functools.wraps(fonction)` — sinon la fonction perd son nom et sa doc ;
  2. `*args, **kwargs` — sinon elle ne marche que sur certaines signatures ;
  3. `return resultat` — sinon la fonction décorée rend None.
"""

import functools
import time
from datetime import datetime
from pathlib import Path

# Chemin du journal. Les tests le redirigent vers un dossier temporaire.
JOURNAL = Path(__file__).parent / "journal.log"


def journalise(fonction):
    """Écrit une ligne dans le journal à chaque appel de la fonction décorée.

    Posé sur `Budget.ajouter` et `Budget.supprimer` : on garde une trace de
    toutes les écritures, sans une seule ligne ajoutée dans ces méthodes.
    """

    @functools.wraps(fonction)          # règle 1
    def enveloppe(*args, **kwargs):     # règle 2
        resultat = fonction(*args, **kwargs)
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # args[0] est `self` quand on décore une méthode : on ne le journalise pas.
        details = args[1:] if args else ()
        with JOURNAL.open("a", encoding="utf-8") as f:
            f.write(f"{horodatage} - {fonction.__name__} - {details}\n")
        return resultat                 # règle 3

    return enveloppe


def chronometre(fonction):
    """Affiche le temps d'exécution de la fonction décorée."""

    @functools.wraps(fonction)
    def enveloppe(*args, **kwargs):
        depart = time.perf_counter()
        resultat = fonction(*args, **kwargs)
        duree = time.perf_counter() - depart
        print(f"  [chrono] {fonction.__name__} : {duree * 1000:.1f} ms")
        return resultat

    return enveloppe


def reessayer(n: int = 3, delai: float = 0.5):
    """BONUS — un décorateur PARAMÉTRÉ (trois niveaux d'imbrication).

    `reessayer(n=3)` rend un décorateur ; ce décorateur rend l'enveloppe.
    C'est pour cela qu'on l'écrit `@reessayer(n=3)` — avec les parenthèses —
    alors que `@chronometre` s'écrit sans.
    """

    def decorateur(fonction):
        @functools.wraps(fonction)
        def enveloppe(*args, **kwargs):
            for tentative in range(1, n + 1):
                try:
                    return fonction(*args, **kwargs)
                except OSError as erreur:
                    if tentative == n:
                        raise               # dernière tentative : on laisse passer
                    print(f"  tentative {tentative}/{n} échouée ({erreur}), on réessaie")
                    time.sleep(delai)
            return None

        return enveloppe

    return decorateur


@functools.cache
def taux_change(devise: str) -> float:
    """Simule un appel réseau lent — le 2e appel est instantané.

    `@functools.cache` mémorise le résultat pour chaque argument déjà vu.
    C'est le carnet d'adresses : on ne cherche pas deux fois le même numéro.
    """
    time.sleep(0.4)                         # on fait semblant d'interroger le web
    return {"EUR": 1.0, "USD": 0.92, "MAD": 0.093}.get(devise, 1.0)


if __name__ == "__main__":
    print("Démo 1 — @chronometre et @functools.wraps")

    @chronometre
    def additionner_lentement(n: int) -> int:
        """Additionne 0 à n."""
        return sum(range(n))

    additionner_lentement(300_000)
    print("  nom conservé grace a @wraps :", additionner_lentement.__name__)
    print("  doc conservée              :", additionner_lentement.__doc__)

    print("\nDémo 2 — @functools.cache (le 2e appel est gratuit)")
    for _ in range(2):
        debut = time.perf_counter()
        taux_change("USD")
        print(f"  taux_change('USD') : {(time.perf_counter() - debut) * 1000:.0f} ms")

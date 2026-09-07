"""Décorateurs de MonBudget v3 — SQUELETTE À COMPLÉTER.

Les trois règles d'or d'une enveloppe :
  1. `@functools.wraps(fonction)`  — garder le nom et la docstring ;
  2. `*args, **kwargs`             — accepter toutes les signatures ;
  3. `return resultat`             — sinon la fonction décorée rend None.
"""

import functools
import time
from datetime import datetime
from pathlib import Path

JOURNAL = Path(__file__).parent / "journal.log"


def journalise(fonction):
    """Écrit une ligne dans JOURNAL à chaque appel de la fonction décorée.

    TODO 1 :
      - décore `enveloppe` avec @functools.wraps(fonction) ;
      - accepte *args et **kwargs ;
      - appelle la vraie fonction et GARDE son résultat ;
      - ouvre JOURNAL en mode "a" (encoding="utf-8") et écris une ligne
        contenant l'horodatage et fonction.__name__ ;
      - renvoie le résultat.

    Indice : quand on décore une MÉTHODE, args[0] est `self` — on ne le
    journalise pas, on prend args[1:].
    """
    # Pour l'instant, le décorateur ne fait rien : il rend la fonction telle
    # quelle. Remplace ce corps par une vraie enveloppe.
    return fonction


def chronometre(fonction):
    """Affiche le temps d'exécution de la fonction décorée.

    TODO 2 : même structure que journalise, mais on mesure
    `time.perf_counter()` avant et après, et on affiche la durée en ms.
    """
    return fonction


if __name__ == "__main__":
    # TODO 3 : décommente et vérifie que le nom EST conservé.
    #
    # @chronometre
    # def somme_lente(n):
    #     """Additionne 0 à n."""
    #     return sum(range(n))
    #
    # print(somme_lente(300_000))
    # print("nom :", somme_lente.__name__)   # doit afficher 'somme_lente'
    # print("doc :", somme_lente.__doc__)    # doit afficher la docstring
    print("Complète les TODO, puis décommente la démo ci-dessus.")
    _ = (functools, time, datetime)   # (évite un avertissement d'import inutilisé)

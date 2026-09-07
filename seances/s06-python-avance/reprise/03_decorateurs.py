"""03 — Les décorateurs, en quatre marches.

L'ANALOGIE : l'**emballage cadeau**. Le contenu ne change pas ; la couche
autour ajoute quelque chose. Un décorateur n'entre JAMAIS dans le code de la
fonction qu'il décore.

On monte les quatre marches dans l'ordre. Ne saute pas la marche 3.
"""

import functools
import time

# ══════════════════════════════════════════════════════════════════════
#  MARCHE 1 — une fonction est un OBJET : on peut la ranger dans une variable
# ══════════════════════════════════════════════════════════════════════
def saluer(nom):
    return f"Bonjour {nom}"


ma_fonction = saluer                 # pas d'appel : pas de parenthèses !
print("Marche 1 :", ma_fonction("Awa"))


# ══════════════════════════════════════════════════════════════════════
#  MARCHE 2 — une fonction peut RECEVOIR une fonction
# ══════════════════════════════════════════════════════════════════════
def appliquer_deux_fois(fonction, valeur):
    return fonction(fonction(valeur))


print("Marche 2 :", appliquer_deux_fois(lambda x: x * 3, 2))     # 18


# ══════════════════════════════════════════════════════════════════════
#  MARCHE 3 — une fonction peut RENDRE une fonction (la marche clé)
# ══════════════════════════════════════════════════════════════════════
def fabriquer_multiplicateur(facteur):
    def multiplier(x):
        return x * facteur           # `facteur` reste connu : c'est une fermeture
    return multiplier                # on rend la FONCTION, on ne l'appelle pas


tripler = fabriquer_multiplicateur(3)
print("Marche 3 :", tripler(10))     # 30


# ══════════════════════════════════════════════════════════════════════
#  MARCHE 4 — le décorateur : recevoir une fonction, en rendre une autre
# ══════════════════════════════════════════════════════════════════════
def chronometre(fonction):
    """Mesure le temps d'exécution. Les 3 règles d'or sont commentées."""

    @functools.wraps(fonction)            # RÈGLE 1 : garder nom + docstring
    def enveloppe(*args, **kwargs):       # RÈGLE 2 : accepter tous les arguments
        depart = time.perf_counter()
        resultat = fonction(*args, **kwargs)
        duree = (time.perf_counter() - depart) * 1000
        print(f"  [chrono] {fonction.__name__} : {duree:.1f} ms")
        return resultat                   # RÈGLE 3 : rendre le résultat !

    return enveloppe


@chronometre                              # équivaut à : lente = chronometre(lente)
def somme_lente(n):
    """Additionne 0 à n."""
    return sum(range(n))


print("Marche 4 :", somme_lente(300_000))
print("  nom conservé :", somme_lente.__name__)      # 'somme_lente' grâce à @wraps
print("  doc conservée:", somme_lente.__doc__)


# ══════════════════════════════════════════════════════════════════════
#  BONUS — @functools.cache : la démo la plus spectaculaire
# ══════════════════════════════════════════════════════════════════════
def fibonacci_lent(n):
    return n if n < 2 else fibonacci_lent(n - 1) + fibonacci_lent(n - 2)


@functools.cache                          # UNE ligne ajoutée
def fibonacci_rapide(n):
    return n if n < 2 else fibonacci_rapide(n - 1) + fibonacci_rapide(n - 2)


debut = time.perf_counter()
fibonacci_lent(28)
sans_cache = (time.perf_counter() - debut) * 1000

debut = time.perf_counter()
fibonacci_rapide(28)
avec_cache = (time.perf_counter() - debut) * 1000

print(f"\nfibonacci(28) sans cache : {sans_cache:8.1f} ms")
print(f"fibonacci(28) avec cache : {avec_cache:8.3f} ms  <- une seule ligne !")


# ══════════════════════════════════════════════════════════════════════
#  À toi de jouer
# ══════════════════════════════════════════════════════════════════════
# TODO 1 : écris un décorateur  @bavard  qui affiche « -> nom_de_la_fonction »
#          AVANT l'appel et « <- terminé » APRÈS. N'oublie aucune des 3 règles.

# TODO 2 : écris un décorateur  @compte_appels  qui compte les appels.
#          Range le compteur sur l'enveloppe : enveloppe.appels = 0, puis
#          incrémente. Vérifie avec  ma_fonction.appels.

# TODO 3 (piège) : enlève @functools.wraps de `chronometre` et relance.
#          Que valent  somme_lente.__name__  et  somme_lente.__doc__ ?

# TODO 4 (bonus) : écris un décorateur PARAMÉTRÉ  @repeter(n=3)  qui appelle
#          la fonction n fois. Indice : trois niveaux (repeter -> decorateur
#          -> enveloppe), et il s'écrit AVEC des parenthèses.

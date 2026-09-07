"""03 — CORRIGÉ. Décorateurs : bavard, compteur, et décorateur paramétré."""

import functools


# TODO 1
def bavard(fonction):
    """Annonce l'entrée et la sortie de la fonction décorée."""

    @functools.wraps(fonction)                 # règle 1
    def enveloppe(*args, **kwargs):            # règle 2
        print(f"-> {fonction.__name__}")
        resultat = fonction(*args, **kwargs)
        print("<- terminé")
        return resultat                        # règle 3

    return enveloppe


@bavard
def additionner(a, b):
    """Additionne deux nombres."""
    return a + b


print("résultat :", additionner(2, 3))
print("nom conservé :", additionner.__name__)


# TODO 2
def compte_appels(fonction):
    """Compte les appels. Le compteur vit SUR l'enveloppe."""

    @functools.wraps(fonction)
    def enveloppe(*args, **kwargs):
        enveloppe.appels += 1
        return fonction(*args, **kwargs)

    enveloppe.appels = 0
    return enveloppe


@compte_appels
def saluer(nom):
    return f"Bonjour {nom}"


saluer("Awa")
saluer("Sékou")
saluer("Fanta")
print("\nsaluer appelée", saluer.appels, "fois")


# TODO 3 — le piège : sans @functools.wraps
def chronometre_sans_wraps(fonction):
    def enveloppe(*args, **kwargs):
        return fonction(*args, **kwargs)
    return enveloppe                            # pas de @wraps !


@chronometre_sans_wraps
def documentee(x):
    """J'ai une docstring."""
    return x


print("\nSANS @wraps -> nom :", documentee.__name__, "| doc :", documentee.__doc__)
print("AVEC @wraps -> nom :", additionner.__name__, "| doc :", additionner.__doc__)


# TODO 4 — décorateur PARAMÉTRÉ (trois niveaux)
def repeter(n=3):
    """Fabrique un décorateur qui appelle la fonction n fois.

    Trois niveaux : repeter(n) rend `decorateur`, qui rend `enveloppe`.
    C'est pourquoi il s'écrit AVEC des parenthèses : @repeter(n=2).
    """

    def decorateur(fonction):
        @functools.wraps(fonction)
        def enveloppe(*args, **kwargs):
            resultat = None
            for _ in range(n):
                resultat = fonction(*args, **kwargs)
            return resultat                     # on rend le dernier résultat

        return enveloppe

    return decorateur


@repeter(n=3)
def coucou():
    print("  coucou")
    return "fini"


print()
print("retour :", coucou())

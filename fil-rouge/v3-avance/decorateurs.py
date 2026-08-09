"""Décorateurs du fil rouge (séance 6)."""

import functools
import time


def chronometre(fonction):
    """Affiche la durée d'exécution de la fonction décorée."""

    @functools.wraps(fonction)  # conserve le nom et la docstring de l'original
    def enveloppe(*args, **kwargs):
        # *args / **kwargs : "accepte n'importe quels arguments et transmets-les
        # tels quels". Indispensable pour un décorateur générique.
        depart = time.perf_counter()
        resultat = fonction(*args, **kwargs)
        duree = time.perf_counter() - depart

        print(f"[chrono] {fonction.__name__} : {duree:.3f} s")
        return resultat  # ⚠ SANS ce return, la fonction décorée rend None.

    return enveloppe  # on rend la fonction-enveloppe, pas son résultat


def journalise(fonction):
    """Journalise chaque appel : nom de la fonction et arguments reçus."""

    @functools.wraps(fonction)
    def enveloppe(*args, **kwargs):
        arguments = ", ".join(
            [repr(a) for a in args[1:]]  # args[0] = self
            + [f"{cle}={valeur!r}" for cle, valeur in kwargs.items()]
        )
        print(f"[journal] {fonction.__name__}({arguments})")
        return fonction(*args, **kwargs)

    return enveloppe


def reessayer(n: int = 3, delai: float = 1.0):
    """Décorateur PARAMÉTRÉ : réessaie n fois avant d'abandonner.

    Trois niveaux d'imbrication :
      1. reessayer(n=3)   -> rend un décorateur
      2. le décorateur    -> rend une enveloppe
      3. l'enveloppe      -> appelle la vraie fonction

    Réutilisé tel quel en séance 9 pour absorber les erreurs réseau.
    """

    def decorateur(fonction):
        @functools.wraps(fonction)
        def enveloppe(*args, **kwargs):
            derniere_erreur = None
            for tentative in range(1, n + 1):
                try:
                    return fonction(*args, **kwargs)
                except Exception as erreur:  # noqa: BLE001 (volontaire ici)
                    derniere_erreur = erreur
                    print(f"[reessai] tentative {tentative}/{n} échouée : {erreur}")
                    if tentative < n:
                        time.sleep(delai)
            raise derniere_erreur

        return enveloppe

    return decorateur

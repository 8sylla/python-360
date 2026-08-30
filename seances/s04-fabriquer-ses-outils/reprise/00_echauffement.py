"""00 — Échauffement : prédis l'output AVANT d'exécuter.

Pour chaque bloc : lis le code, écris ta prédiction sur une feuille, PUIS
lance le fichier (F5 ou le triangle ▶) et compare. Les réponses attendues
sont en commentaire, plus bas — ne les regarde qu'après.
"""

print("=== Échauffement séance 4 ===\n")


# ── Piège 1 : return vs print ────────────────────────────────────────────
def double(n):
    print(n * 2)        # affiche... mais que RENVOIE la fonction ?


resultat = double(5)
print("Piège 1 — resultat vaut :", resultat)
# Prédis la valeur de `resultat`.  (Réponse tout en bas.)


# ── Piège 2 : la valeur par défaut ───────────────────────────────────────
def saluer(prenom, politesse="Bonjour"):
    return f"{politesse} {prenom} !"


print("Piège 2a :", saluer("Awa"))
print("Piège 2b :", saluer("Sékou", "Salut"))
print("Piège 2c :", saluer(politesse="Bonsoir", prenom="Fanta"))


# ── Piège 3 : la portée ──────────────────────────────────────────────────
def prix_ttc(prix_ht):
    tva = prix_ht * 0.2
    return prix_ht + tva


print("Piège 3a :", prix_ttc(100))
# La ligne suivante est en commentaire EXPRÈS. Décommente-la, relance, et
# lis la dernière ligne de l'erreur. Pourquoi `tva` est-elle introuvable ?
# print("Piège 3b :", tva)


# ── Piège 4 : une fonction sans return ───────────────────────────────────
def additionner(a, b):
    somme = a + b
    # (oups, on a oublié le return)


x = additionner(3, 4)
print("Piège 4 — x vaut :", x)


# ═════════════════════════════════════════════════════════════════════════
#  RÉPONSES ATTENDUES (à lire après avoir prédit)
# ═════════════════════════════════════════════════════════════════════════
#  Piège 1 : affiche "10", puis resultat = None. `print` n'est pas `return`.
#  Piège 2 : "Bonjour Awa !" / "Salut Sékou !" / "Bonsoir Fanta !"
#            (nommer les arguments rend l'ordre indifférent).
#  Piège 3 : 120.0, puis NameError: name 'tva' is not defined.
#            `tva` n'existe qu'à l'intérieur de la fonction (la portée).
#  Piège 4 : x = None. Sans `return`, une fonction renvoie None.

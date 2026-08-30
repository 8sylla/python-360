"""01 — Des classiques, transformés en fonctions.

Règle du jour : une fonction REND (return), elle n'affiche pas. C'est ce qui
la rend réutilisable — on peut se servir de son résultat ailleurs.

Complète chaque `# TODO`. Le fichier tourne déjà : les parties non finies
affichent un rappel jusqu'à ce que tu les écrives.
"""


# ── On regarde ensemble : FizzBuzz, version fonction ─────────────────────
# Classique des entretiens. On le RANGE dans une fonction qui rend le mot,
# au lieu de l'afficher. Ainsi on peut le tester, le réutiliser, le compter.
def fizzbuzz(n):
    """Rend 'Fizz', 'Buzz', 'FizzBuzz' ou le nombre, selon les multiples."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


print("FizzBuzz de 1 à 15 :")
for i in range(1, 16):
    print(fizzbuzz(i), end="  ")
print("\n")


# ── À toi de jouer : le pourboire ────────────────────────────────────────
def pourboire(addition, pourcentage=10):
    """Rend le montant du pourboire pour une addition donnée.

    Exemple : pourboire(50) doit rendre 5.0 ; pourboire(50, 15) -> 7.5
    """
    # TODO : calcule et RENVOIE le pourboire (addition * pourcentage / 100).
    return None  # <- remplace


# Petit test intégré : quand ta fonction est bonne, la ligne dit "OK".
attendu = 7.5
obtenu = pourboire(50, 15)
print("Pourboire(50, 15) =", obtenu, "->", "OK" if obtenu == attendu else "à compléter")


# ── À toi de jouer : convertisseur d'unités ──────────────────────────────
def celsius_vers_fahrenheit(c):
    """Rend la température en Fahrenheit.  °F = °C * 9/5 + 32"""
    # TODO : renvoie la conversion. 100 °C -> 212.0 °F ; 0 °C -> 32.0 °F
    return None  # <- remplace


for temp in (0, 37, 100):
    print(f"{temp} °C -> {celsius_vers_fahrenheit(temp)} °F")


# ── Bonus : compter les Fizz ─────────────────────────────────────────────
# Puisque fizzbuzz() RETOURNE (au lieu d'afficher), on peut s'en servir.
# TODO : compte combien de nombres de 1 à 100 donnent exactement "Fizz".
#        (indice : une boucle, un compteur, un if fizzbuzz(i) == "Fizz")

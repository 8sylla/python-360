"""01 — CORRIGÉ. Des classiques, transformés en fonctions."""


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


def pourboire(addition, pourcentage=10):
    """Rend le montant du pourboire pour une addition donnée."""
    return addition * pourcentage / 100


attendu = 7.5
obtenu = pourboire(50, 15)
print("Pourboire(50, 15) =", obtenu, "->", "OK" if obtenu == attendu else "à compléter")


def celsius_vers_fahrenheit(c):
    """Rend la température en Fahrenheit.  °F = °C * 9/5 + 32"""
    return c * 9 / 5 + 32


for temp in (0, 37, 100):
    print(f"{temp} °C -> {celsius_vers_fahrenheit(temp)} °F")


# Bonus : compter les "Fizz" de 1 à 100.
nb_fizz = 0
for i in range(1, 101):
    if fizzbuzz(i) == "Fizz":
        nb_fizz += 1
print("\nNombre de 'Fizz' (exactement) entre 1 et 100 :", nb_fizz)  # 27

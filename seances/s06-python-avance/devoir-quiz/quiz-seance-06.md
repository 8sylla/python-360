# DEVOIR — Séance 6 « Sous le capot »
## Quiz de compréhension

**Formation Python 360° · Commission Scientifique nationale — ASEGUIM**

| | |
|---|---|
| **Barème** | 100 points |
| **Durée conseillée** | 1 h 30 |
| **Rendu** | sur Google Classroom, en texte (pas de capture d'écran) |

---

## Comment faire ce devoir

Cette séance est la plus dense du cursus. Ce devoir n'évalue **pas** ta
capacité à écrire du code : il évalue ta **compréhension**. C'est ce qui
compte ici.

**Trois règles :**

1. **Réponds d'abord SANS exécuter le code.** C'est tout l'intérêt : on veut
   savoir ce que *tu* prévois, pas ce que la machine affiche.
2. **Ensuite, vérifie en exécutant.** Si tu t'es trompé, note-le et explique
   pourquoi — une erreur comprise vaut plus qu'une bonne réponse devinée.
3. **Justifie toujours en une phrase.** « Faux » sans explication ne rapporte
   pas les points ; « Faux, parce que… » les rapporte tous.

Les niveaux montent en difficulté. Si tu bloques au niveau 4 ou 5, ce n'est
pas grave : réponds ce que tu peux, l'important est de montrer ton
raisonnement.

---

# NIVEAU 1 — Reconnaître (10 points)

*Une seule bonne réponse par question. 1 point chacune.*

**1.1** Quand tu écris `len(objet)`, quelle méthode Python cherche-t-il ?
- a) `taille()`
- b) `__len__`
- c) `__size__`
- d) `count()`

**1.2** Quelle méthode est utilisée pour afficher un objet **à l'intérieur
d'une liste** ?
- a) `__str__`
- b) `__repr__`
- c) `__format__`
- d) `__print__`

**1.3** Quel mot-clé transforme une fonction en générateur ?
- a) `return`
- b) `generate`
- c) `yield`
- d) `lazy`

**1.4** À quoi sert `@functools.wraps` ?
- a) à accélérer la fonction décorée
- b) à mettre le résultat en cache
- c) à conserver le nom et la docstring de la fonction décorée
- d) à autoriser plusieurs décorateurs

**1.5** Quelle méthode débloque `for x in objet` ?
- a) `__next__` seulement
- b) `__iter__`
- c) `__loop__`
- d) `__getitem__` obligatoirement

**1.6** Que doit renvoyer `__enter__` pour que `with X() as v:` donne un `v`
utilisable ?
- a) `True`
- b) `None`
- c) `self`
- d) rien

**1.7** Combien de fois peut-on parcourir **le même** générateur ?
- a) autant de fois qu'on veut
- b) une seule fois
- c) deux fois
- d) cela dépend de sa taille
 
**1.8** Quelle commande **met le code en forme** (indentation, espaces) ?
- a) `ruff check .`
- b) `ruff format .`
- c) `pytest -q`
- d) `pip install`

**1.9** Où doit se placer `case _` dans un `match` ?
- a) en premier
- b) au milieu
- c) en dernier
- d) n'importe où

**1.10** Que fait Python à `__hash__` quand tu définis `__eq__` dans une
classe ?
- a) rien du tout
- b) il le met à `None`
- c) il le recalcule automatiquement
- d) il lève une erreur immédiatement

---

# NIVEAU 2 — Comprendre (20 points)

*Vrai ou faux ? **Justifie chaque réponse en une phrase.** 2 points chacune
(1 pt la réponse, 1 pt la justification).*

**2.1** Écrire seulement `__str__` suffit pour que l'objet s'affiche
correctement partout, y compris dans une liste.

**2.2** Pour que `sorted()` fonctionne sur mes objets, je dois écrire au
minimum `__lt__` **et** `__gt__`.

**2.3** Un générateur consomme beaucoup moins de mémoire qu'une liste
contenant les mêmes valeurs.

**2.4** Le code d'un décorateur (hors de l'enveloppe) s'exécute au moment où
l'on **appelle** la fonction décorée.

**2.5** Un `__exit__` qui renvoie `True` fait disparaître silencieusement les
exceptions du bloc `with`.

**2.6** `itertools.groupby` regroupe tous les éléments ayant la même clé, où
qu'ils se trouvent dans la séquence.

**2.7** On peut poser `@functools.cache` sur une fonction qui reçoit une
**liste** en argument.

**2.8** Dans un `match`, écrire `case autre:` compare la valeur testée au
contenu de la variable `autre`.

**2.9** Une fonction nommée `verifie_total()` placée dans un fichier
`test_budget.py` sera exécutée par `pytest`.

**2.10** On peut compter sur `assert` pour valider les données d'un
utilisateur en production.

---

# NIVEAU 3 — Prédire l'output (30 points)

*Écris **exactement** ce que le programme affiche. Si une erreur est levée,
donne **son nom** (ex. `TypeError`). 3 points chacune.*

**3.1**
```python
class Article:
    def __init__(self, nom): self.nom = nom
    def __str__(self): return f"Article {self.nom}"

a = Article("stylo")
print(a)
print([a])
```

**3.2**
```python
def compter():
    yield 1
    yield 2
    yield 3

g = compter()
print(sum(g))
print(sum(g))
```

**3.3**
```python
class Point:
    def __init__(self, x): self.x = x
    def __eq__(self, o): return isinstance(o, Point) and self.x == o.x

print(Point(1) == Point(1))
print(len({Point(1), Point(1)}))
```

**3.4**
```python
def trace(f):
    def env(*a, **k):
        f(*a, **k)
    return env

@trace
def somme(a, b):
    return a + b

print(somme(2, 3))
```

**3.5**
```python
def deco(f):
    def env(*a, **k):
        return f(*a, **k)
    return env

@deco
def calculer():
    """Calcule."""

print(calculer.__name__, "/", calculer.__doc__)
```

**3.6**
```python
from itertools import groupby

mots = ["chat", "chien", "cheval", "ane", "chevre"]
print([(k, len(list(g))) for k, g in groupby(mots, key=lambda m: m[0])])
```

**3.7**
```python
class Session:
    def __enter__(self):
        print("entree")
    def __exit__(self, *a):
        print("sortie")
        return False

with Session() as s:
    print(s)
```

**3.8**
```python
g = (x for x in [1, 2])
print(next(g))
print(next(g))
print(next(g))
```

**3.9**
```python
from itertools import count, islice
print(list(islice(count(10, 5), 4)))
```

**3.10**
```python
from functools import total_ordering

@total_ordering
class Poids:
    def __init__(self, kg): self.kg = kg
    def __eq__(self, o): return self.kg == o.kg
    def __lt__(self, o): return self.kg < o.kg
    def __hash__(self): return hash(self.kg)

print(Poids(5) >= Poids(3), Poids(2) <= Poids(2))
```

---

# NIVEAU 4 — Diagnostiquer (20 points)

*Chaque code ci-dessous **ne fait pas ce qu'on attend**. Pour chacun :*
*(a) décris le symptôme, (b) explique la CAUSE, (c) donne la correction.*
*4 points chacune (1 + 2 + 1).*

**4.1** — On attend `5`, on obtient autre chose.
```python
def journalise(fonction):
    def enveloppe(*args, **kwargs):
        print(f"appel de {fonction.__name__}")
        fonction(*args, **kwargs)
    return enveloppe

@journalise
def additionner(a, b):
    return a + b

resultat = additionner(2, 3)
print(resultat)
```

**4.2** — On veut supprimer les doublons du carnet. Le programme plante.
```python
class Depense:
    def __init__(self, titre, montant):
        self.titre = titre
        self.montant = montant
    def __eq__(self, autre):
        return (self.titre, self.montant) == (autre.titre, autre.montant)

carnet = [Depense("Loyer", 850), Depense("Loyer", 850), Depense("Cafe", 2.5)]
uniques = set(carnet)
```

**4.3** — On attend `2` grosses dépenses et un total de `970`. On obtient `0`.
```python
def grosses(depenses):
    for d in depenses:
        if d["montant"] >= 100:
            yield d

carnet = [{"montant": 850}, {"montant": 2.5}, {"montant": 120}]
flux = grosses(carnet)

print("nombre :", sum(1 for _ in flux))
print("total  :", sum(d["montant"] for d in flux))
```

**4.4** — On attend **2** groupes (Logement, Alimentation). On en obtient 3.
```python
from itertools import groupby

depenses = [
    {"cat": "Logement", "titre": "Loyer"},
    {"cat": "Alimentation", "titre": "Courses"},
    {"cat": "Logement", "titre": "Charges"},
]
for cat, groupe in groupby(depenses, key=lambda d: d["cat"]):
    print(cat, len(list(groupe)))
```

**4.5** — On attend l'ajout d'une dépense. On obtient une `AttributeError`.
```python
class Budget:
    def __init__(self):
        self._depenses = []
    def ajouter(self, d):
        self._depenses.append(d)
    def __enter__(self):
        print("ouverture du carnet")
    def __exit__(self, *args):
        print("carnet sauvegarde")
        return False

with Budget() as budget:
    budget.ajouter("Loyer")
```

---

# NIVEAU 5 — Expliquer (20 points)

*Questions ouvertes. On attend un **raisonnement**, pas du code.*
*Réponds en 5 à 10 lignes. 5 points chacune.*

**5.1** — Python met `__hash__` à `None` dès qu'on écrit `__eq__`. Cela peut
sembler brutal, voire pénible.
**Explique pourquoi c'est en réalité une protection**, et décris le bug —
bien pire — que ce comportement t'évite. Donne un exemple concret avec un
dictionnaire.

**5.2** — On te confie un fichier de relevé bancaire de **4 Go**. Tu dois en
extraire les 20 lignes dont le montant dépasse 1 000 EUR.
**Explique ta stratégie** et **pourquoi** l'approche naïve
(`lignes = fichier.readlines()`) échouerait. Quel outil du jour utilises-tu ?

**5.3** — Un collègue te dit : « les décorateurs, c'est de la magie, je
préfère copier-coller mon code de chronométrage dans mes 40 fonctions ».
**Réponds-lui** en montrant (a) que `@` n'est que du sucre syntaxique, et
(b) ce qui va lui arriver dans deux semaines quand le besoin changera.

**5.4** — « Les tests servent à trouver des bugs. »
Cette phrase est **incomplète**. **Quelle est la vraie raison** d'écrire des
tests ? Illustre avec ce qui s'est passé sur MonBudget entre la séance 5 et
la séance 6.

---

## Barème récapitulatif

| Niveau | Ce qu'il évalue | Points |
|---|---|---|
| 1 — Reconnaître | le vocabulaire et les réflexes | 10 |
| 2 — Comprendre | le mécanisme derrière la syntaxe | 20 |
| 3 — Prédire | la capacité à **simuler Python dans sa tête** | 30 |
| 4 — Diagnostiquer | relier un symptôme à sa cause | 20 |
| 5 — Expliquer | la compréhension profonde et l'utilité | 20 |
| | **Total** | **100** |

---

*Rappel : une erreur que tu comprends et que tu expliques vaut mieux qu'une
bonne réponse devinée. Bon courage.*

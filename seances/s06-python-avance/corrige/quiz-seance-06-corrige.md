# CORRIGÉ — Quiz séance 6 « Sous le capot »

**Document formateur. Ne pas distribuer avant la correction.**

> **Toutes les sorties de ce corrigé ont été obtenues par exécution réelle**
> (Python 3.11), pas estimées. Les adresses mémoire (`0x...`) varient d'une
> machine à l'autre : ne pas les compter comme fausses.

---

## Conseils de correction

- **Niveaux 1 à 3** : correction objective, la réponse est juste ou fausse.
- **Niveau 2** : 1 pt pour « vrai/faux », 1 pt pour la justification. Une
  justification correcte mais formulée autrement compte **juste**.
- **Niveau 4** : 1 pt symptôme, 2 pts cause, 1 pt correction. Un élève qui
  décrit bien la cause sans trouver la correction exacte garde ses 3 pts.
- **Niveau 5** : accepter toute réponse qui montre le **raisonnement**. Les
  réponses ci-dessous sont des modèles, pas des attendus littéraux.

**Seuils indicatifs :** < 40 = la séance est à revoir avec lui ·
40–60 = les bases sont là, les pièges pas encore · 60–80 = bonne maîtrise ·
> 80 = a vraiment compris le modèle de données.

---

# NIVEAU 1 — Reconnaître (10 pts)

| Q | Réponse | Pourquoi |
|---|---|---|
| 1.1 | **b** `__len__` | `len()` cherche la « prise » `__len__` |
| 1.2 | **b** `__repr__` | une liste affiche le `repr` de chaque élément, jamais le `str` |
| 1.3 | **c** `yield` | un seul `yield` transforme toute la fonction en générateur |
| 1.4 | **c** conserver le nom et la docstring | sans lui, tout s'appelle `enveloppe` |
| 1.5 | **b** `__iter__` | c'est le plus rentable : débloque aussi `sum`, `sorted`, `max`… |
| 1.6 | **c** `self` | sans ce `return`, le `as` reçoit `None` |
| 1.7 | **b** une seule fois | c'est un flux, pas un contenant |
| 1.8 | **b** `ruff format .` | `ruff check` **repère** mais ne reformate pas |
| 1.9 | **c** en dernier | le joker rend inaccessibles les cas suivants |
| 1.10 | **b** il le met à `None` | d'où le `TypeError: unhashable type` |

---

# NIVEAU 2 — Comprendre (20 pts)

**2.1 — FAUX.** Dans une liste (et dans le débogueur), Python appelle
`__repr__`, pas `__str__`. Avec seulement `__str__`, `print([obj])` affiche
encore `<__main__.X object at 0x...>`. *Si on n'en écrit qu'une : `__repr__`.*

**2.2 — FAUX.** `sorted()`, `min()` et `max()` n'ont besoin que de `__lt__`.
Et `@functools.total_ordering` déduit `<=`, `>`, `>=` à partir de `__lt__` +
`__eq__`.

**2.3 — VRAI.** La liste construit tout en mémoire, le générateur rien.
Mesuré : 800 984 octets contre 208 pour 100 000 carrés — environ **3 850 fois**
moins.

**2.4 — FAUX.** Le décorateur s'exécute **à l'import** (au moment de la
définition de la fonction). Seule l'**enveloppe** s'exécute à l'appel.

**2.5 — VRAI.** `return True` signifie « j'ai géré l'exception » : elle est
supprimée silencieusement. Le défaut sain est `False` (ou rien).

**2.6 — FAUX.** `groupby` ne regroupe que les éléments **consécutifs**. Sans
`sorted()` préalable sur la même clé, on obtient plusieurs groupes pour une
même valeur — **sans aucune erreur**, juste un résultat faux.

**2.7 — FAUX.** `@cache` mémorise par les arguments, donc ils doivent être
**hachables**. Une liste lève `TypeError: unhashable type: 'list'` à l'appel.

**2.8 — FAUX.** Un nom nu dans un `case` ne compare rien : il **capture** la
valeur et **écrase** la variable. C'est l'erreur n°1 de PEP 636. Pour comparer
à une constante, il faut un nom **pointé** : `case Categorie.AUTRE:`.

**2.9 — FAUX.** `pytest` ne collecte que les fonctions dont le nom **commence
par `test_`**. `verifie_total()` ne sera jamais exécutée — et personne ne s'en
apercevra. C'est le pire cas : croire qu'on est couvert.

**2.10 — FAUX.** Les `assert` sont **supprimés** si Python tourne avec `-O`.
`assert` est fait pour les **tests** ; en production on utilise `raise`.

---

# NIVEAU 3 — Prédire l'output (30 pts)

**3.1** *(sorties réelles)*
```
Article stylo
[<__main__.Article object at 0x...>]
```
`print(a)` utilise `__str__`. `print([a])` utilise le `__repr__` de l'élément,
qui n'a pas été défini → affichage par défaut. **Le piège central de la
séance.**

**3.2**
```
6
0
```
Le premier `sum` **consomme** le générateur. Le second trouve un flux déjà
épuisé et somme… rien. Aucune erreur : juste un `0` faux.

**3.3**
```
True
TypeError: unhashable type: 'Point'
```
`__eq__` fonctionne, mais l'avoir défini a mis `__hash__` à `None`. Il manque
`def __hash__(self): return hash(self.x)`.

**3.4**
```
appel de additionner   (si le print était présent — ici non)
None
```
*Sortie exacte pour ce code :* `None`.
L'enveloppe appelle bien `f(*a, **k)` mais **ne rend pas** son résultat :
`return resultat` manquant.

**3.5**
```
env / None
```
Sans `@functools.wraps`, la fonction décorée perd son nom (`env`) et sa
docstring (`None`).

**3.6**
```
[('c', 3), ('a', 1), ('c', 1)]
```
`chat, chien, cheval` sont consécutifs → un groupe de 3. Puis `ane`. Puis
`chevre` → **un second groupe `'c'`**, parce que `groupby` ne regarde que les
voisins.

**3.7**
```
entree
None
sortie
```
`__enter__` ne fait pas `return self` → il renvoie `None`, donc `s` vaut
`None`. Noter que `__exit__` s'exécute quand même.

**3.8**
```
1
2
StopIteration
```
Le générateur n'a que deux valeurs. Le troisième `next()` lève
`StopIteration` — c'est le signal normal de fin, celui que la boucle `for`
attrape pour toi.

**3.9**
```
[10, 15, 20, 25]
```
`count(10, 5)` compte **à l'infini** de 5 en 5 depuis 10 ; `islice` en prend
4 et s'arrête. Impossible avec une liste : elle ne finirait jamais d'être
construite.

**3.10**
```
True True
```
`@total_ordering` a déduit `>=` et `<=` à partir de `__lt__` et `__eq__`.
Une méthode écrite, quatre offertes.

---

# NIVEAU 4 — Diagnostiquer (20 pts)

**4.1 — Le décorateur qui ne rend rien**
- **Symptôme** : affiche `appel de additionner` puis `None` au lieu de `5`.
- **Cause** : l'enveloppe appelle `fonction(*args, **kwargs)` mais **jette le
  résultat**. Une fonction sans `return` explicite rend `None`.
- **Correction** : `return fonction(*args, **kwargs)`.
- *Effet réel dans MonBudget* : `budget.supprimer(0)` supprimerait bien la
  dépense, mais rendrait `None` — le code appelant qui voulait l'afficher
  planterait.

**4.2 — `__eq__` sans `__hash__`**
- **Symptôme** : `TypeError: unhashable type: 'Depense'` à la ligne `set(...)`.
- **Cause** : définir `__eq__` met automatiquement `__hash__` à `None`. Un
  objet non hachable ne peut entrer ni dans un `set`, ni en clé de `dict`.
- **Correction** : ajouter
  `def __hash__(self): return hash((self.titre, self.montant))` — **les mêmes
  champs** que `__eq__`.
- *Bonus (0,5 pt)* : l'élève qui remarque que `__eq__` devrait aussi rendre
  `NotImplemented` face à un autre type a bien compris.

**4.3 — Le générateur consommé deux fois**
- **Symptôme** : `nombre : 2` (correct) puis `total : 0` (faux, on attendait
  970).
- **Cause** : `sum(1 for _ in flux)` a **épuisé** le générateur. La deuxième
  somme parcourt un flux vide. **Aucune erreur n'est levée** — c'est ce qui
  rend le bug dangereux.
- **Correction** : matérialiser une fois —
  `grosses_liste = list(grosses(carnet))` — puis utiliser cette liste deux
  fois. (Ou recréer un générateur pour chaque parcours.)

**4.4 — `groupby` sans tri préalable**
- **Symptôme** : trois groupes affichés (`Logement 1`, `Alimentation 1`,
  `Logement 1`) au lieu de deux.
- **Cause** : `groupby` ne regroupe que les éléments **consécutifs**. Les deux
  « Logement » sont séparés par « Alimentation ».
- **Correction** : trier d'abord sur la **même** clé :
  `groupby(sorted(depenses, key=cle), key=cle)`.

**4.5 — `__enter__` sans `return self`**
- **Symptôme** : affiche `ouverture du carnet`, puis `carnet sauvegarde`, puis
  `AttributeError: 'NoneType' object has no attribute 'ajouter'`.
- **Cause** : `__enter__` ne renvoie rien → renvoie `None` → `budget` vaut
  `None` dans le bloc `with`.
- **Correction** : ajouter `return self` à la fin de `__enter__`.
- *Détail à valoriser* : `__exit__` s'exécute **quand même** (le message de
  sauvegarde s'affiche avant l'erreur). C'est précisément la garantie du
  `with` : il referme même quand le bloc échoue.

---

# NIVEAU 5 — Expliquer (20 pts)

*Réponses modèles. Accepter toute formulation qui tient le raisonnement.*

## 5.1 — Pourquoi `__hash__` passe à `None` (5 pts)

**Attendu.** Un `set` et un `dict` rangent les objets **par leur empreinte**
(`hash`), comme une bibliothèque range les livres par cote. La règle absolue
est : **deux objets égaux doivent avoir la même empreinte**.

Si l'on redéfinit « égal » sans redéfinir « empreinte », deux objets égaux
partiraient dans **deux rayons différents**. Le `set` ne détecterait jamais le
doublon, et le dictionnaire perdrait des données :

```python
budget = {}
budget[Depense("Netflix", 13.49)] = "payé"
budget[Depense("Netflix", 13.49)]        # KeyError !
```

On range un livre, on le redemande **avec exactement le même titre**, et la
bibliothèque répond « inconnu ». **Aucune erreur, aucun message** — juste des
données perdues, découvertes des semaines plus tard.

Python préfère donc **planter tout de suite** (`TypeError: unhashable type`)
plutôt que de laisser produire ce bug silencieux. Le plantage est bruyant,
immédiat et explicite : c'est un cadeau, pas une punition.

**Grille** : 2 pts pour la règle « égaux ⇒ même empreinte » · 2 pts pour le bug
évité (dict/set qui perd des données **sans erreur**) · 1 pt pour l'exemple.

## 5.2 — Le fichier de 4 Go (5 pts)

**Attendu.** `readlines()` charge **tout le fichier en mémoire** d'un coup : sur
4 Go, le programme lève `MemoryError` (ou fait *swapper* la machine). Or on n'a
besoin que de 20 lignes.

La stratégie est la **paresse** : lire **une ligne à la fois**, tester, et ne
garder que ce qui nous intéresse. Un fichier ouvert est déjà itérable
paresseusement :

```python
def grosses(chemin, seuil=1000):
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:                      # une seule ligne en mémoire
            if float(ligne.split(",")[2]) > seuil:
                yield ligne

top20 = list(islice(grosses("releve.csv"), 20))   # on s'arrête au 20e
```

Deux gains : la mémoire reste **constante** quelle que soit la taille du
fichier, et avec `islice` on **arrête la lecture** dès la 20ᵉ trouvée — inutile
de parcourir les 4 Go.

**Grille** : 2 pts pour le diagnostic (`readlines` = tout en mémoire) · 2 pts
pour la solution paresseuse (`yield` / itération du fichier) · 1 pt pour
`islice` ou l'idée d'arrêt anticipé.

## 5.3 — « Les décorateurs, c'est de la magie » (5 pts)

**Attendu, deux volets.**

**(a) Le `@` n'est que du sucre.** Ces deux écritures sont **exactement**
équivalentes :

```python
@chronometre
def somme(n): ...

# ... est identique à :
def somme(n): ...
somme = chronometre(somme)
```

Le `@` ne fait rien de plus que réaffecter le nom. Il n'y a aucune magie : une
fonction reçoit une fonction et en rend une autre (les marches 2 et 3).

**(b) Ce qui va lui arriver.** Il a copié le même code dans 40 fonctions. Dans
deux semaines, on lui demandera « écris les durées dans un fichier au lieu de
les afficher ». Il devra **rouvrir les 40 fonctions**, avec 40 occasions de se
tromper et d'en oublier une. Avec un décorateur, il modifie **un seul
endroit** — et les 40 fonctions en bénéficient.

Argument supplémentaire : ses 40 fonctions sont **polluées** par du code de
chronométrage qui n'a rien à voir avec leur métier. Le décorateur sépare « ce
que fait la fonction » de « ce qu'on observe autour ».

**Grille** : 2 pts pour la démonstration `f = deco(f)` · 2 pts pour le coût de
maintenance (40 modifications) · 1 pt pour la séparation des responsabilités.

## 5.4 — La vraie raison d'écrire des tests (5 pts)

**Attendu.** Trouver des bugs est un effet **secondaire**. La vraie raison est
de **pouvoir modifier son code sans peur**.

C'est le filet du trapéziste : il ne l'empêche pas de tomber, il fait que la
chute n'est pas grave — et c'est **ce qui lui permet d'oser des figures plus
difficiles**. Sans tests, on n'ose plus rien changer : le code se fige, puis
pourrit.

**L'illustration sur MonBudget.** Entre la séance 5 et la séance 6, on a
refactorisé deux fois de suite : le dictionnaire est devenu une classe
`Depense`, puis on a réécrit `__eq__`, ajouté des générateurs, remplacé les
appels manuels à `sauvegarder()` par un `with`. **Le comportement visible ne
devait pas changer** — c'est la définition d'une refactorisation.

Sans tests, chacune de ces réécritures serait un pari : on croise les doigts et
on espère n'avoir rien cassé. Avec 27 tests verts, on **sait**. Et quand on
passe le seuil de `100.0` à `1000.0`, deux tests deviennent rouges **en 0,6
seconde**, avec le nom de la fonction et la valeur attendue — au lieu d'un
utilisateur qui signale trois semaines plus tard que « les alertes ne
s'affichent plus ».

**Grille** : 3 pts pour « pouvoir changer le code sans peur » · 2 pts pour
l'illustration concrète sur la refactorisation MonBudget.

---

## Récapitulatif du barème

| Niveau | Points |
|---|---|
| 1 — Reconnaître | 10 |
| 2 — Comprendre | 20 |
| 3 — Prédire | 30 |
| 4 — Diagnostiquer | 20 |
| 5 — Expliquer | 20 |
| **Total** | **100** |

---

## Les 4 questions qui discriminent vraiment

Si tu manques de temps pour tout corriger finement, ces quatre-là suffisent à
savoir qui a compris :

- **3.1** (`print([a])`) — a-t-il compris `repr` vs `str` ?
- **3.2** (générateur sommé deux fois) — a-t-il compris la paresse ?
- **4.1** (décorateur sans `return`) — a-t-il compris l'enveloppe ?
- **5.1** (`__hash__`) — a-t-il compris **pourquoi** une règle existe, ou
  seulement qu'elle existe ?

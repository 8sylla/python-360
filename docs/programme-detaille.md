# Formation Python 360° — Programme détaillé

**8 séances de 3 h + un kit de démarrage asynchrone · 100 % en ligne (Google Meet)**
Fil rouge unique : `OpportuniTrack`, un suivi d'opportunités construit de la séance 1 à la séance 8.
Cible Python : **3.14.x** · plancher absolu 3.10 (pour `match/case`).

---

## Les titres officiels

Le **titre court** est celui qui figure sur les slides et qui doit servir de nom de thème dans
Google Classroom. Le **sous-titre** dit ce que la séance couvre ; il va en description.

| N° | Titre court (officiel) | Sous-titre | Phrase de couverture |
|---|---|---|---|
| 0 | **Kit de démarrage** | Ce qu'il faut avoir fait avant la première séance | *Avant de commencer.* |
| 1 | **Parler à la machine** | Découverte, algorithmique, variables, types, entrées/sorties | *Parler à la machine.* |
| 2 | **Décider et répéter** | Booléens, conditions, boucles, lecture d'erreurs | *Décider, et répéter.* |
| 3 | **Ranger l'information** | Listes, dictionnaires, tuples, ensembles, parcours | *Ranger l'information.* |
| 4 | **Fabriquer ses outils** | Fonctions, modules, fichiers, erreurs — et passage à VS Code | *Fabriquer ses outils.* |
| 5 | **Programmation orientée objet** | Classes, objets, dataclasses, composition | *Structurer avec les objets.* |
| 6 | **Sous le capot** | Dunder methods, générateurs, décorateurs, outillage qualité | *Sous le capot.* |
| 7 | **NumPy & pandas** | Du tableau en mémoire au DataFrame | *Les données.* |
| 8 | **Faire parler les données** | Agrégation, jointures, Matplotlib, seaborn | *Faire parler les données.* |

### Variantes présentes dans les guides du formateur

Les guides emploient des titres plus longs pour cinq séances. Ce sont les mêmes contenus ;
seuls les titres du tableau ci-dessus font foi côté apprenants.

| N° | Variante dans le guide formateur |
|---|---|
| 5 | La Programmation Orientée Objet |
| 6 | Sous le capot : Python avancé et fonctionnel |
| 7 | Les données : NumPy et pandas |

---

## La structure en deux arcs

**Arc 1 — La rampe de lancement (S0 → S4).** On apprend des instructions. Environnement :
Google Colab, rien à installer. Se termine par une application complète en ligne de commande.

**Arc 2 — Structurer, puis analyser (S5 → S8).** On apprend à organiser du code, puis à faire
parler des données. Environnement : VS Code + GitHub. Se termine par un tableau de bord tiré
de vraies données, et la clôture de la formation.

> **Trois séances écrites, mais hors programme.** *Aller chercher la donnée* (HTTP, APIs,
> scraping), *API REST avec FastAPI* et *Qualité, tests, production* existent en entier —
> guides minutés, slides et corrigés — dans `_archive-seances-9-11/`. Elles peuvent servir de
> suite, d'atelier ponctuel, ou d'auto-formation guidée.

Le basculement Colab → VS Code a lieu **en séance 4**, pas avant.

---
---

# SÉANCE 0 — Kit de démarrage

**Format :** asynchrone, ~45 min, à faire avant J1.
**Sous-titre :** *Ce qu'il faut avoir fait avant la première séance.*

**Raison d'être :** la séance 1 doit être une séance de code, pas une séance de dépannage.

## Ce que ça couvre

- Ouvrir Google Colab, créer un notebook, **Fichier ▸ Enregistrer une copie dans Drive** (le
  piège du notebook en lecture seule), exécuter une cellule avec `Maj + Entrée`.
- La première ligne de Python de la formation : `print("Bonjour")`.
- Le comportement de Colab : déconnexion après 90 min d'inactivité, code conservé mais
  variables perdues.
- Rejoindre le cours Google Classroom ; règle du support : **coller l'erreur en texte, jamais
  en capture d'écran**.
- Le matériel : un ordinateur (pas une tablette), un casque avec micro, une connexion qui tient
  trois heures.
- Le questionnaire de positionnement (5 questions) — il sert à composer les binômes.
- *Optionnel, requis seulement pour la S4 :* installer Python 3.14.x depuis `python.org`
  (**Windows : cocher « Add python.exe to PATH »**), VS Code + extensions Python et Jupyter,
  créer un compte GitHub.

**Aucun concept Python à proprement parler** en dehors de `print()`. C'est une séance de mise
en condition.

---
---

# SÉANCE 1 — Parler à la machine
### *Découverte, algorithmique, variables, types, entrées/sorties*

> **Promesse :** « Dans 3 heures, tu auras écrit un programme qui te pose des questions et te répond. »

## Ce que ça couvre en Python

**Le modèle mental**
- Ce qu'est un programme, ce qu'est un interpréteur, ce qu'est un algorithme.
- Lecture **ligne par ligne, de haut en bas** : la machine n'anticipe pas et ne devine pas.
- Atelier débranché sur papier : « écris la recette pour qu'un robot prépare un thé » —
  l'ambiguïté, l'ordre, l'implicite.

**L'environnement**
- Colab : cellule de code vs cellule de texte, ordre d'exécution, enregistrement.

**Les instructions**
- `print()` : arguments multiples, texte multiligne.
- **Variables** : affectation, réaffectation, écrasement du contenu, nommage lisible.
  Le `=` n'est pas un égal mathématique — `x = x + 1` est légitime.
- **Les 4 types de base** : `str`, `int`, `float`, `bool`. La fonction `type()`.
- **Opérateurs arithmétiques** : `+`, `-`, `*`, `/`, `//` (division entière), `%` (modulo),
  `**` (puissance). `/` rend toujours un `float`.
- Le piège des types : `"5" + "3"` → `"53"` mais `5 + 3` → `8`, et `"5" + 3` → `TypeError`.
- Répétition de chaîne : `"=" * 40` pour tracer une ligne de séparation.

**Le dialogue**
- `input()` — **rend toujours du texte**, même si l'utilisateur tape 42. C'est le piège n° 1
  de tout débutant.
- Conversions : `int()`, `float()`, `str()`.
- **f-strings** : `f"Bonjour {prenom}, tu as {age} ans"`, et le format `:.1f` pour arrondir
  l'affichage.
- Premières méthodes de chaîne : `.strip()`, `.upper()`.

**Les erreurs**
- Reconnaître `SyntaxError`, `NameError`, `TypeError`.
- **Lire un traceback** : dernière ligne = ce qui ne va pas, ligne du milieu = où, et depuis
  Python 3.11 le `^~~~` pointe le morceau fautif.
- Une dette assumée : `ZeroDivisionError` si l'utilisateur saisit 0 — non corrigée aujourd'hui,
  elle sert d'accroche à la séance 2.

**Bonus (profils techniques)**
- `datetime.date`, soustraction de deux dates, `.days`.
- `prenom.strip().upper()` en chaînage.

## Exercice principal
**« Le calculateur de candidature »** — un programme qui demande un prénom, un nombre d'offres
et un nombre de candidatures, puis affiche un récapitulatif avec le reste à traiter et un taux
en pourcentage.

## Fil rouge — `OpportuniTrack` v0.1
« La carte d'opportunité » : saisie de titre / organisme / pays / deadline, et affichage d'une
fiche formatée.

---
---

# SÉANCE 2 — Décider et répéter
### *Booléens, conditions, boucles, lecture d'erreurs*

> **Promesse :** « Ton programme arrête d'exécuter bêtement : il choisit, et il répète. »

## Ce que ça couvre en Python

**Les booléens**
- `True` / `False` : une condition ne dit pas « oui », elle **vaut** `True`.
- Comparateurs : `==`, `!=`, `<`, `>`, `<=`, `>=`.
- **`=` contre `==`** — la deuxième erreur la plus fréquente de la formation, annoncée
  explicitement.
- Opérateurs logiques `and`, `or`, `not`, tables de vérité, combiner plutôt qu'imbriquer.

**Les conditions**
- `if` / `elif` / `else` : une seule branche est empruntée, jamais deux.
- Les deux-points, et **l'indentation de 4 espaces** comme élément de syntaxe, pas de
  décoration. `IndentationError`.
- Traduire une règle métier écrite en français en une condition Python — le vrai apprentissage
  de la séance.

**Les boucles**
- `for` : « je sais combien de fois ». Parcours d'une liste, parcours d'une chaîne.
- `range()` : commence à 0, **s'arrête avant** la borne.
- `while` : « je répète tant que ». La question à se poser systématiquement — *qu'est-ce qui,
  dans cette boucle, rendra la condition fausse ?*
- **La boucle infinie** : provoquée en direct par le formateur, et le bouton stop de Colab.
- **Compteur et accumulateur** — deux motifs réutilisés jusqu'à la fin de la formation.
  L'écriture `essais += 1`.
- `break` (sortir de la file) et `continue` (passer son tour).
- Le **drapeau booléen** (`trouve = False` … `while not trouve:`).

**Modules et saisie**
- Premier `import` : `random.randint(a, b)` — bornes **incluses**, contrairement à `range`.
- Normaliser une saisie : `.strip().lower()`.

**Bonus**
- Limiter le nombre d'essais, refuser une saisie hors bornes sans consommer d'essai.
- **Inverser les rôles** : l'ordinateur devine par dichotomie — une introduction intuitive à la
  complexité logarithmique (7 coups suffisent toujours sur 1–100).
- Annonce de `try/except` (traité en S4).

## Exercice principal
**« Le nombre mystère »** — l'ordinateur tire un nombre entre 1 et 100, le joueur propose, le
programme répond « trop grand » / « trop petit » et compte les essais.

## Fil rouge — `OpportuniTrack` v0.2
« Le filtre d'éligibilité » : une cascade `if/elif/else` qui décide s'il faut candidater selon
le niveau requis et le nombre de jours restants.

---
---

# SÉANCE 3 — Ranger l'information
### *Listes, dictionnaires, tuples, ensembles, parcours*

> **Promesse :** « Jusqu'ici tu manipulais une info à la fois. Aujourd'hui, tu en gères des centaines. »

## Ce que ça couvre en Python

**La liste**
- Création, ordre, doublons autorisés, modification.
- **Index à partir de 0** ; index négatif : `liste[-1]` est le dernier.
- **Tranches (slicing)** : `liste[1:4]` — borne de gauche incluse, borne de droite exclue.
- Méthodes : `append`, `insert`, `remove`, `pop`, `sort`, plus `len()` et l'opérateur `in`.
- `IndexError: list index out of range`.

**Le dictionnaire**
- Paires **clé : valeur** — on accède par nom, pas par position. Les clés sont uniques.
- `dico["cle"]` (lève `KeyError`) vs **`dico.get("cle")`** (rend `None` ou un défaut) — le
  réflexe professionnel sur des données réelles, toujours incomplètes.
- Ajout, modification, parcours avec `.keys()`, `.values()`, `.items()`.

**Les deux autres structures**
- **Tuple** : une liste plastifiée, non modifiable. Pour ce qui ne doit pas bouger.
- **Ensemble (`set`)** : pas d'ordre, pas de doublon. Le geste utile : `list(set(ma_liste))`.
- **L'arbre de décision** — quelle structure pour quel besoin (slide à imprimer).

**La structure reine : la liste de dictionnaires**
- Le schéma mental du tableau : lignes = dictionnaires, colonnes = clés.
- Annoncé explicitement comme *un DataFrame pandas avant l'heure* — ce qui désamorce l'angoisse
  de la séance 7.

**Trier, filtrer, formater**
- `sorted()` — rend une **nouvelle** liste, ne touche pas à l'originale.
- `key=lambda opp: opp["jours"]` — la mini-fonction jetable qui répond à « comparer sur quoi ? ».
- `min()` / `max()` avec `key=`.
- `enumerate(collection, start=1)` — position et élément en même temps.
- `", ".join(...)` pour recoller une collection de textes.
- Alignement dans les f-strings : `:<25` (gauche), `:>3` (droite) — des colonnes propres sans effort.
- Guillemets simples à l'intérieur d'une f-string ouverte par des doubles.

**Compréhension de liste** (introduction douce)
- Le même filtre écrit en 4 lignes, puis en 1 : `[opp for opp in opportunites if opp["jours"] < 10]`.
- Et **quand ne pas l'utiliser**.

**PEP 8, en 5 règles**
- `snake_case`, 4 espaces, espaces autour des `=`, noms explicites, une instruction par ligne.

**Bonus**
- Compter par catégorie (dictionnaire d'accumulation ou `collections.Counter`).
- Regrouper par clé — un `groupby` fait main, rappelé en S8.
- Tri à deux niveaux : `key=lambda o: (o["pays"], o["jours"])`.

## Exercice principal
**« Le carnet d'opportunités »** — sur une liste de 5 dictionnaires : compter, filtrer les
urgentes, lister les pays sans doublon, trouver la plus urgente, produire le classement complet.

## Fil rouge — `OpportuniTrack` v0.3
Le carnet vit en mémoire : on ajoute, on affiche trié. **Le programme oublie tout à la
fermeture** — le manque qui motive la séance 4.

---
---

# SÉANCE 4 — Fabriquer ses outils
### *Fonctions, modules, fichiers, erreurs — et passage à VS Code*

> **Promesse :** « À la fin de la séance, tu quittes le navigateur : tu as un vrai programme,
> dans un vrai fichier, qui garde tes données. »

**Séance charnière** : elle clôt l'Arc 1 et livre le premier artefact complet.

## Ce que ça couvre en Python

**Le changement d'atelier (20 premières minutes)**
- VS Code : ouvrir un **dossier**, créer `tracker.py`, sélectionner l'interpréteur, exécuter
  (F5 ou terminal intégré). Les 4 zones de l'écran.
- Le formateur ne passe à la suite que quand **tout le monde** a vu un « Bonjour » dans son terminal.
- En fin de séance : le point d'arrêt du débogueur, 5 minutes, effet garanti.

**Les fonctions**
- `def`, paramètres, valeurs par défaut, arguments nommés à l'appel.
- `return` — et **`return` contre `print`**, la confusion la plus coûteuse de la formation :
  *« `print` parle à l'humain, `return` parle au reste du programme. »* Une fonction qui `print`
  est un cul-de-sac ; une fonction qui `return` est une brique. Le `None` implicite.
- `return` nu pour sortir plus tôt.
- **Docstring** (triple guillemet) et `help(ma_fonction)`.
- **Portée** locale / globale : une variable créée dans une fonction disparaît avec elle.
- Les trois bénéfices : ne pas se répéter, nommer une intention, tester une brique isolée.

**Les modules**
- Un fichier `.py` **est** un module. `import outils`, `from outils import charger`, l'alias.
- **`if __name__ == "__main__":`** — « exécute ceci seulement si on lance CE fichier
  directement, pas si on l'importe ».
- Découper un projet en plusieurs fichiers.

**Les fichiers**
- La mémoire longue : sans fichier, tout disparaît à la fermeture.
- **`with open(...)`** — « ouvre, fais, et referme quoi qu'il arrive ».
- **`pathlib.Path`** : la façon moderne, identique sur Windows / macOS / Linux. `.exists()`,
  `.open()`.
- **`encoding="utf-8"` obligatoire** — sinon les accents cassent selon la machine.
- **Trois formats** : TXT (du texte), CSV (un tableau, s'ouvre dans Excel), JSON (des données
  imbriquées — c'est exactement une liste de dictionnaires. C'est aussi le format d'échange du
  web : tout ce qui sort d'une API en ligne a cette forme-là).
- `json.load()` / `json.dump(..., indent=2, ensure_ascii=False)`.
- `csv.DictReader` / `csv.DictWriter` (bonus).

**Les erreurs maîtrisées**
- `try / except ValueError` — la ceinture de sécurité.
- **Règle donnée immédiatement : jamais d'`except:` nu.** On nomme l'erreur qu'on attend,
  sinon on masque des bugs qu'on ne voulait pas masquer.
- Le motif « redemander tant que la saisie est invalide ».

**Python moderne, introduit ici**
- **`match / case`** (3.10+) sur son cas le plus lisible — un menu. Le `case _` comme « sinon ».
  `if/elif` reste correct, c'est dit.
- Les **annotations de type** (`-> list`, `: str`) présentes sans être détaillées :
  « une étiquette qui dit ce que la fonction attend et ce qu'elle rend ». Formalisées en S5.

**Architecture (première marche)**
- `main()` qui **orchestre sans contenir de logique métier**.
- Séparation stockage / programme, sur deux fichiers.
- Grille de revue de code en 3 points : les noms, la répétition, la responsabilité unique.

**Bonus**
- Supprimer une entrée avec confirmation ; export CSV ; remplacer un nombre de jours par une
  vraie date (`datetime.date.fromisoformat`) ; extraire un troisième module.

## Exercice principal / Fil rouge v1 — `OpportuniTrack` CLI
Une application en ligne de commande sur deux fichiers (`stockage.py` + `tracker.py`), avec
menu : ajouter, lister trié, filtrer par pays, quitter. **Les données survivent à la fermeture.**

---
---

# SÉANCE 5 — Programmation orientée objet
### *Classes, objets, dataclasses, composition*

> **Promesse :** « Ton programme de la séance 4 marche. Aujourd'hui, on le rend maintenable par
> quelqu'un d'autre que toi. »

**Début de l'Arc 2.**

## Ce que ça couvre en Python

**Le déclencheur, découvert et non décrété**
- On projette le `tracker.py` de la S4 : six fonctions qui reçoivent toutes la même liste.
  **Quand les mêmes données circulent entre toutes les fonctions, un objet veut exister.**

**Les classes**
- `class`, `__init__`, attributs, méthodes, instanciation.
- **`self` = « moi-même »** : pas un mot-clé magique, simplement le premier paramètre que Python
  remplit tout seul. `self.titre` se lit « mon titre ».
- La classe est le moule, l'objet est le gâteau.

**Les dataclasses — le défaut moderne**
- `@dataclass` : 15 lignes deviennent 6. `__init__`, `__repr__` et `__eq__` offerts.
- **`field(default_factory=list)` et jamais `default=[]`** — sinon la liste est *partagée par
  toutes les instances*. Le piège n° 1 des dataclasses, montré en direct.
- La règle : *si la classe est surtout des attributs → dataclass ; si elle est surtout du
  comportement → classe normale.*

**Enum**
- `class Statut(str, Enum)` : hériter de `str` en plus permet la sérialisation JSON directe.
- **Supprimer les chaînes magiques** : `"en cours"` mal orthographié casse silencieusement le
  filtrage ; `Statut.EN_COURS` lève une erreur immédiate et l'éditeur complète.

**Propriétés et méthodes de classe**
- `@property` : un attribut qui se **recalcule** à chaque lecture (`jours_restants`,
  `est_urgente`). Stocker un nombre de jours serait faux dès demain.
- `@classmethod` et `cls` : les **constructeurs alternatifs** (`Opportunite.depuis_dict(...)`).
- `dataclasses.asdict()`, le dépliage `cls(**donnees)`.
- `date.isoformat()` / `date.fromisoformat()` pour la persistance.

**Héritage et composition**
- Le test en une question : « un `StageEtudiant` **est une** `Opportunite` » → héritage ;
  « un `Carnet` **a des** `Opportunite` » → composition.
- Message assumé : **l'héritage est enseigné en premier et surutilisé en pratique.** Dans du
  code professionnel, la composition domine. On apprend l'héritage pour savoir le lire.

**Encapsulation, version honnête**
- Python n'a pas de `private`. `_attribut` est **un panneau, pas un mur**. Le dire évite une
  confusion durable à ceux qui viennent de Java.
- Rendre une **copie** de la liste interne pour que l'extérieur ne puisse pas la casser.

**Le typage moderne**
- `list[Opportunite]`, `str | None` — et surtout **pas** `typing.List` ni `Optional`, obsolètes.

**Autres gestes**
- `__len__` : la première dunder method de la formation (approfondie en S6).
- `casefold()` : la version robuste de `lower()` pour comparer des textes internationaux.
- **Refactoriser sans changer le comportement visible** — c'est la définition même du mot.

**Bonus**
- Une sous-classe `Bourse(Opportunite)` — et **débattre** : héritage justifié, ou simple champ
  optionnel de plus ?
- `__eq__` pour détecter les doublons ; `@dataclass(frozen=True)` et ses conséquences ;
  `__iter__` sur le `Carnet` — un pont direct vers la S6.

## Fil rouge v2 — `OpportuniTrack` orienté objet
Deux classes : `Opportunite` (dataclass + Enum + properties) et `Carnet` (collection +
persistance). Le `main()` se lit désormais **comme une phrase en français** — le seul argument
qui convainc vraiment un débutant que la POO sert à quelque chose.

---
---

# SÉANCE 6 — Sous le capot
### *Dunder methods, générateurs, décorateurs, et outillage qualité*

> **Promesse :** « Aujourd'hui, tu arrêtes d'utiliser Python et tu commences à le comprendre. »

**La séance la plus exigeante du cursus.** Objectif assumé pour les débutants : **savoir lire**
ce code, pas nécessairement l'écrire.

## Ce que ça couvre en Python

**Les méthodes spéciales (dunder methods)**
- La notion de **protocole** : Python ne demande pas « quelle est ta longueur ? », il cherche
  une prise nommée `__len__`. Analogie de la prise électrique murale.
- `__str__` (pour l'utilisateur) vs `__repr__` (pour le développeur, idéalement réexécutable).
  Règle pratique : *si tu n'en écris qu'une, écris `__repr__`*.
- `__eq__`, `__len__`, `__contains__`, `__iter__`, `__getitem__` — et l'écriture Python que
  chacune débloque.

**Itérateurs et générateurs**
- `yield` : rendre une valeur, **mettre en pause**, reprendre au tour suivant.
- Le distributeur de tickets : une liste imprime 10 millions de tickets d'avance, un générateur
  en imprime un quand on appuie.
- **La preuve chiffrée en direct** : `sys.getsizeof(range(10_000_000))` contre
  `sys.getsizeof(list(range(10_000_000)))`.
- Le piège : **un générateur ne se parcourt qu'une seule fois**.

**Les décorateurs — enseignés en 4 marches obligatoires**
1. Une fonction est une **valeur** : `f = dire_bonjour` (sans parenthèses), puis `f()`.
2. Une fonction peut **recevoir** une fonction.
3. Une fonction peut **fabriquer et rendre** une fonction — la marche difficile, à ne pas presser.
4. `@decorateur` au-dessus d'un `def` **est exactement** `ma_fonction = decorateur(ma_fonction)`.
- `*args, **kwargs` pour accepter n'importe quels arguments et les transmettre.
- **`functools.wraps`** : sans lui la fonction décorée perd son nom et sa docstring et s'appelle
  `wrapper`. Invisible — jusqu'au jour du débogage.
- `time.perf_counter()` pour mesurer.
- Les deux bugs à provoquer en direct : oublier `return resultat` (la fonction rend `None`),
  oublier `@wraps`.

**Les gestionnaires de contexte**
- Révélation du mécanisme derrière le `with open()` de la S4 : `__enter__` / `__exit__`.
- La version courte : `@contextlib.contextmanager` avec un `yield` au milieu.

**`match/case` structurel — bien au-delà du menu de la S4**
- Motifs de dictionnaire, motifs de séquence (`case [premier, *autres]`), **gardes** (`if j < 7`),
  capture typée (`int(j)`), reste (`**reste`).
- Vendu pour ce qu'il est : **du filtrage de forme**, pas un simple `switch`. Particulièrement
  utile pour traiter du JSON — utile dès qu'on traite des données venues d'ailleurs.

**`functools` et `itertools`**
- `@functools.cache` — démonstration spectaculaire sur un Fibonacci récursif.
- `functools.partial` — figer un argument, utile pour les `key=`.
- `itertools.groupby` (après tri !) et `itertools.batched` (3.12+) — ce dernier est utile dès
  qu'on traite un gros fichier par paquets.

**L'outillage qualité — présenté comme un filet, pas comme une contrainte**
- **Ruff** : `ruff format .` (le débat sur les espaces est clos, la machine tranche) et
  `ruff check .` (imports inutiles, variables mortes, style — en quelques millisecondes).
- **pytest** : `assert` = « j'affirme que », et c'est tout. Trois premiers tests écrits sur le
  fil rouge.
- **Le moment pédagogique de la séance** : casser volontairement `est_urgente`, relancer, et
  regarder le test devenir rouge.

**Bonus**
- `@reessayer(n=3, delai=1)` : un décorateur **paramétré** — trois niveaux d'imbrication.
  L'exercice qui sépare ceux qui ont compris de ceux qui ont copié. C'est le motif qui absorbe une erreur réseau passagère.
- `@journalise` avec le module `logging` plutôt que `print`.
- Réécrire une méthode en générateur et mesurer sur 100 000 entrées.
- `__enter__`/`__exit__` sur le `Carnet` : `with Carnet() as c:` charge à l'entrée et sauvegarde
  à la sortie.

## Exercice principal
**Le décorateur `@chronometre`** — affiche le temps d'exécution de la fonction décorée.

## Fil rouge v3
`__str__` et `__eq__` sur `Opportunite`, `__iter__` sur `Carnet`, un `@journalise` sur les
méthodes d'écriture, un dossier `tests/` avec 5 tests verts et `ruff` sans avertissement.

---
---

# SÉANCE 7 — NumPy & pandas
### *Du tableau en mémoire au DataFrame*

> **Promesse :** « Ta liste de dictionnaires plafonne à quelques centaines de lignes. Aujourd'hui,
> on en traite cent mille en une seconde. »

⚠️ **Versions de référence (août 2026) :** pandas **3.0.x**, NumPy 2.5.x, Matplotlib 3.10.x,
seaborn 0.13.x. Les tutoriels antérieurs à 2026 montrent du code qui **provoquera des erreurs**.
Un `requirements.txt` figé est distribué au groupe.

## Ce que ça couvre en Python

**Le pont depuis la S3**
- La liste de dictionnaires de la séance 3 est reprise et convertie en DataFrame :
  « vous connaissez déjà la structure, il ne reste que la syntaxe ».

**NumPy**
- **Pourquoi c'est rapide** : le sac de courses contre la boîte à œufs. Un `ndarray` est
  homogène, contigu en mémoire, de taille de case fixe — la boucle se déroule en C, pas en Python.
- **La vectorisation** : `valeurs * 2` au lieu d'écrire la boucle. Mesure comparative avec
  `%timeit` **produite devant le groupe**, pas annoncée.
- **Les masques booléens** : `masque = tableau > 50` puis `tableau[masque]`. Le concept qui
  débloque tout le reste — c'est exactement le `df[df["jours"] < 7]` de pandas.
- **Le broadcasting** : l'étirement automatique quand les formes diffèrent.

**pandas — les fondations**
- `Series` et `DataFrame` : index, colonnes, valeurs.
- `read_csv()` et **les 4 paramètres qui sauvent** : `sep`, `encoding`, `parse_dates`, `dtype`.
- **Le rituel des 5 commandes** devant tout jeu de données inconnu (slide à imprimer) :
  `df.shape`, `df.head()`, `df.info()`, `df.describe()`, `df["col"].value_counts()`.
  `value_counts()` est le détecteur de saleté : c'est là qu'on découvre que « Maroc », « maroc »
  et « MAROC » sont trois pays différents pour la machine.

**Sélectionner et filtrer**
- **`.loc` (étiquettes) contre `.iloc` (positions)** — la confusion n° 1. Mnémotechnique : le
  **i** de `iloc` comme **index numérique**.
- Masques booléens, `.query()`, tri.
- **`&` et non `and`, `|` et non `or`, avec parenthèses obligatoires** — l'erreur pandas la plus
  fréquente au monde.
- `.assign()` pour créer une colonne — se chaîne mieux que `df["x"] = ...`.

**⚠️ Le Copy-on-Write de pandas 3.0 — enseigné comme une règle unique et positive**

> *Une opération pandas ne modifie jamais la table d'origine : elle en rend une nouvelle. Si tu
> veux garder le résultat, réaffecte-le.*

- L'affectation chaînée (`df[df["x"] > 0]["y"] = ...`) lève désormais une **erreur**, plus un
  avertissement.
- **On n'enseigne jamais `SettingWithCopyWarning` ni `inplace=True`** : ils ont disparu. Un
  tutoriel qui en parle est daté — et c'est une leçon de méthode qui vaut au-delà de pandas.
- Les chaînes sont stockées via **Apache Arrow** : `df.info()` affiche `str` et non plus `object`.

**Nettoyer**
- Valeurs manquantes : `isna()`, `fillna()`, `dropna(subset=[...])` — **on ne supprime que ce
  qui rend la ligne inutilisable**.
- Doublons : `drop_duplicates(subset=[...], keep="first")`.
- Types : `astype()`, `pd.to_numeric(..., errors="coerce")`.
- Textes : l'accesseur **`.str`** — `.str.strip()`, `.str.title()`, `.str.replace(..., regex=True)`.
  C'est la vectorisation appliquée aux chaînes.
- Dates : `pd.to_datetime(..., format="mixed", dayfirst=True, errors="coerce")`, la valeur
  `NaT`, l'accesseur `.dt`, `pd.Timestamp.today().normalize()`, `.dt.days`.
- `to_csv(..., index=False, encoding="utf-8")`.

**Les trois points martelés à l'oral**
1. `&` / `|` et non `and` / `or`, avec parenthèses.
2. **On trace ce qu'on jette.** Un nettoyage silencieux est un nettoyage suspect : chaque
   suppression s'accompagne d'un comptage affiché.
3. `errors="coerce"` est un **choix**, pas un réflexe : il transforme les erreurs en valeurs
   manquantes. On l'assume et on regarde combien il en a produites.

**Bonus**
- Réécrire tout le pipeline en une seule chaîne avec `.pipe()` et des fonctions nommées — la
  forme professionnelle.
- Quasi-doublons par similarité (`difflib.SequenceMatcher`).
- `dtype_backend="pyarrow"` et `df.memory_usage(deep=True)`.

## Exercice principal / Fil rouge v4
**Le nettoyage** d'un jeu de ~300 opportunités volontairement sale : casse incohérente, trois
formats de date, doublons et quasi-doublons, montants du type `"1 500 €"` / `"N/A"` / `""`,
espaces parasites partout.

---
---

# SÉANCE 8 — Faire parler les données
### *Agrégation, jointures, Matplotlib, seaborn*

> **Promesse :** « Un tableau propre ne convainc personne. Un graphique juste, si. »

## Ce que ça couvre en Python

**Agréger**
- **`groupby` = découper, appliquer, combiner** — les trois temps mimés physiquement avec des
  cartes de couleur.
- `.agg(nom=("colonne", "fonction"))` : la **forme moderne nommée**, qui évite les index à
  plusieurs niveaux illisibles. *L'autre forme n'est pas enseignée.*
- `size()`, `reset_index()`, agrégations multiples en un appel.

**Combiner**
- **`merge` = le `RECHERCHEV` d'Excel, en mieux** — la phrase qui suffit pour un public qui
  vient du tableur.
- Les 4 jointures : `inner` (défaut), `left`, `right`, `outer`, avec un schéma d'ensembles.
- **Le piège annoncé avant qu'il ne survienne** : si la clé n'est pas unique à droite, le nombre
  de lignes **explose**. Réflexe installé : comparer `len(df)` avant et après chaque `merge`.
- `pivot_table` — le tableau croisé dynamique.

**Matplotlib**
- **Figure et Axes** : le cadre photo et la photo à l'intérieur. Un cadre peut contenir
  plusieurs photos.
- **Toujours l'interface orientée objet**, jamais l'interface d'état :
  `fig, ax = plt.subplots(figsize=(...))` — et non `plt.bar(...)` qui agit sur « le graphique
  courant », invisible et fragile. Justification : dès qu'on veut deux graphiques côte à côte,
  l'interface d'état devient impraticable.
- `ax.bar` / `ax.barh` / `ax.plot` / `ax.hist`, `set_title`, `set_xlabel`, `set_ylabel`,
  `legend()`, `axvline()` pour une ligne de repère.
- Sous-graphiques : `plt.subplots(2, 2)`, `fig.suptitle()`, `plt.tight_layout()`.
- **Exporter proprement** : `savefig(..., dpi=150, bbox_inches="tight")`, PNG vs SVG.

**seaborn**
- « Matplotlib avec les statistiques incluses » : en une ligne ce qui en prend quinze.
- API classique — `set_theme`, `barplot`, `histplot`, `boxplot`, `scatterplot`, `heatmap`,
  `catplot`, le paramètre `hue`, les **facettes** (un graphique par catégorie, automatiquement).
- L'interface **`seaborn.objects`** (grammaire des graphiques, proche de ggplot2), présentée
  comme une **ouverture**. Position tenue : *l'API classique reste le socle enseigné.*

**Les 5 règles de dataviz honnête** (slide à afficher au mur)
1. **Le titre porte le message**, pas la description. « Le Maroc concentre 60 % des
   opportunités » plutôt que « Opportunités par pays ».
2. **L'axe des barres part de zéro.** Toujours. Le tronquer est le mensonge graphique le plus
   courant.
3. **Trier par valeur**, pas par ordre alphabétique — sauf si l'ordre a un sens (les mois).
4. **Pas de camembert** au-delà de 3 parts, jamais en 3D.
5. **Une question, un graphique.**

**Choisir le bon graphique** (slide à imprimer)
comparer → barres · évoluer → ligne · répartir → histogramme · corréler → nuage de points ·
composer → barres empilées.

**Le moment pédagogique clé**
Faire **réécrire les titres**. La première version des apprenants est toujours descriptive.
Question posée : *« qu'est-ce que ce graphique t'apprend, en une phrase ? »* — la réponse devient
le titre. Cinq minutes qui transforment durablement leur rapport à la visualisation. Un titre qui
annonce **l'absence** de relation est un titre honnête.

**Bonus**
- Le même panneau en `seaborn.objects`, pour comparer la lisibilité du code.
- Évolution mensuelle : `df.resample("ME", on="deadline").size()`.
- Heatmap pays × statut avec `pivot_table` + `sns.heatmap`.
- Une fonction `graphique_par_pays(df, pays)` — **décorée avec le `@chronometre` de la S6**.

## Exercice principal / Fil rouge v5
**Le tableau de bord** : une figure à quatre panneaux répondant à quatre questions — combien par
pays ? comment se répartit l'urgence ? où en sont les candidatures ? le montant dépend-il du délai ?

---
---

# Vue d'ensemble des compétences

| Domaine | Séances | Compétence acquise |
|---|---|---|
| Fondamentaux | 1 – 4 | Variables, types, conditions, boucles, fonctions, fichiers, erreurs |
| Structuration | 4 – 5 | Classes, dataclasses, Enum, modules, séparation des responsabilités |
| Python avancé | 6 | Dunders, générateurs, décorateurs, contextes, `match` structurel |
| Données | 7 | NumPy, pandas 3.0, nettoyage, Copy-on-Write |
| Analyse & visualisation | 8 | `groupby`, `merge`, Matplotlib, seaborn, dataviz honnête |
| Collecte | 9 | HTTP, APIs, BeautifulSoup, éthique du scraping |
| Web | 10 | API REST, FastAPI, Pydantic v2, documentation automatique |
| Production | 6 · 11 | Ruff, pytest, uv, secrets, CI, Docker, déploiement |

## Le fil rouge, version par version

| Version | Séance | Ce que l'application sait faire |
|---|---|---|
| v0.1 | 1 | Afficher une fiche d'opportunité saisie au clavier |
| v0.2 | 2 | Décider s'il faut candidater, selon des règles |
| v0.3 | 3 | Tenir un carnet en mémoire, trié — mais qui oublie tout à la fermeture |
| **v1** | 4 | Application CLI complète, deux modules, données persistées en JSON |
| **v2** | 5 | Refactorisée en deux classes, à comportement identique |
| **v3** | 6 | Pythonique : dunders, générateurs, journalisation, 5 tests verts |
| **v4** | 7 | Un jeu de 300 lignes réelles, nettoyé et exploitable |
| **v5** | 8 | Un tableau de bord à 4 graphiques |
| **v6** | 9 | Un scraper qui alimente le carnet tout seul |
| **v7** | 10 | Une API REST documentée, utilisable par n'importe qui |
| **final** | 11 | Testée, verrouillée, conteneurisée, déployée |

## Les quatre chemins d'après-formation

À présenter en dernière slide de la séance 8, avec une ressource d'entrée pour chacun. Les
trois premiers sont exactement ce que la formation n'a pas eu le temps de couvrir — le dire
franchement vaut mieux que de laisser croire que le sujet est clos.

1. **Data / IA** — scikit-learn, puis PyTorch. Entrée : le cours *Machine Learning* de Kaggle Learn.
2. **Collecter ses propres données** — `requests`, les APIs publiques, BeautifulSoup.
   Entrée : l'annuaire *public-apis* sur GitHub.
3. **Exposer son code** — FastAPI et Pydantic v2. Entrée : le tutoriel officiel FastAPI,
   qui existe en français.
4. **Automatiser son travail** — *Automate the Boring Stuff*, chapitres tableurs, PDF et courriel.

---

## Ce qui a été retiré du programme

Les séances 9, 10 et 11 ont été sorties du cursus. Rien n'a été supprimé : tout est déplacé
dans `_archive-seances-9-11/` à la racine du projet.

| Ce qui est archivé | Contenu |
|---|---|
| `docs/guide-arc2-seances-9-a-11.md` | les trois guides minutés, avec corrigés commentés |
| `slides-latex/decks/` et `complements/` | les sources LaTeX des trois decks |
| `pdf/` | les six PDF déjà compilés (projection + version formateur) |
| `seances/s09 · s10 · s11` | les notebooks « point de reprise » |
| `fil-rouge/v6-scraper · v7-api` | le scraper et l'API, en code complet |
| `docs/formateur/GRILLE-DEMO-DAY.md` | le format et la grille du Demo Day |

**Ce que la séance 8 a récupéré :** la clôture de la formation — le chemin parcouru, les
quatre chemins pour continuer, et les remerciements — qui vivait auparavant en séance 11.
Le deck 08 est passé de 18 à 22 diapos sources.

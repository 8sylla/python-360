# Formation Python 360° — Guide du formateur
## ARC 2 : Séances 5 à 8

**Structurer, puis analyser.** L'Arc 1 a appris des instructions ; l'Arc 2 apprend à organiser du code et à faire parler des données.

---

# Note de version — à lire avant de préparer les séances 7 et 8

L'écosystème data a bougé en profondeur début 2026. **Une grande partie des tutoriels en ligne est aujourd'hui périmée.** Versions de référence pour cette formation :

| Bibliothèque | Version de référence (août 2026) | Ce qui change pour toi |
|---|---|---|
| **pandas** | **3.0.x** (3.0.0 le 21 janvier 2026, dernier correctif 3.0.5 le 22 juillet 2026) | **Rupture majeure.** Copy-on-Write par défaut, chaînes de caractères en backend Apache Arrow, l'affectation chaînée lève désormais une **erreur** au lieu d'un avertissement. Requiert Python 3.11+ |
| **NumPy** | 2.5.x (2.5.1 le 4 juillet 2026) | API 2.x stabilisée ; `np.float_`, `np.NaN` et consorts supprimés depuis la 2.0 |
| **Matplotlib** | 3.10.x | API stable ; privilégier l'interface orientée objet |
| **seaborn** | 0.13.x | L'interface `seaborn.objects` (grammaire des graphiques) coexiste avec l'API historique |

**Conséquences pédagogiques concrètes :**
1. **Ne jamais enseigner `SettingWithCopyWarning`.** Il a disparu. Enseigner à la place la règle du Copy-on-Write : *« une opération pandas rend une nouvelle table ; on réaffecte, on ne modifie pas en place. »* C'est **plus simple** à enseigner que l'ancien modèle. Bonne nouvelle pour un public débutant.
2. **Vérifier la version en début de S7** : `import pandas as pd; print(pd.__version__)`. Colab peut être en retard ; prévoir la cellule `!pip install -q "pandas>=3.0"` et un redémarrage du noyau.
3. Fournir un `requirements.txt` figé au groupe pour que personne ne travaille sur une 2.x :
   ```
   pandas>=3.0,<3.1
   numpy>=2.5,<3
   matplotlib>=3.10
   seaborn>=0.13
   ```
4. **Avertir explicitement les apprenants** : « les vidéos YouTube de 2023-2025 que vous trouverez montrent du code qui provoquera des erreurs. Vérifiez toujours la date. » C'est aussi une leçon de méthode, qui vaut au-delà de pandas.

---
---

# SÉANCE 5 — La Programmation Orientée Objet
### *Classes, objets, dataclasses, composition*

> **Promesse** : « Ton programme de la séance 4 marche. Aujourd'hui, on le rend maintenable par quelqu'un d'autre que toi. »

## Objectifs pédagogiques
1. **Expliquer** ce qu'est une classe, une instance, un attribut, une méthode — avec ses propres mots.
2. **Écrire** une classe avec `__init__`, des attributs et des méthodes, et l'instancier.
3. **Utiliser** `@dataclass` pour les objets porteurs de données, et savoir pourquoi c'est le défaut moderne.
4. **Distinguer** héritage et composition, et **justifier** le choix de la composition dans 80 % des cas.
5. **Employer** `Enum` pour remplacer les chaînes magiques.
6. **Annoter** ses classes et méthodes avec les types modernes (`list[str]`, `str | None`).
7. **Refactoriser** le fil rouge sans casser son comportement.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–15 | **Le problème** | Plénière | Projection du `tracker.py` de la S4 : 6 fonctions qui se passent toutes la même liste en paramètre. « Quelque chose veut naître ici. » |
| 15–45 | **Théorie 1** : classe et instance | Plénière + live coding | Le moule et les objets. `class`, `__init__`, `self`, attributs, méthodes. |
| 45–75 | **Pratique 1** | Individuel | Écrire une classe `Opportunite` from scratch, l'instancier 3 fois. |
| 75–85 | **PAUSE** | — | — |
| 85–105 | **Théorie 2** : `@dataclass`, `Enum`, `@property` | Live coding | La même classe réduite de 15 à 6 lignes. `__repr__` gratuit. Les statuts en `Enum`. Une propriété calculée. |
| 105–125 | **Théorie 3** : héritage vs composition | Plénière | « est un » / « a un ». Le piège de la hiérarchie profonde. |
| 125–165 | **Pratique 2 — Fil rouge v2** | Binômes | Refactorisation complète du tracker. |
| 165–175 | **Revue de code croisée** | Binômes échangés | Chaque binôme lit le code d'un autre et repère une responsabilité mal placée. |
| 175–180 | **Clôture** | Plénière | Teaser S6 : « la semaine prochaine, on regarde ce que Python fait dans notre dos ». |

## Concepts clés — expliqués simplement

**La classe = le moule ; l'objet = le gâteau.** Un moule ne se mange pas : il sert à fabriquer autant de gâteaux qu'on veut, tous de la même forme, mais avec des parfums différents. `class Opportunite` est le moule, `bourse = Opportunite("Smarts-Up", "France", 12)` est un gâteau.

**Pourquoi passer à l'objet ?** À faire découvrir plutôt qu'à décréter. Dans le code de la S4, toutes les fonctions commençaient par recevoir la même liste : `afficher(opportunites)`, `filtrer(opportunites, pays)`, `sauvegarder(opportunites)`. **Quand les mêmes données circulent entre toutes les fonctions, c'est le signe qu'un objet veut exister** : les données et les traitements qui les concernent doivent voyager ensemble.

**`self` = « moi-même ».** C'est la façon dont l'objet se désigne lui-même de l'intérieur. `self.titre` se lit « mon titre ». Ce n'est pas un mot-clé magique : c'est simplement le premier paramètre, que Python remplit automatiquement.

**`@dataclass` : le raccourci moderne.** Quand une classe existe surtout pour *porter des données*, on n'écrit plus le `__init__` à la main :
```python
from dataclasses import dataclass

@dataclass
class Opportunite:
    titre: str
    pays: str
    jours: int
```
Trois lignes remplacent quinze, et on obtient gratuitement un affichage lisible et la comparaison entre objets. Règle simple à donner : *« si ta classe est surtout des attributs, prends une dataclass ; si elle est surtout du comportement, écris une classe normale. »*

**L'`Enum` supprime les chaînes magiques.** `statut = "en_cours"` est fragile : une faute de frappe (`"en cours"`) ne provoque aucune erreur et casse silencieusement le filtrage. Avec `Statut.EN_COURS`, la faute de frappe devient une erreur immédiate, et l'éditeur propose la complétion.

**Héritage ou composition ?** Le test en une question :
- « Un `StageEtudiant` **est une** `Opportunite` » → héritage plausible.
- « Un `Carnet` **a des** `Opportunite` » → composition, sans hésiter.

Message à faire passer clairement, car c'est l'erreur classique des formations POO : **l'héritage est enseigné en premier et surutilisé en pratique.** Dans du code professionnel, la composition domine largement. On enseigne l'héritage parce qu'il faut savoir le lire, pas parce qu'il faut en mettre partout.

**Encapsulation, version honnête.** Python n'a pas de `private`. La convention `_attribut` signifie « ceci est interne, n'y touche pas ». C'est un panneau, pas un mur. Ne pas raconter aux apprenants qu'il existe une protection réelle : cette franchise leur évitera une confusion durable s'ils viennent de Java.

## Plan des slides — Séance 5 (20 slides)

1. **Couverture** — « Séance 5 : structurer avec les objets ». Mention : *début de l'Arc 2*.
2. **Frise** — le basculement visuel entre les deux arcs.
3. **Le code de la semaine dernière** — capture avec la liste `opportunites` surlignée dans les 6 signatures de fonction.
4. **Le signal** — « quand la même donnée passe partout, un objet veut naître ».
5. **Le moule et le gâteau** — photo d'un moule + trois gâteaux différents.
6. **Anatomie d'une classe** — code annoté : `class`, `__init__`, `self`, attributs, méthodes.
7. **Instancier** — une ligne de code, trois objets créés, schéma mémoire simplifié.
8. **`self` = moi-même** — la même méthode vue « de l'intérieur » et « de l'extérieur ».
9. **Exercice 1 : la classe `Opportunite`**.
10. **Avant / après `@dataclass`** — 15 lignes à gauche, 6 à droite. Slide à fort effet.
11. **Ce que `@dataclass` offre gratuitement** — `__init__`, `__repr__`, `__eq__` (annonce de la S6).
12. **⚠️ Les chaînes magiques** — le bug de la faute de frappe, en rouge.
13. **`Enum` à la rescousse** — le même code, la faute devient une erreur.
14. **`@property`** — l'attribut qui se calcule tout seul (`est_urgente`).
15. **« est un » vs « a un »** — deux schémas côte à côte.
16. **⚠️ Le piège de l'héritage** — arbre à 5 niveaux barré en rouge, composition à plat à côté.
17. **Les annotations de type modernes** — `list[Opportunite]`, `str | None`, sans `typing.List` (obsolète).
18. **Fil rouge v2 : la cible** — le diagramme des deux classes `Opportunite` et `Carnet`.
19. **Grille de revue de code** — 4 questions.
20. **Bilan / teaser S6**.

## Exercice pratique / Fil rouge v2 — `OpportuniTrack` orienté objet

**Énoncé.** Refactoriser le tracker de la S4 en deux classes : `Opportunite` (une opportunité) et `Carnet` (la collection + la persistance). Le comportement visible du programme ne doit **pas** changer — c'est la définition même d'une refactorisation.

### Corrigé commenté — `modeles.py`

```python
"""Modèle de données d'OpportuniTrack."""

from dataclasses import dataclass, field, asdict
from datetime import date
from enum import Enum


class Statut(str, Enum):
    """Statuts possibles d'une candidature.

    Hériter de `str` en plus de `Enum` permet de sérialiser directement
    en JSON sans conversion : Statut.A_FAIRE se comporte comme "a_faire".
    """
    A_FAIRE = "a_faire"
    EN_COURS = "en_cours"
    ENVOYEE = "envoyee"
    ARCHIVEE = "archivee"


@dataclass
class Opportunite:
    """Une opportunité repérée (bourse, stage, appel à candidature)."""

    titre: str
    organisme: str
    pays: str
    deadline: date
    # field(default=...) : valeur par défaut pour un champ de dataclass.
    statut: Statut = Statut.A_FAIRE
    tags: list[str] = field(default_factory=list)
    # ⚠️ default_factory=list et NON default=[] :
    # une liste par défaut serait PARTAGÉE par toutes les instances.
    # C'est le piège n°1 des dataclasses — le montrer en direct.

    @property
    def jours_restants(self) -> int:
        """Nombre de jours avant la deadline, calculé à la volée.

        Une @property se lit comme un attribut (opp.jours_restants, sans
        parenthèses) mais se recalcule à chaque lecture. C'est exactement
        ce qu'on veut ici : stocker le nombre de jours serait faux dès demain.
        """
        return (self.deadline - date.today()).days

    @property
    def est_urgente(self) -> bool:
        """Urgente = échéance dans moins de 7 jours et pas encore envoyée."""
        return 0 <= self.jours_restants < 7 and self.statut != Statut.ENVOYEE

    def marquer_envoyee(self) -> None:
        """Change le statut. La méthode DIT ce qu'elle fait ; le code appelant
        n'a pas à connaître le nom du champ interne."""
        self.statut = Statut.ENVOYEE

    def en_dict(self) -> dict:
        """Version dictionnaire, prête pour le JSON."""
        donnees = asdict(self)                      # dataclass -> dict
        donnees["deadline"] = self.deadline.isoformat()  # date -> "2026-12-31"
        return donnees

    @classmethod
    def depuis_dict(cls, donnees: dict) -> "Opportunite":
        """Reconstruit une Opportunite depuis un dictionnaire JSON.

        @classmethod : une méthode qui ne travaille pas sur UNE instance
        mais sur la classe elle-même. Usage typique : les constructeurs
        alternatifs. `cls` est à la classe ce que `self` est à l'instance.
        """
        donnees = dict(donnees)                     # copie : on ne modifie pas l'entrée
        donnees["deadline"] = date.fromisoformat(donnees["deadline"])
        donnees["statut"] = Statut(donnees.get("statut", "a_faire"))
        return cls(**donnees)                       # ** déplie le dict en arguments
```

### Corrigé commenté — `carnet.py`

```python
"""Collection d'opportunités et persistance."""

import json
from pathlib import Path

from modeles import Opportunite, Statut


class Carnet:
    """Gère une collection d'Opportunite et sa sauvegarde sur disque.

    COMPOSITION : un Carnet *a des* Opportunite. Il n'en hérite pas.
    """

    def __init__(self, fichier: Path = Path("donnees.json")) -> None:
        self.fichier = fichier
        self._opportunites: list[Opportunite] = []
        # Le _ signale : "interne, passe par les méthodes". Convention, pas verrou.

    # ---------- Lecture ----------

    def __len__(self) -> int:
        """Permet d'écrire len(carnet). Première dunder method de la formation :
        on approfondira en séance 6."""
        return len(self._opportunites)

    def toutes(self) -> list[Opportunite]:
        """Renvoie une COPIE : personne ne peut modifier la liste interne
        par accident depuis l'extérieur."""
        return list(self._opportunites)

    def urgentes(self) -> list[Opportunite]:
        return [o for o in self._opportunites if o.est_urgente]

    def par_pays(self, pays: str) -> list[Opportunite]:
        return [o for o in self._opportunites
                if o.pays.casefold() == pays.casefold()]
        # casefold() est la version robuste de lower() pour comparer
        # des textes internationaux.

    def triees_par_urgence(self) -> list[Opportunite]:
        return sorted(self._opportunites, key=lambda o: o.deadline)

    # ---------- Écriture ----------

    def ajouter(self, opportunite: Opportunite) -> None:
        self._opportunites.append(opportunite)

    def supprimer(self, index: int) -> Opportunite:
        return self._opportunites.pop(index)

    # ---------- Persistance ----------

    def charger(self) -> None:
        if not self.fichier.exists():
            return
        with self.fichier.open(encoding="utf-8") as f:
            self._opportunites = [Opportunite.depuis_dict(d) for d in json.load(f)]

    def sauvegarder(self) -> None:
        with self.fichier.open("w", encoding="utf-8") as f:
            json.dump([o.en_dict() for o in self._opportunites],
                      f, indent=2, ensure_ascii=False)
```

**Ce que `main()` devient** — à projeter comme récompense de la refactorisation :
```python
carnet = Carnet()
carnet.charger()
...
case "2":
    for opp in carnet.triees_par_urgence():
        print(f"{opp.titre:<30}{opp.pays:<15}{opp.jours_restants:>4} j")
```
Faire constater à voix haute : **le code principal se lit maintenant comme une phrase en français.** C'est le seul argument qui convainc vraiment un débutant que la POO sert à quelque chose.

### Palier bonus
1. Ajouter une classe `Bourse(Opportunite)` avec un champ `montant` — et **débattre** : est-ce vraiment un cas d'héritage, ou un simple champ optionnel de plus ?
2. Implémenter `__eq__` pour détecter les doublons (titre + organisme identiques).
3. Rendre `Opportunite` immuable avec `@dataclass(frozen=True)` et discuter des conséquences sur `marquer_envoyee()`.
4. Ajouter `__iter__` au `Carnet` pour pouvoir écrire `for opp in carnet:` — un pont direct vers la S6.

### Grille de revue de code croisée
1. Une classe = une responsabilité. Laquelle porte cette classe, en une phrase ?
2. Y a-t-il une méthode qui pourrait vivre ailleurs ?
3. Un attribut est-il modifié directement de l'extérieur alors qu'une méthode existe ?
4. Les noms de méthodes sont-ils des **verbes** ?

## Ressources — Séance 5
| Ressource | Lien | Note |
|---|---|---|
| Tutoriel officiel — Classes | https://docs.python.org/fr/3/tutorial/classes.html | Section 9 |
| `dataclasses` (doc officielle) | https://docs.python.org/fr/3/library/dataclasses.html | Lire la section sur `default_factory` |
| `enum` (doc officielle) | https://docs.python.org/fr/3/library/enum.html | Voir aussi `StrEnum` (3.11+) |
| Real Python — OOP in Python | https://realpython.com/python3-object-oriented-programming/ | Progressif |
| Real Python — Data Classes | https://realpython.com/python-data-classes/ | — |
| Real Python — `@property` | https://realpython.com/python-property/ | — |
| PEP 557 — Data Classes | https://peps.python.org/pep-0557/ | La motivation d'origine, utile au formateur |
| *Fluent Python*, 2e éd. (Ramalho) | https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/ | Ch. 5 et 11. **Le livre de chevet du formateur pour les S5-S6** |
| `attrs` (alternative) | https://www.attrs.org/ | À mentionner en une phrase, pas à enseigner |

---
---

# SÉANCE 6 — Sous le capot : Python avancé et fonctionnel
### *Dunder methods, générateurs, décorateurs, et outillage qualité*

> **Promesse** : « Aujourd'hui, tu arrêtes d'utiliser Python et tu commences à le comprendre. »

C'est la séance la plus exigeante de la formation. Prévoir un notebook de reprise très complet, et assumer que les débutants ne mèneront pas tous les exercices à terme — l'objectif pour eux est de **savoir lire** ce code, pas de savoir l'écrire.

## Objectifs pédagogiques
1. **Expliquer** le rôle des méthodes spéciales (`__str__`, `__repr__`, `__eq__`, `__len__`, `__iter__`) et en implémenter au moins deux.
2. **Écrire** un générateur avec `yield` et **articuler** son intérêt mémoire.
3. **Écrire** un décorateur simple avec `functools.wraps` et **expliquer** ce qu'il fait au moment de l'import.
4. **Utiliser** un gestionnaire de contexte et en créer un avec `contextlib.contextmanager`.
5. **Employer** `match/case` sur des motifs structurels (au-delà du menu de la S4).
6. **Exploiter** `functools` et `itertools` sur au moins deux cas concrets.
7. **Faire tourner** `ruff` sur son projet et **écrire** ses trois premiers tests `pytest`.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–10 | Rituel | Plénière | « Pourquoi `print(mon_objet)` affiche-t-il `<__main__.Carnet object at 0x7f...>` ? » |
| 10–35 | **Théorie 1** : les dunder methods | Live coding | Le protocole plutôt que l'interface. `__str__` vs `__repr__`, `__eq__`, `__len__`, `__contains__`. |
| 35–55 | **Pratique 1** | Individuel | Rendre le `Carnet` affichable, mesurable et parcourable. |
| 55–80 | **Théorie 2** : itérateurs et générateurs | Live coding + mesure | `__iter__`, `yield`, la paresse, comparaison mémoire chiffrée avec `sys.getsizeof`. |
| 80–90 | **PAUSE** | — | — |
| 90–120 | **Théorie 3** : décorateurs | Live coding progressif | Fonction = objet → fonction qui prend une fonction → sucre `@` → `functools.wraps`. **Quatre étapes, jamais moins.** |
| 120–140 | **Pratique 2** | Binômes | Écrire `@chronometre` et `@journalise`. |
| 140–155 | **Théorie 4** : contextes, `match` structurel, `functools`/`itertools` | Plénière rapide | Tour d'horizon avec un cas d'usage chacun. |
| 155–175 | **Atelier qualité** | Individuel guidé | `ruff check` / `ruff format` sur le projet + 3 tests `pytest` qui passent. |
| 175–180 | **Clôture** | Plénière | Teaser S7 : « la semaine prochaine, 40 000 lignes de données. » |

## Concepts clés — expliqués simplement

**Les dunder methods = les prises normalisées.** Python ne demande pas à tes objets « quelle est ta longueur ? » ; il cherche une prise nommée `__len__`. Si elle existe, `len(objet)` fonctionne. C'est ce qu'on appelle un **protocole** : Python définit la forme de la prise, tu décides ce qu'il y a derrière. Analogie : la prise électrique murale — l'appareil n'a pas besoin de connaître la centrale.

**`__str__` vs `__repr__`.** `__str__` s'adresse à l'utilisateur (« Bourse Smarts-Up — France ») ; `__repr__` s'adresse au développeur et devrait idéalement être du code réexécutable (`Opportunite(titre='...', pays='France')`). Règle pratique : *si tu n'en écris qu'une, écris `__repr__`* — Python l'utilisera par défaut pour les deux, et c'est celle qui s'affiche dans les listes et le débogueur.

**Le générateur = le distributeur de tickets.** Une liste, c'est imprimer les 10 millions de tickets d'avance et les stocker. Un générateur, c'est un distributeur qui en imprime **un** quand tu appuies. Il ne calcule que ce qu'on lui demande, quand on le lui demande.
```python
def lignes_du_fichier(chemin):
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            yield ligne.strip()   # rend une ligne, MET EN PAUSE, reprend au prochain tour
```
Faire la démonstration chiffrée en direct : `sys.getsizeof(range(10_000_000))` contre `sys.getsizeof(list(range(10_000_000)))`. L'écart entre quelques dizaines d'octets et plusieurs centaines de mégaoctets marque durablement.

**Le décorateur = l'emballage cadeau.** Il enveloppe une fonction pour lui ajouter un comportement sans toucher à son contenu. Le contenu du cadeau ne change pas ; ce qu'on voit de l'extérieur, si.

**Enseigner le décorateur en quatre marches obligatoires** — c'est ce découpage qui fait la différence entre « je copie » et « je comprends » :
1. *Une fonction est une valeur comme une autre.* `f = dire_bonjour` (sans parenthèses !) puis `f()`.
2. *Une fonction peut recevoir une fonction.* `def deux_fois(f): f(); f()`
3. *Une fonction peut fabriquer et rendre une fonction.* C'est la marche difficile ; y consacrer le temps nécessaire.
4. *`@decorateur` au-dessus d'un `def` est exactement `ma_fonction = decorateur(ma_fonction)`.* Écrire les deux formes côte à côte au tableau.

**`functools.wraps`** : sans lui, la fonction décorée perd son nom et sa docstring — elle s'appelle désormais `wrapper`. C'est un détail invisible qui devient très visible le jour du débogage. À présenter comme un réflexe, pas comme une option.

**Le gestionnaire de contexte = « quoi qu'il arrive, referme ».** Le `with open()` de la S4 était déjà un contexte. On révèle maintenant le mécanisme : `__enter__` / `__exit__`, ou plus simplement `@contextmanager` avec un `yield` au milieu.

**`match/case` structurel** — bien au-delà du menu :
```python
match evenement:
    case {"type": "offre", "pays": "France", **reste}:
        ...
    case {"type": "offre", "jours": int(j)} if j < 7:   # garde
        ...
    case [premier, *autres]:                            # motif de séquence
        ...
    case _:
        ...
```
Le vendre pour ce qu'il est : **du filtrage de forme**, pas un simple `switch`. C'est particulièrement utile dès qu'on traite du JSON — donc dès qu'on touche à des données venues d'ailleurs.

**`functools` et `itertools`, deux gestes utiles chacun :**
- `@functools.cache` : mémorise les résultats d'une fonction coûteuse. Démonstration spectaculaire sur Fibonacci récursif.
- `functools.partial` : fige un argument, utile pour les `key=`.
- `itertools.groupby` (après tri !) et `itertools.batched` (3.12+) pour découper en lots — utile dès qu'on traite un gros fichier par paquets.

**Le pont vers la qualité.** Ne pas présenter `ruff` et `pytest` comme des contraintes administratives mais comme un **filet** :
- `ruff format` : plus jamais de débat sur les espaces. La machine tranche.
- `ruff check` : détecte les imports inutiles, les variables mortes, les erreurs de style… en quelques millisecondes.
- `pytest` : le premier test qu'on écrit est celui de la fonction qu'on vient de casser. C'est le meilleur angle de motivation.

```python
# tests/test_modeles.py
from datetime import date, timedelta
from modeles import Opportunite, Statut


def test_jours_restants():
    demain = date.today() + timedelta(days=1)
    opp = Opportunite("Test", "Org", "Maroc", demain)
    assert opp.jours_restants == 1          # assert : "j'affirme que". C'est tout.


def test_est_urgente_si_proche():
    opp = Opportunite("Test", "Org", "Maroc", date.today() + timedelta(days=3))
    assert opp.est_urgente is True


def test_non_urgente_si_deja_envoyee():
    opp = Opportunite("Test", "Org", "Maroc", date.today() + timedelta(days=3),
                      statut=Statut.ENVOYEE)
    assert opp.est_urgente is False
```
Faire tourner `pytest -q`, obtenir trois points verts. Puis **casser volontairement** `est_urgente` (mettre `< 30`) et relancer : le test rouge est le moment pédagogique de la séance.

## Plan des slides — Séance 6 (24 slides)

1. **Couverture** + 2. **Frise** + 3. **L'énigme du jour** (`<object at 0x7f...>`).
2. **Les prises normalisées** — schéma prise murale / appareils.
3. **`__str__` vs `__repr__`** — deux colonnes, deux publics.
4. **Le catalogue des dunders utiles** — tableau : `__len__`, `__eq__`, `__contains__`, `__iter__`, `__getitem__` + l'écriture Python correspondante.
5. **Exercice 1 : rendre le `Carnet` pythonique**.
6. **Le distributeur de tickets** — liste vs générateur, illustration.
7. **`yield` en action** — schéma d'exécution en 4 temps (pause / reprise).
8. **La preuve par la mémoire** — capture de `sys.getsizeof`, chiffres en gros.
9. **⚠️ Un générateur ne se parcourt qu'une fois** — la démonstration de l'erreur.
10. **Marche 1 : une fonction est une valeur** — `f = dire_bonjour`.
11. **Marche 2 : une fonction reçoit une fonction**.
12. **Marche 3 : une fonction rend une fonction** — la slide à ne pas presser.
13. **Marche 4 : le sucre `@`** — les deux écritures équivalentes côte à côte.
14. **Un décorateur complet, annoté** — chaque ligne numérotée et expliquée.
15. **`functools.wraps`** — avant/après, le nom perdu puis retrouvé.
16. **Exercice 2 : `@chronometre`**.
17. **Le gestionnaire de contexte** — « quoi qu'il arrive, referme » + `@contextmanager`.
18. **`match` structurel** — le même JSON traité en `if` imbriqués vs en `match`. Effet visuel fort.
19. **`functools` / `itertools` en 6 gestes** — tableau.
20. **Le filet de sécurité** — logos `ruff` + `pytest`.
21. **`ruff` en 2 commandes** — `ruff format .` et `ruff check .`.
22. **Mon premier test** — le code + la sortie verte.
23. **Le test qui devient rouge** — capture de l'échec, avec le diff `pytest`.
24. **Bilan / teaser S7**.

## Exercice pratique — Le décorateur `@chronometre`

**Énoncé (socle).** Écrire un décorateur qui affiche le temps d'exécution d'une fonction, puis l'appliquer à une fonction lente.

### Corrigé commenté

```python
import functools
import time


def chronometre(fonction):
    """Décorateur : affiche la durée d'exécution de la fonction décorée."""

    @functools.wraps(fonction)   # conserve le nom et la docstring de l'original
    def enveloppe(*args, **kwargs):
        # *args / **kwargs : "accepte n'importe quels arguments et transmets-les
        # tels quels". Indispensable pour un décorateur générique.
        depart = time.perf_counter()      # perf_counter : horloge de précision
        resultat = fonction(*args, **kwargs)   # on appelle la vraie fonction
        duree = time.perf_counter() - depart

        print(f"[chrono] {fonction.__name__} : {duree:.3f} s")
        return resultat   # ⚠️ SANS ce return, la fonction décorée rend None.
                          # C'est LE bug classique du décorateur : le provoquer en direct.

    return enveloppe      # on rend la fonction-enveloppe, pas son résultat :
                          # pas de parenthèses ici.


@chronometre
def charger_beaucoup(n: int) -> list[int]:
    """Simule un traitement lent."""
    return [i ** 2 for i in range(n)]


charger_beaucoup(5_000_000)
# [chrono] charger_beaucoup : 0.412 s
```

**Deux erreurs à provoquer en direct** (elles valent mieux qu'une explication) :
1. Retirer `return resultat` → la fonction rend `None`, tout casse en aval.
2. Retirer `@functools.wraps` → `charger_beaucoup.__name__` affiche `enveloppe`.

### Palier bonus
1. `@reessayer(n=3, delai=1)` : un décorateur **paramétré** — trois niveaux d'imbrication. C'est l'exercice qui sépare ceux qui ont compris de ceux qui ont copié. C'est aussi le motif exact qu'on écrit pour absorber une erreur réseau passagère.
2. `@journalise` qui écrit dans un fichier avec le module `logging` plutôt que `print`.
3. Réécrire `Carnet.urgentes()` en générateur et mesurer la différence sur 100 000 entrées.
4. Implémenter `__enter__`/`__exit__` sur `Carnet` pour que `with Carnet() as c:` charge à l'entrée et sauvegarde à la sortie.

## Fil rouge — `OpportuniTrack` v3
- `Opportunite.__str__` pour un affichage propre, `__eq__` pour la détection de doublons.
- `Carnet.__iter__` : `for opp in carnet:` fonctionne.
- Un décorateur `@journalise` sur `ajouter()` et `supprimer()` — le carnet tient un journal de ses modifications.
- Un dossier `tests/` avec 5 tests qui passent, et `ruff` sans avertissement.

## Ressources — Séance 6
| Ressource | Lien | Note |
|---|---|---|
| Modèle de données Python (dunders) | https://docs.python.org/fr/3/reference/datamodel.html | Dense mais c'est **la** référence |
| Real Python — Primer on Decorators | https://realpython.com/primer-on-python-decorators/ | La meilleure progression pédagogique disponible |
| Real Python — Generators | https://realpython.com/introduction-to-python-generators/ | — |
| Real Python — Context Managers | https://realpython.com/python-with-statement/ | — |
| `functools` | https://docs.python.org/fr/3/library/functools.html | `wraps`, `cache`, `partial` |
| `itertools` | https://docs.python.org/fr/3/library/itertools.html | Voir la section « Recipes » en bas de page |
| `contextlib` | https://docs.python.org/fr/3/library/contextlib.html | — |
| PEP 636 — Pattern matching | https://peps.python.org/pep-0636/ | Les motifs structurels |
| **Ruff** — doc officielle | https://docs.astral.sh/ruff/ | Formateur + linter, remplace black/flake8/isort |
| **pytest** — doc officielle | https://docs.pytest.org/ | Commencer par « Get Started » |
| *Fluent Python*, 2e éd. | https://www.fluentpython.com/ | Ch. 1 (modèle de données), 9 (décorateurs), 17 (générateurs) |
| PyMOTW-3 | https://pymotw.com/3/ | Un module standard par page, avec exemples |

---
---

# SÉANCE 7 — Les données : NumPy et pandas
### *Du tableau en mémoire au DataFrame*

> **Promesse** : « Ta liste de dictionnaires plafonne à quelques centaines de lignes. Aujourd'hui, on en traite cent mille en une seconde. »

## Objectifs pédagogiques
1. **Expliquer** pourquoi un `ndarray` est plus rapide qu'une liste Python, et **mesurer** l'écart.
2. **Utiliser** la vectorisation, l'indexation booléenne et le broadcasting NumPy.
3. **Charger** un CSV dans un DataFrame et **inspecter** un jeu de données inconnu en 5 commandes.
4. **Sélectionner** avec `.loc` / `.iloc` et **filtrer** avec des masques booléens.
5. **Nettoyer** : types, valeurs manquantes, doublons, textes, dates.
6. **Appliquer** le modèle Copy-on-Write de pandas 3.0 (réaffecter plutôt que modifier en place).

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–10 | **Mise en place** | Individuel | Vérification de version, `pip install -r requirements.txt`, chargement du dataset. |
| 10–20 | **Le pont** | Plénière | Reprise de la liste de dictionnaires de la S3 → même chose en DataFrame. « Vous connaissez déjà la structure. » |
| 20–45 | **Théorie 1** : NumPy | Live coding + mesure | `ndarray`, homogénéité, vectorisation, `%timeit` comparatif, broadcasting, masques. |
| 45–60 | **Pratique 1** | Individuel | 6 manipulations sur un tableau de notes/scores. |
| 60–70 | **PAUSE** | — | — |
| 70–100 | **Théorie 2** : pandas, les fondations | Live coding | Series, DataFrame, `read_csv`, les 5 commandes d'inspection, `dtypes`. |
| 100–125 | **Théorie 3** : sélectionner et filtrer | Live coding | `.loc` / `.iloc`, masques, `.query()`, tri, colonnes calculées avec `.assign()`. |
| 125–140 | **Théorie 4** : nettoyer (pandas 3.0) | Live coding | `isna`, `fillna`, `dropna`, `astype`, `.str`, `to_datetime`, `drop_duplicates`. Le modèle Copy-on-Write. |
| 140–172 | **Pratique 2 — Fil rouge v4** | Binômes | Nettoyage d'un jeu de 300 opportunités volontairement sale. |
| 172–180 | **Clôture** | Plénière | Teaser S8. |

## Concepts clés — expliqués simplement

**Pourquoi NumPy est rapide : la boîte à œufs contre le sac de courses.** Une liste Python est un sac : chaque élément peut être n'importe quoi, chacun est rangé à un endroit différent de la mémoire, et Python doit vérifier le type à chaque opération. Un `ndarray` est une boîte à œufs : **une seule sorte de contenu, des cases contiguës, de taille identique**. Le processeur peut alors traiter plusieurs cases par instruction, et la boucle se déroule en C, pas en Python.

**La vectorisation = arrêter d'écrire la boucle.**
```python
# La façon "liste" : Python fait 1 000 000 de tours
resultats = [x * 2 for x in valeurs]

# La façon NumPy : une seule instruction, la boucle est dans le C
resultats = valeurs * 2
```
Mesurer en direct avec `%timeit` : l'écart est typiquement de 1 à 2 ordres de grandeur. **Ne pas se contenter d'annoncer le chiffre, le produire devant le groupe.**

**Le masque booléen** est le concept qui débloque tout le reste :
```python
masque = tableau > 50          # un tableau de True/False, de même forme
tableau[masque]                # ne garde que les cases True
```
C'est exactement le mécanisme qu'on retrouvera dans pandas : `df[df["jours"] < 7]`. Le faire dessiner par le groupe : une rangée de valeurs, une rangée de cases cochées.

**Le broadcasting = l'étirement automatique.** Quand les formes ne correspondent pas exactement, NumPy « étire » la plus petite s'il le peut. `tableau + 10` fonctionne parce que le 10 est diffusé à toutes les cases. Le présenter simplement, sans les règles complètes — elles viendront naturellement à l'usage.

**Le DataFrame = le tableur programmable.** Deux façons de le présenter selon le profil :
- Pour les profils non techniques : « c'est un onglet Excel, mais piloté par du code, reproductible, et sans limite de lignes ».
- Pour les techniques : « c'est la liste de dictionnaires de la séance 3, stockée en colonnes plutôt qu'en lignes — d'où sa vitesse ».

**Les 5 commandes d'inspection**, à imposer comme un rituel devant tout jeu de données inconnu :
```python
df.shape        # combien de lignes, combien de colonnes ?
df.head()       # à quoi ça ressemble ?
df.info()       # quels types, combien de valeurs manquantes ?
df.describe()   # quelles distributions pour les colonnes numériques ?
df["pays"].value_counts()   # que contient réellement cette colonne ?
```
Faire de `value_counts()` un réflexe : c'est là qu'on découvre que « Maroc », « maroc » et « MAROC » sont trois pays différents pour la machine.

**`.loc` contre `.iloc`** — la source de confusion n°1 :
- `.loc` travaille avec les **étiquettes** (noms de colonnes, valeurs d'index).
- `.iloc` travaille avec les **positions** (des entiers, comme en S3).
Moyen mnémotechnique : le **i** de `iloc` comme **index numérique**.

**⚠️ Le changement majeur de pandas 3.0 : le Copy-on-Write.** À enseigner comme une **règle unique et positive**, sans jamais évoquer l'ancien monde :

> *Une opération pandas ne modifie jamais la table d'origine : elle en rend une nouvelle. Si tu veux garder le résultat, réaffecte-le.*

```python
# ✅ La bonne façon, la seule à enseigner
df = df.dropna(subset=["deadline"])
df = df.assign(urgent=df["jours"] < 7)

# ❌ Provoque désormais une ERREUR (et non plus un simple avertissement)
df[df["jours"] > 0]["statut"] = "actif"
```
Cette rupture est en réalité une **aubaine pédagogique** : le modèle mental « chaque étape produit une nouvelle table » est plus simple que l'ancien, et il prépare directement au chaînage de méthodes. Si un apprenant trouve un tutoriel qui parle de `SettingWithCopyWarning` ou de `inplace=True`, c'est le signal que le contenu est daté.

**Les chaînes de caractères en pandas 3.0** sont désormais stockées via Apache Arrow plutôt qu'en `object`. Conséquence visible pour l'apprenant : `df.info()` affiche `str` et non plus `object`, et les opérations `.str` sont nettement plus rapides. Ne pas en faire un chapitre — juste éviter que la surprise déstabilise.

## Plan des slides — Séance 7 (23 slides)

1. **Couverture** + 2. **Frise**.
2. **Le pont** — la liste de dictionnaires de la S3 à gauche, le DataFrame à droite, mêmes données.
3. **⚠️ Note de version** — pandas 3.0, et l'avertissement « les tutoriels d'avant 2026 vont vous mentir ».
4. **Le sac de courses vs la boîte à œufs** — schéma mémoire.
5. **La vectorisation** — les deux codes côte à côte.
6. **La preuve chronométrée** — capture `%timeit`, chiffres en très gros.
7. **Le masque booléen** — schéma de la rangée de cases cochées.
8. **Le broadcasting** — animation de l'étirement du scalaire.
9. **Exercices NumPy flash**.
10. **Series et DataFrame** — anatomie annotée : index, colonnes, valeurs.
11. **Charger des données** — `read_csv` et ses 4 paramètres qui sauvent (`sep`, `encoding`, `parse_dates`, `dtype`).
12. **Le rituel des 5 commandes** — **slide à imprimer et afficher au mur**.
13. **`value_counts()`, le détecteur de saleté** — capture montrant « Maroc / maroc / MAROC ».
14. **`.loc` vs `.iloc`** — deux colonnes + le moyen mnémotechnique.
15. **Filtrer avec un masque** — le parallèle direct avec la slide NumPy.
16. **⚠️ La règle d'or de pandas 3.0** — pleine page : *« pandas rend une nouvelle table. Réaffecte. »*
17. **Le code qui plante maintenant** — l'affectation chaînée et son erreur.
18. **Nettoyer : la trousse à outils** — tableau : manquants, doublons, types, textes, dates.
19. **Les dates** — `to_datetime`, l'accesseur `.dt`, le piège des formats jour/mois.
20. **Créer une colonne : `.assign()`** — et pourquoi il se chaîne mieux que `df["x"] = ...`.
21. **Le pipeline de nettoyage** — les 6 étapes chaînées, vue d'ensemble.
22. **Exercice : 300 opportunités très sales**.
23. **Bilan / teaser S8**.

## Exercice pratique / Fil rouge v4 — Le nettoyage

**Le jeu de données** (le formateur le génère à l'avance, `opportunites_brutes.csv`, ~300 lignes, avec des défauts délibérés) :
- casse incohérente sur `pays` (`Maroc`, `maroc`, ` MAROC `) ;
- dates en trois formats différents et quelques dates vides ;
- doublons exacts et quasi-doublons ;
- colonne `montant` contenant `"1 500 €"`, `"N/A"`, `""` ;
- espaces parasites partout.

### Corrigé commenté

```python
import pandas as pd

# 1) CHARGEMENT ------------------------------------------------------------
# encoding : toujours l'expliciter. sep : la France exporte souvent en ";".
df = pd.read_csv("opportunites_brutes.csv", encoding="utf-8", sep=",")

# 2) INSPECTION (le rituel) -------------------------------------------------
print(df.shape)
print(df.info())
print(df["pays"].value_counts())   # ici on découvre la casse incohérente

# 3) NETTOYAGE DES TEXTES ---------------------------------------------------
# .str donne accès aux méthodes de texte sur TOUTE la colonne d'un coup :
# c'est la vectorisation de la séance, appliquée aux chaînes.
df = df.assign(
    pays=df["pays"].str.strip().str.title(),        # " maroc " -> "Maroc"
    titre=df["titre"].str.strip(),
    organisme=df["organisme"].str.strip(),
)
# assign() rend une NOUVELLE table (Copy-on-Write) : on réaffecte à df.

# 4) DATES ------------------------------------------------------------------
# format="mixed" laisse pandas détecter chaque format ligne par ligne.
# errors="coerce" transforme l'irrécupérable en NaT (Not a Time) plutôt
# que de faire planter tout le chargement.
df = df.assign(deadline=pd.to_datetime(df["deadline"],
                                       format="mixed",
                                       dayfirst=True,      # 03/04 = 3 avril
                                       errors="coerce"))

nb_dates_perdues = df["deadline"].isna().sum()
print(f"{nb_dates_perdues} dates illisibles")   # on TRACE ce qu'on perd

# 5) MONTANTS ---------------------------------------------------------------
montants = (df["montant"]
            .str.replace(r"[^\d,.]", "", regex=True)  # ne garde que les chiffres
            .str.replace(",", ".", regex=False)       # virgule décimale -> point
            .replace("", None))
df = df.assign(montant=pd.to_numeric(montants, errors="coerce"))

# 6) DOUBLONS ---------------------------------------------------------------
avant = len(df)
df = df.drop_duplicates(subset=["titre", "organisme"], keep="first")
print(f"{avant - len(df)} doublons supprimés")

# 7) LIGNES INEXPLOITABLES --------------------------------------------------
# On ne supprime QUE ce qui rend la ligne inutilisable. Supprimer toute ligne
# ayant une valeur manquante quelque part est presque toujours une erreur.
df = df.dropna(subset=["titre", "deadline"])

# 8) COLONNES CALCULÉES -----------------------------------------------------
aujourd_hui = pd.Timestamp.today().normalize()   # minuit, pour comparer des jours
df = df.assign(
    jours_restants=(df["deadline"] - aujourd_hui).dt.days,
)
df = df.assign(
    urgente=(df["jours_restants"] >= 0) & (df["jours_restants"] < 7),
    # ⚠️ & et non "and" : on combine deux COLONNES de booléens, pas deux valeurs.
    # Et les parenthèses sont obligatoires (priorité des opérateurs).
)

# 9) SAUVEGARDE -------------------------------------------------------------
df.to_csv("opportunites_propres.csv", index=False, encoding="utf-8")
print(f"✅ {len(df)} lignes propres sur {avant} au départ")
```

**Les trois points à marteler à l'oral :**
1. **`&` et non `and`**, `|` et non `or`, avec des parenthèses. C'est l'erreur pandas la plus fréquente au monde.
2. **On trace ce qu'on jette.** Un nettoyage silencieux est un nettoyage suspect. Chaque suppression s'accompagne d'un comptage affiché.
3. **`errors="coerce"`** est un choix, pas un réflexe : il transforme les erreurs en valeurs manquantes. On l'assume et on regarde combien il en a produites.

### Palier bonus
1. Réécrire tout le pipeline en **une seule chaîne** de méthodes avec `.pipe()` et des fonctions nommées — la forme professionnelle.
2. Détecter les quasi-doublons par similarité de titre (`difflib.SequenceMatcher`).
3. Comparer les temps de `df["pays"].str.upper()` en pandas 3.0 (Arrow) et sur une colonne convertie en `object`.
4. Explorer `pd.read_csv(..., dtype_backend="pyarrow")` et mesurer l'occupation mémoire avec `df.memory_usage(deep=True)`.

## Ressources — Séance 7
| Ressource | Lien | Note |
|---|---|---|
| **pandas — Nouveautés 3.0** | https://pandas.pydata.org/docs/whatsnew/v3.0.0.html | **À lire avant de préparer la séance** |
| pandas — Guide utilisateur | https://pandas.pydata.org/docs/user_guide/index.html | La section « Copy-on-Write » est incontournable |
| pandas — 10 minutes to pandas | https://pandas.pydata.org/docs/user_guide/10min.html | Le point d'entrée à distribuer |
| pandas — Comparaison avec Excel | https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html | **La ressource idéale pour le public non technique** |
| NumPy — Absolute Beginners | https://numpy.org/doc/stable/user/absolute_beginners.html | Excellent et à jour |
| NumPy — Broadcasting | https://numpy.org/doc/stable/user/basics.broadcasting.html | — |
| NumPy — Notes de version 2.5 | https://numpy.org/news/ | Suivi des ruptures d'API |
| Real Python — pandas DataFrame | https://realpython.com/pandas-dataframe/ | Vérifier la date de mise à jour de l'article |
| *Python for Data Analysis*, 3e éd. (Wes McKinney) | https://wesmckinney.com/book/ | Gratuit en ligne, par le créateur de pandas. Ch. 5-7. Écrit pour pandas 2.x : signaler l'écart sur le Copy-on-Write |
| Kaggle Learn — pandas | https://www.kaggle.com/learn/pandas | Exercices auto-corrigés, gratuit |
| pandas cheat sheet (officielle) | https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf | À imprimer pour le groupe |

---
---

# SÉANCE 8 — Faire parler les données
### *Agrégation, jointures, Matplotlib, seaborn*

> **Promesse** : « Un tableau propre ne convainc personne. Un graphique juste, si. »

## Objectifs pédagogiques
1. **Agréger** avec `groupby` + `agg` et **lire** le résultat.
2. **Combiner** deux tables avec `merge` et **choisir** le bon type de jointure.
3. **Construire** un tableau croisé avec `pivot_table`.
4. **Construire** un graphique Matplotlib avec l'interface orientée objet (`fig, ax`).
5. **Choisir** le type de graphique adapté à la question posée.
6. **Produire** un graphique seaborn, en API classique et avec l'interface `objects`.
7. **Appliquer** 5 règles de dataviz honnête et **exporter** une figure publiable.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–10 | Rituel | Plénière | Un graphique trompeur trouvé dans la presse : le groupe repère l'entourloupe. |
| 10–40 | **Théorie 1** : `groupby` | Live coding | Le modèle découper–appliquer–combiner. `agg`, agrégations multiples, `reset_index`. |
| 40–60 | **Théorie 2** : `merge` et `pivot_table` | Live coding | Les 4 jointures illustrées, le piège de l'explosion de lignes. |
| 60–75 | **Pratique 1** | Individuel | 5 questions métier à répondre par une agrégation. |
| 75–85 | **PAUSE** | — | — |
| 85–110 | **Théorie 3** : Matplotlib | Live coding | Figure vs Axes. `fig, ax = plt.subplots()`. Titres, axes, légende, export. |
| 110–130 | **Théorie 4** : seaborn | Live coding | API classique (`barplot`, `histplot`, `boxplot`, `heatmap`) puis `seaborn.objects`. |
| 130–145 | **Théorie 5** : dataviz honnête | Plénière | Les 5 règles, illustrées par des contre-exemples. |
| 145–172 | **Pratique 2 — Fil rouge v5** | Binômes | Le tableau de bord en 4 graphiques. |
| 172–180 | **Clôture de la formation** | Plénière | Le chemin parcouru, les quatre chemins pour continuer, remerciements. |

## Concepts clés — expliqués simplement

**`groupby` = découper, appliquer, combiner.** Trois temps à mimer physiquement devant le groupe avec des cartes de couleur :
1. **Découper** le paquet en tas selon une colonne (les pays).
2. **Appliquer** un calcul à chaque tas (compter, moyenner).
3. **Combiner** les résultats en une nouvelle table.
```python
resume = (df.groupby("pays")
            .agg(nombre=("titre", "count"),
                 jours_moyens=("jours_restants", "mean"),
                 prochaine=("deadline", "min"))
            .reset_index())
```
La syntaxe `nom=("colonne", "fonction")` est la forme moderne : elle nomme les colonnes de sortie, ce qui évite les index à plusieurs niveaux illisibles pour un débutant. **Ne pas enseigner l'autre forme.**

**`merge` = le tableur `RECHERCHEV`, en mieux.** Pour un public qui vient d'Excel, cette phrase suffit à faire passer le concept. Les quatre types, avec un schéma d'ensembles :
- `inner` : seulement ce qui existe des deux côtés (défaut).
- `left` : tout ce qui est à gauche, complété si possible.
- `right` : l'inverse.
- `outer` : tout le monde.

**Le piège à annoncer avant qu'il ne survienne** : si la clé de jointure n'est pas unique à droite, le nombre de lignes **explose**. Réflexe à installer : comparer `len(df)` avant et après chaque `merge`. Si ça a grossi, c'est un bug.

**Matplotlib : Figure et Axes.** L'analogie du cadre photo : la **Figure** est le cadre (la feuille entière), l'**Axes** est la photo à l'intérieur (une zone de tracé, avec ses axes). Un cadre peut contenir plusieurs photos.

**Toujours enseigner l'interface orientée objet, jamais l'interface d'état :**
```python
# ✅ explicite, se compose, fonctionne partout
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(resume["pays"], resume["nombre"])
ax.set_title("Opportunités par pays")

# ❌ plt.bar(...) : agit sur "le graphique courant", invisible et fragile
```
Justification à donner : dès qu'on veut deux graphiques côte à côte, l'interface d'état devient impraticable. Autant prendre la bonne habitude tout de suite.

**seaborn = matplotlib avec les statistiques incluses.** Il fait en une ligne ce qui prend quinze lignes en Matplotlib (moyennes par groupe, intervalles de confiance, facettes). Deux interfaces coexistent :
- l'**API classique** (`sns.barplot`, `sns.histplot`…) — la plus documentée, celle qu'on trouve partout ;
- l'interface **`seaborn.objects`**, fondée sur la grammaire des graphiques, plus proche de ggplot2 :
```python
import seaborn.objects as so

(so.Plot(df, x="pays", y="jours_restants", color="statut")
   .add(so.Dot(), so.Jitter())
   .label(title="Urgence par pays"))
```
Position à tenir : **enseigner l'API classique comme socle**, montrer `objects` comme une ouverture. Les deux sont maintenues ; l'API classique reste largement majoritaire dans la documentation existante.

**Les 5 règles de dataviz honnête** (à afficher au mur) :
1. **Le titre porte le message**, pas la description. « Le Maroc concentre 60 % des opportunités » plutôt que « Opportunités par pays ».
2. **L'axe des barres part de zéro.** Toujours. Le tronquer est le mensonge graphique le plus courant.
3. **Trier** par valeur, pas par ordre alphabétique — sauf si l'ordre a un sens (les mois).
4. **Pas de camembert** au-delà de 3 parts, jamais en 3D. L'œil humain compare mal des angles.
5. **Une question, un graphique.** Si tu ne peux pas dire en une phrase ce que le graphique répond, il n'est pas prêt.

## Plan des slides — Séance 8 (24 slides)

1. **Couverture** + 2. **Frise**.
2. **Le graphique menteur du jour** — un vrai exemple, axe tronqué.
3. **Découper – appliquer – combiner** — schéma en 3 temps avec des cartes de couleur.
4. **`groupby` annoté** — code + tableau de sortie côte à côte.
5. **Plusieurs agrégations d'un coup** — la syntaxe nommée.
6. **⚠️ `reset_index()`** — avant/après, pour comprendre l'index de groupe.
7. **`merge` = RECHERCHEV** — deux tables, une clé, le résultat.
8. **Les 4 jointures** — diagrammes d'ensembles colorés.
9. **⚠️ L'explosion de lignes** — 100 lignes → 4 000, avec le réflexe de vérification.
10. **`pivot_table`** — le tableau croisé dynamique, en face de sa version Excel.
11. **Exercice : 5 questions métier**.
12. **Le cadre et la photo** — Figure vs Axes, illustration.
13. **Le squelette d'un graphique** — les 6 lignes à connaître par cœur.
14. **⚠️ OO plutôt que `plt.`** — deux colonnes, l'une barrée.
15. **Quel graphique pour quelle question ?** — **la slide à imprimer** : comparer → barres ; évoluer → ligne ; répartir → histogramme ; corréler → nuage ; composer → barres empilées.
16. **seaborn en une ligne** — le même graphique en 15 lignes Matplotlib puis en 1 ligne seaborn.
17. **Le catalogue seaborn** — vignettes : `barplot`, `histplot`, `boxplot`, `scatterplot`, `heatmap`, `catplot`.
18. **Les facettes** — un graphique par pays, automatiquement.
19. **`seaborn.objects`** — l'écriture en grammaire des graphiques, présentée comme une ouverture.
20. **Les 5 règles de dataviz honnête** — pleine page.
21. **Avant / après** — le même graphique mal fait puis bien fait.
22. **Exporter proprement** — `dpi`, `bbox_inches="tight"`, PNG vs SVG.
23. **Fil rouge v5 : le tableau de bord cible** — capture des 4 graphiques.
24. **Le chemin parcouru** — de « je n'ai jamais codé » à « je fais parler mes données ».
25. **Quatre chemins pour continuer** — Data/IA, collecter, exposer, automatiser.
26. **Merci** — le dépôt reste ouvert, et Classroom aussi.

## Exercice pratique / Fil rouge v5 — Le tableau de bord

**Énoncé.** À partir du fichier nettoyé en S7, produire une figure unique à quatre panneaux répondant à quatre questions : *combien par pays ? comment se répartit l'urgence ? où en sont les candidatures ? le montant dépend-il du délai ?*

### Corrigé commenté

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")     # un thème lisible, en une ligne
df = pd.read_csv("opportunites_propres.csv", parse_dates=["deadline"])

# Une figure (le cadre) contenant 4 Axes (les photos), en 2 rangées × 2 colonnes.
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("OpportuniTrack — état du carnet", fontsize=16, weight="bold")

# --- 1. Combien par pays ? ------------------------------------------------
par_pays = (df.groupby("pays")
              .size()                       # size() compte les lignes par groupe
              .sort_values(ascending=False) # RÈGLE 3 : on trie par valeur
              .reset_index(name="nombre"))

sns.barplot(data=par_pays, x="nombre", y="pays", ax=axes[0, 0], color="#4C72B0")
# Barres HORIZONTALES : les noms de pays restent lisibles sans rotation.
axes[0, 0].set_title("Le Maroc concentre la majorité des opportunités")
# RÈGLE 1 : le titre porte le message.
axes[0, 0].set_xlabel("Nombre d'opportunités")
axes[0, 0].set_ylabel("")

# --- 2. Répartition des délais --------------------------------------------
sns.histplot(data=df, x="jours_restants", bins=20, ax=axes[0, 1], color="#DD8452")
axes[0, 1].axvline(7, color="red", linestyle="--", label="Seuil d'urgence")
# Une ligne de repère transforme un histogramme en outil de décision.
axes[0, 1].set_title("Un tiers des opportunités expire sous 7 jours")
axes[0, 1].set_xlabel("Jours restants")
axes[0, 1].legend()

# --- 3. Où en sont les candidatures ? -------------------------------------
statuts = df["statut"].value_counts().reset_index()
statuts.columns = ["statut", "nombre"]
sns.barplot(data=statuts, x="statut", y="nombre", ax=axes[1, 0], hue="statut",
            legend=False, palette="viridis")
# hue= est requis pour colorier par catégorie dans les versions récentes de seaborn.
axes[1, 0].set_title("La moitié du carnet n'a pas encore été traitée")

# --- 4. Le montant dépend-il du délai ? -----------------------------------
sns.scatterplot(data=df, x="jours_restants", y="montant",
                hue="pays", alpha=0.6, ax=axes[1, 1])
axes[1, 1].set_title("Aucune relation nette entre montant et délai")
# Un titre qui annonce l'ABSENCE de relation est un titre honnête :
# tous les graphiques ne racontent pas une histoire, et c'est une information.

plt.tight_layout()                   # évite le chevauchement des titres
fig.savefig("dashboard.png", dpi=150, bbox_inches="tight")
# dpi=150 : net à l'impression. bbox_inches="tight" : pas de marge blanche parasite.
plt.show()
```

**Le moment pédagogique clé de la séance** : faire réécrire les quatre titres. La première version des apprenants sera toujours descriptive (« Nombre par pays »). Leur demander : *« qu'est-ce que ce graphique t'apprend, en une phrase ? »* et remplacer le titre par la réponse. C'est un exercice de 5 minutes qui transforme définitivement leur rapport à la visualisation.

### Palier bonus
1. Refaire le panneau 1 avec `seaborn.objects` et comparer la lisibilité du code.
2. Ajouter une évolution mensuelle des deadlines (`df.resample("ME", on="deadline").size()`).
3. Construire une heatmap pays × statut avec `pivot_table` + `sns.heatmap`.
4. Fabriquer une fonction `graphique_par_pays(df, pays)` qui produit une figure paramétrée — et la décorer avec le `@chronometre` de la S6.
5. Exporter en SVG et comparer le rendu après zoom.

## Ressources — Séance 8
| Ressource | Lien | Note |
|---|---|---|
| pandas — Group by (split-apply-combine) | https://pandas.pydata.org/docs/user_guide/groupby.html | — |
| pandas — Merge, join, concatenate | https://pandas.pydata.org/docs/user_guide/merging.html | Les schémas d'ensembles y sont |
| Matplotlib — Quick start guide | https://matplotlib.org/stable/users/explain/quick_start.html | Explique Figure/Axes proprement |
| Matplotlib — Cheatsheets officielles | https://matplotlib.org/cheatsheets/ | **À imprimer et distribuer** |
| Matplotlib — Galerie d'exemples | https://matplotlib.org/stable/gallery/index.html | Chercher visuellement, copier le code |
| seaborn — Tutoriel officiel | https://seaborn.pydata.org/tutorial.html | — |
| seaborn — Interface `objects` | https://seaborn.pydata.org/tutorial/objects_interface.html | Pour le palier bonus |
| seaborn — Galerie | https://seaborn.pydata.org/examples/index.html | — |
| *Fundamentals of Data Visualization* (Wilke) | https://clauswilke.com/dataviz/ | **Gratuit en ligne.** La référence sur le choix du graphique |
| *Storytelling with Data* (Knaflic) | https://www.storytellingwithdata.com/blog | Le blog suffit pour la culture dataviz |
| From Data to Viz | https://www.data-to-viz.com/ | Arbre de décision interactif : quelle donnée → quel graphique |
| Python Graph Gallery | https://python-graphgallery.com/ | Catalogue de code prêt à adapter |

---

## Clôture du cursus — à dire au groupe en fin de S8

Chaque participant sait désormais : structurer du code en objets, lire du Python avancé,
nettoyer un jeu de données réel et en tirer une figure publiable. En huit séances, à partir
de zéro.

**Ce qu'on n'a pas eu le temps de faire — et qui se tient debout tout seul.** Le dire
franchement en dernière slide vaut mieux que de laisser croire que le sujet est clos :

1. **Aller chercher la donnée** — HTTP, APIs publiques, scraping. Jusqu'ici, quelqu'un a
   toujours fourni le CSV.
2. **Exposer son code** — une API REST avec FastAPI, pour qu'un résultat ne vive plus
   seulement dans le notebook de son auteur.
3. **Livrer** — tests, environnement verrouillé, conteneur, déploiement.

Ce sont trois séances entières, déjà écrites et archivées dans `_archive-seances-9-11/`.
Elles peuvent servir de suite, d'atelier ponctuel, ou d'auto-formation guidée pour ceux
qui veulent continuer.

**Les quatre chemins d'après-formation**, à présenter en dernière slide avec une ressource
d'entrée pour chacun :

1. **Data / IA** — scikit-learn, puis PyTorch. Entrée : le cours *Machine Learning* de Kaggle Learn.
2. **Collecter ses propres données** — `requests`, les APIs publiques, BeautifulSoup.
   Entrée : l'annuaire *public-apis* sur GitHub.
3. **Exposer son code** — FastAPI et Pydantic v2. Entrée : le tutoriel officiel FastAPI,
   qui existe en français.
4. **Automatiser son travail** — *Automate the Boring Stuff*, chapitres tableurs, PDF et courriel.

## Ce que le formateur devrait préparer avant le jour J

- [ ] Le dépôt GitHub complet, avec un dossier par séance (énoncé, corrigé, slides, ressources)
- [ ] Les notebooks « point de reprise » — un par séance, avec le code de départ déjà écrit
- [ ] Le jeu de données sale de la S7, généré et testé
- [ ] Les environnements testés sur Windows **et** macOS (les écarts se paient en séance)
- [ ] Le cours Google Classroom créé, un thème par séance, lien Meet généré
- [ ] Les slides à imprimer et afficher : arbre de décision des structures (S3), rituel des
      5 commandes (S7), quel graphique pour quelle question (S8)
- [ ] Un plan B pour les coupures d'internet : les corrigés distribués hors ligne

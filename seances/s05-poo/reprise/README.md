# Séance 5 — Reprise (TD) : penser en objets

**Programmation orientée objet · classes, dataclass, enum, @property.**

On reste dans **VS Code**, sur de vrais fichiers `.py` (comme en séance 4).
Ce dossier est ton terrain d'entraînement pour apprendre à **fabriquer tes
propres types**.

---

## Ouvrir et exécuter

1. **VS Code ▸ Fichier ▸ Ouvrir le dossier…** → choisis **ce dossier** `reprise/`.
2. Interpréteur **Python 3.11** (en bas à droite).
3. Exécute un fichier : le **▶** en haut à droite, **F5**, ou dans le terminal :

```bash
python 00_echauffement.py
```

Chaque fichier commence par une partie **« On regarde ensemble »** (déjà écrite)
puis **« À toi de jouer »** avec des `# TODO`. Corrigés dans
[`../corrige/reprise/`](../corrige/reprise/) — **après** avoir essayé.

## L'ordre des fichiers

| Fichier | Ce qu'on y travaille |
|---|---|
| `00_echauffement.py` | prédis l'output : instance vs classe, `self`, le piège `= []` |
| `01_classe_a_la_main.py` | écrire une classe de zéro : `__init__`, `self`, méthodes |
| `02_dataclass_enum_property.py` | `@dataclass`, `StrEnum`, `@property`, `default_factory` |
| `03_composition_budget.py` | un `Budget` qui **a des** `Depense` — pont vers le devoir |

## Le vocabulaire du jour

- **classe** = le moule ; **instance** = le gâteau sorti du moule.
- **`self`** = « moi-même » : `self.montant` se lit « mon montant ».
- **méthode** = une fonction rangée dans une classe (un **verbe** : `ajouter`,
  `sauvegarder`).
- **`@property`** = un attribut qui se **calcule** à la lecture (sans `()`).

## Bloqué ?

Colle **le message d'erreur complet en texte** (jamais une capture) dans
Google Classroom. La dernière ligne du traceback dit ce qui ne va pas.

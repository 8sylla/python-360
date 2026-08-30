# Séance 4 — Reprise (TD) : on quitte le navigateur

**Fabriquer ses outils · Fonctions, modules, fichiers, erreurs.**

À partir d'aujourd'hui, on ne travaille plus dans Colab mais dans **VS Code**,
sur de **vrais fichiers `.py`**, avec un **vrai terminal** et un **débogueur**.
Ce dossier est ton terrain d'entraînement pour la séance.

---

## 1. Ouvrir ce dossier dans VS Code

1. **VS Code ▸ Fichier ▸ Ouvrir le dossier…** et choisis **ce dossier
   `reprise/`** (pas un fichier seul : un *dossier*). C'est important — les
   imports d'un fichier vers un autre ne marchent que si VS Code est ouvert
   sur le dossier qui les contient.
2. En bas à droite de la fenêtre, clique sur la version de Python et choisis
   **Python 3.11** (l'interpréteur de la formation).
3. Si VS Code te propose d'installer l'extension **Python** de Microsoft :
   accepte. C'est elle qui colore le code, exécute, et débogue.

## 2. Exécuter un fichier

Ouvre `00_echauffement.py`, puis, au choix :

- le **triangle ▶** en haut à droite (« Run Python File ») ;
- ou la touche **F5** (« Exécuter et déboguer ») ;
- ou, dans le terminal intégré (**Terminal ▸ Nouveau terminal**) :

```bash
python 00_echauffement.py
```

La sortie s'affiche dans le panneau **Terminal**, en bas. C'est là que ton
programme te parle, et c'est là que tu colles les erreurs pour les lire.

## 3. Le débogueur — le point d'arrêt (à essayer en fin de séance)

C'est le super-pouvoir de VS Code, celui que Colab n'a pas :

1. Clique dans la **marge**, juste à gauche d'un numéro de ligne. Un **point
   rouge** apparaît : c'est un *point d'arrêt* (*breakpoint*).
2. Lance avec **F5**. Le programme s'arrête **sur cette ligne, avant** de
   l'exécuter.
3. À gauche, le panneau **Variables** montre le contenu de chaque boîte en
   direct. Avance ligne par ligne avec **F10**.

> Plus besoin de semer des `print()` partout pour comprendre un bug : tu
> **vois** ce que la machine voit.

---

## 4. L'ordre des fichiers

Fais-les dans l'ordre. Chaque fichier commence par une partie
**« On regarde ensemble »** (déjà écrite, à lire et exécuter) puis une partie
**« À toi de jouer »** avec des `# TODO` à compléter.

| Fichier | Ce qu'on y travaille |
|---|---|
| `00_echauffement.py` | Prédis l'output : `return` vs `print`, défauts, portée |
| `01_fonctions_fameuses.py` | FizzBuzz, pourboire, convertisseur — en fonctions |
| `outils_budget.py` | **Un module** : des outils à importer (pas à exécuter) |
| `02_utiliser_le_module.py` | `import`, `from … import`, `if __name__ == "__main__"` |
| `03_fichiers_et_erreurs.py` | `pathlib`, `with open()`, JSON, `try / except` |

Le corrigé complet est dans [`../corrige/reprise/`](../corrige/reprise/) —
à ouvrir **après** avoir essayé.

## 5. Bloqué ?

Colle **le message d'erreur complet en texte** (jamais une capture) dans le
flux du cours sur Google Classroom. La **dernière ligne** d'un traceback dit
toujours ce qui ne va pas.

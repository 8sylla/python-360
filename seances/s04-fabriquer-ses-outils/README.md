# Séance 4 — Fabriquer ses outils

**samedi 29 août 2026 · 3 h**

> **La bascule vers le local.** À partir de cette séance, on quitte Google
> Colab pour **VS Code** : de vrais fichiers `.py`, un vrai terminal, un
> débogueur. Voir *Travailler en local* dans le [README racine](../../README.md).

## Au programme

- Fonctions : paramètres, `return`, docstring, portée
- `return` contre `print` — la confusion la plus coûteuse
- Modules, `import`, et `if __name__ == "__main__"`
- Fichiers : `pathlib`, `with open()`, JSON et CSV (`DictReader`/`DictWriter`)
- `try` / `except`, et pourquoi jamais d'`except` nu
- `match` / `case` (Python 3.10+)

## Ce que contient ce dossier

| Dossier / fichier | Ce que c'est | Quand |
|---|---|---|
| [`reprise/`](reprise/) | Le **TD** : un dossier VS Code de fichiers `.py` à ouvrir et compléter en séance | la veille |
| [`devoir-monbudget/`](devoir-monbudget/) | Le **devoir** : squelette du projet MonBudget v1 à finir chez soi | en séance |
| [`corrige/`](corrige/) | Les **corrigés** (TD + notes) | après la séance |

Le corrigé de référence du projet MonBudget v1 est publié dans
[`fil-rouge/v1-cli/`](../../fil-rouge/v1-cli/).

## Démarrer (VS Code)

1. Récupère le dépôt en local (une seule fois) :

   ```bash
   git clone https://github.com/8sylla/python-360.git
   cd python-360
   ```

2. **VS Code ▸ Fichier ▸ Ouvrir le dossier…** puis choisis le dossier du TD :
   [`seances/s04-fabriquer-ses-outils/reprise/`](reprise/). Suis son
   [README](reprise/README.md) — il explique tout : interpréteur, exécution,
   et le **point d'arrêt** du débogueur.

3. En bas à droite de VS Code, choisis l'interpréteur **Python 3.11**.

## Bloqué ?

Colle **le message d'erreur complet en texte** — jamais une capture — dans le
flux du cours sur Google Classroom. La dernière ligne d'un traceback dit
toujours ce qui ne va pas.

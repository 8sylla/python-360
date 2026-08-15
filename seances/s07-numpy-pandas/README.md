# Séance 7 — NumPy & pandas

**mercredi 9 septembre 2026 · 3 h**

## Au programme

- Pourquoi un `ndarray` est plus rapide qu'une liste
- Vectorisation, masques booléens, broadcasting
- `read_csv`, et le rituel des cinq commandes d'inspection
- `.loc` contre `.iloc`
- Nettoyer : manquants, doublons, types, textes, dates
- Le Copy-on-Write de pandas 3.0 — on réaffecte, on ne modifie pas

## Ce que contient ce dossier

| Fichier | Quand il arrive |
|---|---|
| `reprise.ipynb` | la veille de la séance — le code de départ fonctionne déjà |
| `corrige/` | après la séance |

Le dossier est vide tant que la séance n'a pas eu lieu. C'est normal.

## Ouvrir le notebook

Sans rien installer, directement dans Colab :

```
https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s07-numpy-pandas/reprise.ipynb
```

Premier réflexe une fois ouvert : **Fichier ▸ Enregistrer une copie dans
Drive**. Sans ça, tu travailles dans un fichier en lecture seule et tout
disparaît à la fermeture.

## Bloqué ?

Colle **le message d'erreur complet en texte** — jamais une capture — dans
le flux du cours sur Google Classroom. La dernière ligne d'un traceback dit
toujours ce qui ne va pas.

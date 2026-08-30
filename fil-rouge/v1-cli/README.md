# `MonBudget` — v1-cli

**Séance 4 · L'application en ligne de commande.**

La première version « pour de vrai » de MonBudget : un programme dans de vrais
fichiers `.py`, qui garde tes dépenses sur le disque entre deux lancements.

Ce dossier est la **version de référence** (le corrigé du devoir de la séance 4).
Le squelette à compléter est dans
[`../../seances/s04-fabriquer-ses-outils/devoir-monbudget/`](../../seances/s04-fabriquer-ses-outils/devoir-monbudget/).

---

## Ce que fait v1

- **Ajouter** une dépense (titre, catégorie, montant) au clavier ;
- **Afficher** le carnet, trié par montant, avec le total ;
- **Filtrer** par catégorie ;
- **Quitter** proprement.

Les dépenses **survivent à la fermeture** : elles sont écrites en **JSON** dans
`depenses.json`, créé automatiquement au premier ajout.

## Les deux modules

| Fichier | Rôle |
|---|---|
| `stockage.py` | Lire / écrire le fichier JSON (`charger`, `sauvegarder`) |
| `tracker.py` | Le programme : menu, saisie, affichage, filtre |

`tracker.py` **importe** `stockage` : la logique de fichier est rangée d'un
côté, le programme de l'autre. `main()` ne fait qu'orchestrer — c'est la
première marche vers la POO de la séance 5.

## Lancer

```bash
cd fil-rouge/v1-cli
python tracker.py
```

> Envie de partir d'un carnet déjà rempli ? Copie l'exemple :
> `cp depenses.example.json depenses.json` (le vrai `depenses.json` n'est pas
> versionné — il t'appartient).

## Le format de stockage

```json
[
  { "titre": "Loyer", "categorie": "Logement", "montant": 850.0 },
  { "titre": "Pass Navigo", "categorie": "Transport", "montant": 86.4 }
]
```

## Ce qui manque encore (et prépare la suite)

Toutes les fonctions se passent la **même liste** `depenses` en argument, en
la trimballant partout. En **séance 5**, une dépense deviendra un objet
`Depense`, et le carnet une classe `Budget` qui portera ses propres méthodes —
c'est la refactorisation `v2-poo`.

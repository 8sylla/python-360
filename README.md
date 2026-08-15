# python-360

Formation Python 360° — Commission Scientifique nationale, **ASEGUIM**.

Neuf séances en ligne, du 15 août au 12 septembre 2026.

**Portail :** <https://8sylla.github.io/python-360/>

---

## Le programme

| # | Séance | Date | Durée |
|---|---|---|---|
| 0 | Kit de démarrage | sam. 15 août | 2 h 30 |
| 1 | Parler à la machine | mer. 19 août | 3 h |
| 2 | Décider et répéter | sam. 22 août | 3 h |
| 3 | Ranger l'information | mer. 26 août | 3 h |
| 4 | Fabriquer ses outils | sam. 29 août | 3 h |
| 5 | Programmation orientée objet | mer. 2 sept. | 3 h |
| 6 | Sous le capot | sam. 5 sept. | 3 h |
| 7 | NumPy & pandas | mer. 9 sept. | 3 h |
| 8 | Faire parler les données | sam. 12 sept. | 3 h |

Le détail de chaque séance est dans le README de son dossier,
sous [`seances/`](seances/).

---

## Ouvrir un notebook

Sans rien installer, dans Google Colab :

```
https://colab.research.google.com/github/8sylla/python-360/blob/main/seances/s01-parler-a-la-machine/reprise.ipynb
```

Premier réflexe : **Fichier ▸ Enregistrer une copie dans Drive**.

## Travailler en local (à partir de la séance 4)

```bash
git clone https://github.com/8sylla/python-360.git
cd python-360
uv sync
```

---

## Organisation

```
portail/     le site public, déployé sur GitHub Pages
seances/     un dossier par séance : notebook de reprise et corrigé
fil-rouge/   MonBudget, une version par étape du parcours
data/        les jeux de données des séances 7 et 8
```

Les dossiers se remplissent séance après séance. S'ils sont vides, c'est que
la séance n'a pas encore eu lieu.

---

## Le fil rouge

`MonBudget`, un suivi de dépenses personnelles, construit de la séance 1 à
la séance 8. Voir [`fil-rouge/`](fil-rouge/).

---

## Versions

L'écosystème a bougé début 2026 : beaucoup de tutoriels encore bien
référencés donnent du code qui ne marche plus.

| Outil | Version | À savoir |
|---|---|---|
| Python | 3.12 minimum | numpy 2.5 ne descend pas plus bas |
| pandas | 3.0+ | Copy-on-Write : l'affectation chaînée lève une erreur |
| NumPy | 2.5+ | API 2.x |
| Matplotlib | 3.10+ | interface orientée objet (`fig, ax`) |
| seaborn | 0.13+ | `hue=` requis pour colorier par catégorie |

Vérifier la date d'un tutoriel avant de le suivre.

---

## Licence

Voir [`LICENSE`](LICENSE).

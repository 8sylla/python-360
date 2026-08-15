# Formation Python 360° — Guide du formateur
## ARC 1 : La rampe de lancement (Séances 0 à 4)

**Format** : 8 séances de 3h · **Environnement** : Google Colab (S1→S3) puis VS Code (S4→S8) · **Fil rouge** : `OpportuniTrack`
**Cible Python** : 3.14.x (dernière stable). 3.13 accepté. Plancher absolu : 3.10 (pour `match-case`).

---

# Boîte à outils transversale du formateur

## Les 5 règles d'or de l'Arc 1

1. **Jamais de mot de jargon sans son analogie dans la même phrase.** « Une variable, c'est-à-dire une boîte étiquetée. »
2. **Personne ne regarde le formateur coder pendant plus de 8 minutes d'affilée.** Au-delà, l'attention des débutants décroche.
3. **L'erreur est le programme de la séance, pas un accident.** Le formateur provoque volontairement 2 à 3 erreurs par séance et les lit à voix haute.
4. **Un débutant qui ne voit rien s'afficher croit qu'il a échoué.** Tout exercice de l'Arc 1 doit produire une sortie visible.
5. **Différenciation systématique** : exercice socle (tous) + palier bonus (profils techniques) pendant que le formateur circule.

## Rituels de séance

| Moment | Rituel | Durée |
|---|---|---|
| Ouverture | « L'erreur du jour » : un traceback projeté, on le décode ensemble | 5 min |
| Milieu | « Pair programming » : binômes débutant/technique, un pilote + un copilote, on échange à mi-parcours | — |
| Clôture | « Une ligne, un mot » : chacun écrit dans le chat un mot retenu | 5 min |

## Charte anti-décrochage

- Aucun exercice n'exige d'avoir réussi le précédent : le formateur distribue un **notebook « point de reprise »** avec le code de départ déjà écrit.
- Un cours **Google Classroom** dont le flux sert de fil `SOS erreurs` : on y colle **le message d'erreur complet en texte**, jamais une capture floue.
- Un dépôt GitHub `formation-python/` avec un dossier par séance : `enonce.ipynb`, `corrige.ipynb`, `slides.pdf`, `ressources.md`.

---
---

# SÉANCE 0 — Kit de démarrage
### *(asynchrone, ~45 min, à réaliser avant J1)*

**Raison d'être** : la séance 1 doit être une séance de code, pas une séance de dépannage. 100 % des formations Python débutants perdent 45 minutes sur l'installation le premier jour. On les supprime.

## Objectifs pédagogiques
À l'issue du kit, l'apprenant est capable de :
1. Ouvrir un notebook Google Colab et exécuter une cellule de code.
2. Accéder au dépôt GitHub de la formation.
3. (Optionnel, pour la S4) Avoir Python et VS Code installés sur sa machine.

## Contenu du pack (envoyé par mail + canal)

**A. Une vidéo de 6 minutes** (écran enregistré, sans montage) : « J'ouvre Colab, j'exécute ma première ligne. »

**B. Une fiche PDF d'une page — « Les 3 clics » :**
1. Aller sur `colab.research.google.com` → *Nouveau notebook*.
2. Taper `print("Bonjour")` dans la cellule.
3. Appuyer sur `Maj + Entrée`. → Si « Bonjour » s'affiche, tu es prêt.

**C. Un questionnaire de positionnement (5 questions, 2 min)** — sert à composer les binômes :
- As-tu déjà écrit du code ? (jamais / un peu de HTML ou Excel / oui, un autre langage)
- Es-tu à l'aise avec un tableur (formules, tri, filtres) ? (0 à 5)
- Ton objectif principal ? (automatiser mon travail / analyser des données / créer une appli / curiosité)
- Ton système ? (Windows / macOS / Linux)
- Ton débit internet est-il stable ? (détermine qui doit basculer en local plus tôt)

**D. Installation locale (non bloquante pour S1-S3, requise pour S4)**
- Python 3.14.x depuis `python.org/downloads` — **Windows : cocher impérativement « Add python.exe to PATH »**.
- VS Code depuis `code.visualstudio.com` + extension officielle **Python** (Microsoft) + extension **Jupyter**.
- Vérification : ouvrir un terminal et taper `python --version` (Windows) ou `python3 --version` (macOS/Linux).

**E. Compte GitHub** créé, pseudo envoyé au formateur.

## Idées de slides (support PDF de 7 pages)
1. **Couverture** — Titre de la formation, nom du formateur, dates, logo de la communauté.
2. **La promesse** — « En 8 séances, tu passes de "je n'ai jamais codé" à "je fais parler mes données". » Visuel : la frise des 8 séances.
3. **Ce dont tu as besoin** — un navigateur, un compte Google. C'est tout (pour les 3 premières séances).
4. **Les 3 clics** — 3 captures d'écran annotées de Colab.
5. **Si tu veux prendre de l'avance** — installation locale, captures Windows/macOS.
6. **Où demander de l'aide** — lien du canal, règle « colle ton erreur en texte, pas en photo ».
7. **Le questionnaire** — QR code + lien.

## Ressources — Séance 0
| Ressource | Lien | Pourquoi |
|---|---|---|
| Téléchargements officiels Python | https://www.python.org/downloads/ | Source unique de vérité pour les versions |
| Google Colab — notebook d'accueil | https://colab.research.google.com/ | Zéro installation |
| Colab — FAQ officielle | https://research.google.com/colaboratory/faq.html | Limites, GPU, durée de session |
| VS Code — Tutoriel Python officiel | https://code.visualstudio.com/docs/python/python-tutorial | Le parcours d'installation de référence |
| Extension Python (Microsoft) | https://marketplace.visualstudio.com/items?itemName=ms-python.python | À installer, pas une alternative |
| GitHub — Hello World | https://docs.github.com/en/get-started/start-your-journey/hello-world | Créer son premier dépôt |

---
---

# SÉANCE 1 — Parler à la machine
### *Découverte, algorithmique, variables, types, entrées/sorties*

> **Promesse affichée en début de séance** : « Dans 3 heures, tu auras écrit un programme qui te pose des questions et te répond. »

## Objectifs pédagogiques
À la fin de la séance, l'apprenant est capable de :
1. **Expliquer** avec ses propres mots ce qu'est un programme et ce que fait l'interpréteur Python.
2. **Exécuter** une cellule dans Google Colab et interpréter ce qui s'affiche.
3. **Décomposer** un problème simple en une suite d'étapes ordonnées (algorithme), sur papier.
4. **Utiliser** `print()`, les variables, les 4 types de base (`str`, `int`, `float`, `bool`) et les opérateurs arithmétiques.
5. **Récupérer** une saisie utilisateur avec `input()` et la **convertir** dans le bon type.
6. **Reconnaître** trois erreurs classiques : `SyntaxError`, `NameError`, `TypeError`.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–15 | Accueil | Plénière | Tour de table express (prénom + « ce que j'aimerais automatiser »). Présentation de la promesse, du fil rouge, de la charte « l'erreur est normale ». |
| 15–35 | **Théorie 1** : c'est quoi programmer ? | Plénière | Analogie de la recette. Ordinateur = exécutant très rapide et très bête. Langage machine → langage Python → interpréteur. |
| 35–50 | **Atelier débranché** | Binômes, papier | « Écris la recette pour qu'un robot prépare un thé. » Le formateur joue le robot et exécute *littéralement* : révèle l'ambiguïté, l'ordre, l'implicite. |
| 50–60 | **Démo Colab** | Plénière | Créer un notebook, cellule de code vs cellule texte, exécuter, l'ordre d'exécution, le crayon d'enregistrement. |
| 60–80 | **Pratique 1** | Individuel | Faire afficher son prénom, un calcul, un texte multiligne. Provoquer volontairement une `SyntaxError` (guillemet manquant) et la lire. |
| 80–90 | **PAUSE** | — | — |
| 90–115 | **Théorie 2** : variables et types | Plénière + live coding | Boîte étiquetée, affectation, réaffectation, nommage. Les 4 types. `type()`. Opérateurs `+ - * / // % **`. |
| 115–130 | **Théorie 3** : dialoguer | Plénière + live coding | `input()`, le piège du texte, `int()` / `float()`, f-strings. |
| 130–160 | **Pratique 2 — Exercice principal** | Binômes | Le « Calculateur de candidature » (ci-dessous). |
| 160–172 | **Mise en commun** | Plénière | Deux binômes projettent leur code. Le formateur corrige en direct, sans jamais dire « c'est faux » : « qu'est-ce que la machine a compris, elle ? ». |
| 172–180 | **Clôture** | Plénière | Fil rouge du jour, devoir, teaser S2 (« la semaine prochaine, le programme prendra des décisions tout seul »). |

## Concepts clés — expliqués simplement

**Le programme = une recette.** Une recette de cuisine est une suite d'instructions dans un ordre précis. Python lit ta recette **ligne par ligne, de haut en bas**, sans jamais anticiper ni deviner. C'est un exécutant parfaitement obéissant et parfaitement stupide : si tu oublies « allumer le four », il servira une pâte crue sans se plaindre.

**La variable = une boîte étiquetée.** `age = 25` signifie : « prends une boîte, colle l'étiquette *age* dessus, mets 25 dedans ». Trois conséquences à faire dire par le groupe :
- Le `=` n'est **pas** un égal mathématique, c'est une flèche « on range dans ». `x = x + 1` est absurde en maths, normal ici.
- Si tu remets quelque chose dans la boîte, l'ancien contenu est perdu.
- Le nom de l'étiquette est libre… mais un bon nom est un cadeau que tu fais à toi-même dans deux semaines. `n` vs `nombre_de_candidatures`.

**Le type = la nature du contenu.** On ne fait pas les mêmes gestes avec du texte et avec un nombre.
- `"5" + "3"` donne `"53"` (on colle deux textes)
- `5 + 3` donne `8` (on additionne deux nombres)
- `"5" + 3` → **TypeError**, Python refuse de deviner.

**Le piège n°1 de tout débutant** : `input()` rend **toujours du texte**, même si l'utilisateur tape 42. D'où la conversion : `age = int(input("Ton âge : "))`.

**Lire un message d'erreur.** À projeter en grand et à décortiquer de bas en haut :
```
Traceback (most recent call last):
  File "candidature.py", line 4, in <module>
    total = nb_offres + "3"
            ~~~~~~~~~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
- **Dernière ligne** = ce qui ne va pas.
- **Ligne du milieu** = où ça s'est passé (numéro de ligne).
- Depuis Python 3.11+, le petit `^~~~` pointe même le morceau fautif.

## Plan des slides — Séance 1 (18 slides)

1. **Couverture** — « Séance 1 : Parler à la machine ». Sous-titre : *aucun prérequis*.
2. **La promesse du jour** — capture d'écran du programme final qui dialogue.
3. **Le parcours en 11 étapes** — frise, la S1 est surlignée. (Slide récurrente à chaque séance.)
4. **La règle du jeu** — « L'erreur n'est pas un échec, c'est un message. » Trois engagements du formateur.
5. **C'est quoi un programme ?** — À gauche une recette de cuisine, à droite le même code Python. Mise en miroir visuelle.
6. **L'ordinateur est bête** — illustration : « Prépare un thé » → le robot verse l'eau sur le sachet resté dans sa boîte.
7. **Atelier : la recette du robot** — la consigne, 8 minutes au chrono.
8. **Ce qu'on vient de découvrir** — un algorithme = étapes ordonnées, non ambiguës, finies.
9. **Notre atelier : Google Colab** — capture annotée en 4 zones (cellule code, bouton exécuter, sortie, menu).
10. **Ma première ligne** — `print("Bonjour")` en très gros. Rien d'autre sur la slide.
11. **La variable = une boîte étiquetée** — schéma : boîte, étiquette `prenom`, contenu `"Awa"`.
12. **Attention : `=` n'est pas égal** — animation en 2 temps : `x = 5` puis `x = x + 1` → `6`.
13. **Les 4 types de base** — tableau : `str` (texte), `int` (entier), `float` (décimal), `bool` (vrai/faux) + un exemple concret chacun.
14. **Le piège des types** — `"5" + "3" = "53"` vs `5 + 3 = 8`. Grand visuel.
15. **Parler à l'utilisateur** — `input()` + le rappel « ça sort toujours en texte » (icône panneau attention).
16. **Les f-strings** — `f"Bonjour {prenom}, tu as {age} ans"`. Coloriser les accolades.
17. **Exercice : le calculateur de candidature** — l'énoncé + la sortie attendue en capture.
18. **Ce qu'on a appris / Pour la prochaine fois** — 5 puces + le devoir.

## Exercice pratique — « Le calculateur de candidature »

**Énoncé (niveau socle).** Écris un programme qui :
1. demande le prénom de l'utilisateur ;
2. demande combien d'offres il a repérées cette semaine ;
3. demande combien de candidatures il a envoyées ;
4. affiche un récapitulatif propre avec le nombre d'offres restantes à traiter et le taux de candidature en pourcentage.

**Sortie attendue :**
```
Bonjour Awa !
Tu as repéré 12 offres et envoyé 5 candidatures.
Il te reste 7 offres à traiter.
Taux de candidature : 41.7 %
```

### Corrigé commenté

```python
# 1) On récupère le prénom. input() renvoie du TEXTE : parfait, un prénom est du texte.
prenom = input("Quel est ton prénom ? ")

# 2) et 3) Ici on attend des NOMBRES. input() donnant du texte, on convertit avec int().
#    Sans le int(), la ligne 8 tenterait de soustraire deux textes -> TypeError.
nb_offres = int(input("Combien d'offres as-tu repérées ? "))
nb_candidatures = int(input("Combien de candidatures as-tu envoyées ? "))

# 4) Un calcul simple. Le résultat est rangé dans une nouvelle boîte.
offres_restantes = nb_offres - nb_candidatures

# 5) La division / donne toujours un float (nombre à virgule), même sur 10 / 2.
#    On multiplie par 100 pour obtenir un pourcentage.
taux = nb_candidatures / nb_offres * 100

# 6) L'affichage. Le f devant les guillemets active les f-strings :
#    tout ce qui est entre { } est remplacé par la valeur de la variable.
print(f"Bonjour {prenom} !")
print(f"Tu as repéré {nb_offres} offres et envoyé {nb_candidatures} candidatures.")
print(f"Il te reste {offres_restantes} offres à traiter.")

# 7) :.1f est un "format" : affiche le nombre avec 1 chiffre après la virgule.
#    Sans lui, on obtiendrait 41.666666666666664 -> illisible.
print(f"Taux de candidature : {taux:.1f} %")
```

**Points d'attention à commenter à l'oral :**
- Le `f` collé au guillemet ouvrant : l'oubli le plus fréquent, le résultat affiche littéralement `{prenom}`.
- `:.1f` est le premier « format » rencontré. Ne pas l'expliquer en profondeur, le donner comme un outil.
- Si l'utilisateur saisit `0` offre, le programme plante (`ZeroDivisionError`). **Ne pas le corriger aujourd'hui** : le noter au tableau comme une dette, on la remboursera en S2 avec `if`. C'est un excellent accroche pour la séance suivante.

### Palier bonus (profils techniques)
1. Gérer le cas `nb_offres == 0` sans utiliser `if` (indice : impossible proprement → c'est le but, ça motive la S2).
2. Ajouter le nombre de jours restants avant une date limite, avec le module `datetime` :
   ```python
   from datetime import date
   deadline = date(2026, 12, 31)
   print(f"Jours restants : {(deadline - date.today()).days}")
   ```
3. Afficher le prénom en majuscules et sans espaces parasites : `prenom.strip().upper()`.

## Fil rouge — `OpportuniTrack` v0.1
> « La carte d'opportunité »

Le programme demande à l'utilisateur les informations d'**une** opportunité (titre, organisme, pays, date limite) et affiche une fiche formatée :

```python
titre = input("Titre de l'opportunité : ")
organisme = input("Organisme : ")
pays = input("Pays : ")
deadline = input("Date limite (JJ/MM/AAAA) : ")

print("=" * 40)          # * répète le texte 40 fois : une ligne de séparation
print(f"  {titre.upper()}")
print(f"  Organisme : {organisme}")
print(f"  Pays      : {pays}")
print(f"  Deadline  : {deadline}")
print("=" * 40)
```

**Ce que ça prépare** : en S2 on vérifiera la date, en S3 on stockera plusieurs opportunités, en S4 on les sauvegardera dans un fichier.

## Devoir (20 min)
Reprendre la fiche d'opportunité et y ajouter deux informations de son choix. Poster une capture de la sortie dans le canal.

## Ressources — Séance 1
| Ressource | Lien | Note |
|---|---|---|
| Tutoriel officiel Python (en français) | https://docs.python.org/fr/3/tutorial/ | Chapitres 1 à 3. La référence, gratuite et traduite |
| *Automate the Boring Stuff*, 3e éd. (gratuit en ligne) | https://automatetheboringstuff.com/3e/ | Chapitre 1 « Python Basics ». La 3e édition est la version à jour |
| *Think Python*, 3e éd. | https://allendowney.github.io/ThinkPython/ | Chapitres 1-2, notebooks Colab intégrés — idéal pour ce public |
| Real Python — Variables | https://realpython.com/python-variables/ | Explications visuelles |
| Real Python — f-strings | https://realpython.com/python-f-strings/ | Couvre aussi les nouveautés 3.12+ |
| Colab — Bienvenue | https://colab.research.google.com/notebooks/intro.ipynb | À dupliquer et distribuer |
| PSF — Beginner's Guide | https://wiki.python.org/moin/BeginnersGuide/NonProgrammers | Curation officielle pour non-programmeurs |
| Exercism — parcours Python | https://exercism.org/tracks/python | Exercices corrigés par des mentors humains, gratuit |

---
---

# SÉANCE 2 — Décider et répéter
### *Booléens, conditions, boucles, lecture d'erreurs*

> **Promesse** : « Aujourd'hui, ton programme arrête d'exécuter bêtement : il choisit, et il répète. »

## Objectifs pédagogiques
1. **Construire** une expression booléenne avec `== != < > <= >=` et `and / or / not`.
2. **Écrire** une structure `if / elif / else` correctement indentée.
3. **Distinguer** les cas d'usage de `for` (je sais combien de fois) et `while` (je répète tant que).
4. **Utiliser** `range()`, un compteur et un accumulateur.
5. **Diagnostiquer** seul une `IndentationError` et une boucle infinie.
6. **Traduire** une règle métier écrite en français en une condition Python.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–10 | Rituel « l'erreur du jour » | Plénière | Le `ZeroDivisionError` laissé en dette en S1. Résolution en direct à la fin du bloc théorie 1. |
| 10–35 | **Théorie 1** : les booléens et `if` | Plénière + live coding | Vrai/Faux, comparateurs, `if/elif/else`. L'indentation. |
| 35–60 | **Pratique 1** | Individuel | 6 micro-exercices en escalier (majeur/mineur, mention d'un score, éligibilité). |
| 60–80 | **Théorie 2** : `and / or / not` et l'imbrication | Plénière | Tables de vérité illustrées. Quand imbriquer, quand combiner. |
| 80–90 | **PAUSE** | — | — |
| 90–115 | **Théorie 3** : les boucles | Plénière + live coding | `for` sur un nombre et sur un texte, `range()`, `while`, compteur, accumulateur, `break` / `continue`. |
| 115–150 | **Pratique 2 — Exercice principal** | Binômes | Le jeu du nombre mystère (ci-dessous). |
| 150–165 | **Défi collectif** | Plénière | Le formateur écrit une boucle infinie en direct, laisse tourner, demande au groupe de trouver pourquoi. |
| 165–172 | **Fil rouge** | Individuel | Filtrage d'une opportunité. |
| 172–180 | **Clôture** | Plénière | Bilan, devoir, teaser S3. |

## Concepts clés — expliqués simplement

**Le booléen = une réponse par oui ou non.** Il n'existe que deux valeurs : `True` et `False`. Toute condition est ramenée à ça. `12 > 5` n'affiche pas « oui », ça **vaut** `True`.

**`==` contre `=`.** Un seul égal : « je range dans la boîte ». Deux égaux : « est-ce que c'est pareil ? ». C'est la deuxième erreur la plus fréquente de la formation ; l'annoncer explicitement fait gagner une heure de dépannage.

**Le `if` = un panneau de signalisation.** Le programme roule tout droit ; au panneau, il regarde la condition et prend une route. `elif` = « sinon, essaie plutôt cette route ». `else` = « sinon, dans tous les autres cas ». **Une seule branche est empruntée**, jamais deux.

**L'indentation = les tiroirs.** En Python, le décalage de 4 espaces n'est pas de la décoration : c'est ce qui dit « cette ligne est *à l'intérieur* du if ». Analogie : les paragraphes en retrait d'un contrat, qui appartiennent à l'article au-dessus.

**`for` contre `while`.**
- `for` = « pour chacun des éléments de… » → *je connais d'avance le nombre de tours.* Distribuer un paquet de 12 tracts : 12 tours.
- `while` = « tant que… » → *je ne sais pas combien de tours.* Remplir un seau : tant qu'il n'est pas plein.
- **Le danger du `while`** : si rien ne change à l'intérieur, il tourne pour l'éternité. Toujours se demander : « qu'est-ce qui, dans cette boucle, va finir par rendre la condition fausse ? »

**Le compteur et l'accumulateur.** Deux motifs qui reviendront jusqu'à la fin de la formation :
```python
total = 0                # l'accumulateur commence vide
for prix in [10, 25, 5]:
    total = total + prix # à chaque tour, on ajoute au total
```

## Plan des slides — Séance 2 (20 slides)

1. **Couverture** — « Séance 2 : Décider et répéter ».
2. **La frise** — S2 surlignée.
3. **L'erreur du jour** — le traceback `ZeroDivisionError` de la semaine dernière, en grand.
4. **Rappel express S1** — 4 icônes : print, variable, type, input.
5. **Vrai ou faux** — la slide ne contient que `True` et `False`.
6. **Les comparateurs** — tableau : `==`, `!=`, `<`, `>`, `<=`, `>=` avec un exemple parlant chacun.
7. **⚠️ `=` vs `==`** — pleine page, deux colonnes, code rouge / code vert.
8. **Le panneau de signalisation** — schéma de l'aiguillage `if / elif / else`.
9. **Anatomie d'un `if`** — le code annoté par des flèches : les deux-points, l'indentation, le bloc.
10. **L'indentation, ce n'est pas décoratif** — le même code avec et sans indentation, et l'`IndentationError` produite.
11. **Combiner : `and`, `or`, `not`** — trois phrases en français traduites en Python.
12. **Table de vérité illustrée** — pictogrammes plutôt que 0/1.
13. **Exercices en escalier** — les 6 énoncés.
14. **Répéter : deux façons** — deux colonnes, `for` (je sais combien) / `while` (je ne sais pas).
15. **`for` et `range()`** — visualisation de `range(5)` → 0,1,2,3,4. Insister : **ça commence à 0 et ça s'arrête avant 5**.
16. **Compteur et accumulateur** — animation en 3 étapes du total qui grossit.
17. **⚠️ La boucle infinie** — le code fautif + le bouton stop de Colab entouré en rouge.
18. **`break` et `continue`** — analogie : sortir de la file / passer son tour.
19. **Exercice : le nombre mystère** — l'énoncé + un exemple de partie.
20. **Bilan / devoir / teaser**.

## Exercice pratique — « Le nombre mystère »

**Énoncé (socle).** L'ordinateur choisit un nombre entre 1 et 100. Le joueur propose des nombres ; le programme répond « trop grand » ou « trop petit », et le félicite quand il trouve, en indiquant en combien de coups.

### Corrigé commenté

```python
import random  # module de la bibliothèque standard : rien à installer

# randint(1, 100) tire un entier au hasard, bornes INCLUSES (contrairement à range).
secret = random.randint(1, 100)

essais = 0          # le compteur : combien de propositions ont été faites
trouve = False      # un booléen "drapeau" : passera à True quand on aura gagné

print("J'ai choisi un nombre entre 1 et 100. À toi de le trouver !")

# On répète TANT QUE le drapeau est faux.
# La condition finira par devenir fausse car "trouve" changera dans la boucle.
while not trouve:
    proposition = int(input("Ta proposition : "))
    essais = essais + 1   # équivaut à : essais += 1

    if proposition < secret:
        print("Trop petit !")
    elif proposition > secret:
        print("Trop grand !")
    else:
        # Ce else n'est atteint que si ce n'est ni plus petit ni plus grand :
        # donc c'est forcément égal.
        trouve = True   # on lève le drapeau -> la boucle s'arrêtera au prochain test
        print(f"Bravo ! Trouvé en {essais} essais.")
```

**Points d'attention à l'oral :**
- `while not trouve` se lit « tant que ce n'est pas trouvé ». Faire lire la ligne à voix haute en français : la traduction littérale est la meilleure aide mémoire.
- Le `else` sans condition : demander au groupe *pourquoi* on peut être sûr que c'est l'égalité.
- Montrer la variante `while True: ... break` et dire honnêtement que les deux sont acceptables ; celle avec drapeau est plus lisible pour des débutants.

### Palier bonus
1. Limiter la partie à 7 essais, avec un message de défaite.
2. Refuser une saisie hors de 1–100 sans consommer d'essai.
3. Inverser les rôles : **l'ordinateur devine** le nombre du joueur par dichotomie — excellent pour introduire intuitivement la complexité logarithmique (7 coups suffisent toujours).
4. Blinder la saisie non numérique (annonce du `try/except` de la S4).

## Fil rouge — `OpportuniTrack` v0.2
> « Le filtre d'éligibilité »

Le programme demande les critères d'une opportunité et décide si l'utilisateur doit candidater :

```python
pays = input("Pays de l'opportunité : ").strip().lower()
jours_restants = int(input("Jours avant la date limite : "))
niveau_requis = input("Niveau requis (licence/master/doctorat) : ").strip().lower()
mon_niveau = "master"

# Une règle métier écrite en français, puis traduite ligne à ligne :
# "Je candidate si le niveau correspond ET s'il reste au moins 3 jours."
if niveau_requis == mon_niveau and jours_restants >= 3:
    print("✅ À CANDIDATER — priorité haute")
elif niveau_requis == mon_niveau and jours_restants > 0:
    print("⏰ URGENT — moins de 3 jours, prépare un dossier minimal")
elif jours_restants <= 0:
    print("❌ Trop tard, deadline dépassée")
else:
    print("↪️ Niveau non correspondant — à archiver")
```

**Astuce pédagogique** : faire écrire la règle **en français** au tableau avant de coder. La traduction français → Python est le vrai apprentissage de la séance.

## Ressources — Séance 2
| Ressource | Lien | Note |
|---|---|---|
| Tutoriel officiel — Structures de contrôle | https://docs.python.org/fr/3/tutorial/controlflow.html | Section 4 |
| Real Python — Conditional Statements | https://realpython.com/python-conditional-statements/ | Très visuel |
| Real Python — `for` loops | https://realpython.com/python-for-loop/ | — |
| Real Python — `while` loops | https://realpython.com/python-while-loop/ | Traite explicitement les boucles infinies |
| *Automate the Boring Stuff* 3e, ch. 2 | https://automatetheboringstuff.com/3e/chapter2.html | « Flow Control » |
| Python Tutor (visualiseur pas-à-pas) | https://pythontutor.com/ | **Outil clé de cette séance** : projeter l'exécution ligne par ligne |
| Codingame / Codewars (8 kyu) | https://www.codewars.com/ | Pour le palier bonus |

---
---

# SÉANCE 3 — Ranger l'information
### *Listes, dictionnaires, tuples, ensembles, parcours*

> **Promesse** : « Jusqu'ici tu manipulais une info à la fois. Aujourd'hui, tu gères des centaines. »

## Objectifs pédagogiques
1. **Choisir** la bonne structure de données parmi liste, dictionnaire, tuple et ensemble selon le besoin.
2. **Créer, lire, modifier** une liste : indexation, `append`, `remove`, `len`, `in`, tranches (`slicing`).
3. **Créer et parcourir** un dictionnaire (`clé: valeur`), avec `.keys()`, `.values()`, `.items()`, `.get()`.
4. **Combiner** les structures : une **liste de dictionnaires** — la structure qui portera tout le reste de la formation.
5. **Trier et filtrer** une collection (`sorted` avec `key`, filtrage par boucle).
6. **Écrire** une compréhension de liste simple et savoir quand ne pas l'utiliser.
7. **Appliquer** les règles PEP 8 de base sur le nommage et les espaces.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–10 | Rituel « l'erreur du jour » | Plénière | `IndexError: list index out of range` — décryptage. |
| 10–35 | **Théorie 1** : la liste | Plénière + live coding | Création, index à partir de 0, index négatif, tranches, méthodes, `in`, `len`. |
| 35–55 | **Pratique 1** | Individuel | 8 micro-manipulations sur une liste de pays. |
| 55–80 | **Théorie 2** : le dictionnaire | Plénière + live coding | Clé/valeur, accès, ajout, `get()` et son défaut, parcours avec `.items()`. |
| 80–90 | **PAUSE** | — | — |
| 90–110 | **Théorie 3** : tuple, ensemble, et « quelle structure choisir ? » | Plénière | Arbre de décision projeté. Dédoublonnage avec `set`. |
| 110–125 | **Théorie 4** : la liste de dictionnaires | Live coding | Le schéma mental du « tableau » : lignes = dictionnaires, colonnes = clés. Annonce explicite : « c'est un DataFrame pandas avant l'heure ». |
| 125–160 | **Pratique 2 — Exercice principal** | Binômes | Le carnet d'opportunités (ci-dessous). |
| 160–170 | **Bonus doux** : la compréhension de liste | Plénière | Le même filtre écrit en 4 lignes puis en 1. |
| 170–180 | **Clôture** | Plénière | PEP 8 en 5 règles, devoir, teaser S4. |

## Concepts clés — expliqués simplement

**La liste = une liste de courses numérotée.** Ordonnée, modifiable, on peut avoir deux fois le même élément. `pays[0]` est le **premier**. La numérotation commence à zéro — analogie de l'ascenseur français : le rez-de-chaussée est l'étage 0, le « premier » est au-dessus.

**L'index négatif** est un cadeau de Python : `liste[-1]` est le dernier élément, sans avoir à calculer la longueur.

**La tranche (`slicing`)** : `liste[1:4]` prend de l'index 1 **inclus** à l'index 4 **exclu**. Analogie du ticket de train : on monte à la gare 1, on descend avant la gare 4.

**Le dictionnaire = un répertoire téléphonique.** On ne cherche pas « la 3e personne », on cherche « le numéro de Fatou ». On accède par **clé**, pas par position. Une clé est unique.

**`dico["ville"]` vs `dico.get("ville")`** : le premier plante si la clé n'existe pas, le second rend `None` (ou une valeur par défaut). Sur des données du monde réel — toujours incomplètes — `.get()` est le réflexe professionnel.

**Le tuple = une liste plastifiée.** Même chose qu'une liste, mais on ne peut plus rien modifier. Sert pour ce qui ne doit pas bouger : des coordonnées, une date, un couple de valeurs.

**L'ensemble (`set`) = un sac sans doublons.** Pas d'ordre, pas de répétition. Le geste le plus utile de la vie réelle : `list(set(ma_liste))` supprime les doublons en une ligne.

**L'arbre de décision** (à afficher et à laisser au mur) :
- Mes données ont-elles un **nom** pour chaque champ ? → **dictionnaire**
- Sinon, l'**ordre** compte-t-il et vais-je **modifier** ? → **liste**
- Ordre important mais **jamais de modification** ? → **tuple**
- Je veux juste savoir **qui est présent, sans doublon** ? → **ensemble**

**La structure reine : la liste de dictionnaires.**
```python
opportunites = [
    {"titre": "Bourse Smarts-Up", "pays": "France", "jours": 12},
    {"titre": "Stage data",       "pays": "Maroc",  "jours": 3},
]
```
Faire dessiner au tableau le tableau équivalent (lignes/colonnes). Dire la phrase suivante mot pour mot : *« Ce que vous venez d'écrire, c'est exactement ce que pandas appellera un DataFrame en séance 7. Vous avez déjà compris la structure ; il ne restera que la syntaxe. »* Cette phrase désamorce l'angoisse de l'Arc 2.

## Plan des slides — Séance 3 (21 slides)

1. **Couverture** + 2. **Frise** + 3. **L'erreur du jour** (`IndexError`).
2. **Le problème** — 40 variables `pays1, pays2, pays3…` à l'écran. « Ça ne tient pas. »
3. **La liste** — la liste de courses manuscrite à côté du code équivalent.
4. **⚠️ On compte à partir de 0** — schéma de l'ascenseur / cases numérotées 0,1,2,3.
5. **L'index négatif** — les mêmes cases annotées -1, -2, -3.
6. **Les tranches** — la métaphore du ticket de train, bornes incluse/exclue coloriées.
7. **La boîte à outils de la liste** — tableau : `append`, `insert`, `remove`, `pop`, `sort`, `len`, `in`.
8. **Parcourir une liste** — le `for` de la S2, appliqué. Rappel visuel.
9. **Exercices flash** — les 8 micro-manipulations.
10. **Le dictionnaire** — capture d'un répertoire de contacts en face du code.
11. **Clé et valeur** — schéma d'une fiche : `"titre" → "Bourse Smarts-Up"`.
12. **⚠️ `[ ]` plante, `.get()` protège** — deux blocs code, l'un avec un `KeyError` rouge.
13. **Parcourir un dictionnaire** — les 3 façons (`keys`, `values`, `items`).
14. **Le tuple** — icône plastifiée / cadenas.
15. **L'ensemble** — le sac de billes où les doublons disparaissent + `list(set(...))`.
16. **Quelle structure choisir ?** — l'arbre de décision en pleine page (**la slide à imprimer**).
17. **La structure reine** — la liste de dictionnaires + le tableau équivalent côte à côte.
18. **« C'est déjà un DataFrame »** — teaser de la S7.
19. **Exercice : le carnet d'opportunités**.
20. **PEP 8 en 5 règles** — snake_case, 4 espaces, espaces autour des `=`, noms explicites, une instruction par ligne.
21. **Bilan / devoir / teaser S4**.

## Exercice pratique — « Le carnet d'opportunités »

**Énoncé (socle).** On te fournit une liste de dictionnaires. Écris un programme qui :
1. affiche le nombre total d'opportunités ;
2. affiche uniquement celles dont la deadline est dans moins de 10 jours ;
3. affiche la liste des pays représentés, **sans doublon** ;
4. affiche l'opportunité la plus urgente ;
5. trie et affiche toutes les opportunités de la plus urgente à la moins urgente.

```python
opportunites = [
    {"titre": "Bourse Smarts-Up",     "organisme": "Univ. Paris Cité", "pays": "France", "jours": 12},
    {"titre": "Stage Data Analyst",   "organisme": "OCP",              "pays": "Maroc",  "jours": 3},
    {"titre": "Programme IsDB",       "organisme": "IsDB",             "pays": "Maroc",  "jours": 25},
    {"titre": "Hackathon IA",         "organisme": "CESAM",            "pays": "Maroc",  "jours": 7},
    {"titre": "Erasmus Mundus",       "organisme": "UE",               "pays": "France", "jours": 40},
]
```

### Corrigé commenté

```python
# --- 1) Combien d'opportunités ? -------------------------------------------
# len() sur une liste = nombre d'éléments (ici, nombre de dictionnaires).
print(f"Total : {len(opportunites)} opportunités\n")

# --- 2) Les urgentes --------------------------------------------------------
print("À traiter en priorité (moins de 10 jours) :")
for opp in opportunites:
    # opp est un DICTIONNAIRE. On accède à ses champs par leur nom.
    if opp["jours"] < 10:
        print(f"  - {opp['titre']} ({opp['jours']} j) — {opp['organisme']}")
        # ATTENTION : guillemets SIMPLES à l'intérieur d'une f-string
        # ouverte par des guillemets doubles, sinon Python croit que le texte se termine.

# --- 3) Les pays sans doublon ----------------------------------------------
pays_vus = []                     # une liste vide qu'on va remplir
for opp in opportunites:
    pays_vus.append(opp["pays"])  # on empile tous les pays, doublons compris

pays_uniques = set(pays_vus)      # le set élimine automatiquement les doublons
print(f"\nPays représentés : {', '.join(sorted(pays_uniques))}")
# join() colle les éléments d'une collection de textes avec un séparateur.
# sorted() les remet dans l'ordre alphabétique (un set n'a pas d'ordre).

# --- 4) La plus urgente -----------------------------------------------------
# min() cherche le plus petit. key= indique SUR QUOI comparer :
# ici, sur la valeur de la clé "jours" de chaque dictionnaire.
plus_urgente = min(opportunites, key=lambda opp: opp["jours"])
print(f"\nLa plus urgente : {plus_urgente['titre']} ({plus_urgente['jours']} j)")

# --- 5) Le classement complet ----------------------------------------------
# sorted() rend une NOUVELLE liste triée, sans toucher à l'originale.
classement = sorted(opportunites, key=lambda opp: opp["jours"])
print("\nClassement par urgence :")
for rang, opp in enumerate(classement, start=1):
    # enumerate() donne en même temps la position ET l'élément.
    print(f"  {rang}. {opp['titre']:<25} {opp['jours']:>3} j")
    # :<25 aligne le texte à gauche sur 25 caractères, :>3 aligne le nombre à droite.
    # Résultat : des colonnes propres sans effort.
```

**Sur le `lambda`** : ne pas en faire un chapitre. Le présenter comme *« une mini-fonction jetable qui répond à la question : comparer sur quoi ? »*. Les profils techniques apprécieront ; les débutants le copieront comme une formule. On le formalisera en S6.

### Palier bonus
1. Compter le nombre d'opportunités **par pays** (dictionnaire d'accumulation, ou `collections.Counter`).
2. Réécrire le filtre de la question 2 en **compréhension de liste** :
   ```python
   urgentes = [opp for opp in opportunites if opp["jours"] < 10]
   ```
3. Regrouper les opportunités par pays dans un dictionnaire `{"Maroc": [...], "France": [...]}` — c'est un `groupby` fait main, à rappeler en S8.
4. Trier à deux niveaux : par pays puis par urgence (`key=lambda o: (o["pays"], o["jours"])`).

## Fil rouge — `OpportuniTrack` v0.3
Le carnet vit désormais **en mémoire** : l'utilisateur peut ajouter une opportunité (construite en dictionnaire) à la liste, puis afficher le carnet trié. Le programme oublie tout à la fermeture — **c'est le manque qui motive la S4** (« et si on gardait ça dans un fichier ? »).

## Ressources — Séance 3
| Ressource | Lien | Note |
|---|---|---|
| Tutoriel officiel — Structures de données | https://docs.python.org/fr/3/tutorial/datastructures.html | Section 5, listes/sets/dicts/compréhensions |
| Real Python — Lists and Tuples | https://realpython.com/python-lists-tuples/ | — |
| Real Python — Dictionaries | https://realpython.com/python-dicts/ | — |
| Real Python — List Comprehensions | https://realpython.com/list-comprehension-python/ | Pour le palier bonus |
| PEP 8 (texte officiel) | https://peps.python.org/pep-0008/ | Ne pas le faire lire en entier : en extraire 5 règles |
| PEP 8 — version lisible | https://pep8.org/ | Mise en page nettement plus digeste |
| Python Tutor | https://pythontutor.com/ | Projeter la construction d'une liste de dicts pas à pas |
| `collections` (doc officielle) | https://docs.python.org/fr/3/library/collections.html | `Counter`, `defaultdict` pour le bonus |

---
---

# SÉANCE 4 — Fabriquer ses outils
### *Fonctions, modules, fichiers, erreurs — et passage à VS Code*

> **Promesse** : « À la fin de la séance, tu quittes le navigateur : tu as un vrai programme, dans un vrai fichier, qui garde tes données. »

C'est la séance charnière de la formation : elle clôt la rampe de lancement et livre le premier artefact complet.

## Objectifs pédagogiques
1. **Écrire** une fonction avec paramètres, valeur de retour et docstring.
2. **Distinguer** `return` et `print` — la confusion la plus coûteuse de la formation.
3. **Expliquer** la portée locale/globale à un niveau opérationnel.
4. **Organiser** son code en plusieurs fichiers et importer ses propres modules.
5. **Lire et écrire** un fichier texte, CSV et JSON avec `pathlib`, `csv` et `json`.
6. **Protéger** un programme des saisies invalides avec `try / except`.
7. **Travailler** dans VS Code : ouvrir un dossier, exécuter un script, utiliser le terminal intégré.

## Déroulé minuté (180 min)

| Temps | Bloc | Modalité | Contenu |
|---|---|---|---|
| 0–20 | **Migration vers VS Code** | Pas-à-pas guidé | Ouvrir un dossier, créer `tracker.py`, sélectionner l'interpréteur, exécuter (F5 / terminal). Le formateur ne passe à la suite que quand tout le monde a vu un « Bonjour » s'afficher dans le terminal. |
| 20–45 | **Théorie 1** : la fonction | Plénière + live coding | Motivation (la répétition), `def`, paramètres, `return`, docstring, appel. |
| 45–70 | **Pratique 1** | Individuel | Transformer trois blocs de code copiés-collés de la S3 en fonctions. |
| 70–80 | **PAUSE** | — | — |
| 80–100 | **Théorie 2** : modules et organisation | Plénière | `import`, `from … import`, créer `outils.py`, `if __name__ == "__main__"`. |
| 100–125 | **Théorie 3** : fichiers et erreurs | Live coding | `with open(...)`, `pathlib.Path`, JSON, CSV, `try/except`. |
| 125–165 | **Pratique 2 — Fil rouge v1** | Binômes | `OpportuniTrack` complet en ligne de commande. |
| 165–175 | **Mise en commun** | Plénière | Deux projections, revue de code bienveillante avec une grille en 3 points. |
| 175–180 | **Clôture solennelle** | Plénière | « Vous venez de finir la rampe de lancement. » Annonce de l'Arc 2 et de ce qui change. |

## Concepts clés — expliqués simplement

**La fonction = une machine à café.** Tu mets quelque chose dedans (les **paramètres**), elle fait son travail à l'intérieur (le **corps**), elle te rend quelque chose (le **`return`**). Tu n'as pas besoin de savoir comment elle chauffe l'eau pour t'en servir. Trois bénéfices à énoncer : **ne pas se répéter**, **nommer une intention**, **tester une brique isolée**.

**`return` contre `print` — la grande confusion.** À faire vivre par l'échec :
```python
def double(n):
    print(n * 2)      # affiche, mais ne RENDT rien

resultat = double(5)  # affiche 10... et resultat vaut None
print(resultat + 1)   # TypeError !
```
Formule à faire répéter : *« `print` parle à l'humain. `return` parle au reste du programme. »* Une fonction qui `print` est un cul-de-sac ; une fonction qui `return` est une brique.

**La portée = les murs de la machine.** Une variable créée dans une fonction n'existe qu'à l'intérieur ; elle disparaît quand la fonction se termine. Ce n'est pas une punition, c'est une protection : personne ne peut casser l'intérieur de ta machine par accident.

**Le module = un tiroir de la boîte à outils.** Un fichier `.py` est un module. `import outils` ouvre le tiroir ; `from outils import charger` sort un seul outil. Et `if __name__ == "__main__":` se traduit : *« exécute ceci seulement si on lance CE fichier directement, pas si on l'importe. »*

**Le fichier = la mémoire longue.** Sans fichier, tout disparaît à la fermeture. `with open(...)` se lit : « ouvre le fichier, fais ce qu'il y a à faire, et **referme-le quoi qu'il arrive** ». Le `with` évite l'oubli de fermeture — on reverra ce mécanisme en profondeur en S6.

**Quel format choisir ?**
- **TXT** : du texte brut, pour des notes.
- **CSV** : un tableau. S'ouvre dans Excel. Parfait pour échanger avec des non-développeurs.
- **JSON** : des données **imbriquées** (une liste de dictionnaires !). C'est aussi le format d'échange du web : tout ce qui sort d'une API en ligne a cette forme-là.

**`try / except` = la ceinture de sécurité.** « Essaie ceci ; si ça casse pour telle raison, fais plutôt cela. » Règle professionnelle à donner tout de suite : **on n'écrit jamais `except:` tout seul** — on nomme l'erreur qu'on attend (`except ValueError:`), sinon on masque des bugs qu'on ne voulait pas masquer.

## Plan des slides — Séance 4 (22 slides)

1. **Couverture** + 2. **Frise** (fin de l'Arc 1 marquée visuellement).
2. **On change d'atelier** — Colab → VS Code, captures des 4 zones (explorateur, éditeur, terminal, barre d'état avec l'interpréteur).
3. **Checklist de migration** — 5 étapes numérotées, à cocher.
4. **Le problème du copier-coller** — 30 lignes à l'écran, le même bloc surligné 3 fois.
5. **La machine à café** — schéma entrée → traitement → sortie.
6. **Anatomie d'une fonction** — code annoté : `def`, nom, parenthèses, deux-points, indentation, `return`.
7. **Appeler une fonction** — définition vs appel, avec l'ordre d'exécution numéroté.
8. **⚠️ `print` vs `return`** — pleine page, deux colonnes, l'exemple qui plante.
9. **Les paramètres** — obligatoires, avec valeur par défaut, nommés à l'appel.
10. **La docstring** — le triple guillemet, et la démo de `help(ma_fonction)`.
11. **La portée** — schéma : la boîte de la fonction avec des murs.
12. **Exercice : refactoriser la S3**.
13. **Le module = un tiroir** — arborescence de fichiers projetée.
14. **`import` : les 3 formes** — tableau comparatif + quand utiliser laquelle.
15. **`if __name__ == "__main__"`** — la traduction en français sur la slide.
16. **La mémoire longue** — icône RAM volatile vs disque.
17. **`with open()`** — le code annoté + « il referme tout seul ».
18. **TXT / CSV / JSON** — trois colonnes, le même carnet représenté dans les trois formats.
19. **⚠️ L'encodage** — `encoding="utf-8"` toujours. Un exemple d'accent cassé.
20. **La ceinture de sécurité** — `try/except` + le rappel « jamais d'`except` nu ».
21. **Le fil rouge v1** — capture du menu de l'application terminée.
22. **Fin de l'Arc 1 / ce qui change en S5**.

## Exercice pratique / Fil rouge v1 — `OpportuniTrack` CLI

**Énoncé.** Une application en ligne de commande, répartie sur deux fichiers, qui propose un menu : ajouter une opportunité, lister le carnet trié par urgence, filtrer par pays, sauvegarder, quitter. Les données survivent à la fermeture du programme.

**Arborescence :**
```
opportunitrack/
├── stockage.py   # les outils de lecture/écriture
├── tracker.py    # le programme principal
└── donnees.json  # créé automatiquement
```

### Corrigé commenté — `stockage.py`

```python
"""Outils de persistance du carnet d'opportunités (lecture/écriture JSON)."""

import json
from pathlib import Path

# Path() est la façon moderne de désigner un fichier : elle fonctionne
# à l'identique sur Windows, macOS et Linux (fini les problèmes de \ et /).
FICHIER = Path("donnees.json")


def charger() -> list:
    """Renvoie la liste des opportunités enregistrées.

    Renvoie une liste vide si aucun fichier n'existe encore
    (cas du tout premier lancement).
    """
    if not FICHIER.exists():
        return []          # sortie anticipée : plus lisible qu'un gros if/else

    # encoding="utf-8" est OBLIGATOIRE : sans lui, les accents et
    # les caractères non latins peuvent être illisibles selon la machine.
    with FICHIER.open("r", encoding="utf-8") as f:
        return json.load(f)   # transforme le texte JSON en objets Python


def sauvegarder(opportunites: list) -> None:
    """Écrit la liste complète dans le fichier JSON (écrase le contenu)."""
    with FICHIER.open("w", encoding="utf-8") as f:
        # indent=2  -> fichier lisible par un humain
        # ensure_ascii=False -> conserve les accents tels quels
        json.dump(opportunites, f, indent=2, ensure_ascii=False)
```

### Corrigé commenté — `tracker.py`

```python
"""OpportuniTrack — carnet d'opportunités en ligne de commande."""

from stockage import charger, sauvegarder   # on importe NOS outils


def demander_entier(question: str) -> int:
    """Redemande une saisie tant que l'utilisateur ne donne pas un entier.

    C'est la ceinture de sécurité : sans elle, taper "douze" fait planter
    tout le programme et l'utilisateur perd ce qu'il avait saisi.
    """
    while True:
        reponse = input(question)
        try:
            return int(reponse)   # si la conversion réussit, on SORT de la boucle
        except ValueError:
            # On nomme l'erreur attendue : un except nu masquerait tout, y compris
            # un Ctrl+C ou un vrai bug.
            print("  ⚠️  Merci de saisir un nombre entier.")


def saisir_opportunite() -> dict:
    """Construit un dictionnaire à partir des saisies de l'utilisateur."""
    return {
        "titre": input("Titre : ").strip(),
        "organisme": input("Organisme : ").strip(),
        "pays": input("Pays : ").strip().title(),  # .title() -> "maroc" devient "Maroc"
        "jours": demander_entier("Jours restants : "),
    }


def afficher(opportunites: list) -> None:
    """Affiche le carnet trié de la plus urgente à la moins urgente."""
    if not opportunites:                 # une liste vide vaut False
        print("\n(Carnet vide)\n")
        return                           # return sans valeur = "je m'arrête ici"

    print(f"\n{'TITRE':<30}{'PAYS':<15}{'JOURS':>6}")
    print("-" * 51)
    for opp in sorted(opportunites, key=lambda o: o["jours"]):
        print(f"{opp['titre']:<30}{opp['pays']:<15}{opp['jours']:>6}")
    print()


def filtrer_par_pays(opportunites: list, pays: str) -> list:
    """Renvoie une NOUVELLE liste ne contenant que le pays demandé.

    La fonction ne modifie pas la liste d'origine : c'est une bonne habitude
    qui évitera beaucoup de bugs à partir de la séance 5.
    """
    return [opp for opp in opportunites if opp["pays"].lower() == pays.lower()]


MENU = """
=== OpportuniTrack ===
1. Ajouter une opportunité
2. Afficher le carnet
3. Filtrer par pays
4. Quitter
"""


def main() -> None:
    """Boucle principale du programme."""
    opportunites = charger()     # on récupère ce qui avait été sauvegardé

    while True:
        print(MENU)
        choix = input("Ton choix : ").strip()

        # match/case (Python 3.10+) : plus lisible qu'une cascade de if/elif
        # quand on compare UNE variable à plusieurs valeurs fixes.
        match choix:
            case "1":
                opportunites.append(saisir_opportunite())
                sauvegarder(opportunites)     # on sauvegarde immédiatement
                print("✅ Ajoutée et sauvegardée.")
            case "2":
                afficher(opportunites)
            case "3":
                pays = input("Quel pays ? ")
                afficher(filtrer_par_pays(opportunites, pays))
            case "4":
                print("À bientôt !")
                break                          # sort du while -> fin du programme
            case _:
                # le _ est le "sinon" du match : n'importe quelle autre valeur
                print("Choix invalide.")


# Ce bloc ne s'exécute QUE si l'on lance directement `python tracker.py`.
# Si un autre fichier fait `import tracker`, main() ne démarre pas tout seul.
if __name__ == "__main__":
    main()
```

**Notes pédagogiques :**
- **`match/case` est introduit ici volontairement**, sur son cas d'usage le plus lisible (un menu). C'est du Python 3.10+ moderne, et c'est plus facile à lire pour un débutant qu'une cascade de `elif`. Bien préciser que `if/elif` reste correct.
- Les **annotations de type** (`-> list`, `: str`) sont présentes sans être expliquées en détail : les présenter comme *« une étiquette qui dit ce que la fonction attend et ce qu'elle rend »*. Elles seront formalisées en S5.
- Faire remarquer que `main()` ne contient **aucune logique métier** : elle ne fait qu'orchestrer. C'est la première marche vers l'architecture propre de l'Arc 2.

### Palier bonus
1. Ajouter une option « supprimer une opportunité » (par numéro, avec confirmation).
2. Exporter le carnet en CSV avec le module `csv` (`csv.DictWriter`) pour l'ouvrir dans Excel.
3. Remplacer le champ `jours` par une vraie date (`datetime.date.fromisoformat`) et calculer les jours restants automatiquement.
4. Créer une troisième fonction module `affichage.py` et réorganiser les imports.

### Grille de revue de code (mise en commun, 3 points)
1. **Les noms** — un inconnu comprendrait-il ce que fait cette fonction rien qu'à son nom ?
2. **La répétition** — vois-tu deux blocs presque identiques ? Ils veulent devenir une fonction.
3. **La responsabilité** — cette fonction fait-elle *une seule* chose ?

## Ressources — Séance 4
| Ressource | Lien | Note |
|---|---|---|
| Tutoriel officiel — Fonctions | https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions | Section 4.9 |
| Tutoriel officiel — Modules | https://docs.python.org/fr/3/tutorial/modules.html | Section 6 |
| Tutoriel officiel — Erreurs et exceptions | https://docs.python.org/fr/3/tutorial/errors.html | Section 8 |
| `pathlib` (doc officielle) | https://docs.python.org/fr/3/library/pathlib.html | La façon moderne de gérer les chemins |
| `json` (doc officielle) | https://docs.python.org/fr/3/library/json.html | — |
| `csv` (doc officielle) | https://docs.python.org/fr/3/library/csv.html | `DictReader` / `DictWriter` |
| PEP 636 — Tutoriel `match` officiel | https://peps.python.org/pep-0636/ | **La référence** pour le pattern matching 3.10+ |
| Real Python — Defining Functions | https://realpython.com/defining-your-own-python-function/ | — |
| Real Python — `structural pattern matching` | https://realpython.com/structural-pattern-matching/ | Va bien au-delà du menu, utile pour le formateur |
| VS Code — Editing Python | https://code.visualstudio.com/docs/python/editing | Après le tutoriel d'installation |
| VS Code — Debugging Python | https://code.visualstudio.com/docs/python/debugging | Le point d'arrêt : à montrer 5 min en fin de séance, effet garanti |
| *Automate the Boring Stuff* 3e, ch. 3 & 10 | https://automatetheboringstuff.com/3e/ | Fonctions ; lecture/écriture de fichiers |

---

## Fin de l'Arc 1 — bilan à annoncer au groupe

Après quatre séances, chaque participant :
- a écrit environ 250 lignes de Python ;
- possède une application fonctionnelle qui persiste ses données ;
- sait lire un message d'erreur sans paniquer ;
- travaille dans un environnement de développement professionnel.

**Ce qui change à partir de la S5** : on cesse d'apprendre des instructions, on commence à apprendre à **structurer**. Prévenir explicitement que le rythme monte, et que le palier bonus des séances précédentes devient le socle. Il reste alors quatre séances : la moitié du chemin est faite.

---
*Suite : Arc 2 — Séances 5 à 8 (POO, Python avancé, NumPy/pandas, dataviz). La séance 8 clôt la formation.*

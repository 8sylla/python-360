# Le dispositif en ligne

**Formation Python 360° — 100 % à distance.**
Commission Scientifique nationale · ASEGUIM

Huit séances de 3 h. **Cinq outils, pas un de plus.** Ce document dit quoi
monter, ce qu'on fait pendant une séance du début à la fin, et quels devoirs
on donne.

---

## 1. Les cinq outils

| Outil | Ce qu'il porte | Quand |
| --- | --- | --- |
| **Google Classroom** | le cours : annonces, supports, devoirs, remises, notes, calendrier | S0 → S8 |
| **Google Meet** | la séance en direct | S0 → S8 |
| **Google Colab** | écrire du code sans rien installer | S0 → S3 |
| **VS Code** | écrire du code pour de vrai | S4 → S8 |
| **GitHub** | le fil rouge, et le travail en équipe | S4 → S8 |

**Trois au début, cinq à la fin.** Un apprenant de la séance 1 n'a besoin que
d'un navigateur et d'un compte Google.

### Ce que j'avais mis en trop, et pourquoi je l'enlève

| Enlevé | Pourquoi |
| --- | --- |
| **Google Sites** | Classroom *est* le portail. C'était un doublon pur. |
| **Google Chat** | Le flux Classroom porte les annonces et les questions. Un deuxième endroit où parler, c'est un endroit où personne ne va. |
| **Google Forms** | Classroom crée les quiz lui-même (« Devoir avec questionnaire »), et les corrige. |
| **Google Sheets** | Classroom tient le carnet de notes et l'état des remises. Le tableau à la main faisait triple emploi. |
| **Google Drive** (comme dossier à parcourir) | Classroom crée et range son propre dossier Drive. On y dépose depuis Classroom, on n'y navigue pas. |

> Classroom fabrique aussi **son propre lien Meet**, réservé aux membres du
> cours, et **son propre calendrier** avec les dates de rendu. Pas d'événement
> Agenda récurrent à créer, pas de lien à recoller.

---

## 2. À vérifier avant tout le reste

### Classroom est-il ouvert sur ton compte ?

Ouvre `classroom.google.com` avec ton compte professionnel.

- **Tu vois « Créer un cours »** → tout est réglé.
- **Tu es bloqué** → Classroom n'est pas inclus dans les formules Workspace
  *Business*. Crée le cours depuis un **compte Google personnel** : c'est
  gratuit et complet. C'est le seul endroit du dispositif où ton compte pro ne
  sert pas.

### Meet : les deux fonctions qui portent la pédagogie

| Fonction | Pourquoi elle compte | Si tu ne l'as pas |
| --- | --- | --- |
| **Salles de sous-groupes** | les binômes, cœur des ateliers | deuxième réunion Meet permanente, lien épinglé dans Classroom |
| **Enregistrement** | le replay, qui rattrape les absents | OBS Studio en local, dépôt du fichier dans Classroom |

**Fais le test à vide aujourd'hui** : une réunion, un deuxième compte,
et tu vérifies partage d'écran *avec le son*, salles de sous-groupes,
enregistrement. Quinze minutes.

---

## 3. Colab puis VS Code — oui, et voici où basculer

Tu me demandes si la bascule reste utile. **Oui, et elle n'est pas
négociable** — mais elle n'est pas un aller simple.

| Séances | Outil | Pourquoi celui-là |
| --- | --- | --- |
| **S0 → S3** | **Colab** | Zéro installation. La première cause d'abandon en semaine 1, c'est un Python qui ne s'installe pas. On l'élimine. |
| **S4 → S6** | **VS Code** | On écrit des **fichiers** qui s'appellent entre eux, des fonctions, des classes, des tests. Colab ne sait pas faire ça. |
| **S7 → S8** | **VS Code, en mode notebook** | Explorer des données veut un notebook. VS Code ouvre les `.ipynb` nativement : même outil, autre façon de s'en servir. |

**Le point important : S7 et S8 ne reviennent pas à Colab.** On y retrouve le
confort du notebook *sans changer d'outil* — VS Code ouvre les notebooks
directement. C'est ce qui évite d'avoir deux environnements en parallèle
pendant cinq séances.

**La bascule tombe en S4 pour une raison précise :** la séance 4 s'appelle
« Fabriquer ses outils ». C'est là qu'on écrit la première fonction réutilisée
ailleurs et le premier fichier lu depuis un autre fichier. Le notebook devient
un obstacle exactement à ce moment-là, pas avant.

> **Prévois-le :** la séance 4 commence par 20 minutes d'installation, en
> salles de sous-groupes, pendant que ceux qui sont prêts avancent. La cause
> n° 1 de blocage sous Windows reste la case **« Add python.exe to PATH »**
> non cochée.

---

## 4. La journée type

Exemple sur une séance de **18 h 00 à 21 h 00**. Décale tout si ton horaire
diffère ; les durées, elles, ne bougent pas.

### Avant — 30 minutes

| Heure | Ce que tu fais |
| --- | --- |
| **17 h 30** | Machine redémarrée. Mail, notifications, tout fermé. Ne pas déranger. |
| **17 h 40** | Ouvrir : les slides en PDF (écran 1), VS Code ou Colab avec le code du jour (écran 2), Classroom sur l'onglet « Travaux ». |
| **17 h 45** | Tester micro, caméra, et le partage d'écran **avec le son**. |
| **17 h 50** | Ouvrir la salle Meet. Vérifier que le devoir de la semaine est bien rendu par le plus grand nombre — ça te dit dans quel état arrive le groupe. |
| **17 h 55** | Accueillir **nommément** ceux qui arrivent. C'est ce qui fait qu'ils reviennent. |

### Pendant — 3 heures

| Heure | Bloc | Ce qui se passe |
| --- | --- | --- |
| **18 h 00** | **Lancer l'enregistrement.** | |
| 18 h 00 – 18 h 10 | **L'erreur du jour** | Un traceback projeté — pris dans les questions de la semaine. On le décode ensemble. Personne ne code encore. |
| 18 h 10 – 18 h 20 | **Le retour sur le devoir** | Deux ou trois rendus montrés, sans nommer. Ce qui marche, ce qui revient souvent. |
| 18 h 20 – 18 h 55 | **Bloc 1 — notion + live coding** | Jamais plus de 6 minutes sans qu'ils fassent quelque chose. Un sondage à 18 h 35. |
| 18 h 55 – 19 h 05 | **Pause** | Minuteur partagé à l'écran, sinon elle en fait 20. |
| 19 h 05 – 19 h 20 | **Bloc 2 — la notion difficile** | Celle de la séance. Analogie d'abord, code ensuite. |
| 19 h 20 – 19 h 35 | **Atelier 1, en binôme** | Salles de sous-groupes, 15 min. Tu passes dans chaque salle 90 secondes. |
| 19 h 35 – 19 h 45 | **Correction de l'atelier 1** | Un binôme présente et partage son écran. Pas toi. |
| 19 h 45 – 19 h 55 | **Pause** | |
| 19 h 55 – 20 h 15 | **Bloc 3 — les pièges** | Les erreurs qu'ils vont rencontrer, provoquées en direct. Sondage à 20 h 10. |
| 20 h 15 – 20 h 35 | **Atelier 2, en binôme** | Le plus dur de la séance. 20 min. |
| 20 h 35 – 20 h 45 | **Correction de l'atelier 2** | |
| 20 h 45 – 20 h 55 | **Le fil rouge** | OpportuniTrack : la version du jour, en live coding. |
| 20 h 55 – 21 h 00 | **Clôture** | « Une ligne, un mot » dans le chat. Le devoir est annoncé **et publié dans Classroom pendant que tu parles**. |

### Après — 1 heure

| Heure | Ce que tu fais |
| --- | --- |
| **21 h 00** | **Arrêter l'enregistrement avant de quitter**, sinon il continue. |
| **21 h 15** | Déposer le replay dans Classroom, en « Document » du jour. |
| **21 h 20** | Publier le corrigé des deux ateliers. |
| **21 h 30** | Vérifier que le devoir est bien publié, avec sa date de rendu. |
| **Le lendemain** | Message privé (commentaire privé Classroom) à ceux qui ont manqué **deux séances d'affilée**. C'est le geste qui sauve le plus d'abandons. |

### Les trois gestes qui remplacent la présence physique

1. **Un sondage toutes les 20 minutes.** En salle, tu lis les visages. En
   ligne, tu ne lis rien. Deux options suffisent : *ça tourne / je suis
   bloqué·e*.
2. **« Tu partages ton écran ? »** Vingt fois plus rapide que de faire décrire
   une erreur. C'est pour ça que le partage est ouvert à tous.
3. **Le chat Meet est perdu à la fin.** Ce qui mérite de survivre, tu le
   reposes dans le flux Classroom pendant la pause.

---

## 5. Les six types de devoirs

Un seul devoir noté par séance. Les autres formes servent à autre chose que
la note.

### 5.1 Le devoir d'application — **toutes les séances**

Le devoir principal. Il **prolonge** l'atelier 2 de la séance, il ne le répète
pas : une contrainte de plus, un cas de plus.

- **Charge :** 30 à 45 minutes.
- **Rendu :** un fichier (`.ipynb` jusqu'à S3, `.py` ensuite) déposé dans
  Classroom.
- **Notation :** `Fait / Fait avec réserve / À reprendre`. **Jamais de note
  chiffrée** : ce qui compte, c'est que le travail avance.
- **Retour :** deux phrases en commentaire privé — ce qui est juste, et la
  prochaine marche.

### 5.2 Le devoir de reprise — **avant chaque séance**

Rouvrir le notebook « point de reprise » de la séance à venir et l'exécuter
de bout en bout. Cinq minutes. Ça garantit que **personne n'arrive avec un
environnement cassé**, et que celui qui a manqué la semaine dernière est à
jour.

- **Rendu :** aucun. Une case à cocher dans Classroom.

### 5.3 Le devoir fil rouge — **S4, S5, S7 et S8**

Une version d'OpportuniTrack, poussée sur **GitHub**. C'est le seul devoir
qui s'accumule : à la fin, le dépôt raconte toute la formation.

- **Rendu :** un lien de commit collé dans Classroom.
- **Ce qu'on regarde :** que ça tourne, et que le message de commit dise ce
  qui a changé.

### 5.4 Le quiz éclair — **avant S5 et avant S7**

Cinq questions, corrigées automatiquement par Classroom, cinq minutes.

Ce n'est **pas** une évaluation : c'est ton radar. Il te dit qui a décroché
avant les deux marches raides — le passage à l'objet, puis le passage aux
données — pendant qu'il est encore temps de rattraper.

- **Rendu :** automatique.
- **Ce que tu en fais :** en dessous de 3/5, un message privé et un créneau de
  15 minutes.

### 5.5 La revue croisée — **S6 et S8**

Chacun lit le code d'un camarade et laisse **deux remarques** : une chose qui
marche bien, une question. Pas de correction, pas de jugement.

C'est l'exercice qui apprend le plus vite à lire du code — et le plus proche
de ce qui se passe dans une vraie équipe.

- **Rendu :** un commentaire sous le devoir du camarade (S6), puis une revue
  de *pull request* sur GitHub (S8).

### 5.6 Le livrable final — **S8**

Le dépôt complet : le fil rouge dans ses cinq versions, trois tests qui
passent, un `README` qui explique comment lancer le projet en deux commandes,
et le tableau de bord exporté. Plus cinq minutes de présentation en direct en
fin de dernière séance : ce que fait mon projet, une démonstration, la
difficulté que j'ai rencontrée.

- **C'est le seul travail noté.**

### Le rythme, en un coup d'œil

| Séance | Application | Reprise | Fil rouge | Quiz | Revue | Final |
| --- | :-: | :-: | :-: | :-: | :-: | :-: |
| S0 | | ✔ | | | | |
| S1 | ✔ | ✔ | | | | |
| S2 | ✔ | ✔ | | | | |
| S3 | ✔ | ✔ | | | | |
| S4 | ✔ | ✔ | ✔ | | | |
| S5 | ✔ | ✔ | ✔ | | | |
| S6 | ✔ | ✔ | | ✔ | ✔ | |
| S7 | ✔ | ✔ | ✔ | | | |
| S8 | | ✔ | ✔ | | ✔ | ✔ |

> Les quiz sont placés **avant** S5 et S7, donc rendus en fin de S4 et de S6.

---

## 6. Le montage, une fois pour toutes

### Le cours Classroom

Un cours, nommé `Python 360° — ASEGUIM`. Dans **Travaux et devoirs**, crée un
**thème par séance** : `S00 — Kit de démarrage`, `S01 — Parler à la machine`…
Chaque thème reçoit ensuite, dans l'ordre :

1. le **Document** « Slides » (le PDF) ;
2. le **Document** « Notebook de reprise » ;
3. le **Devoir** d'application, avec sa date de rendu ;
4. après la séance, le **Document** « Replay » et le **Document** « Corrigé ».

**Le lien Meet** se crée depuis les paramètres du cours (« Générer un lien
Meet »). Il est réservé aux membres, et il ne change jamais.

### Les dates de rendu

Toujours **la veille de la séance suivante, à 20 h**. Une règle unique, jamais
d'exception à retenir. Classroom relance tout seul.

### GitHub

Une **organisation** `python360-aseguim`, un dépôt par apprenant à partir de
S4, créé depuis un dépôt modèle (*template repository*). Tu es
collaborateur sur chacun — c'est comme ça que tu relis sans rien télécharger.

---

## 7. Les checklists

### Une fois pour toutes

- [ ] Classroom accessible (sinon : compte personnel)
- [ ] Cours créé, un thème par séance
- [ ] Lien Meet généré depuis Classroom
- [ ] Test à vide de Meet : breakout, enregistrement, partage avec son
- [ ] Organisation GitHub + dépôt modèle
- [ ] Kit de démarrage (S0) publié
- [ ] Règle du rendu annoncée : la veille, 20 h

### La veille de chaque séance

- [ ] Jeu de données régénéré (les deadlines sont relatives au jour)
- [ ] Notebook de reprise exécuté dans un **noyau neuf**
- [ ] Slides du jour publiés dans le thème de la séance
- [ ] Devoir de la séance préparé, date de rendu posée
- [ ] Notebooks de binômes créés (jusqu'à S3)

### Le jour même

- [ ] 17 h 30 machine redémarrée, notifications coupées
- [ ] 17 h 45 micro, caméra, partage avec son testés
- [ ] 17 h 50 état des rendus regardé
- [ ] 18 h 00 **enregistrement lancé**
- [ ] Deux sondages placés (18 h 35, 20 h 10)
- [ ] Salles de sous-groupes préparées
- [ ] 21 h 00 enregistrement **arrêté avant de quitter**
- [ ] 21 h 30 replay, corrigé et devoir publiés

---

## 8. Ce que je n'ai pas pu vérifier

- **Classroom sur ton compte professionnel.** Il n'est pas inclus dans les
  formules Workspace *Business*, mais il est gratuit sur un compte Google
  personnel. Ouvre `classroom.google.com` : la réponse tient en dix secondes.
- **Les salles de sous-groupes dans ton Meet.** Elles portent tous les
  ateliers en binôme. Repli documenté au § 2, mais teste avant de t'engager.
- **L'horaire.** La journée type est calée sur 18 h – 21 h. Si tes apprenants
  sont répartis entre la Guinée, le Maroc et la France, l'heure ne conviendra
  pas à tout le monde — à trancher avec la liste des inscrits en main.

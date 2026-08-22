import json

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Séance 2 — Décider et répéter\n",
    "\n",
    "**Formation Python 360° · Commission Scientifique nationale — ASEGUIM**\n",
    "\n",
    "---\n",
    "\n",
    "## Avant toute chose\n",
    "\n",
    "**Fichier ▸ Enregistrer une copie dans Drive.**\n",
    "\n",
    "Sans ça, tu travailles dans un fichier en lecture seule : rien ne sera\n",
    "gardé quand tu fermeras l'onglet.\n",
    "\n",
    "---\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1 · Décider\n",
    "\n",
    "## On regarde ensemble : le booléen\n",
    "\n",
    "Il n'existe que deux réponses : `True`. `False`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "a_finance = True\n",
    "type(a_finance)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## On regarde ensemble : les faux amis\n",
    "\n",
    "Un égal (`=`) sert à ranger. Deux égaux (`==`) servent à demander si c'est pareil.\n",
    "De plus, une majuscule change tout, et un type aussi."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Erasmus\" != \"erasmus\")\n",
    "print(12 == \"12\")\n",
    "print(12 == 12.0)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## On regarde ensemble : l'aiguillage avec IF / ELIF / ELSE\n",
    "\n",
    "Le `if` est un aiguillage. Python s'arrête à la première vraie."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "jours_restants = 2\n",
    "if jours_restants < 0:\n",
    "    print(\"Deadline dépassée\")\n",
    "elif jours_restants < 7:\n",
    "    print(\"URGENT\")\n",
    "else:\n",
    "    print(\"Tu as le temps\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Le piège invisible\n",
    "\n",
    "Prédisez ce qui se passe ici avant d'exécuter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "niveau_requis = \"Master\"\n",
    "mon_niveau = \"Licence\"\n",
    "\n",
    "if mon_niveau == niveau_requis:\n",
    "    decision = \"CANDIDATER\"\n",
    "elif mon_niveau == \"Doctorat\":\n",
    "    decision = \"CANDIDATER\"\n",
    "\n",
    "# print(decision)  # Va produire une erreur si decommente. Pourquoi ?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## On regarde ensemble : Le fil rouge — OpportuniTrack v0.2\n",
    "\n",
    "On candidate si le niveau correspond ET s'il reste 3 jours."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "jours = 5\n",
    "niveau_requis = \"Master\"\n",
    "mon_niveau = \"Master\"\n",
    "\n",
    "if niveau_requis == mon_niveau and jours >= 3:\n",
    "    print(\"À CANDIDATER\")\n",
    "elif jours <= 0:\n",
    "    print(\"Trop tard\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Le quatrième faux ami\n",
    "\n",
    "Attention à la saisie `input()`. Tout peut être testé comme un booléen."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "reponse = input(\"Continuer ? (oui/non) : \")\n",
    "if reponse:  # Ceci est vrai même si l'on tape \"non\" !\n",
    "    print(\"On continue\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Atelier 1 — Le tri des opportunités\n",
    "\n",
    "Demande le nom d'une bourse et le nombre de jours restants.\n",
    "Affiche `URGENT` si moins de 4 jours, `A_PREPARER` si moins de 15, `PLUS_TARD` au-delà. Et `DEPASSE` si le nombre est négatif.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A toi de jouer\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Atelier fameux N°1 — FizzBuzz\n",
    "\n",
    "Pour chaque jour du mois (1 à 30) :\n",
    "- si le jour est un multiple de 3 et de 5 -> afficher \"FizzBuzz\"\n",
    "- sinon si multiple de 3 -> afficher \"Fizz\"\n",
    "- sinon si multiple de 5 -> afficher \"Buzz\"\n",
    "- sinon -> afficher le jour"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A toi de jouer\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "# 2 · Répéter\n",
    "\n",
    "## On regarde ensemble : for et range\n",
    "\n",
    "On répète quand on sait combien de fois avec `for`. `range` s'arrête avant la borne de fin."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(3, 7):\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## On regarde ensemble : while\n",
    "\n",
    "On répète tant qu'une condition est vraie. Il faut changer la variable à l'intérieur, sinon boucle infinie."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "n = 3\n",
    "while n > 0:\n",
    "    print(n)\n",
    "    n = n - 1\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Point de contrôle\n",
    "\n",
    "Combien de fois passe-t-on dans `for i in range(3, 7)` ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verifie ta reponse avec le code ci-dessous\n",
    "# for i in range(3, 7):\n",
    "#     print(\"Tour :\", i)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Atelier fameux N°2 — Somme d'Euler #1\n",
    "\n",
    "Calcule la somme de tous les jours du mois (1 à 30, exclu 30) qui sont multiples de 3 ou de 5."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A toi de jouer\n",
    "total = 0\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercice — Le nombre mystère\n",
    "\n",
    "- L'ordinateur choisit un nombre entre 1 et 100\n",
    "- Le joueur propose : « trop grand » ou « trop petit »\n",
    "- Compter les essais et féliciter\n",
    "- Bonus : limiter à 7 essais"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "secret = random.randint(1, 100)\n",
    "# A toi de jouer\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Atelier 2 — Le compteur de candidatures\n",
    "\n",
    "Une liste de six deadlines en jours est donnée. Compte combien sont urgentes (moins de 4 jours) et affiche le total, puis la proportion."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "deadlines = [2, 18, 1, 40, 3, 7]\n",
    "urgentes = 0\n",
    "\n",
    "# A toi de jouer\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n",
    "# 3 · Lire les erreurs\n",
    "\n",
    "## On regarde ensemble\n",
    "\n",
    "Un message d'erreur (traceback) se lit de bas en haut :\n",
    "1. Le fichier et la ligne\n",
    "2. La ligne de code fautive\n",
    "3. Le type d'erreur + le message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "total = 100\n",
    "nb_depenses = 0\n",
    "# provoque une ZeroDivisionError\n",
    "# moyenne = total / nb_depenses\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## On rembourse la dette\n",
    "\n",
    "On empeche l'erreur de se produire au lieu de la corriger apres."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "offres = 0\n",
    "envoyees = 0\n",
    "\n",
    "if offres == 0:\n",
    "    print(\"Aucune offre : rien a calculer.\")\n",
    "else:\n",
    "    print(f\"Taux : {envoyees / offres * 100:.1f} %\")\n"
   ]
  }
 ]
}

target_path = r"d:\Projects\_python-360\python-360\seances\s02-decider-et-repeter\reprise.ipynb"
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"Reprise V3 created at {target_path}")

"""Import d'un relevé hétérogène — le `match` structurel (PEP 636).

En séance 4, `match` servait de menu (comparer une variable à des valeurs).
Ici on l'utilise pour ce qu'il fait vraiment : **filtrer par la FORME** des
données. C'est le gabarit de tri à formes : le cube ne passe pas dans le rond.

Un vrai relevé bancaire importé n'a jamais deux fois la même forme : parfois
un dict, parfois une ligne CSV déjà découpée, parfois un montant en texte.
"""

from modeles import Categorie, Depense


def depuis_ligne(ligne) -> Depense | None:
    """Transforme une ligne de relevé (forme inconnue) en Depense, ou None.

    L'ordre des `case` compte : le premier motif qui correspond gagne.
    """
    match ligne:
        # 1. Dict complet, montant numérique (int OU float), avec garde.
        #    `**reste` capture les clés en trop ; `as m` nomme la valeur.
        case {"libelle": str(titre), "montant": (int() | float()) as m, **reste} if m > 0:
            return Depense(titre, float(m), Categorie.depuis_texte(reste.get("categorie", "")))

        # 2. Même forme, mais le montant est écrit en texte à la française.
        case {"libelle": str(titre), "montant": str(brut)}:
            propre = brut.replace("EUR", "").replace("€", "").replace(",", ".").strip()
            return Depense(titre, float(propre))

        # 3. Motif de SÉQUENCE : une ligne CSV déjà découpée.
        #    `*reste` absorbe les colonnes surnuméraires — ici la catégorie,
        #    si elle est présente.
        case [str(titre), montant, *reste]:
            categorie = Categorie.depuis_texte(reste[0]) if reste else Categorie.AUTRE
            return Depense(titre, float(montant), categorie)

        # 4. Motif de CLASSE : c'est déjà une Depense, on la garde telle quelle.
        case Depense():
            return ligne

        # 5. Un remboursement (montant négatif) : on l'ignore volontairement.
        case {"montant": m} if isinstance(m, (int, float)) and m < 0:
            return None

        # 6. Le joker, TOUJOURS en dernier.
        case _:
            return None


def importer(lignes) -> list[Depense]:
    """Convertit un relevé entier, en écartant silencieusement l'inexploitable."""
    resultats = (depuis_ligne(ligne) for ligne in lignes)   # générateur
    return [d for d in resultats if d is not None]


if __name__ == "__main__":
    releve = [
        {"libelle": "Loyer", "montant": 850.0, "categorie": "Logement"},
        {"libelle": "Courses", "montant": 54},                 # int
        {"libelle": "Netflix", "montant": "13,49 EUR"},        # texte français
        ["Pass Navigo", "86.40", "Transport"],                 # ligne CSV
        {"libelle": "Remboursement", "montant": -20.0},        # ignoré
        {"autre_chose": 1},                                    # inexploitable
    ]
    for depense in importer(releve):
        print(" ", depense)

"""API OpportuniTrack (séance 10).

Lancer :  uv run uvicorn main:app --reload
Ouvrir :  http://127.0.0.1:8000/docs
"""

from fastapi import Depends, FastAPI, HTTPException, Query, status
from schemas import OpportuniteCreation, OpportuniteLecture
from stockage import DepotOpportunites

app = FastAPI(
    title="OpportuniTrack API",
    description="Suivi d'opportunités : bourses, stages, appels à candidature.",
    version="1.0.0",
)
# Ces trois champs alimentent directement la page /docs.


def get_depot() -> DepotOpportunites:
    """Dépendance : fournit l'accès aux données.

    L'injection de dépendances permet de REMPLACER cette source par une fausse
    dans les tests, sans toucher au code des routes.
    """
    return DepotOpportunites()


@app.get("/opportunites", response_model=list[OpportuniteLecture], tags=["Lecture"])
def lister(
    pays: str | None = Query(None, description="Filtrer par pays"),
    urgentes_seulement: bool = False,
    depot: DepotOpportunites = Depends(get_depot),
):
    """Liste les opportunités, avec filtres optionnels.

    Cette docstring devient la description de la route dans /docs :
    documenter son code documente son API. Deux effets, un seul effort.
    """
    resultats = depot.toutes()

    if pays:
        resultats = [o for o in resultats if o.pays.casefold() == pays.casefold()]
    if urgentes_seulement:
        resultats = [o for o in resultats if o.urgente]

    return resultats
    # response_model convertit en JSON et FILTRE les champs non déclarés :
    # rien ne fuit par accident.


@app.get("/opportunites/{opp_id}", response_model=OpportuniteLecture, tags=["Lecture"])
def consulter(opp_id: int, depot: DepotOpportunites = Depends(get_depot)):
    """Consulte une opportunité par son identifiant."""
    opportunite = depot.par_id(opp_id)

    if opportunite is None:
        # Le bon code + un message utile. Ne JAMAIS rendre 200 avec un corps
        # vide pour une ressource absente : c'est mentir au client.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aucune opportunité d'identifiant {opp_id}",
        )
    return opportunite


@app.post(
    "/opportunites",
    response_model=OpportuniteLecture,
    status_code=status.HTTP_201_CREATED,  # 201 = créé, pas 200
    tags=["Écriture"],
)
def creer(
    donnees: OpportuniteCreation,  # la validation a DÉJÀ eu lieu ici
    depot: DepotOpportunites = Depends(get_depot),
):
    """Crée une opportunité.

    Si le corps de la requête est invalide, cette fonction n'est jamais appelée :
    FastAPI a répondu 422 avec le détail des champs fautifs.
    """
    return depot.ajouter(donnees)


@app.delete("/opportunites/{opp_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Écriture"])
def supprimer(opp_id: int, depot: DepotOpportunites = Depends(get_depot)):
    """Supprime une opportunité. 204 = succès, sans contenu à renvoyer."""
    if not depot.supprimer(opp_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Introuvable")


@app.get("/statistiques", tags=["Analyse"])
def statistiques(depot: DepotOpportunites = Depends(get_depot)):
    """Le groupby de la séance 8, exposé en JSON."""
    toutes = depot.toutes()

    par_pays: dict[str, int] = {}
    for opp in toutes:
        par_pays[opp.pays] = par_pays.get(opp.pays, 0) + 1

    return {
        "total": len(toutes),
        "urgentes": sum(1 for o in toutes if o.urgente),
        "par_pays": par_pays,
    }

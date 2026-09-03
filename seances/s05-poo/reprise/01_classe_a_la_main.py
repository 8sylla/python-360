"""01 — Écrire une classe de zéro : __init__, self, méthodes.

Avant les raccourcis (dataclass), on écrit une classe « à la main » pour voir
la mécanique. Une classe = un moule ; chaque objet créé = un exemplaire.
"""


# ── On regarde ensemble : un compte bancaire ─────────────────────────────
class CompteBancaire:
    """Un compte avec un titulaire et un solde."""
    banque = "ASEGUIM"  

    def __init__(self, titulaire, solde=0):
        # __init__ est le « constructeur » : il prépare le nouvel objet.
        self.titulaire = titulaire     # self = l'objet en train de naître
        self.solde = solde

    def deposer(self, montant):
        """Ajoute de l'argent (une méthode = un verbe)."""
        self.solde += montant

    def resume(self):
        """Rend une phrase décrivant le compte."""
        return f"Compte de {self.titulaire} : {self.solde:.2f} EUR"
    
    def retirer(self, montant):
        """Retire de l'argent si le solde est suffisant."""
        if montant > self.solde:
            print(f"Retrait refusé : solde insuffisant ({self.solde:.2f} EUR).")
        else:
            self.solde -= montant
            print(f"Retrait de {montant:.2f} EUR effectué. Nouveau solde : {self.solde:.2f} EUR.")


compte = CompteBancaire("Awa", 100)
compte.deposer(50)
print(compte.resume())        # Compte de Awa : 150.00 EUR


# ── À toi de jouer ───────────────────────────────────────────────────────
# TODO 1 : ajoute une méthode retirer(self, montant) qui DIMINUE le solde,
#          mais REFUSE (affiche un message et ne change rien) si le retrait
#          dépasse le solde disponible.
#
# TODO 2 : crée un deuxième compte pour "Sékou" avec 20 EUR, dépose 30,
#          essaie de retirer 100 (doit être refusé), puis affiche son résumé.

compte_sekou = CompteBancaire("Sékou", 20)
compte_sekou.deposer(30)
compte_sekou.retirer(100)  
print(compte_sekou.resume())


# ── Bonus : un attribut de CLASSE (partagé par tous les comptes) ──────────
# TODO 3 : ajoute dans la classe, AVANT __init__, une ligne  banque = "ASEGUIM"
#          (sans self). C'est un attribut de classe : le même pour tous les
#          comptes. Vérifie avec  print(compte.banque)  et  print(CompteBancaire.banque)

print(compte.banque)  # Affiche "ASEGUIM"
print(CompteBancaire.banque)  # Affiche aussi "ASEGUIM"


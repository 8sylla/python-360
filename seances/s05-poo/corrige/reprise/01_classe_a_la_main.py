"""01 — CORRIGÉ. Écrire une classe de zéro."""


class CompteBancaire:
    """Un compte avec un titulaire et un solde."""

    banque = "ASEGUIM"        # attribut de CLASSE : partagé par tous les comptes

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        """Retire, sauf si le solde est insuffisant."""
        if montant > self.solde:
            print(f"  Refusé : {self.titulaire} n'a que {self.solde:.2f} EUR.")
            return
        self.solde -= montant

    def resume(self):
        return f"Compte de {self.titulaire} ({self.banque}) : {self.solde:.2f} EUR"


compte = CompteBancaire("Awa", 100)
compte.deposer(50)
compte.retirer(30)
print(compte.resume())        # 120.00 EUR

sekou = CompteBancaire("Sékou", 20)
sekou.deposer(30)
sekou.retirer(100)            # refusé
print(sekou.resume())         # 50.00 EUR

print(compte.banque, CompteBancaire.banque)   # ASEGUIM ASEGUIM

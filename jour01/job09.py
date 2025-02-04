class Produit:
    def __init__(self):
        self.nom = ""
        self.prixHT = 0
        self.TVA = 0

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * self.TVA / 100
        return prixTTC
    
    def afficher(self):
        return self.CalculerPrixTTC()

    def changerNom(self, nouveauNom):
        self.nom = nouveauNom
    
    def changerPrix(self, nouveauPrix):
        self.prixHT = nouveauPrix

    def afficherNom(self):
        return self.nom

    def afficherPrixHT(self):
        return self.prixHT

    def afficherTVA(self):
        return self.TVA
    

truc = Produit()
truc.nom = "moi"
truc.prixHT = 120
truc.TVA = 20

print(truc.afficher())
truc.changerPrix(60)
truc.changerNom("toi")
print(truc.afficher())
print(truc.afficherPrixHT())
print(truc.afficherNom())

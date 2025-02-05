class Voiture:
    def __init__(self):
        self.__marque = ""
        self.__modele = ""
        self.__annee = 0
        self.__kilometrage = 0
        self.en_marche = False
        self.__reservoir = 50
    
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_marque(self, new_marque):
        self.__marque = new_marque

    def set_modele(self, new_modele):
        self.__modele = new_modele

    def set_annee(self, new_annee):
        self.__annee = new_annee

    def set_kilometrage(self, new_kilometrage):
        self.__kilometrage = new_kilometrage

    def demarrer(self):
        if self.en_marche == False and self.__verifier_plein() > 5:
            self.en_marche = True
        elif self.en_marche == True:
            print("Voiture déjà en marche")
        elif self.__verifier_plein() <= 5:
            print("merci de faire le plein")
    
    def arreter(self):
        if self.en_marche == True:
            self.en_marche = False
        else : print("Voiture déjà à l'arrêt")

    def __verifier_plein(self):
        return self.__reservoir


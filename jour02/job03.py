class Livre:
    def __init__(self):
        self.__titre = ""
        self.__auteur = ""
        self.__page = 0
        self.__disponible = True

    def getTitre(self):
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur

    def getPage(self):
        return self.__page

    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur
    
    def setPage(self, page):
        if type(page) == int:
            self.__page = page
        else : 
            print("Entrez un nb")
    
    def verification(self):
        if self.__disponible == True:
            return True
        else : return False

    def emprunter(self):
        if self.verification() == True:
            self.__disponible = False
        else:
            print("Livre indisponible")

    def rendre(self):
        if self.verification() == False:
            self.__disponible = True
        else :
            print("Livre non connu")

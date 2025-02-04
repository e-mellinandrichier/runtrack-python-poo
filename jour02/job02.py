class Livre:
    def __init__(self):
        self.__titre = ""
        self.__auteur = ""
        self.__page = 0

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


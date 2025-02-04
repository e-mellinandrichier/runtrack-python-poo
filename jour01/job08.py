class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouveauRayon):
        self.rayon = nouveauRayon
    
    def afficherInfos(self):
        print(self.rayon)
    
    def circonference(self):
        return(2 * 3.14 * self.rayon)

    def aire(self):
        return(3.14 * self.rayon * self.rayon)

    def diametre(self):
        return(self.rayon *2)

circle = Cercle(4)
circle2 = Cercle(7)

circle.afficherInfos()
circle.changerRayon(7)
circle.afficherInfos()
# print(circle.circonference())
# print(circle.aire())
# print(circle.diametre())

# print(circle2.circonference())
# print(circle2.aire())
# print(circle2.diametre())
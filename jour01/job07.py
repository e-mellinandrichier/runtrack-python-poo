class Personnage:
    def __init__(self):
        self.y = 0
        self.x = 0
    
    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1
    
    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1
    
    def position(self):
        return(self.y, self.x)

truc = Personnage()
print(truc.position())
truc.haut()
print(truc.position())
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f'X : {self.x}')
        print(f'Y : {self.y}')

    def afficherX(self):
        print(f'X est {self.x}')

    def afficherY(self):
        print(f'Y est {self.y}')
    
    def changerX(self, newx):
        self.x = newx

    def changerY(self, newy):
        self.y = newy

objet1 = Point(12, 24)
objet1.afficherLesPoints()
objet1.afficherX()
objet1.afficherY()
objet1.changerX(35)
objet1.afficherX()
objet1.changerY(67)
objet1.afficherY()
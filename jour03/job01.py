class Ville():
    def __init__(self):
        self.__nom = ""
        self.__habitants = 0

    def getNom(self):
        return self.__nom

    def getHabitants(self):
        return self.__habitants
    
    def setNom(self, nouveauNom):
        self.__nom = nouveauNom

    def setHabitants(self, nouveauHabitant):
        self.__habitants = nouveauHabitant

class Personne():
    def __init__(self):
        self.__nom = ""
        self.__age = 0
        self.ville = Ville()

    def getNom(self):
        return self.__nom

    def getAge(self):
        return self.__age

    def setNom(self, nouveauNom):
        self.__nom = nouveauNom

    def setAge(self, nouveauAge):
        self.__age = nouveauAge

    def ajouterPopulation(self):
        self.ville.setHabitants(self.ville.getHabitants() + 1) 

v1 = Ville()
v1.setNom("Paris")
v1.setHabitants(1000000)
print(v1.getNom())
print(v1.getHabitants())

v2 = Ville()
v2.setNom("Marseille")
v2.setHabitants(861635)

p1 = Personne()
p1.setNom("John")
p1.setAge(45)
p1.ville = v1
p1.ajouterPopulation()
print(v1.getHabitants())

p2 = Personne()
p1.setNom("Myrtille")
p1.setAge(4)
p1.ville = v1

p3 = Personne()
p1.setNom("Chloe")
p1.setAge(18)
p1.ville = v2


print(v2.getHabitants())
print(p1.ville.getNom())



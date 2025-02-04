class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        print(f"L'age de l'animal : {self.age} ans")
        self.age +=1
        print(f"L'age de l'animal : {self.age} ans")

    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal se nomme {self.prenom}")


chien = Animal()
chien.vieillir()
chien.nommer("Luna")
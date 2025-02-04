class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age +=1

chien = Animal()
chien.vieillir()
print(chien.age)
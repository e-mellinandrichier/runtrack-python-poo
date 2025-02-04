class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print(f'Je suis {self.nom} {self.prenom}')
    
x = Personne('moi', 'moi')
y = Personne('toi', 'toi')
x.SePresenter()
y.SePresenter()
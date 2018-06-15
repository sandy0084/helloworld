#declare la classe
class Singe:

    #constructeur
    def __init__(self, nom):
        #attribut
        self.nom = nom
        print('creation singe ' + self.nom)

    # declarer une methode
    def mangeBanane(self, banane):
        print(self.nom + " mange la banane " + banane.couleur)

    def reproduitSinge(self,singe,nom_enfant):
        print(self.nom + " et " + singe.nom + " reproduisent " + nom_enfant)
        enfant = Singe(nom_enfant)
        return enfant


#declare la classe
class Banane:

    #constructeur
    def __init__(self, couleur):
        #attribut
        self.couleur = couleur
        print('creation banane ' + self.couleur)


s1 = Singe('Pierre')
s2 = Singe('Marie')

b1 = Banane('Jaune')
b2 = Banane('Verte')

s1.mangeBanane(b1)
s2.mangeBanane(b2)

s3 = s1.reproduitSinge(s2, 'Robert')

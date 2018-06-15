#declare la classe
class Graphe:

    #constructeur
    def __init__(self):
        #attribut
        self.noeud = []
        self.arete = []

    # declarer une methode
    def ajouterNoeud(self, noeud):
        print(noeud + " est ajoute ")
        self.noeud.append(noeud)

    def ajouterArete(self,noeud1, noeud2):
        print("Ajouter arete entre " + noeud1 + " et " + noeud2)
        self.arete.append(noeud1 + ":" + noeud2)

    def existArete(self, n1, n2):
        for a in self.arete:
            if a == (n1 + ':' + n2):
                return True
        return False


graphe = Graphe()

graphe.ajouterNoeud('n1')
graphe.ajouterNoeud('n2')
graphe.ajouterNoeud('n3')
graphe.ajouterArete('n1', 'n2')

print(graphe.existArete('n1', 'n2'))
print(graphe.existArete('n1', 'n3'))
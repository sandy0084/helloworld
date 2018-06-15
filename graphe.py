#declare la classe
class Graphe:

    #constructeur
    def __init__(self):
        #attribut
        self.noeud = []
        #self.arete = arete
        #print('creation noeud ' + self.noeud)
        #print('creattion arete ' + self.arete)

    # declarer une methode
    def ajouterNoeud(self, noeud):
        print(noeud + " est ajoute ")
        self.noeud.append(noeud)

  #  def ajouterArete(self,arete):
  #      print(self.arete + " est ajoutee ")


graphe = Graphe()

graphe.ajouterNoeud('noeud2')
#graphe.ajouterArete('arete2')
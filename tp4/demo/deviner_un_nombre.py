# SVL CTD4

class Jeu :

    def __init__(self, generateur, lecteur, afficheur) :
        self.generateur = generateur
        self.lecteur = lecteur
        self.afficheur = afficheur

    def jouer(self) :
        nombre_secret = self.generateur.alea()
        gagne = False
        tentatives = 0
        while not gagne and tentatives != 5 :
            self.afficheur.affiche_invite()
            nombre_entre = self.lecteur.lire()
            tentatives += 1
            if nombre_secret == nombre_entre :
                gagne = True
            elif nombre_secret > nombre_entre :
                self.afficheur.affiche_trop_petit()
            else :
                self.afficheur.affiche_trop_grand()
        if gagne :
            self.afficheur.affiche_gagne()
        else :
            self.afficheur.affiche_perd()


class Lecteur :

    def __init__(self, flot_entree=sys.stdin) :
        self.flot = flot_entree

    def lire(self) :
        return int(self.flot.readline())

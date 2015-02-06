# ex bibliotheque - SVL 1415 - M. Nebut

"""
Service des emprunts de la bibliothèque.

Comportements à tester :
- cas nominal
- cas exceptionnel : le membre a atteint son quota
- cas exceptionnel : le livre n'est que consultable
"""

class ServiceDEmprunt :

    def __init__(self, lesemprunts) :
        self.emprunts = lesemprunts

    def emprunter(self, livre, carte)  :
        if not livre.est_empruntable() :
            raise LivreNonEmpruntableError()
        self.emprunts.ajouterEmprunt(livre, carte)

class LivreNonEmpruntableError(Exception) :
    pass

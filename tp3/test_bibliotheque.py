# ex bibliotheque - SVL 1415 - M. Nebut

import unittest
from mockito import *
from bibliotheque import *

class TesterUnEmprunt(unittest.TestCase) :

    def setUp(self) :
        self.livre = mock()
        self.carte = mock()
        self.stockageEmprunts = mock()
        self.service = ServiceDEmprunt(self.stockageEmprunts)
        

    def test_cas_nominal_emprunt_reussi(self) :
        
        when(self.livre).est_empruntable().thenReturn(True)
        
        self.service.emprunter(self.livre, self.carte)

        verify(self.stockageEmprunts).ajouterEmprunt(self.livre, self.carte)

    def test_emprunt_echoue_car_livre_non_empruntable(self) :
        
        when(self.livre).est_empruntable().thenReturn(False)
        
        self.assertRaises(LivreNonEmpruntableError,
                          self.service.emprunter,
                          self.livre, self.carte)



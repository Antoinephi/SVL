# SVL 14-15 - M. NEBUT
# démo prog par contrats avec contract pour Python

import mockito
import unittest

class TestBoite(unittest.TestCase):

    # ce test ne passe pas si les contrats sont actives
    def test_ouvrir_la_boite_ouvre_les_clapets(self):
        clapet1 = mock()
        clapet2 = mock()
        boite = Boite([clapet1, clapet2])

        boite.ouvrir()

        verify(clapet1).ouvrir()
        verify(clapet2).ouvrir()

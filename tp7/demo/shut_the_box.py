# SVL 14-15 - M. NEBUT
# demo prog par contrats avec contract pour Python

class Boite:

    def __init__(self, liste_clapets):
        self.clapets = liste_clapets

    def ouvrir():
        """
        post:
             forall(self.clapets, Clapet.est_ouvert)
        """
        for clapet in self.clapets:
            clapet.ouvrir()


class Clapet:

    def __init__(self):
        self.ouvert = True

    def est_ouvert(self):
        return self.ouvert

    def ouvrir(self):
        self.ouvert = True

import contract
contract.checkmod(__name__)

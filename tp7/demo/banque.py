# SVL 14-15 - M. NEBUT
# démo prog par contrats avec contract pour Python

class Compte :
    """
    Le decouvert peut etre autorise. 
    inv:
        implies(self.decouvert_autorise,
                self.montant >= self.decouvert,
                self.montant >= 0)

    """

    def __init__(self):
        """
        post:
             self.montant == 0.0
             self.decouvert_autorise == False
             self.decouvert == - 400
        """
        self.montant = 0.0
        self.decouvert_autorise = False
        self.decouvert = - 400.0

    def crediter(self, somme):
        """
        pre:
            somme > 0
        post[self.montant]:
            self.montant == __old__.self.montant + somme
        """
        self.montant += somme

    def debiter(self, somme):
        """
        pre:
            somme > 0
            implies(self.decouvert_autorise,
                    self.montant - somme > self.decouvert,
                    self.montant > somme)
        """
        self.montant -= somme

# ne respecte pas le principe de substitution de Liskov
class ComptePlafonne(Compte):

    def __init__(self, plafond):
        self.plafond = plafond
        self.montant = 0.0
        self.decouvert_autorise = False
        self.decouvert = - 400.0


    def crediter(self, somme):
        """
        pre :
            somme > 0
            self.montant + somme <= self.plafond # invalide du point de vue de la précond
        """
        self.montant += somme
    
import contract
contract.checkmod(__name__)

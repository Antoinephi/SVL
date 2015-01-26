# TP2 SVL - Damien CORNETTE / Antoine PHILIPPE M1S2 2015


"""
Caisse : Une caisse permet de lire, et debiter une carte de son solde monetaire et/ou de tickets.

******** Verification de la presence de la carte *********
On verifie avant toute action que la carte est bien inseree, sinon on renvoit une erreur.

>>> caisse = Caisse()
>>> carte = Carte()
>>> caisse.solde_porte_monnaie()
Traceback (most recent call last):
...
restaurant.CarteNonInsereeErreur

******** Affichage du solde de la carte ************
>>> caisse.inserer_carte(carte)
>>> caisse.crediter_porte_monnaie_carte(20.0)
>>> caisse.solde_porte_monnaie()
20.0

"""


class Caisse :

	def __init__(self):
		self.carte = None

	def solde_porte_monnaie(self):
		if self.carte == None :	
			raise CarteNonInsereeErreur()

		return self.carte.get_solde_porte_monnaie()

	def inserer_carte(self, une_carte):
		self.carte = une_carte

	def crediter_porte_monnaie_carte(self, montant):
		self.carte.crediter_porte_monnaie(montant)

	def payer_repas_monnaie(self, montant):
		self.carte.debiter_porte_monnaie(montant)


class CarteNonInsereeErreur(Exception):
	pass

class SoldeNegatifErreur(Exception):
	pass


class Carte :


	def __init__(self) :
		self.solde_porte_monnaie = 0

	def get_solde_porte_monnaie(self) :
		return self.solde_porte_monnaie

	def crediter_porte_monnaie(self, montant) :
		if montant < 0.0 :
			raise CreditNegatifErreur
		self.solde_porte_monnaie += montant

	def debiter_porte_monnaie(self, montant) :
		if montant > self.solde_porte_monnaie :
			raise SoldeInsuffisantErreur
		if montant < 0.0 :
			raise DebitNegatifErreur
		self.solde_porte_monnaie -= montant

class CreditNegatifErreur(Exception) :
	pass

class DebitNegatifErreur(Exception) :
	pass

class SoldeInsuffisantErreur(Exception):
	pass
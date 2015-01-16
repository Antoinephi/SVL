# TP1 SVL Antoine PHILIPPE / Damien CORNETTE
"""
	Representation d'un compte bancaire.

>>> compte = Compte()

Un compte est cree vide.

>>> compte.solde()
0.0

On peut crediter sur ce compte.

>>> compte.crediter(20.0)
>>> compte.solde()
20.0

On ne peut pas crediter negativement sur le compte.

>>> compte.crediter(-20.0)
Traceback (most recent call last):
...
banque.CreditNegatifError

On peut debiter sur ce compte.

>>> compte.debiter(20.0)
>>> compte.solde()
0.0

On ne peut pas debiter negativement sur le compte.

>>> compte.debiter(-20.0)
Traceback (most recent call last):
...
banque.DebitNegatifError
"""


class Compte :

	def __init__(self) :
		self.solde_interne = 0.0

	def solde(self) :
		return self.solde_interne

	def crediter(self, montant) :
		
		if montant < 0 :
			raise CreditNegatifError

		self.solde_interne += montant

	def debiter(self, montant) :
		
		if montant < 0 :
			raise DebitNegatifError

		self.solde_interne -= montant


class CreditNegatifError(Exception) :
	pass

class DebitNegatifError(Exception) :
	pass
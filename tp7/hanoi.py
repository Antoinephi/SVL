# Damien Cornette & Antoine PHILIPPE
# SVL - TP7 - 20 Mars 2015

class Disque:

	"""
	La taille ne peut pas etre <= 0.
	inv:
		self.taille > 0
	"""

	def __init__(self, taille):
		"""
			post :
				self.taille == taille
		"""
		self.taille = taille


class Pile:


	"""
		Une pile contient une liste de disques, initiallement vide.

		self.liste_disques.__len__() == 0

		La pile possede une taille maximum.

		self.taille > 0
		self.liste_disques.__len__() <= taille 

	"""

	def __init__(self, taille):
		"""
			post :
				self.taille == taille
				self.liste_disques == []
		"""
		self.liste_disques = []
		self.taille = taille


	def ajouter_disque(self, disque):
		"""
			post[self.liste_disques] :
				self.liste_disques.__len__() == __old__.self.liste_disques.__len__() + 1
				disque in self.liste_disques
			pre :
				self.liste_disques == [] or self.liste_disques[-1].taille > disque.taille 

		"""
		if self.liste_disques.__len__() < self.taille :
			self.liste_disques.append(disque)
		else :
			raise PilePleineException()

	def retirer_disque(self):
		"""
			post[self.liste_disques] :
				self.liste_disques.__len__() == __old__.self.liste_disques.__len__() - 1	
		"""
		if self.liste_disques.__len__() > 0 :
			return self.liste_disques.pop()
		else :
			raise PileVideException()


class PilePleineException(Exception):
	pass

class PileVideException(Exception):
	pass

import contract
contract.checkmod(__name__)


#SVL TP5 Damien CORNETTE / Antoine PHILIPPE
from random import randint


"""

class LancerDes:
	pass

Tests Lancé de dés :

- cas nominal 

class Joueur:
	pass

class Clapet:
	pass

Test clapet :

etat, numero

getEtat
setEtat
getNumero

- cas nominal : clapet ouvert

- cas exceptionnel :
	=> fermer clapet déjà fermé
	=> clapet valeur incorrecte


class Jeu:
	pass

	=> Liste de 9 clapets
	=> Liste de 2 joueurs

	fermer_claper(numero)
		=> Mock verifer appel à fermer() du clapet 




"""


class LancerDe():

	def lancer(self):
		return randint(1,6)
		
class Clapet():

	def __init__(self, numero):
		if numero > 9 or numero < 1:
			raise NumeroClapetIncorrectErreur()
		self.numero = numero
		self.estOuvert = True


	def fermer(self):
		if not self.estOuvert :
			raise ClapetDejaFermeErreur()

		self.estOuvert = False
		return True


class ClapetDejaFermeErreur(Exception):
	pass

class NumeroClapetIncorrectErreur(Exception):
	pass

class BoiteFermeErreur(Exception):
	pass


"""

Jeu 

1 tour :
>>> J1 joue tant que : clapet ouvert && non bloqué
>>> J2 // etc

=> 10 tours ou fermer tous les clapets

"""
class Boite :

	def __init__(self):
		self.listeClapets = []

	def init_clapets(self):
		for i in range(8):
			self.listeClapets.append(Clapet(i+1))

	def getListeClapets(self):
		return self.listeClapets

	def getListeClapetsOuverts(self):
		pass

	def boiteFermee(self):
		pass

	def fermerClapets(self, clapetsAFerme):
		for clapet in clapetsAFerme :
			self.listeClapets[clapet].fermer()

class Partie :

	def lancer_partie(self, joueur, boite):
		valeur_des = joueur.lancer_des()
		valeur_clapets = joueur.proposer_clapets(valeur_des)
		boite.fermerClapets(valeur_clapets)

class Joueur :
	pass


class Jeu :

	def __init__(self, boite, partie, j1, j2):
		self.j1 = j1
		self.j2 = j2
		self.boite = boite
		self.nbTour = 0
		self.partie = partie

	def changer_joueur(self, joueur):
		return self.j2 if joueur == self.j1 else self.j1

	def jouer(self, joueur):
		while self.nbTour < 10 :
			self.partie.lancer_partie(joueur, self.boite)
			if self.boite.boiteFermee() :
				raise BoiteFermeErreur()
			joueur = self.changer_joueur(joueur)
			self.nbTour += 1





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

class Jeu :

	def __init__(self):
		self.j1 = None
		self.j2 = None
		self.listeClapet = None



# Antoine PHILIPPE CTP SVL



"""
Un clapet a 2 etat : ouvert et ferme

>>> clapet = Clapet()

Il est initialise ouvert
>>> clapet.estOuvert()
True

On peut le fermer
>>> clapet.fermer()
>>> clapet.estOuvert()
False

Et le réouvrir
>>> clapet.ouvrir()
>>> clapet.estOuvert()
True

"""


class Clapet:

	def __init__(self):
		self.ouvert = True

	def fermer(self):
		self.ouvert = False

	def ouvrir(self):
		self.ouvert = True

	def estOuvert(self):
		return self.ouvert

class Boite:

	def __init__(self):
		self.listeClapets = []

	def ajouterClapet(self, clapet):
		self.listeClapets.append(clapet)

	def ouvrir(self):
		for clapet in self.listeClapets :
			clapet.ouvrir()

	def fermerClapet(self, numClapet):
		self.listeClapets[numClapet].fermer()
		if self.estFermee() :
			raise ShutTheBoxException


	def estFermee(self):
		for clapet in self.listeClapets :
			if clapet.estOuvert() :
				return False
		return True

	def estOuverte(self):
		for clapet in self.listeClapets :
			if not clapet.estOuvert() :
				return False
		return True


class ShutTheBoxException(Exception):
	pass
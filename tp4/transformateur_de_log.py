# TP4 SVL Damien CORNETTE / Antoine PHILIPPE

import sys

"""

transformateur = TransformateurLog()

transformateur.setLecteur(lecteur)

transformateur.getMessage()



Lecteur => fichier, ouvre => lit ligne/ligne


"""

class TransformateurLog :

	def __init__(self):
		self.lecteur = None
	
	def setLecteur(self, lecteur):
		self.lecteur = lecteur

	def getMessage(self):
		if self.lecteur == None:
			raise LecteurNonInitialiseErreur()
		else :
			return self.lecteur.lireMessage()

	def estPrioritaire(self, message):
		return (message[1] >= 5)

	def ecrireMessageLog(self, message, fichier=sys.stdout):
		fichier.write(message)

class LecteurNonInitialiseErreur(Exception):
	pass
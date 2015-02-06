# SVL - TP3 - M1S2 - Damien CORNETTE / Antoine PHILIPPE


"""

Utilisateur = nom, prenom, login (max 8 lettres min sans accents)

Creation d'un login utilisateur, cas nominal succes.
>>> admin = Administrateur()
>>> admin.creer_login("titi", "toto")
titi



"""


class Administration :
	
	def __init__(self, bdd):
		self.bdd = bdd


	def creer_login(self, nom, prenom):
		login = nom[:8].lower()

		"""Si login existe deja en bdd"""
		if self.bdd.verifier_login(login) :
			new_login = nom[:7] + prenom[0]

			"""Si new_login existe egalement en bdd"""
			if self.bdd.verifier_login(new_login):
				self.saisir_login()
				raise LoginDejaExistantErreur()

			return new_login
		else :
			return login
	
	def saisir_login(self):
		self.bdd.ajouter_login()


class CalculChaine :

	def calcul_8_login(self, nom):
		return nom[:8].lower()

	def calcul_7_nom_1_prenom_login(self, nom, prenom):
		return nom[:7] + prenom[0]

class LoginDejaExistantErreur(Exception):
	pass
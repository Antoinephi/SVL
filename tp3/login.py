# SVL - TP3 - M1S2 - Damien CORNETTE / Antoine PHILIPPE


"""

Utilisateur = nom, prenom, login (max 8 lettres min sans accents)

Creation d'un login utilisateur, cas nominal succes.
>>> admin = Administration()
>>> admin.creer_login("titi", "toto")
titi

Creation d'un login utilisateur avec une longueur de nom > 8
>>> admin.creer_login("nom_tres_long")
nom_tres 



"""


class Administration :
	
	def __init__(self, bdd):
		self.bdd = bdd

	def creer_login(self, nom, prenom):
		login = CalculChaine.calcul_8_login(nom)

		"""Si login existe deja en bdd"""
		if self.bdd.verifier_login(login) :
			new_login = CalculChaine.calcul_7_nom_1_prenom_login(nom, prenom)

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
	@staticmethod
	def calcul_8_login(nom):
		login = nom[:8].lower()
		if len(login) == 0:
			raise ChaineVideErreur()
		return nom[:8].lower()

	def calcul_7_nom_1_prenom_login(nom, prenom):
		login = (nom[:7] + prenom[:1]).lower()
		if len(login) == 0:
			raise ChaineVideErreur()

		return login


class LoginDejaExistantErreur(Exception):
	pass

class ChaineVideErreur(Exception):
	pass
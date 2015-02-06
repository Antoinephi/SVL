# SVL - TP3 - M1S2 - Damien CORNETTE / Antoine PHILIPPE

import unittest
from login import *
from mockito import *

class TestLogin(unittest.TestCase):

	"""Declaration des principaux objets et mocks"""
	def setUp(self):
		self.bdd = mock()
		self.admin = Administration(self.bdd)


	"""Creation d'un login utilisateur, cas nominal succes."""
	def test_creation_login_succes(self):
		self.assertEqual(self.admin.creer_login("nom_tres_long", "prenom_tres_long"), "nom_tres")

	def test_creation_login_trop_longueur(self):
		self.assertTrue(len(self.admin.creer_login("nom_tres_long", "prenom_tres_long")) <= 8)

	def test_creation_login_maj_succes(self):
		self.assertEqual(self.admin.creer_login("NOM_TRES_LONG", "prenom_tres_long"), "nom_tres")

	def test_creation_login_deja_existant_une_fois(self):
		when(self.bdd).verifier_login("nom_tres").thenReturn(True)
		self.assertEqual(self.admin.creer_login("nom_tres_long", "prenom_tres_long"), "nom_trep")

	def test_creation_login_deja_existant_deux_fois(self):
		when(self.bdd).verifier_login("nom_tres").thenReturn(True)
		when(self.bdd).verifier_login("nom_trep").thenReturn(True)
		self.assertRaises(LoginDejaExistantErreur, self.admin.creer_login, "nom_tres_long", "prenom_tres_long")

class TestCalculChaine(unittest.TestCase):

	def test_calcul_8_login_chaine_ok(self):
		self.assertEqual(CalculChaine.calcul_8_login("nom_tres_long"), "nom_tres")

	def test_calcul_calcul_7_nom_1_prenom_login_ok(self):
		self.assertEqual(CalculChaine.calcul_7_nom_1_prenom_login("nom_tres_long", "prenom_tres_long"), "nom_trep")

	def test_chaine_vide_erreur_calcul_login(self):
		self.assertRaises(ChaineVideErreur, CalculChaine.calcul_8_login, "")

	def test_chaine_vide_erreur_calcul_login_deux(self):
		self.assertRaises(ChaineVideErreur, CalculChaine.calcul_7_nom_1_prenom_login, "", "")


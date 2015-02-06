# SVL - TP3 - M1S2 - Damien CORNETTE / Antoine PHILIPPE

import unittest
from login import *
from mockito import *

class TestLogin(unittest.TestCase):


	def setUp(self):
		self.bdd = mock()
		self.admin = Administration(self.bdd)

	def test_creation_login_succes(self):
		self.assertEqual(self.admin.creer_login("titi", "toto"), "titi")

	def test_creation_login_maj_succes(self):
		self.assertEqual(self.admin.creer_login("TITI", "toto"), "titi")

	def test_creation_login_deja_existant_une_fois(self):
		when(self.bdd).verifier_login("titi").thenReturn(True)
		self.assertEqual(self.admin.creer_login("titi", "toto"), "titit")

	def test_creation_login_deja_existant_deux_fois(self):
		when(self.bdd).verifier_login("titi").thenReturn(True)
		when(self.bdd).verifier_login("titit").thenReturn(True)
		self.assertRaises(LoginDejaExistantErreur, self.admin.creer_login, "titi", "toto")

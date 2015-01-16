# TP1 SVL Antoine PHILIPPE / Damien CORNETTE

import unittest
from banque import Compte
from banque import CreditNegatifError
from banque import DebitNegatifError


class TestCreationCompte(unittest.TestCase) :

	def test_un_compte_est_cree_avec_solde_nul(self) :
		compte = Compte()
		self.assertEqual(compte.solde(), [])


class TestCrediterCompte(unittest.TestCase) :
	def setUp(self) :
		self.compte = Compte()

	def test_un_compte_est_crediter(self):
		self.compte.crediter(20.0)
		self.assertEqual(self.compte.solde(), [20.0])

	def test_on_ne_peut_pas_crediter_un_montant_negatif(self) :
		self.assertRaises(CreditNegatifError,
					self.compte.crediter,
					-20.0)
class TestDebiterCompte(unittest.TestCase) :
	
	def setUp(self) :
		self.compte = Compte()

	def test_un_compte_est_debite(self):
		self.compte.debiter(20.0)
		self.assertEqual(self.compte.solde(), [-20.0])

	def test_on_ne_peut_pas_debiter_un_montant_negatif(self) :
		self.assertRaises(DebitNegatifError, self.compte.debiter, -20.0)


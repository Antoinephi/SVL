## TP2 SVL - Damien CORNETTE / Antoine PHILIPPE M1S2 2015

import unittest
from restaurant import *
from mockito import *

class TestCaisse(unittest.TestCase) :

	def setUp(self) :
		self.caisse = Caisse()
		self.carte = mock()

	def test_verif_carte_inseree_erreur(self) :
		self.assertRaises(CarteNonInsereeErreur, self.caisse.solde_porte_monnaie)

	def test_affichage_solde_carte(self) :
		when(self.carte).get_solde_porte_monnaie().thenReturn(20.0)
		self.caisse.inserer_carte(self.carte)
		self.assertEqual(self.caisse.solde_porte_monnaie(), 20.0)

	def test_crediter_porte_monnaie_carte(self):
		self.caisse.inserer_carte(self.carte)
		self.caisse.crediter_porte_monnaie_carte(20.0)
		verify(self.carte).crediter_porte_monnaie(20.0)

	def test_payer_repas_monnaie_avec_exception(self):
		when(self.carte).debiter_porte_monnaie(15.0).thenRaise(SoldeNegatifErreur)
		self.caisse.inserer_carte(self.carte)
		self.assertRaises(SoldeNegatifErreur, self.caisse.payer_repas_monnaie, 15.0)

	def test_payer_repas_monnaie_sans_erreur(self):
		self.caisse.inserer_carte(self.carte)
		self.caisse.payer_repas_monnaie(15.0)
		verify(self.carte).debiter_porte_monnaie(15.0)


class TestCarte(unittest.TestCase) :

	def setUp(self) :
		self.carte = Carte()

	def test_affichage_solde(self) :
		self.assertEqual(self.carte.get_solde_porte_monnaie(), 0)

	def test_crediter_solde_monnaie(self) :
		self.carte.crediter_porte_monnaie(20.0)
		self.assertEqual(self.carte.get_solde_porte_monnaie(), 20.0)

	def test_crediter_solde_monnaie_negatif_erreur(self):
		self.assertRaises(CreditNegatifErreur, self.carte.crediter_porte_monnaie, -20)

	def test_debiter_solde_monnaie(self):
		self.carte.crediter_porte_monnaie(20.0)
		self.carte.debiter_porte_monnaie(15.0)
		self.assertEqual(self.carte.get_solde_porte_monnaie(), 5.0)

	def test_debiter_solde_monnaie_negatif_erreur(self):
		self.assertRaises(DebitNegatifErreur, self.carte.debiter_porte_monnaie, -20)

	def test_debiter_solde_superieur_montant_porte_monnaire(self):
		self.assertRaises(SoldeInsuffisantErreur, self.carte.debiter_porte_monnaie, 20.0)

#SVL TP5 Damien CORNETTE / Antoine PHILIPPE

import unittest
from mockito import *
from shut_the_box import *

# class TestLanceDe(unittest.TestCase):

# 	def setUp(self):
# 		self.lanceDe = LancerDe()


# 	def test_lancer_un_de_ok(self):
# 		myRandom = mock()
# 		when(myRandom).ran().thenReturn(5)
# 		self.assertEqual(self.lanceDe.lancer(lambda: myRandom.ran()), 5)

class TestClapet(unittest.TestCase):

	def setUp(self):
		self.clapet = Clapet(1)

	def test_clapet_numero_incorrect(self):
		self.assertRaises(NumeroClapetIncorrectErreur,  Clapet, 10)

	def test_clapet_ouvert(self):
		self.assertTrue(self.clapet.fermer())

	def test_clapet_deja_fermer_erreur(self):
		self.clapet.fermer()
		self.assertRaises(ClapetDejaFermeErreur, self.clapet.fermer)

class TestBoite(unittest.TestCase):
	def setUp(self):
		self.boite = Boite()

	def test_clapets_init_ok(self):
		self.boite.init_clapets()
		self.assertTrue(len(self.boite.getListeClapets()) > 0)

class TestJeu(unittest.TestCase):

	def setUp(self):
		self.j1 = mock()
		self.j2 = mock()
		self.boite = mock()
		self.partie = mock()
		self.jeu = Jeu(self.boite, self.partie, self.j1, self.j2)

	def test_partie_10_tour(self):
		self.jeu.jouer(self.j1)
		verify(self.partie, times=5).lancer_partie(self.j1, self.boite)
		verify(self.partie, times=5).lancer_partie(self.j2, self.boite)

	def test_partie_avec_boite_ferme(self):
		when(self.boite).boiteFermee().thenReturn(True)
		self.assertRaises(BoiteFermeErreur, self.jeu.jouer, self.j1)

class TestPartie(unittest.TestCase):

	def setUp(self):
		self.partie = Partie()
		self.j1 = mock()
		self.boite = mock()

	def test_execution_tour_joueur(self):
		when(self.j1).lancer_des().thenReturn(10)
		when(self.j1).proposer_clapets(10).thenReturn([4,6])
		self.partie.lancer_partie(self.j1, self.boite)
		verify(self.boite).fermerClapets([4,6])
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

class TestJeu(unittest.TestCase):

	def setUp(self):
		self.jeu = Jeu()


	def test_clapets_init_ok(self):
		self.jeu.init_clapets()
		self.assertTrue(len(self.jeu.getListeClapets()) > 0)

# Antoine PHILIPPE CTP SVL

import unittest
from mockito import *
from shut_the_box import *

class TestClapet(unittest.TestCase):

	def setUp(self):
		self.clapet = Clapet()


	def test_clapet_initialement_ouvert(self):
		self.assertTrue(self.clapet.estOuvert())

	def test_clapet_fermeture(self):
		self.clapet.fermer()
		self.assertFalse(self.clapet.estOuvert())

	def test_clapet_ouverture(self):
		self.clapet.fermer()
		self.clapet.ouvrir()
		self.assertTrue(self.clapet.estOuvert())


class TestBoite(unittest.TestCase):
	
	def setUp(self):
		self.boite = Boite()
		self.clapet_1 = mock()
		self.clapet_2 = mock()
		self.boite.ajouterClapet(self.clapet_1)
		self.boite.ajouterClapet(self.clapet_2)

	def test_ouverture_de_la_boite(self):
		when(self.clapet_1).estOuvert().thenReturn(True)
		when(self.clapet_2).estOuvert().thenReturn(True)
		self.boite.ouvrir()
		self.assertTrue(self.boite.estOuverte())

	def test_fermeture_1_clapet(self):
		when(self.clapet_2).estOuvert().thenReturn(True)
		self.boite.fermerClapet(0)
		verify(self.clapet_1).fermer()

	def test_fermeture_boite_declenche_exception(self):
		when(self.clapet_1).estOuvert().thenReturn(False)
		when(self.clapet_2).estOuvert().thenReturn(False)
		self.assertRaises(ShutTheBoxException, self.boite.fermerClapet, 1)
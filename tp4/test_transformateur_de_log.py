# TP4 SVL Damien CORNETTE / Antoine PHILIPPE

import unittest
from mockito import *
from transformateur_de_log import *
from io import StringIO
import sys

class TestTransformateurLog(unittest.TestCase):

	def setUp(self):
		self.lecteur = mock()
		self.transformateur = TransformateurLog()

	def test_set_lecteur_ok(self):
		self.transformateur.setLecteur(self.lecteur)
		assert self.transformateur.lecteur is not None


	def test_set_lecteur_erreur(self):
		assert self.transformateur.lecteur is None

	def test_get_message_ok(self):
		MSG = ["2015-02-06", 6, "error"]
		self.transformateur.setLecteur(self.lecteur)		
		when(self.lecteur).lireMessage().thenReturn(MSG)
		self.assertEqual(self.transformateur.getMessage(), MSG)

	def test_get_message_erreur(self):
		MSG = None
		self.assertRaises(LecteurNonInitialiseErreur, self.transformateur.getMessage)

	def test_message_prioritaire(self):
		MSG = ["2015-02-06", 6, "error"]
		self.assertTrue(self.transformateur.estPrioritaire(MSG))

	def test_message_non_prioritaire(self):
		MSG = ["2015-02-06", 4, "error"]
		self.assertFalse(self.transformateur.estPrioritaire(MSG))


	def test_ecire_message_log(self):
		message = "2015-02-06, 6, error"
		flot_sortie = StringIO()
		self.transformateur.ecrireMessageLog(message)
		self.assertEqual(flot_sortie.readline(), message)



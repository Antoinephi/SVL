# Damien Cornette & Antoine Philippe


from selenium import webdriver
import unittest

class testCalculIMC(unittest.TestCase):


	#Si on utilse cette methode, les tests suivant echouent, on ne sait pas pourquoi
	# @classmethod
	# def setUpClass(cls):
	# 	cls.navigateur = webdriver.Firefox()
	# 	cls.navigateur.get('http://localhost:8080')

	@classmethod
	def setUp(cls):
		cls.navigateur = webdriver.Firefox()
		cls.navigateur.get('http://localhost:8080')


	@classmethod
	def tearDownClass(cls):
		cls.navigateur.quit()

	def test_titre_page(self):
		self.assertEqual(self.navigateur.title, "IMC")

	def test_input_taille(self):
		boite = self.navigateur.find_element_by_id("saisie_taille")
		name = boite.get_attribute("name")
		self.assertEqual(name, "taille")

	def test_envoi_donnee_taille(self):
		boite = self.navigateur.find_element_by_id("saisie_taille")
		boite.send_keys("177\n")
		resultat = self.navigateur.find_element_by_id("resultat")
		self.assertEqual(resultat.text, "Résultat : 70.25 Kg")
# Damien Cornette & Antoine Philippe 

"""
taille x 100 - 100 - (taille x 100 - 150) / 4
"""

import cherrypy

PAGE_ACCUEIL = """
		<html>
			<head>
				<title>IMC</title>
			</head>
			<body>
				<form action="/calcul">
					<input type="text" name="taille" placeholder="Saisir taille" id="saisie_taille"></input>
					<input type="submit" value="Valider"></input>
				</form>
			</body>
		</html>
"""
  
class CalculIMC:

	@cherrypy.expose
	def index(self):
		return PAGE_ACCUEIL

	@cherrypy.expose
	def calcul(self, taille=None):
		if not taille:
			taille = 0
		page = """
		<html>
			<body>
				<div id="resultat">Résultat : 
		"""
		page += str(self._calcul(int(taille)))
		page +=	""" Kg
				</div>
			</body>
		</html>
		"""
		return page

	def _calcul(self, taille):
		return (taille  - 100 - (taille - 150) / 4)


class MavauseSaisieErreur(Exception):
	pass


cherrypy.quickstart(CalculIMC())
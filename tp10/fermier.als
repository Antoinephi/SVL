// SVL TP10 Damien Cornette & Antoine PHILIPPE 

module fermier
open util/ordering[Etat]

abstract sig Personnage {
	mange : lone Personnage
}

one sig Chou extends Personnage {}
one sig Loup extends Personnage {}
one sig Chevre extends Personnage {}
one sig Fermier extends Personnage {}

sig Etat {
	rive_droite : set Personnage,
	rive_gauche : set Personnage,
	mort : set Personnage,
}


/******* Invariants ********/


fact qui_mange_qui {
	Loup.mange = Chevre
	Chevre.mange = Chou
	Chou.mange = none
	Fermier.mange = none
}

fact un_personnage_n_a_qu_un_etat {
   all etat : Etat | disj[etat.rive_droite, etat.rive_gauche, etat.mort] // disj : predicat predefini Alloy
}

fact un_personnage_a_un_etat {
  all etat : Etat | etat.rive_droite + etat.rive_gauche + etat.mort= Personnage
}


fact etat_initial {
  first.rive_gauche = Personnage
  first.rive_droite = none // ens vide
  no first.mort
}

fact etat_final {
  last.rive_droite = Personnage
  last.rive_gauche  = none
  no last.mort
}

/******* Fonctions ********/


fun qui_est_mange (personnages : set Personnage) : set Personnage {
	personnages.mange
}


/******** predicats *******/


pred fermier_passe_droite_a_gauche(f : Fermier, avant : Etat, apres : Etat) {
	f in avant.rive_droite
	apres.rive_droite = avant.rive_droite - f
	apres.rive_gauche = avant.rive_gauche + f
}

pred fermier_passe_gauche_a_droite(f : Fermier, avant : Etat, apres : Etat) {
	f in avant.rive_gauche
	apres.rive_droite = avant.rive_droite + f
	apres.rive_gauche = avant.rive_gauche - f
}

pred fermier_passe_droite_a_gauche_avec_personnage(f : Fermier, p : Personnage, avant : Etat, apres : Etat) {
	p in avant.rive_droite
	f in avant.rive_droite
	apres.rive_droite = avant.rive_droite - f - p
	apres.rive_gauche = avant.rive_gauche + f + p
}

pred fermier_passe_gauche_a_droite_avec_personnage(f : Fermier, p : Personnage, avant : Etat, apres : Etat) {
	p in avant.rive_gauche
	f in avant.rive_gauche
	apres.rive_droite = avant.rive_droite + f + p
	apres.rive_gauche = avant.rive_gauche - f - p
}

pred fermier_passe_rive(f : Fermier, p : lone Personnage, avant : Etat , apres : Etat){
	
}

pred generate {}



/******* commandes **********/

run generate for 4 Etat
run fermier_passe_droite_a_gauche for 3 Etat
run fermier_passe_gauche_a_droite for 3 Etat
run fermier_passe_droite_a_gauche_avec_personnage for 3 Etat
run fermier_passe_gauche_a_droite_avec_personnage for 3 Etat
run fermier_passe_rive for 3 Etat

// SVL TP10 Damien Cornette & Antoine PHILIPPE 

module fermier
open util/ordering[Etat]

abstract sig Object {}
one sig Chou extends Object {}
one sig Loup extends Object {
	mange : Chevre
}
one sig Chevre extends Object {
	mange : Chou
}
one sig Fermier extends Object {}

one sig Etat {
	rive_droite : set Object,
	rive_gauche : set Object 
}
/******* Fonctions ********/

fun qui_manque_qui(groupe : set Object) : set Object {
	

}




/******** predicats *******/

pred passage_droite_sans_objet(e : Etat, e' : Etat, f : Fermier){
	e'.rive_gauche = e.rive_gauche - f 
	e'.rive_droite = e.rive_droite + f
}

pred passage_droite_avec_object(e : Etat, e' : Etat, f : Fermier, o : Object){
	e'.rive_gauche = e.rive_gauche  - f - o
	e'.rive_gauche = e.rive_gauche  - o
	e'.e.rive_droite = e.rive_droite +  o
	e'.e.rive_droite = e.rive_droite + f  
}

pred passage_gauche_sans_objet(e : Etat, e' Etat, f : Fermier){
	e'.rive_droite = e.rive_droite - f 
	e'.rive_gauche = rive_gauche + f
}

pred passage_gauche_avec_objet(e : Etat, e' Etat, f : Fermier, o : Object){
	e'.rive_droite = e.rive_droite - f 
	e'.rive_droite = e.rive_droite  - o
	e'.rive_gauche = rive_gauche + f 
	e'.rive_gauche = rive_gauche + o
}

/******* commandes **********/

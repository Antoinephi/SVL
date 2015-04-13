// SVL 1415
// demo CTD10
// carnet d'adresse avec traces de Carnet

module carnet_precond
open util/ordering[Carnet]

sig Identifiant{}
sig Surnom {}
sig Adresse {}
sig Carnet {
   id : Identifiant,
   nommage : Surnom -> lone Adresse // 0 ou 1
}

/******** operations *******/

pred ajout(c : Carnet, c' : Carnet, s : Surnom, a : Adresse) {
   no s.(c.nommage) // precond
   c'.id = c.id
   c'.nommage = c.nommage + s -> a
}



fact carnet_initial_vide {
    no first.nommage
}

fact carnets_successifs {
    all c : Carnet - last, c' : Carnet | c' = next[c] implies some s : Surnom, a : Adresse | ajout[c,c',s,a]   
}

/******** predicats *******/


/******** assertions ********/

// faux : le contre-ex sera une trace
assert aucune_adresse_mapee_par_2_surnoms {
    all c : Carnet, a : Adresse | #(c.nommage).a < 2
}

/******* commandes **********/

check aucune_adresse_mapee_par_2_surnoms for 3

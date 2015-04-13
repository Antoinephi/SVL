// SVL 1415
// demo CTD10
// carnet d'adresse

module carnet_simple

sig Identifiant{}
sig Surnom {}
sig Adresse {}
sig Carnet {
   id : Identifiant,
   nommage : Surnom -> lone Adresse // 0 ou 1
}

/******** operations *******/

pred ajout(c : Carnet, c' : Carnet, s : Surnom, a : Adresse) {
   c'.id = c.id
   c'.nommage = c.nommage + s -> a // union +
}

pred suppression_surnom(c : Carnet, c' : Carnet, s : Surnom) {
   c'.id = c.id
   c'.nommage = c.nommage - s -> Adresse // difference -
   // c'.nommage = c.nommage - { s0 : Surnom, a : Adresse | s0 = s } // idem
}

/******** predicats *******/

pred genererInstances(c : Carnet){
   // #Surnom = 2
   // some a : Adresse |  #(c.nommage).a = 3 // pointée par 3 surnoms
   // some s : Surnom | #s.(c.nommage) > 1 // inconsistant
}

pred genererAjout(c1 : Carnet, c2 : Carnet, s : Surnom, a : Adresse) {
    ajout[c1, c2, s, a] and c1 != c2
}

pred test_suppression(c1 : Carnet, c2 : Carnet, s : Surnom) {
	suppression_surnom[c1, c2, s]
}

/******** assertions ********/

// fausse car pas de précond
assert pas_de_surnom_pointant_differentes_adresses {
   all c : Carnet | no s : Surnom | #s.(c.nommage) > 1
}

assert ajout_modifie_carnet {
   all c1, c2 : Carnet, s : Surnom, a : Adresse |  ajout[c1, c2, s, a] implies 
         c1.nommage != c2.nommage
}

assert suppression_surnom_plus_dans_carnet {
   all c1, c2, c3 : Carnet, s : Surnom |  suppression_surnom[c2, c3, s] implies
	c1.nommage = c3.nommage 
}


/******* commandes **********/

run genererInstances for 3 but 1 Carnet
run genererAjout for 2
run test_suppression
check pas_de_surnom_pointant_differentes_adresses for 3
check ajout_modifie_carnet for 2
check suppression_surnom_plus_dans_carnet for 3

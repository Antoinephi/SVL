// SVL 1415
// demo CTD10
// carnet d'adresse - corrigé TP9

module carnet_precond

sig Identifiant{}
sig Surnom {}
sig Adresse {}
sig Carnet {
   id : Identifiant,
   nommage : Surnom -> lone Adresse // 0 ou 1
}

/******** operations *******/

pred ajout(c : Carnet, c' : Carnet, s : Surnom, a : Adresse) {
   no surnom2adresses[c,s] // precond
   c'.id = c.id
   c'.nommage = c.nommage + s -> a
}

pred suppression_surnom(c : Carnet, c' : Carnet, s : Surnom) {
   some surnom2adresses[c,s] // precond
   c'.id = c.id
   c'.nommage = c.nommage - s -> Adresse // difference -
}

fun surnom2adresses(c : Carnet, s : Surnom) : lone Adresse {
   s.(c.nommage)
}

pred modifier_adresse(c, c' : Carnet, a1, a2 : Adresse) {
    a1 != a2
    c'.nommage = c.nommage - Surnom -> a1 + (c.nommage).a1 -> a2
    c'.id = c.id
// - (c.nommage).a1 -> a1 
}

pred modifier_adresse_bis(c, c' : Carnet, a1, a2 : Adresse) {
    a1 != a2
    all s: Surnom | s.(c.nommage) = a1 implies  s.(c'.nommage) = a2
    all s: Surnom | s.(c.nommage) != a1 implies  s.(c'.nommage) = s.(c.nommage)
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

pred generer_modif(c, c' : Carnet, a1, a2 : Adresse) { 
   modifier_adresse[c, c', a1, a2] and some (c.nommage).a1
}

/******** assertions ********/

assert pas_de_surnom_pointant_differentes_adresses {
   all c : Carnet | no s : Surnom | #s.(c.nommage) > 1
}

// vrai car precond
assert ajout_modifie_carnet {
   all c1, c2 : Carnet, s : Surnom, a : Adresse |  ajout[c1, c2, s, a] implies 
         c1.nommage != c2.nommage
}

assert apres_suppression_surnom_plus_dans_carnet {
   all c, c' : Carnet, s : Surnom | suppression_surnom[c, c', s] implies no s.(c'.nommage)   
}

assert suppression_annule_ajout {
   all c1, c2, c3 : Carnet, s : Surnom, a : Adresse | ajout[c1, c2, s, a] and suppression_surnom[c2, c3, s]
            implies c1.nommage = c3.nommage   
}

assert suppr_annule_ajout_bis {
  all c1, c2 : Carnet, s : Surnom, a : Adresse | ajout[c1, c2, s, a] implies suppression_surnom[c2, c1, s]
}

assert adresse_modifiee_plus_ds_carnet {
  all  c1, c2 : Carnet, a1, a2 : Adresse | modifier_adresse[c1, c2, a1, a2] implies no (c2.nommage).a1
}

assert modification_locale {
  all  c1, c2 : Carnet, a1, a2, a3 : Adresse | modifier_adresse[c1, c2, a1, a2]  and some (c1.nommage).a3 and a3 != a1 and a3 != a2
           implies (c1.nommage).a3 = (c2.nommage).a3 
}

/******* commandes **********/

run genererInstances for 3 but 1 Carnet
run genererAjout for 2
run generer_modif for 2
check pas_de_surnom_pointant_differentes_adresses for 3
check ajout_modifie_carnet for 2
check apres_suppression_surnom_plus_dans_carnet for 3 but 2 Carnet
check suppression_annule_ajout for 3
check suppr_annule_ajout_bis for 3 but 1 Surnom, 1 Adresse
check adresse_modifiee_plus_ds_carnet for 3
check modification_locale for 3

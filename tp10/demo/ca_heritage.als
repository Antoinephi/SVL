// SVL 1415
// demo CTD10
// carnet d'adresse avec heritage

module carnet_heritage

abstract sig Element {}
sig Surnom extends Element {}
sig Adresse extends Element {}
sig Carnet {
   surnoms : set Surnom,
   nommage : surnoms -> lone Element
}

fact nommage_pas_cyclique {
    all c : Carnet | no s : Surnom | s in s.^(c.nommage) // cloture transitive 
}

fact nommage_termine_sur_une_adresse {
  all c : Carnet, s : Surnom | some s.^(c.nommage) & Adresse
}

pred generer_instances {}


run generer_instances for 4 but 1 Carnet

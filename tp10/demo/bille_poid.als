// demo 3 SVL 1415 - M. Nebut
// l'ex des billes, avec param bille pour les mvts
// la bille la plus lourde du plateau tombe

module billes
open util/ordering[Etat]

abstract sig Bille {
    plus_lourde_que : set Bille
}
one sig Bleue extends Bille {}
one sig Jaune extends Bille {}
one sig Verte extends Bille {}

fact lourdeur {
   Bleue.plus_lourde_que = { Jaune + Verte}
   Jaune.plus_lourde_que = { Verte }
   Verte.plus_lourde_que = none
}

sig Etat {
    haut : set Bille,
    milieu : set Bille,
    bas : set Bille
}

fun la_plus_lourde (billes : set Bille) : Bille {
   billes - billes.plus_lourde_que
}

// invariants sur Etat

fact une_bille_est_sur_un_seul_plateau {
   all etat : Etat | disj[etat.haut, etat.milieu, etat.bas] // disj : predicat predefini Alloy
}

fact une_bille_est_sur_un_plateau {
  all etat : Etat | etat.haut + etat.milieu + etat.bas = Bille
}

fact deux_places_au_milieu {
  all etat : Etat | #etat.milieu <= 2
}  

// opérations

pred deplacement_H_M [avant, apres : Etat, bille : Bille] {
   // precond
   bille in la_plus_lourde[avant.haut]
   // post cond
   apres.haut = avant.haut - bille
   apres.milieu = avant.milieu + bille
   apres.bas = avant.bas
}

pred deplacement_M_B [avant, apres : Etat, bille : Bille] {
   // precond
   bille in la_plus_lourde[avant.milieu]
   // post cond
   apres.haut = avant.haut
   apres.milieu = avant.milieu - bille
   apres.bas = avant.bas + bille
}

// vérifier que possible d'avoir 2 états liés par un déplacement

assert etats_differents {
  all avant, apres : Etat, bille : Bille |  deplacement_M_B[avant, apres, bille] implies 
               (avant.haut != apres.haut or avant.milieu != apres.milieu or avant.bas != apres.bas)
}

// traces

pred begaiement[avant, apres : Etat] {
 avant.haut = apres.haut and avant.milieu = apres.milieu and avant.bas = apres.bas
}

fact etat_initial {
  first.haut = Bille
  first.milieu = none // ens vide
  no first.bas
}

fact etat_final {
  last.bas = Bille
}

fact etats_successifs {
/* // ou alors
   all avant : Etat - last, apres : next[avant] |  some bille : Bille | deplacement_H_M[avant, apres, bille] 
                                      or deplacement_M_B [avant, apres, bille]
*/
   all avant : Etat - last, apres : Etat |  apres = next[avant] implies
                 (some bille : Bille | (deplacement_H_M[avant, apres, bille] 
                                              or deplacement_M_B [avant, apres, bille]
                                              or begaiement[avant, apres] ))

}

pred generer {}

// traces de taille n Etat exactement
run generer for 7 Etat // OK sans le begaiement
//run generer for 10 Etat  // begaiement necessaire
run deplacement_H_M for 2 Etat
run deplacement_M_B for 2 Etat

check etats_differents

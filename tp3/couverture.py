# SVL 1415 - M. Nebut
# ex couverture noeuds / branches avec coverage

def couverture_avec_branche(b) :
    if b :
        print("true - inside") 
    print("following")

def test_branche() :
    couverture_avec_branche(True)
    couverture_avec_branche(False)

def couverture_condition_composee(a,b) :
    if a or b :
        print("true - inside")
    print("following")

def test_condition_composee() :
    couverture_condition_composee(True, False)
    couverture_condition_composee(False, False)

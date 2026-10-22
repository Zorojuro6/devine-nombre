from devine import deviner, pire_cas

def test_trouve_du_premier_coup():
    assert deviner(50) == 1

def test_hors_intervalle():
    assert deviner(150) == None

def test_pire_cas_100():
    assert pire_cas() == 7

def test_pire_cas_1000():
    assert pire_cas(1, 1000) == 10
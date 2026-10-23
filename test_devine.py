from devine import deviner, pire_cas
import pytest

def test_trouve_du_premier_coup():
    assert deviner(50) == 1

def test_hors_intervalle():
    with pytest.raises(ValueError):
        deviner(150)

def test_pire_cas_100():
    assert pire_cas() == 7

def test_pire_cas_1000():
    assert pire_cas(1, 1000) == 10
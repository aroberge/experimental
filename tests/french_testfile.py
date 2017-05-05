''' Just testing a small subset of all the French syntax '''

from __experimental__ import french_syntax

de math importe pi

def test_bool():
    assert Vrai, "Vrai is True"
    assert not Faux, "Faux is False"

def test_for():
    total = 0
    pour i dans intervalle(10):
        total += i
    assert total == 45

if __name__ == "__main__":
    test_bool()
    test_for()
    print("Success.")

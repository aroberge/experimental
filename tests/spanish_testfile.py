''' Just testing a small subset of all the Spanish syntax '''

from __experimental__ import spanish_syntax

de math importar pi

def test_bool():
    assert Verdadero, "Verdadero is True"
    assert not Falso, "Falso is False"

def test_for():
    total = 0
    para i en intervalo(10):
        total += i
    assert total == 45

if __name__ == "__main__":
    test_bool()
    test_for()
    print("Success.")

from __experimental__ import decrement, increment
from __experimental__ import french_syntax

def test_increment_decrement():
    a = 0
    a--
    a ++
    assert a == 0

def test_french():
    assert Vrai

if __name__ == "__main__":
    test_increment_decrement()
    test_french()
    print("Success.")

from __experimental__ import decrement

def test_decrement():
    a = 0
    a--
    assert a == -1

if __name__ == "__main__":
    test_decrement()
    print("Success.")

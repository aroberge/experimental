from __experimental__ import increment

def test_increment():
    a = 0
    a++
    assert a == 1

if __name__ == "__main__":
    test_increment()
    print("Success.")

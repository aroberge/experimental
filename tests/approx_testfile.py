from __experimental__ import approx

def test_approx():
    assert 0.1 + 0.2 ~= 0.3, "0.1 + 0.2 is approximately equal to 0.3"
    assert 0.1 + 0.2 ~= 0.3 # no message


if __name__ == "__main__":
    test_approx()
    print("Success.")

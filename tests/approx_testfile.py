from __experimental__ import approx

def test_assert():
    assert 0.1 + 0.2 ~= 0.3, "test approximately equal"
    assert 0.1 + 0.2 ~= 0.3 # no message, but comment
    assert 0.1 + 0.2 <~= 0.3, 'test less than or approximately equal'
    assert 0.1 + 0.2 >~= 0.3, 'test greater than or approximately equal'

def test_if():
    if 0.1 + 0.2 ~= 0.3:
        pass
    else:
        raise SyntaxError

if __name__ == "__main__":
    test_assert()
    test_if()
    print("Success.")

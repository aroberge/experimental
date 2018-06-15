from __experimental__ import approx

def test_assert():
    abs_tol = rel_tol = 1e-8
    assert 0.1 + 0.2 != 0.3
    assert 0.1 + 0.2 ~= 0.3, "test approximately equal"
    assert 0.1 + 0.2 ~= 0.3 # no message, but comment
    assert 0.1 + 0.2 <~= 0.3, 'test less than or approximately equal'
    assert 0.1 + 0.2 >~= 0.3, 'test greater than or approximately equal'


def test_if():
    abs_tol = rel_tol = 1e-8    
    if 0.1 + 0.2 ~= 0.3:
        pass
    else:
        raise SyntaxError


def test_missing_parameter():
    try:
        assert 0.1 + 0.2 ~= 0.3
        raise SyntaxError
    except NameError:
        pass

    rel_tol = 1e-8 
    try:
        assert 0.1 + 0.2 ~= 0.3
        raise SyntaxError
    except NameError:
        pass          

    abs_tol = 1e-8 
    assert 0.1 + 0.2 ~= 0.3 

if __name__ == "__main__":
    test_assert()
    test_if()
    print("Success.")

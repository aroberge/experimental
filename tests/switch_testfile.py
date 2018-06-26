from __experimental__ import switch_statement

def example(n):
    result = ''
    switch n:
        case 2:
            result += '2 is even and '
        case 3, 5, 7:
            result += f'{n} is prime'
            break
        case 0: pass
        case 1:
            pass
        case 4, 6, 8, 9:
            result = f'{n} is not prime'
            break
        default:
            result = f'{n} is not a single digit integer'
    return result

def test_switch():
    assert example(0) == '0 is not prime'
    assert example(1) == '1 is not prime'
    assert example(2) == '2 is even and 2 is prime'
    assert example(3) == '3 is prime'
    assert example(4) == '4 is not prime'
    assert example(5) == '5 is prime'
    assert example(6) == '6 is not prime'
    assert example(7) == '7 is prime'
    assert example(8) == '8 is not prime'
    assert example(9) == '9 is not prime'
    assert example(10) == '10 is not a single digit integer'


if __name__ == "__main__":
    test_switch()
    print("Success.")

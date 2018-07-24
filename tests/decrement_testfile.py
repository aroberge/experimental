from __experimental__ import decrement

def test_decrement():
    a = 2
    a--
    assert a == 1

def test_decrement_after_colon():
    usual = 10
    for _ in range(3): usual -= 1
    if True: usual -= 1
    assert usual == 6

    unusual = 10
    for _ in range(3): unusual--
    if True: unusual--
    assert unusual == 6

if __name__ == "__main__":
    test_decrement()
    test_decrement_after_colon()
    print("Success.")

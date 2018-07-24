from __experimental__ import increment

def test_increment():
    a = 0
    a++
    assert a == 1

def test_increment_after_colon():
    usual = 0
    for _ in range(3): usual += 1
    if True: usual += 1
    assert usual == 4

    unusual = 0
    for _ in range(3): unusual++
    if True: unusual++
    assert unusual == 4

if __name__ == "__main__":
    test_increment()
    test_increment_after_colon()
    print("Success.")

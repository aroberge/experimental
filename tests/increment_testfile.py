from __experimental__ import increment

def test_increment():
    a = 0
    a++
    assert a == 1

# This test won't even run, as var++ after the colon fails to parse
# correctly and is considered invalid syntax.
def test_increment_after_colon():
    this_works = 0
    for _ in range(3): this_works += 1
    if True: this_works += 1
    assert this_works == 4

    this_fails = 0
    for _ in range(3): this_fails++
    if True: this_fails++
    assert this_fails == 4

if __name__ == "__main__":
    test_increment()
    print("Success.")

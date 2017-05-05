from __experimental__ import repeat_keyword

def test_repeat():
    i = 1
    repeat 4:
        i += 1
    assert i == 5

if __name__ == "__main__":
    test_repeat()
    print("Success.")

from __experimental__ import alt_range

def test_le_lt():
    result = []
    for x in 2 <= x < 7:
        result.append(x)
    assert result == [2, 3, 4, 5, 6]

def test_le_le():
    result = []
    for x in 2 <= x <= 7:
        result.append(x)
    assert result == [2, 3, 4, 5, 6, 7]


def test_lt_le():
    result = []
    for x in 2 < x <= 7:
        result.append(x)
    assert result == [3, 4, 5, 6, 7]


def test_lt_lt():
    result = []
    for x in 2 < x < 7:
        result.append(x)
    assert result == [3, 4, 5, 6]

if __name__ == "__main__":
    test_le_lt()
    print("Success.")

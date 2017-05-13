from __experimental__ import int_seq


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


def test_ge_gt():
    result = []
    for x3 in 7 >= x3 > 2:
        result.append(x3)
    assert result == [7, 6, 5, 4, 3]


def test_ge_ge():
    result = []
    for other_ in 5 >= other_ >= 2:
        result.append(other_)
    assert result == [5, 4, 3, 2]


def test_gt_ge():
    result = []
    for _yx in -5 > _yx >= -8:
        result.append(_yx)
    assert result == [-6, -7, -8]


def test_gt_gt():
    result = []
    for x in 10 >= x >= 5:
        result.append(x)
    assert result == [10, 9, 8, 7, 6, 5]


if __name__ == "__main__":
    test_le_lt()
    test_le_le()
    test_lt_le()
    test_lt_lt()
    test_ge_gt()
    test_ge_ge()
    test_gt_ge()
    test_gt_gt()
    print("Success.")

from __experimental__ import int_seq


def test_le_lt():
    result = []
    for x in 2 <= x < 7:  # optional comment
        result.append(x)
    assert result == [2, 3, 4, 5, 6]

def test_le_lt_paren():
    result = []
    for x in (2 <= x < 7):
        result.append(x)
    assert result == [2, 3, 4, 5, 6]

def test_le_lt_cond():
    result = []
    for x in 2 <= x < 7 if x % 2 == 0:#another comment
        result.append(x)
    assert result == [2, 4, 6]


def test_le_le():
    result = []
    for x in 2 <= x <= 7:
        result.append(x)
    assert result == [2, 3, 4, 5, 6, 7]


def test_le_le_cond():
    def is_even(n):
        return n % 2 == 0
    result = []
    for x_ in 2 <= x_ <= 7 if is_even(x_):
        result.append(x_)
    assert result == [2, 4, 6]


def test_lt_le():
    result = []
    for x in 2 < x <= 7:
        result.append(x)
    assert result == [3, 4, 5, 6, 7]


def test_lt_le_cond():
    result = []
    for x in 2 < x <= 7 if x in [3, 5]:
        result.append(x)
    assert result == [3, 5]


def test_lt_lt():
    result = []
    for x inseq 2 < x < 7:
        result.append(x)
    assert result == [3, 4, 5, 6]


def test_lt_lt_cond():
    result = []
    for x in 2 < x < 7 if False:
        result.append(x)
    assert result == []


def test_ge_gt():
    result = []
    for x3 in 7 >= x3 > 2:
        result.append(x3)
    assert result == [7, 6, 5, 4, 3]


def test_ge_gt_cond():
    result = []
    for x3 inseq 7 >= x3 > 2 if True:
        result.append(x3)
    assert result == [7, 6, 5, 4, 3]


def test_ge_ge():
    result = []
    for other_ in 5 >= other_ >= 2:
        result.append(other_)
    assert result == [5, 4, 3, 2]


def test_ge_ge_cond():
    result = []
    for other_ in 5 >= other_ >= 2 if other_ % 3:
        result.append(other_)
    assert result == [5, 4, 2]


def test_gt_ge():
    result = []
    for _yx in -5 > _yx >= -8:
        result.append(_yx)
    assert result == [-6, -7, -8]


def test_gt_ge_cond():
    result = []
    for _yx in -5 > _yx >= -8 if _yx != -7:
        result.append(_yx)
    assert result == [-6, -8]


def test_gt_gt():
    result = []
    for x in 10 >= x >= 5:
        result.append(x)
    assert result == [10, 9, 8, 7, 6, 5]


def test_gt_gt_cond():
    result = []
    for x in 10 >= x >= 5 if x%2==0 or x==5:
        result.append(x)
    assert result == [10, 8, 6, 5]

def test_gt_gt_cond_paren():
    result = []
    for x in( 10 >= x >= 5 )if x%2==0 or x==5:
        result.append(x)
    assert result == [10, 8, 6, 5]


if __name__ == "__main__":
    test_le_lt()
    test_le_lt_paren()
    test_le_lt_cond()
    test_le_le()
    test_le_le_cond()
    test_lt_le()
    test_lt_le_cond()
    test_lt_lt()
    test_lt_lt_cond()
    test_ge_gt()
    test_ge_gt_cond()
    test_ge_ge()
    test_ge_ge_cond()
    test_gt_ge()
    test_gt_ge_cond()
    test_gt_gt()
    test_gt_gt_cond()
    test_gt_gt_cond_paren()
    print("Success.")

from __experimental__ import where_clause

def next(i):
    return i+1


def twice(i, next):
    where:
        i: int
        next: Function[[int], int]
        return: int
    return next(next(i))

def test_where():
    i = 3
    where:
        i: int
    assert twice(i, next) == 5

if __name__ == "__main__":
    test_where()
    print("Success.")

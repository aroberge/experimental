from __experimental__ import function_keyword

def test_function():
    square = function x: x**2
    assert square(3) == 9

if __name__ == "__main__":
    test_function()
    print("Success.")

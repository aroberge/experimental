from __experimental__ import pep542

def test_pep542():
    class MyClass:
        pass

    def MyClass.square(self, x):
        return x**2

    my_instance = MyClass()

    def my_instance.out():
        return 42

    assert my_instance.out() == 42
    assert my_instance.square(3) == 9

if __name__ == "__main__":
    test_pep542()
    print("Success.")

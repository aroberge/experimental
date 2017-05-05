from __experimental__ import print_keyword

import sys

class MyOutput:
    def __init__(self):
        self.out = []
    def write(self, text):
        self.out.append(text)
    def flush(self):
        self.out = []

def test_print():
    original = sys.stdout
    sys.stdout = output = MyOutput()
    print "Hello World!"
    assert output.out == ["Hello World!", "\n"]
    output.flush()
    print
    assert output.out == ["\n"]
    sys.stdout = original

if __name__ == "__main__":
    test_print()
    print("Success.")

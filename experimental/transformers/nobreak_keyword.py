'''    from __experimental__ import nobreak_keyword

enables to use the fake keyword `nobreak` instead of `else`, as in

    for i in range(3):
        print(i)
    nobreak:
        print("The entire loop was run.")

Note that `nobreak` can be use everywhere `else` could be used,
(including in `if` blocks) even if would not make sense.

The transformation is done using the tokenize module; it should
only affect code and not content of strings.
'''

from utils.one2one import translate

def transform_source(source):
    return translate(source, {'nobreak': 'else'})


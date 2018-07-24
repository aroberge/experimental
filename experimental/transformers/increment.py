'''
    from __experimental__ import increment

enables transformation of code of the form

    name ++  # optional comment
    other++

into

    name += 1  # optional comment
    other+= 1

Space(s) betwen `name` and `++` are ignored.
'''

from io import StringIO
import tokenize


def transform_source(src):
    toks = tokenize.generate_tokens(StringIO(src).readline)
    result = []
    last_name = None
    last_plus = False
    for toktype, tokvalue, _, _, _ in toks:
        if toktype == tokenize.NAME:
            if last_name is not None:  # two names in a row: not an increment
                result.append((tokenize.NAME, last_name))
                result.append((tokenize.NAME, tokvalue))
                last_name = None
            else:
                last_name = tokvalue
        elif last_name is not None:
            if toktype == tokenize.OP and tokvalue == '+':
                if last_plus:
                    result.extend([
                        (tokenize.NAME, last_name),
                        (tokenize.OP, '='),
                        (tokenize.NAME, last_name),
                        (tokenize.OP, '+'),
                        (tokenize.NUMBER, '1')
                    ])
                    last_plus = False
                    last_name = None
                else:
                    last_plus = True
            else:
                result.append((tokenize.NAME, last_name))
                if last_plus:
                    result.append((tokenize.OP, '+'))
                    last_plus = False
                result.append((toktype, tokvalue))
                last_name = None
        else:
            result.append((toktype, tokvalue))

    if last_name:
        result.append((tokenize.NAME, last_name))
    return tokenize.untokenize(result)

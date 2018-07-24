'''
    from __experimental__ import decrement

enables transformation of code of the form

    name --  # optional comment
    other--

into

    name -= 1  # optional comment
    other-= 1

Space(s) betwen `name` and `--` are ignored.
'''

from io import StringIO
import tokenize


def transform_source(src):
    toks = tokenize.generate_tokens(StringIO(src).readline)
    result = []
    last_name = None
    last_minus = False
    for toktype, tokvalue, _, _, _ in toks:
        if toktype == tokenize.NAME:
            if last_name is not None:  # two names in a row: not an increment
                result.append((tokenize.NAME, last_name))
                result.append((tokenize.NAME, tokvalue))
                last_name = None
            else:
                last_name = tokvalue
        elif last_name is not None:
            if toktype == tokenize.OP and tokvalue == '-':
                if last_minus:
                    result.extend([
                        (tokenize.NAME, last_name),
                        (tokenize.OP, '='),
                        (tokenize.NAME, last_name),
                        (tokenize.OP, '-'),
                        (tokenize.NUMBER, '1')
                    ])
                    last_minus = False
                    last_name = None
                else:
                    last_minus = True
            else:
                result.append((tokenize.NAME, last_name))
                if last_minus:
                    result.append((tokenize.OP, '-'))
                    last_minus = False
                result.append((toktype, tokvalue))
                last_name = None
        else:
            result.append((toktype, tokvalue))

    if last_name:
        result.append((tokenize.NAME, last_name))
    return tokenize.untokenize(result)

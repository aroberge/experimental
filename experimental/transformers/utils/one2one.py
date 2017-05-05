'''This module contains a single function: translate.

Using the tokenize module, this function parses some source code
an apply a translation based on a one-to-one translation table
represented by a Python dict.
'''

from io import StringIO
import tokenize


def translate(source, dictionary):
    '''A dictionary with a one-to-one translation of keywords is used
    to provide the transformation.
    '''
    toks = tokenize.generate_tokens(StringIO(source).readline)
    result = []
    for toktype, tokvalue, _, _, _ in toks:
        if toktype == tokenize.NAME and tokvalue in dictionary:
            result.append((toktype, dictionary[tokvalue]))
        else:
            result.append((toktype, tokvalue))
    return tokenize.untokenize(result)

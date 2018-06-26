'''from __experimental__ import switch_statement

allows the use of a Pythonic switch statement (implemented with if clauses).
A current limitation is that there can only be one level of switch statement
i.e. you cannot have a switch statement inside a case of another switch statement.

Here's an example usage

    def example(n):
        result = ''
        switch n:
            case 2:
                result += '2 is even and '
            case 3, 5, 7:
                result += f'{n} is prime'
                break
            case 0: pass
            case 1:
                pass
            case 4, 6, 8, 9:
                result = f'{n} is not prime'
                break
            default:
                result = f'{n} is not a single digit integer'
        return result

    def test_switch():
        assert example(0) == '0 is not prime'
        assert example(1) == '1 is not prime'
        assert example(2) == '2 is even and 2 is prime'
        assert example(3) == '3 is prime'
        assert example(4) == '4 is not prime'
        assert example(5) == '5 is prime'
        assert example(6) == '6 is not prime'
        assert example(7) == '7 is prime'
        assert example(8) == '8 is not prime'
        assert example(9) == '9 is not prime'
        assert example(10) == '10 is not a single digit integer'
        assert example(42) == '42 is not a single digit integer'
'''

import builtins
import tokenize
from io import StringIO

class Switch:
    ''' Adapted from http://code.activestate.com/recipes/410692/'''
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def __next__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

builtins._Switch = Switch

def transform_source(text):
    '''Replaces instances of

        switch expression:
    by

        for __case in _Switch(n):

    and replaces

        case expression:

    by

        if __case(expression):

    and

        default:

    by

        if __case():
    '''
    toks = tokenize.generate_tokens(StringIO(text).readline)
    result = []
    replacing_keyword = False
    for toktype, tokvalue, _, _, _ in toks:
        if toktype == tokenize.NAME and tokvalue == 'switch':
            result.extend([
                (tokenize.NAME, 'for'),
                (tokenize.NAME, '__case'),
                (tokenize.NAME, 'in'),
                (tokenize.NAME, '_Switch'),
                (tokenize.OP, '(')
            ])
            replacing_keyword = True
        elif toktype == tokenize.NAME and (tokvalue == 'case' or tokvalue == 'default'):
            result.extend([
                (tokenize.NAME, 'if'),
                (tokenize.NAME, '__case'),
                (tokenize.OP, '(')
            ])
            replacing_keyword = True
        elif replacing_keyword and tokvalue == ':':
            result.extend([
                (tokenize.OP, ')'),
                (tokenize.OP, ':')
            ])
            replacing_keyword = False
        else:
            result.append((toktype, tokvalue))
    return tokenize.untokenize(result)


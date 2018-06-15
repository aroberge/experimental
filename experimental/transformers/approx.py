'''
    from __experimental__ import approx

defines some syntax for approximate comparisons within a certain tolerance.
The comparison operators are:

    ~=    # approximately equal
    <~=   # less than or approximately equal
    >~=   # greater than or approximately equal

Given two mathematical terms or expressions a and b, they can occur:

    - on a single line
    - immediately following an assert keyword
    - immediately following an if keyword

However, in the current implementation, anything else will fail.  Thus

    assert 0.1 + 0.2 ~= 0.3

will work; however

    assert not 1 + 2 ~= 3

will raise an AssertionError, because the `not` will not be parsed correctly.

The implementation for the approximation is inspired from Numpy's isclose method
https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.isclose.html
and uses both an absolute tolerance and a relative tolerance parameter
(default value of 1.0e-8).  The values for these parameters can be changed using
`set_tols`.

Here's the result of a quick demo

    > python -m experimental
    experimental console version 0.9.5. [Python version: 3.6.1]

    ~~> from __experimental__ import approx
    ~~> 0.1 + 0.2
    0.30000000000000004
    ~~> 0.1 + 0.2 == 0.3   # standard equality test
    False
    ~~> 0.1 + 0.2 ~= 0.3   # approximate equality test
    True
    ~~> 2 ** 0.5
    1.4142135623730951
    ~~> set_tols(0.001, 0.001)
    ~~> 2 ** 0.5  ~= 1.414
    True
'''

import builtins

def set_tols(atol, rtol):
    builtins.__atol__ = atol 
    builtins.__rtol__ = rtol 
set_tols(1e-8, 1e-8)

def approx_eq(a, b):
    '''Inspired by Numpy's isclose
    https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.isclose.html
    '''
    return abs(a - b) <= (builtins.__atol__ + builtins.__rtol__ * (abs(a) + abs(b)))

def approx_le(a, b):
    return (a < b) or approx_eq(a, b)

def approx_ge(a, b):
    return (a > b) or approx_eq(a, b)


builtins.__approx_eq__ = approx_eq
builtins.__approx_le__ = approx_le
builtins.__approx_ge__ = approx_ge
builtins.set_tols = set_tols 


def transform_source(source):
    newlines = []
    approx_present = False
    for line in source.splitlines():
        line_without_comment = line.split('#')[0]
        for operator in ['<~=', '>~=', '~=', '≅']:
            if operator in line_without_comment:
                line = transform_line(line_without_comment, operator)
                break
        newlines.append(line)
    return '\n'.join(newlines)


def transform_line(line, operator):
    assert line.find('#') == -1
    indent = ' '*(len(line) - len(line.lstrip()))
    line = line.lstrip()
    for keyword in ['assert ', 'if ']:
        if line.startswith(keyword):
            line = line[len(keyword):]
            break
    else:
        keyword = ''
    split = line.split(operator)
    lhs = split[0]
    rest = split[1]
    
    if ',' in rest: 
        separator = ','
    elif ':' in rest:
        separator = ':'
    else:
        separator = ''

    if separator:
        split = rest.split(separator)
        rhs = split[0]
        rest = split[1]
    else:
        rhs = rest 
        rest = ''

    functions = {
        '~=': '__approx_eq__',
        '<~=': '__approx_le__',
        '>~=': '__approx_ge__'
        }

    new_line = (indent + keyword + functions[operator] +
                "(" + lhs + "," + rhs + ")" + 
                separator + rest)
    return new_line

if __name__ == '__main__':
    print(transform_line('assert 0.1 + 0.2 ~= 0.3', '~='))
    print(transform_line('    assert 0.1 + 0.2 ~= 0.3', '~='))
    test_code = '''
def test_approx():
    assert 0.1 + 0.2 ~= 0.3, "0.1 + 0.2 is approximately equal to 0.3"
    assert 0.1 + 0.2 ~= 0.3 # no message, but comments
    '''
    print(transform_source(test_code))


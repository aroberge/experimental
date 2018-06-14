'''
≅
≃
≈
'''

__approx = """
def __approx(a, b):
    '''Inspired by Numpy's isclose
    https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.isclose.html
    '''
    atol = 1e-8
    rtol = 1e-8
    try:
        absolute_tolerance = __atol__
    except NameError:
        absolute_tolerance = atol

    if absolute_tolerance is None: # used to reset
        absolute_tolerance = atol

    try:
        relative_tolerance = __rtol__
    except NameError:
        relative_tolerance = rtol

    if relative_tolerance is None: # used to reset
        relative_tolerance = rtol

    return abs(a - b) <= (atol + rtol * max(abs(b), abs(a)))

"""

def transform_source(source):
    newlines = []
    approx_present = False
    for line in source.splitlines():
        if '~=' in line:
            line = transform_assert(line)
            approx_present = True
        newlines.append(line)
    if approx_present:
        result = __approx
    else:
        result = ''

    return result + '\n'.join(newlines)


def transform_assert(line):
    split = line.split('assert')
    indent = split[0]
    rest = split[1]
    split = rest.split('~=')
    lhs = split[0]
    rest = split[1]
    if '#' in rest:
        rest = rest.split('#')[0]
    if ',' in rest:
        split = rest.split(',')
        rhs = split[0]
        message = split[1]
    else:
        rhs = rest
        message = False

    newline = indent + "assert " + "__approx(" + lhs + "," + rhs + ")"
    if message:
        newline = newline + "," + message
    return newline

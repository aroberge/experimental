'''
    from __experimental__ import approx

defines some syntax for approximate comparisons within a certain tolerance that
must have been previously defined by two variables visible in the current scope:

    rel_tol  # relative tolerance
    abs_tol  # absolute tolerance

These comparisons are done using `math.isclose()`; see this function's
docstring to learn more about the value of the two parameters.

The comparison operators are:

    ~=    # approximately equal
    <~=   # less than or approximately equal
    >~=   # greater than or approximately equal

Given two mathematical terms or expressions a and b, they can occur:

    - on a single line
    - immediately following an assert keyword
    - immediately following an if keyword

However, in the current implementation, anything else will fail.  

    abs_tol = rel_tol = 1e-8
    assert 0.1 + 0.2 ~= 0.3

will work; however

    abs_tol = rel_tol = 1e-8
    assert not 1 + 2 ~= 3

will raise an AssertionError, because the `not` will not be parsed correctly.


Here's the result of a quick demo

    > python -m experimental                                                
    experimental console version 0.9.6. [Python version: 3.6.1]             
                                                                            
    ~~> from __experimental__ import approx                                 
    ~~> 0.1 + 0.2                                                           
    0.30000000000000004                                                     
    ~~> 0.1 + 0.2 == 0.3                                                    
    False                                                                   
    ~~> # Attempt to use approximate comparison without defining tolerances    
    ~~> 0.1 + 0.2 ~= 0.3                                                    
    Traceback (most recent call last):                                      
      File "<console>", line 1, in <module>                                 
    NameError: name 'rel_tol' is not defined                                
    ~~> rel_tol = abs_tol = 1e-8                                            
    ~~> 0.1 + 0.2 ~= 0.3                                                    
    True                                                                    
    ~~> 2**0.5 ~= 1.414                                                     
    False                                                                   
    ~~> abs_tol = 0.001                                                     
    ~~> 2**0.5 ~= 1.414                                                     
    True                                                                    
'''

import builtins

def approx_eq(a, b, rel_tol, abs_tol):
    from math import isclose 

    if abs_tol == rel_tol == 0:
        print("approximate comparisons are implemented using math.isclose")
        print("At least one of rel_tol or abs_tol must be defined either as a local or global variable.")
        raise NotImplementedError

    return isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)

def approx_le(a, b, rel_tol, abs_tol):
    return (a < b) or approx_eq(a, b, rel_tol, abs_tol)

def approx_ge(a, b, rel_tol, abs_tol):
    return (a > b) or approx_eq(a, b, rel_tol, abs_tol)


builtins.__approx_eq__ = approx_eq
builtins.__approx_le__ = approx_le
builtins.__approx_ge__ = approx_ge


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
                "(" + lhs + "," + rhs + ", rel_tol, abs_tol)" + 
                separator + rest)
    return new_line


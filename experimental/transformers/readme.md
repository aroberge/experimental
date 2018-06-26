
Most of the content of this readme has been automatically extracted from
the docstring of each file found in this directory.

Note that multiple transforms can be used in a single file, e.g.

```python
from __experimental__ import increment, decrement
from __experimental__ import function_keyword
```


## approx.py 


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


## convert_py2.py 

    from __experimental__ import convert_py2

triggers the use of the lib2to3 Python library to automatically convert
the code from Python 2 to Python 3 prior to executing it.

As long as lib2to3 can convert the code, this means that code written
using Python 2 syntax can be run using a Python 3 interpreter.


## decrement.py 


    from __experimental__ import decrement

enables transformation of code of the form

    name --  # optional comment
    other--

into

    name -= 1  # optional comment
    other-= 1

Space(s) betwen `name` and `--` are ignored.

This change is done as a simple string replacement, on a line by line basis.
Therefore, it can change not only code but content of triple quoted strings
as well. A more robust solution could always be implemented
using the tokenize module.


## french_syntax.py 

    from __experimental__ import french_syntax

allows the use of a predefined subset of Python keyword to be written
as their French equivalent; **English and French keywords can be mixed**.

Thus, code like:

    si Vrai:
        imprime("French can be used.")
    autrement:
        print(Faux)

Will be translated to

    if True:
        print("French can be used.")
    else:
        print(False)

This type of transformation could be useful when teaching the
very basic concepts of programming to (young) beginners who use
non-ascii based language and would find it difficult to type
ascii characters.

The transformation is done using the tokenize module; it should
only affect code and not content of strings.


## function_keyword.py 

    from __experimental__ import function_keyword

enables to use the word `function` instead of `lambda`, as in

    square = function x: x**2

    square(3)  # returns 9

`lambda` can still be used in the source code.

The transformation is done using the tokenize module; it should
only affect code and not content of strings.


## increment.py 


    from __experimental__ import increment

enables transformation of code of the form

    name ++  # optional comment
    other++

into

    name += 1  # optional comment
    other+= 1

Space(s) betwen `name` and `++` are ignored.

This change is done as a simple string replacement, on a line by line basis.
Therefore, it can change not only code but content of triple quoted strings
as well. A more robust solution could always be implemented
using the tokenize module.


## int_seq.py 

    from __experimental__ import int_seq

makes it possible to use an alternative syntax instead of using `range`
in a for loop.  To be more specific, instead of

    for i in range(3):
        print(i)

we could write

    for i in 0 <= i < 3:
        print(i)

or

    for i in 0 <= i <= 2:   # compare upper boundary with previous case
        print(i)

By reversing the order of the comparison operators, we iterate in reverse.
Thus, for example

    for i in 10 >= i > 0:
        print(i)

would be equivalent to

    for i in range(10, 0, -1):
        print(i)

An additional condition can be added; for example

    for i in 1 <= i < 10  if (i % 2 == 0):
        print(i)

would print the first 4 even integers.

In addition, `inseq` is possible to use as a keyword instead of `in`.
`inseq` is meant to mean `in sequence`. Also, the "range" can be enclosed
in parentheses for greater clarity. Thus, the following is valid:

    for i inseq (1 <= i < 10)  if (i % 2 == 0):
        print(i)

The transformation is done using a regex search and is only valid
on a single line. **There is no guarantee that all legitimately
valid cases will be recognized as such.**


## nobreak_keyword.py 

    from __experimental__ import nobreak_keyword

enables to use the fake keyword `nobreak` instead of `else`, as in

    for i in range(3):
        print(i)
    nobreak:
        print("The entire loop was run.")

Note that `nobreak` can be use everywhere `else` could be used,
(including in `if` blocks) even if would not make sense.

The transformation is done using the tokenize module; it should
only affect code and not content of strings.


## pep542.py 

    from __experimental__ import pep542

Trying to implement https://www.python.org/dev/peps/pep-0542/


## print_keyword.py 

    from __experimental__ import print_keyword

triggers the use of the lib2to3 Python library to automatically convert
all `print` statements (assumed to use the Python 2 syntax) into
function calls.


## repeat_keyword.py 

    from __experimental__ import repeat_keyword

introduces `repeat` as a keyword to write simple loops that repeat
a set number of times.  That is:

    repeat 3:
        a = 2
        repeat a*a:
            pass

is equivalent to

    for __VAR_1 in range(3):
        a = 2
        for __VAR_2 in range(a*a):
            pass

The names of the variables are chosen so as to ensure that they
do not appear in the source code to be translated.

The transformation is done using the tokenize module; it should
only affect code and not content of strings.


## spanish_syntax.py 

    from __experimental__ import spanish_syntax

allows the use of a predefined subset of Python keyword to be written
as their Spanish equivalent; **English and Spanish keywords can be mixed**.

    Neutral latin-american Spanish 
        - translation by Sebastian Silva <sebastian at fuentelibre.org>

Thus, code like:

    si Verdadero:
        imprime("Spanish can be used.")
    sino:
        print(Falso)

Will be translated to

    if True:
        print("Spanish can be used.")
    else:
        print(False)

This type of transformation could be useful when teaching the
very basic concepts of programming to (young) beginners who use
non-ascii based language and would find it difficult to type
ascii characters.

The transformation is done using the tokenize module; it should
only affect code and not content of strings.


## switch_statement.py 

from __experimental__ import switch_statement

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


## where_clause.py 

    from __experimental__ import where_clause

shows how one could use `where` as a keyword to introduce a code
block that would be ignored by Python. The idea was to use this as
a _pythonic_ notation as an alternative for the optional type hinting described
in PEP484.  **This idea has been rejected** as it would not have
been compatible with some older versions of Python, unlike the
approach that has been accepted.
https://www.python.org/dev/peps/pep-0484/#other-forms-of-new-syntax

:warning: This transformation **cannot** be used in the console.

For more details, please see two of my recent blog posts:

https://aroberge.blogspot.ca/2015/12/revisiting-old-friend-yet-again.html

https://aroberge.blogspot.ca/2015/01/type-hinting-in-python-focus-on.html

I first suggested this idea more than 12 years ago! ;-)

https://aroberge.blogspot.ca/2005/01/where-keyword-and-python-as-pseudo.html



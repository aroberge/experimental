
Most of the content of this readme has been automatically extracted from
the docstring of each file found in this directory.

Note that multiple transforms can be used in a single file, e.g.

```python
from __experimental__ import increment, decrement
from __experimental__ import function_keyword
```


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



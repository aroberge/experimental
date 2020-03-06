# Warning

:warning: This project is kept for historical reason but it has rendered obsolete by the creation of [ideas](https://github.com/aroberge/ideas).


### A bit of nostalgia
```python
> python -m experimental
experimental console version 0.9.3 [Python version: 3.5.2]

~~> from __experimental__ import print_keyword
~~> print "Hello world!"
Hello world!
```

# What is `experimental`?

`experimental` is a simple Python module intended to facilitate exploring different syntax construct in Python in an easy way.  Unless you have a very compelling and almost unimaginable reason to do so,
:warning: **it should not be used in production**.

Without `experimental`, if you want to modify Python's syntax, say by adding a new keyword, you need to:

1. Get a copy of Python's repository on your computer
2. modify the grammar file
3. modify the lexer
4. modify the parser
5. modify the compiler
6. recompile all the sources

This is a very involved process.
`experimental` is a Python module that provides a much simpler way to experiment with changes to Python's syntax.

## Installation

To install `experimental`, you can use the standard way:

    pip install experimental

`experimental` currently requires Python 3.4+.

## Usage overview

There are many ways to use `experimental`.

### Alternative Python console
If you simply want to have start a experimental Python console, as shown at the top of this readme file, type

    python -m experimental


### Automatically processing a file - 1

Suppose you have the following file:

```python
> type test.py
from __experimental__ import print_keyword
print "Hello world!"
```

Simply add the name of the test file (without the .py extension) at the end.

```
> python -m experimental test
Hello world!
```

### Automatically processing a file - 2

You can also activate some transformations by inserting them on the
command line between `experimental`
and the name of your python script on the command line.

```python
> type test.py
print "Hello world!"

> python -m experimental print_keyword test
Hello world!
```

### Automatically processing a file and activating a console

Like normal Python, you can execute a script and start an interactive session
afterwards by using the `-i` flag

```python
> type test.py
print "Hello world!"
my_variable = 3
print

> python -i -m experimental print_keyword test
Hello world!

experimental console version 0.9.3 [Python version: 3.5.2]

~~> my_variable
3
```

### Everything but the kitchen sink approach

You can combine declarations within a file with declarations on the command line.

```python
> type test.py
from __experimental__ import increment, decrement
from __experimental__ import nobreak_keyword
from __experimental__ import int_seq

square = function x: x**2

my_variable = 6

for i in 4 < i <= 7 if my_variable==i:
    my_variable++
nobreak:
    my_variable = square(my_variable)

print my_variable
```

```python
> python -i -m experimental print_keyword function_keyword test
49
experimental console version 0.9.3. [Python version: 3.5.2]

~~> my_variable--
~~> print my_variable
48
~~> from __experimental__ import repeat_keyword
~~> repeat 3:
...    print "This is definitely **not** Python."
...
This is definitely **not** Python.
This is definitely **not** Python.
This is definitely **not** Python.
~~>
```

## Additional information

### Dependencies

`experimental` only uses code from the standard library for its execution. However, for testing, I most often use [pytest](https://docs.pytest.org/en/latest/contents.html) to collect and run all the tests, which are simple assertion based comparisons.

### How does it work?

`experimental` uses an import hook to replace the usual import mechanism. Normally, a Python file is first located, then its source is read and finally it is executed _as is_. With `experimental`, an extra step is inserted after the file is read so that its source code can be modified in memory prior to being executed.

### Available transformations

See [the readme file in the transformers directory](https://github.com/aroberge/experimental/blob/master/experimental/transformers/readme.md). Some transformations are **robust**, whereas others ... well, you are very likely to find situations where some transformations are not behaving as you'd expect. These are not bugs, you understand, but rather invitations for you to explore the poorly written code, make some improvements and submit them for consideration.

You are also more than welcome to submit your own experimental code transformations. I'm particularly interested to see new approaches used to transform source code. If you do so, you should include at least some minimal examples as test cases.

### Limitation of the console

Code transformations done in the console are performed on a "line by line" basis.
As a result, transformations that work with an entire code block are likely to fail
in the console.  An example is the `where_clause`
If you create similar transformations, you might want to define a global
variable `NO_CONSOLE` in your module, as was done in
[where_clause](https://github.com/aroberge/experimental/blob/master/experimental/transformers/where_clause.py).


### Automated tests

See [the readme file in the tests directory](https://github.com/aroberge/experimental/blob/master/tests/readme.md) for details.


## To do

- Add version based on `imp` for older Python versions.


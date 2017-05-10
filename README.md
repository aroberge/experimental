
### A bit of nostalgia
```python
> python -m experimental
experimental console. [Python version: 3.5.2]

~~> from __experimental__ import print_keyword
~~> print "Hello world!"
Hello world!
```

# What is `experimental`?

`experimental` is a simple Python module intended to facilitate exploring different syntax construct in Python in an easy way.  Unless you have a very compelling reason to do so, it should not be used in production.

Without `experimental`, if you want to modify Python's syntax, say by adding a new keyword, you need to:

1. Get a copy of Python's repository on your computer
2. modify the grammar file
3. modify the lexer
4. modify the parser
5. modify the compiler
6. recompile all the sources

This is a very involved process.  There has to be a better way if one just want to try some quick experiment.

`experimental` is a Python module that provides a much simpler way to experiment with changes to Python's syntax.

## Installation

To install `experimental`, you can use the standard way:

    pip install experimental

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

experimental console. [Python version: 3.5.2]

~~> my_variable
3
```

## Additional information

### Available transformations

See [the readme file in the transformers directory](https://github.com/aroberge/experimental/blob/master/experimental/transformers/readme.md).

### Automated tests

See [the readme file in the tests directory](https://github.com/aroberge/experimental/blob/master/tests/readme.md).


<span style="color:red; font-weight:bold">More to come...</span>


## To do

- [ ] Complete readme

- [ ] Add code/warning to remove code-block based transformations for console

- [ ] Add code transformation illustrating rejected PEP 315  (do while)

- [ ] Add code transformation illustrating rejected PEP 284 (for lower <= var < upper:)

- [x] Add code transformation illustrating new PEP 542 (dot assignment in functions)

- [ ] Add version based on imp for older Python versions.

- [x] Need to create automated tests for the console

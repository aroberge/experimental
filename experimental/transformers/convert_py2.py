'''    from __experimental__ import convert_py2

triggers the use of the lib2to3 Python library to automatically convert
the code from Python 2 to Python 3 prior to executing it.

As long as lib2to3 can convert the code, this means that code written
using Python 2 syntax can be run using a Python 3 interpreter.
'''


from utils.simple2to3 import MyRefactoringTool, get_lib2to3_fixers

try:
    my_fixes = MyRefactoringTool(get_lib2to3_fixers())
except:
    print("Cannot create MyRefactoringTool in convert_py2.")
    my_fixes = None


def transform_source(source):
    if my_fixes is None:
        return source
    return my_fixes.refactor_source(source)

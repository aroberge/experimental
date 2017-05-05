'''    from __experimental__ import print_keyword

triggers the use of the lib2to3 Python library to automatically convert
all `print` statements (assumed to use the Python 2 syntax) into
function calls.
'''

from utils.simple2to3 import MyRefactoringTool, get_single_fixer

try:
    my_fixes = MyRefactoringTool( [get_single_fixer("print")] )
except:
    print("Cannot create MyRefactoringTool in print_keyword.")
    my_fixes = None

def transform_source(source):
    if my_fixes is None:
        return source
    return my_fixes.refactor_source(source)


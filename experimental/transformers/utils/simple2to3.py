import os
from lib2to3.refactor import RefactoringTool
import lib2to3.fixes as fixer_dir

# This simple module appears to be incompatible with the import
# hook. For this reason, it is important to wrap calls to it
# with a try/except clause.  I have found that a bare except,
# that catches all errors, is definitely the best way to proceed.

def get_lib2to3_fixers():
    '''returns a list of all fixers found in the lib2to3 library'''
    fixers = []
    fixer_dirname = fixer_dir.__path__[0]
    for name in sorted(os.listdir(fixer_dirname)):
        if name.startswith("fix_") and name.endswith(".py"):
            fixers.append("lib2to3.fixes." + name[:-3])
    return fixers


def get_single_fixer(fixname):
    '''return a single fixer found in the lib2to3 library'''
    fixer_dirname = fixer_dir.__path__[0]
    for name in sorted(os.listdir(fixer_dirname)):
        if (name.startswith("fix_") and name.endswith(".py") 
            and fixname == name[4:-3]):
            return "lib2to3.fixes." + name[:-3]


class MyRefactoringTool(RefactoringTool):
    '''This class must be instantiated with a list of all desired fixers'''
    _used_fixes = []

    def __init__(self, fixer_names):
        # avoid duplicating fixers if called multiple times
        fixers = [fix for fix in fixer_names if fix not in self._used_fixes]
        super().__init__(fixers, options=None, explicit=None)
        self._used_fixes.extend(fixers)

    def refactor_source(self, source):
        source += "\n" # Silence certain parse errors
        tree = self.refactor_string(source, "original")
        return str(tree)[:-1]


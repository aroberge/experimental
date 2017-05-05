#pylint: disable=W0603, W0122
'''A custom Importer making use of the import hook capability

Note that the protocole followed is no longer as described in PEP 302 [1]

This code was adapted from
http://stackoverflow.com/q/43571737/558799
which is a question I asked when I wanted to adopt an approach using
a deprecated module (imp) and which followed PEP 302.

[1] https://www.python.org/dev/peps/pep-0302/
'''

import os.path
import sys

from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location

from . import transforms

# add the path where the default transformers should be found
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "transformers")))

MAIN_MODULE_NAME = None
def import_main(name):
    '''Imports the module that is to be interpreted as the main module.

       experimental is often invoked with a script meant to be run as the
       main module its source is transformed.  The invocation will be

       python -m experimental [trans1, trans2, ...] main_script

       Python identifies experimental as the main script; we artificially
       change this so that "main_script" is properly identified as such.
    '''
    global MAIN_MODULE_NAME
    MAIN_MODULE_NAME = name
    return __import__(name)


class MyMetaFinder(MetaPathFinder):
    '''A custom finder to locate modules.  The main reason for this code
       is to ensure that our custom loader, which does the code transformations,
       is used.'''
    def find_spec(self, fullname, path, target=None):
        '''finds the appropriate properties (spec) of a module, and sets
           its loader.'''
        if not path:
            path = [os.getcwd()]
        if "." in fullname:
            name = fullname.split(".")[-1]
        else:
            name = fullname
        for entry in path:
            if os.path.isdir(os.path.join(entry, name)):
                # this module has child modules
                filename = os.path.join(entry, name, "__init__.py")
                submodule_locations = [os.path.join(entry, name)]
            else:
                filename = os.path.join(entry, name + ".py")
                submodule_locations = None
            if not os.path.exists(filename):
                continue

            return spec_from_file_location(fullname, filename,
                                           loader=MyLoader(filename),
                                           submodule_search_locations=submodule_locations)
        return None # we don't know how to import this

sys.meta_path.insert(0, MyMetaFinder())


class MyLoader(Loader):
    '''A custom loader which will transform the source prior to its execution'''
    def __init__(self, filename):
        self.filename = filename

    def create_module(self, spec):
        return None # use default module creation semantics

    def exec_module(self, module):
        '''import the source code, transforma it before executing it so that
           it is known to Python.'''
        global MAIN_MODULE_NAME
        if module.__name__ == MAIN_MODULE_NAME:
            module.__name__ = "__main__"
            MAIN_MODULE_NAME = None

        with open(self.filename) as f:
            source = f.read()

        if transforms.transformers:
            source = transforms.transform(source)
        else:
            for line in source.split('\n'):
                if transforms.FROM_EXPERIMENTAL.match(line):
                    ## transforms.transform will extract all such relevant
                    ## lines and add them all relevant transformers
                    source = transforms.transform(source)
                    break
        exec(source, vars(module))

    def get_code(self, _):
        '''Hack to silence an error when running experimental as main script
           See below for an explanation'''
        return compile("None", "<string>", 'eval')

"""
When this code was run as part of a normal script, no error was raised.
When I changed it into a package, and tried to run it as a module, an
error occurred as shown below. By looking at the sources for the
importlib module, I saw that some classes had a get_code() method which
returned a code object.  Rather than trying to recreate all the code,
I wrote the above hack which seems to silence any error.

$ python -m experimental
Python version: 3.5.2 |Anaconda 4.2.0 (64-bit)| ...

    Python console with easily modifiable syntax.

~~> exit()
Leaving non-standard console.

Traceback (most recent call last):
  ...
  AttributeError: 'MyLoader' object has no attribute 'get_code'
"""

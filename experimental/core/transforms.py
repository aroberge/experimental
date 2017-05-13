#pylint: disable=W1401, C0103, W0703
'''This module takes care of identifying, importing and adding source
code transformers. It also contains a function, `transform`, which
takes care of invoking all known transformers to convert a source code.
'''
import re
import sys

FROM_EXPERIMENTAL = re.compile("(^from\s+__experimental__\s+import\s+)")

class NullTransformer:
    '''NullTransformer is a convenience class which can generate instances
    to be used when a given transformer cannot be imported.'''
    def transform_source(self, source): #pylint: disable=I0011, R0201, C0111
        return source

transformers = {}
def add_transformers(line):
    '''Extract the transformers names from a line of code of the form
       from __experimental__ import transformer1 [,...]
       and adds them to the globally known dict
    '''
    assert FROM_EXPERIMENTAL.match(line)

    line = FROM_EXPERIMENTAL.sub(' ', line)
    # we now have: " transformer1 [,...]"
    line = line.split("#")[0]    # remove any end of line comments
    # and insert each transformer as an item in a list
    for trans in line.replace(' ', '').split(','):
        import_transformer(trans)


def import_transformer(name):
    '''If needed, import a transformer, and adds it to the globally known dict
       The code inside a module where a transformer is defined should be
       standard Python code, which does not need any transformation.
       So, we disable the import hook, and let the normal module import
       do its job - which is faster and likely more reliable than our
       custom method.
    '''
    if name in transformers:
        return transformers[name]

    # We are adding a transformer built from normal/standard Python code.
    # As we are not performing transformations, we temporarily disable
    # our import hook, both to avoid potential problems AND because we
    # found that this resulted in much faster code.
    hook = sys.meta_path[0]
    sys.meta_path = sys.meta_path[1:]
    try:
        transformers[name] = __import__(name)
    except ImportError:
        sys.stderr.write("Warning: Import Error in add_transformers: %s not found\n" % name)
        transformers[name] = NullTransformer()
    except Exception as e:
        sys.stderr.write("Unexpected exception in transforms.import_transformer%s\n " %
                         e.__class__.__name__)
    finally:
        sys.meta_path.insert(0, hook) # restore import hook

    return transformers[name]

def extract_transformers_from_source(source):
    '''Scan a source for lines of the form
       from __experimental__ import transformer1 [,...]
       identifying transformers to be used. Such line is passed to the
       add_transformer function, after which it is removed from the
       code to be executed.
    '''
    lines = source.split('\n')
    linenumbers = []
    for number, line in enumerate(lines):
        if FROM_EXPERIMENTAL.match(line):
            add_transformers(line)
            linenumbers.insert(0, number)

    # drop the "fake" import from the source code
    for number in linenumbers:
        del lines[number]
    return '\n'.join(lines)


def transform(source):
    '''Used to convert the source code, making use of known transformers.

       "transformers" are modules which must contain a function

           transform_source(source)

       which returns a tranformed source.
       Some transformers (for example, those found in the standard library
       module lib2to3) cannot cope with non-standard syntax; as a result, they
       may fail during a first attempt. We keep track of all failing
       transformers and keep retrying them until either they all succeeded
       or a fixed set of them fails twice in a row.
    '''
    source = extract_transformers_from_source(source)

    not_done = transformers
    while True:
        failed = {}
        for name in not_done:
            tr_module = import_transformer(name)
            try:
                source = tr_module.transform_source(source)
            except Exception as e:
                failed[name] = tr_module
                # from traceback import print_exc
                # print("Unexpected exception in transforms.transform",
                #       e.__class__.__name__)
                # print_exc()

        if not failed:
            break
        if failed == not_done:
            print("Warning: the following transforms could not be done:")
            for key in failed:
                print(key)
            break
        not_done = failed  # attempt another pass

    return source

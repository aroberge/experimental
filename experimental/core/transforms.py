#pylint: disable=W1401, C0103, W0703
'''This module takes care of identifying, importing and adding source
code transformers. It also contains a function, `transform`, which
takes care of invoking all known transformers to convert a source code.
'''
import re
import sys

FROM_EXPERIMENTAL = re.compile("(^from\s+__experimental__\s+import\s+)")
CONSOLE_ACTIVE = False  # changed by console.start_console()

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
        # Some transformers are not allowed in the console.
        # If an attempt is made to activate one of them in the console,
        # we replace it by a transformer that does nothing and print a
        # message specific to that transformer as written in its module.
        if CONSOLE_ACTIVE:
            if hasattr(transformers[name], "NO_CONSOLE"):
                print(transformers[name].NO_CONSOLE)
                transformers[name] = NullTransformer()
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

def remove_not_allowed_in_console():
    '''This function should be called from the console, when it starts.

    Some transformers are not allowed in the console and they could have
    been loaded prior to the console being activated. We effectively remove them
    and print an information message specific to that transformer
    as written in the transformer module.

    '''
    not_allowed_in_console = []
    if CONSOLE_ACTIVE:
        for name in transformers:
            tr_module = import_transformer(name)
            if hasattr(tr_module, "NO_CONSOLE"):
                not_allowed_in_console.append((name, tr_module))
        for name, tr_module in not_allowed_in_console:
            print(tr_module.NO_CONSOLE)
            # Note: we do not remove them, so as to avoid seeing the
            # information message displayed again if an attempt is
            # made to re-import them from a console instruction.
            transformers[name] = NullTransformer()


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

    # Some transformer fail when multiple non-Python constructs
    # are present. So, we loop multiple times keeping track of
    # which transformations have been unsuccessfully performed.
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
        # Insanity is doing the same Tting over and overaAgain and
        # expecting different results ...
        # If the exact same set of transformations are not performed
        # twice in a row, there is no point in trying out a third time.
        if failed == not_done:
            print("Warning: the following transforms could not be done:")
            for key in failed:
                print(key)
            break
        not_done = failed  # attempt another pass

    return source

#pylint: disable=W0102, C0103
import code
import platform
import sys

from . import transforms

# define banner and prompt here so that they can be imported in tests
banner = "experimental console. [Python version: %s]\n" % platform.python_version()
prompt = "~~> "


class ExperimentalInteractiveConsole(code.InteractiveConsole):
    '''A Python console that emulates the normal Python interpreter
       except that it support experimental code transformations.'''

    def push(self, line):
        """Transform and push a line to the interpreter.

        The line should not have a trailing newline; it may have
        internal newlines.  The line is appended to a buffer and the
        interpreter's runsource() method is called with the
        concatenated contents of the buffer as source.  If this
        indicates that the command was executed or invalid, the buffer
        is reset; otherwise, the command is incomplete, and the buffer
        is left as it was after the line was appended.  The return
        value is 1 if more input is required, 0 if the line was dealt
        with in some way (this is the same as runsource()).

        """
        if transforms.FROM_EXPERIMENTAL.match(line):
            transforms.add_transformers(line)
            self.buffer.append("\n")
        else:
            self.buffer.append(line)

        add_pass = False
        if line.rstrip(' ').endswith(":"):
            add_pass = True
        source = "\n".join(self.buffer)
        if add_pass:
            source += "pass"
        source = transforms.transform(source)
        if add_pass:
            source = source.rstrip(' ')[:-4]

        # some transformations may strip an empty line meant to end a block
        if not self.buffer[-1]:
            source += "\n"
        more = self.runsource(source, self.filename)

        if not more:
            self.resetbuffer()
        return more


def start_console(local_vars={}):
    '''Starts a console; modified from code.interact'''
    sys.ps1 = prompt
    console = ExperimentalInteractiveConsole(locals=local_vars)
    console.interact(banner=banner)

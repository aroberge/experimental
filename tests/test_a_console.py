# pylint: disable=C0103
import subprocess
from .common import experimental

banner = experimental.core.console.banner
prompt = experimental.core.console.prompt

### sessions items:
### (command, input, expected_output, expected_error)

sessions = [
    ("python -m experimental", """
from __experimental__ import increment, decrement, print_keyword
a = 3
print a
a++
print a
a--
print a
exit()
""", """
3
4
3
"""),
    ("python -i -m experimental tests.decrement_testfile",
     'a = 7 \na--\nprint(a)',
     'Success.\n6'),
    ("python -i -m experimental tests.french_testfile",
     'Vrai',
     'Success.\nTrue'),
    ("python -i -m experimental tests.function_testfile",
     'sq = function x: x**2\nsq(3)',
     'Success.\n9'),
    ("python -i -m experimental tests.increment_testfile",
     'a = 7 \na++ \nprint(a)',
     'Success.\n8'),
    ("python -i -m experimental tests.print_testfile",
     'print 1', 'Success.\n1'),
    ("python -i -m experimental tests.repeat_testfile",
     'repeat 2:\n  print("*", end="")\n\n', 'Success.\n... ... **'),
]

def compare_output(real, expected):
    '''The output from the console includes the prompt.
       To make tests less brittle and easier to write, we strip the prompt
       and remove leading and trailing spaces.
    '''
    return real.replace(prompt, '').strip() == expected.strip()

def test_console():
    '''Function discoverable and run by pytest'''
    for command, inp, out in sessions:
        process = subprocess.Popen(
            command,
            shell=False,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True  # use strings as input
        )
        stdout, stderr = process.communicate(inp)
        process.wait()
        assert compare_output(stdout, out)


if __name__ == "__main__":
    test_console()

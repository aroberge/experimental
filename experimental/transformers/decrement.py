'''
    from __experimental__ import decrement

enables transformation of code of the form

    name --  # optional comment

into

    name -= 1  # optional comment

Space(s) betwen `name` and `--` are ignored.

This can change not only code but content of triple quoted strings
as well. A more robust solution could always be implemented
using the tokenize module.
'''

def transform_source(src):
    newlines = []
    for line in src.splitlines():
        if ('--') in line:
            newlines.append(transform_line(line))
        else:
            newlines.append(line)
    result = '\n'.join(newlines)
    return result

def transform_line(line):
    original = line
    try:
        first, second = line.split("#")[0].split('--')
    except ValueError:
        return original
    # if line is of the form
    # ...identifier...--...
    # where "..." represent optional spaces
    if first.strip().isidentifier() and second.strip() == '':
        return original.replace("--", "-= 1")
    else:
        return original

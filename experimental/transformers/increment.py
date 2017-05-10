'''
    from __experimental__ import increment

enables transformation of code of the form

    name ++  # optional comment
    other++

into

    name += 1  # optional comment
    other+= 1

Space(s) betwen `name` and `++` are ignored.

This change is done as a simple string replacement, on a line by line basis.
Therefore, it can change not only code but content of triple quoted strings
as well. A more robust solution could always be implemented
using the tokenize module.
'''

def transform_source(src):
    newlines = []
    for line in src.splitlines():
        if ('++') in line:
            newlines.append(transform_line(line))
        else:
            newlines.append(line)
    result = '\n'.join(newlines)
    return result

def transform_line(line):
    original = line
    try:
        first, second = line.split("#")[0].split('++')
    except ValueError:
        return original
    # if line is of the form
    # ...identifier...++...
    # where "..." represent optional spaces
    if first.strip().isidentifier() and second.strip() == '':
        return original.replace("++", "+= 1")
    else:
        return original

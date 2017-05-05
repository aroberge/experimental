'''    from __experimental__ import pep542

Trying to implement https://www.python.org/dev/peps/pep-0542/
'''

from io import StringIO
import tokenize

def transform_source(text):
    toks = tokenize.generate_tokens(StringIO(text).readline)
    result = []
    special_def_clause = False
    potential_prefix = None
    prefix = None
    begin_col = 0

    for toktype, tokvalue, begin, _, _ in toks:
        if not special_def_clause and toktype == tokenize.NAME and tokvalue == "def":
            special_def_clause = True   # potentially
            begin_col = begin[1]
        elif special_def_clause and potential_prefix is None and prefix is None:
            potential_prefix = (toktype, tokvalue)
            continue
        elif special_def_clause and potential_prefix and prefix is None:
            if toktype == tokenize.OP and tokvalue == ".":
                prefix = potential_prefix
                continue
            else:  # normal def
                result.append(potential_prefix)
                special_def_clause = False
                potential_prefix = None
        elif special_def_clause and potential_prefix and prefix:
            fn_name = tokvalue
            potential_prefix = None
        elif special_def_clause and not potential_prefix and prefix and ((
                toktype == tokenize.NAME and begin[1] == begin_col) or (
                toktype == tokenize.ENDMARKER)):
            # insert special naming
            result.append(prefix)
            result.append((tokenize.OP, "."))
            result.append((tokenize.NAME, fn_name))
            result.append((tokenize.EQUAL, "="))
            result.append((tokenize.NAME, fn_name))
            result.append((tokenize.NEWLINE, "\n"))
            # remove from local variables
            result.append((tokenize.NAME, "del"))
            result.append((tokenize.NAME, fn_name))
            result.append((tokenize.NEWLINE, "\n"))
            result.append((tokenize.NEWLINE, "\n"))

            result.append((toktype, tokvalue))

            special_def_clause = False
            potential_prefix = None
            prefix = None
            begin_col = 0
            continue
        result.append((toktype, tokvalue))

    return tokenize.untokenize(result)

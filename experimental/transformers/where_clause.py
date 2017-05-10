'''    from __experimental__ import where_clause

shows how one could use `where` as a keyword to introduce a code
block that would be ignored by Python. The idea was to use this as
a _pythonic_ notation as an alternative for the optional type hinting described
in PEP484.  **This idea has been rejected.**

<span style="color:red; font-weight:bold">Warning:</span>
This transformation **cannot** be used in the console.

For more details, please see two of my recent blog posts:

https://aroberge.blogspot.ca/2015/12/revisiting-old-friend-yet-again.html

https://aroberge.blogspot.ca/2015/01/type-hinting-in-python-focus-on.html

I first suggested this idea more than 12 years ago! ;-)

https://aroberge.blogspot.ca/2005/01/where-keyword-and-python-as-pseudo.html
'''

from io import StringIO
import tokenize

def transform_source(text):
    '''removes a "where" clause which is identified by the use of "where"
    as an identifier and ends at the first DEDENT (i.e. decrease in indentation)'''
    toks = tokenize.generate_tokens(StringIO(text).readline)
    result = []
    where_clause = False
    for toktype, tokvalue, _, _, _ in toks:
        if toktype == tokenize.NAME and tokvalue == "where":
            where_clause = True
        elif where_clause and toktype == tokenize.DEDENT:
            where_clause = False
            continue

        if not where_clause:
            result.append((toktype, tokvalue))
    return tokenize.untokenize(result)


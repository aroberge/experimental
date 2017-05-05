'''This creates a readme.md file in the directory experimental/transformers
by extracting the docstring of each transform found in that directory.
'''

import os
import sys

target_dir = os.path.abspath(os.path.join(
                    os.path.dirname(__file__), '..', "experimental/transformers"))

os.chdir(target_dir)
sys.path.insert(0, target_dir)

docstrings = ['''
The content of this readme has been automatically extracted from
the docstring of each file found in this directory.

Note that multiple transforms can be used in a single file, e.g.

    from __experimental__ import increment, decrement
    from __experimental__ import function_keyword
''']

for f in os.listdir('.'):
    if f.startswith("_") or os.path.isdir(f) or not f.endswith(".py"):
        continue

    name = f[:-3]
    script = __import__(name)
    docstrings.append("## %s " % f)
    if script.__doc__ is None:
        script.__doc__ = "Docstring missing."
    docstrings.append(script.__doc__)

with open("readme.md", "w") as readme:
    readme.write("\n\n".join(docstrings))


'''    from __experimental__ import french_syntax

allows the use of a predefined subset of Python keyword to be written
as their French equivalent; **English and French keywords can be mixed**.

Thus, code like:

    si Vrai:
        imprime("French can be used.")
    autrement:
        print(Faux)

Will be translated to

    if True:
        print("French can be used.")
    else:
        print(False)

This type of transformation could be useful when teaching the
very basic concepts of programming to (young) beginners who use
non-ascii based language and would find it difficult to type
ascii characters.

The transformation is done using the tokenize module; it should
only affect code and not content of strings.
'''

from utils.one2one import translate

def transform_source(source):
    '''Input text is assumed to contain some French equivalent words to
       normal Python keywords and a few builtin functions.
       These are transformed into normal Python keywords and functions.
    '''
    # continue, def, global, lambda, nonlocal remain unchanged by choice

    dictionary = {'Faux': 'False', 'Aucun': 'None', 'Vrai': 'True',
                   'et': 'and', 'comme': 'as', 'affirme': 'assert',
                   'sortir': 'break', 'classe': 'class', 'élimine': 'del',
                   'ousi': 'elif', 'autrement': 'else', 'exception': 'except',
                   'finalement': 'finally', 'pour': 'for', 'de': 'from',
                   'si': 'if', 'importe': 'import', 'dans': 'in', 'est': 'is',
                   'non': 'not', 'ou': 'or', 'passe': 'pass',
                   'soulever': 'raise', 'retourne': 'return', 'essayer': 'try',
                   'pendant': 'while', 'avec': 'with', 'céder': 'yield',
                   'imprime': 'print', 'intervalle': 'range'}

    return translate(source, dictionary)

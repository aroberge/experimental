'''    from __experimental__ import spanish_syntax

allows the use of a predefined subset of Python keyword to be written
as their Spanish equivalent; **English and Spanish keywords can be mixed**.

    Neutral latin-american Spanish 
        - translation by Sebastian Silva <sebastian at fuentelibre.org>

Thus, code like:

    si Verdadero:
        imprime("Spanish can be used.")
    sino:
        print(Falso)

Will be translated to

    if True:
        print("Spanish can be used.")
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

    dictionary = {'Falso': 'False', 'Nada': 'None', 'Verdadero': 'True',
                   'y': 'and', 'como': 'as', 'afirmar': 'assert',
                   'interrumpir': 'break', 'clase': 'class', 'eliminar': 'del',
                   'osi': 'elif', 'sino': 'else', 'excepto': 'except',
                   'finalmente': 'finally', 'para': 'for', 'de': 'from',
                   'si': 'if', 'importar': 'import', 'en': 'in', 'es': 'is',
                   'no': 'not', 'o': 'or', 'seguir': 'pass',
                   'elevar': 'raise', 'retornar': 'return', 'intentar': 'try',
                   'mientras': 'while', 'con': 'with', 'ceder': 'yield',
                   'imprimir': 'print', 'intervalo': 'range'}

    return translate(source, dictionary)

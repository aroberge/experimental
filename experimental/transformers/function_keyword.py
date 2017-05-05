'''    from __experimental__ import function_keyword

enables to use the word `function` instead of `lambda`, as in

    square = function x: x**2

    square(3)  # returns 9
'''

from utils.one2one import translate

def transform_source(source):
    '''Replaces instances of
        function
    by
        lambda
    '''
    return translate(source, {'function': 'lambda'})


if __name__ == '__main__':
    sample = '''square = function x: x**2'''

    comparison = '''square =lambda x :x **2 '''

    if comparison == transform_source(sample):
        print("Transformation done correctly")
    else:
        print("Transformation done incorrectly")
        import difflib
        d = difflib.Differ()
        diff = d.compare(comparison.splitlines(),
                         transform_source(sample).splitlines())
        print('\n'.join(diff))

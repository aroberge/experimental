#pylint: skip-file
from setuptools import setup, find_packages


from pypandoc import convert
def convert_md(filename):
    return convert(filename, 'rst')


setup(name='experimental',
    version='0.9',
    description="Enables easy modification of Python's syntax on the fly.",
    long_description = convert_md('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Interpreters',
    ],
    url='https://github.com/aroberge/experimental',
    author='André Roberge',
    author_email='Andre.Roberge@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['dist', 'build', 'tools']),
    zip_safe=False)

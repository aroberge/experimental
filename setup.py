#pylint: skip-file
from setuptools import setup, find_packages
from distutils.util import convert_path

## converting readme for pypi
from pypandoc import convert
def convert_md(filename):
    return convert(filename, 'rst')

version_path = convert_path('experimental/version.py')
with open(version_path) as version_file:
    exec(version_file.read())


setup(name='experimental',
    version=__version__,
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

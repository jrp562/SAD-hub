"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call
from setuptools import Command, find_packages, setup
from ssa import __version__


setup(
    name = 'ssa',
    version = __version__,
    description = 'A Super Store App form the command line.',
    #long_description = long_description,
    url = 'https://github.com/jrp562/SAD-hub',
    author = '',
    author_email = '',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'ssa=ssa.cli:main',
        ],
    },
    #cmdclass = {'test': RunTests},
)

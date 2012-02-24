import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'webkit2png',
    version = '0.5.0',
    author = 'Paul Hammond, packaged by Daniel Naab',
    description = ('Creates screenshots via webkit.'),
    license = 'BSD',
    url = 'https://github.com/danielnaab/webkit2png',
    packages=['webkit2png'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],
)

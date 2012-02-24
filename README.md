webkit2png
==========

webkit2png is a command line tool that creates png screenshots of webpages.

This fork has refactored out the png generation into a separate function that
may be treated as a library.  In addition, it is pip-installable via setuptools.

    $ pip install -e git+git://github.com/danielnaab/webkit2png.git#egg=webkit2png

For more details, visit http://www.paulhammond.org/webkit2png/

Usage
-----
For command-line usage information, view the help text.

    $ python webkit2png.py --help

Otherwise, urls are specified via positional arguments and options are
keyword arguments.   Here are a two equivalent examples:

    from webkit2png import create_pngs
    create_pngs('http://www.google.com', 'http://www.yahoo.com')

    # These are the default options, used for demonstration:
    options = {
        'scale': 0.25,
        'clipheight': 150.0,
        'width': 800.0,
        'nojs': None,
        'clipped': None,
        'fullsize': None,
        'thumb': None,
        'height': 600.0,
        'delay': 0,
        'datestamp': None,
        'filename': '',
        'dir': './',
        'zoom': 1.0,
        'noimages': None,
        'debug': None,
        'js': None,
        'transparent': False,
        'md5': None,
        'clipwidth': 200.0
    }
    urls = ['http://www.google.com', 'http://www.yahoo.com']
    create_pngs(*urls, **options)

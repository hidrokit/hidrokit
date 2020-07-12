#!/usr/bin/env python
# -*- coding: utf-8 -*-


import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'hidrokit'
DESCRIPTION = 'analisis hidrologi dengan python'
URL = 'https://github.com/hidrokit/hidrokit'
EMAIL = 'timhidrokit@gmail.com'
AUTHOR = 'Hidrokit'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = ''

# What packages are required for this module to be executed?
REQUIRED = [
    'numpy', 'pandas', 'matplotlib',
]

# What packages are optional?
EXTRAS = {
    'excel': ['openpyxl', 'xlrd', 'xlwt'],
}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Where the magic happens:
setup(
    # PACKAGE INFORMATION
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,

    # Packages settings
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*", "docs"]
    ),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',

    # Classifiers
    # Trove classifiers
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Development status
        'Development Status :: 3 - Alpha',

        # Intended Audience
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Hydrology',

        # License
        'License :: OSI Approved :: MIT License',

        # Python Version
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    project_urls={
        'Documentation': 'https://hidrokit.github.io/hidrokit',
        'ReadTheDocs': 'https://hidrokit.readthedocs.io/en/stable/',
        'Bug Reports': 'https://github.com/hidrokit/hidrokit/issues',
        'Source': 'https://github.com/hidrokit/hidrokit/',
    },
)

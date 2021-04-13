# -*- coding: utf-8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os
import codecs
from setuptools import setup, find_packages

# Save version and author to __meta__.py
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'src', 'swagger_yaml_2_html', '__meta__.py')
meta = '''# Automatically created. Please do not edit.
__version__ = '%s'
__author__ = 'rezamt'
''' % version
with open(path, 'w') as F:
    F.write(meta)

setup(
    # Basic info
    name='swagger-yaml-2-html',
    version=version,
    author='rezamt',
    author_email='rezamt@gmail.com',
    url='',
    description='A short description for your project.',
    long_description=codecs.open('README.rst', 'rb', 'utf8').read(),

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and dependencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'Django==1.11.29',
        'pytz==2018.5',
        'PyYAML==5.1.2',

    ],
    extras_require={
        'dev': [
            'python-boilerplate[dev]',
        ],
    },
    entry_points={
        'console_scripts': [
            'swagger-yaml-2-html = swagger_yaml_2_html.__main__:main'
        ]
    },
    # Other configurations
    zip_safe=False,
    platforms='any',
)
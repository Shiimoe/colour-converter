#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open
from os import path
import os, stat, sys

here = path.abspath(path.dirname(__file__))

setup(
    name='colour_converter',
    version='0.1',
    description='Convert between RGB and hex colour values',
    url='https://github.com/Demonstrandum/colour-converter',
    author='clichetouche, Demonstrandum',
    author_email='knutsen@jetspace.co, twigg@jetspace.co',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
    ],
    keywords='covert colours hex RGB',
    packages=find_packages(),
    install_requires=[],
    scripts=['bin/colour-convert']
)

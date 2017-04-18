# -*- coding: utf-8 -*
"""
Setup script for BDDOCS.
USAGE:
    python setup.py install
"""
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='bddocs',
      version='0.34',
      description='Create end-user readable docs in Pythonic way',
      long_description=readme(),
      author='Yuri Reis & Alexandre Reis',
      install_requires=['wheel', 'fpdf>=1.7.2', 'plotly>=2.0.7'],
      url='http://github.com/yurireeis/bddocs',
      dependency_links=['http://github.com/yurireeis/bddocs/tarball/master#egg=master'],
      platforms='All'
      )

# -*- coding: utf-8 -*
"""
Setup script for BDDOCS.
USAGE:
    python setup.py install
"""

import sys
import os.path
from setuptools import find_packages, setup

HERE0 = os.path.dirname(__file__) or os.curdir
os.chdir(HERE0)
HERE = os.curdir
sys.path.insert(0, HERE)


# -----------------------------------------------------------------------------
# CONFIGURATION:
# -----------------------------------------------------------------------------
python_version = float('{}'.format(sys.version_info[:2]))
requirements = ["plotly>=2.0.7", "fpdf>=1.7.2"]
if python_version < 3.3:
    Exception('You must have to install ver. 3.3 or higher')

BDDOCS = os.path.join(HERE, "bddocs")
# README = os.path.join(HERE, "README.rst")
# description = "".join(open(README).readlines()[4:])


# -----------------------------------------------------------------------------
# UTILITY:
# -----------------------------------------------------------------------------
def find_packages_by_root_package(where):
    """
    Better than excluding everything that is not needed,
    collect only what is needed.
    """
    root_package = os.path.basename(where)
    packages = ["%s.%s" % (root_package, sub_package)
                for sub_package in find_packages(where)]
    packages.insert(0, root_package)
    return packages


# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
setup(
    name="bddocs",
    version="1.0.0.dev0",
    description="bdddocs is behaviour-driven development documentation exporter, Python style",
    author="Yuri Reis, Alexandre Reis",
    author_email="yuri.reis@msn.com",
    url="http://github.com/yurireeis/bddocs",
    provides=["bddocs"],
    packages=find_packages_by_root_package(BDDOCS),
    entry_points={
        "console_scripts": [
            "bddocs = bddocs.__main__:main"
        ],
    },
    install_requires=requirements,
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: BSD License",
    ],
    zip_safe=True,
)

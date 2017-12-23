#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
from pygoogle import __author__, __version__

setup(
    name="pygoogle",
    author=__author__,
    version=__version__,
    packages=["pygoogle"],
    entry_points={
        "console_scripts": [
            "pygoogle=pygoogle.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ]
)


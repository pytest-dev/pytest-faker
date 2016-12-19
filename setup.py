#!/usr/bin/env python
"""pytest-faker package config."""

import codecs
import os
from setuptools import setup

import pytest_faker


dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, "README.rst"), encoding="utf-8").read() + "\n" +
    codecs.open(os.path.join(dirname, "AUTHORS.rst"), encoding="utf-8").read() + "\n" +
    codecs.open(os.path.join(dirname, "CHANGES.rst"), encoding="utf-8").read()
)

setup(
    name="pytest-faker",
    description="Faker integration with the pytest framework.",
    long_description=long_description,
    author="Anatoly Bubenkov, Oleg Pidsadnyi and others",
    license="MIT license",
    author_email="bubenkoff@gmail.com",
    url="https://github.com/pytest-dev/pytest-faker",
    version=pytest_faker.__version__,
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ] + [("Programming Language :: Python :: %s" % x) for x in "2.7 3.0 3.1 3.2 3.3 3.4".split()],
    install_requires=[
        "Faker>=0.7.3",
    ],
    # the following makes a plugin available to py.test
    entry_points={
        "pytest11": [
            "pytest-faker = pytest_faker.plugin",
        ],
    },
    tests_require=["tox"],
    packages=["pytest_faker"],
    include_package_data=True,
)

#!/usr/bin/env python2

from distutils.core import Command
import unittest

from setuptools import setup, find_packages


class Test(Command):
    description = "run the test suite"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        loader = unittest.TestLoader()
        suite = loader.discover("tests")
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    kwargs = {
        "cmdclass": {"test": Test},
        "name": "pymanopt",
        "version": "0.1",
        "description": ("Toolbox for manifold optimization with support for "
                        "automatic differentiation"),
        "url": "https://pymanopt.github.io",
        "author": "Jamie Townsend",
        "author_email": "jamiehntownsend@gmail.com",
        "license": "BSD",
        "packages": find_packages(),
    }
    setup(**kwargs)

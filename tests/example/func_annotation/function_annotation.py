# coding: utf-8

""" This module is the example of special functions' documentation,
    such as async function, context manager and generator.
"""

from abc import abstractmethod
from contextlib import contextmanager


async def async_function():
    """ Docstring of async_function.
    """
    pass

@contextmanager
def with_function():
    """ Docstring of with_function.
    """
    pass

def async_with_function():
    """ Docstring of async_with_function.
    """
    pass

async_with_function.__returns_acontextmanager__ = True

def for_function():
    """ Docstring of for_function.
    """
    yield

async def async_for_function():
    """ Docstring of async_for_function.
    """
    yield

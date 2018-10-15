# coding: utf-8

""" This module is the example of special functions' documentation,
    such as async function, context manager and generator.
"""

from abc import abstractmethod
from contextlib import contextmanager


async def async_function():
    """ .. function::
            :async:

            Docstring of async_function.
    """
    pass

@contextmanager
def with_function():
    """ .. function::
            :with:

            Docstring of with_function.
    """
    pass

@contextmanager
async def async_with_function():
    """ .. function::
            :async-with:

            Docstring of async_with_function.
    """
    pass

def for_function():
    """ .. function::
            :for:

            Docstring of for_function.
    """
    pass

async def async_for_function():
    """ .. function::
            :async-for:

            Docstring of async_for_function.
    """
    pass

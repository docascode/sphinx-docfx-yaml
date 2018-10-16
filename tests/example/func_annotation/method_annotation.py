# coding: utf-8

""" This module is the example of special class methods' documentation,
    such as classmethods, staticmethods and abstractmethods.
"""

from abc import abstractmethod
from contextlib import contextmanager

class AbstractStaticClass:
    """ The class containing special methods.
    """

    @staticmethod
    def static_method():
        """ Docstring of static_method.
        """
        pass

    @classmethod
    def class_method(cls):
        """ Docstring of class_method.
        """
        pass

    @abstractmethod
    def abstract_method(self):
        """ Docstring of abstract_method.
        """
        pass

    async def async_method(self):
        """ Docstring of async_method.
        """
        pass

    @contextmanager
    def with_method(self):
        """ Docstring of with_method.
        """
        pass

    def async_with_method(self):
        """ Docstring of async_with_method.
        """
        pass

    def for_method(self):
        """ Docstring of for_method.
        """
        yield

    async def async_for_method(self):
        """ Docstring of async_for_method.
        """
        yield

AbstractStaticClass.async_with_method.__returns_acontextmanager__ = True

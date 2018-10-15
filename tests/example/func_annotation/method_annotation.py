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
        """ .. method::
                :staticmethod:

                Docstring of static_method.
        """
        pass

    @classmethod
    def class_method(cls):
        """ .. method::
                :classmethod:

                Docstring of class_method.
        """
        pass

    @abstractmethod
    def abstract_method(self):
        """ .. method::
                :abstractmethod:

                Docstring of abstract_method.
        """
        pass

    async def async_method(self):
        """ .. method::
                :async:

                Docstring of async_method.
        """
        pass

    @contextmanager
    def with_method(self):
        """ .. method::
                :with:

                Docstring of with_method.
        """
        pass

    @contextmanager
    async def async_with_method(self):
        """ .. method::
                :async-with:

                Docstring of async_with_method.
        """
        pass

    def for_method(self):
        """ .. method::
                :for:

                Docstring of for_method.
        """
        pass

    async def async_for_method(self):
        """ .. method::
                :async-for:

                Docstring of async_for_method.
        """
        pass

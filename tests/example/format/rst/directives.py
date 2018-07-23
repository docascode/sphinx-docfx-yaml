# coding: utf-8

""" Docstring of module :mod:`format.rst.directives`.
This module is used for testing self-defined directives.

.. remarks:: Remarks from module directives.
"""

module_var = ''
""".. remarks:: Remarks from module variable."""


def func():
    """
    .. remarks:: Remarks from module function.
    """
    pass


class DirectivesFoo(object):
    """ Docstring of class :class:`format.rst.directives.DirectivesFoo`.

    .. remarks:: Remarks from class.
        Multi-line content should be supported.
    """

    var_remarks = ''
    """.. remarks:: Remarks from class attribute :class:`format.rst.directives.DirectivesFoo.var_remarks`."""

    def method_remarks(self):
        """
        .. remarks:: Remarks from class method :meth:`format.rst.directives.DirectivesFoo.method_remarks`
        """
        pass

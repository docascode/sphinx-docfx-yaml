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

    .. note::
        Note content from class docstring.
        Second line of note content.
        many lines of content.

    .. warning::
        Warning message from class docstring.
        Second line.

    .. tip::
        Tip content. :class:`format.rst.foo.Foo`

    .. important::
        Important content.

    .. caution::
        Caution content.

    .. remarks:: Remarks from class.
        Multi-line content should be supported.

        .. note::
            Note conetnt under class remarks.
            Second line of note content.

        .. warning::
            Warning content under class remarks.
            Second line.
            :class:`format.rst.foo.Foo`

        .. tip::
            Tip content.

        .. important::
            Important content.

        .. caution::
            Caution content.
    """

    var_remarks = ''
    """ .. remarks:: Remarks from class attribute :class:`format.rst.directives.DirectivesFoo.var_remarks`."""

    def method_remarks(self):
        """
        .. remarks:: Remarks from class method :meth:`format.rst.directives.DirectivesFoo.method_remarks`
            Another reference: :class:`format.rst.directives.DirectivesFoo`
        """
        pass

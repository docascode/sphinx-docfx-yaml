"""Example module

This is a description
"""


class Foo(object):
    """
    A sweet Foo class that does stuff.

    .. remarks:: This is remarks message of class Foo.
    """

    class_var = 42  #: Class var docstring

    another_class_var = 42
    """Another class var docstring"""

    class Meta(object):
        """A nested class just to test things out"""

        @classmethod
        def foo():
            """The foo class method"""
            return True

    def method_okay(self, foo=None, bar=None):
        """
        This method should parse okay

        .. remarks:: This is remarks message of method Foo.method_okay.
            And multiple lines should be supported.

        :param str foo: The foo param
        :param str bar: The bar param
        :return: That the method is okay
        :rtype: boolean
        """
        return True

    def method_markdown(self):
        """
        Check out our `site <http://sphinx-docfx-yaml.readthedocs.io/en/latest/>`_ for more info.
        """
        pass

    def method_multiline(self, foo=None, bar=None,
                         baz=None):
        """This is on multiple lines, but should parse okay too

        pydocstyle gives us lines of source. Test if this means that multiline
        definitions are covered in the way we're anticipating here
        """
        return True

    def method_tricky(self, foo=None, bar=dict(foo=1, bar=2)):
        """This will likely fail our argument testing

        We parse naively on commas, so the nested dictionary will throw this off
        """
        return True

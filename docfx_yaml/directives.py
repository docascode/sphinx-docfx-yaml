# coding: utf-8

"""
This module is used to add extra supported directives to sphinx.
"""

from docutils.parsers.rst import Directive
from docutils import nodes

from .nodes import remarks


class RemarksDirective(Directive):
    """
    Class to enable remarks directive.
    """

    # Enable content in the directive
    has_content = True

    # Directive class must override run function.
    def run(self):
        self.assert_has_content()

        text = '\n'.join(self.content)

        return_nodes = []

        node = remarks('', text)
        return_nodes.append(node)

        return return_nodes

class TodoDirective(Directive):
    """
    Class to ignore todo directive.
    """

    # Enable content in the directive
    has_content = True

    # Directive class must override run function.
    def run(self):
        return_nodes = []

        return return_nodes

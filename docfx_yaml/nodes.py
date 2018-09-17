# coding: utf-8

"""
This module is used to add extra supported nodes to sphinx.
"""

from docutils import nodes

class remarks(nodes.paragraph, nodes.Element):
    """
    New node for remarks messages.
    """

    @staticmethod
    def visit_remarks(self, node):
        self.visit_paragraph(node)

    @staticmethod
    def depart_remarks(self, node):
        self.depart_paragraph(node)

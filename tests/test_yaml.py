import yaml
import os
import shutil
from contextlib import contextmanager
import unittest

from sphinx.application import Sphinx


@contextmanager
def sphinx_build(test_dir):
    os.chdir('tests/{0}'.format(test_dir))
    try:
        app = Sphinx(
            srcdir='.',
            confdir='.',
            outdir='_build/text',
            doctreedir='_build/.doctrees',
            buildername='text',
        )
        app.build(force_all=True)
        yield
    finally:
        shutil.rmtree('_build')
        os.chdir('../..')


class PythonTests(unittest.TestCase):

    def test_yaml(self):
        """
        A basic YAML test to hold test data.

       :param str sender: The person :ref:`sending** the message
       :param str recipient: The recipient of the message,
                             `YAML <http://example.com>`_.
       :param str message_body: The body of the message
       :param priority: The priority of the message, can be a number 1-5
       :type priority: integer or None
       :return: the message id
       :rtype: int
       :raises ValueError: if the message_body exceeds 160 characters
       :raises TypeError: if the message_body is not a basestring
        """
        self.assertTrue(1, 1)

    def test_functional(self):
        """
        A basic functional test
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.example.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                self.assertEqual(
                    data['items'][0]['fullName'],
                    'example.example'
                )

    def test_module_summary(self):
        """
        Test that we're pulling the top-level module summary
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.example.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.example':
                        self.assertEqual(
                            item['summary'],
                            'Example module\n\nThis is a description'
                        )
                        break
                else:
                    self.fail('Module not found')

    def test_references(self):
        """
        Test references are properly inserted.
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.example.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                # Test that references are properly put at the top-level
                self.assertTrue(
                    'references' in data
                )
                # Check reference parent
                self.assertEqual(
                    data['references'][0]['parent'],
                    'example.example'

                )

    def test_inheritance(self):
        """
        Test multiple inheritance is properly resolved.
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.multiple_inheritance.ObservableArbitraryWidget.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.multiple_inheritance.ObservableArbitraryWidget':
                        self.assertTrue(
                            'inheritance' in item
                        )
                        self.assertEqual(
                            item['inheritance'][0]['type'],
                            'example.multiple_inheritance.ArbitraryWidget'
                        )
                        self.assertEqual(
                            item['inheritance'][1]['type'],
                            'example.multiple_inheritance.Subject'
                        )

    def test_docfields(self):
        """
        Test docfields are parsed properly
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.example.Foo.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.example.Foo.method_okay':
                        self.assertEqual(
                            item['syntax']['return'],
                            {'type': 'boolean', 'description': 'That the method is okay'},
                        )

    def test_vcs(self):
        """
        Test VCS info is parsed properly.
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.example.Foo.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.example.Foo':
                        self.assertEqual(
                            item['source']['startLine'],
                            7,
                        )
                        self.assertEqual(
                            item['source']['remote']['path'],
                            'tests/pyexample/example/example.py',
                        )

    def test_markdown(self):
        """
        Test Markdown content is converted
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.example.Foo.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.example.Foo.method_markdown':
                        self.assertEqual(
                            item['summary'],
                            'Check out our '
                            '[site](http://sphinx-docfx-yaml.readthedocs.io/en/latest/)'
                            ' for more info.',
                        )

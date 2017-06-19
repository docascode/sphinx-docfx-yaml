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
            with open(
                '_build/text/docfx_yaml/'
                'example.multiple_inheritance.ObservableArbitraryWidget.yml'
            ) as yml_file:
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
                            {'type': ['boolean'], 'description': 'That the method is okay'},
                        )
                        self.assertEqual(
                            item['syntax']['parameters'][1]['defaultValue'],
                            'None',
                        )
                        self.assertEqual(
                            item['syntax']['parameters'][1]['description'],
                            'The foo param',
                        )
                        self.assertEqual(
                            item['syntax']['content'],
                            'method_okay(self, foo=None, bar=None)',
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

    def test_napoleon(self):
        """
        Test Napolean content is converted
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.nap.Base.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.nap.Base.foo':
                        self.assertEqual(
                            item['syntax']['parameters'][1]['description'],
                            'The Foo instance is destructed'
                        )
                        self.assertEqual(
                            item['seealsoContent'],
                            'Some cool stuff online.'
                        )

    def test_xref(self):
        """
        Test xref parsing for Python domain objects
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.nap.Base.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.nap.Base.ref':
                        self.assertEqual(
                            item['seealsoContent'],
                            'Depends on @example.example.Foo Relative reference on @example.nap.Base.foo'
                        )

    def test_toc(self):
        """
        Test second level toc nesting
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/toc.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data:
                    if 'items' in item:
                        self.assertEqual(
                            item['items'][0]['name'],
                            'example.enum_type.EnumFoo'
                        )
                        break

    def test_examples(self):
        """
        Test second level toc nesting
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.nap.Base.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.nap.Base.ref':
                        self.assertEqual(
                            item['example'].split('\n')[2],
                            """>>> print('docblock 1')"""
                        )
                        self.assertEqual(
                            item['example'].split('\n')[7],
                            """>>> print('docblock 2')"""
                        )

    def test_enum(self):
        """
        Test enum type support
        """
        with sphinx_build('pyexample'):
            with open('_build/text/docfx_yaml/example.enum_type.EnumFoo.yml') as yml_file:
                data = yaml.safe_load(yml_file)
                for item in data['items']:
                    if item['uid'] == 'example.enum_type.EnumFoo':
                        self.assertEqual(
                            item['children'],
                            ['example.enum_type.EnumFoo.VALUE0', 'example.enum_type.EnumFoo.VALUE1']
                        )
                    if item['uid'] == 'example.enum_type.EnumFoo.VALUE0':
                        self.assertEqual(
                            item['syntax'],
                            {'content': 'VALUE0 = 0', 'return': {'type': ['example.enum_type.EnumFoo']}}
                        )
                        self.assertEqual(
                            item['type'],
                            'attribute'
                        )
                    if item['uid'] == 'example.enum_type.EnumFoo.VALUE1':
                        self.assertEqual(
                            item['syntax'],
                            {'content': 'VALUE1 = 1', 'return': {'type': ['example.enum_type.EnumFoo']}}
                        )
                        self.assertEqual(
                            item['type'],
                            'attribute'
                        )

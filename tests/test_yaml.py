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


class LanguageIntegrationTests(unittest.TestCase):

    def _run_test(self, test_dir, test_file, test_string):
        with sphinx_build(test_dir):
            with open(test_file) as fin:
                text = fin.read().strip()
                self.assertIn(test_string, text)


class PythonTests(LanguageIntegrationTests):

    def test_integration(self):
        with sphinx_build('pyexample'):
            data = yaml.safe_load(open('_build/text/docfx_yaml/example.example.yml'))
            self.assertEqual(
                data['items'][0]['name'],
                'example.example.Foo'
            )

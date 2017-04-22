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

    def test_yaml(self):
        """
       A basic YAML test

       :param str sender: The person :ref:`sending** the message
       :param str recipient: The recipient of the message, `YAML <http://example.com>`_ 
       :param str message_body: The body of the message
       :param priority: The priority of the message, can be a number 1-5
       :type priority: integer or None
       :return: the message id
       :rtype: int
       :raises ValueError: if the message_body exceeds 160 characters
       :raises TypeError: if the message_body is not a basestring
        """
        self.assertTrue(1, 1)


class PythonTests(LanguageIntegrationTests):

    def test_integration(self):
        with sphinx_build('pyexample'):
            data = yaml.safe_load(open('_build/text/docfx_yaml/example.example.yml'))
            self.assertEqual(
                data['items'][2]['name'],
                'example.example.Foo'
            )

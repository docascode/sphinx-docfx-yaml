import os
import shutil
import unittest
from contextlib import contextmanager
from sphinx.application import Sphinx

@contextmanager
def sphinx_build(test_dir):
    os.chdir('tests/{0}'.format(test_dir))

    try:
        app = Sphinx(
            srcdir='../example/doc',
            confdir='../example/doc',
            outdir='_build/yaml',
            doctreedir='_build/.doctrees',
            buildername='html',
        )
        app.build(force_all=True)
        yield
    finally:
        # shutil.rmtree('_build')
        os.chdir('../..')

if __name__ == '__main__':
    with sphinx_build('debug'):
        print('Debug finished.')

# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

source_suffix = '.rst'
master_doc = 'index'
project = u'example'
copyright = u'2018, Microsoft'
author = u'Yiding Tian'
version = '0.1'
release = '0.1'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'Example Document'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'docfx_yaml.extension'
]
intersphinx_mapping = {'python': ('https://docs.python.org/3.6', None)}

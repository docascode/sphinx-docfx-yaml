# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.abspath('.'))

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'example'
copyright = u'2018, Microsoft'
author = u'Yiding Tian'
version = '0.1'
release = '0.1'

language = 'en'
pygments_style = 'sphinx'

html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'Example Document'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intershpinx',
    'sphinx.ext.extlinks',
    'docfx_yaml.extension'
]

# sphinx.ext.autodoc options
autodoc_docstring_signature = False

# sphinx.ext.napoleon options
napoleon_use_admonition_for_examples = True
remove_inheritance_for_notfound_class = True

# sphinx.ext.intershpinx options
intersphinx_mapping = {'python': ('https://docs.python.org/3.6', None)}

# sphinx.ext.extlinks options
extlinks = {}

exclude_patterns = [
    '_build',
    '*.tests.*rst'
]
# -*- coding: utf-8 -*-
"""
Sphinx DocFX YAML Top-level Extension.

This extension allows you to automagically generate DocFX YAML from your Python Domains.
"""
import os

from yaml import safe_dump as dump

from sphinx.util.console import darkgreen, bold
from sphinx.util import ensuredir
from sphinx.errors import ExtensionError

from .settings import API_ROOT


class Extension(object):
    """
    This is just for testing.

        print "hello world"

    This is more testing.
    """

    pass

    def foo(self):
        """
        Foo test method
        """
        pass

    def bar(self, woot):
        """
        Test bar method
        """
        pass


# We need to map the Python type names to what DocFX is expecting
TYPE_MAPPING = {
    'method': 'Method',
    'function': 'Method',
    'module': 'Namespace',
    'class': 'Class',
    'exception': 'Class',  # Hack this for now
    'attribute': 'Property',  # Ditto
}


def build_init(app):
    """
    Set up environment data
    """
    if not app.config.docfx_yaml_output:
        raise ExtensionError('You must configure an docfx_yaml_output setting')

    app.env.docfx_yaml_modules = {}


def process_docstring(app, _type, name, obj, options, lines):
    cls = None
    if _type in ['function', 'exception']:
        module = '.'.join(name.split('.')[:-1])
    elif _type in ['method', 'attribute']:
        cls = '.'.join(name.split('.')[:-1])
        module = '.'.join(name.split('.')[:-2])
    elif _type in ['class']:
        module = '.'.join(name.split('.')[:-1])
    elif _type in ['module']:
        module = name
    else:
        print('Unknown Type: %s' % _type)
        return

    try:
        mapped_type = TYPE_MAPPING[_type]
    except:
        print('Invalid Type Mapping: %s' % _type)

    datam = {
        'module': module,
        'uid': name,
        'type': mapped_type,
        '_type': _type,
        'name': name,
        'summary': '\n'.join(lines),
    }

    if cls:
        datam['class'] = cls
    if _type in ['class', 'module']:
        datam['children'] = []

    if module not in app.env.docfx_yaml_modules:
        app.env.docfx_yaml_modules[module] = [datam]
    else:
        app.env.docfx_yaml_modules[module].append(datam)

    insert_children(app, _type, datam)


def insert_children(app, _type, datam):
    insert_module = app.env.docfx_yaml_modules[datam['module']]
    for obj in insert_module:
        if _type in ['method', 'attribute'] and \
                obj['_type'] == 'class' and \
                obj['uid'] == datam['class']:
            obj['children'].append(datam['uid'])
            break
        elif _type in ['class', 'function', 'exception'] and \
                obj['_type'] == 'module' and \
                obj['module'] == datam['module']:
            obj['children'].append(datam['uid'])
            break
    else:
        print('Module has no children: %s' % datam['module'])


def build_finished(app, exception):
    """
    Output YAML on the file system.
    """

    normalized_output = os.path.normpath(os.path.join(
        app.builder.outdir,  # Output Directory for Builder
        app.config.docfx_yaml_output
    ))

    # Get correct data set
    # if app.config.docfx_yaml_mode == 'rst':
    #     iter_data = app.env.docfx_yaml_data
    if app.config.docfx_yaml_mode == 'module':
        iter_data = app.env.docfx_yaml_modules

    for filename, yaml_data in iter_data.items():
        if not filename:
            # Skip objects without a module
            continue
        out_file = os.path.join(normalized_output, '%s.yml' % filename)
        ensuredir(os.path.dirname(out_file))
        if app.verbosity > 1:
            app.info(bold('[docfx_yaml] ') + darkgreen('Outputting %s' % filename))
        dump({'items': yaml_data}, open(out_file, 'w+'), default_flow_style=False)


def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)
    app.connect('builder-inited', build_init)
    app.connect('build-finished', build_finished)
    app.add_config_value('docfx_yaml_output', API_ROOT, 'html')
    app.add_config_value('docfx_yaml_ignore', [], 'html')
    app.add_config_value('docfx_yaml_mode', 'module', 'html')

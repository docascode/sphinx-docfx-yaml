# -*- coding: utf-8 -*-
"""
Sphinx DocFX YAML Top-level Extension.

This extension allows you to automagically generate DocFX YAML from your Python Domains.
"""
import os
from collections import defaultdict

from yaml import safe_dump as dump

from sphinx.util.console import darkgreen, bold, red
from sphinx.util import ensuredir
from sphinx.errors import ExtensionError
from sphinx import addnodes

from .settings import API_ROOT


def build_init(app):
    if not app.config.docfx_yaml_output:
        raise ExtensionError('You must configure an docfx_yaml_output setting')

    app.env.docfx_yaml_data = {}
    app.env.docfx_yaml_modules = {}


def doctree_resolved(app, doctree, docname):
    """
    Render out the YAML from the Sphinx domain objects
    """
    ignore_patterns = app.config.docfx_yaml_ignore or None
    yaml_data, yaml_modules = extract_yaml(app, doctree, ignore_patterns)
    if yaml_data:
        app.env.docfx_yaml_data[docname] = yaml_data
    if yaml_modules:
        for module in yaml_modules:
            app.env.docfx_yaml_modules[module] = yaml_modules[module]


def extract_yaml(app, doctree, ignore_patterns):
    """
    Iterate over all Python domain objects and output YAML
    """
    items = []
    modules = defaultdict(list)

    for desc_node in doctree.traverse(addnodes.desc):
        if desc_node.attributes['domain'] != 'py':
            app.info(bold('[docfx_yaml] ') + red(
                'Skipping Domain Object (%s)' % desc_node.attributes['domain']
            ))
            continue

        module = desc_node[0].attributes['module']
        _type = desc_node.attributes['objtype']
        full_name = desc_node[0].attributes['fullname']
        _id = desc_node[0].attributes['ids'][0]
        name = desc_node[0].attributes['names'][0]
        source = desc_node[0].source
        summary = desc_node[1][0].astext()

        try:
            args = [arg.strip() for arg in desc_node[0][3].astext().split(',')]
        except:
            args = []

        if args:
            full_name += "({args})".format(args=', '.join(args))

        mapping = {
            'method': 'Method',
            'function': 'Method',
            'module': 'Namespace',
            'class': 'Class',
        }

        try:
            mapped_type = mapping[_type]
        except:
            print('Invalid Type Mapping: %s' % _type)


        datam = {
            'module': str(module),
            'uid': _id,
            'type': mapped_type,
            'name': name,
            'fullName': full_name,
            'summary': summary,
            'rst_source': source,
        }


        items.append(datam)
        modules[module].append(datam)

    return (items, modules)


def build_finished(app, exception):
    """
    Output YAML on the file system.
    """

    normalized_output = os.path.normpath(os.path.join(
        app.builder.outdir,  # Output Directory for Builder
        app.config.docfx_yaml_output
    ))

    # Get correct data set
    if app.config.docfx_yaml_mode == 'rst':
        iter_data = app.env.docfx_yaml_data
    if app.config.docfx_yaml_mode == 'module':
        iter_data = app.env.docfx_yaml_modules

    for filename, yaml_data in iter_data.items():
        out_file = os.path.join(normalized_output, '%s.yml' % filename)
        ensuredir(os.path.dirname(out_file))
        if app.verbosity > 1:
            app.info(bold('[docfx_yaml] ') + darkgreen('Outputting %s' % filename))
        dump({'items': yaml_data}, open(out_file, 'w+'), default_flow_style=False)


def setup(app):
    app.connect('builder-inited', build_init)
    app.connect('doctree-resolved', doctree_resolved)
    app.connect('build-finished', build_finished)
    app.add_config_value('docfx_yaml_output', API_ROOT, 'html')
    app.add_config_value('docfx_yaml_ignore', [], 'html')
    app.add_config_value('docfx_yaml_mode', 'module', 'html')

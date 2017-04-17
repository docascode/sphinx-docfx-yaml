"""
Deprecated approach that pulls domain data from doctree.

This approach will work for non-autodoc domains.
However,
the approach used in this extension is easiest for autodoc.

In order to build the approach going forward,
a bit more work needs to be done to pull docstrings in raw format.
"""

from docutils import nodes
from sphinx.util.console import bold, red
from sphinx.util.docfields import _is_single_paragraph
from sphinx import addnodes

TITLE_MAP = {
    'Returns': 'return',
    'Return type': 'return_type',
    'Raises': 'raises',
    'Parameters': 'params',
}


def doctree_resolved(app, doctree, docname):
    """
    Render out the YAML from the Sphinx domain objects
    """
    yaml_data, yaml_modules = extract_yaml(app, doctree, ignore_patterns=None)
    extract_info_lists(app, doctree)
    # if yaml_data:
    #     app.env.docfx_yaml_data[docname] = yaml_data
    # if yaml_modules:
    #     for module in yaml_modules:
    #         app.env.docfx_yaml_modules[module] = yaml_modules[module]


def extract_info_lists(app, doctree):
    for desc_node in doctree.traverse(addnodes.desc):
        if desc_node.attributes['domain'] != 'py':
            app.info(bold('[docfx_yaml] ') + red(
                'Skipping Domain Object (%s)' % desc_node.attributes['domain']
            ))
            continue

        module = desc_node[0].attributes['module']
        for node in desc_node.traverse(nodes.field_list):
            for field in node:
                fieldname, fieldbody = field
                try:
                    # split into field type and argument
                    fieldtype, fieldarg = fieldname.astext().split(None, 1)
                except ValueError:
                    # maybe an argument-less field type?
                    fieldtype, fieldarg = fieldname.astext(), ''

                # collect the content, trying not to keep unnecessary paragraphs
                if _is_single_paragraph(fieldbody):
                    content = fieldbody.children[0].children
                else:
                    content = fieldbody.children

                print(module, fieldtype, fieldarg, fieldname, fieldbody, content)


def extract_yaml(app, doctree, ignore_patterns):
    """
    Iterate over all Python domain objects and output YAML
    """
    items = []
    modules = {}

    for desc_node in doctree.traverse(addnodes.desc):
        if desc_node.attributes['domain'] != 'py':
            app.info(bold('[docfx_yaml] ') + red(
                'Skipping Domain Object (%s)' % desc_node.attributes['domain']
            ))
            continue

        module = desc_node[0].attributes['module']

        if not module:
            app.info(bold('[docfx_yaml] ') + red(
                'Skipping object with no module'
            ))
            continue

        if module not in modules:
            modules[module] = [{
                'module': str(module),
                'uid': str(module),
                'type': 'Namespace',
                '_type': 'module',
                'name': str(module),
                'children': []
            }]

        _type = desc_node.attributes['objtype']
        full_name = desc_node[0].attributes['fullname']
        try:
            _id = desc_node[0].attributes['ids'][0]
        except Exception:
            _id = '{module}.{full_name}'.format(module=module, full_name=full_name)
            print('Non-standard id: %s' % _id)
        name = desc_node[0].attributes['names'][0]
        source = desc_node[0].source
        try:
            summary = desc_node[1][0].astext()
        except (KeyError, IndexError):
            summary = ''

        try:
            args = [arg.strip() for arg in desc_node[0][3].astext().split(',')]
        except Exception:
            args = []

        if args:
            full_name += "({args})".format(args=', '.join(args))

        # We need to map the Python type names to what DocFX is expecting

        datam = {
            'module': str(module),
            'uid': _id,
            '_type': _type,
            'name': name,
            'fullName': full_name,
            'summary': summary,
            'rst_source': source,
        }

        if _type == 'method':
            datam['class'] = '.'.join(name.split('.')[:-1])
        if _type == 'class':
            datam['children'] = []

        # insert_children(_type, datam, modules)
        items.append(datam)

        modules[module].append(datam)

    return (items, modules)

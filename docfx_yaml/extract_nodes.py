"""
Deprecated approach that pulls domain data from doctree.

This approach will work for non-autodoc domains.
However,
the approach used in this extension is easiest for autodoc.

In order to build the approach going forward,
a bit more work needs to be done to pull docstrings in raw format.
"""

from sphinx.util.console import darkgreen, bold, red
from sphinx import addnodes


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
        except:
            _id = '{module}.{full_name}'.format(module=module, full_name=full_name)
            print('Non-standard id: %s' % _id)
        name = desc_node[0].attributes['names'][0]
        source = desc_node[0].source
        try:
            summary = desc_node[1][0].astext()
            import ipdb
            ipdb.set_trace()
        except (KeyError, IndexError):
            summary = ''

        try:
            args = [arg.strip() for arg in desc_node[0][3].astext().split(',')]
        except:
            args = []

        if args:
            full_name += "({args})".format(args=', '.join(args))

        # We need to map the Python type names to what DocFX is expecting
        try:
            mapped_type = TYPE_MAPPING[_type]
        except:
            print('Invalid Type Mapping: %s' % _type)

        datam = {
            'module': str(module),
            'uid': _id,
            'type': mapped_type,
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

        insert_children(_type, datam, modules)
        items.append(datam)

        modules[module].append(datam)

    return (items, modules)

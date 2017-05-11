from docutils import nodes
from functools import partial

from sphinx.util.docfields import _is_single_paragraph
from sphinx.util import docfields
from sphinx import directives, addnodes

from .utils import transform_node as _transform_node


def _get_desc_data(node):
    assert node.tagname == 'desc'
    if node.attributes['domain'] != 'py':
        print(
            'Skipping Domain Object (%s)' % node.attributes['domain']
        )
        return None, None
    module = node[0].attributes['module']
    full_name = node[0].attributes['fullname'].split('.')[-1]
    try:
        uid = node[0].attributes['ids'][0]
    except Exception:
        uid = '{module}.{full_name}'.format(module=module, full_name=full_name)
        print('Non-standard id: %s' % uid)
    return full_name, uid


def _hacked_transform(typemap, node):
    """
    Taken from docfields.py from sphinx.

    This does all the steps around gathering data,
    but doesn't actually do the node transformations.
    """
    entries = []
    groupindices = {}
    types = {}

    # step 1: traverse all fields and collect field types and content
    for field in node:
        fieldname, fieldbody = field
        try:
            # split into field type and argument
            fieldtype, fieldarg = fieldname.astext().split(None, 1)
        except ValueError:
            # maybe an argument-less field type?
            fieldtype, fieldarg = fieldname.astext(), ''
        typedesc, is_typefield = typemap.get(fieldtype, (None, None))

        # sort out unknown fields
        if typedesc is None or typedesc.has_arg != bool(fieldarg):
            # either the field name is unknown, or the argument doesn't
            # match the spec; capitalize field name and be done with it
            new_fieldname = fieldtype[0:1].upper() + fieldtype[1:]
            if fieldarg:
                new_fieldname += ' ' + fieldarg
            fieldname[0] = nodes.Text(new_fieldname)
            entries.append(field)
            continue

        typename = typedesc.name

        # collect the content, trying not to keep unnecessary paragraphs
        if _is_single_paragraph(fieldbody):
            content = fieldbody.children[0].children
        else:
            content = fieldbody.children

        # if the field specifies a type, put it in the types collection
        if is_typefield:
            # filter out only inline nodes; others will result in invalid
            # markup being written out
            content = [n for n in content if isinstance(n, nodes.Inline) or
                       isinstance(n, nodes.Text)]
            if content:
                types.setdefault(typename, {})[fieldarg] = content
            continue

        # also support syntax like ``:param type name:``
        if typedesc.is_typed:
            try:
                argtype, argname = fieldarg.split(None, 1)
            except ValueError:
                pass
            else:
                types.setdefault(typename, {})[argname] = \
                    [nodes.Text(argtype)]
                fieldarg = argname

        translatable_content = nodes.inline(fieldbody.rawsource,
                                            translatable=True)
        translatable_content.source = fieldbody.parent.source
        translatable_content.line = fieldbody.parent.line
        translatable_content += content

        # grouped entries need to be collected in one entry, while others
        # get one entry per field
        if typedesc.is_grouped:
            if typename in groupindices:
                group = entries[groupindices[typename]]
            else:
                groupindices[typename] = len(entries)
                group = [typedesc, []]
                entries.append(group)
            entry = typedesc.make_entry(fieldarg, [translatable_content])
            group[1].append(entry)
        else:
            entry = typedesc.make_entry(fieldarg, [translatable_content])
            entries.append([typedesc, entry])

    return (entries, types)


def patch_docfields(app):
    """
    Grab syntax data from the Sphinx info fields.

    This is done by monkeypatching into the DocFieldTransformer,
    which is what Sphinx uses to transform the docutils ``nodes.field``
    into the sphinx ``docfields.Field`` objects.

    See usage in Sphinx
    `here <https://github.com/sphinx-doc/sphinx/blob/master/sphinx/directives/__init__.py#L180>`_.

    This also performs the RST doctree to Markdown transformation on the content,
    using the :any:`docfx_yaml.writers.MarkdownWriter`.
    """

    transform_node = partial(_transform_node, app)

    def get_data_structure(entries, types):
        """
        Get a proper docfx YAML data structure from the entries & types
        """

        data = {
            'parameters': [],
            'variables': [],
            'exceptions': [],
            'return': {},
        }

        def make_param(_id, _description, _type=None):
            ret = {
                'id': _id,
                'description': _description,
            }
            if _type:
                ret['type'] = [_type]
            return ret

        for entry in entries:
            if isinstance(entry, nodes.field):
                # pass-through old field
                pass
            else:
                fieldtype, content = entry
                fieldtypes = types.get(fieldtype.name, {})
                if fieldtype.name == 'exceptions':
                    for _type, _description in content:
                        data['exceptions'].append({
                            'type': _type,
                            'description': transform_node(_description[0])
                        })
                if fieldtype.name == 'returntype':
                    returntype_ret = u''.join(n.astext() for n in content[1])
                    if returntype_ret:
                        data['return']['type'] = [returntype_ret]
                if fieldtype.name == 'returnvalue':
                    returnvalue_ret = transform_node(content[1][0])
                    if returnvalue_ret:
                        data['return']['description'] = returnvalue_ret
                if fieldtype.name in ['parameter', 'variable']:
                    for field, node_list in content:
                        _id = field
                        _description = transform_node(node_list[0])
                        if field in fieldtypes:
                            _type = u''.join(n.astext() for n in fieldtypes[field])
                        else:
                            _type = None
                        if fieldtype.name == 'parameter':
                            _data = make_param(_id=_id, _type=_type, _description=_description)
                            data['parameters'].append(_data)
                        if fieldtype.name == 'variable':
                            _data = make_param(_id=_id, _type=_type, _description=_description)
                            data['variables'].append(_data)

        return data

    class PatchedDocFieldTransformer(docfields.DocFieldTransformer):

        def __init__(self, directive):
            self.directive = directive
            super(PatchedDocFieldTransformer, self).__init__(directive)

        def transform_all(self, node):
            """Transform all field list children of a node."""
            # don't traverse, only handle field lists that are immediate children
            summary = []
            data = {}
            name, uid = _get_desc_data(node.parent)
            for child in node:
                if isinstance(child, addnodes.desc):
                    # Don't recurse into child nodes
                    continue
                elif isinstance(child, nodes.field_list):
                    (entries, types) = _hacked_transform(self.typemap, child)
                    _data = get_data_structure(entries, types)
                    data.update(_data)
                elif isinstance(child, addnodes.seealso):
                    data['seealso'] = transform_node(child)
                elif isinstance(child, nodes.admonition) and 'Example' in child[0].astext():
                    data['example'] = transform_node(child[1])
                else:
                    content = transform_node(child)
                    summary.append(content)
            if summary:
                data['summary'] = '\n'.join(summary)
            # Don't include empty data
            for key, val in data.copy().items():
                if not val:
                    del data[key]
            self.directive.env.docfx_info_field_data[uid] = data
            super(PatchedDocFieldTransformer, self).transform_all(node)

    directives.DocFieldTransformer = PatchedDocFieldTransformer

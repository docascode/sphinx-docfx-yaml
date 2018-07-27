How to Document Python API
===

This is a guidance for writing docstrings of your python code. The API reference will be hosted on [Microsoft Docs][docs].
***

# Overview
We generate the API reference documentation from source code files automatically. Actually our tool is an extension for [Sphinx][sphinx]. If you are familiar with [Sphinx][sphinx], this guidance will be extremely easy for you. Find our tool on [Github][docfx_yaml].

All the docstrings should be written in [reStructuredText][rst] (RST) format.

## Directives
Directives are a mechanism to extend the content of RST. Every directive declares a block of content with specific role. Start a new line with `.. directive_name::` to use the directive.

For example, following directive declares a `See Also` content:

``` rst
An empty line should be added between plain contents and directive blocks as below.

.. seealso:: Content of seealso block.
    Indents should be used for multiple lines contents.

More plain contens.
```

### All Supported Sphinx Directives

|directives|description|
|---:|---|
|*.. seealso::*|Indicating `See Also` content. Read [See Also](#see-also) for more information.|
|*.. code-block::*|Indicating a code fragment. Read [Code](#code) for more information.|
|*.. literalinclude::*|Include contents from another file. Read more [here](http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude).|
|*.. admonition::*|Read [Example](#example) for more information.|
|*.. math::*|Indicating a math formula. Latex format is supported. See [Math](#math).|
|*.. rubric::*||
|*.. title::*||
|*::*|Indicating a literal block. The contents will be regarded as plain text. See [Literal Block](#literal-block).|


## Inline Markups

# Reference
## Class
## Module
## Package
## Methods
## Functions
## Images
## Links
## List
## Math
## Table
## Include
## Example
## Code
## Note
## Warning
## See Also
## Remarks
## Literal Block

# Google/Numpy Style Docstring
Google-style and Numpy-style

You can write your doc strings in two kinds of styles.

reStrctureText
===
reStrctureText is a
Supported field lists:
- :param:
- :args:
- :return:
- :rtype:

refering:
- :class:
- :meth:
- :func:
- :mod:

Google/Numpy
===
Args (alias of Parameters)
Arguments (alias of Parameters)
Example
Examples
Methods
Parameters
Return (alias of Returns)
Returns
Raises
References
See Also

[docs]: https://docs.microsoft.com
[sphinx]: http://www.sphinx-doc.org
[docfx_yaml]: https://github.com/docascode/sphinx-docfx-yaml
[rst]: http://docutils.sourceforge.net/rst.html

How to Document Python API
===

This is a guidance for writing docstrings of your python code. The API reference will be hosted on [Microsoft Docs][docs].
***

# Overview
We generate the API reference documentation from source code files automatically. Actually our tool is an extension for [Sphinx][sphinx]. If you are familiar with [Sphinx][sphinx], section [All Supported Sphinx Directives](#all-supported-sphinx-directives) and [All Supported Inline Markups](#all-supported-inline-markups) will be usefully.

All the docstrings should be written in [reStructuredText][rst] (RST) format.

Find our tool on [Github][docfx_yaml].

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

| directives            | description                                                                                                                                                |
| --------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *.. seealso::*        | Indicating `See Also` content. Read [See Also](#see-also) for more information.                                                                            |
| *.. code-block::*     | Indicating a code fragment. Read [Code](#code) for more information.                                                                                       |
| *.. literalinclude::* | Include contents from another file. Read more [here](http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude). |
| *.. admonition::*     | Read [Example](#example) for more information.                                                                                                             |
| *.. math::*           | Indicating a math formula. [Latex format](https://en.wikibooks.org/wiki/LaTeX/Mathematics) is supported. See [Math](#math).                                |
| *.. title::*          | Indicating a title.                                                                                                                                        |
| *::*                  | Indicating a literal block. The contents will be regarded as plain text. See [Literal Block](#literal-block).                                              |

## Inline Markups

Inline markups are used to describe detailed information of package members. Such as Modules, Classes, Class Methods, Class Attributes, Functions and Variables. Inline markups follows such fomat:

``` rst
:inline_markup_name: Description for this markup.
```

For example, `:param:` describes parameter information of functions:

``` python
def foo(arg1, arg2):
    """ Docstring of function foo.

    :param arg1: Describing the first parameter of foo().
    :param arg2: Describing the second parameter of foo().
    """
    pass
```

### All Supported Inline Markups

| inline markup | description                                                           |
| ------------: | --------------------------------------------------------------------- |
| *:param:*     | Description of a function/method parameter.                           |
| *:parameter:* | Alias of :param:                                                      |
| *:arg:*       | Alias of :param:                                                      |
| *:argument:*  | Alias of :param:                                                      |
| *:key:*       | Alias of :param:                                                      |
| *:keyword:*   | Alias of :param:                                                      |
| *:type:*      | Type of a parameter. Creates a cross-reference if possible.           |
| *:raises:*    | That (and when) a specific exception is raised.                       |
| *:raise:*     | Alias of :raises:                                                     |
| *:except:*    | Alias of :raises:                                                     |
| *:exception:* | Alias of :raises:                                                     |
| *:var:*       | Description of a variable. Also used for describing class attributes. |
| *:ivar:*      | Alias of :var:                                                        |
| *:cvar:*      | Alias of :var:                                                        |
| *:vartype:*   | Type of a variable. Creates a cross-reference if possible.            |
| *:returns:*   | Description of the return value.                                      |
| *:return:*    | Alias of :returns:                                                    |
| *:rtype:*     | Return type. Creates a cross-reference if possible.                   |

# Details

Following contents will show how to write docstring for specific purposes in detail and give some examples.

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
## Cross Reference

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

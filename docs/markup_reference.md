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

### Attributes

To describe attributes of a class, use `:var:` inline markup. `:vartype:` can be used to tell the type of attributes.

Example:
``` python
TODO: include code.
```

### Constructor Parameters

Although docstrings of magic methods and private methods will be ignored. You can still introduce the constructor parameters in class's doc string by using `:param:` and `:type:`

Example:
``` python
TODO: include code.
```

### Remarks

`.. remarks::` is not a directive supported by Sphinx or RST, but only supported by our tool.

Example:
``` python
TODO: include code.
```

## Module

Module's docstring should be the very first line below magic comments. Even before the `import` statements.

For example:
``` ptyhon
TODO: include code.
```

## Package

Packages' docstrings are contained in `__init__.py`. They should obey the same rule as module docstrings.

Example:
``` python
TODO: include code.
```

## Methods/Functions

`:param:`, `:type:`, `:raises:`, `:returns:` and `:rtype:` are used to document a function or method.

There are two kinkds of ways to describe function parameters and their type:

``` python
TODO: include code.
```

Content of `:returns:` shows what is the return value.

`:raises:`, `:type:`, `:rtype:` will create cross references if possible. Contents of `:type:` and `:rtype:` can only be class name or type name. `:raises:` may contain both type name and description. For example:

``` python
TODO: include code.
```

<!-- ## Images -->
## External Links

External links can be written in two formats in RST: inline link and seperate link. Read more [here](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#external-links).

But note that our tool only support inline external link format currently. As an example:

``` python
TODO: include code.
```

## List

Two kinds of RST list formats are fully supported in our tool. Read more about [Bullet Lists](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#bullet-lists) and [Enumerated Lists](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#enumerated-lists)

## Math

You are able to create a formula using Latex math format with the help of `.. math::` directive in docstring.

Example:
``` python
TODO: include code.
```

<!-- ## Table -->
## Include

If you want to include contents from another file, `.. literalinclude::` would be helpful. Further more, you can include certain lines of the files. See more details [here](http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude).

## Example

If you would like to show an example of how to use your API, use `.. amonition::` directive and include "Example" in the content.

Example:
``` python
TODO: include code.
```

NOTE: If you are using Google or Numpy style docstring formating, just using the keyword "Example" will be fine.

## Code

To show a code block, use `.. code-block::` directive. Note that there should be an empty line between the directive and code content, as shown in below:

``` python
TODO: include code.
```

<!-- ## Note -->
<!-- ## Warning -->
## See Also

`.. seealso::` creates a bolck of content showing readers more information.

Example:
``` python
```

NOTE: `See Also` in Numpy-style docstring can only contains class name or type name.

Example:
``` python
```

<!-- ## Literal Block -->
## Cross Reference

When you would like to insert a cross reference in your docstring, following markups will be helpful:

1. `:func:`: Referencing a function.
2. `:meth:`: Referencing a class method.
3. `:class:`: Referencing a class.
4. `:mod:`: Referencing a module or a package.
5. `:any:`: Referencing anything.

All contents of these markups should be the full name of objects. It means you have to use the physical path of a class even if you created a short alias by importing it in `__init__.py`.

Example:
``` rst
:func:`package.module.class`
```

# Google/Numpy Style Docstring

You are free to write your docstrings in these two kinds of styles. Examples are show [here](http://www.sphinx-doc.org/en/master/usage/extensions/example_numpy.html?highlight=numpy).

Although you are able to mix content in these two styles together with RST format contents, it is not recommended by us avoiding potential conflictions.

## Supported Fields

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

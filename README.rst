Sphinx DocFX YAML
=================

.. image:: https://travis-ci.org/ericholscher/sphinx-docfx-yaml.svg?branch=master
   :target: https://travis-ci.org/ericholscher/sphinx-docfx-yaml

.. image:: https://ci.appveyor.com/api/projects/status/m9t5a331de14mwfi/branch/master?svg=true
   :target: https://ci.appveyor.com/project/ericholscher/sphinx-docfx-yaml

.. warning:: This is a pre-release version. Some or all features might not work yet.

Sphinx DocFX YAML is an exporter for the Sphinx Python domain into `DocFX YAML <https://dotnet.github.io/docfx/spec/metadata_format_spec.html>`_. 

Contents
--------

.. toctree::
   :glob:
   :maxdepth: 2

   design
   api

Basic Workflow
--------------

* Write RST that includes the Python domain (either manually or with autodoc)
* Render internal doctree into YAML
* Output YAML into output directory

Install
-------

First you need to install docfx-yaml:

.. code:: bash

    pip install sphinx-docfx-yaml

Then add it to your Sphinx project's ``conf.py``:

.. code:: python

    extensions = ['docfx-yaml.extension']

    # Document Python Code
    docfx_yaml_output = 'path/for/output/files'

This is needed because we will be outputting rst files into the ``docfx-yaml``
directory.  

Modes
-----

There are two output modes that specify the structure of the YAML files.
The first is ``module`` which means that the YAML files will be output in files coresponding to the name of their module.
The second modes is ``rst`` which outputs them in the same structure as the RST files they were defined in.

Design
------

Read more about the deisgn in our :doc:`design`.


# coding: utf-8
# Used for testing pkg_resources-style namespace package.
# See more: https://packaging.python.org/guides/packaging-namespace-packages/#pkg-resources-style-namespace-packages

__import__('pkg_resources').declare_namespace(__name__)

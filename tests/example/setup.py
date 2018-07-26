from setuptools import setup, find_packages

setup(
    name='example',
    version='0.1',
    author='Yiding Tian',
    author_email='yitian@microsoft.com',
    url='https://github.com/docascode/sphinx-docfx-yaml/tree/master/tests/example',
    description='Test Package for sphinx-docfx-yaml',
    package_dir={'': '.'},
    packages=find_packages('.', exclude=['doc']),
    include_package_data=True
)

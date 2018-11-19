import codecs
from setuptools import setup, find_packages
extra_setup = dict(
install_requires=[
    'PyYAML',
    'wheel>=0.24.0',
    'sphinx==1.5.5',
    'unidecode',
],
setup_requires=['pytest-runner'],
tests_require=['pytest', 'mock'],
)

setup(
    name='sphinx-docfx-yaml',
    version='1.2.63',
    author='Eric Holscher',
    author_email='eric@ericholscher.com',
    url='https://github.com/ericholscher/sphinx-docfx-yaml',
    description='Sphinx Python Domain to DocFX YAML Generator',
    package_dir={'': '.'},
    packages=find_packages('.', exclude=['tests']),
    long_description=codecs.open("README.rst", "r", "utf-8").read(),
    # trying to add files...
    include_package_data=True,
    **extra_setup
)

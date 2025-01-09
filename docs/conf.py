# Configuration file for the Sphinx documentation builder.
# All configuration has been moved from this file into the pyproject.toml file for
# convenience.

from sphinx_pyproject import SphinxConfig

config = SphinxConfig("../pyproject.toml", globalns=globals())

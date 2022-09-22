# Configuration file for the Sphinx documentation builder

import os
import textwrap
import furiosa

# -- Project information -----------------------------------------------------

project = 'furiosa'
copyright = '2022, Ellen M. Price'
author = '@emprice'

# The full version, including alpha/beta/rc tags
release = furiosa.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings
extensions = ['furiosa', 'sphinx.ext.todo', 'sphinx.ext.mathjax',
              'sphinx.ext.autodoc']
todo_include_todos = True

smartquotes = True
primary_domain = 'py'
highlight_language = 'default'

#html_logo = '_static/logo.svg'
html_title = 'furiosa'

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'furiosa'
pygments_style = 'nordlight'
pygments_dark_style = 'norddark'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory
html_static_path = ['_static']
#html_favicon = 'favicon.ico'

# vim: set ft=python:

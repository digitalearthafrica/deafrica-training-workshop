# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import ytsphinx.youtube
ytsphinx.setup = ytsphinx.youtube.setup

# -- Project information -----------------------------------------------------

project = 'Digital Earth Africa Training'
copyright = '2020, Digital Earth Africa'
author = 'Digital Earth Africa'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# The document name of the “master” document, that is, the document that contains
# the root toctree directive. Default is 'index'.
# Changed in version 2.0: The default is changed to 'index' from 'contents'.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme",
    "ytsphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    'logo_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/logo.png'

html_favicon = '_static/favicon.jpg'

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# Don't execute notebooks
nbsphinx_execute = 'never'

# Use table-wrapping style
html_context = {
    'css_files': [
        '_static/theme_override.css',  # override wide tables in RTD theme
        ],
     }


# Translation options
gettext_uuid = True
gettext_compact = False

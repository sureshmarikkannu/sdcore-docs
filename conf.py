# SPDX-FileCopyrightText: 2021 Open Networking Foundation <info@opennetworking.org>
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os

def get_version():
    with open("VERSION") as f:
        return f.read().strip()

# -- Project information -----------------------------------------------------

project = u'SD-Core Docs'
copyright = u'2021-current, Open Networking Foundation'
author = u'Open Networking Foundation'

# The short X.Y version
version = get_version()

# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# make all warnings errors
warning_is_error = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinxcontrib.spelling',
    "sphinx_multiversion",
]

# require document prefix on section labels
autosectionlabel_prefix_document = True

# Text files with lists of words that shouldn't fail the spellchecker:
spelling_word_list_filename=['dict.txt', ]

# sphinx-multiversion prep, run in each versioned source directory
prep_commands = [
]

# include only the branches matching master and aether-*
smv_branch_whitelist = r'^(master|sdcore-.*)$'

# Don't include any tags - smv docs say you can put None here, but that is broken
# https://github.com/Holzhaus/sphinx-multiversion/issues/47
smv_tag_whitelist = r'notags'

# include all remote branches
smv_remote_whitelist = r'^.*$'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
        '*/LICENSE.md',
        '*/vendor',
        '.DS_Store',
        'README',
        'Thumbs.db',
        '_build',
        'requirements.txt',
        'venv-docs',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_logo = '_static/sdcore.svg'

html_favicon = '_static/sdcore-favicon-128.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'logo_only': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SD-CoreDocs'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'SD-CoreDocs.tex', u'SD-Core Docs',
     u'ONF', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'SD-Core Docs', u'SD-Core Docs',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'SD-Core Docs', u'SD-Core Docs',
     author, 'SD-CoreDocs', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# blockdiag/etc. config

rackdiag_antialias = True
rackdiag_html_image_format = "SVG"
rackdiag_fontpath = [
    "_static/fonts/Inconsolata-Regular.ttf",
    "_static/fonts/Inconsolata-Bold.ttf",
]

nwdiag_antialias = True
nwdiag_html_image_format = "SVG"
nwdiag_fontpath = [
    "_static/fonts/Inconsolata-Regular.ttf",
    "_static/fonts/Inconsolata-Bold.ttf",
]

# -- Options for todo extension ----------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for linkcheck ---------------------------------------------------
# The link checker strips off .md from links and then complains
linkcheck_ignore = [
    r'https://jenkins.aetherproject.org/.*',
    r'https://gerrit.opencord.org/.*',
]

linkcheck_timeout = 3
linkcheck_retries = 2

# -- options for Intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
    'aether': ('https://docs.aetherproject.org/master', None),
    'onf': ('https://docs.opennetworking.org/', None),
    'sysapproach5g': ('https://5g.systemsapproach.org/', None),
    'sysapproachnet': ('https://book.systemsapproach.org/', None),
    'sysapproachsdn': ('https://sdn.systemsapproach.org/', None),
    }

def setup(app):

    app.add_css_file('css/rtd_theme_mods.css')

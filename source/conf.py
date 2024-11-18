
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'matter-handbook'
copyright = '2024, Matter Contributors'
author = 'Matter Contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for MyST --------------------------------------------------------
myst_heading_anchors = 6

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']
html_logo = "_static/images/logo.png"
html_favicon = "_static/images/favicon.ico"

html_theme_options = {
    "repository_url": "https://github.com/project-chip/matter-handbook",
    "use_repository_button": True,
}

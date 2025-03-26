# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GADemo Documentation'
html_title = "GADemo Documentation"
html_short_title = "GADemo Documentation"

copyright = '2025, Paloma L Sett'
author = 'Paloma L Sett'
release = '0.11.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser",
              "sphinx_design", 
              "sphinxcontrib.bibtex"]

bibtex_bibfiles = ['references/references.bib']

myst_enable_extensions = [
    "colon_fence",  # Habilita ::: para grids e cards
    "html_admonition",
    "html_image",
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "attrs_inline",
    "attrs_block",
]


source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

html_logo = "_static/icon.png"
html_favicon = "_static/favicon.ico"



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_static_path = ['_static']
html_css_files = ['style.css']


locale_dirs = ['locale/']
gettext_compact = False

html_theme_options = {
    "logo": {
        "text": "GADemo Documentation",
        "image_light": "icon.png",
        "image_dark": "icon.png",
    },
    "navbar_start": ["navbar-logo"],
    "use_edit_page_button": True,
    "navigation_depth": 3,
    "show_prev_next": True,
    "navbar_end": ["icon-links", "theme-switcher", "version-switcher"],
    "switcher": {
        "json_url": "_static/switcher.json",
        "version_match": "0.11.2"
    },
    "icon_links": [
        {
            "name": "Backend Repository",
            "url": "https://github.com/palomaflsette/GAdemo-api",
            "icon": "fab fa-github",
            "type": "fontawesome"
        },
        {
            "name": "Frontend Repository",
            "url": "https://github.com/palomaflsette/gademo-front",
            "icon": "fab fa-github",
            "type": "fontawesome"
        }
    ]
}


html_context = {
    "github_user": "palomaflsette",        
    "github_repo": "gademo-docs",     
    "github_version": "main",    
    "doc_path": "source",      
}

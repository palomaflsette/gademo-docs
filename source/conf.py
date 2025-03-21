# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GAdemo Documentation'
html_title = "GAdemo Documentation"
html_short_title = "GAdemo Documentation"

copyright = '2025, Paloma L Sett'
author = 'Paloma L Sett'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser",
              "sphinx_design"]

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



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_static_path = ['_static']

locale_dirs = ['locale/']
gettext_compact = False

html_theme_options = {
    "use_edit_page_button": True,
    "navigation_depth": 3,  # Define a profundidade da navegação lateral
    "show_prev_next": True,  # Adiciona botões "Próximo" e "Anterior"
    # Permite troca de temas e versões
    "navbar_end": ["theme-switcher", "version-switcher"],
    "switcher": {
        "json_url": "_static/switcher.json",  # Caminho para o arquivo de idiomas
        "version_match": "1.0.0"
    },
}

html_context = {
    "github_user": "palomaflsette",        
    "github_repo": "gademo-docs",     
    "github_version": "main",    
    "doc_path": "source",      
}

# ==================================================================================================
# Sphinx Configuration for {{ package_name }}
#
# Uses MyST-Parser for Markdown support alongside reStructuredText.
#
# See Also
# --------
# - Sphinx: https://www.sphinx-doc.org/
# - MyST-Parser: https://myst-parser.readthedocs.io/
# ==================================================================================================

project = "{{ package_name }}"
author = "{{ author_name }}"
copyright = "2025, {{ author_name }}"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "_templates"]

# --- HTML Output ---------------------------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

# --- MyST-Parser Configuration ------------------------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# --- Napoleon (Docstring Style) ------------------------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True

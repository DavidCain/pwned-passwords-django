"""
Configuration file for the Sphinx documentation builder:

https://www.sphinx-doc.org/

"""
import sys

extensions = [
    "notfound.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxext.opengraph",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "pwned-passwords-django"
copyright = "2018, James Bennett"
version = "1.7"
release = "1.7a1"
exclude_trees = ["_build"]
pygments_style = "sphinx"
htmlhelp_basename = "pwned-passwords-djangodoc"
html_theme = "furo"
latex_documents = [
    (
        "index",
        "pwned-passwords-django.tex",
        "pwned-passwords-django Documentation",
        "James Bennett",
        "manual",
    )
]

intersphinx_mapping = {
    "django": (
        "https://docs.djangoproject.com/en/stable/",
        "https://docs.djangoproject.com/en/stable/_objects/",
    ),
    "python": ("https://docs.python.org/3", None),
}

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if "spelling" in sys.argv:
    extensions.append("sphinxcontrib.spelling")

# Spelling language.
spelling_lang = "en_US"

# Location of word list.
spelling_word_list_filename = "spelling_wordlist.txt"

# OGP metadata configuration.
ogp_enable_meta_description = True
ogp_site_url = "https://pwned-passwords-django.readthedocs.io/"

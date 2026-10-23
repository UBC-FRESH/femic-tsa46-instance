"""Sphinx configuration for FEMIC Great Bear Rainforest North TSA 46 Instance."""

import sys
from pathlib import Path

project = "FEMIC Great Bear Rainforest North TSA 46 Instance"
author = "UBC-FRESH"
copyright = "2026, UBC-FRESH"

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

extensions: list[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_member_order = "bysource"
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_use_param = True
napoleon_use_rtype = False

html_theme = "sphinx_rtd_theme"
html_title = "FEMIC GBR North TSA 46 Instance"
html_extra_path = ["llms.txt"]

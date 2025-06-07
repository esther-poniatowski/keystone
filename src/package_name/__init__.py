"""
Package: `{{ package_name }}`

File: `__init__.py`

Package initialization:
-
- Exposes the main module and version information.

Modules
-------
module_name:
    Example module with minimal functionality.
"""
from importlib.metadata import version

__version__ = version(__package__)
__author__ = "{{ author_name }}"
__email__ = "{{ email }}"

__all__ = []

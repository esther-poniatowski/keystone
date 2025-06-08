"""
Command-line entry point for the `{{ package_name }}` package.

Usage
-----
To invoke the package::

    python -m {{ package_name }}


See Also
--------
{{ package_name }}.cli: Command-line interface module for the package.
"""
from .cli import app

app()

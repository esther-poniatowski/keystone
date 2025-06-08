"""
Entry point for the `{{ package_name }}` package, invoked as a module.

Usage
-----
To launch the command-line interface, execute::

    python -m {{ package_name }}


See Also
--------
{{ package_name }}.cli: Module implementing the application's command-line interface.
"""
from .cli import app

app()

"""
Initialization logic and public interface for the `{{ package_name }}` package.

Variables
---------
__version__ : str, default "0.0.0+unknown"
    Version of the package. If the package metadata is unavailable (e.g. in editable or source-only
    environments), a fallback value is provided (PEP 440 compliant).
__all__ : list
    Public objects exposed by this package.

Functions
---------
info() -> str
    Format diagnostic information about the package and platform.

Examples
--------
To programmatically retrieve the package version:

    >>> import {{ package_name }}
    >>> {{ package_name }}.__version__
    '0.1.0'

See Also
--------
importlib.metadata.version
    Function to retrieve the version of a package.
PackageNotFoundError
    Exception raised when the package is not found in the environment.
"""
from importlib.metadata import version, PackageNotFoundError
import platform

try:
    if __package__ is None: # erroneous script execution
        raise PackageNotFoundError
    __version__ = version(__package__)
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__all__ = ["info", "__version__"]


def info() -> str:
    """Format diagnostic information on package and platform."""
    return f"{__package__} {__version__} | Platform: {platform.system()} Python {platform.python_version()}"

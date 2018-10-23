"""Push countries to ratify UN treaties"""
import pathlib
import string

# Version of UN Treaties
__version__ = "0.1.2"

# Use importlib.resources
try:
    from importlib import resources  # >= 3.7
except ImportError:
    import importlib_resources as resources  # noqa


def get_local_path(file_name):
    """Get a path to a local file"""
    safe_chars = string.ascii_letters + string.digits + "_."
    safe_name = "".join(l if l in safe_chars else "-" for l in file_name)
    local_dir = pathlib.Path.home() / f".{__name__}"
    local_dir.mkdir(exist_ok=True)

    return local_dir / safe_name

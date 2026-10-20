from pathlib import Path


def get_project_root():
    """Return the root directory of the project."""
    return Path(__file__).resolve().parent.parent


def get_data_directory():
    """Return the directory where datasets will be stored."""
    return get_project_root() / "data"

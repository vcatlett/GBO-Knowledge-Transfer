"""Top-level package for AstrID"""

from pathlib import Path

__version__ = "25.1.0"

all = ["AstrIDVersion"]


def AstrIDVersion():
    """
    Version of the AstrID code

    Returns
    -------
    v : str
        The current version of AstrID
    """
    v = __version__
    return v


def get_path_root():
    """
    Root of the AstrID repository

    Returns
    -------
    path_root : str
        The path to the root of this repository
    """
    path_root = Path(__file__).parent.parent.parent
    return path_root

from pathlib import Path


def get_path_static():
    """
    Returns the absolute path to astrid/gui/static/

    Returns
    -------
    static_path : `pathlib.Path`
        The path to astrid/gui/static/
    """
    static_path = Path(__file__).parent
    return static_path

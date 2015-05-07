from pystrap.http_util import page_exists


PYPI_URL = 'https://pypi.python.org/pypi'


def is_pypi_name_available(name, page_exists_fn=page_exists):
    """
    Returns True if the package with the given name does not already exist in
    the Python Package Index (PyPI).

    For example, the "pystrap" package is in use (you're using it!):
    >>> is_pypi_name_available('pystrap')
    False

    But a pseudo-random package name is (overwhelmingly likely) not in use:
    >>> import uuid
    >>> is_pypi_name_available(uuid.uuid4().hex)
    True
    """
    return not page_exists_fn('/'.join((PYPI_URL, name)))

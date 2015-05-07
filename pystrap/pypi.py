import requests


def is_pypi_name_available(name):
    r = requests.head(
        'https://pypi.python.org/pypi/{n}'.format(n=name),
        allow_redirects=True)
    return r.status_code != requests.codes.ok  # pylint: disable=no-member

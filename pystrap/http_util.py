import requests


def page_exists(url):
    """
    Returns True if a 200 response is returned from the given URL, otherwise
    returns False.

    For example, we know the page for this project exists:
    >>> page_exists('https://github.com/themattrix/python-pystrap')
    True

    We also know that the page for a fake project does not exist:
    >>> page_exists('https://github.com/themattrix/fake-project')
    False
    """
    r = requests.head(url, allow_redirects=True)
    return r.status_code == requests.codes.ok  # pylint: disable=no-member

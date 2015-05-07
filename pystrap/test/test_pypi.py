from mock import call, Mock
from nose.tools import eq_
from pystrap import pypi


def test_is_pypi_name_available_url():
    mock_page_exists = Mock()

    pypi.is_pypi_name_available(
        name='test_package',
        page_exists_fn=mock_page_exists)

    eq_(mock_page_exists.mock_calls, [
        call('https://pypi.python.org/pypi/test_package')])

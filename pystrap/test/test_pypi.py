from nose.tools import eq_
from pystrap import pypi
from uuid import uuid4


def test_real_pypi_name_not_available():
    eq_(pypi.is_pypi_name_available('pystrap'), False)


def test_real_pypi_name_available():
    eq_(pypi.is_pypi_name_available(uuid4().hex), True)

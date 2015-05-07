# pylint: disable=no-member
#         Disabled because responses exposes many members dynamically.

import responses
from collections import namedtuple
from nose.tools import eq_
from pystrap import http_util


def test_page_exists_scenarios():
    t = namedtuple('test_scenario', ('status_code', 'expected_result'))

    def generate_scenarios():
        yield t(200, True)
        for code in range(201, 208):
            yield t(code, False)
        yield t(404, False)

    @responses.activate
    def assert_page_exists_scenario(scenario):
        responses.add(responses.HEAD, __TEST_URL, status=scenario.status_code)
        exists = http_util.page_exists(url=__TEST_URL)
        eq_(len(responses.calls), 1)
        eq_(responses.calls[0].request.url, __TEST_URL)
        eq_(exists, scenario.expected_result)

    for s in generate_scenarios():
        yield assert_page_exists_scenario, s


# This test is disabled until the next version of responses is released.
# The next version should support redirection.
#
# @responses.activate
# def test_page_exists_after_redirect():
#     responses.add(
#         responses.HEAD,
#         __TEST_URL,
#         status=302,
#         adding_headers={'location': '/real', 'content-length': '0'})
#
#     responses.add(
#         responses.HEAD,
#         __TEST_URL + 'real/',
#         status=200)
#
#     exists = http_util.page_exists(url=__TEST_URL)
#
#     eq_(len(responses.calls), 2)
#     eq_([c.response.status_code for c in responses.calls], [302, 200])
#     eq_(exists, True)


#
# Test Helpers
#

__TEST_URL = 'https://test.com/'  # responses wants the trailing slash

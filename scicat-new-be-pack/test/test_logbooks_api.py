# coding: utf-8

"""
    Dacat API

    SciCat backend API  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import scicat_new_be_pack
from scicat_new_be_pack.api.logbooks_api import LogbooksApi  # noqa: E501
from scicat_new_be_pack.rest import ApiException


class TestLogbooksApi(unittest.TestCase):
    """LogbooksApi unit test stubs"""

    def setUp(self):
        self.api = scicat_new_be_pack.api.logbooks_api.LogbooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_logbooks_controller_find_all(self):
        """Test case for logbooks_controller_find_all

        """
        pass

    def test_logbooks_controller_find_by_name(self):
        """Test case for logbooks_controller_find_by_name

        """
        pass


if __name__ == '__main__':
    unittest.main()

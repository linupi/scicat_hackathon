# coding: utf-8

"""
    Dacat API

    SciCat backend API  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import scicat_fake_openapi
from scicat_fake_openapi.api.auth_api import AuthApi  # noqa: E501
from scicat_fake_openapi.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = scicat_fake_openapi.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auth_controller_ad_login(self):
        """Test case for auth_controller_ad_login

        """
        pass

    def test_auth_controller_login(self):
        """Test case for auth_controller_login

        """
        pass

    def test_auth_controller_whoami(self):
        """Test case for auth_controller_whoami

        """
        pass


if __name__ == '__main__':
    unittest.main()

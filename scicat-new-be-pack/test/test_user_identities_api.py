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
from scicat_new_be_pack.api.user_identities_api import UserIdentitiesApi  # noqa: E501
from scicat_new_be_pack.rest import ApiException


class TestUserIdentitiesApi(unittest.TestCase):
    """UserIdentitiesApi unit test stubs"""

    def setUp(self):
        self.api = scicat_new_be_pack.api.user_identities_api.UserIdentitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_identities_controller_find_one(self):
        """Test case for user_identities_controller_find_one

        """
        pass


if __name__ == '__main__':
    unittest.main()

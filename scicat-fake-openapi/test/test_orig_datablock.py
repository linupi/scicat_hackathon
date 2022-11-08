# coding: utf-8

"""
    Dacat API

    SciCat backend API  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import scicat_fake_openapi
from scicat_fake_openapi.models.orig_datablock import OrigDatablock  # noqa: E501
from scicat_fake_openapi.rest import ApiException

class TestOrigDatablock(unittest.TestCase):
    """OrigDatablock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrigDatablock
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = scicat_fake_openapi.models.orig_datablock.OrigDatablock()  # noqa: E501
        if include_optional :
            return OrigDatablock(
                owner_group = '0', 
                access_groups = [
                    '0'
                    ], 
                instrument_group = '0', 
                created_by = '0', 
                updated_by = '0', 
                id = '0', 
                dataset_id = '0', 
                size = 1.337, 
                data_file_list = [
                    '0'
                    ]
            )
        else :
            return OrigDatablock(
                owner_group = '0',
                access_groups = [
                    '0'
                    ],
                created_by = '0',
                updated_by = '0',
                id = '0',
                dataset_id = '0',
                size = 1.337,
                data_file_list = [
                    '0'
                    ],
        )

    def testOrigDatablock(self):
        """Test OrigDatablock"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

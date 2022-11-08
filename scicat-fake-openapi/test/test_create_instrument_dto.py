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
from scicat_fake_openapi.models.create_instrument_dto import CreateInstrumentDto  # noqa: E501
from scicat_fake_openapi.rest import ApiException

class TestCreateInstrumentDto(unittest.TestCase):
    """CreateInstrumentDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateInstrumentDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = scicat_fake_openapi.models.create_instrument_dto.CreateInstrumentDto()  # noqa: E501
        if include_optional :
            return CreateInstrumentDto(
                name = '0', 
                custom_metadata = None
            )
        else :
            return CreateInstrumentDto(
                name = '0',
        )

    def testCreateInstrumentDto(self):
        """Test CreateInstrumentDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

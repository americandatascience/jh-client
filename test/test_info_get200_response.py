# coding: utf-8

"""
    JupyterHub

    The REST API for JupyterHub

    The version of the OpenAPI document: 4.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from jh_client.models.info_get200_response import InfoGet200Response

class TestInfoGet200Response(unittest.TestCase):
    """InfoGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfoGet200Response:
        """Test InfoGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InfoGet200Response`
        """
        model = InfoGet200Response()
        if include_optional:
            return InfoGet200Response(
                version = '',
                python = '',
                sys_executable = '',
                authenticator = jh_client.models._info_get_200_response_authenticator._info_get_200_response_authenticator(
                    class = '', 
                    version = '', ),
                spawner = jh_client.models._info_get_200_response_spawner._info_get_200_response_spawner(
                    class = '', 
                    version = '', )
            )
        else:
            return InfoGet200Response(
        )
        """

    def testInfoGet200Response(self):
        """Test InfoGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

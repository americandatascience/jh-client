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

from jh_client.models.info_get200_response_spawner import InfoGet200ResponseSpawner

class TestInfoGet200ResponseSpawner(unittest.TestCase):
    """InfoGet200ResponseSpawner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfoGet200ResponseSpawner:
        """Test InfoGet200ResponseSpawner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InfoGet200ResponseSpawner`
        """
        model = InfoGet200ResponseSpawner()
        if include_optional:
            return InfoGet200ResponseSpawner(
                var_class = '',
                version = ''
            )
        else:
            return InfoGet200ResponseSpawner(
        )
        """

    def testInfoGet200ResponseSpawner(self):
        """Test InfoGet200ResponseSpawner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

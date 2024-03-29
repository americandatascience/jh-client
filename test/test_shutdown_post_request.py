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

from jh_client.models.shutdown_post_request import ShutdownPostRequest

class TestShutdownPostRequest(unittest.TestCase):
    """ShutdownPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShutdownPostRequest:
        """Test ShutdownPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShutdownPostRequest`
        """
        model = ShutdownPostRequest()
        if include_optional:
            return ShutdownPostRequest(
                proxy = True,
                servers = True
            )
        else:
            return ShutdownPostRequest(
        )
        """

    def testShutdownPostRequest(self):
        """Test ShutdownPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

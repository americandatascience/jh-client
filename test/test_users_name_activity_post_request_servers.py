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

from openapi_client.models.users_name_activity_post_request_servers import UsersNameActivityPostRequestServers

class TestUsersNameActivityPostRequestServers(unittest.TestCase):
    """UsersNameActivityPostRequestServers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersNameActivityPostRequestServers:
        """Test UsersNameActivityPostRequestServers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersNameActivityPostRequestServers`
        """
        model = UsersNameActivityPostRequestServers()
        if include_optional:
            return UsersNameActivityPostRequestServers(
                server_name = openapi_client.models._users__name__activity_post_request_servers__server_name_._users__name__activity_post_request_servers__server_name_(
                    last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return UsersNameActivityPostRequestServers(
        )
        """

    def testUsersNameActivityPostRequestServers(self):
        """Test UsersNameActivityPostRequestServers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

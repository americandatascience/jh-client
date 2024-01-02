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

from jh_client.models.user import User

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> User:
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = User()
        if include_optional:
            return User(
                name = '',
                admin = True,
                roles = [
                    ''
                    ],
                groups = [
                    ''
                    ],
                server = '',
                pending = 'spawn',
                last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                servers = {
                    'key' : jh_client.models.server.Server(
                        name = '', 
                        ready = True, 
                        stopped = True, 
                        pending = 'spawn', 
                        url = '', 
                        progress_url = '', 
                        started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        state = jh_client.models.state.state(), 
                        user_options = jh_client.models.user_options.user_options(), )
                    },
                auth_state = None
            )
        else:
            return User(
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

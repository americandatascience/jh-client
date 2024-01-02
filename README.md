# Jupyter Hub Python Client
An SDK and API-wrapper for the jupyter hub REST API. 

- API version: 4.0.2
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /hub/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/hub/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    cookie_name = 'cookie_name_example' # str | 
    cookie_value = 'cookie_value_example' # str | 

    try:
        # Identify a user from a cookie
        api_response = api_instance.authorizations_cookie_cookie_name_cookie_value_get(cookie_name, cookie_value)
        print("The response of DefaultApi->authorizations_cookie_cookie_name_cookie_value_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->authorizations_cookie_cookie_name_cookie_value_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */hub/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**authorizations_cookie_cookie_name_cookie_value_get**](docs/DefaultApi.md#authorizations_cookie_cookie_name_cookie_value_get) | **GET** /authorizations/cookie/{cookie_name}/{cookie_value} | Identify a user from a cookie
*DefaultApi* | [**authorizations_token_post**](docs/DefaultApi.md#authorizations_token_post) | **POST** /authorizations/token | Request a new API token
*DefaultApi* | [**authorizations_token_token_get**](docs/DefaultApi.md#authorizations_token_token_get) | **GET** /authorizations/token/{token} | Identify a user or service from an API token
*DefaultApi* | [**groups_get**](docs/DefaultApi.md#groups_get) | **GET** /groups | List groups
*DefaultApi* | [**groups_name_delete**](docs/DefaultApi.md#groups_name_delete) | **DELETE** /groups/{name} | Delete a group
*DefaultApi* | [**groups_name_get**](docs/DefaultApi.md#groups_name_get) | **GET** /groups/{name} | Get a group by name
*DefaultApi* | [**groups_name_post**](docs/DefaultApi.md#groups_name_post) | **POST** /groups/{name} | Create a group
*DefaultApi* | [**groups_name_properties_put**](docs/DefaultApi.md#groups_name_properties_put) | **PUT** /groups/{name}/properties | Set the group properties.  Added in JupyterHub 3.2. 
*DefaultApi* | [**groups_name_users_delete**](docs/DefaultApi.md#groups_name_users_delete) | **DELETE** /groups/{name}/users | Remove users from a group 
*DefaultApi* | [**groups_name_users_post**](docs/DefaultApi.md#groups_name_users_post) | **POST** /groups/{name}/users | Add users to a group
*DefaultApi* | [**info_get**](docs/DefaultApi.md#info_get) | **GET** /info | Get detailed info about JupyterHub
*DefaultApi* | [**oauth2_authorize_get**](docs/DefaultApi.md#oauth2_authorize_get) | **GET** /oauth2/authorize | OAuth 2.0 authorize endpoint
*DefaultApi* | [**oauth2_token_post**](docs/DefaultApi.md#oauth2_token_post) | **POST** /oauth2/token | Request an OAuth2 token
*DefaultApi* | [**proxy_get**](docs/DefaultApi.md#proxy_get) | **GET** /proxy | Get the proxy&#39;s routing table
*DefaultApi* | [**proxy_patch**](docs/DefaultApi.md#proxy_patch) | **PATCH** /proxy | Notify the Hub about a new proxy
*DefaultApi* | [**proxy_post**](docs/DefaultApi.md#proxy_post) | **POST** /proxy | Force the Hub to sync with the proxy
*DefaultApi* | [**root_get**](docs/DefaultApi.md#root_get) | **GET** / | Get JupyterHub version
*DefaultApi* | [**services_get**](docs/DefaultApi.md#services_get) | **GET** /services | List services
*DefaultApi* | [**services_name_get**](docs/DefaultApi.md#services_name_get) | **GET** /services/{name} | Get a service by name
*DefaultApi* | [**shutdown_post**](docs/DefaultApi.md#shutdown_post) | **POST** /shutdown | Shutdown the Hub
*DefaultApi* | [**user_get**](docs/DefaultApi.md#user_get) | **GET** /user | Return authenticated user&#39;s model
*DefaultApi* | [**users_get**](docs/DefaultApi.md#users_get) | **GET** /users | List users
*DefaultApi* | [**users_name_activity_post**](docs/DefaultApi.md#users_name_activity_post) | **POST** /users/{name}/activity | Notify Hub of activity for a given user.
*DefaultApi* | [**users_name_delete**](docs/DefaultApi.md#users_name_delete) | **DELETE** /users/{name} | Delete a user
*DefaultApi* | [**users_name_get**](docs/DefaultApi.md#users_name_get) | **GET** /users/{name} | Get a user by name
*DefaultApi* | [**users_name_patch**](docs/DefaultApi.md#users_name_patch) | **PATCH** /users/{name} | Modify a user
*DefaultApi* | [**users_name_post**](docs/DefaultApi.md#users_name_post) | **POST** /users/{name} | Create a single user
*DefaultApi* | [**users_name_server_delete**](docs/DefaultApi.md#users_name_server_delete) | **DELETE** /users/{name}/server | Stop a user&#39;s server
*DefaultApi* | [**users_name_server_post**](docs/DefaultApi.md#users_name_server_post) | **POST** /users/{name}/server | Start a user&#39;s single-user notebook server
*DefaultApi* | [**users_name_servers_server_name_delete**](docs/DefaultApi.md#users_name_servers_server_name_delete) | **DELETE** /users/{name}/servers/{server_name} | Stop a user&#39;s named server
*DefaultApi* | [**users_name_servers_server_name_post**](docs/DefaultApi.md#users_name_servers_server_name_post) | **POST** /users/{name}/servers/{server_name} | Start a user&#39;s single-user named-server notebook server
*DefaultApi* | [**users_name_tokens_get**](docs/DefaultApi.md#users_name_tokens_get) | **GET** /users/{name}/tokens | List tokens for the user
*DefaultApi* | [**users_name_tokens_post**](docs/DefaultApi.md#users_name_tokens_post) | **POST** /users/{name}/tokens | Create a new token for the user
*DefaultApi* | [**users_name_tokens_token_id_delete**](docs/DefaultApi.md#users_name_tokens_token_id_delete) | **DELETE** /users/{name}/tokens/{token_id} | Delete (revoke) a token by id
*DefaultApi* | [**users_name_tokens_token_id_get**](docs/DefaultApi.md#users_name_tokens_token_id_get) | **GET** /users/{name}/tokens/{token_id} | Get the model for a token by id
*DefaultApi* | [**users_post**](docs/DefaultApi.md#users_post) | **POST** /users | Create multiple users


## Documentation For Models

 - [AuthorizationsTokenPost200Response](docs/AuthorizationsTokenPost200Response.md)
 - [AuthorizationsTokenPostRequest](docs/AuthorizationsTokenPostRequest.md)
 - [Get200Response](docs/Get200Response.md)
 - [Group](docs/Group.md)
 - [GroupsNameUsersPostRequest](docs/GroupsNameUsersPostRequest.md)
 - [InfoGet200Response](docs/InfoGet200Response.md)
 - [InfoGet200ResponseAuthenticator](docs/InfoGet200ResponseAuthenticator.md)
 - [InfoGet200ResponseSpawner](docs/InfoGet200ResponseSpawner.md)
 - [Oauth2TokenPost200Response](docs/Oauth2TokenPost200Response.md)
 - [ProxyPatchRequest](docs/ProxyPatchRequest.md)
 - [RequestIdentity](docs/RequestIdentity.md)
 - [Server](docs/Server.md)
 - [Service](docs/Service.md)
 - [ShutdownPostRequest](docs/ShutdownPostRequest.md)
 - [Token](docs/Token.md)
 - [User](docs/User.md)
 - [UsersNameActivityPostRequest](docs/UsersNameActivityPostRequest.md)
 - [UsersNameActivityPostRequestServers](docs/UsersNameActivityPostRequestServers.md)
 - [UsersNameActivityPostRequestServersServerName](docs/UsersNameActivityPostRequestServersServerName.md)
 - [UsersNamePatchRequest](docs/UsersNamePatchRequest.md)
 - [UsersNameTokensPostRequest](docs/UsersNameTokensPostRequest.md)
 - [UsersPostRequest](docs/UsersPostRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="token"></a>
### token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="oauth2"></a>
### oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://hub.example/hub/api/oauth2/authorize
- **Scopes**: 
 - **(no_scope)**: Identify the owner of the requesting entity.
 - **self**: The user’s own resources _(metascope for users, resolves to (no_scope) for services)_
 - **inherit**: Everything that the token-owning entity can access _(metascope for tokens)_
 - **admin-ui**: Access the admin page. Permission to take actions via the admin page granted separately.
 - **admin:users**: Read, write, create and delete users and their authentication state, not including their servers or tokens.
 - **admin:auth_state**: Read a user’s authentication state.
 - **users**: Read and write permissions to user models (excluding servers, tokens and authentication state).
 - **delete:users**: Delete users.
 - **list:users**: List users, including at least their names.
 - **read:users**: Read user models (excluding including servers, tokens and authentication state).
 - **read:users:name**: Read names of users.
 - **read:users:groups**: Read users’ group membership.
 - **read:users:activity**: Read time of last user activity.
 - **read:roles**: Read role assignments.
 - **read:roles:users**: Read user role assignments.
 - **read:roles:services**: Read service role assignments.
 - **read:roles:groups**: Read group role assignments.
 - **users:activity**: Update time of last user activity.
 - **admin:servers**: Read, start, stop, create and delete user servers and their state.
 - **admin:server_state**: Read and write users’ server state.
 - **servers**: Start and stop user servers.
 - **read:servers**: Read users’ names and their server models (excluding the server state).
 - **delete:servers**: Stop and delete users' servers.
 - **tokens**: Read, write, create and delete user tokens.
 - **read:tokens**: Read user tokens.
 - **admin:groups**: Read and write group information, create and delete groups.
 - **groups**: Read and write group information, including adding/removing users to/from groups.
 - **list:groups**: List groups, including at least their names.
 - **read:groups**: Read group models.
 - **read:groups:name**: Read group names.
 - **delete:groups**: Delete groups.
 - **list:services**: List services, including at least their names.
 - **read:services**: Read service models.
 - **read:services:name**: Read service names.
 - **read:hub**: Read detailed information about the Hub.
 - **access:servers**: Access user servers via API or browser.
 - **access:services**: Access services via API or browser.
 - **proxy**: Read information about the proxy’s routing table, sync the Hub with the proxy and notify the Hub about a new proxy.
 - **shutdown**: Shutdown the hub.
 - **read:metrics**: Read prometheus metrics.





# openapi_client.DefaultApi

All URIs are relative to */hub/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizations_cookie_cookie_name_cookie_value_get**](DefaultApi.md#authorizations_cookie_cookie_name_cookie_value_get) | **GET** /authorizations/cookie/{cookie_name}/{cookie_value} | Identify a user from a cookie
[**authorizations_token_post**](DefaultApi.md#authorizations_token_post) | **POST** /authorizations/token | Request a new API token
[**authorizations_token_token_get**](DefaultApi.md#authorizations_token_token_get) | **GET** /authorizations/token/{token} | Identify a user or service from an API token
[**groups_get**](DefaultApi.md#groups_get) | **GET** /groups | List groups
[**groups_name_delete**](DefaultApi.md#groups_name_delete) | **DELETE** /groups/{name} | Delete a group
[**groups_name_get**](DefaultApi.md#groups_name_get) | **GET** /groups/{name} | Get a group by name
[**groups_name_post**](DefaultApi.md#groups_name_post) | **POST** /groups/{name} | Create a group
[**groups_name_properties_put**](DefaultApi.md#groups_name_properties_put) | **PUT** /groups/{name}/properties | Set the group properties.  Added in JupyterHub 3.2. 
[**groups_name_users_delete**](DefaultApi.md#groups_name_users_delete) | **DELETE** /groups/{name}/users | Remove users from a group 
[**groups_name_users_post**](DefaultApi.md#groups_name_users_post) | **POST** /groups/{name}/users | Add users to a group
[**info_get**](DefaultApi.md#info_get) | **GET** /info | Get detailed info about JupyterHub
[**oauth2_authorize_get**](DefaultApi.md#oauth2_authorize_get) | **GET** /oauth2/authorize | OAuth 2.0 authorize endpoint
[**oauth2_token_post**](DefaultApi.md#oauth2_token_post) | **POST** /oauth2/token | Request an OAuth2 token
[**proxy_get**](DefaultApi.md#proxy_get) | **GET** /proxy | Get the proxy&#39;s routing table
[**proxy_patch**](DefaultApi.md#proxy_patch) | **PATCH** /proxy | Notify the Hub about a new proxy
[**proxy_post**](DefaultApi.md#proxy_post) | **POST** /proxy | Force the Hub to sync with the proxy
[**root_get**](DefaultApi.md#root_get) | **GET** / | Get JupyterHub version
[**services_get**](DefaultApi.md#services_get) | **GET** /services | List services
[**services_name_get**](DefaultApi.md#services_name_get) | **GET** /services/{name} | Get a service by name
[**shutdown_post**](DefaultApi.md#shutdown_post) | **POST** /shutdown | Shutdown the Hub
[**user_get**](DefaultApi.md#user_get) | **GET** /user | Return authenticated user&#39;s model
[**users_get**](DefaultApi.md#users_get) | **GET** /users | List users
[**users_name_activity_post**](DefaultApi.md#users_name_activity_post) | **POST** /users/{name}/activity | Notify Hub of activity for a given user.
[**users_name_delete**](DefaultApi.md#users_name_delete) | **DELETE** /users/{name} | Delete a user
[**users_name_get**](DefaultApi.md#users_name_get) | **GET** /users/{name} | Get a user by name
[**users_name_patch**](DefaultApi.md#users_name_patch) | **PATCH** /users/{name} | Modify a user
[**users_name_post**](DefaultApi.md#users_name_post) | **POST** /users/{name} | Create a single user
[**users_name_server_delete**](DefaultApi.md#users_name_server_delete) | **DELETE** /users/{name}/server | Stop a user&#39;s server
[**users_name_server_post**](DefaultApi.md#users_name_server_post) | **POST** /users/{name}/server | Start a user&#39;s single-user notebook server
[**users_name_servers_server_name_delete**](DefaultApi.md#users_name_servers_server_name_delete) | **DELETE** /users/{name}/servers/{server_name} | Stop a user&#39;s named server
[**users_name_servers_server_name_post**](DefaultApi.md#users_name_servers_server_name_post) | **POST** /users/{name}/servers/{server_name} | Start a user&#39;s single-user named-server notebook server
[**users_name_tokens_get**](DefaultApi.md#users_name_tokens_get) | **GET** /users/{name}/tokens | List tokens for the user
[**users_name_tokens_post**](DefaultApi.md#users_name_tokens_post) | **POST** /users/{name}/tokens | Create a new token for the user
[**users_name_tokens_token_id_delete**](DefaultApi.md#users_name_tokens_token_id_delete) | **DELETE** /users/{name}/tokens/{token_id} | Delete (revoke) a token by id
[**users_name_tokens_token_id_get**](DefaultApi.md#users_name_tokens_token_id_get) | **GET** /users/{name}/tokens/{token_id} | Get the model for a token by id
[**users_post**](DefaultApi.md#users_post) | **POST** /users | Create multiple users


# **authorizations_cookie_cookie_name_cookie_value_get**
> User authorizations_cookie_cookie_name_cookie_value_get(cookie_name, cookie_value)

Identify a user from a cookie

Used by single-user notebook servers to hand off cookie authentication to the Hub

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (token):

```python
import time
import os
import openapi_client
from openapi_client.models.user import User
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
    except Exception as e:
        print("Exception when calling DefaultApi->authorizations_cookie_cookie_name_cookie_value_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cookie_name** | **str**|  | 
 **cookie_value** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user identified by the cookie |  -  |
**404** | A user is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorizations_token_post**
> AuthorizationsTokenPost200Response authorizations_token_post(credentials=credentials)

Request a new API token

Request a new API token to use with the JupyterHub REST API. If not already authenticated, username and password can be sent in the JSON request body. Logging in via this method is only available when the active Authenticator accepts passwords (e.g. not OAuth). 

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.authorizations_token_post200_response import AuthorizationsTokenPost200Response
from openapi_client.models.authorizations_token_post_request import AuthorizationsTokenPostRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    credentials = openapi_client.AuthorizationsTokenPostRequest() # AuthorizationsTokenPostRequest |  (optional)

    try:
        # Request a new API token
        api_response = api_instance.authorizations_token_post(credentials=credentials)
        print("The response of DefaultApi->authorizations_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authorizations_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**AuthorizationsTokenPostRequest**](AuthorizationsTokenPostRequest.md)|  | [optional] 

### Return type

[**AuthorizationsTokenPost200Response**](AuthorizationsTokenPost200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new API token |  -  |
**403** | The user can not be authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorizations_token_token_get**
> authorizations_token_token_get(token)

Identify a user or service from an API token

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    token = 'token_example' # str | 

    try:
        # Identify a user or service from an API token
        api_instance.authorizations_token_token_get(token)
    except Exception as e:
        print("Exception when calling DefaultApi->authorizations_token_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user or service identified by the API token |  -  |
**404** | A user or service is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get**
> List[Group] groups_get(offset=offset, limit=limit)

List groups

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.group import Group
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    offset = 3.4 # float | Return a number of groups starting at the specified offset. Can be used with limit to paginate. If unspecified, return all groups.  (optional)
    limit = 3.4 # float | Return a finite number of groups. Can be used with offset to paginate. If unspecified, use api_page_default_limit.  (optional)

    try:
        # List groups
        api_response = api_instance.groups_get(offset=offset, limit=limit)
        print("The response of DefaultApi->groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| Return a number of groups starting at the specified offset. Can be used with limit to paginate. If unspecified, return all groups.  | [optional] 
 **limit** | **float**| Return a finite number of groups. Can be used with offset to paginate. If unspecified, use api_page_default_limit.  | [optional] 

### Return type

[**List[Group]**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_name_delete**
> groups_name_delete(name)

Delete a group

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | group name

    try:
        # Delete a group
        api_instance.groups_name_delete(name)
    except Exception as e:
        print("Exception when calling DefaultApi->groups_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| group name | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The group has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_name_get**
> Group groups_name_get(name)

Get a group by name

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.group import Group
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | group name

    try:
        # Get a group by name
        api_response = api_instance.groups_name_get(name)
        print("The response of DefaultApi->groups_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->groups_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| group name | 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_name_post**
> Group groups_name_post(name)

Create a group

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.group import Group
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | group name

    try:
        # Create a group
        api_response = api_instance.groups_name_post(name)
        print("The response of DefaultApi->groups_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->groups_name_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| group name | 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The group has been created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_name_properties_put**
> Group groups_name_properties_put(name, body)

Set the group properties.  Added in JupyterHub 3.2. 

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.group import Group
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | group name
    body = None # object | The new group properties, as a JSON dict.

    try:
        # Set the group properties.  Added in JupyterHub 3.2. 
        api_response = api_instance.groups_name_properties_put(name, body)
        print("The response of DefaultApi->groups_name_properties_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->groups_name_properties_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| group name | 
 **body** | **object**| The new group properties, as a JSON dict. | 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties have been updated. The updated group model is returned.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_name_users_delete**
> groups_name_users_delete(name)

Remove users from a group 

Body should be a JSON dictionary where `users` is a list of usernames to remove from the groups.  ```json {   \"users\": [\"name1\", \"name2\"] } ``` 

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | group name

    try:
        # Remove users from a group 
        api_instance.groups_name_users_delete(name)
    except Exception as e:
        print("Exception when calling DefaultApi->groups_name_users_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| group name | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The users have been removed from the group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_name_users_post**
> Group groups_name_users_post(name, body)

Add users to a group

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.group import Group
from openapi_client.models.groups_name_users_post_request import GroupsNameUsersPostRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | group name
    body = openapi_client.GroupsNameUsersPostRequest() # GroupsNameUsersPostRequest | The users to add to the group

    try:
        # Add users to a group
        api_response = api_instance.groups_name_users_post(name, body)
        print("The response of DefaultApi->groups_name_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->groups_name_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| group name | 
 **body** | [**GroupsNameUsersPostRequest**](GroupsNameUsersPostRequest.md)| The users to add to the group | 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The users have been added to the group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_get**
> InfoGet200Response info_get()

Get detailed info about JupyterHub

Detailed JupyterHub information, including Python version, JupyterHub's version and executable path, and which Authenticator and Spawner are active. 

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.info_get200_response import InfoGet200Response
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get detailed info about JupyterHub
        api_response = api_instance.info_get()
        print("The response of DefaultApi->info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InfoGet200Response**](InfoGet200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed JupyterHub info |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_authorize_get**
> oauth2_authorize_get(client_id, response_type, redirect_uri, state=state)

OAuth 2.0 authorize endpoint

Redirect users to this URL to begin the OAuth process. It is not an API endpoint. 

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (token):

```python
import time
import os
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
    client_id = 'client_id_example' # str | The client id
    response_type = 'response_type_example' # str | The response type (always 'code')
    redirect_uri = 'redirect_uri_example' # str | The redirect url
    state = 'state_example' # str | A state string (optional)

    try:
        # OAuth 2.0 authorize endpoint
        api_instance.oauth2_authorize_get(client_id, response_type, redirect_uri, state=state)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth2_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client id | 
 **response_type** | **str**| The response type (always &#39;code&#39;) | 
 **redirect_uri** | **str**| The redirect url | 
 **state** | **str**| A state string | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | OAuth2Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_token_post**
> Oauth2TokenPost200Response oauth2_token_post(client_id, client_secret, grant_type, code, redirect_uri)

Request an OAuth2 token

Request an OAuth2 token from an authorization code. This request completes the OAuth process. 

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (token):

```python
import time
import os
import openapi_client
from openapi_client.models.oauth2_token_post200_response import Oauth2TokenPost200Response
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
    client_id = 'client_id_example' # str | The client id
    client_secret = 'client_secret_example' # str | The client secret
    grant_type = 'grant_type_example' # str | The grant type (always 'authorization_code')
    code = 'code_example' # str | The code provided by the authorization redirect
    redirect_uri = 'redirect_uri_example' # str | The redirect url

    try:
        # Request an OAuth2 token
        api_response = api_instance.oauth2_token_post(client_id, client_secret, grant_type, code, redirect_uri)
        print("The response of DefaultApi->oauth2_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth2_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client id | 
 **client_secret** | **str**| The client secret | 
 **grant_type** | **str**| The grant type (always &#39;authorization_code&#39;) | 
 **code** | **str**| The code provided by the authorization redirect | 
 **redirect_uri** | **str**| The redirect url | 

### Return type

[**Oauth2TokenPost200Response**](Oauth2TokenPost200Response.md)

### Authorization

[oauth2](../README.md#oauth2), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON response including the token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_get**
> object proxy_get(offset=offset, limit=limit)

Get the proxy's routing table

A convenience alias for getting the routing table directly from the proxy

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    offset = 3.4 # float | Return a number of routes starting at the given offset. Can be used with limit to paginate. If unspecified, return all routes.  (optional)
    limit = 3.4 # float | Return a finite number of routes. Can be used with offset to paginate. If unspecified, use api_page_default_limit  (optional)

    try:
        # Get the proxy's routing table
        api_response = api_instance.proxy_get(offset=offset, limit=limit)
        print("The response of DefaultApi->proxy_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->proxy_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| Return a number of routes starting at the given offset. Can be used with limit to paginate. If unspecified, return all routes.  | [optional] 
 **limit** | **float**| Return a finite number of routes. Can be used with offset to paginate. If unspecified, use api_page_default_limit  | [optional] 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Routing table |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_patch**
> proxy_patch(body)

Notify the Hub about a new proxy

Notifies the Hub of a new proxy to use.

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.proxy_patch_request import ProxyPatchRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    body = openapi_client.ProxyPatchRequest() # ProxyPatchRequest | Any values that have changed for the new proxy. All keys are optional.

    try:
        # Notify the Hub about a new proxy
        api_instance.proxy_patch(body)
    except Exception as e:
        print("Exception when calling DefaultApi->proxy_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProxyPatchRequest**](ProxyPatchRequest.md)| Any values that have changed for the new proxy. All keys are optional. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_post**
> proxy_post()

Force the Hub to sync with the proxy

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Force the Hub to sync with the proxy
        api_instance.proxy_post()
    except Exception as e:
        print("Exception when calling DefaultApi->proxy_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> Get200Response root_get()

Get JupyterHub version

This endpoint is not authenticated for the purpose of clients and user to identify the JupyterHub version before setting up authentication. 

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (token):

```python
import time
import os
import openapi_client
from openapi_client.models.get200_response import Get200Response
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

    try:
        # Get JupyterHub version
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Get200Response**](Get200Response.md)

### Authorization

[oauth2](../README.md#oauth2), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JupyterHub version |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_get**
> List[Service] services_get()

List services

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # List services
        api_response = api_instance.services_get()
        print("The response of DefaultApi->services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->services_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Service]**](Service.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The service list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_name_get**
> Service services_name_get(name)

Get a service by name

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | service name

    try:
        # Get a service by name
        api_response = api_instance.services_name_get(name)
        print("The response of DefaultApi->services_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->services_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| service name | 

### Return type

[**Service**](Service.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Service model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_post**
> shutdown_post(body=body)

Shutdown the Hub

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.shutdown_post_request import ShutdownPostRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    body = openapi_client.ShutdownPostRequest() # ShutdownPostRequest |  (optional)

    try:
        # Shutdown the Hub
        api_instance.shutdown_post(body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->shutdown_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShutdownPostRequest**](ShutdownPostRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Shutdown successful |  -  |
**400** | Unexpeced value for proxy or servers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> RequestIdentity user_get()

Return authenticated user's model

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.request_identity import RequestIdentity
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Return authenticated user's model
        api_response = api_instance.user_get()
        print("The response of DefaultApi->user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RequestIdentity**](RequestIdentity.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authenticated user or service&#39;s model is returned with additional information about the permissions associated with the request token.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> List[User] users_get(state=state, offset=offset, limit=limit, include_stopped_servers=include_stopped_servers)

List users

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.user import User
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    state = 'state_example' # str | Return only users who have servers in the given state. If unspecified, return all users.  active: all users with any active servers (ready OR pending) ready: all users who have any ready servers (running, not pending) inactive: all users who have *no* active servers (complement of active)  Added in JupyterHub 1.3  (optional)
    offset = 3.4 # float | Return a number users starting at the given offset. Can be used with limit to paginate. If unspecified, return all users.  (optional)
    limit = 3.4 # float | Return a finite number of users. Can be used with offset to paginate. If unspecified, use api_page_default_limit.  (optional)
    include_stopped_servers = True # bool | Include stopped servers in user model(s). Added in JupyterHub 3.0. Allows retrieval of information about stopped servers, such as activity and state fields.  (optional)

    try:
        # List users
        api_response = api_instance.users_get(state=state, offset=offset, limit=limit, include_stopped_servers=include_stopped_servers)
        print("The response of DefaultApi->users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Return only users who have servers in the given state. If unspecified, return all users.  active: all users with any active servers (ready OR pending) ready: all users who have any ready servers (running, not pending) inactive: all users who have *no* active servers (complement of active)  Added in JupyterHub 1.3  | [optional] 
 **offset** | **float**| Return a number users starting at the given offset. Can be used with limit to paginate. If unspecified, return all users.  | [optional] 
 **limit** | **float**| Return a finite number of users. Can be used with offset to paginate. If unspecified, use api_page_default_limit.  | [optional] 
 **include_stopped_servers** | **bool**| Include stopped servers in user model(s). Added in JupyterHub 3.0. Allows retrieval of information about stopped servers, such as activity and state fields.  | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Hub&#39;s user list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_activity_post**
> users_name_activity_post(name, body=body)

Notify Hub of activity for a given user.

Notify the Hub of activity by the user, e.g. accessing a service or (more likely) actively using a server.

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.users_name_activity_post_request import UsersNameActivityPostRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username
    body = openapi_client.UsersNameActivityPostRequest() # UsersNameActivityPostRequest |  (optional)

    try:
        # Notify Hub of activity for a given user.
        api_instance.users_name_activity_post(name, body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_activity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 
 **body** | [**UsersNameActivityPostRequest**](UsersNameActivityPostRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication/Authorization error |  -  |
**404** | No such user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_delete**
> users_name_delete(name)

Delete a user

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username

    try:
        # Delete a user
        api_instance.users_name_delete(name)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The user has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_get**
> User users_name_get(name)

Get a user by name

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.user import User
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username

    try:
        # Get a user by name
        api_response = api_instance.users_name_get(name)
        print("The response of DefaultApi->users_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The User model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_patch**
> User users_name_patch(name, body)

Modify a user

Change a user's name or admin status

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.user import User
from openapi_client.models.users_name_patch_request import UsersNamePatchRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username
    body = openapi_client.UsersNamePatchRequest() # UsersNamePatchRequest | Updated user info. At least one key to be updated (name or admin) is required.

    try:
        # Modify a user
        api_response = api_instance.users_name_patch(name, body)
        print("The response of DefaultApi->users_name_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 
 **body** | [**UsersNamePatchRequest**](UsersNamePatchRequest.md)| Updated user info. At least one key to be updated (name or admin) is required. | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated user info |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_post**
> User users_name_post(name)

Create a single user

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.user import User
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username

    try:
        # Create a single user
        api_response = api_instance.users_name_post(name)
        print("The response of DefaultApi->users_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The user has been created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_server_delete**
> users_name_server_delete(name)

Stop a user's server

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username

    try:
        # Stop a user's server
        api_instance.users_name_server_delete(name)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_server_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The user&#39;s notebook server has not yet stopped as it is taking a while to stop |  -  |
**204** | The user&#39;s notebook server has stopped |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_server_post**
> users_name_server_post(name, options=options)

Start a user's single-user notebook server

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username
    options = None # object | Spawn options can be passed as a JSON body when spawning via the API instead of spawn form. The structure of the options will depend on the Spawner's configuration. The body itself will be available as `user_options` for the Spawner.  (optional)

    try:
        # Start a user's single-user notebook server
        api_instance.users_name_server_post(name, options=options)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_server_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 
 **options** | **object**| Spawn options can be passed as a JSON body when spawning via the API instead of spawn form. The structure of the options will depend on the Spawner&#39;s configuration. The body itself will be available as &#x60;user_options&#x60; for the Spawner.  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The user&#39;s notebook server has started |  -  |
**202** | The user&#39;s notebook server has not yet started, but has been requested |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_servers_server_name_delete**
> users_name_servers_server_name_delete(name, server_name)

Stop a user's named server

To remove the named server in addition to deleting it, the body may be a JSON dictionary with a boolean `remove` field:  ```json {\"remove\": true} ``` 

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username
    server_name = 'server_name_example' # str | name given to a named-server

    try:
        # Stop a user's named server
        api_instance.users_name_servers_server_name_delete(name, server_name)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_servers_server_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 
 **server_name** | **str**| name given to a named-server | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The user&#39;s notebook named-server has not yet stopped as it is taking a while to stop |  -  |
**204** | The user&#39;s notebook named-server has stopped |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_servers_server_name_post**
> users_name_servers_server_name_post(name, server_name, options=options)

Start a user's single-user named-server notebook server

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username
    server_name = 'server_name_example' # str | name given to a named-server.  Note that depending on your JupyterHub infrastructure there are chracterter size limitation to `server_name`. Default spawner with K8s pod will not allow Jupyter Notebooks to be spawned with a name that contains more than 253 characters (keep in mind that the pod will be spawned with extra characters to identify the user and hub). 
    options = None # object | Spawn options can be passed as a JSON body when spawning via the API instead of spawn form. The structure of the options will depend on the Spawner's configuration.  (optional)

    try:
        # Start a user's single-user named-server notebook server
        api_instance.users_name_servers_server_name_post(name, server_name, options=options)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_servers_server_name_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 
 **server_name** | **str**| name given to a named-server.  Note that depending on your JupyterHub infrastructure there are chracterter size limitation to &#x60;server_name&#x60;. Default spawner with K8s pod will not allow Jupyter Notebooks to be spawned with a name that contains more than 253 characters (keep in mind that the pod will be spawned with extra characters to identify the user and hub).  | 
 **options** | **object**| Spawn options can be passed as a JSON body when spawning via the API instead of spawn form. The structure of the options will depend on the Spawner&#39;s configuration.  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The user&#39;s notebook named-server has started |  -  |
**202** | The user&#39;s notebook named-server has not yet started, but has been requested |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_tokens_get**
> List[Token] users_name_tokens_get(name)

List tokens for the user

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.token import Token
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username

    try:
        # List tokens for the user
        api_response = api_instance.users_name_tokens_get(name)
        print("The response of DefaultApi->users_name_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_tokens_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 

### Return type

[**List[Token]**](Token.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of tokens |  -  |
**401** | Authentication/Authorization error |  -  |
**404** | No such user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_tokens_post**
> Token users_name_tokens_post(name, token_params=token_params)

Create a new token for the user

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.token import Token
from openapi_client.models.users_name_tokens_post_request import UsersNameTokensPostRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username
    token_params = openapi_client.UsersNameTokensPostRequest() # UsersNameTokensPostRequest |  (optional)

    try:
        # Create a new token for the user
        api_response = api_instance.users_name_tokens_post(name, token_params=token_params)
        print("The response of DefaultApi->users_name_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 
 **token_params** | [**UsersNameTokensPostRequest**](UsersNameTokensPostRequest.md)|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created token |  -  |
**400** | Body must be a JSON dict or empty |  -  |
**403** | Requested role does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_tokens_token_id_delete**
> users_name_tokens_token_id_delete(name, token_id)

Delete (revoke) a token by id

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username
    token_id = 'token_id_example' # str | 

    try:
        # Delete (revoke) a token by id
        api_instance.users_name_tokens_token_id_delete(name, token_id)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_tokens_token_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 
 **token_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The token has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_name_tokens_token_id_get**
> Token users_name_tokens_token_id_get(name, token_id)

Get the model for a token by id

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.token import Token
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    name = 'name_example' # str | username
    token_id = 'token_id_example' # str | 

    try:
        # Get the model for a token by id
        api_response = api_instance.users_name_tokens_token_id_get(name, token_id)
        print("The response of DefaultApi->users_name_tokens_token_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_name_tokens_token_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| username | 
 **token_id** | **str**|  | 

### Return type

[**Token**](Token.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The info for the new token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> List[User] users_post(body)

Create multiple users

### Example

* OAuth Authentication (oauth2):

```python
import time
import os
import openapi_client
from openapi_client.models.user import User
from openapi_client.models.users_post_request import UsersPostRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    body = openapi_client.UsersPostRequest() # UsersPostRequest | 

    try:
        # Create multiple users
        api_response = api_instance.users_post(body)
        print("The response of DefaultApi->users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersPostRequest**](UsersPostRequest.md)|  | 

### Return type

[**List[User]**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The users have been created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


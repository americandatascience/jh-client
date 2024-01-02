# UsersNameActivityPostRequestServers

Register activity for specific servers by name. The keys of this dict are the names of servers. The default server has an empty name (''). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_name** | [**UsersNameActivityPostRequestServersServerName**](UsersNameActivityPostRequestServersServerName.md) |  | [optional] 

## Example

```python
from openapi_client.models.users_name_activity_post_request_servers import UsersNameActivityPostRequestServers

# TODO update the JSON string below
json = "{}"
# create an instance of UsersNameActivityPostRequestServers from a JSON string
users_name_activity_post_request_servers_instance = UsersNameActivityPostRequestServers.from_json(json)
# print the JSON string representation of the object
print UsersNameActivityPostRequestServers.to_json()

# convert the object into a dict
users_name_activity_post_request_servers_dict = users_name_activity_post_request_servers_instance.to_dict()
# create an instance of UsersNameActivityPostRequestServers from a dict
users_name_activity_post_request_servers_form_dict = users_name_activity_post_request_servers.from_dict(users_name_activity_post_request_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UsersNameActivityPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_activity** | **datetime** | Timestamp of last-seen activity for this user. Only needed if this is not activity associated with using a given server.  | [optional] 
**servers** | [**UsersNameActivityPostRequestServers**](UsersNameActivityPostRequestServers.md) |  | [optional] 

## Example

```python
from openapi_client.models.users_name_activity_post_request import UsersNameActivityPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersNameActivityPostRequest from a JSON string
users_name_activity_post_request_instance = UsersNameActivityPostRequest.from_json(json)
# print the JSON string representation of the object
print UsersNameActivityPostRequest.to_json()

# convert the object into a dict
users_name_activity_post_request_dict = users_name_activity_post_request_instance.to_dict()
# create an instance of UsersNameActivityPostRequest from a dict
users_name_activity_post_request_form_dict = users_name_activity_post_request.from_dict(users_name_activity_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



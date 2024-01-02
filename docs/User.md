# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user&#39;s name | [optional] 
**admin** | **bool** | Whether the user is an admin | [optional] 
**roles** | **List[str]** | The names of roles this user has | [optional] 
**groups** | **List[str]** | The names of groups where this user is a member | [optional] 
**server** | **str** | The user&#39;s notebook server&#39;s base URL, if running; null if not. | [optional] 
**pending** | **str** | The currently pending action, if any | [optional] 
**last_activity** | **datetime** | Timestamp of last-seen activity from the user | [optional] 
**servers** | [**Dict[str, Server]**](Server.md) | The servers for this user. By default: only includes _active_ servers. Changed in 3.0: if &#x60;?include_stopped_servers&#x60; parameter is specified, stopped servers will be included as well.  | [optional] 
**auth_state** | **object** | Authentication state of the user. Only available with admin:users:auth_state scope. None otherwise.  | [optional] 

## Example

```python
from jh_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



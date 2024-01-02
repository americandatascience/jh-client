# GroupsNameUsersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | List of usernames to add to the group | [optional] 

## Example

```python
from jh_client.models.groups_name_users_post_request import GroupsNameUsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsNameUsersPostRequest from a JSON string
groups_name_users_post_request_instance = GroupsNameUsersPostRequest.from_json(json)
# print the JSON string representation of the object
print GroupsNameUsersPostRequest.to_json()

# convert the object into a dict
groups_name_users_post_request_dict = groups_name_users_post_request_instance.to_dict()
# create an instance of GroupsNameUsersPostRequest from a dict
groups_name_users_post_request_form_dict = groups_name_users_post_request.from_dict(groups_name_users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



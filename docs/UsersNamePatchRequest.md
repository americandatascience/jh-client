# UsersNamePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the new name (optional, if another key is updated i.e. admin) | [optional] 
**admin** | **bool** | update admin (optional, if another key is updated i.e. name) | [optional] 

## Example

```python
from openapi_client.models.users_name_patch_request import UsersNamePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersNamePatchRequest from a JSON string
users_name_patch_request_instance = UsersNamePatchRequest.from_json(json)
# print the JSON string representation of the object
print UsersNamePatchRequest.to_json()

# convert the object into a dict
users_name_patch_request_dict = users_name_patch_request_instance.to_dict()
# create an instance of UsersNamePatchRequest from a dict
users_name_patch_request_form_dict = users_name_patch_request.from_dict(users_name_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



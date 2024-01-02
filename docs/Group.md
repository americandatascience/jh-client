# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The group&#39;s name | [optional] 
**users** | **List[str]** | The names of users who are members of this group | [optional] 
**properties** | **object** | Group properties (a dictionary).  Unused by JupyterHub itself, but an extension point to store information about groups.  Added in JupyterHub 3.2.  | [optional] 
**roles** | **List[str]** | The names of roles this group has | [optional] 

## Example

```python
from openapi_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print Group.to_json()

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_form_dict = group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



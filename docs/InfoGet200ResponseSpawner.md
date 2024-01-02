# InfoGet200ResponseSpawner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** | The Python class currently active for spawning single-user notebook servers | [optional] 
**version** | **str** | The version of the currently active Spawner | [optional] 

## Example

```python
from openapi_client.models.info_get200_response_spawner import InfoGet200ResponseSpawner

# TODO update the JSON string below
json = "{}"
# create an instance of InfoGet200ResponseSpawner from a JSON string
info_get200_response_spawner_instance = InfoGet200ResponseSpawner.from_json(json)
# print the JSON string representation of the object
print InfoGet200ResponseSpawner.to_json()

# convert the object into a dict
info_get200_response_spawner_dict = info_get200_response_spawner_instance.to_dict()
# create an instance of InfoGet200ResponseSpawner from a dict
info_get200_response_spawner_form_dict = info_get200_response_spawner.from_dict(info_get200_response_spawner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# InfoGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of JupyterHub itself | [optional] 
**python** | **str** | The Python version, as returned by sys.version | [optional] 
**sys_executable** | **str** | The path to sys.executable running JupyterHub | [optional] 
**authenticator** | [**InfoGet200ResponseAuthenticator**](InfoGet200ResponseAuthenticator.md) |  | [optional] 
**spawner** | [**InfoGet200ResponseSpawner**](InfoGet200ResponseSpawner.md) |  | [optional] 

## Example

```python
from openapi_client.models.info_get200_response import InfoGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InfoGet200Response from a JSON string
info_get200_response_instance = InfoGet200Response.from_json(json)
# print the JSON string representation of the object
print InfoGet200Response.to_json()

# convert the object into a dict
info_get200_response_dict = info_get200_response_instance.to_dict()
# create an instance of InfoGet200Response from a dict
info_get200_response_form_dict = info_get200_response.from_dict(info_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



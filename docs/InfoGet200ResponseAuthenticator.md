# InfoGet200ResponseAuthenticator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** | The Python class currently active for JupyterHub Authentication | [optional] 
**version** | **str** | The version of the currently active Authenticator | [optional] 

## Example

```python
from jh_client.models.info_get200_response_authenticator import InfoGet200ResponseAuthenticator

# TODO update the JSON string below
json = "{}"
# create an instance of InfoGet200ResponseAuthenticator from a JSON string
info_get200_response_authenticator_instance = InfoGet200ResponseAuthenticator.from_json(json)
# print the JSON string representation of the object
print InfoGet200ResponseAuthenticator.to_json()

# convert the object into a dict
info_get200_response_authenticator_dict = info_get200_response_authenticator_instance.to_dict()
# create an instance of InfoGet200ResponseAuthenticator from a dict
info_get200_response_authenticator_form_dict = info_get200_response_authenticator.from_dict(info_get200_response_authenticator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



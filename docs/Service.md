# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The service&#39;s name | [optional] 
**admin** | **bool** | Whether the service is an admin | [optional] 
**roles** | **List[str]** | The names of roles this service has | [optional] 
**url** | **str** | The internal url where the service is running | [optional] 
**prefix** | **str** | The proxied URL prefix to the service&#39;s url | [optional] 
**pid** | **float** | The PID of the service process (if managed) | [optional] 
**command** | **List[str]** | The command used to start the service (if managed) | [optional] 
**info** | **object** | Additional information a deployment can attach to a service. JupyterHub does not use this field.  | [optional] 

## Example

```python
from jh_client.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print Service.to_json()

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_form_dict = service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



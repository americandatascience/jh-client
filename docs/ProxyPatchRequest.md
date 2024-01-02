# ProxyPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address of the new proxy | [optional] 
**port** | **str** | Port of the new proxy | [optional] 
**protocol** | **str** | Protocol of new proxy, if changed | [optional] 
**auth_token** | **str** | CONFIGPROXY_AUTH_TOKEN for the new proxy | [optional] 

## Example

```python
from jh_client.models.proxy_patch_request import ProxyPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyPatchRequest from a JSON string
proxy_patch_request_instance = ProxyPatchRequest.from_json(json)
# print the JSON string representation of the object
print ProxyPatchRequest.to_json()

# convert the object into a dict
proxy_patch_request_dict = proxy_patch_request_instance.to_dict()
# create an instance of ProxyPatchRequest from a dict
proxy_patch_request_form_dict = proxy_patch_request.from_dict(proxy_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



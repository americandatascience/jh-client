# ShutdownPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy** | **bool** | Whether the proxy should be shutdown as well (default from Hub config) | [optional] 
**servers** | **bool** | Whether users&#39; notebook servers should be shutdown as well (default from Hub config) | [optional] 

## Example

```python
from openapi_client.models.shutdown_post_request import ShutdownPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShutdownPostRequest from a JSON string
shutdown_post_request_instance = ShutdownPostRequest.from_json(json)
# print the JSON string representation of the object
print ShutdownPostRequest.to_json()

# convert the object into a dict
shutdown_post_request_dict = shutdown_post_request_instance.to_dict()
# create an instance of ShutdownPostRequest from a dict
shutdown_post_request_form_dict = shutdown_post_request.from_dict(shutdown_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



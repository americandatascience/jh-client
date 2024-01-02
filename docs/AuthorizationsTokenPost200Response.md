# AuthorizationsTokenPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The new API token. | [optional] 

## Example

```python
from openapi_client.models.authorizations_token_post200_response import AuthorizationsTokenPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationsTokenPost200Response from a JSON string
authorizations_token_post200_response_instance = AuthorizationsTokenPost200Response.from_json(json)
# print the JSON string representation of the object
print AuthorizationsTokenPost200Response.to_json()

# convert the object into a dict
authorizations_token_post200_response_dict = authorizations_token_post200_response_instance.to_dict()
# create an instance of AuthorizationsTokenPost200Response from a dict
authorizations_token_post200_response_form_dict = authorizations_token_post200_response.from_dict(authorizations_token_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



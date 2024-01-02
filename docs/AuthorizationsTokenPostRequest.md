# AuthorizationsTokenPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from jh_client.models.authorizations_token_post_request import AuthorizationsTokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationsTokenPostRequest from a JSON string
authorizations_token_post_request_instance = AuthorizationsTokenPostRequest.from_json(json)
# print the JSON string representation of the object
print AuthorizationsTokenPostRequest.to_json()

# convert the object into a dict
authorizations_token_post_request_dict = authorizations_token_post_request_instance.to_dict()
# create an instance of AuthorizationsTokenPostRequest from a dict
authorizations_token_post_request_form_dict = authorizations_token_post_request.from_dict(authorizations_token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Oauth2TokenPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The new API token for the user | [optional] 
**token_type** | **str** | Will always be &#39;Bearer&#39; | [optional] 

## Example

```python
from jh_client.models.oauth2_token_post200_response import Oauth2TokenPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth2TokenPost200Response from a JSON string
oauth2_token_post200_response_instance = Oauth2TokenPost200Response.from_json(json)
# print the JSON string representation of the object
print Oauth2TokenPost200Response.to_json()

# convert the object into a dict
oauth2_token_post200_response_dict = oauth2_token_post200_response_instance.to_dict()
# create an instance of Oauth2TokenPost200Response from a dict
oauth2_token_post200_response_form_dict = oauth2_token_post200_response.from_dict(oauth2_token_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



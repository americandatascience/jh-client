# Token


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token itself. Only present in responses to requests for a new token. | [optional] 
**id** | **str** | The id of the API token. Used for modifying or deleting the token. | [optional] 
**user** | **str** | The user that owns a token (undefined if owned by a service) | [optional] 
**service** | **str** | The service that owns the token (undefined of owned by a user) | [optional] 
**roles** | **List[str]** | Deprecated in JupyterHub 3, always an empty list. Tokens have &#39;scopes&#39; starting from JupyterHub 3. | [optional] 
**scopes** | **List[str]** | List of scopes this token has been assigned. New in JupyterHub 3. In JupyterHub 2.x, tokens were assigned &#39;roles&#39; insead of scopes. | [optional] 
**note** | **str** | A note about the token, typically describing what it was created for. | [optional] 
**created** | **datetime** | Timestamp when this token was created | [optional] 
**expires_at** | **datetime** | Timestamp when this token expires. Null if there is no expiry. | [optional] 
**last_activity** | **datetime** | Timestamp of last-seen activity using this token. Can be null if token has never been used.  | [optional] 
**session_id** | **str** | The session id associated with the token, if any. Only used for tokens set during oauth flows.  Added in 2.0.  | [optional] 

## Example

```python
from openapi_client.models.token import Token

# TODO update the JSON string below
json = "{}"
# create an instance of Token from a JSON string
token_instance = Token.from_json(json)
# print the JSON string representation of the object
print Token.to_json()

# convert the object into a dict
token_dict = token_instance.to_dict()
# create an instance of Token from a dict
token_form_dict = token.from_dict(token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



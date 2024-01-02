# RequestIdentity

The model for the entity making the request. Extends User or Service model to add information about the specific credentials (e.g. session or token-authorised scopes). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The service&#39;s name | [optional] 
**admin** | **bool** | Whether the service is an admin | [optional] 
**roles** | **List[str]** | The names of roles this service has | [optional] 
**groups** | **List[str]** | The names of groups where this user is a member | [optional] 
**server** | **str** | The user&#39;s notebook server&#39;s base URL, if running; null if not. | [optional] 
**pending** | **str** | The currently pending action, if any | [optional] 
**last_activity** | **datetime** | Timestamp of last-seen activity from the user | [optional] 
**servers** | [**Dict[str, Server]**](Server.md) | The servers for this user. By default: only includes _active_ servers. Changed in 3.0: if &#x60;?include_stopped_servers&#x60; parameter is specified, stopped servers will be included as well.  | [optional] 
**auth_state** | **object** | Authentication state of the user. Only available with admin:users:auth_state scope. None otherwise.  | [optional] 
**url** | **str** | The internal url where the service is running | [optional] 
**prefix** | **str** | The proxied URL prefix to the service&#39;s url | [optional] 
**pid** | **float** | The PID of the service process (if managed) | [optional] 
**command** | **List[str]** | The command used to start the service (if managed) | [optional] 
**info** | **object** | Additional information a deployment can attach to a service. JupyterHub does not use this field.  | [optional] 
**session_id** | **str** | The session id associated with the request&#39;s OAuth token, if any. null, if the request token not associated with a session id.  Added in 2.0.  | [optional] 
**scopes** | **List[str]** | The list of all expanded scopes the request credentials have access to.  Added in 2.0.  | [optional] 

## Example

```python
from openapi_client.models.request_identity import RequestIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of RequestIdentity from a JSON string
request_identity_instance = RequestIdentity.from_json(json)
# print the JSON string representation of the object
print RequestIdentity.to_json()

# convert the object into a dict
request_identity_dict = request_identity_instance.to_dict()
# create an instance of RequestIdentity from a dict
request_identity_form_dict = request_identity.from_dict(request_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



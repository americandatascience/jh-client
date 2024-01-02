# Server


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The server&#39;s name. The user&#39;s default server has an empty name (&#39;&#39;) | [optional] 
**ready** | **bool** | Whether the server is ready for traffic. Will always be false when any transition is pending.  | [optional] 
**stopped** | **bool** | Whether the server is stopped. Added in JupyterHub 3.0, and only useful when using the &#x60;?include_stopped_servers&#x60; request parameter. Now that stopped servers may be included (since JupyterHub 3.0), this is the simplest way to select stopped servers. Always equivalent to &#x60;not (ready or pending)&#x60;.  | [optional] 
**pending** | **str** | The currently pending action, if any. A server is not ready if an action is pending.  | [optional] 
**url** | **str** | The URL where the server can be accessed (typically /user/:name/:server.name/).  | [optional] 
**progress_url** | **str** | The URL for an event-stream to retrieve events during a spawn.  | [optional] 
**started** | **datetime** | UTC timestamp when the server was last started. | [optional] 
**last_activity** | **datetime** | UTC timestamp last-seen activity on this server. | [optional] 
**state** | **object** | Arbitrary internal state from this server&#39;s spawner. Only available on the hub&#39;s users list or get-user-by-name method, and only with admin:users:server_state scope. None otherwise. | [optional] 
**user_options** | **object** | User specified options for the user&#39;s spawned instance of a single-user server. | [optional] 

## Example

```python
from openapi_client.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print Server.to_json()

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_form_dict = server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



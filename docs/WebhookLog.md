# WebhookLog

Log model for webhook invocations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**description** | **str** | Webhook description | 
**invoked_at** | **datetime** | The time the webhook was invoked | [optional] 
**status_code** | **int** | The HTTP status code returned by the webhook endpoint | 
**request_url** | **str** | The URL to which the webhook request was sent | 
**webhook_method** | **str** | The HTTP method used for the webhook request (e.g., POST, GET) | 
**successful** | **bool** | Whether the webhook invocation was successful (2xx status code) | 
**error_message** | **str** |  | [optional] 
**response_body** | **str** |  | [optional] 
**response_headers** | **Dict[str, object]** |  | [optional] 
**request_headers** | **Dict[str, object]** |  | [optional] 
**payload** | **Dict[str, object]** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**action_history_id** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.webhook_log import WebhookLog

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLog from a JSON string
webhook_log_instance = WebhookLog.from_json(json)
# print the JSON string representation of the object
print(WebhookLog.to_json())

# convert the object into a dict
webhook_log_dict = webhook_log_instance.to_dict()
# create an instance of WebhookLog from a dict
webhook_log_from_dict = WebhookLog.from_dict(webhook_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



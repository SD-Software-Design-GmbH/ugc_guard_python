# WebhookLogBase

Base model without any potentially big data fields.

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

## Example

```python
from ugc_guard_python.models.webhook_log_base import WebhookLogBase

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLogBase from a JSON string
webhook_log_base_instance = WebhookLogBase.from_json(json)
# print the JSON string representation of the object
print(WebhookLogBase.to_json())

# convert the object into a dict
webhook_log_base_dict = webhook_log_base_instance.to_dict()
# create an instance of WebhookLogBase from a dict
webhook_log_base_from_dict = WebhookLogBase.from_dict(webhook_log_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



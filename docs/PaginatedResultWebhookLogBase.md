# PaginatedResultWebhookLogBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[WebhookLogBase]**](WebhookLogBase.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_webhook_log_base import PaginatedResultWebhookLogBase

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultWebhookLogBase from a JSON string
paginated_result_webhook_log_base_instance = PaginatedResultWebhookLogBase.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultWebhookLogBase.to_json())

# convert the object into a dict
paginated_result_webhook_log_base_dict = paginated_result_webhook_log_base_instance.to_dict()
# create an instance of PaginatedResultWebhookLogBase from a dict
paginated_result_webhook_log_base_from_dict = PaginatedResultWebhookLogBase.from_dict(paginated_result_webhook_log_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



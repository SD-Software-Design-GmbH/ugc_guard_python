# MailLogWithInvoker

Pydantic model for MailLog with additional invoker information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**content** | **Dict[str, object]** |  | [optional] 
**log_type** | [**LogType**](LogType.md) | Type of the log entry (created, updated, deleted) | [optional] 
**invoker_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**email** | **str** |  | 
**successful** | **bool** |  | 
**error_message** | **str** |  | 
**hidden** | **bool** |  | 
**mail_invoker** | [**UserBase**](UserBase.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.mail_log_with_invoker import MailLogWithInvoker

# TODO update the JSON string below
json = "{}"
# create an instance of MailLogWithInvoker from a JSON string
mail_log_with_invoker_instance = MailLogWithInvoker.from_json(json)
# print the JSON string representation of the object
print(MailLogWithInvoker.to_json())

# convert the object into a dict
mail_log_with_invoker_dict = mail_log_with_invoker_instance.to_dict()
# create an instance of MailLogWithInvoker from a dict
mail_log_with_invoker_from_dict = MailLogWithInvoker.from_dict(mail_log_with_invoker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



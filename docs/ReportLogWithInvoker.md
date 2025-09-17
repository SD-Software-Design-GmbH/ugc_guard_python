# ReportLogWithInvoker

Pydantic model for ReportLog with additional invoker information.

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
**report_id** | **str** |  | 
**report_invoker** | [**UserBase**](UserBase.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.report_log_with_invoker import ReportLogWithInvoker

# TODO update the JSON string below
json = "{}"
# create an instance of ReportLogWithInvoker from a JSON string
report_log_with_invoker_instance = ReportLogWithInvoker.from_json(json)
# print the JSON string representation of the object
print(ReportLogWithInvoker.to_json())

# convert the object into a dict
report_log_with_invoker_dict = report_log_with_invoker_instance.to_dict()
# create an instance of ReportLogWithInvoker from a dict
report_log_with_invoker_from_dict = ReportLogWithInvoker.from_dict(report_log_with_invoker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



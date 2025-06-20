# Report

A report is an incident reported by the reporter. The reporter things the resource reported is not allowed. E.g. the message was hateful, contains forbidden content, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**module_id** | **str** |  | 
**type_id** | **str** |  | 
**id** | **str** |  | [optional] 
**report_state** | [**ReportState**](ReportState.md) |  | [optional] 
**main_content_id** | **str** |  | 
**reported_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.report import Report

# TODO update the JSON string below
json = "{}"
# create an instance of Report from a JSON string
report_instance = Report.from_json(json)
# print the JSON string representation of the object
print(Report.to_json())

# convert the object into a dict
report_dict = report_instance.to_dict()
# create an instance of Report from a dict
report_from_dict = Report.from_dict(report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



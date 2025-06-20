# ReportDB

Extends the Report model to include the database only fields that shall not be reported to the user.

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
from ugc_guard_python.models.report_db import ReportDB

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDB from a JSON string
report_db_instance = ReportDB.from_json(json)
# print the JSON string representation of the object
print(ReportDB.to_json())

# convert the object into a dict
report_db_dict = report_db_instance.to_dict()
# create an instance of ReportDB from a dict
report_db_from_dict = ReportDB.from_dict(report_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



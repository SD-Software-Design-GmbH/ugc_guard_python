# ReportCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**module_id** | **str** |  | 
**type_id** | **str** |  | 

## Example

```python
from ugc_guard_python.models.report_create import ReportCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCreate from a JSON string
report_create_instance = ReportCreate.from_json(json)
# print the JSON string representation of the object
print(ReportCreate.to_json())

# convert the object into a dict
report_create_dict = report_create_instance.to_dict()
# create an instance of ReportCreate from a dict
report_create_from_dict = ReportCreate.from_dict(report_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



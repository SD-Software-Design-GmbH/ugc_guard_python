# ComparedModuleState

The stats now vs the stats before a certain date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**now** | [**ModuleStats**](ModuleStats.md) |  | 
**prior** | [**ModuleStats**](ModuleStats.md) |  | 
**prior_date** | **datetime** |  | 

## Example

```python
from ugc_guard_python.models.compared_module_state import ComparedModuleState

# TODO update the JSON string below
json = "{}"
# create an instance of ComparedModuleState from a JSON string
compared_module_state_instance = ComparedModuleState.from_json(json)
# print the JSON string representation of the object
print(ComparedModuleState.to_json())

# convert the object into a dict
compared_module_state_dict = compared_module_state_instance.to_dict()
# create an instance of ComparedModuleState from a dict
compared_module_state_from_dict = ComparedModuleState.from_dict(compared_module_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



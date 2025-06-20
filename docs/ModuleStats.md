# ModuleStats

Represents statistics for a module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **str** |  | 
**total_reports** | **int** |  | [optional] [default to 0]
**total_files** | **int** |  | [optional] [default to 0]
**total_reporters** | **int** |  | [optional] [default to 0]
**total_actions** | **int** |  | [optional] [default to 0]
**total_types** | **int** |  | [optional] [default to 0]
**total_open_reports** | **int** |  | [optional] [default to 0]

## Example

```python
from ugc_guard_python.models.module_stats import ModuleStats

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleStats from a JSON string
module_stats_instance = ModuleStats.from_json(json)
# print the JSON string representation of the object
print(ModuleStats.to_json())

# convert the object into a dict
module_stats_dict = module_stats_instance.to_dict()
# create an instance of ModuleStats from a dict
module_stats_from_dict = ModuleStats.from_dict(module_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



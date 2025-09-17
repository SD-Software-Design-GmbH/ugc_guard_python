# Guard

Base model for the guard feature.  Guards are used to check content against rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str** | Name of the guard, e.g., &#39;Content Guard&#39;, &#39;Report Guard&#39;, etc. | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** | Indicates whether the guard is currently enabled or disabled | [optional] [default to True]
**module_id** | **str** | ID of the module associated with this guard | [optional] 
**type_id** | **str** |  | [optional] 
**on_fail_action** | [**GuardOnFailAction**](GuardOnFailAction.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.guard import Guard

# TODO update the JSON string below
json = "{}"
# create an instance of Guard from a JSON string
guard_instance = Guard.from_json(json)
# print the JSON string representation of the object
print(Guard.to_json())

# convert the object into a dict
guard_dict = guard_instance.to_dict()
# create an instance of Guard from a dict
guard_from_dict = Guard.from_dict(guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



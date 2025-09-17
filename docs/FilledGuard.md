# FilledGuard

Model for a filled guard, which includes the guard and its options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guard** | [**Guard**](Guard.md) |  | 
**rules** | [**List[Rule]**](Rule.md) |  | [optional] 
**rule_connections** | [**List[GuardRuleConnection]**](GuardRuleConnection.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.filled_guard import FilledGuard

# TODO update the JSON string below
json = "{}"
# create an instance of FilledGuard from a JSON string
filled_guard_instance = FilledGuard.from_json(json)
# print the JSON string representation of the object
print(FilledGuard.to_json())

# convert the object into a dict
filled_guard_dict = filled_guard_instance.to_dict()
# create an instance of FilledGuard from a dict
filled_guard_from_dict = FilledGuard.from_dict(filled_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



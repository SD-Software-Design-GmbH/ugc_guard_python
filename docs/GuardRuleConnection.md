# GuardRuleConnection

Model for the connection between guards and rules.  This model is used to associate guards with specific rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guard_id** | **str** | ID of the guard | 
**rule_id** | **str** | ID of the rule | 
**running_order** | **int** | Order in which this report should be processed by the guard (lower numbers are processed first) | [optional] [default to 0]

## Example

```python
from ugc_guard_python.models.guard_rule_connection import GuardRuleConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GuardRuleConnection from a JSON string
guard_rule_connection_instance = GuardRuleConnection.from_json(json)
# print the JSON string representation of the object
print(GuardRuleConnection.to_json())

# convert the object into a dict
guard_rule_connection_dict = guard_rule_connection_instance.to_dict()
# create an instance of GuardRuleConnection from a dict
guard_rule_connection_from_dict = GuardRuleConnection.from_dict(guard_rule_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



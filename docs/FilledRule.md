# FilledRule

Model for a filled rule, which includes the rule and its options.  This model is used to represent a rule with its options filled in, either deterministic or non-deterministic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**Rule**](Rule.md) |  | 
**deterministic_options** | [**DeterministicRuleOptions**](DeterministicRuleOptions.md) |  | [optional] 
**non_deterministic_options** | [**NonDeterministicRuleOptions**](NonDeterministicRuleOptions.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.filled_rule import FilledRule

# TODO update the JSON string below
json = "{}"
# create an instance of FilledRule from a JSON string
filled_rule_instance = FilledRule.from_json(json)
# print the JSON string representation of the object
print(FilledRule.to_json())

# convert the object into a dict
filled_rule_dict = filled_rule_instance.to_dict()
# create an instance of FilledRule from a dict
filled_rule_from_dict = FilledRule.from_dict(filled_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



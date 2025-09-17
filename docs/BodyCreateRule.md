# BodyCreateRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**Rule**](Rule.md) |  | 
**deterministic_options** | [**DeterministicRuleOptions**](DeterministicRuleOptions.md) |  | [optional] 
**non_deterministic_options** | [**NonDeterministicRuleOptions**](NonDeterministicRuleOptions.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.body_create_rule import BodyCreateRule

# TODO update the JSON string below
json = "{}"
# create an instance of BodyCreateRule from a JSON string
body_create_rule_instance = BodyCreateRule.from_json(json)
# print the JSON string representation of the object
print(BodyCreateRule.to_json())

# convert the object into a dict
body_create_rule_dict = body_create_rule_instance.to_dict()
# create an instance of BodyCreateRule from a dict
body_create_rule_from_dict = BodyCreateRule.from_dict(body_create_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



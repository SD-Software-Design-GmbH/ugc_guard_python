# DeterministicRuleOptions

Options for deterministic rules, such as blacklists or whitelists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**words** | **List[str]** | List of words for the deterministic rule, e.g., blacklisted or whitelisted words | [optional] 
**is_blacklist** | **bool** | Indicates whether the rule is a blacklist (True) or a whitelist (False) | [optional] [default to True]
**threshold** | **int** |  | [optional] 
**validation_option** | [**DeterministicRuleValidationOptions**](DeterministicRuleValidationOptions.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.deterministic_rule_options import DeterministicRuleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DeterministicRuleOptions from a JSON string
deterministic_rule_options_instance = DeterministicRuleOptions.from_json(json)
# print the JSON string representation of the object
print(DeterministicRuleOptions.to_json())

# convert the object into a dict
deterministic_rule_options_dict = deterministic_rule_options_instance.to_dict()
# create an instance of DeterministicRuleOptions from a dict
deterministic_rule_options_from_dict = DeterministicRuleOptions.from_dict(deterministic_rule_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



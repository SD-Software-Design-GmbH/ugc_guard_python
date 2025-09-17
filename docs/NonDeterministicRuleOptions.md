# NonDeterministicRuleOptions

Options for non-deterministic rules, such as AI models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**prompt_template** | **str** | Template for the prompt used in the AI model, allowing dynamic content insertion | [optional] 

## Example

```python
from ugc_guard_python.models.non_deterministic_rule_options import NonDeterministicRuleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of NonDeterministicRuleOptions from a JSON string
non_deterministic_rule_options_instance = NonDeterministicRuleOptions.from_json(json)
# print the JSON string representation of the object
print(NonDeterministicRuleOptions.to_json())

# convert the object into a dict
non_deterministic_rule_options_dict = non_deterministic_rule_options_instance.to_dict()
# create an instance of NonDeterministicRuleOptions from a dict
non_deterministic_rule_options_from_dict = NonDeterministicRuleOptions.from_dict(non_deterministic_rule_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



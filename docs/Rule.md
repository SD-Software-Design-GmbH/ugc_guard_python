# Rule

Base model for a rule.  If a rule is non-deterministic, it will lead to an AIEvaluation object If a rule is deterministic, it will lead to a DeterministicEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **str** | Creation timestamp in ISO format | [optional] 
**updated_at** | **str** |  | [optional] 
**name** | **str** | Name of the rule, e.g., &#39;Spam Filter&#39;, &#39;Content Classifier&#39;, etc. | [optional] 
**description** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**is_deterministic** | **bool** | Indicates whether the rule is deterministic (e.g., black/whitelist) or non-deterministic (e.g., AI model) | [optional] [default to True]
**enabled** | **bool** | Indicates whether the rule is currently enabled or disabled | [optional] [default to True]
**deterministic_options_id** | **str** |  | [optional] 
**non_deterministic_options_id** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print(Rule.to_json())

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_from_dict = Rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



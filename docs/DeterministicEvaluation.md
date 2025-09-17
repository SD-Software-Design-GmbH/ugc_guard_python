# DeterministicEvaluation

Base model for deterministic rule evaluations.  This model is used to store the results of deterministic rule evaluations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**rule_id** | **str** | ID of the rule that was evaluated | [optional] 
**report_id** | **str** |  | [optional] 
**matched_words** | **List[str]** | List of words that matched the rule during evaluation. If blacklist is used, these are the words that triggered the rule. If whitelist is used, these are the words that did trigger the rule because they are not part of the whitelist | [optional] 
**is_match** | **bool** | Indicates whether the rule matched the content of the report | [optional] [default to False]

## Example

```python
from ugc_guard_python.models.deterministic_evaluation import DeterministicEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of DeterministicEvaluation from a JSON string
deterministic_evaluation_instance = DeterministicEvaluation.from_json(json)
# print the JSON string representation of the object
print(DeterministicEvaluation.to_json())

# convert the object into a dict
deterministic_evaluation_dict = deterministic_evaluation_instance.to_dict()
# create an instance of DeterministicEvaluation from a dict
deterministic_evaluation_from_dict = DeterministicEvaluation.from_dict(deterministic_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



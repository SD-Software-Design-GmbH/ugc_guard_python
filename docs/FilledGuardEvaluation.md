# FilledGuardEvaluation

Model for a filled guard evaluation, which includes the guard and its evaluations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guard_evaluation** | [**GuardEvaluation**](GuardEvaluation.md) |  | 
**ai_evaluations** | [**List[AIEvaluation]**](AIEvaluation.md) |  | [optional] 
**deterministic_evaluations** | [**List[DeterministicEvaluation]**](DeterministicEvaluation.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.filled_guard_evaluation import FilledGuardEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of FilledGuardEvaluation from a JSON string
filled_guard_evaluation_instance = FilledGuardEvaluation.from_json(json)
# print the JSON string representation of the object
print(FilledGuardEvaluation.to_json())

# convert the object into a dict
filled_guard_evaluation_dict = filled_guard_evaluation_instance.to_dict()
# create an instance of FilledGuardEvaluation from a dict
filled_guard_evaluation_from_dict = FilledGuardEvaluation.from_dict(filled_guard_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



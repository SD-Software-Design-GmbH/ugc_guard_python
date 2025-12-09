# GuardEvaluation

Model for the evaluation of guards.  This model is used to store the results of guard evaluations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**ongoing** | **bool** | Indicates whether the evaluation is still ongoing or has been completed | [optional] [default to True]
**passed** | **bool** |  | [optional] 
**failed** | **bool** | Indicates whether the guard evaluation failed. Null if ongoing. | [optional] [default to False]
**failure_reason** | **str** |  | [optional] 
**content_json** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**guard_id** | **str** | ID of the guard that was evaluated | 
**report_id** | **str** |  | 
**severity** | **int** |  | [optional] 

## Example

```python
from ugc_guard_python.models.guard_evaluation import GuardEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of GuardEvaluation from a JSON string
guard_evaluation_instance = GuardEvaluation.from_json(json)
# print the JSON string representation of the object
print(GuardEvaluation.to_json())

# convert the object into a dict
guard_evaluation_dict = guard_evaluation_instance.to_dict()
# create an instance of GuardEvaluation from a dict
guard_evaluation_from_dict = GuardEvaluation.from_dict(guard_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



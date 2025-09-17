# AIEvaluationBase

Base model for AI evaluation. This is used to define the common fields for all AI evaluations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_selected_category** | [**ReportCategory**](ReportCategory.md) |  | [optional] 
**severity** | **int** | Severity of the report, 1-5, 5 being the most severe.  | [optional] [default to 1]
**explanation** | **str** | Explanation of the AI&#39;s decision | [optional] 
**action_recommendation** | **str** | Recommended action to take on the report | [optional] 
**rule_id** | **str** |  | 

## Example

```python
from ugc_guard_python.models.ai_evaluation_base import AIEvaluationBase

# TODO update the JSON string below
json = "{}"
# create an instance of AIEvaluationBase from a JSON string
ai_evaluation_base_instance = AIEvaluationBase.from_json(json)
# print the JSON string representation of the object
print(AIEvaluationBase.to_json())

# convert the object into a dict
ai_evaluation_base_dict = ai_evaluation_base_instance.to_dict()
# create an instance of AIEvaluationBase from a dict
ai_evaluation_base_from_dict = AIEvaluationBase.from_dict(ai_evaluation_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



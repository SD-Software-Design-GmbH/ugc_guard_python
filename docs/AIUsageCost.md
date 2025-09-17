# AIUsageCost

Represents the costs for AI usage for the given month and model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_model** | [**AiModel**](AiModel.md) |  | 
**month** | **int** |  | 
**year** | **int** |  | 
**costs** | **float** |  | [optional] [default to 0.0]

## Example

```python
from ugc_guard_python.models.ai_usage_cost import AIUsageCost

# TODO update the JSON string below
json = "{}"
# create an instance of AIUsageCost from a JSON string
ai_usage_cost_instance = AIUsageCost.from_json(json)
# print the JSON string representation of the object
print(AIUsageCost.to_json())

# convert the object into a dict
ai_usage_cost_dict = ai_usage_cost_instance.to_dict()
# create an instance of AIUsageCost from a dict
ai_usage_cost_from_dict = AIUsageCost.from_dict(ai_usage_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



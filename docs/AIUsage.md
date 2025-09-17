# AIUsage

Logs the usage of AI models per organization per month.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**month** | **int** | The month of the AI | 
**year** | **int** | The year of the AI usage | 
**used_tokens** | **int** | The number of tokens used by the AI model in this month | [optional] [default to 0]
**used_input_tokens** | **int** | The number of input tokens used by the AI model in this month | [optional] [default to 0]
**used_output_tokens** | **int** | The number of output tokens used by the AI model in this month | [optional] [default to 0]
**ai_model** | **str** |  | 
**usage_count** | **int** |  | [optional] [default to 0]

## Example

```python
from ugc_guard_python.models.ai_usage import AIUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AIUsage from a JSON string
ai_usage_instance = AIUsage.from_json(json)
# print the JSON string representation of the object
print(AIUsage.to_json())

# convert the object into a dict
ai_usage_dict = ai_usage_instance.to_dict()
# create an instance of AIUsage from a dict
ai_usage_from_dict = AIUsage.from_dict(ai_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



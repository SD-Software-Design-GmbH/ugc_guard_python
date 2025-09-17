# AiModel

Represents available AI models.  Not a table because it is loaded from the config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to False]
**model** | **str** |  | 
**description** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**costs_per_factor_input_tokens** | **float** |  | [optional] [default to 0.0]
**costs_per_factor_output_tokens** | **float** |  | [optional] [default to 0.0]
**factor_tokens** | **int** |  | [optional] [default to 1000]

## Example

```python
from ugc_guard_python.models.ai_model import AiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AiModel from a JSON string
ai_model_instance = AiModel.from_json(json)
# print the JSON string representation of the object
print(AiModel.to_json())

# convert the object into a dict
ai_model_dict = ai_model_instance.to_dict()
# create an instance of AiModel from a dict
ai_model_from_dict = AiModel.from_dict(ai_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



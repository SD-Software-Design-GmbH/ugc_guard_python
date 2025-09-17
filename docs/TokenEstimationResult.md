# TokenEstimationResult

Represents the token estimation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens_estimation** | **int** |  | 
**estimated_costs** | **float** |  | 
**model** | [**AiModel**](AiModel.md) |  | 

## Example

```python
from ugc_guard_python.models.token_estimation_result import TokenEstimationResult

# TODO update the JSON string below
json = "{}"
# create an instance of TokenEstimationResult from a JSON string
token_estimation_result_instance = TokenEstimationResult.from_json(json)
# print the JSON string representation of the object
print(TokenEstimationResult.to_json())

# convert the object into a dict
token_estimation_result_dict = token_estimation_result_instance.to_dict()
# create an instance of TokenEstimationResult from a dict
token_estimation_result_from_dict = TokenEstimationResult.from_dict(token_estimation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



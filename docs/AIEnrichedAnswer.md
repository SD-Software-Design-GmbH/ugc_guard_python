# AIEnrichedAnswer

Represents an enriched answer with all evaluations for a report, and all enabled AI models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluations** | [**List[AIEvaluation]**](AIEvaluation.md) |  | [optional] 
**ai_models** | [**List[AiModel]**](AiModel.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.ai_enriched_answer import AIEnrichedAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of AIEnrichedAnswer from a JSON string
ai_enriched_answer_instance = AIEnrichedAnswer.from_json(json)
# print the JSON string representation of the object
print(AIEnrichedAnswer.to_json())

# convert the object into a dict
ai_enriched_answer_dict = ai_enriched_answer_instance.to_dict()
# create an instance of AIEnrichedAnswer from a dict
ai_enriched_answer_from_dict = AIEnrichedAnswer.from_dict(ai_enriched_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



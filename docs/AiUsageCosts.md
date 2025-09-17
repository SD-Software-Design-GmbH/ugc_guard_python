# AiUsageCosts

Represents the AI usage costs for an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**costs** | **Dict[str, List[AIUsageCost]]** |  | [optional] 

## Example

```python
from ugc_guard_python.models.ai_usage_costs import AiUsageCosts

# TODO update the JSON string below
json = "{}"
# create an instance of AiUsageCosts from a JSON string
ai_usage_costs_instance = AiUsageCosts.from_json(json)
# print the JSON string representation of the object
print(AiUsageCosts.to_json())

# convert the object into a dict
ai_usage_costs_dict = ai_usage_costs_instance.to_dict()
# create an instance of AiUsageCosts from a dict
ai_usage_costs_from_dict = AiUsageCosts.from_dict(ai_usage_costs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



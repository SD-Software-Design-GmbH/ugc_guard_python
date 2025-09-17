# ExtendedActionHistory

Represents an extended action history with additional information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**action_id** | **str** |  | 
**content_unique_partner_id** | **str** |  | [optional] 
**person_id** | **str** |  | 
**report_id** | **str** |  | 
**performed_at** | **datetime** |  | [optional] 
**performed_by_id** | **str** |  | 
**success** | **bool** |  | [optional] [default to False]
**person** | [**Person**](Person.md) |  | [optional] 
**performed_by** | [**UserBase**](UserBase.md) |  | [optional] 
**action** | [**ActionBase**](ActionBase.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.extended_action_history import ExtendedActionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedActionHistory from a JSON string
extended_action_history_instance = ExtendedActionHistory.from_json(json)
# print the JSON string representation of the object
print(ExtendedActionHistory.to_json())

# convert the object into a dict
extended_action_history_dict = extended_action_history_instance.to_dict()
# create an instance of ExtendedActionHistory from a dict
extended_action_history_from_dict = ExtendedActionHistory.from_dict(extended_action_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



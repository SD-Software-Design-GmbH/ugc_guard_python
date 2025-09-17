# ActionHistory

Model for ActionHistory. This is used to log the actions performed on a type.

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

## Example

```python
from ugc_guard_python.models.action_history import ActionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ActionHistory from a JSON string
action_history_instance = ActionHistory.from_json(json)
# print the JSON string representation of the object
print(ActionHistory.to_json())

# convert the object into a dict
action_history_dict = action_history_instance.to_dict()
# create an instance of ActionHistory from a dict
action_history_from_dict = ActionHistory.from_dict(action_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ActionBase

Base model for Action. This is used to define the common fields for all actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**url** | **str** |  | 
**is_destructive** | **bool** |  | [optional] [default to False]
**type_id** | **str** |  | 

## Example

```python
from ugc_guard_python.models.action_base import ActionBase

# TODO update the JSON string below
json = "{}"
# create an instance of ActionBase from a JSON string
action_base_instance = ActionBase.from_json(json)
# print the JSON string representation of the object
print(ActionBase.to_json())

# convert the object into a dict
action_base_dict = action_base_instance.to_dict()
# create an instance of ActionBase from a dict
action_base_from_dict = ActionBase.from_dict(action_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



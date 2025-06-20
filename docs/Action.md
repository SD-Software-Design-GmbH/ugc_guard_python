# Action

Model for Action. An action is a specific operation that can be performed on a type.  E.g.: - Obscure image on the partner server - Tombstone chat message - Remove sender (user) from chat room - Etc

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
from ugc_guard_python.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print(Action.to_json())

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_from_dict = Action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



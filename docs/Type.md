# Type

Model for Type. A type is a specific type of resource that can be used in a module.  E.g.: User, Chat-Room, Chat-Message, Forum-Post, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**module_id** | **str** |  | 
**is_user_type** | **bool** |  | [optional] [default to False]
**action_secret** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.type import Type

# TODO update the JSON string below
json = "{}"
# create an instance of Type from a JSON string
type_instance = Type.from_json(json)
# print the JSON string representation of the object
print(Type.to_json())

# convert the object into a dict
type_dict = type_instance.to_dict()
# create an instance of Type from a dict
type_from_dict = Type.from_dict(type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



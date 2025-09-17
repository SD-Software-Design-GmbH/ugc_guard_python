# UserBase

Base model for User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.user_base import UserBase

# TODO update the JSON string below
json = "{}"
# create an instance of UserBase from a JSON string
user_base_instance = UserBase.from_json(json)
# print the JSON string representation of the object
print(UserBase.to_json())

# convert the object into a dict
user_base_dict = user_base_instance.to_dict()
# create an instance of UserBase from a dict
user_base_from_dict = UserBase.from_dict(user_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



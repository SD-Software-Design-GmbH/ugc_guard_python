# ChangePasswordBody

Represents the body for changing a password.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_password** | **str** |  | [optional] 
**new_password** | **str** |  | 

## Example

```python
from ugc_guard_python.models.change_password_body import ChangePasswordBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePasswordBody from a JSON string
change_password_body_instance = ChangePasswordBody.from_json(json)
# print the JSON string representation of the object
print(ChangePasswordBody.to_json())

# convert the object into a dict
change_password_body_dict = change_password_body_instance.to_dict()
# create an instance of ChangePasswordBody from a dict
change_password_body_from_dict = ChangePasswordBody.from_dict(change_password_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



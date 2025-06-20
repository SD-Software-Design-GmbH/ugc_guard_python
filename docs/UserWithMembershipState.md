# UserWithMembershipState

A user model that includes the membership state in the requested organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | 
**email** | **str** |  | 
**avatar_url** | **str** |  | [optional] 
**membership_state** | [**UserOrganizationMembershipState**](UserOrganizationMembershipState.md) |  | 

## Example

```python
from ugc_guard_python.models.user_with_membership_state import UserWithMembershipState

# TODO update the JSON string below
json = "{}"
# create an instance of UserWithMembershipState from a JSON string
user_with_membership_state_instance = UserWithMembershipState.from_json(json)
# print the JSON string representation of the object
print(UserWithMembershipState.to_json())

# convert the object into a dict
user_with_membership_state_dict = user_with_membership_state_instance.to_dict()
# create an instance of UserWithMembershipState from a dict
user_with_membership_state_from_dict = UserWithMembershipState.from_dict(user_with_membership_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



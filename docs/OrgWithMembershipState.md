# OrgWithMembershipState

A class to represent an organization with its membership state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**logo_id** | **str** |  | 
**enabled_ai_list** | **List[str]** |  | [optional] 
**enabled_ai** | **bool** |  | [optional] 
**support_email** | **str** |  | [optional] 
**membership_state** | [**UserOrganizationMembershipState**](UserOrganizationMembershipState.md) |  | 

## Example

```python
from ugc_guard_python.models.org_with_membership_state import OrgWithMembershipState

# TODO update the JSON string below
json = "{}"
# create an instance of OrgWithMembershipState from a JSON string
org_with_membership_state_instance = OrgWithMembershipState.from_json(json)
# print the JSON string representation of the object
print(OrgWithMembershipState.to_json())

# convert the object into a dict
org_with_membership_state_dict = org_with_membership_state_instance.to_dict()
# create an instance of OrgWithMembershipState from a dict
org_with_membership_state_from_dict = OrgWithMembershipState.from_dict(org_with_membership_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



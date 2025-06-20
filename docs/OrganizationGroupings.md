# OrganizationGroupings

A class to group your organizations by their membership states.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invites** | [**List[OrgWithMembershipState]**](OrgWithMembershipState.md) |  | [optional] [default to []]
**reviewers** | [**List[OrgWithMembershipState]**](OrgWithMembershipState.md) |  | [optional] [default to []]
**members** | [**List[OrgWithMembershipState]**](OrgWithMembershipState.md) |  | [optional] [default to []]
**admins** | [**List[OrgWithMembershipState]**](OrgWithMembershipState.md) |  | [optional] [default to []]

## Example

```python
from ugc_guard_python.models.organization_groupings import OrganizationGroupings

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGroupings from a JSON string
organization_groupings_instance = OrganizationGroupings.from_json(json)
# print the JSON string representation of the object
print(OrganizationGroupings.to_json())

# convert the object into a dict
organization_groupings_dict = organization_groupings_instance.to_dict()
# create an instance of OrganizationGroupings from a dict
organization_groupings_from_dict = OrganizationGroupings.from_dict(organization_groupings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



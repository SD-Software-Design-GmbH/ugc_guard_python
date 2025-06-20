# PaginatedResultUserWithMembershipState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[UserWithMembershipState]**](UserWithMembershipState.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_user_with_membership_state import PaginatedResultUserWithMembershipState

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultUserWithMembershipState from a JSON string
paginated_result_user_with_membership_state_instance = PaginatedResultUserWithMembershipState.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultUserWithMembershipState.to_json())

# convert the object into a dict
paginated_result_user_with_membership_state_dict = paginated_result_user_with_membership_state_instance.to_dict()
# create an instance of PaginatedResultUserWithMembershipState from a dict
paginated_result_user_with_membership_state_from_dict = PaginatedResultUserWithMembershipState.from_dict(paginated_result_user_with_membership_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



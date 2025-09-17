# UserWithIdentityProviders

A user model that includes the identity providers associated with the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**identity_providers** | [**List[UserIdentityMappingWithProvider]**](UserIdentityMappingWithProvider.md) |  | [optional] [default to []]

## Example

```python
from ugc_guard_python.models.user_with_identity_providers import UserWithIdentityProviders

# TODO update the JSON string below
json = "{}"
# create an instance of UserWithIdentityProviders from a JSON string
user_with_identity_providers_instance = UserWithIdentityProviders.from_json(json)
# print the JSON string representation of the object
print(UserWithIdentityProviders.to_json())

# convert the object into a dict
user_with_identity_providers_dict = user_with_identity_providers_instance.to_dict()
# create an instance of UserWithIdentityProviders from a dict
user_with_identity_providers_from_dict = UserWithIdentityProviders.from_dict(user_with_identity_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



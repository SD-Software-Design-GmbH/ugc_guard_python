# UserIdentityMappingWithProvider

A user identity mapping that includes the identity provider details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID of the user in the UGC Guard database | 
**identity_provider_id** | **str** |  | 
**identity_provider_user_id** | **str** | The unique user ID in the identity provider (sub) | 
**identity_provider** | [**IdentityProviderBase**](IdentityProviderBase.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.user_identity_mapping_with_provider import UserIdentityMappingWithProvider

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentityMappingWithProvider from a JSON string
user_identity_mapping_with_provider_instance = UserIdentityMappingWithProvider.from_json(json)
# print the JSON string representation of the object
print(UserIdentityMappingWithProvider.to_json())

# convert the object into a dict
user_identity_mapping_with_provider_dict = user_identity_mapping_with_provider_instance.to_dict()
# create an instance of UserIdentityMappingWithProvider from a dict
user_identity_mapping_with_provider_from_dict = UserIdentityMappingWithProvider.from_dict(user_identity_mapping_with_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IdentityProviderBase

Base model for IdentityProvider. This is used to define the public facing fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**enabled** | **bool** | Whether the identity provider is enabled | [optional] [default to False]

## Example

```python
from ugc_guard_python.models.identity_provider_base import IdentityProviderBase

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderBase from a JSON string
identity_provider_base_instance = IdentityProviderBase.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderBase.to_json())

# convert the object into a dict
identity_provider_base_dict = identity_provider_base_instance.to_dict()
# create an instance of IdentityProviderBase from a dict
identity_provider_base_from_dict = IdentityProviderBase.from_dict(identity_provider_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



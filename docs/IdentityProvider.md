# IdentityProvider

Model for IdentityProviders (like Google, Apple, Hanko, etc.).  Using OpenID Connect (OIDC) for authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**enabled** | **bool** | Whether the identity provider is enabled | [optional] [default to False]
**client_id** | **str** | Client ID for the OIDC provider | 
**client_secret** | **str** | Client secret for the OIDC provider | 
**discovery_url** | **str** | Discovery URL for the OIDC provider | 
**organization_id** | **str** | The organization this identity provider belongs to | 
**scopes** | **str** | Scopes to request from the OIDC provider. Default is openid profile email. Separated by spaces. | [optional] [default to 'openid profile email']
**auto_create_user** | **bool** | Whether to automatically create a user when they authenticate with this provider. If false, the user must be created manually before they can authenticate. | [optional] [default to True]
**allow_linking** | **bool** | Whether to allow linking of this identity provider to existing users (using the E-Mail). If false, users must authenticate with this provider to create a new account. | [optional] [default to True]
**identity_token_user_field** | **str** | The field in the identity token that contains the user ID. Default is &#39;sub&#39; which is common in OIDC providers. | [optional] [default to 'sub']
**identity_token_email_field** | **str** | The field in the identity token that contains the user&#39;s email. Default is &#39;email&#39; which is common in OIDC providers. | [optional] [default to 'email']
**identity_token_username_field** | **str** | The field in the identity token that contains the user&#39;s username. Default is &#39;preferred_username&#39; which is common in OIDC providers. We will fallback to &#39;username&#39; if not found, and then to &#39;email&#39;. | [optional] [default to 'preferred_username']
**identity_token_name_field** | **str** | The field in the identity token that contains the user&#39;s username. Default is &#39;preferred_username&#39; which is common in OIDC providers. We will fallback to &#39;username&#39; if not found, and then to &#39;email&#39;. | [optional] [default to 'name']
**identity_token_avatar_url_field** | **str** | The field in the identity token that contains the user&#39;s avatar URL. Default is &#39;picture&#39; which is common in OIDC providers. | [optional] [default to 'picture']
**identity_token_channels_mapper_field** | **str** | The field in the identity token that contains the user&#39;s channels. Default is &#39;channels&#39;. | [optional] [default to 'channels']

## Example

```python
from ugc_guard_python.models.identity_provider import IdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProvider from a JSON string
identity_provider_instance = IdentityProvider.from_json(json)
# print the JSON string representation of the object
print(IdentityProvider.to_json())

# convert the object into a dict
identity_provider_dict = identity_provider_instance.to_dict()
# create an instance of IdentityProvider from a dict
identity_provider_from_dict = IdentityProvider.from_dict(identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



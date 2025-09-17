# LoginPreparation

Represents the preparation needed for a login.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[OrganizationBase]**](OrganizationBase.md) |  | [optional] [default to []]
**identity_providers** | **Dict[str, List[IdentityProviderBase]]** |  | [optional] 

## Example

```python
from ugc_guard_python.models.login_preparation import LoginPreparation

# TODO update the JSON string below
json = "{}"
# create an instance of LoginPreparation from a JSON string
login_preparation_instance = LoginPreparation.from_json(json)
# print the JSON string representation of the object
print(LoginPreparation.to_json())

# convert the object into a dict
login_preparation_dict = login_preparation_instance.to_dict()
# create an instance of LoginPreparation from a dict
login_preparation_from_dict = LoginPreparation.from_dict(login_preparation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



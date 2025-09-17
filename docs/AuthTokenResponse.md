# AuthTokenResponse

Represents the response for an authentication token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**token_type** | **str** |  | [optional] [default to 'bearer']

## Example

```python
from ugc_guard_python.models.auth_token_response import AuthTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenResponse from a JSON string
auth_token_response_instance = AuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AuthTokenResponse.to_json())

# convert the object into a dict
auth_token_response_dict = auth_token_response_instance.to_dict()
# create an instance of AuthTokenResponse from a dict
auth_token_response_from_dict = AuthTokenResponse.from_dict(auth_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



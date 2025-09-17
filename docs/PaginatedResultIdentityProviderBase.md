# PaginatedResultIdentityProviderBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[IdentityProviderBase]**](IdentityProviderBase.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_identity_provider_base import PaginatedResultIdentityProviderBase

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultIdentityProviderBase from a JSON string
paginated_result_identity_provider_base_instance = PaginatedResultIdentityProviderBase.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultIdentityProviderBase.to_json())

# convert the object into a dict
paginated_result_identity_provider_base_dict = paginated_result_identity_provider_base_instance.to_dict()
# create an instance of PaginatedResultIdentityProviderBase from a dict
paginated_result_identity_provider_base_from_dict = PaginatedResultIdentityProviderBase.from_dict(paginated_result_identity_provider_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



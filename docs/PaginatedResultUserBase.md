# PaginatedResultUserBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[UserBase]**](UserBase.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_user_base import PaginatedResultUserBase

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultUserBase from a JSON string
paginated_result_user_base_instance = PaginatedResultUserBase.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultUserBase.to_json())

# convert the object into a dict
paginated_result_user_base_dict = paginated_result_user_base_instance.to_dict()
# create an instance of PaginatedResultUserBase from a dict
paginated_result_user_base_from_dict = PaginatedResultUserBase.from_dict(paginated_result_user_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



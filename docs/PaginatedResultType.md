# PaginatedResultType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[Type]**](Type.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_type import PaginatedResultType

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultType from a JSON string
paginated_result_type_instance = PaginatedResultType.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultType.to_json())

# convert the object into a dict
paginated_result_type_dict = paginated_result_type_instance.to_dict()
# create an instance of PaginatedResultType from a dict
paginated_result_type_from_dict = PaginatedResultType.from_dict(paginated_result_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PaginatedResultGuard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[Guard]**](Guard.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_guard import PaginatedResultGuard

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultGuard from a JSON string
paginated_result_guard_instance = PaginatedResultGuard.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultGuard.to_json())

# convert the object into a dict
paginated_result_guard_dict = paginated_result_guard_instance.to_dict()
# create an instance of PaginatedResultGuard from a dict
paginated_result_guard_from_dict = PaginatedResultGuard.from_dict(paginated_result_guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



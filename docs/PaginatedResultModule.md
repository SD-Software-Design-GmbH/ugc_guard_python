# PaginatedResultModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[Module]**](Module.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_module import PaginatedResultModule

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultModule from a JSON string
paginated_result_module_instance = PaginatedResultModule.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultModule.to_json())

# convert the object into a dict
paginated_result_module_dict = paginated_result_module_instance.to_dict()
# create an instance of PaginatedResultModule from a dict
paginated_result_module_from_dict = PaginatedResultModule.from_dict(paginated_result_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



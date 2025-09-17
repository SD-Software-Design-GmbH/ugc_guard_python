# PaginatedResultExtendedActionHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[ExtendedActionHistory]**](ExtendedActionHistory.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_extended_action_history import PaginatedResultExtendedActionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultExtendedActionHistory from a JSON string
paginated_result_extended_action_history_instance = PaginatedResultExtendedActionHistory.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultExtendedActionHistory.to_json())

# convert the object into a dict
paginated_result_extended_action_history_dict = paginated_result_extended_action_history_instance.to_dict()
# create an instance of PaginatedResultExtendedActionHistory from a dict
paginated_result_extended_action_history_from_dict = PaginatedResultExtendedActionHistory.from_dict(paginated_result_extended_action_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



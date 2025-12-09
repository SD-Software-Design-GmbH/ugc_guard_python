# PaginatedResultGuardEvaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[GuardEvaluation]**](GuardEvaluation.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_guard_evaluation import PaginatedResultGuardEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultGuardEvaluation from a JSON string
paginated_result_guard_evaluation_instance = PaginatedResultGuardEvaluation.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultGuardEvaluation.to_json())

# convert the object into a dict
paginated_result_guard_evaluation_dict = paginated_result_guard_evaluation_instance.to_dict()
# create an instance of PaginatedResultGuardEvaluation from a dict
paginated_result_guard_evaluation_from_dict = PaginatedResultGuardEvaluation.from_dict(paginated_result_guard_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



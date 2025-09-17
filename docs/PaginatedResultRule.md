# PaginatedResultRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[Rule]**](Rule.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_rule import PaginatedResultRule

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultRule from a JSON string
paginated_result_rule_instance = PaginatedResultRule.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultRule.to_json())

# convert the object into a dict
paginated_result_rule_dict = paginated_result_rule_instance.to_dict()
# create an instance of PaginatedResultRule from a dict
paginated_result_rule_from_dict = PaginatedResultRule.from_dict(paginated_result_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



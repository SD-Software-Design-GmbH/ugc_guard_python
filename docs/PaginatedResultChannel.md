# PaginatedResultChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[Channel]**](Channel.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_channel import PaginatedResultChannel

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultChannel from a JSON string
paginated_result_channel_instance = PaginatedResultChannel.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultChannel.to_json())

# convert the object into a dict
paginated_result_channel_dict = paginated_result_channel_instance.to_dict()
# create an instance of PaginatedResultChannel from a dict
paginated_result_channel_from_dict = PaginatedResultChannel.from_dict(paginated_result_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



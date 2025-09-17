# AllContentResponse

The content data for a report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_content** | [**ContentPublic**](ContentPublic.md) |  | [optional] 
**context** | [**List[ContentPublic]**](ContentPublic.md) |  | 
**history** | [**List[ActionHistory]**](ActionHistory.md) |  | [optional] [default to []]
**types** | [**List[Type]**](Type.md) |  | [optional] [default to []]

## Example

```python
from ugc_guard_python.models.all_content_response import AllContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllContentResponse from a JSON string
all_content_response_instance = AllContentResponse.from_json(json)
# print the JSON string representation of the object
print(AllContentResponse.to_json())

# convert the object into a dict
all_content_response_dict = all_content_response_instance.to_dict()
# create an instance of AllContentResponse from a dict
all_content_response_from_dict = AllContentResponse.from_dict(all_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_type** | [**ContentType**](ContentType.md) |  | [optional] 
**body** | **str** |  | [optional] 
**media_identifiers** | **List[str]** |  | [optional] 
**extra_data** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**unique_partner_id** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**creator_id** | **str** |  | 
**type_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**creator** | [**Person**](Person.md) |  | [optional] 
**comments** | [**List[CommentWithCreator]**](CommentWithCreator.md) |  | [optional] [default to []]

## Example

```python
from ugc_guard_python.models.content_public import ContentPublic

# TODO update the JSON string below
json = "{}"
# create an instance of ContentPublic from a JSON string
content_public_instance = ContentPublic.from_json(json)
# print the JSON string representation of the object
print(ContentPublic.to_json())

# convert the object into a dict
content_public_dict = content_public_instance.to_dict()
# create an instance of ContentPublic from a dict
content_public_from_dict = ContentPublic.from_dict(content_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentCreate

Model for creating content. This is used to define the fields required to create a new content.

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
**creator_id** | **str** |  | [optional] 
**type_id** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.content_create import ContentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ContentCreate from a JSON string
content_create_instance = ContentCreate.from_json(json)
# print the JSON string representation of the object
print(ContentCreate.to_json())

# convert the object into a dict
content_create_dict = content_create_instance.to_dict()
# create an instance of ContentCreate from a dict
content_create_from_dict = ContentCreate.from_dict(content_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



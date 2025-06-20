# Content

A report context is a content that is related to the report.

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
**id** | **str** |  | [optional] 
**report_id** | **str** |  | 

## Example

```python
from ugc_guard_python.models.content import Content

# TODO update the JSON string below
json = "{}"
# create an instance of Content from a JSON string
content_instance = Content.from_json(json)
# print the JSON string representation of the object
print(Content.to_json())

# convert the object into a dict
content_dict = content_instance.to_dict()
# create an instance of Content from a dict
content_from_dict = Content.from_dict(content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



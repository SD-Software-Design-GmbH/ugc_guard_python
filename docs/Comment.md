# Comment

A comment is a user comment on a report or content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**creator_id** | **str** |  | 
**show_public** | **bool** | Is this comment visible to the public? If true, it will be shown in the reporters report page. | [optional] [default to False]
**report_id** | **str** |  | 
**content_id** | **str** |  | 

## Example

```python
from ugc_guard_python.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



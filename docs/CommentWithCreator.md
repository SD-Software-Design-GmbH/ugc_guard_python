# CommentWithCreator

Represents a comment with its creator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**creator_id** | **str** |  | 
**show_public** | **bool** | Is this comment visible to the public? If true, it will be shown in the reporters report page. | [optional] [default to False]
**creator** | [**UserBase**](UserBase.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.comment_with_creator import CommentWithCreator

# TODO update the JSON string below
json = "{}"
# create an instance of CommentWithCreator from a JSON string
comment_with_creator_instance = CommentWithCreator.from_json(json)
# print the JSON string representation of the object
print(CommentWithCreator.to_json())

# convert the object into a dict
comment_with_creator_dict = comment_with_creator_instance.to_dict()
# create an instance of CommentWithCreator from a dict
comment_with_creator_from_dict = CommentWithCreator.from_dict(comment_with_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



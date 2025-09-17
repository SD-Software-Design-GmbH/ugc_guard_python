# File

A file is a somewhere stored object that is related to a report or content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**report_id** | **str** |  | 
**content_id** | **str** |  | 
**file_path** | **str** |  | [optional] 
**file_type** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**blur_hash** | **str** |  | [optional] 
**uploader_id** | **str** |  | 
**in_s3** | **bool** |  | [optional] [default to False]
**secret** | **str** |  | [optional] 
**uploaded_at** | **datetime** |  | [optional] 
**removed_at** | **datetime** |  | [optional] 
**module_id** | **str** |  | 
**person_id** | **str** |  | 

## Example

```python
from ugc_guard_python.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



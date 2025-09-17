# PublicImage

A public image is an image that is available for public access, typically stored in S3 or similar storage. Public images can be profile pictures (of UGC Guard users), logos of organizations, or other images that are not sensitive and can be shared publicly.  These images are available via a public URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**file_type** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**uploader_id** | **str** |  | 
**blur_hash** | **str** |  | [optional] 
**in_s3** | **bool** |  | [optional] [default to False]
**uploaded_at** | **datetime** |  | [optional] 
**removed_at** | **datetime** |  | [optional] 

## Example

```python
from ugc_guard_python.models.public_image import PublicImage

# TODO update the JSON string below
json = "{}"
# create an instance of PublicImage from a JSON string
public_image_instance = PublicImage.from_json(json)
# print the JSON string representation of the object
print(PublicImage.to_json())

# convert the object into a dict
public_image_dict = public_image_instance.to_dict()
# create an instance of PublicImage from a dict
public_image_from_dict = PublicImage.from_dict(public_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



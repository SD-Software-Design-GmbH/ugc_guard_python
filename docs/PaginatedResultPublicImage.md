# PaginatedResultPublicImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[PublicImage]**](PublicImage.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_public_image import PaginatedResultPublicImage

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultPublicImage from a JSON string
paginated_result_public_image_instance = PaginatedResultPublicImage.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultPublicImage.to_json())

# convert the object into a dict
paginated_result_public_image_dict = paginated_result_public_image_instance.to_dict()
# create an instance of PaginatedResultPublicImage from a dict
paginated_result_public_image_from_dict = PaginatedResultPublicImage.from_dict(paginated_result_public_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



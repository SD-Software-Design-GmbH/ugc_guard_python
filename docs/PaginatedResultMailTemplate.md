# PaginatedResultMailTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[MailTemplate]**](MailTemplate.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_mail_template import PaginatedResultMailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultMailTemplate from a JSON string
paginated_result_mail_template_instance = PaginatedResultMailTemplate.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultMailTemplate.to_json())

# convert the object into a dict
paginated_result_mail_template_dict = paginated_result_mail_template_instance.to_dict()
# create an instance of PaginatedResultMailTemplate from a dict
paginated_result_mail_template_from_dict = PaginatedResultMailTemplate.from_dict(paginated_result_mail_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



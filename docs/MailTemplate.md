# MailTemplate

Model for MailTemplate. This is used to store the templates for emails.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**type** | [**MailTemplateType**](MailTemplateType.md) |  | 
**id** | **str** |  | [optional] 
**module_id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from ugc_guard_python.models.mail_template import MailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplate from a JSON string
mail_template_instance = MailTemplate.from_json(json)
# print the JSON string representation of the object
print(MailTemplate.to_json())

# convert the object into a dict
mail_template_dict = mail_template_instance.to_dict()
# create an instance of MailTemplate from a dict
mail_template_from_dict = MailTemplate.from_dict(mail_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MailTemplateBase

Everything that is needed for sending a mail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**type** | [**MailTemplateType**](MailTemplateType.md) |  | 

## Example

```python
from ugc_guard_python.models.mail_template_base import MailTemplateBase

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplateBase from a JSON string
mail_template_base_instance = MailTemplateBase.from_json(json)
# print the JSON string representation of the object
print(MailTemplateBase.to_json())

# convert the object into a dict
mail_template_base_dict = mail_template_base_instance.to_dict()
# create an instance of MailTemplateBase from a dict
mail_template_base_from_dict = MailTemplateBase.from_dict(mail_template_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



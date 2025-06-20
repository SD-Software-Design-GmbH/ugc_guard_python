# MailTemplatesWithDefaults

A model that combines all mail templates for a module with default templates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_templates** | [**List[MailTemplate]**](MailTemplate.md) |  | [optional] [default to []]
**default_templates** | [**List[MailTemplateBase]**](MailTemplateBase.md) |  | [optional] [default to []]

## Example

```python
from ugc_guard_python.models.mail_templates_with_defaults import MailTemplatesWithDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplatesWithDefaults from a JSON string
mail_templates_with_defaults_instance = MailTemplatesWithDefaults.from_json(json)
# print the JSON string representation of the object
print(MailTemplatesWithDefaults.to_json())

# convert the object into a dict
mail_templates_with_defaults_dict = mail_templates_with_defaults_instance.to_dict()
# create an instance of MailTemplatesWithDefaults from a dict
mail_templates_with_defaults_from_dict = MailTemplatesWithDefaults.from_dict(mail_templates_with_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



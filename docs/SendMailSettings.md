# SendMailSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_mail_on_report** | **bool** |  | [optional] [default to False]
**send_mail_on_report_to_user** | **bool** |  | [optional] [default to False]
**send_mail_on_resolved_report_to_user** | **bool** |  | [optional] [default to False]
**send_mail_on_escalation_to_creators** | **bool** |  | [optional] [default to False]
**send_mail_on_rejection_to_creator** | **bool** |  | [optional] [default to False]

## Example

```python
from ugc_guard_python.models.send_mail_settings import SendMailSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SendMailSettings from a JSON string
send_mail_settings_instance = SendMailSettings.from_json(json)
# print the JSON string representation of the object
print(SendMailSettings.to_json())

# convert the object into a dict
send_mail_settings_dict = send_mail_settings_instance.to_dict()
# create an instance of SendMailSettings from a dict
send_mail_settings_from_dict = SendMailSettings.from_dict(send_mail_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



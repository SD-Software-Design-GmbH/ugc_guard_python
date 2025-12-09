# BodyCreateMagicReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**ReportCreate**](ReportCreate.md) |  | 
**reporter** | [**Reporter**](Reporter.md) |  | 
**main_content** | [**ContentCreate**](ContentCreate.md) |  | 
**report_context** | [**List[ContentCreate]**](ContentCreate.md) |  | 
**report_context_persons** | [**List[Person]**](Person.md) |  | 
**main_content_sender** | [**MainContentSender**](MainContentSender.md) |  | [optional] 
**channels** | **List[str]** |  | [optional] 

## Example

```python
from ugc_guard_python.models.body_create_magic_report import BodyCreateMagicReport

# TODO update the JSON string below
json = "{}"
# create an instance of BodyCreateMagicReport from a JSON string
body_create_magic_report_instance = BodyCreateMagicReport.from_json(json)
# print the JSON string representation of the object
print(BodyCreateMagicReport.to_json())

# convert the object into a dict
body_create_magic_report_dict = body_create_magic_report_instance.to_dict()
# create an instance of BodyCreateMagicReport from a dict
body_create_magic_report_from_dict = BodyCreateMagicReport.from_dict(body_create_magic_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



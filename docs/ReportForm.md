# ReportForm

ReportForm is a SQLModel that represents the structure of a report form in the database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The name of the report form | 
**description** | **str** |  | [optional] 
**is_active** | **bool** | Whether the report form is active or not | [optional] [default to True]
**color_base_hex** | **str** |  | [optional] 
**logo_id** | **str** |  | [optional] 
**module_id** | **str** |  | 
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**final_text** | **str** |  | [optional] 
**redirect_uris** | **str** |  | [optional] 
**ask_for_email** | **bool** | Whether to ask for the user&#39;s email address when submitting the report form | [optional] [default to False]
**ask_for_captcha** | **bool** | Whether to ask for a CAPTCHA when submitting the report form | [optional] [default to False]

## Example

```python
from ugc_guard_python.models.report_form import ReportForm

# TODO update the JSON string below
json = "{}"
# create an instance of ReportForm from a JSON string
report_form_instance = ReportForm.from_json(json)
# print the JSON string representation of the object
print(ReportForm.to_json())

# convert the object into a dict
report_form_dict = report_form_instance.to_dict()
# create an instance of ReportForm from a dict
report_form_from_dict = ReportForm.from_dict(report_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



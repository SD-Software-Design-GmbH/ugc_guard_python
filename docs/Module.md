# Module

Model for Module. A module can be an application or a service.  E.g.: easyVerein or a submodule of easyVerein like easyVerein-Chat or easyVerein-Forum

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_mail_on_report** | **bool** |  | [optional] [default to False]
**send_mail_on_report_to_user** | **bool** |  | [optional] [default to False]
**send_mail_on_resolved_report_to_user** | **bool** |  | [optional] [default to False]
**id** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**auto_ai_validation** | **bool** |  | [optional] [default to False]

## Example

```python
from ugc_guard_python.models.module import Module

# TODO update the JSON string below
json = "{}"
# create an instance of Module from a JSON string
module_instance = Module.from_json(json)
# print the JSON string representation of the object
print(Module.to_json())

# convert the object into a dict
module_dict = module_instance.to_dict()
# create an instance of Module from a dict
module_from_dict = Module.from_dict(module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



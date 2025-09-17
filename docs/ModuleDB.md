# ModuleDB

Extends the Module model to include the database only fields that shall not be reported to the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_mail_on_report** | **bool** |  | [optional] [default to False]
**send_mail_on_report_to_user** | **bool** |  | [optional] [default to False]
**send_mail_on_resolved_report_to_user** | **bool** |  | [optional] [default to False]
**send_mail_on_escalation_to_creators** | **bool** |  | [optional] [default to False]
**send_mail_on_rejection_to_creator** | **bool** |  | [optional] [default to False]
**id** | **str** |  | [optional] 
**logo_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**auto_ai_validation** | **bool** |  | [optional] [default to False]
**secret** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.module_db import ModuleDB

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleDB from a JSON string
module_db_instance = ModuleDB.from_json(json)
# print the JSON string representation of the object
print(ModuleDB.to_json())

# convert the object into a dict
module_db_dict = module_db_instance.to_dict()
# create an instance of ModuleDB from a dict
module_db_from_dict = ModuleDB.from_dict(module_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



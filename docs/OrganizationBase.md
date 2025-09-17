# OrganizationBase

    

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**logo_id** | **str** |  | 
**enabled_ai_list** | **List[str]** |  | [optional] 
**enabled_ai** | **bool** |  | [optional] 
**support_email** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.organization_base import OrganizationBase

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationBase from a JSON string
organization_base_instance = OrganizationBase.from_json(json)
# print the JSON string representation of the object
print(OrganizationBase.to_json())

# convert the object into a dict
organization_base_dict = organization_base_instance.to_dict()
# create an instance of OrganizationBase from a dict
organization_base_from_dict = OrganizationBase.from_dict(organization_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



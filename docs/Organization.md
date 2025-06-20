# Organization

Model for Organization. Organizations contain many modules and many users  E.g.: Software-Design GmbH

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**enabled_ai_list** | **List[str]** |  | [optional] 
**enabled_ai** | **bool** |  | [optional] 
**support_email** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



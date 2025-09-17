# Reporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**module_id** | **str** |  | 
**unique_partner_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**extra_data** | **Dict[str, object]** |  | [optional] 
**media_identifiers** | **List[str]** |  | [optional] 

## Example

```python
from ugc_guard_python.models.reporter import Reporter

# TODO update the JSON string below
json = "{}"
# create an instance of Reporter from a JSON string
reporter_instance = Reporter.from_json(json)
# print the JSON string representation of the object
print(Reporter.to_json())

# convert the object into a dict
reporter_dict = reporter_instance.to_dict()
# create an instance of Reporter from a dict
reporter_from_dict = Reporter.from_dict(reporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



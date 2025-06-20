# ReportersWithPerson

Reporters with person information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** |  | 
**reporter_id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**reporter_category** | [**ReportCategory**](ReportCategory.md) |  | [optional] 
**custom_message** | **str** |  | [optional] 
**reporter** | [**Person**](Person.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.reporters_with_person import ReportersWithPerson

# TODO update the JSON string below
json = "{}"
# create an instance of ReportersWithPerson from a JSON string
reporters_with_person_instance = ReportersWithPerson.from_json(json)
# print the JSON string representation of the object
print(ReportersWithPerson.to_json())

# convert the object into a dict
reporters_with_person_dict = reporters_with_person_instance.to_dict()
# create an instance of ReportersWithPerson from a dict
reporters_with_person_from_dict = ReportersWithPerson.from_dict(reporters_with_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



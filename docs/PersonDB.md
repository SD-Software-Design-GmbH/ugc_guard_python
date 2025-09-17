# PersonDB

Extends the Person model to include the database only fields that shall not be reported to the user.

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
from ugc_guard_python.models.person_db import PersonDB

# TODO update the JSON string below
json = "{}"
# create an instance of PersonDB from a JSON string
person_db_instance = PersonDB.from_json(json)
# print the JSON string representation of the object
print(PersonDB.to_json())

# convert the object into a dict
person_db_dict = person_db_instance.to_dict()
# create an instance of PersonDB from a dict
person_db_from_dict = PersonDB.from_dict(person_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



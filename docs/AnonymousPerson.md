# AnonymousPerson

A person is a user that created the content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**module_id** | **str** |  | 
**unique_partner_id** | **str** |  | [optional] 

## Example

```python
from ugc_guard_python.models.anonymous_person import AnonymousPerson

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymousPerson from a JSON string
anonymous_person_instance = AnonymousPerson.from_json(json)
# print the JSON string representation of the object
print(AnonymousPerson.to_json())

# convert the object into a dict
anonymous_person_dict = anonymous_person_instance.to_dict()
# create an instance of AnonymousPerson from a dict
anonymous_person_from_dict = AnonymousPerson.from_dict(anonymous_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MainContentSender


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

## Example

```python
from ugc_guard_python.models.main_content_sender import MainContentSender

# TODO update the JSON string below
json = "{}"
# create an instance of MainContentSender from a JSON string
main_content_sender_instance = MainContentSender.from_json(json)
# print the JSON string representation of the object
print(MainContentSender.to_json())

# convert the object into a dict
main_content_sender_dict = main_content_sender_instance.to_dict()
# create an instance of MainContentSender from a dict
main_content_sender_from_dict = MainContentSender.from_dict(main_content_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ChannelUser

A channel is a user group that can be used to define which user has access to which resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from ugc_guard_python.models.channel_user import ChannelUser

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelUser from a JSON string
channel_user_instance = ChannelUser.from_json(json)
# print the JSON string representation of the object
print(ChannelUser.to_json())

# convert the object into a dict
channel_user_dict = channel_user_instance.to_dict()
# create an instance of ChannelUser from a dict
channel_user_from_dict = ChannelUser.from_dict(channel_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



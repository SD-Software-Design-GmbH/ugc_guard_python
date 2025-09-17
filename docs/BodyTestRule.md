# BodyTestRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_content** | [**ContentCreate**](ContentCreate.md) |  | 
**context** | [**List[ContentCreate]**](ContentCreate.md) |  | [optional] 

## Example

```python
from ugc_guard_python.models.body_test_rule import BodyTestRule

# TODO update the JSON string below
json = "{}"
# create an instance of BodyTestRule from a JSON string
body_test_rule_instance = BodyTestRule.from_json(json)
# print the JSON string representation of the object
print(BodyTestRule.to_json())

# convert the object into a dict
body_test_rule_dict = body_test_rule_instance.to_dict()
# create an instance of BodyTestRule from a dict
body_test_rule_from_dict = BodyTestRule.from_dict(body_test_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



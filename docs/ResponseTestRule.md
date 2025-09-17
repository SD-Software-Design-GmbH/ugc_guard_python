# ResponseTestRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**rule_id** | **str** |  | 
**report_id** | **str** |  | [optional] 
**matched_words** | **List[str]** | List of words that matched the rule during evaluation. If blacklist is used, these are the words that triggered the rule. If whitelist is used, these are the words that did trigger the rule because they are not part of the whitelist | [optional] 
**is_match** | **bool** | Indicates whether the rule matched the content of the report | [optional] [default to False]
**ai_selected_category** | [**ReportCategory**](ReportCategory.md) |  | [optional] 
**severity** | **int** | Severity of the report, 1-5, 5 being the most severe.  | [optional] [default to 1]
**explanation** | **str** | Explanation of the AI&#39;s decision | [optional] 
**action_recommendation** | **str** | Recommended action to take on the report | [optional] 

## Example

```python
from ugc_guard_python.models.response_test_rule import ResponseTestRule

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseTestRule from a JSON string
response_test_rule_instance = ResponseTestRule.from_json(json)
# print the JSON string representation of the object
print(ResponseTestRule.to_json())

# convert the object into a dict
response_test_rule_dict = response_test_rule_instance.to_dict()
# create an instance of ResponseTestRule from a dict
response_test_rule_from_dict = ResponseTestRule.from_dict(response_test_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GuardEvaluationUsageStats

Represents usage statistics for guard evaluations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_evaluations** | **int** |  | [optional] [default to 0]
**total_passed** | **int** |  | [optional] [default to 0]
**total_intervened** | **int** |  | [optional] [default to 0]
**total_failed** | **int** |  | [optional] [default to 0]
**change_evaluations** | **int** |  | [optional] [default to 0]
**change_passed** | **int** |  | [optional] [default to 0]
**change_intervened** | **int** |  | [optional] [default to 0]
**change_failed** | **int** |  | [optional] [default to 0]
**lower_bound** | **datetime** |  | [optional] 
**upper_bound** | **datetime** |  | [optional] 

## Example

```python
from ugc_guard_python.models.guard_evaluation_usage_stats import GuardEvaluationUsageStats

# TODO update the JSON string below
json = "{}"
# create an instance of GuardEvaluationUsageStats from a JSON string
guard_evaluation_usage_stats_instance = GuardEvaluationUsageStats.from_json(json)
# print the JSON string representation of the object
print(GuardEvaluationUsageStats.to_json())

# convert the object into a dict
guard_evaluation_usage_stats_dict = guard_evaluation_usage_stats_instance.to_dict()
# create an instance of GuardEvaluationUsageStats from a dict
guard_evaluation_usage_stats_from_dict = GuardEvaluationUsageStats.from_dict(guard_evaluation_usage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



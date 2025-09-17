# ReportWithReportersAndEvaluations

Report with reporters information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**module_id** | **str** |  | 
**type_id** | **str** |  | 
**id** | **str** |  | [optional] 
**report_state** | [**ReportState**](ReportState.md) |  | [optional] 
**main_content_id** | **str** |  | 
**reported_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**secret** | **str** |  | [optional] 
**reporters** | [**List[ReportersWithPerson]**](ReportersWithPerson.md) |  | [optional] [default to []]
**evaluations** | [**List[AIEvaluation]**](AIEvaluation.md) |  | [optional] [default to []]
**guard_evaluations** | [**List[GuardEvaluation]**](GuardEvaluation.md) |  | [optional] [default to []]

## Example

```python
from ugc_guard_python.models.report_with_reporters_and_evaluations import ReportWithReportersAndEvaluations

# TODO update the JSON string below
json = "{}"
# create an instance of ReportWithReportersAndEvaluations from a JSON string
report_with_reporters_and_evaluations_instance = ReportWithReportersAndEvaluations.from_json(json)
# print the JSON string representation of the object
print(ReportWithReportersAndEvaluations.to_json())

# convert the object into a dict
report_with_reporters_and_evaluations_dict = report_with_reporters_and_evaluations_instance.to_dict()
# create an instance of ReportWithReportersAndEvaluations from a dict
report_with_reporters_and_evaluations_from_dict = ReportWithReportersAndEvaluations.from_dict(report_with_reporters_and_evaluations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



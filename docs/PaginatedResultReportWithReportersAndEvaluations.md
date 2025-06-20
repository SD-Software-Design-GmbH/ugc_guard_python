# PaginatedResultReportWithReportersAndEvaluations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[ReportWithReportersAndEvaluations]**](ReportWithReportersAndEvaluations.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_report_with_reporters_and_evaluations import PaginatedResultReportWithReportersAndEvaluations

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultReportWithReportersAndEvaluations from a JSON string
paginated_result_report_with_reporters_and_evaluations_instance = PaginatedResultReportWithReportersAndEvaluations.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultReportWithReportersAndEvaluations.to_json())

# convert the object into a dict
paginated_result_report_with_reporters_and_evaluations_dict = paginated_result_report_with_reporters_and_evaluations_instance.to_dict()
# create an instance of PaginatedResultReportWithReportersAndEvaluations from a dict
paginated_result_report_with_reporters_and_evaluations_from_dict = PaginatedResultReportWithReportersAndEvaluations.from_dict(paginated_result_report_with_reporters_and_evaluations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



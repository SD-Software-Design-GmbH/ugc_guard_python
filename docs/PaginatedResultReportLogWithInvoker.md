# PaginatedResultReportLogWithInvoker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[ReportLogWithInvoker]**](ReportLogWithInvoker.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_report_log_with_invoker import PaginatedResultReportLogWithInvoker

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultReportLogWithInvoker from a JSON string
paginated_result_report_log_with_invoker_instance = PaginatedResultReportLogWithInvoker.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultReportLogWithInvoker.to_json())

# convert the object into a dict
paginated_result_report_log_with_invoker_dict = paginated_result_report_log_with_invoker_instance.to_dict()
# create an instance of PaginatedResultReportLogWithInvoker from a dict
paginated_result_report_log_with_invoker_from_dict = PaginatedResultReportLogWithInvoker.from_dict(paginated_result_report_log_with_invoker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



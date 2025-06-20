# PaginatedResultReportDB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[ReportDB]**](ReportDB.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_report_db import PaginatedResultReportDB

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultReportDB from a JSON string
paginated_result_report_db_instance = PaginatedResultReportDB.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultReportDB.to_json())

# convert the object into a dict
paginated_result_report_db_dict = paginated_result_report_db_instance.to_dict()
# create an instance of PaginatedResultReportDB from a dict
paginated_result_report_db_from_dict = PaginatedResultReportDB.from_dict(paginated_result_report_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



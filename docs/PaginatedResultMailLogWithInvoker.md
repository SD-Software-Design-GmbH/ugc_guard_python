# PaginatedResultMailLogWithInvoker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of items available items in the database following given criteria | 
**items** | [**List[MailLogWithInvoker]**](MailLogWithInvoker.md) | List of items returned in the response following given criteria | 

## Example

```python
from ugc_guard_python.models.paginated_result_mail_log_with_invoker import PaginatedResultMailLogWithInvoker

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultMailLogWithInvoker from a JSON string
paginated_result_mail_log_with_invoker_instance = PaginatedResultMailLogWithInvoker.from_json(json)
# print the JSON string representation of the object
print(PaginatedResultMailLogWithInvoker.to_json())

# convert the object into a dict
paginated_result_mail_log_with_invoker_dict = paginated_result_mail_log_with_invoker_instance.to_dict()
# create an instance of PaginatedResultMailLogWithInvoker from a dict
paginated_result_mail_log_with_invoker_from_dict = PaginatedResultMailLogWithInvoker.from_dict(paginated_result_mail_log_with_invoker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ugc_guard_python.LogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mail_logs**](LogsApi.md#get_mail_logs) | **GET** /logs/mail/{organization_id} | Get Mail Logs
[**get_report_logs**](LogsApi.md#get_report_logs) | **GET** /logs/report/{organization_id} | Get Report Logs


# **get_mail_logs**
> PaginatedResultMailLogWithInvoker get_mail_logs(organization_id, offset=offset, limit=limit, query=query)

Get Mail Logs

Get paginated mail logs for an organization.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_mail_log_with_invoker import PaginatedResultMailLogWithInvoker
from ugc_guard_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ugc_guard_python.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ugc_guard_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ugc_guard_python.LogsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    query = 'query_example' # str |  (optional)

    try:
        # Get Mail Logs
        api_response = api_instance.get_mail_logs(organization_id, offset=offset, limit=limit, query=query)
        print("The response of LogsApi->get_mail_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->get_mail_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 

### Return type

[**PaginatedResultMailLogWithInvoker**](PaginatedResultMailLogWithInvoker.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_logs**
> PaginatedResultReportLogWithInvoker get_report_logs(organization_id, offset=offset, limit=limit, query=query)

Get Report Logs

Get paginated report logs for an organization.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_report_log_with_invoker import PaginatedResultReportLogWithInvoker
from ugc_guard_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ugc_guard_python.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ugc_guard_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ugc_guard_python.LogsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    query = 'query_example' # str |  (optional)

    try:
        # Get Report Logs
        api_response = api_instance.get_report_logs(organization_id, offset=offset, limit=limit, query=query)
        print("The response of LogsApi->get_report_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->get_report_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 

### Return type

[**PaginatedResultReportLogWithInvoker**](PaginatedResultReportLogWithInvoker.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


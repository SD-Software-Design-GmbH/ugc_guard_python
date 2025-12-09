# ugc_guard_python.WebhookLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_webhook_log_by_id**](WebhookLogsApi.md#get_webhook_log_by_id) | **GET** /webhooks/logs/{log_id} | Get Webhook Log By Id
[**get_webhook_logs_for_organization**](WebhookLogsApi.md#get_webhook_logs_for_organization) | **GET** /webhooks/logs/organization/{organization_id} | Get Webhook Logs For Organization


# **get_webhook_log_by_id**
> WebhookLog get_webhook_log_by_id(log_id)

Get Webhook Log By Id

Get a webhook log entry by its ID.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.webhook_log import WebhookLog
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
    api_instance = ugc_guard_python.WebhookLogsApi(api_client)
    log_id = 'log_id_example' # str | 

    try:
        # Get Webhook Log By Id
        api_response = api_instance.get_webhook_log_by_id(log_id)
        print("The response of WebhookLogsApi->get_webhook_log_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookLogsApi->get_webhook_log_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_id** | **str**|  | 

### Return type

[**WebhookLog**](WebhookLog.md)

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

# **get_webhook_logs_for_organization**
> PaginatedResultWebhookLogBase get_webhook_logs_for_organization(organization_id, offset=offset, limit=limit)

Get Webhook Logs For Organization

Get paginated webhook logs for a specific organization.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_webhook_log_base import PaginatedResultWebhookLogBase
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
    api_instance = ugc_guard_python.WebhookLogsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Webhook Logs For Organization
        api_response = api_instance.get_webhook_logs_for_organization(organization_id, offset=offset, limit=limit)
        print("The response of WebhookLogsApi->get_webhook_logs_for_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookLogsApi->get_webhook_logs_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultWebhookLogBase**](PaginatedResultWebhookLogBase.md)

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


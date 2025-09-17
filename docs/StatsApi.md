# ugc_guard_python.StatsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compared_module_stats**](StatsApi.md#get_compared_module_stats) | **GET** /stats/module/{module_id}/compared | Get Module Stats Compared To Prior Date
[**get_module_stats**](StatsApi.md#get_module_stats) | **GET** /stats/module/{module_id} | Get Module Stats
[**get_organization_stats**](StatsApi.md#get_organization_stats) | **GET** /stats/org/{org_id} | Get Organization Stats


# **get_compared_module_stats**
> ComparedModuleState get_compared_module_stats(module_id, prior_date=prior_date)

Get Module Stats Compared To Prior Date

Get statistics for a module compared to a prior date.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.compared_module_state import ComparedModuleState
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
    api_instance = ugc_guard_python.StatsApi(api_client)
    module_id = 'module_id_example' # str | 
    prior_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Module Stats Compared To Prior Date
        api_response = api_instance.get_compared_module_stats(module_id, prior_date=prior_date)
        print("The response of StatsApi->get_compared_module_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_compared_module_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **prior_date** | **datetime**|  | [optional] 

### Return type

[**ComparedModuleState**](ComparedModuleState.md)

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

# **get_module_stats**
> ModuleStats get_module_stats(module_id, until=until)

Get Module Stats

Get statistics for a module.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.module_stats import ModuleStats
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
    api_instance = ugc_guard_python.StatsApi(api_client)
    module_id = 'module_id_example' # str | 
    until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Module Stats
        api_response = api_instance.get_module_stats(module_id, until=until)
        print("The response of StatsApi->get_module_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_module_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **until** | **datetime**|  | [optional] 

### Return type

[**ModuleStats**](ModuleStats.md)

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

# **get_organization_stats**
> object get_organization_stats(org_id)

Get Organization Stats

Get statistics for an organization.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
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
    api_instance = ugc_guard_python.StatsApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        # Get Organization Stats
        api_response = api_instance.get_organization_stats(org_id)
        print("The response of StatsApi->get_organization_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_organization_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

**object**

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


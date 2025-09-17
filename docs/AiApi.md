# ugc_guard_python.AiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_usage_costs_for_organization**](AiApi.md#get_ai_usage_costs_for_organization) | **GET** /ai/usage/{organization_id}/cost | Get The Ai Costs For Organization
[**get_all_ai_models**](AiApi.md#get_all_ai_models) | **GET** /ai/models | Get All Ai Models
[**get_all_ai_usage_for_organization**](AiApi.md#get_all_ai_usage_for_organization) | **GET** /ai/usage/{organization_id}/all | Get All Ai Usage For Organization
[**get_all_monthly_ai_usage_for_organization**](AiApi.md#get_all_monthly_ai_usage_for_organization) | **GET** /ai/usage/{organization_id} | Get All Monthly Ai Usage For Organization
[**get_monthly_ai_usage_for_organization_model**](AiApi.md#get_monthly_ai_usage_for_organization_model) | **GET** /ai/usage/{organization_id}/{ai_model} | Get Monthly Ai Usage For Organization And Model


# **get_ai_usage_costs_for_organization**
> AiUsageCosts get_ai_usage_costs_for_organization(organization_id)

Get The Ai Costs For Organization

Get the costs of all Models.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.ai_usage_costs import AiUsageCosts
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
    api_instance = ugc_guard_python.AiApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get The Ai Costs For Organization
        api_response = api_instance.get_ai_usage_costs_for_organization(organization_id)
        print("The response of AiApi->get_ai_usage_costs_for_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->get_ai_usage_costs_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**AiUsageCosts**](AiUsageCosts.md)

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

# **get_all_ai_models**
> List[AiModel] get_all_ai_models()

Get All Ai Models

Get a list of all available AI models.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.ai_model import AiModel
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
    api_instance = ugc_guard_python.AiApi(api_client)

    try:
        # Get All Ai Models
        api_response = api_instance.get_all_ai_models()
        print("The response of AiApi->get_all_ai_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->get_all_ai_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AiModel]**](AiModel.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ai_usage_for_organization**
> List[AIUsage] get_all_ai_usage_for_organization(organization_id)

Get All Ai Usage For Organization

Get all AI usage for a specific organization.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.ai_usage import AIUsage
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
    api_instance = ugc_guard_python.AiApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get All Ai Usage For Organization
        api_response = api_instance.get_all_ai_usage_for_organization(organization_id)
        print("The response of AiApi->get_all_ai_usage_for_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->get_all_ai_usage_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[AIUsage]**](AIUsage.md)

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

# **get_all_monthly_ai_usage_for_organization**
> List[AIUsage] get_all_monthly_ai_usage_for_organization(organization_id, month=month)

Get All Monthly Ai Usage For Organization

Get all monthly AI usage for a specific organization.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.ai_usage import AIUsage
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
    api_instance = ugc_guard_python.AiApi(api_client)
    organization_id = 'organization_id_example' # str | 
    month = '2013-10-20' # date |  (optional)

    try:
        # Get All Monthly Ai Usage For Organization
        api_response = api_instance.get_all_monthly_ai_usage_for_organization(organization_id, month=month)
        print("The response of AiApi->get_all_monthly_ai_usage_for_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->get_all_monthly_ai_usage_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **month** | **date**|  | [optional] 

### Return type

[**List[AIUsage]**](AIUsage.md)

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

# **get_monthly_ai_usage_for_organization_model**
> List[AIUsage] get_monthly_ai_usage_for_organization_model(organization_id, ai_model, month=month)

Get Monthly Ai Usage For Organization And Model

Get monthly AI usage for a specific organization and AI model.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.ai_usage import AIUsage
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
    api_instance = ugc_guard_python.AiApi(api_client)
    organization_id = 'organization_id_example' # str | 
    ai_model = 'ai_model_example' # str | 
    month = '2013-10-20' # date |  (optional)

    try:
        # Get Monthly Ai Usage For Organization And Model
        api_response = api_instance.get_monthly_ai_usage_for_organization_model(organization_id, ai_model, month=month)
        print("The response of AiApi->get_monthly_ai_usage_for_organization_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->get_monthly_ai_usage_for_organization_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **ai_model** | **str**|  | 
 **month** | **date**|  | [optional] 

### Return type

[**List[AIUsage]**](AIUsage.md)

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


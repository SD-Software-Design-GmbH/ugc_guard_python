# ugc_guard_python.ReportFormsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report_form**](ReportFormsApi.md#create_report_form) | **POST** /report_forms/ | Create Report Form
[**delete_report_form**](ReportFormsApi.md#delete_report_form) | **DELETE** /report_forms/{report_form_id} | Delete Report Form
[**get_report_form**](ReportFormsApi.md#get_report_form) | **GET** /report_forms/{report_form_id} | Get Report Form
[**get_report_forms_for_module**](ReportFormsApi.md#get_report_forms_for_module) | **GET** /report_forms/module/{module_id} | Get Report Forms For Module
[**update_report_form**](ReportFormsApi.md#update_report_form) | **PUT** /report_forms/{report_form_id} | Update Report Form


# **create_report_form**
> ReportForm create_report_form(report_form_base)

Create Report Form

Create a new report form.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.report_form import ReportForm
from ugc_guard_python.models.report_form_base import ReportFormBase
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
    api_instance = ugc_guard_python.ReportFormsApi(api_client)
    report_form_base = ugc_guard_python.ReportFormBase() # ReportFormBase | 

    try:
        # Create Report Form
        api_response = api_instance.create_report_form(report_form_base)
        print("The response of ReportFormsApi->create_report_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportFormsApi->create_report_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_form_base** | [**ReportFormBase**](ReportFormBase.md)|  | 

### Return type

[**ReportForm**](ReportForm.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_form**
> object delete_report_form(report_form_id)

Delete Report Form

Delete a report form.

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
    api_instance = ugc_guard_python.ReportFormsApi(api_client)
    report_form_id = 'report_form_id_example' # str | 

    try:
        # Delete Report Form
        api_response = api_instance.delete_report_form(report_form_id)
        print("The response of ReportFormsApi->delete_report_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportFormsApi->delete_report_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_form_id** | **str**|  | 

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

# **get_report_form**
> ReportForm get_report_form(report_form_id, redirect_uri=redirect_uri)

Get Report Form

Get a report form by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.report_form import ReportForm
from ugc_guard_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ugc_guard_python.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ugc_guard_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ugc_guard_python.ReportFormsApi(api_client)
    report_form_id = 'report_form_id_example' # str | 
    redirect_uri = 'redirect_uri_example' # str |  (optional)

    try:
        # Get Report Form
        api_response = api_instance.get_report_form(report_form_id, redirect_uri=redirect_uri)
        print("The response of ReportFormsApi->get_report_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportFormsApi->get_report_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_form_id** | **str**|  | 
 **redirect_uri** | **str**|  | [optional] 

### Return type

[**ReportForm**](ReportForm.md)

### Authorization

No authorization required

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

# **get_report_forms_for_module**
> List[ReportForm] get_report_forms_for_module(module_id)

Get Report Forms For Module

Get all report forms for a specific module.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.report_form import ReportForm
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
    api_instance = ugc_guard_python.ReportFormsApi(api_client)
    module_id = 'module_id_example' # str | 

    try:
        # Get Report Forms For Module
        api_response = api_instance.get_report_forms_for_module(module_id)
        print("The response of ReportFormsApi->get_report_forms_for_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportFormsApi->get_report_forms_for_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 

### Return type

[**List[ReportForm]**](ReportForm.md)

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

# **update_report_form**
> ReportForm update_report_form(report_form_id, report_form_base)

Update Report Form

Update an existing report form.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.report_form import ReportForm
from ugc_guard_python.models.report_form_base import ReportFormBase
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
    api_instance = ugc_guard_python.ReportFormsApi(api_client)
    report_form_id = 'report_form_id_example' # str | 
    report_form_base = ugc_guard_python.ReportFormBase() # ReportFormBase | 

    try:
        # Update Report Form
        api_response = api_instance.update_report_form(report_form_id, report_form_base)
        print("The response of ReportFormsApi->update_report_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportFormsApi->update_report_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_form_id** | **str**|  | 
 **report_form_base** | [**ReportFormBase**](ReportFormBase.md)|  | 

### Return type

[**ReportForm**](ReportForm.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


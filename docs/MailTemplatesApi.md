# ugc_guard_python.MailTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mail_template**](MailTemplatesApi.md#create_mail_template) | **POST** /mail_templates/ | Create Mail Template
[**delete_mail_template**](MailTemplatesApi.md#delete_mail_template) | **DELETE** /mail_templates/{template_id} | Delete Mail Template
[**get_all_mail_templates_for_module_with_defaults**](MailTemplatesApi.md#get_all_mail_templates_for_module_with_defaults) | **GET** /mail_templates/modules/{module_id}/with_defaults | Get All Mail Templates For Module And All Defaults
[**get_mail_template_by_id**](MailTemplatesApi.md#get_mail_template_by_id) | **GET** /mail_templates/{template_id} | Get Mail Template By Id
[**get_mail_template_by_type**](MailTemplatesApi.md#get_mail_template_by_type) | **GET** /mail_templates/type/{template_type} | Get Mail Template By Type
[**get_mail_templates_for_module**](MailTemplatesApi.md#get_mail_templates_for_module) | **GET** /mail_templates/modules/{module_id} | Get Mail Templates For Module
[**update_mail_template**](MailTemplatesApi.md#update_mail_template) | **PUT** /mail_templates/{template_id} | Update Mail Template


# **create_mail_template**
> MailTemplate create_mail_template(mail_template)

Create Mail Template

Create a new mail template.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.mail_template import MailTemplate
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
    api_instance = ugc_guard_python.MailTemplatesApi(api_client)
    mail_template = ugc_guard_python.MailTemplate() # MailTemplate | 

    try:
        # Create Mail Template
        api_response = api_instance.create_mail_template(mail_template)
        print("The response of MailTemplatesApi->create_mail_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->create_mail_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_template** | [**MailTemplate**](MailTemplate.md)|  | 

### Return type

[**MailTemplate**](MailTemplate.md)

### Authorization

No authorization required

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

# **delete_mail_template**
> bool delete_mail_template(template_id)

Delete Mail Template

Delete a mail template by its ID.

### Example


```python
import ugc_guard_python
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
    api_instance = ugc_guard_python.MailTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Delete Mail Template
        api_response = api_instance.delete_mail_template(template_id)
        print("The response of MailTemplatesApi->delete_mail_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->delete_mail_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

**bool**

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

# **get_all_mail_templates_for_module_with_defaults**
> MailTemplatesWithDefaults get_all_mail_templates_for_module_with_defaults(module_id, offset=offset, limit=limit)

Get All Mail Templates For Module And All Defaults

Get all mail templates for a specific module, including default templates.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.mail_templates_with_defaults import MailTemplatesWithDefaults
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
    api_instance = ugc_guard_python.MailTemplatesApi(api_client)
    module_id = 'module_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Mail Templates For Module And All Defaults
        api_response = api_instance.get_all_mail_templates_for_module_with_defaults(module_id, offset=offset, limit=limit)
        print("The response of MailTemplatesApi->get_all_mail_templates_for_module_with_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->get_all_mail_templates_for_module_with_defaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**MailTemplatesWithDefaults**](MailTemplatesWithDefaults.md)

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

# **get_mail_template_by_id**
> MailTemplate get_mail_template_by_id(template_id)

Get Mail Template By Id

Get a mail template by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.mail_template import MailTemplate
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
    api_instance = ugc_guard_python.MailTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Get Mail Template By Id
        api_response = api_instance.get_mail_template_by_id(template_id)
        print("The response of MailTemplatesApi->get_mail_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->get_mail_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**MailTemplate**](MailTemplate.md)

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

# **get_mail_template_by_type**
> MailTemplate get_mail_template_by_type(template_type, module_id)

Get Mail Template By Type

Get a mail template by its type.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.mail_template import MailTemplate
from ugc_guard_python.models.mail_template_type import MailTemplateType
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
    api_instance = ugc_guard_python.MailTemplatesApi(api_client)
    template_type = ugc_guard_python.MailTemplateType() # MailTemplateType | 
    module_id = 'module_id_example' # str | 

    try:
        # Get Mail Template By Type
        api_response = api_instance.get_mail_template_by_type(template_type, module_id)
        print("The response of MailTemplatesApi->get_mail_template_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->get_mail_template_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | [**MailTemplateType**](.md)|  | 
 **module_id** | **str**|  | 

### Return type

[**MailTemplate**](MailTemplate.md)

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

# **get_mail_templates_for_module**
> PaginatedResultMailTemplate get_mail_templates_for_module(module_id, offset=offset, limit=limit)

Get Mail Templates For Module

Get all mail templates for a specific module.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_mail_template import PaginatedResultMailTemplate
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
    api_instance = ugc_guard_python.MailTemplatesApi(api_client)
    module_id = 'module_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Mail Templates For Module
        api_response = api_instance.get_mail_templates_for_module(module_id, offset=offset, limit=limit)
        print("The response of MailTemplatesApi->get_mail_templates_for_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->get_mail_templates_for_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultMailTemplate**](PaginatedResultMailTemplate.md)

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

# **update_mail_template**
> MailTemplate update_mail_template(template_id, mail_template)

Update Mail Template

Update an existing mail template.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.mail_template import MailTemplate
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
    api_instance = ugc_guard_python.MailTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    mail_template = ugc_guard_python.MailTemplate() # MailTemplate | 

    try:
        # Update Mail Template
        api_response = api_instance.update_mail_template(template_id, mail_template)
        print("The response of MailTemplatesApi->update_mail_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->update_mail_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **mail_template** | [**MailTemplate**](MailTemplate.md)|  | 

### Return type

[**MailTemplate**](MailTemplate.md)

### Authorization

No authorization required

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


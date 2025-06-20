# ugc_guard_python.FilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /files/{file_id} | Delete File
[**download_file**](FilesApi.md#download_file) | **GET** /files/download/{file_id} | Download File
[**get_file_by_id**](FilesApi.md#get_file_by_id) | **GET** /files/{file_id} | Get File By Id
[**update_file**](FilesApi.md#update_file) | **PUT** /files/{file_id}/{secret} | Update File
[**upload_file**](FilesApi.md#upload_file) | **POST** /files/upload | Upload File


# **delete_file**
> File delete_file(file_id)

Delete File

Delete a file.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.file import File
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
    api_instance = ugc_guard_python.FilesApi(api_client)
    file_id = 'file_id_example' # str | 

    try:
        # Delete File
        api_response = api_instance.delete_file(file_id)
        print("The response of FilesApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 

### Return type

[**File**](File.md)

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

# **download_file**
> download_file(file_id, secret=secret)

Download File

Download a file.

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
    api_instance = ugc_guard_python.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    secret = 'secret_example' # str |  (optional)

    try:
        # Download File
        api_instance.download_file(file_id, secret=secret)
    except Exception as e:
        print("Exception when calling FilesApi->download_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **secret** | **str**|  | [optional] 

### Return type

void (empty response body)

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

# **get_file_by_id**
> File get_file_by_id(file_id, secret=secret)

Get File By Id

Get a file by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.file import File
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
    api_instance = ugc_guard_python.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    secret = 'secret_example' # str |  (optional)

    try:
        # Get File By Id
        api_response = api_instance.get_file_by_id(file_id, secret=secret)
        print("The response of FilesApi->get_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **secret** | **str**|  | [optional] 

### Return type

[**File**](File.md)

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

# **update_file**
> File update_file(file_id, secret, file)

Update File

Update a file.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.file import File
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
    api_instance = ugc_guard_python.FilesApi(api_client)
    file_id = 'file_id_example' # str | 
    secret = 'secret_example' # str | 
    file = '/path/to/file' # File | 

    try:
        # Update File
        api_response = api_instance.update_file(file_id, secret, file)
        print("The response of FilesApi->update_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**|  | 
 **secret** | **str**|  | 
 **file** | [**File**](File.md)|  | 

### Return type

[**File**](File.md)

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

# **upload_file**
> File upload_file(module_id, upload_file, secret=secret)

Upload File

Upload a file.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.file import File
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
    api_instance = ugc_guard_python.FilesApi(api_client)
    module_id = 'module_id_example' # str | 
    upload_file = None # bytearray | 
    secret = 'secret_example' # str |  (optional)

    try:
        # Upload File
        api_response = api_instance.upload_file(module_id, upload_file, secret=secret)
        print("The response of FilesApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **upload_file** | **bytearray**|  | 
 **secret** | **str**|  | [optional] 

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


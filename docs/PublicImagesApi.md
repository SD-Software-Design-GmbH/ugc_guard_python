# ugc_guard_python.PublicImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_public_image**](PublicImagesApi.md#delete_public_image) | **DELETE** /public_images/{public_image_id} | Delete Public Image
[**download_public_image**](PublicImagesApi.md#download_public_image) | **GET** /public_images/download/{public_image_id} | Download Public Image
[**get_public_image_by_id**](PublicImagesApi.md#get_public_image_by_id) | **GET** /public_images/{public_image_id} | Get Public Image By Id
[**get_public_images_by_user_id**](PublicImagesApi.md#get_public_images_by_user_id) | **GET** /public_images/myself | Get Public Images By User Id
[**upload_public_image**](PublicImagesApi.md#upload_public_image) | **POST** /public_images/upload | Upload Public Image


# **delete_public_image**
> object delete_public_image(public_image_id)

Delete Public Image

Delete a public image by its ID.

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
    api_instance = ugc_guard_python.PublicImagesApi(api_client)
    public_image_id = 'public_image_id_example' # str | 

    try:
        # Delete Public Image
        api_response = api_instance.delete_public_image(public_image_id)
        print("The response of PublicImagesApi->delete_public_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicImagesApi->delete_public_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_image_id** | **str**|  | 

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

# **download_public_image**
> object download_public_image(public_image_id)

Download Public Image

Download a public image by its ID.

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
    api_instance = ugc_guard_python.PublicImagesApi(api_client)
    public_image_id = 'public_image_id_example' # str | 

    try:
        # Download Public Image
        api_response = api_instance.download_public_image(public_image_id)
        print("The response of PublicImagesApi->download_public_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicImagesApi->download_public_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_image_id** | **str**|  | 

### Return type

**object**

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

# **get_public_image_by_id**
> PublicImage get_public_image_by_id(public_image_id)

Get Public Image By Id

Get a public image by its ID.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.public_image import PublicImage
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
    api_instance = ugc_guard_python.PublicImagesApi(api_client)
    public_image_id = 'public_image_id_example' # str | 

    try:
        # Get Public Image By Id
        api_response = api_instance.get_public_image_by_id(public_image_id)
        print("The response of PublicImagesApi->get_public_image_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicImagesApi->get_public_image_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_image_id** | **str**|  | 

### Return type

[**PublicImage**](PublicImage.md)

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

# **get_public_images_by_user_id**
> PaginatedResultPublicImage get_public_images_by_user_id(offset=offset, limit=limit)

Get Public Images By User Id

Retrieve all public images uploaded by the current user.

:param session: The database session for CRUD operations.
:param current_user: The currently authenticated user.
:param offset: The number of items to skip before starting to collect the result set.
:param limit: The maximum number of items to return.

:raises HTTPException: If the user is not authenticated.
:return: A PaginatedResult containing the count and the list of PublicImage objects.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_public_image import PaginatedResultPublicImage
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
    api_instance = ugc_guard_python.PublicImagesApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Public Images By User Id
        api_response = api_instance.get_public_images_by_user_id(offset=offset, limit=limit)
        print("The response of PublicImagesApi->get_public_images_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicImagesApi->get_public_images_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultPublicImage**](PaginatedResultPublicImage.md)

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

# **upload_public_image**
> PublicImage upload_public_image(upload_file)

Upload Public Image

Upload a public image.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.public_image import PublicImage
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
    api_instance = ugc_guard_python.PublicImagesApi(api_client)
    upload_file = None # bytearray | 

    try:
        # Upload Public Image
        api_response = api_instance.upload_public_image(upload_file)
        print("The response of PublicImagesApi->upload_public_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicImagesApi->upload_public_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_file** | **bytearray**|  | 

### Return type

[**PublicImage**](PublicImage.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

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


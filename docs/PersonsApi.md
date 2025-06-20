# ugc_guard_python.PersonsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_person**](PersonsApi.md#create_person) | **POST** /persons/ | Create Person
[**delete_person**](PersonsApi.md#delete_person) | **DELETE** /persons/{person_id} | Delete Person
[**get_person_by_id**](PersonsApi.md#get_person_by_id) | **GET** /persons/{person_id} | Get Person By Id
[**get_person_by_upi_id**](PersonsApi.md#get_person_by_upi_id) | **GET** /persons/by_upid/{upi_id} | Get Person By Upi Id
[**update_person**](PersonsApi.md#update_person) | **PUT** /persons/ | Update Person


# **create_person**
> AnonymousPerson create_person(person_db, secret=secret)

Create Person

Create a new person.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.anonymous_person import AnonymousPerson
from ugc_guard_python.models.person_db import PersonDB
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
    api_instance = ugc_guard_python.PersonsApi(api_client)
    person_db = ugc_guard_python.PersonDB() # PersonDB | 
    secret = 'secret_example' # str |  (optional)

    try:
        # Create Person
        api_response = api_instance.create_person(person_db, secret=secret)
        print("The response of PersonsApi->create_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->create_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_db** | [**PersonDB**](PersonDB.md)|  | 
 **secret** | **str**|  | [optional] 

### Return type

[**AnonymousPerson**](AnonymousPerson.md)

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

# **delete_person**
> PersonDB delete_person(person_id)

Delete Person

Delete a person by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.person_db import PersonDB
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
    api_instance = ugc_guard_python.PersonsApi(api_client)
    person_id = 'person_id_example' # str | 

    try:
        # Delete Person
        api_response = api_instance.delete_person(person_id)
        print("The response of PersonsApi->delete_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->delete_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**|  | 

### Return type

[**PersonDB**](PersonDB.md)

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

# **get_person_by_id**
> PersonDB get_person_by_id(person_id)

Get Person By Id

Get a person by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.person_db import PersonDB
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
    api_instance = ugc_guard_python.PersonsApi(api_client)
    person_id = 'person_id_example' # str | 

    try:
        # Get Person By Id
        api_response = api_instance.get_person_by_id(person_id)
        print("The response of PersonsApi->get_person_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_person_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**|  | 

### Return type

[**PersonDB**](PersonDB.md)

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

# **get_person_by_upi_id**
> AnonymousPerson get_person_by_upi_id(upi_id, module_id, secret=secret)

Get Person By Upi Id

Get a person by its Unique Partner ID

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.anonymous_person import AnonymousPerson
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
    api_instance = ugc_guard_python.PersonsApi(api_client)
    upi_id = 'upi_id_example' # str | 
    module_id = 'module_id_example' # str | 
    secret = 'secret_example' # str |  (optional)

    try:
        # Get Person By Upi Id
        api_response = api_instance.get_person_by_upi_id(upi_id, module_id, secret=secret)
        print("The response of PersonsApi->get_person_by_upi_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_person_by_upi_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upi_id** | **str**|  | 
 **module_id** | **str**|  | 
 **secret** | **str**|  | [optional] 

### Return type

[**AnonymousPerson**](AnonymousPerson.md)

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

# **update_person**
> PersonDB update_person(person_db)

Update Person

Update a person.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.person_db import PersonDB
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
    api_instance = ugc_guard_python.PersonsApi(api_client)
    person_db = ugc_guard_python.PersonDB() # PersonDB | 

    try:
        # Update Person
        api_response = api_instance.update_person(person_db)
        print("The response of PersonsApi->update_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->update_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_db** | [**PersonDB**](PersonDB.md)|  | 

### Return type

[**PersonDB**](PersonDB.md)

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


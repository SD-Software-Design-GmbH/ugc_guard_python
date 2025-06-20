# ugc_guard_python.ActionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_action**](ActionsApi.md#create_action) | **POST** /actions/ | Create Action
[**delete_action**](ActionsApi.md#delete_action) | **DELETE** /actions/{action_id} | Delete Action
[**get_action_by_id**](ActionsApi.md#get_action_by_id) | **GET** /actions/{action_id} | Get Action By Id
[**get_all_actions_of_type**](ActionsApi.md#get_all_actions_of_type) | **GET** /actions/ | Get All Actions Of Type
[**get_user_type_action_by_id**](ActionsApi.md#get_user_type_action_by_id) | **GET** /actions/user_type/{module_id} | Get User Type Action By Id
[**perform_action**](ActionsApi.md#perform_action) | **GET** /actions/{action_id}/perform | Perform Action
[**update_action**](ActionsApi.md#update_action) | **PUT** /actions/ | Update Action


# **create_action**
> Action create_action(action)

Create Action

Create a new action.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.action import Action
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
    api_instance = ugc_guard_python.ActionsApi(api_client)
    action = ugc_guard_python.Action() # Action | 

    try:
        # Create Action
        api_response = api_instance.create_action(action)
        print("The response of ActionsApi->create_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->create_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**Action**](Action.md)|  | 

### Return type

[**Action**](Action.md)

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

# **delete_action**
> Action delete_action(action_id)

Delete Action

Delete an action by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.action import Action
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
    api_instance = ugc_guard_python.ActionsApi(api_client)
    action_id = 'action_id_example' # str | 

    try:
        # Delete Action
        api_response = api_instance.delete_action(action_id)
        print("The response of ActionsApi->delete_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->delete_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 

### Return type

[**Action**](Action.md)

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

# **get_action_by_id**
> Action get_action_by_id(action_id)

Get Action By Id

Get an action by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.action import Action
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
    api_instance = ugc_guard_python.ActionsApi(api_client)
    action_id = 'action_id_example' # str | 

    try:
        # Get Action By Id
        api_response = api_instance.get_action_by_id(action_id)
        print("The response of ActionsApi->get_action_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_action_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 

### Return type

[**Action**](Action.md)

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

# **get_all_actions_of_type**
> List[Action] get_all_actions_of_type(type_id, offset=offset, limit=limit)

Get All Actions Of Type

Get all actions of a type.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.action import Action
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
    api_instance = ugc_guard_python.ActionsApi(api_client)
    type_id = 'type_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Actions Of Type
        api_response = api_instance.get_all_actions_of_type(type_id, offset=offset, limit=limit)
        print("The response of ActionsApi->get_all_actions_of_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_all_actions_of_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Action]**](Action.md)

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

# **get_user_type_action_by_id**
> List[Action] get_user_type_action_by_id(module_id)

Get User Type Action By Id

Gets all actions that belong to the user type of the module

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.action import Action
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
    api_instance = ugc_guard_python.ActionsApi(api_client)
    module_id = 'module_id_example' # str | 

    try:
        # Get User Type Action By Id
        api_response = api_instance.get_user_type_action_by_id(module_id)
        print("The response of ActionsApi->get_user_type_action_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_user_type_action_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 

### Return type

[**List[Action]**](Action.md)

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

# **perform_action**
> Action perform_action(action_id, content_id, on_user=on_user)

Perform Action

Perform an action.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.action import Action
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
    api_instance = ugc_guard_python.ActionsApi(api_client)
    action_id = 'action_id_example' # str | 
    content_id = 'content_id_example' # str | 
    on_user = False # bool |  (optional) (default to False)

    try:
        # Perform Action
        api_response = api_instance.perform_action(action_id, content_id, on_user=on_user)
        print("The response of ActionsApi->perform_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->perform_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 
 **content_id** | **str**|  | 
 **on_user** | **bool**|  | [optional] [default to False]

### Return type

[**Action**](Action.md)

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

# **update_action**
> Action update_action(action)

Update Action

Update an action.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.action import Action
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
    api_instance = ugc_guard_python.ActionsApi(api_client)
    action = ugc_guard_python.Action() # Action | 

    try:
        # Update Action
        api_response = api_instance.update_action(action)
        print("The response of ActionsApi->update_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->update_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**Action**](Action.md)|  | 

### Return type

[**Action**](Action.md)

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


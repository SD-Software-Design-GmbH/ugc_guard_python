# ugc_guard_python.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel**](UsersApi.md#create_channel) | **POST** /users/channels | Create Channel
[**delete_channel**](UsersApi.md#delete_channel) | **DELETE** /users/channels/{channel_id} | Delete Channel
[**get_channel_by_id**](UsersApi.md#get_channel_by_id) | **GET** /users/channels/by_id/{channel_id} | Get Channel By Id
[**get_channel_by_id_or_name**](UsersApi.md#get_channel_by_id_or_name) | **GET** /users/channels/by_id_or_name/{id_or_name} | Get Channel By Id Or Name
[**get_channels_of_current_user**](UsersApi.md#get_channels_of_current_user) | **GET** /users/my/channels | Get Channels Of Current User
[**get_channels_of_user**](UsersApi.md#get_channels_of_user) | **GET** /users/{user_id}/channels | Get Channels Of User
[**get_channels_of_user_users_channels_of_user_id_get**](UsersApi.md#get_channels_of_user_users_channels_of_user_id_get) | **GET** /users/channels/of/{user_id} | Get Channels Of User
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /users/myself | Get Current User
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{user_id} | Get User By Id
[**get_users_of_channel**](UsersApi.md#get_users_of_channel) | **GET** /users/channels/{channel_id}/users | Get Users Of Channel
[**join_channel**](UsersApi.md#join_channel) | **POST** /users/channels/{channel_id}/join | Join Channel
[**join_channel_by_email**](UsersApi.md#join_channel_by_email) | **POST** /users/channels/{channel_id}/join_by_email | Join Channel By Email
[**leave_channel**](UsersApi.md#leave_channel) | **POST** /users/channels/{channel_id}/leave | Leave Channel
[**update_channel**](UsersApi.md#update_channel) | **PUT** /users/channels/{channel_id} | Update Channel


# **create_channel**
> Channel create_channel(channel)

Create Channel

Create a new channel.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.channel import Channel
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    channel = ugc_guard_python.Channel() # Channel | 

    try:
        # Create Channel
        api_response = api_instance.create_channel(channel)
        print("The response of UsersApi->create_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | [**Channel**](Channel.md)|  | 

### Return type

[**Channel**](Channel.md)

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

# **delete_channel**
> bool delete_channel(channel_id)

Delete Channel

Delete a channel by its ID.

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
    api_instance = ugc_guard_python.UsersApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        # Delete Channel
        api_response = api_instance.delete_channel(channel_id)
        print("The response of UsersApi->delete_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

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

# **get_channel_by_id**
> Channel get_channel_by_id(channel_id)

Get Channel By Id

Get a channel by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.channel import Channel
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        # Get Channel By Id
        api_response = api_instance.get_channel_by_id(channel_id)
        print("The response of UsersApi->get_channel_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_channel_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**Channel**](Channel.md)

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

# **get_channel_by_id_or_name**
> Channel get_channel_by_id_or_name(id_or_name)

Get Channel By Id Or Name

Get a channel by its ID or name.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.channel import Channel
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    id_or_name = 'id_or_name_example' # str | 

    try:
        # Get Channel By Id Or Name
        api_response = api_instance.get_channel_by_id_or_name(id_or_name)
        print("The response of UsersApi->get_channel_by_id_or_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_channel_by_id_or_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**|  | 

### Return type

[**Channel**](Channel.md)

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

# **get_channels_of_current_user**
> PaginatedResultChannel get_channels_of_current_user(offset=offset, limit=limit)

Get Channels Of Current User

Get the channels of the current user.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_channel import PaginatedResultChannel
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Channels Of Current User
        api_response = api_instance.get_channels_of_current_user(offset=offset, limit=limit)
        print("The response of UsersApi->get_channels_of_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_channels_of_current_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultChannel**](PaginatedResultChannel.md)

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

# **get_channels_of_user**
> PaginatedResultChannel get_channels_of_user(user_id, limit=limit, offset=offset)

Get Channels Of User

Get the channels of a user.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_channel import PaginatedResultChannel
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Channels Of User
        api_response = api_instance.get_channels_of_user(user_id, limit=limit, offset=offset)
        print("The response of UsersApi->get_channels_of_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_channels_of_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PaginatedResultChannel**](PaginatedResultChannel.md)

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

# **get_channels_of_user_users_channels_of_user_id_get**
> PaginatedResultChannel get_channels_of_user_users_channels_of_user_id_get(user_id, limit=limit, offset=offset)

Get Channels Of User

Get the channels of a user.
:param user_id: The ID of the user
:param session: Database session
:param current_user: Current user
:param limit: Limit for pagination
:param offset: Offset for pagination
:return: Dictionary containing the channels of the user

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_channel import PaginatedResultChannel
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Channels Of User
        api_response = api_instance.get_channels_of_user_users_channels_of_user_id_get(user_id, limit=limit, offset=offset)
        print("The response of UsersApi->get_channels_of_user_users_channels_of_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_channels_of_user_users_channels_of_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PaginatedResultChannel**](PaginatedResultChannel.md)

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

# **get_current_user**
> UserBase get_current_user()

Get Current User

Get the current user.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.user_base import UserBase
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
    api_instance = ugc_guard_python.UsersApi(api_client)

    try:
        # Get Current User
        api_response = api_instance.get_current_user()
        print("The response of UsersApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserBase**](UserBase.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserBase get_user_by_id(user_id)

Get User By Id

Get a user by their ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.user_base import UserBase
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User By Id
        api_response = api_instance.get_user_by_id(user_id)
        print("The response of UsersApi->get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserBase**](UserBase.md)

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

# **get_users_of_channel**
> PaginatedResultUserBase get_users_of_channel(channel_id, limit=limit, offset=offset)

Get Users Of Channel

Get the users of a channel by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_user_base import PaginatedResultUserBase
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    channel_id = 'channel_id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Users Of Channel
        api_response = api_instance.get_users_of_channel(channel_id, limit=limit, offset=offset)
        print("The response of UsersApi->get_users_of_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_of_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PaginatedResultUserBase**](PaginatedResultUserBase.md)

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

# **join_channel**
> ChannelUser join_channel(channel_id, user_id)

Join Channel

Join a channel by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.channel_user import ChannelUser
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    channel_id = 'channel_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Join Channel
        api_response = api_instance.join_channel(channel_id, user_id)
        print("The response of UsersApi->join_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->join_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ChannelUser**](ChannelUser.md)

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

# **join_channel_by_email**
> ChannelUser join_channel_by_email(channel_id, email)

Join Channel By Email

Join a channel by its ID using email.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.channel_user import ChannelUser
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    channel_id = 'channel_id_example' # str | 
    email = 'email_example' # str | 

    try:
        # Join Channel By Email
        api_response = api_instance.join_channel_by_email(channel_id, email)
        print("The response of UsersApi->join_channel_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->join_channel_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **email** | **str**|  | 

### Return type

[**ChannelUser**](ChannelUser.md)

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

# **leave_channel**
> bool leave_channel(channel_id, user_id=user_id)

Leave Channel

Leave a channel by its ID.

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
    api_instance = ugc_guard_python.UsersApi(api_client)
    channel_id = 'channel_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Leave Channel
        api_response = api_instance.leave_channel(channel_id, user_id=user_id)
        print("The response of UsersApi->leave_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->leave_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 

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

# **update_channel**
> Channel update_channel(channel_id, channel)

Update Channel

Update an existing channel.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.channel import Channel
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
    api_instance = ugc_guard_python.UsersApi(api_client)
    channel_id = 'channel_id_example' # str | 
    channel = ugc_guard_python.Channel() # Channel | 

    try:
        # Update Channel
        api_response = api_instance.update_channel(channel_id, channel)
        print("The response of UsersApi->update_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **channel** | [**Channel**](Channel.md)|  | 

### Return type

[**Channel**](Channel.md)

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


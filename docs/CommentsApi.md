# ugc_guard_python.CommentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](CommentsApi.md#create_comment) | **POST** /comments/ | Create Comment
[**delete_comment**](CommentsApi.md#delete_comment) | **DELETE** /comments/{comment_id} | Delete Comment
[**get_comment_by_id**](CommentsApi.md#get_comment_by_id) | **GET** /comments/{comment_id} | Get Comment By Id
[**get_comments_by_content_id**](CommentsApi.md#get_comments_by_content_id) | **GET** /comments/content/{content_id} | Get Comments By Content Id
[**get_comments_by_report_id**](CommentsApi.md#get_comments_by_report_id) | **GET** /comments/report/{report_id} | Get Comments By Report Id
[**update_comment**](CommentsApi.md#update_comment) | **POST** /comments/{comment_id} | Update Comment


# **create_comment**
> Comment create_comment(comment)

Create Comment

Create a new comment.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.comment import Comment
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
    api_instance = ugc_guard_python.CommentsApi(api_client)
    comment = ugc_guard_python.Comment() # Comment | 

    try:
        # Create Comment
        api_response = api_instance.create_comment(comment)
        print("The response of CommentsApi->create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->create_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

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

# **delete_comment**
> object delete_comment(comment_id)

Delete Comment

Delete a comment.

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
    api_instance = ugc_guard_python.CommentsApi(api_client)
    comment_id = 'comment_id_example' # str | 

    try:
        # Delete Comment
        api_response = api_instance.delete_comment(comment_id)
        print("The response of CommentsApi->delete_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->delete_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 

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

# **get_comment_by_id**
> CommentWithCreator get_comment_by_id(comment_id)

Get Comment By Id

Get a comment by its ID.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.comment_with_creator import CommentWithCreator
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
    api_instance = ugc_guard_python.CommentsApi(api_client)
    comment_id = 'comment_id_example' # str | 

    try:
        # Get Comment By Id
        api_response = api_instance.get_comment_by_id(comment_id)
        print("The response of CommentsApi->get_comment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_comment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 

### Return type

[**CommentWithCreator**](CommentWithCreator.md)

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

# **get_comments_by_content_id**
> PaginatedResultCommentWithCreator get_comments_by_content_id(content_id, offset=offset, limit=limit)

Get Comments By Content Id

Get all comments associated with a specific content ID.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_comment_with_creator import PaginatedResultCommentWithCreator
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
    api_instance = ugc_guard_python.CommentsApi(api_client)
    content_id = 'content_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Comments By Content Id
        api_response = api_instance.get_comments_by_content_id(content_id, offset=offset, limit=limit)
        print("The response of CommentsApi->get_comments_by_content_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_comments_by_content_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultCommentWithCreator**](PaginatedResultCommentWithCreator.md)

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

# **get_comments_by_report_id**
> PaginatedResultCommentWithCreator get_comments_by_report_id(report_id, secret=secret, offset=offset, limit=limit)

Get Comments By Report Id

Get all comments associated with a specific report ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_comment_with_creator import PaginatedResultCommentWithCreator
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
    api_instance = ugc_guard_python.CommentsApi(api_client)
    report_id = 'report_id_example' # str | 
    secret = 'secret_example' # str |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Comments By Report Id
        api_response = api_instance.get_comments_by_report_id(report_id, secret=secret, offset=offset, limit=limit)
        print("The response of CommentsApi->get_comments_by_report_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_comments_by_report_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **secret** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultCommentWithCreator**](PaginatedResultCommentWithCreator.md)

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

# **update_comment**
> CommentWithCreator update_comment(comment_id, comment)

Update Comment

Update a comment.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.comment import Comment
from ugc_guard_python.models.comment_with_creator import CommentWithCreator
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
    api_instance = ugc_guard_python.CommentsApi(api_client)
    comment_id = 'comment_id_example' # str | 
    comment = ugc_guard_python.Comment() # Comment | 

    try:
        # Update Comment
        api_response = api_instance.update_comment(comment_id, comment)
        print("The response of CommentsApi->update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->update_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **comment** | [**Comment**](Comment.md)|  | 

### Return type

[**CommentWithCreator**](CommentWithCreator.md)

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


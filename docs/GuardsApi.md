# ugc_guard_python.GuardsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_guard**](GuardsApi.md#create_guard) | **POST** /guards/ | Create Guard
[**delete_guard**](GuardsApi.md#delete_guard) | **DELETE** /guards/{guard_id} | Delete Guard
[**enqueue_guard_evaluation**](GuardsApi.md#enqueue_guard_evaluation) | **POST** /guards/{guard_id}/enqueue | Enqueue Guard Evaluation
[**estimate_tokens_for_guard**](GuardsApi.md#estimate_tokens_for_guard) | **POST** /guards/{guard_id}/estimate | Estimate Tokens For Guard
[**get_guard**](GuardsApi.md#get_guard) | **GET** /guards/{guard_id} | Get Guard
[**get_guard_evaluation**](GuardsApi.md#get_guard_evaluation) | **GET** /guards/results/{evaluation_id} | Get Guard Evaluation
[**get_guard_evaluation_stats**](GuardsApi.md#get_guard_evaluation_stats) | **GET** /guards/results/stats | Get Guard Evaluation Stats
[**link_rule_to_guard**](GuardsApi.md#link_rule_to_guard) | **POST** /guards/{guard_id}/link/{rule_id} | Link Rule To Guard
[**list_guard_evaluations**](GuardsApi.md#list_guard_evaluations) | **GET** /guards/results/ | List Guard Evaluations
[**list_guards**](GuardsApi.md#list_guards) | **GET** /guards/ | List Guards
[**unlink_rule_from_guard**](GuardsApi.md#unlink_rule_from_guard) | **DELETE** /guards/{guard_id}/link/{rule_id} | Unlink Rule From Guard
[**update_guard**](GuardsApi.md#update_guard) | **PUT** /guards/{guard_id} | Update Guard
[**update_running_order_of_guard**](GuardsApi.md#update_running_order_of_guard) | **POST** /guards/{guard_id}/updateRO | Update Running Order Of Guard


# **create_guard**
> Guard create_guard(guard)

Create Guard

Create a new guard

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.guard import Guard
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard = ugc_guard_python.Guard() # Guard | 

    try:
        # Create Guard
        api_response = api_instance.create_guard(guard)
        print("The response of GuardsApi->create_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->create_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard** | [**Guard**](Guard.md)|  | 

### Return type

[**Guard**](Guard.md)

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

# **delete_guard**
> object delete_guard(guard_id)

Delete Guard

Delete a guard

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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str | 

    try:
        # Delete Guard
        api_response = api_instance.delete_guard(guard_id)
        print("The response of GuardsApi->delete_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->delete_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 

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

# **enqueue_guard_evaluation**
> GuardEvaluation enqueue_guard_evaluation(guard_id, body_enqueue_guard_evaluation, type_id=type_id, module_secret=module_secret)

Enqueue Guard Evaluation

Enqueue a guard evaluation to be processed asynchronously

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.body_enqueue_guard_evaluation import BodyEnqueueGuardEvaluation
from ugc_guard_python.models.guard_evaluation import GuardEvaluation
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str | 
    body_enqueue_guard_evaluation = ugc_guard_python.BodyEnqueueGuardEvaluation() # BodyEnqueueGuardEvaluation | 
    type_id = 'type_id_example' # str |  (optional)
    module_secret = 'module_secret_example' # str |  (optional)

    try:
        # Enqueue Guard Evaluation
        api_response = api_instance.enqueue_guard_evaluation(guard_id, body_enqueue_guard_evaluation, type_id=type_id, module_secret=module_secret)
        print("The response of GuardsApi->enqueue_guard_evaluation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->enqueue_guard_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 
 **body_enqueue_guard_evaluation** | [**BodyEnqueueGuardEvaluation**](BodyEnqueueGuardEvaluation.md)|  | 
 **type_id** | **str**|  | [optional] 
 **module_secret** | **str**|  | [optional] 

### Return type

[**GuardEvaluation**](GuardEvaluation.md)

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

# **estimate_tokens_for_guard**
> TokenEstimationResult estimate_tokens_for_guard(guard_id, body_estimate_tokens_for_guard, ai_model=ai_model)

Estimate Tokens For Guard

Estimates how many AI Tokens would be used to run this guard on the given content and context

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.body_estimate_tokens_for_guard import BodyEstimateTokensForGuard
from ugc_guard_python.models.token_estimation_result import TokenEstimationResult
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str | 
    body_estimate_tokens_for_guard = ugc_guard_python.BodyEstimateTokensForGuard() # BodyEstimateTokensForGuard | 
    ai_model = 'ai_model_example' # str |  (optional)

    try:
        # Estimate Tokens For Guard
        api_response = api_instance.estimate_tokens_for_guard(guard_id, body_estimate_tokens_for_guard, ai_model=ai_model)
        print("The response of GuardsApi->estimate_tokens_for_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->estimate_tokens_for_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 
 **body_estimate_tokens_for_guard** | [**BodyEstimateTokensForGuard**](BodyEstimateTokensForGuard.md)|  | 
 **ai_model** | **str**|  | [optional] 

### Return type

[**TokenEstimationResult**](TokenEstimationResult.md)

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

# **get_guard**
> FilledGuard get_guard(guard_id)

Get Guard

Get a guard by ID

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.filled_guard import FilledGuard
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str | 

    try:
        # Get Guard
        api_response = api_instance.get_guard(guard_id)
        print("The response of GuardsApi->get_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->get_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 

### Return type

[**FilledGuard**](FilledGuard.md)

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

# **get_guard_evaluation**
> FilledGuardEvaluation get_guard_evaluation(evaluation_id, module_secret=module_secret)

Get Guard Evaluation

Get the result of a guard evaluation by its ID

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.filled_guard_evaluation import FilledGuardEvaluation
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    evaluation_id = 'evaluation_id_example' # str | 
    module_secret = 'module_secret_example' # str |  (optional)

    try:
        # Get Guard Evaluation
        api_response = api_instance.get_guard_evaluation(evaluation_id, module_secret=module_secret)
        print("The response of GuardsApi->get_guard_evaluation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->get_guard_evaluation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation_id** | **str**|  | 
 **module_secret** | **str**|  | [optional] 

### Return type

[**FilledGuardEvaluation**](FilledGuardEvaluation.md)

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

# **get_guard_evaluation_stats**
> GuardEvaluationUsageStats get_guard_evaluation_stats(guard_id=guard_id, module_id=module_id, lower_bound=lower_bound, upper_bound=upper_bound)

Get Guard Evaluation Stats

Get guard evaluation statistics

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.guard_evaluation_usage_stats import GuardEvaluationUsageStats
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str |  (optional)
    module_id = 'module_id_example' # str |  (optional)
    lower_bound = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    upper_bound = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Guard Evaluation Stats
        api_response = api_instance.get_guard_evaluation_stats(guard_id=guard_id, module_id=module_id, lower_bound=lower_bound, upper_bound=upper_bound)
        print("The response of GuardsApi->get_guard_evaluation_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->get_guard_evaluation_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | [optional] 
 **module_id** | **str**|  | [optional] 
 **lower_bound** | **datetime**|  | [optional] 
 **upper_bound** | **datetime**|  | [optional] 

### Return type

[**GuardEvaluationUsageStats**](GuardEvaluationUsageStats.md)

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

# **link_rule_to_guard**
> GuardRuleConnection link_rule_to_guard(guard_id, rule_id, position=position)

Link Rule To Guard

Link a rule to a guard

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.guard_rule_connection import GuardRuleConnection
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str | 
    rule_id = 'rule_id_example' # str | 
    position = 1 # int |  (optional) (default to 1)

    try:
        # Link Rule To Guard
        api_response = api_instance.link_rule_to_guard(guard_id, rule_id, position=position)
        print("The response of GuardsApi->link_rule_to_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->link_rule_to_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 
 **rule_id** | **str**|  | 
 **position** | **int**|  | [optional] [default to 1]

### Return type

[**GuardRuleConnection**](GuardRuleConnection.md)

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

# **list_guard_evaluations**
> PaginatedResultGuardEvaluation list_guard_evaluations(guard_id=guard_id, module_id=module_id, ongoing=ongoing, passed=passed, failed=failed, sort_by=sort_by, sort_order=sort_order, search_query=search_query, before=before, after=after, offset=offset, limit=limit)

List Guard Evaluations

Get paginated list of guard evaluations

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_guard_evaluation import PaginatedResultGuardEvaluation
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str |  (optional)
    module_id = 'module_id_example' # str |  (optional)
    ongoing = True # bool |  (optional)
    passed = True # bool |  (optional)
    failed = True # bool |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_order = 'sort_order_example' # str |  (optional)
    search_query = 'search_query_example' # str |  (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List Guard Evaluations
        api_response = api_instance.list_guard_evaluations(guard_id=guard_id, module_id=module_id, ongoing=ongoing, passed=passed, failed=failed, sort_by=sort_by, sort_order=sort_order, search_query=search_query, before=before, after=after, offset=offset, limit=limit)
        print("The response of GuardsApi->list_guard_evaluations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->list_guard_evaluations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | [optional] 
 **module_id** | **str**|  | [optional] 
 **ongoing** | **bool**|  | [optional] 
 **passed** | **bool**|  | [optional] 
 **failed** | **bool**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **search_query** | **str**|  | [optional] 
 **before** | **datetime**|  | [optional] 
 **after** | **datetime**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultGuardEvaluation**](PaginatedResultGuardEvaluation.md)

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

# **list_guards**
> PaginatedResultGuard list_guards(module_id, offset=offset, limit=limit)

List Guards

List all guards for a module

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_guard import PaginatedResultGuard
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    module_id = 'module_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List Guards
        api_response = api_instance.list_guards(module_id, offset=offset, limit=limit)
        print("The response of GuardsApi->list_guards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->list_guards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultGuard**](PaginatedResultGuard.md)

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

# **unlink_rule_from_guard**
> object unlink_rule_from_guard(guard_id, rule_id)

Unlink Rule From Guard

Unlink a rule from a guard

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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str | 
    rule_id = 'rule_id_example' # str | 

    try:
        # Unlink Rule From Guard
        api_response = api_instance.unlink_rule_from_guard(guard_id, rule_id)
        print("The response of GuardsApi->unlink_rule_from_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->unlink_rule_from_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 
 **rule_id** | **str**|  | 

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

# **update_guard**
> Guard update_guard(guard_id, guard)

Update Guard

Update a guard

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.guard import Guard
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str | 
    guard = ugc_guard_python.Guard() # Guard | 

    try:
        # Update Guard
        api_response = api_instance.update_guard(guard_id, guard)
        print("The response of GuardsApi->update_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->update_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 
 **guard** | [**Guard**](Guard.md)|  | 

### Return type

[**Guard**](Guard.md)

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

# **update_running_order_of_guard**
> FilledGuard update_running_order_of_guard(guard_id, request_body)

Update Running Order Of Guard

Given all rule ids in the correct order, update the running order of the rules in the guard

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.filled_guard import FilledGuard
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
    api_instance = ugc_guard_python.GuardsApi(api_client)
    guard_id = 'guard_id_example' # str | 
    request_body = ['request_body_example'] # List[Optional[str]] | 

    try:
        # Update Running Order Of Guard
        api_response = api_instance.update_running_order_of_guard(guard_id, request_body)
        print("The response of GuardsApi->update_running_order_of_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardsApi->update_running_order_of_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_id** | **str**|  | 
 **request_body** | [**List[Optional[str]]**](str.md)|  | 

### Return type

[**FilledGuard**](FilledGuard.md)

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


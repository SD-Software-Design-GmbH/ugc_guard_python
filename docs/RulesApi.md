# ugc_guard_python.RulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rule**](RulesApi.md#create_rule) | **POST** /rules/ | Create Rule
[**delete_rule**](RulesApi.md#delete_rule) | **DELETE** /rules/{rule_id} | Delete Rule
[**get_rule**](RulesApi.md#get_rule) | **GET** /rules/{rule_id} | Get Rule
[**list_rules**](RulesApi.md#list_rules) | **GET** /rules/ | List Rules
[**test_rule**](RulesApi.md#test_rule) | **POST** /rules/{rule_id}/test | Test Rule
[**update_deterministic_options**](RulesApi.md#update_deterministic_options) | **PUT** /rules/{rule_id}/deterministic-options | Update Deterministic Options
[**update_non_deterministic_options**](RulesApi.md#update_non_deterministic_options) | **PUT** /rules/{rule_id}/non-deterministic-options | Update Non Deterministic Options
[**update_rule**](RulesApi.md#update_rule) | **PUT** /rules/{rule_id} | Update Rule


# **create_rule**
> FilledRule create_rule(body_create_rule)

Create Rule

Create a new rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.body_create_rule import BodyCreateRule
from ugc_guard_python.models.filled_rule import FilledRule
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
    api_instance = ugc_guard_python.RulesApi(api_client)
    body_create_rule = ugc_guard_python.BodyCreateRule() # BodyCreateRule | 

    try:
        # Create Rule
        api_response = api_instance.create_rule(body_create_rule)
        print("The response of RulesApi->create_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->create_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_create_rule** | [**BodyCreateRule**](BodyCreateRule.md)|  | 

### Return type

[**FilledRule**](FilledRule.md)

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

# **delete_rule**
> bool delete_rule(rule_id)

Delete Rule

Delete a rule by ID

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
    api_instance = ugc_guard_python.RulesApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Delete Rule
        api_response = api_instance.delete_rule(rule_id)
        print("The response of RulesApi->delete_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->delete_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

**bool**

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

# **get_rule**
> FilledRule get_rule(rule_id)

Get Rule

Get a rule by ID

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.filled_rule import FilledRule
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
    api_instance = ugc_guard_python.RulesApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Get Rule
        api_response = api_instance.get_rule(rule_id)
        print("The response of RulesApi->get_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->get_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**FilledRule**](FilledRule.md)

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

# **list_rules**
> PaginatedResultRule list_rules(organization_id=organization_id, offset=offset, limit=limit)

List Rules

List all rules for an organization

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_rule import PaginatedResultRule
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
    api_instance = ugc_guard_python.RulesApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # List Rules
        api_response = api_instance.list_rules(organization_id=organization_id, offset=offset, limit=limit)
        print("The response of RulesApi->list_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->list_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultRule**](PaginatedResultRule.md)

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

# **test_rule**
> ResponseTestRule test_rule(rule_id, body_test_rule, type_id=type_id, ai_model=ai_model)

Test Rule

Test a rule by ID

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.body_test_rule import BodyTestRule
from ugc_guard_python.models.response_test_rule import ResponseTestRule
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
    api_instance = ugc_guard_python.RulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    body_test_rule = ugc_guard_python.BodyTestRule() # BodyTestRule | 
    type_id = 'type_id_example' # str |  (optional)
    ai_model = 'ai_model_example' # str |  (optional)

    try:
        # Test Rule
        api_response = api_instance.test_rule(rule_id, body_test_rule, type_id=type_id, ai_model=ai_model)
        print("The response of RulesApi->test_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->test_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **body_test_rule** | [**BodyTestRule**](BodyTestRule.md)|  | 
 **type_id** | **str**|  | [optional] 
 **ai_model** | **str**|  | [optional] 

### Return type

[**ResponseTestRule**](ResponseTestRule.md)

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

# **update_deterministic_options**
> DeterministicRuleOptions update_deterministic_options(rule_id, deterministic_rule_options)

Update Deterministic Options

Update deterministic options for a rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.deterministic_rule_options import DeterministicRuleOptions
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
    api_instance = ugc_guard_python.RulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    deterministic_rule_options = ugc_guard_python.DeterministicRuleOptions() # DeterministicRuleOptions | 

    try:
        # Update Deterministic Options
        api_response = api_instance.update_deterministic_options(rule_id, deterministic_rule_options)
        print("The response of RulesApi->update_deterministic_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->update_deterministic_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **deterministic_rule_options** | [**DeterministicRuleOptions**](DeterministicRuleOptions.md)|  | 

### Return type

[**DeterministicRuleOptions**](DeterministicRuleOptions.md)

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

# **update_non_deterministic_options**
> NonDeterministicRuleOptions update_non_deterministic_options(rule_id, non_deterministic_rule_options)

Update Non Deterministic Options

Update non-deterministic options for a rule

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.non_deterministic_rule_options import NonDeterministicRuleOptions
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
    api_instance = ugc_guard_python.RulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    non_deterministic_rule_options = ugc_guard_python.NonDeterministicRuleOptions() # NonDeterministicRuleOptions | 

    try:
        # Update Non Deterministic Options
        api_response = api_instance.update_non_deterministic_options(rule_id, non_deterministic_rule_options)
        print("The response of RulesApi->update_non_deterministic_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->update_non_deterministic_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **non_deterministic_rule_options** | [**NonDeterministicRuleOptions**](NonDeterministicRuleOptions.md)|  | 

### Return type

[**NonDeterministicRuleOptions**](NonDeterministicRuleOptions.md)

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

# **update_rule**
> FilledRule update_rule(rule_id, rule)

Update Rule

Update a rule by ID

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.filled_rule import FilledRule
from ugc_guard_python.models.rule import Rule
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
    api_instance = ugc_guard_python.RulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    rule = ugc_guard_python.Rule() # Rule | 

    try:
        # Update Rule
        api_response = api_instance.update_rule(rule_id, rule)
        print("The response of RulesApi->update_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->update_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **rule** | [**Rule**](Rule.md)|  | 

### Return type

[**FilledRule**](FilledRule.md)

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


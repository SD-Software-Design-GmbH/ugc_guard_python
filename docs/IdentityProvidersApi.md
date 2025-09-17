# ugc_guard_python.IdentityProvidersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_identity_provider**](IdentityProvidersApi.md#add_identity_provider) | **POST** /identity/providers | Add Identity Provider
[**get_identity_provider**](IdentityProvidersApi.md#get_identity_provider) | **GET** /identity/providers/{identity_provider_id} | Get Identity Provider
[**list_enabled_identity_providers**](IdentityProvidersApi.md#list_enabled_identity_providers) | **GET** /identity/providers/enabled | List Enabled Identity Providers
[**list_identity_providers**](IdentityProvidersApi.md#list_identity_providers) | **GET** /identity/providers | List Identity Providers
[**login_for_access_token**](IdentityProvidersApi.md#login_for_access_token) | **POST** /identity/token | Login For Access Token
[**oidc_callback**](IdentityProvidersApi.md#oidc_callback) | **GET** /identity/callback/{identity_provider_id} | Oidc Callback
[**oidc_login**](IdentityProvidersApi.md#oidc_login) | **GET** /identity/providers/{identity_provider_id}/login | Oidc Login
[**prepare_email_for_identity_providers**](IdentityProvidersApi.md#prepare_email_for_identity_providers) | **GET** /identity/prepare/email/{email} | Prepare Email For Identity Providers
[**prepare_organization_for_identity_providers**](IdentityProvidersApi.md#prepare_organization_for_identity_providers) | **GET** /identity/prepare/org/{organization_id} | Prepare Organization For Identity Providers
[**remove_identity_provider**](IdentityProvidersApi.md#remove_identity_provider) | **DELETE** /identity/providers/{identity_provider_id} | Remove Identity Provider
[**update_identity_provider**](IdentityProvidersApi.md#update_identity_provider) | **POST** /identity/providers/{identity_provider_id} | Update Identity Provider
[**validate_access_token**](IdentityProvidersApi.md#validate_access_token) | **GET** /identity/validate | Validate Access Token


# **add_identity_provider**
> IdentityProvider add_identity_provider(identity_provider)

Add Identity Provider

Add a new identity provider

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.identity_provider import IdentityProvider
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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    identity_provider = ugc_guard_python.IdentityProvider() # IdentityProvider | 

    try:
        # Add Identity Provider
        api_response = api_instance.add_identity_provider(identity_provider)
        print("The response of IdentityProvidersApi->add_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->add_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider** | [**IdentityProvider**](IdentityProvider.md)|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

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

# **get_identity_provider**
> IdentityProvider get_identity_provider(identity_provider_id)

Get Identity Provider

Get details of a specific identity provider

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.identity_provider import IdentityProvider
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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    identity_provider_id = 'identity_provider_id_example' # str | 

    try:
        # Get Identity Provider
        api_response = api_instance.get_identity_provider(identity_provider_id)
        print("The response of IdentityProvidersApi->get_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->get_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider_id** | **str**|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

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

# **list_enabled_identity_providers**
> PaginatedResultIdentityProviderBase list_enabled_identity_providers(organization_id)

List Enabled Identity Providers

List all enabled identity providers for an organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_identity_provider_base import PaginatedResultIdentityProviderBase
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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List Enabled Identity Providers
        api_response = api_instance.list_enabled_identity_providers(organization_id)
        print("The response of IdentityProvidersApi->list_enabled_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->list_enabled_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**PaginatedResultIdentityProviderBase**](PaginatedResultIdentityProviderBase.md)

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

# **list_identity_providers**
> PaginatedResultIdentityProviderBase list_identity_providers(organization_id)

List Identity Providers

List all identity providers for an organization

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_identity_provider_base import PaginatedResultIdentityProviderBase
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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List Identity Providers
        api_response = api_instance.list_identity_providers(organization_id)
        print("The response of IdentityProvidersApi->list_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->list_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**PaginatedResultIdentityProviderBase**](PaginatedResultIdentityProviderBase.md)

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

# **login_for_access_token**
> AuthTokenResponse login_for_access_token(username, password, totp=totp, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login For Access Token

Login with username and password, returns jwtToken

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.auth_token_response import AuthTokenResponse
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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    totp = 'totp_example' # str |  (optional)
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login For Access Token
        api_response = api_instance.login_for_access_token(username, password, totp=totp, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of IdentityProvidersApi->login_for_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->login_for_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **totp** | **str**|  | [optional] 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**AuthTokenResponse**](AuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_callback**
> object oidc_callback(identity_provider_id, code, state, error=error, redirect=redirect)

Oidc Callback

Handle OIDC callback

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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    identity_provider_id = 'identity_provider_id_example' # str | 
    code = 'code_example' # str | 
    state = 'state_example' # str | 
    error = 'error_example' # str |  (optional)
    redirect = True # bool |  (optional) (default to True)

    try:
        # Oidc Callback
        api_response = api_instance.oidc_callback(identity_provider_id, code, state, error=error, redirect=redirect)
        print("The response of IdentityProvidersApi->oidc_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->oidc_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider_id** | **str**|  | 
 **code** | **str**|  | 
 **state** | **str**|  | 
 **error** | **str**|  | [optional] 
 **redirect** | **bool**|  | [optional] [default to True]

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

# **oidc_login**
> oidc_login(identity_provider_id)

Oidc Login

Initiate OIDC login flow

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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    identity_provider_id = 'identity_provider_id_example' # str | 

    try:
        # Oidc Login
        api_instance.oidc_login(identity_provider_id)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->oidc_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider_id** | **str**|  | 

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
**307** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_email_for_identity_providers**
> LoginPreparation prepare_email_for_identity_providers(email)

Prepare Email For Identity Providers

Returns the available identity providers (made up by the organizations of th user) for the given email

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.login_preparation import LoginPreparation
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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    email = 'email_example' # str | 

    try:
        # Prepare Email For Identity Providers
        api_response = api_instance.prepare_email_for_identity_providers(email)
        print("The response of IdentityProvidersApi->prepare_email_for_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->prepare_email_for_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**LoginPreparation**](LoginPreparation.md)

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

# **prepare_organization_for_identity_providers**
> LoginPreparation prepare_organization_for_identity_providers(organization_id)

Prepare Organization For Identity Providers

Returns the available identity providers for the given organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.login_preparation import LoginPreparation
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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Prepare Organization For Identity Providers
        api_response = api_instance.prepare_organization_for_identity_providers(organization_id)
        print("The response of IdentityProvidersApi->prepare_organization_for_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->prepare_organization_for_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**LoginPreparation**](LoginPreparation.md)

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

# **remove_identity_provider**
> bool remove_identity_provider(identity_provider_id)

Remove Identity Provider

Remove an identity provider

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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    identity_provider_id = 'identity_provider_id_example' # str | 

    try:
        # Remove Identity Provider
        api_response = api_instance.remove_identity_provider(identity_provider_id)
        print("The response of IdentityProvidersApi->remove_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->remove_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider_id** | **str**|  | 

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

# **update_identity_provider**
> IdentityProvider update_identity_provider(identity_provider_id, identity_provider)

Update Identity Provider

Update an existing identity provider

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ugc_guard_python
from ugc_guard_python.models.identity_provider import IdentityProvider
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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)
    identity_provider_id = 'identity_provider_id_example' # str | 
    identity_provider = ugc_guard_python.IdentityProvider() # IdentityProvider | 

    try:
        # Update Identity Provider
        api_response = api_instance.update_identity_provider(identity_provider_id, identity_provider)
        print("The response of IdentityProvidersApi->update_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->update_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider_id** | **str**|  | 
 **identity_provider** | [**IdentityProvider**](IdentityProvider.md)|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

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

# **validate_access_token**
> str validate_access_token()

Validate Access Token

Validate the access token

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
    api_instance = ugc_guard_python.IdentityProvidersApi(api_client)

    try:
        # Validate Access Token
        api_response = api_instance.validate_access_token()
        print("The response of IdentityProvidersApi->validate_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProvidersApi->validate_access_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


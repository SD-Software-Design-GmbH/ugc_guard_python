# ugc_guard_python.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation_to_organization**](OrganizationsApi.md#accept_invitation_to_organization) | **POST** /organizations/accept/{organization_id} | Accept Invitation To Organization
[**change_membership_state**](OrganizationsApi.md#change_membership_state) | **POST** /organizations/membership/{organization_id} | Change Membership State
[**create_organization**](OrganizationsApi.md#create_organization) | **POST** /organizations/ | Create Organization
[**delete_organization**](OrganizationsApi.md#delete_organization) | **DELETE** /organizations/{organization_id} | Delete Organization
[**deny_invitation_to_organization**](OrganizationsApi.md#deny_invitation_to_organization) | **DELETE** /organizations/invite/deny/{organization_id} | Deny Invitation To Organization
[**get_membership_state**](OrganizationsApi.md#get_membership_state) | **GET** /organizations/membership/{organization_id} | Get Membership State
[**get_my_organizations**](OrganizationsApi.md#get_my_organizations) | **GET** /organizations/ | Get All Organizations
[**get_my_organizations_grouped**](OrganizationsApi.md#get_my_organizations_grouped) | **GET** /organizations/grouped | Get All Of Your Organizations Grouped By Membership State
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /organizations/{organization_id} | Get Organization
[**get_organization_members**](OrganizationsApi.md#get_organization_members) | **GET** /organizations/{organization_id}/members | Get Organization Members
[**invite_user_to_organization**](OrganizationsApi.md#invite_user_to_organization) | **POST** /organizations/invite/by_id/{user_id} | Invite User To Organization
[**invite_user_to_organization_by_email**](OrganizationsApi.md#invite_user_to_organization_by_email) | **POST** /organizations/invite/by_email | Invite User To Organization By Email
[**leave_organization**](OrganizationsApi.md#leave_organization) | **DELETE** /organizations/leave/{organization_id} | Leave Organization
[**revoke_user_from_organization**](OrganizationsApi.md#revoke_user_from_organization) | **DELETE** /organizations/revoke/{organization_id}/{user_id} | Revoke User From Organization
[**update_organization**](OrganizationsApi.md#update_organization) | **PUT** /organizations/{organization_id} | Update Organization


# **accept_invitation_to_organization**
> bool accept_invitation_to_organization(organization_id)

Accept Invitation To Organization

Accepts an invitation to the organization

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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Accept Invitation To Organization
        api_response = api_instance.accept_invitation_to_organization(organization_id)
        print("The response of OrganizationsApi->accept_invitation_to_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->accept_invitation_to_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

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

# **change_membership_state**
> UserOrganizationMembershipState change_membership_state(organization_id, body, user_id=user_id)

Change Membership State

Changes the membership state of the user in the organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.user_organization_membership_state import UserOrganizationMembershipState
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    body = 'body_example' # str | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        # Change Membership State
        api_response = api_instance.change_membership_state(organization_id, body, user_id=user_id)
        print("The response of OrganizationsApi->change_membership_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->change_membership_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **body** | **str**|  | 
 **user_id** | **str**|  | [optional] 

### Return type

[**UserOrganizationMembershipState**](UserOrganizationMembershipState.md)

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

# **create_organization**
> Organization create_organization(organization)

Create Organization

Creates a new organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.organization import Organization
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization = ugc_guard_python.Organization() # Organization | 

    try:
        # Create Organization
        api_response = api_instance.create_organization(organization)
        print("The response of OrganizationsApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | [**Organization**](Organization.md)|  | 

### Return type

[**Organization**](Organization.md)

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

# **delete_organization**
> bool delete_organization(organization_id)

Delete Organization

Deletes the organization

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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Delete Organization
        api_response = api_instance.delete_organization(organization_id)
        print("The response of OrganizationsApi->delete_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

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

# **deny_invitation_to_organization**
> bool deny_invitation_to_organization(organization_id)

Deny Invitation To Organization

Denies an invitation to the organization

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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Deny Invitation To Organization
        api_response = api_instance.deny_invitation_to_organization(organization_id)
        print("The response of OrganizationsApi->deny_invitation_to_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->deny_invitation_to_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

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

# **get_membership_state**
> UserOrganizationMembershipState get_membership_state(organization_id)

Get Membership State

Returns the membership state of the user in the organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.user_organization_membership_state import UserOrganizationMembershipState
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Membership State
        api_response = api_instance.get_membership_state(organization_id)
        print("The response of OrganizationsApi->get_membership_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_membership_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**UserOrganizationMembershipState**](UserOrganizationMembershipState.md)

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

# **get_my_organizations**
> List[Organization] get_my_organizations(offset=offset, limit=limit)

Get All Organizations

Returns all organizations the current user is invited, member or admin of

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.organization import Organization
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Organizations
        api_response = api_instance.get_my_organizations(offset=offset, limit=limit)
        print("The response of OrganizationsApi->get_my_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_my_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Organization]**](Organization.md)

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

# **get_my_organizations_grouped**
> OrganizationGroupings get_my_organizations_grouped(offset=offset, limit=limit)

Get All Of Your Organizations Grouped By Membership State

Returns all organizations the current user is invited, member or admin of, grouped by membership state

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.organization_groupings import OrganizationGroupings
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Of Your Organizations Grouped By Membership State
        api_response = api_instance.get_my_organizations_grouped(offset=offset, limit=limit)
        print("The response of OrganizationsApi->get_my_organizations_grouped:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_my_organizations_grouped: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**OrganizationGroupings**](OrganizationGroupings.md)

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

# **get_organization**
> Organization get_organization(organization_id)

Get Organization

Returns the organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.organization import Organization
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Organization
        api_response = api_instance.get_organization(organization_id)
        print("The response of OrganizationsApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**Organization**](Organization.md)

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

# **get_organization_members**
> PaginatedResultUserWithMembershipState get_organization_members(organization_id, search_term=search_term, offset=offset, limit=limit)

Get Organization Members

Returns all members of the organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_user_with_membership_state import PaginatedResultUserWithMembershipState
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    search_term = 'search_term_example' # str |  (optional)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Organization Members
        api_response = api_instance.get_organization_members(organization_id, search_term=search_term, offset=offset, limit=limit)
        print("The response of OrganizationsApi->get_organization_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **search_term** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultUserWithMembershipState**](PaginatedResultUserWithMembershipState.md)

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

# **invite_user_to_organization**
> Organization invite_user_to_organization(user_id, organization_id)

Invite User To Organization

Invites a user to the organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.organization import Organization
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    user_id = 'user_id_example' # str | 
    organization_id = 'organization_id_example' # str | 

    try:
        # Invite User To Organization
        api_response = api_instance.invite_user_to_organization(user_id, organization_id)
        print("The response of OrganizationsApi->invite_user_to_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->invite_user_to_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **organization_id** | **str**|  | 

### Return type

[**Organization**](Organization.md)

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

# **invite_user_to_organization_by_email**
> bool invite_user_to_organization_by_email(email, organization_id)

Invite User To Organization By Email

Invites a user to the organization by email

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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    email = 'email_example' # str | 
    organization_id = 'organization_id_example' # str | 

    try:
        # Invite User To Organization By Email
        api_response = api_instance.invite_user_to_organization_by_email(email, organization_id)
        print("The response of OrganizationsApi->invite_user_to_organization_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->invite_user_to_organization_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **organization_id** | **str**|  | 

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

# **leave_organization**
> bool leave_organization(organization_id)

Leave Organization

Leaves the organization

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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Leave Organization
        api_response = api_instance.leave_organization(organization_id)
        print("The response of OrganizationsApi->leave_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->leave_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

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

# **revoke_user_from_organization**
> bool revoke_user_from_organization(organization_id, user_id)

Revoke User From Organization

Revokes a user from the organization

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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Revoke User From Organization
        api_response = api_instance.revoke_user_from_organization(organization_id, user_id)
        print("The response of OrganizationsApi->revoke_user_from_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->revoke_user_from_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **user_id** | **str**|  | 

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

# **update_organization**
> Organization update_organization(organization_id, organization)

Update Organization

Updates the organization

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.organization import Organization
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
    api_instance = ugc_guard_python.OrganizationsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    organization = ugc_guard_python.Organization() # Organization | 

    try:
        # Update Organization
        api_response = api_instance.update_organization(organization_id, organization)
        print("The response of OrganizationsApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **organization** | [**Organization**](Organization.md)|  | 

### Return type

[**Organization**](Organization.md)

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


# ugc_guard_python.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_magic_report**](ReportsApi.md#create_magic_report) | **POST** /reports/magic | Create Magic Report
[**create_report**](ReportsApi.md#create_report) | **POST** /reports/ | Create Report
[**escalate_report**](ReportsApi.md#escalate_report) | **GET** /reports/{report_id}/escalate | Escalate Report
[**get_all_reports**](ReportsApi.md#get_all_reports) | **GET** /reports/all | Get All Reports
[**get_content_of_report**](ReportsApi.md#get_content_of_report) | **GET** /reports/{report_id}/content | Get Content Of Report
[**get_enriched_evaluations_of_report**](ReportsApi.md#get_enriched_evaluations_of_report) | **GET** /reports/{report_id}/enriched_evaluations | Get Enriched Evaluations Of Report
[**get_evaluations_of_report**](ReportsApi.md#get_evaluations_of_report) | **GET** /reports/{report_id}/evaluations | Get Evaluations Of Report
[**get_my_reports**](ReportsApi.md#get_my_reports) | **GET** /reports/my/{module_id} | Get My Reports
[**get_report_by_id**](ReportsApi.md#get_report_by_id) | **GET** /reports/{report_id} | Get Report By Id
[**get_reporters_of_report**](ReportsApi.md#get_reporters_of_report) | **GET** /reports/{report_id}/reporters | Get Reporters Of Report
[**reject_report**](ReportsApi.md#reject_report) | **GET** /reports/{report_id}/reject | Reject Report
[**update_report**](ReportsApi.md#update_report) | **PUT** /reports/ | Update Report
[**validate_report**](ReportsApi.md#validate_report) | **GET** /reports/{report_id}/validate | Validate Report


# **create_magic_report**
> ReportDB create_magic_report(report_category, secret, body_create_magic_report, custom_message=custom_message)

Create Magic Report

Create a new report using our magic endpoint. This is recommended.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.body_create_magic_report import BodyCreateMagicReport
from ugc_guard_python.models.report_category import ReportCategory
from ugc_guard_python.models.report_db import ReportDB
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_category = ugc_guard_python.ReportCategory() # ReportCategory | 
    secret = 'secret_example' # str | 
    body_create_magic_report = ugc_guard_python.BodyCreateMagicReport() # BodyCreateMagicReport | 
    custom_message = 'custom_message_example' # str |  (optional)

    try:
        # Create Magic Report
        api_response = api_instance.create_magic_report(report_category, secret, body_create_magic_report, custom_message=custom_message)
        print("The response of ReportsApi->create_magic_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->create_magic_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_category** | [**ReportCategory**](.md)|  | 
 **secret** | **str**|  | 
 **body_create_magic_report** | [**BodyCreateMagicReport**](BodyCreateMagicReport.md)|  | 
 **custom_message** | **str**|  | [optional] 

### Return type

[**ReportDB**](ReportDB.md)

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

# **create_report**
> ReportDB create_report(secret, report_db)

Create Report

Create a new report manually.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.report_db import ReportDB
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    secret = 'secret_example' # str | 
    report_db = ugc_guard_python.ReportDB() # ReportDB | 

    try:
        # Create Report
        api_response = api_instance.create_report(secret, report_db)
        print("The response of ReportsApi->create_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->create_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret** | **str**|  | 
 **report_db** | [**ReportDB**](ReportDB.md)|  | 

### Return type

[**ReportDB**](ReportDB.md)

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

# **escalate_report**
> ReportDB escalate_report(report_id)

Escalate Report

Escalate a report to the escalate state

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.report_db import ReportDB
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 

    try:
        # Escalate Report
        api_response = api_instance.escalate_report(report_id)
        print("The response of ReportsApi->escalate_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->escalate_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**ReportDB**](ReportDB.md)

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

# **get_all_reports**
> PaginatedResultReportDB get_all_reports(offset=offset, limit=limit)

Get All Reports

Get all reports in the database.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_report_db import PaginatedResultReportDB
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Reports
        api_response = api_instance.get_all_reports(offset=offset, limit=limit)
        print("The response of ReportsApi->get_all_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_all_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultReportDB**](PaginatedResultReportDB.md)

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

# **get_content_of_report**
> AllContentResponse get_content_of_report(report_id, secret=secret)

Get Content Of Report

Get all content of a report.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.all_content_response import AllContentResponse
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 
    secret = 'secret_example' # str |  (optional)

    try:
        # Get Content Of Report
        api_response = api_instance.get_content_of_report(report_id, secret=secret)
        print("The response of ReportsApi->get_content_of_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_content_of_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **secret** | **str**|  | [optional] 

### Return type

[**AllContentResponse**](AllContentResponse.md)

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

# **get_enriched_evaluations_of_report**
> AIEnrichedAnswer get_enriched_evaluations_of_report(report_id)

Get Enriched Evaluations Of Report

Get all AI evaluations of a report and all available AI Models.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.ai_enriched_answer import AIEnrichedAnswer
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 

    try:
        # Get Enriched Evaluations Of Report
        api_response = api_instance.get_enriched_evaluations_of_report(report_id)
        print("The response of ReportsApi->get_enriched_evaluations_of_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_enriched_evaluations_of_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**AIEnrichedAnswer**](AIEnrichedAnswer.md)

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

# **get_evaluations_of_report**
> List[AIEvaluation] get_evaluations_of_report(report_id, offset=offset, limit=limit)

Get Evaluations Of Report

Get all AI evaluations of a report.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.ai_evaluation import AIEvaluation
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Evaluations Of Report
        api_response = api_instance.get_evaluations_of_report(report_id, offset=offset, limit=limit)
        print("The response of ReportsApi->get_evaluations_of_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_evaluations_of_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[AIEvaluation]**](AIEvaluation.md)

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

# **get_my_reports**
> PaginatedResultReportWithReportersAndEvaluations get_my_reports(module_id, query=query, states=states, sort_by=sort_by, sort_order=sort_order, offset=offset, limit=limit)

Get My Reports

Get all reports the user has access to.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.paginated_result_report_with_reporters_and_evaluations import PaginatedResultReportWithReportersAndEvaluations
from ugc_guard_python.models.report_state import ReportState
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    module_id = 'module_id_example' # str | 
    query = 'query_example' # str |  (optional)
    states = [ugc_guard_python.ReportState()] # List[ReportState] | Filter by report states (optional)
    sort_by = 'sort_by_example' # str | Sort by field (optional)
    sort_order = 'desc' # str | Sort order, either 'asc' or 'desc' (optional) (default to 'desc')
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get My Reports
        api_response = api_instance.get_my_reports(module_id, query=query, states=states, sort_by=sort_by, sort_order=sort_order, offset=offset, limit=limit)
        print("The response of ReportsApi->get_my_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_my_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **query** | **str**|  | [optional] 
 **states** | [**List[ReportState]**](ReportState.md)| Filter by report states | [optional] 
 **sort_by** | **str**| Sort by field | [optional] 
 **sort_order** | **str**| Sort order, either &#39;asc&#39; or &#39;desc&#39; | [optional] [default to &#39;desc&#39;]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedResultReportWithReportersAndEvaluations**](PaginatedResultReportWithReportersAndEvaluations.md)

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

# **get_report_by_id**
> ReportDB get_report_by_id(report_id, secret=secret)

Get Report By Id

Get a report by its ID.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.report_db import ReportDB
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 
    secret = 'secret_example' # str |  (optional)

    try:
        # Get Report By Id
        api_response = api_instance.get_report_by_id(report_id, secret=secret)
        print("The response of ReportsApi->get_report_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_report_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **secret** | **str**|  | [optional] 

### Return type

[**ReportDB**](ReportDB.md)

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

# **get_reporters_of_report**
> List[ReportersWithPerson] get_reporters_of_report(report_id, secret=secret)

Get Reporters Of Report

Get all reporters of a report.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.reporters_with_person import ReportersWithPerson
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 
    secret = 'secret_example' # str |  (optional)

    try:
        # Get Reporters Of Report
        api_response = api_instance.get_reporters_of_report(report_id, secret=secret)
        print("The response of ReportsApi->get_reporters_of_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_reporters_of_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **secret** | **str**|  | [optional] 

### Return type

[**List[ReportersWithPerson]**](ReportersWithPerson.md)

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

# **reject_report**
> ReportDB reject_report(report_id)

Reject Report

Resolves a report to the rejected state

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.report_db import ReportDB
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 

    try:
        # Reject Report
        api_response = api_instance.reject_report(report_id)
        print("The response of ReportsApi->reject_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reject_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

### Return type

[**ReportDB**](ReportDB.md)

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

# **update_report**
> ReportDB update_report(report_db)

Update Report

Update an existing report.

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.report_db import ReportDB
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_db = ugc_guard_python.ReportDB() # ReportDB | 

    try:
        # Update Report
        api_response = api_instance.update_report(report_db)
        print("The response of ReportsApi->update_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->update_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_db** | [**ReportDB**](ReportDB.md)|  | 

### Return type

[**ReportDB**](ReportDB.md)

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

# **validate_report**
> Report validate_report(report_id, ai_model)

Validate Report

Validates a report using the given ai model

### Example


```python
import ugc_guard_python
from ugc_guard_python.models.report import Report
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
    api_instance = ugc_guard_python.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 
    ai_model = 'ai_model_example' # str | 

    try:
        # Validate Report
        api_response = api_instance.validate_report(report_id, ai_model)
        print("The response of ReportsApi->validate_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->validate_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **ai_model** | **str**|  | 

### Return type

[**Report**](Report.md)

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


# scicat_fake_openapi.JobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs_controller_create**](JobsApi.md#jobs_controller_create) | **POST** /api/v3/jobs | 
[**jobs_controller_find_all**](JobsApi.md#jobs_controller_find_all) | **GET** /api/v3/jobs | 
[**jobs_controller_find_one**](JobsApi.md#jobs_controller_find_one) | **GET** /api/v3/jobs/{id} | 
[**jobs_controller_fullfacet**](JobsApi.md#jobs_controller_fullfacet) | **GET** /api/v3/jobs/fullfacet | 
[**jobs_controller_fullquery**](JobsApi.md#jobs_controller_fullquery) | **GET** /api/v3/jobs/fullquery | 
[**jobs_controller_remove**](JobsApi.md#jobs_controller_remove) | **DELETE** /api/v3/jobs/{id} | 
[**jobs_controller_update**](JobsApi.md#jobs_controller_update) | **PATCH** /api/v3/jobs/{id} | 


# **jobs_controller_create**
> Job jobs_controller_create(create_job_dto)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_fake_openapi
from scicat_fake_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_fake_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_fake_openapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_fake_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_fake_openapi.JobsApi(api_client)
    create_job_dto = scicat_fake_openapi.CreateJobDto() # CreateJobDto | 

    try:
        api_response = api_instance.jobs_controller_create(create_job_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_dto** | [**CreateJobDto**](CreateJobDto.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_find_all**
> list[Job] jobs_controller_find_all(filter=filter)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_fake_openapi
from scicat_fake_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_fake_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_fake_openapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_fake_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_fake_openapi.JobsApi(api_client)
    filter = 'filter_example' # str | Database filters to apply when retrieve all jobs (optional)

    try:
        api_response = api_instance.jobs_controller_find_all(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Database filters to apply when retrieve all jobs | [optional] 

### Return type

[**list[Job]**](Job.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_find_one**
> object jobs_controller_find_one(id)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_fake_openapi
from scicat_fake_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_fake_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_fake_openapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_fake_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_fake_openapi.JobsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.jobs_controller_find_one(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_fullfacet**
> list[object] jobs_controller_fullfacet()



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_fake_openapi
from scicat_fake_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_fake_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_fake_openapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_fake_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_fake_openapi.JobsApi(api_client)
    
    try:
        api_response = api_instance.jobs_controller_fullfacet()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_fullfacet: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_fullquery**
> list[Job] jobs_controller_fullquery()



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_fake_openapi
from scicat_fake_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_fake_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_fake_openapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_fake_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_fake_openapi.JobsApi(api_client)
    
    try:
        api_response = api_instance.jobs_controller_fullquery()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_fullquery: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Job]**](Job.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_remove**
> object jobs_controller_remove(id)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_fake_openapi
from scicat_fake_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_fake_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_fake_openapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_fake_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_fake_openapi.JobsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.jobs_controller_remove(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_controller_update**
> object jobs_controller_update(id, update_job_dto)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_fake_openapi
from scicat_fake_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_fake_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_fake_openapi.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_fake_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_fake_openapi.JobsApi(api_client)
    id = 'id_example' # str | 
update_job_dto = scicat_fake_openapi.UpdateJobDto() # UpdateJobDto | 

    try:
        api_response = api_instance.jobs_controller_update(id, update_job_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->jobs_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_job_dto** | [**UpdateJobDto**](UpdateJobDto.md)|  | 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


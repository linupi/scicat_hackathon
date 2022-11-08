# scicat_fake_openapi.LogbooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logbooks_controller_find_all**](LogbooksApi.md#logbooks_controller_find_all) | **GET** /api/v3/logbooks | 
[**logbooks_controller_find_by_name**](LogbooksApi.md#logbooks_controller_find_by_name) | **GET** /api/v3/logbooks/{name} | 


# **logbooks_controller_find_all**
> object logbooks_controller_find_all()



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
    api_instance = scicat_fake_openapi.LogbooksApi(api_client)
    
    try:
        api_response = api_instance.logbooks_controller_find_all()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogbooksApi->logbooks_controller_find_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **logbooks_controller_find_by_name**
> object logbooks_controller_find_by_name(name, filters)



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
    api_instance = scicat_fake_openapi.LogbooksApi(api_client)
    name = 'name_example' # str | 
filters = 'filters_example' # str | 

    try:
        api_response = api_instance.logbooks_controller_find_by_name(name, filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogbooksApi->logbooks_controller_find_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **filters** | **str**|  | 

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


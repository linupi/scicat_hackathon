# scicat_fake_openapi.PoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policies_controller_count**](PoliciesApi.md#policies_controller_count) | **GET** /api/v3/policies/count | 
[**policies_controller_create**](PoliciesApi.md#policies_controller_create) | **POST** /api/v3/policies | 
[**policies_controller_find_all**](PoliciesApi.md#policies_controller_find_all) | **GET** /api/v3/policies | 
[**policies_controller_find_one**](PoliciesApi.md#policies_controller_find_one) | **GET** /api/v3/policies/{id} | 
[**policies_controller_remove**](PoliciesApi.md#policies_controller_remove) | **DELETE** /api/v3/policies/{id} | 
[**policies_controller_update**](PoliciesApi.md#policies_controller_update) | **PATCH** /api/v3/policies/{id} | 
[**policies_controller_update_where**](PoliciesApi.md#policies_controller_update_where) | **POST** /api/v3/policies/updateWhere | 


# **policies_controller_count**
> policies_controller_count(where)



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
    api_instance = scicat_fake_openapi.PoliciesApi(api_client)
    where = 'where_example' # str | 

    try:
        api_instance.policies_controller_count(where)
    except ApiException as e:
        print("Exception when calling PoliciesApi->policies_controller_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_controller_create**
> Policy policies_controller_create(create_policy_dto)



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
    api_instance = scicat_fake_openapi.PoliciesApi(api_client)
    create_policy_dto = scicat_fake_openapi.CreatePolicyDto() # CreatePolicyDto | 

    try:
        api_response = api_instance.policies_controller_create(create_policy_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->policies_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_policy_dto** | [**CreatePolicyDto**](CreatePolicyDto.md)|  | 

### Return type

[**Policy**](Policy.md)

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

# **policies_controller_find_all**
> list[Policy] policies_controller_find_all(filter=filter)



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
    api_instance = scicat_fake_openapi.PoliciesApi(api_client)
    filter = 'filter_example' # str | Database filters to apply when retrieve all policies (optional)

    try:
        api_response = api_instance.policies_controller_find_all(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->policies_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Database filters to apply when retrieve all policies | [optional] 

### Return type

[**list[Policy]**](Policy.md)

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

# **policies_controller_find_one**
> object policies_controller_find_one(id)



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
    api_instance = scicat_fake_openapi.PoliciesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.policies_controller_find_one(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->policies_controller_find_one: %s\n" % e)
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

# **policies_controller_remove**
> object policies_controller_remove(id)



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
    api_instance = scicat_fake_openapi.PoliciesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.policies_controller_remove(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->policies_controller_remove: %s\n" % e)
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

# **policies_controller_update**
> object policies_controller_update(id, update_policy_dto)



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
    api_instance = scicat_fake_openapi.PoliciesApi(api_client)
    id = 'id_example' # str | 
update_policy_dto = scicat_fake_openapi.UpdatePolicyDto() # UpdatePolicyDto | 

    try:
        api_response = api_instance.policies_controller_update(id, update_policy_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesApi->policies_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_policy_dto** | [**UpdatePolicyDto**](UpdatePolicyDto.md)|  | 

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

# **policies_controller_update_where**
> policies_controller_update_where(owner_group_list, data, owner_grouplist)



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
    api_instance = scicat_fake_openapi.PoliciesApi(api_client)
    owner_group_list = 'owner_group_list_example' # str | 
data = 'data_example' # str | Policy JSON object
owner_grouplist = None # object | Stringified array of owner groups

    try:
        api_instance.policies_controller_update_where(owner_group_list, data, owner_grouplist)
    except ApiException as e:
        print("Exception when calling PoliciesApi->policies_controller_update_where: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_group_list** | **str**|  | 
 **data** | **str**| Policy JSON object | 
 **owner_grouplist** | [**object**](.md)| Stringified array of owner groups | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


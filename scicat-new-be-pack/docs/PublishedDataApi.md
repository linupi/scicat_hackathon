# scicat_new_be_pack.PublishedDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**published_data_controller_count**](PublishedDataApi.md#published_data_controller_count) | **GET** /api/v3/publisheddata/count | 
[**published_data_controller_create**](PublishedDataApi.md#published_data_controller_create) | **POST** /api/v3/publisheddata | 
[**published_data_controller_find_all**](PublishedDataApi.md#published_data_controller_find_all) | **GET** /api/v3/publisheddata | 
[**published_data_controller_find_one**](PublishedDataApi.md#published_data_controller_find_one) | **GET** /api/v3/publisheddata/{id} | 
[**published_data_controller_form_populate**](PublishedDataApi.md#published_data_controller_form_populate) | **GET** /api/v3/publisheddata/formpopulate | 
[**published_data_controller_register**](PublishedDataApi.md#published_data_controller_register) | **POST** /api/v3/publisheddata/{id}/register | 
[**published_data_controller_remove**](PublishedDataApi.md#published_data_controller_remove) | **DELETE** /api/v3/publisheddata/{id} | 
[**published_data_controller_resync**](PublishedDataApi.md#published_data_controller_resync) | **POST** /api/v3/publisheddata/{id}/resync | 
[**published_data_controller_update**](PublishedDataApi.md#published_data_controller_update) | **PATCH** /api/v3/publisheddata/{id} | 


# **published_data_controller_count**
> object published_data_controller_count(filter=filter)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    filter = None # object | Database filters to apply when retrieve published data count (optional)

    try:
        api_response = api_instance.published_data_controller_count(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| Database filters to apply when retrieve published data count | [optional] 

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

# **published_data_controller_create**
> PublishedData published_data_controller_create(create_published_data_dto)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    create_published_data_dto = scicat_new_be_pack.CreatePublishedDataDto() # CreatePublishedDataDto | 

    try:
        api_response = api_instance.published_data_controller_create(create_published_data_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_published_data_dto** | [**CreatePublishedDataDto**](CreatePublishedDataDto.md)|  | 

### Return type

[**PublishedData**](PublishedData.md)

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

# **published_data_controller_find_all**
> list[PublishedData] published_data_controller_find_all(filter=filter)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    filter = 'filter_example' # str | Database filters to apply when retrieve all published data (optional)

    try:
        api_response = api_instance.published_data_controller_find_all(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Database filters to apply when retrieve all published data | [optional] 

### Return type

[**list[PublishedData]**](PublishedData.md)

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

# **published_data_controller_find_one**
> object published_data_controller_find_one(id)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.published_data_controller_find_one(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_find_one: %s\n" % e)
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

# **published_data_controller_form_populate**
> object published_data_controller_form_populate(pid)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    pid = 'pid_example' # str | Dataset pid used to fetch form data.

    try:
        api_response = api_instance.published_data_controller_form_populate(pid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_form_populate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**| Dataset pid used to fetch form data. | 

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

# **published_data_controller_register**
> object published_data_controller_register(id)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.published_data_controller_register(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_register: %s\n" % e)
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **published_data_controller_remove**
> object published_data_controller_remove(id)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.published_data_controller_remove(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_remove: %s\n" % e)
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

# **published_data_controller_resync**
> object published_data_controller_resync(id, update_published_data_dto)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    id = 'id_example' # str | 
update_published_data_dto = scicat_new_be_pack.UpdatePublishedDataDto() # UpdatePublishedDataDto | 

    try:
        api_response = api_instance.published_data_controller_resync(id, update_published_data_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_resync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_published_data_dto** | [**UpdatePublishedDataDto**](UpdatePublishedDataDto.md)|  | 

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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **published_data_controller_update**
> object published_data_controller_update(id, update_published_data_dto)



### Example

* Bearer (JWT) Authentication (bearer):
```python
from __future__ import print_function
import time
import scicat_new_be_pack
from scicat_new_be_pack.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = scicat_new_be_pack.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = scicat_new_be_pack.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with scicat_new_be_pack.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scicat_new_be_pack.PublishedDataApi(api_client)
    id = 'id_example' # str | 
update_published_data_dto = scicat_new_be_pack.UpdatePublishedDataDto() # UpdatePublishedDataDto | 

    try:
        api_response = api_instance.published_data_controller_update(id, update_published_data_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublishedDataApi->published_data_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_published_data_dto** | [**UpdatePublishedDataDto**](UpdatePublishedDataDto.md)|  | 

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


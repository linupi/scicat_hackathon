# scicat_fake_openapi.InstrumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instruments_controller_create**](InstrumentsApi.md#instruments_controller_create) | **POST** /api/v3/instruments | 
[**instruments_controller_find_all**](InstrumentsApi.md#instruments_controller_find_all) | **GET** /api/v3/instruments | 
[**instruments_controller_find_one**](InstrumentsApi.md#instruments_controller_find_one) | **GET** /api/v3/instruments/{id} | 
[**instruments_controller_remove**](InstrumentsApi.md#instruments_controller_remove) | **DELETE** /api/v3/instruments/{id} | 
[**instruments_controller_update**](InstrumentsApi.md#instruments_controller_update) | **PATCH** /api/v3/instruments/{id} | 


# **instruments_controller_create**
> Instrument instruments_controller_create(create_instrument_dto)



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
    api_instance = scicat_fake_openapi.InstrumentsApi(api_client)
    create_instrument_dto = scicat_fake_openapi.CreateInstrumentDto() # CreateInstrumentDto | 

    try:
        api_response = api_instance.instruments_controller_create(create_instrument_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstrumentsApi->instruments_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_instrument_dto** | [**CreateInstrumentDto**](CreateInstrumentDto.md)|  | 

### Return type

[**Instrument**](Instrument.md)

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

# **instruments_controller_find_all**
> list[Instrument] instruments_controller_find_all(filter=filter)



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
    api_instance = scicat_fake_openapi.InstrumentsApi(api_client)
    filter = 'filter_example' # str | Database filters to apply when retrieve all instruments (optional)

    try:
        api_response = api_instance.instruments_controller_find_all(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstrumentsApi->instruments_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Database filters to apply when retrieve all instruments | [optional] 

### Return type

[**list[Instrument]**](Instrument.md)

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

# **instruments_controller_find_one**
> object instruments_controller_find_one(id)



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
    api_instance = scicat_fake_openapi.InstrumentsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.instruments_controller_find_one(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstrumentsApi->instruments_controller_find_one: %s\n" % e)
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

# **instruments_controller_remove**
> object instruments_controller_remove(id)



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
    api_instance = scicat_fake_openapi.InstrumentsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.instruments_controller_remove(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstrumentsApi->instruments_controller_remove: %s\n" % e)
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

# **instruments_controller_update**
> object instruments_controller_update(id, update_instrument_dto)



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
    api_instance = scicat_fake_openapi.InstrumentsApi(api_client)
    id = 'id_example' # str | 
update_instrument_dto = scicat_fake_openapi.UpdateInstrumentDto() # UpdateInstrumentDto | 

    try:
        api_response = api_instance.instruments_controller_update(id, update_instrument_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstrumentsApi->instruments_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_instrument_dto** | [**UpdateInstrumentDto**](UpdateInstrumentDto.md)|  | 

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


# scicat_new_be_pack.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_ad_login**](AuthApi.md#auth_controller_ad_login) | **POST** /api/v3/auth/msad | 
[**auth_controller_login**](AuthApi.md#auth_controller_login) | **POST** /api/v3/auth/login | 
[**auth_controller_whoami**](AuthApi.md#auth_controller_whoami) | **GET** /api/v3/auth/whoami | 


# **auth_controller_ad_login**
> object auth_controller_ad_login(credentials_dto)



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
    api_instance = scicat_new_be_pack.AuthApi(api_client)
    credentials_dto = scicat_new_be_pack.CredentialsDto() # CredentialsDto | 

    try:
        api_response = api_instance.auth_controller_ad_login(credentials_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->auth_controller_ad_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_dto** | [**CredentialsDto**](CredentialsDto.md)|  | 

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

# **auth_controller_login**
> object auth_controller_login(credentials_dto)



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
    api_instance = scicat_new_be_pack.AuthApi(api_client)
    credentials_dto = scicat_new_be_pack.CredentialsDto() # CredentialsDto | 

    try:
        api_response = api_instance.auth_controller_login(credentials_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->auth_controller_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_dto** | [**CredentialsDto**](CredentialsDto.md)|  | 

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

# **auth_controller_whoami**
> object auth_controller_whoami()



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
    api_instance = scicat_new_be_pack.AuthApi(api_client)
    
    try:
        api_response = api_instance.auth_controller_whoami()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->auth_controller_whoami: %s\n" % e)
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


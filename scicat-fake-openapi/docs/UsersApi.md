# scicat_fake_openapi.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_controller_create_settings**](UsersApi.md#users_controller_create_settings) | **POST** /api/v3/users/{id}/settings | 
[**users_controller_find_by_id**](UsersApi.md#users_controller_find_by_id) | **GET** /api/v3/users/{id} | 
[**users_controller_get_settings**](UsersApi.md#users_controller_get_settings) | **GET** /api/v3/users/{id}/settings | 
[**users_controller_get_user_identity**](UsersApi.md#users_controller_get_user_identity) | **GET** /api/v3/users/{id}/userIdentity | 
[**users_controller_get_user_jwt**](UsersApi.md#users_controller_get_user_jwt) | **POST** /api/v3/users/jwt | 
[**users_controller_login**](UsersApi.md#users_controller_login) | **POST** /api/v3/users/login | 
[**users_controller_patch_settings**](UsersApi.md#users_controller_patch_settings) | **PATCH** /api/v3/users/{id}/settings | 
[**users_controller_remove_settings**](UsersApi.md#users_controller_remove_settings) | **DELETE** /api/v3/users/{id}/settings | 
[**users_controller_update_settings**](UsersApi.md#users_controller_update_settings) | **PUT** /api/v3/users/{id}/settings | 


# **users_controller_create_settings**
> UserSettings users_controller_create_settings(id)



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.users_controller_create_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_create_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserSettings**](UserSettings.md)

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

# **users_controller_find_by_id**
> object users_controller_find_by_id(id)



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.users_controller_find_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_find_by_id: %s\n" % e)
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

# **users_controller_get_settings**
> object users_controller_get_settings(id)



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.users_controller_get_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_get_settings: %s\n" % e)
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

# **users_controller_get_user_identity**
> object users_controller_get_user_identity(id)



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.users_controller_get_user_identity(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_get_user_identity: %s\n" % e)
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

# **users_controller_get_user_jwt**
> object users_controller_get_user_jwt()



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    
    try:
        api_response = api_instance.users_controller_get_user_jwt()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_get_user_jwt: %s\n" % e)
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_login**
> object users_controller_login(credentials_dto)



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    credentials_dto = scicat_fake_openapi.CredentialsDto() # CredentialsDto | 

    try:
        api_response = api_instance.users_controller_login(credentials_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_login: %s\n" % e)
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

# **users_controller_patch_settings**
> object users_controller_patch_settings(id)



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.users_controller_patch_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_patch_settings: %s\n" % e)
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

# **users_controller_remove_settings**
> object users_controller_remove_settings(id)



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.users_controller_remove_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_remove_settings: %s\n" % e)
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

# **users_controller_update_settings**
> object users_controller_update_settings(id)



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
    api_instance = scicat_fake_openapi.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.users_controller_update_settings(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_controller_update_settings: %s\n" % e)
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


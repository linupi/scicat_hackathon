# scicat_new_be_pack.SamplesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samples_controller_create**](SamplesApi.md#samples_controller_create) | **POST** /api/v3/samples | 
[**samples_controller_create_attachments**](SamplesApi.md#samples_controller_create_attachments) | **POST** /api/v3/samples/{id}/attachments | 
[**samples_controller_create_dataset**](SamplesApi.md#samples_controller_create_dataset) | **POST** /api/v3/samples/{id}/datasets | 
[**samples_controller_find_all**](SamplesApi.md#samples_controller_find_all) | **GET** /api/v3/samples | 
[**samples_controller_find_all_attachments**](SamplesApi.md#samples_controller_find_all_attachments) | **GET** /api/v3/samples/{id}/attachments | 
[**samples_controller_find_all_datasets**](SamplesApi.md#samples_controller_find_all_datasets) | **GET** /api/v3/samples/{id}/datasets | 
[**samples_controller_find_by_id**](SamplesApi.md#samples_controller_find_by_id) | **GET** /api/v3/samples/{id} | 
[**samples_controller_find_one**](SamplesApi.md#samples_controller_find_one) | **GET** /api/v3/samples/findOne | 
[**samples_controller_find_one_attachment_and_remove**](SamplesApi.md#samples_controller_find_one_attachment_and_remove) | **DELETE** /api/v3/samples/{id}/attachments/{fk} | 
[**samples_controller_find_one_attachment_and_update**](SamplesApi.md#samples_controller_find_one_attachment_and_update) | **PATCH** /api/v3/samples/{id}/attachments/{fk} | 
[**samples_controller_find_one_dataset_and_remove**](SamplesApi.md#samples_controller_find_one_dataset_and_remove) | **DELETE** /api/v3/samples/{id}/datasets/{fk} | 
[**samples_controller_find_one_dataset_and_update**](SamplesApi.md#samples_controller_find_one_dataset_and_update) | **PATCH** /api/v3/samples/{id}/datasets/{fk} | 
[**samples_controller_fullquery**](SamplesApi.md#samples_controller_fullquery) | **GET** /api/v3/samples/fullquery | 
[**samples_controller_metadata_keys**](SamplesApi.md#samples_controller_metadata_keys) | **GET** /api/v3/samples/metadataKeys | 
[**samples_controller_remove**](SamplesApi.md#samples_controller_remove) | **DELETE** /api/v3/samples/{id} | 
[**samples_controller_update**](SamplesApi.md#samples_controller_update) | **PATCH** /api/v3/samples/{id} | 


# **samples_controller_create**
> Sample samples_controller_create(create_sample_dto)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    create_sample_dto = scicat_new_be_pack.CreateSampleDto() # CreateSampleDto | 

    try:
        api_response = api_instance.samples_controller_create(create_sample_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sample_dto** | [**CreateSampleDto**](CreateSampleDto.md)|  | 

### Return type

[**Sample**](Sample.md)

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

# **samples_controller_create_attachments**
> Attachment samples_controller_create_attachments(id, create_attachment_dto)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 
create_attachment_dto = scicat_new_be_pack.CreateAttachmentDto() # CreateAttachmentDto | 

    try:
        api_response = api_instance.samples_controller_create_attachments(id, create_attachment_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_create_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_attachment_dto** | [**CreateAttachmentDto**](CreateAttachmentDto.md)|  | 

### Return type

[**Attachment**](Attachment.md)

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

# **samples_controller_create_dataset**
> Dataset samples_controller_create_dataset(id, create_raw_dataset_dto)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 
create_raw_dataset_dto = scicat_new_be_pack.CreateRawDatasetDto() # CreateRawDatasetDto | 

    try:
        api_response = api_instance.samples_controller_create_dataset(id, create_raw_dataset_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_create_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_raw_dataset_dto** | [**CreateRawDatasetDto**](CreateRawDatasetDto.md)|  | 

### Return type

[**Dataset**](Dataset.md)

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

# **samples_controller_find_all**
> list[Sample] samples_controller_find_all(filters=filters)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    filters = 'filters_example' # str | Database filters to apply when retrieve all samples (optional)

    try:
        api_response = api_instance.samples_controller_find_all(filters=filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Database filters to apply when retrieve all samples | [optional] 

### Return type

[**list[Sample]**](Sample.md)

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

# **samples_controller_find_all_attachments**
> list[Attachment] samples_controller_find_all_attachments(id)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_controller_find_all_attachments(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_all_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Attachment]**](Attachment.md)

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

# **samples_controller_find_all_datasets**
> object samples_controller_find_all_datasets(id)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_controller_find_all_datasets(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_all_datasets: %s\n" % e)
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

# **samples_controller_find_by_id**
> object samples_controller_find_by_id(id)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_controller_find_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_by_id: %s\n" % e)
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

# **samples_controller_find_one**
> object samples_controller_find_one(filter)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    filter = 'filter_example' # str | 

    try:
        api_response = api_instance.samples_controller_find_one(filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | 

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

# **samples_controller_find_one_attachment_and_remove**
> object samples_controller_find_one_attachment_and_remove(id, fk)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 

    try:
        api_response = api_instance.samples_controller_find_one_attachment_and_remove(id, fk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_one_attachment_and_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fk** | **str**|  | 

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

# **samples_controller_find_one_attachment_and_update**
> object samples_controller_find_one_attachment_and_update(id, fk, update_attachment_dto)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 
update_attachment_dto = scicat_new_be_pack.UpdateAttachmentDto() # UpdateAttachmentDto | 

    try:
        api_response = api_instance.samples_controller_find_one_attachment_and_update(id, fk, update_attachment_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_one_attachment_and_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fk** | **str**|  | 
 **update_attachment_dto** | [**UpdateAttachmentDto**](UpdateAttachmentDto.md)|  | 

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

# **samples_controller_find_one_dataset_and_remove**
> object samples_controller_find_one_dataset_and_remove(id, fk)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 

    try:
        api_response = api_instance.samples_controller_find_one_dataset_and_remove(id, fk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_one_dataset_and_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fk** | **str**|  | 

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

# **samples_controller_find_one_dataset_and_update**
> object samples_controller_find_one_dataset_and_update(id, fk, update_raw_dataset_dto)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 
update_raw_dataset_dto = scicat_new_be_pack.UpdateRawDatasetDto() # UpdateRawDatasetDto | 

    try:
        api_response = api_instance.samples_controller_find_one_dataset_and_update(id, fk, update_raw_dataset_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_find_one_dataset_and_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fk** | **str**|  | 
 **update_raw_dataset_dto** | [**UpdateRawDatasetDto**](UpdateRawDatasetDto.md)|  | 

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

# **samples_controller_fullquery**
> list[Sample] samples_controller_fullquery()



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    
    try:
        api_response = api_instance.samples_controller_fullquery()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_fullquery: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Sample]**](Sample.md)

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

# **samples_controller_metadata_keys**
> list[str] samples_controller_metadata_keys()



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    
    try:
        api_response = api_instance.samples_controller_metadata_keys()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_metadata_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

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

# **samples_controller_remove**
> object samples_controller_remove(id)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.samples_controller_remove(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_remove: %s\n" % e)
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

# **samples_controller_update**
> object samples_controller_update(id, update_sample_dto)



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
    api_instance = scicat_new_be_pack.SamplesApi(api_client)
    id = 'id_example' # str | 
update_sample_dto = scicat_new_be_pack.UpdateSampleDto() # UpdateSampleDto | 

    try:
        api_response = api_instance.samples_controller_update(id, update_sample_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SamplesApi->samples_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_sample_dto** | [**UpdateSampleDto**](UpdateSampleDto.md)|  | 

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


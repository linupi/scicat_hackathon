# scicat_new_be_pack.DatasetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasets_controller_append_to_array_field**](DatasetsApi.md#datasets_controller_append_to_array_field) | **POST** /api/v3/datasets/{id}/appendToArrayField | 
[**datasets_controller_count**](DatasetsApi.md#datasets_controller_count) | **GET** /api/v3/datasets/count | 
[**datasets_controller_create**](DatasetsApi.md#datasets_controller_create) | **POST** /api/v3/datasets | 
[**datasets_controller_create_attachment**](DatasetsApi.md#datasets_controller_create_attachment) | **POST** /api/v3/datasets/{id}/attachments | 
[**datasets_controller_create_datablock**](DatasetsApi.md#datasets_controller_create_datablock) | **POST** /api/v3/datasets/{id}/datablocks | 
[**datasets_controller_create_orig_datablock**](DatasetsApi.md#datasets_controller_create_orig_datablock) | **POST** /api/v3/datasets/{id}/origdatablocks | 
[**datasets_controller_find_all**](DatasetsApi.md#datasets_controller_find_all) | **GET** /api/v3/datasets | 
[**datasets_controller_find_all_attachments**](DatasetsApi.md#datasets_controller_find_all_attachments) | **GET** /api/v3/datasets/{id}/attachments | 
[**datasets_controller_find_all_datablocks**](DatasetsApi.md#datasets_controller_find_all_datablocks) | **GET** /api/v3/datasets/{id}/datablocks | 
[**datasets_controller_find_all_orig_datablocks**](DatasetsApi.md#datasets_controller_find_all_orig_datablocks) | **GET** /api/v3/datasets/{id}/origdatablocks | 
[**datasets_controller_find_by_id**](DatasetsApi.md#datasets_controller_find_by_id) | **GET** /api/v3/datasets/{id} | 
[**datasets_controller_find_by_id_and_delete**](DatasetsApi.md#datasets_controller_find_by_id_and_delete) | **DELETE** /api/v3/datasets/{id} | 
[**datasets_controller_find_by_id_and_update**](DatasetsApi.md#datasets_controller_find_by_id_and_update) | **PATCH** /api/v3/datasets/{id} | 
[**datasets_controller_find_by_id_replace_or_create**](DatasetsApi.md#datasets_controller_find_by_id_replace_or_create) | **PUT** /api/v3/datasets/{id} | 
[**datasets_controller_find_one**](DatasetsApi.md#datasets_controller_find_one) | **GET** /api/v3/datasets/findOne | 
[**datasets_controller_find_one_attachment_and_remove**](DatasetsApi.md#datasets_controller_find_one_attachment_and_remove) | **DELETE** /api/v3/datasets/{id}/attachments/{fk} | 
[**datasets_controller_find_one_attachment_and_update**](DatasetsApi.md#datasets_controller_find_one_attachment_and_update) | **PATCH** /api/v3/datasets/{id}/attachments/{fk} | 
[**datasets_controller_find_one_datablock_and_remove**](DatasetsApi.md#datasets_controller_find_one_datablock_and_remove) | **DELETE** /api/v3/datasets/{id}/datablocks/{fk} | 
[**datasets_controller_find_one_datablock_and_update**](DatasetsApi.md#datasets_controller_find_one_datablock_and_update) | **PATCH** /api/v3/datasets/{id}/datablocks/{fk} | 
[**datasets_controller_find_one_orig_datablock_and_remove**](DatasetsApi.md#datasets_controller_find_one_orig_datablock_and_remove) | **DELETE** /api/v3/datasets/{id}/origdatablocks/{fk} | 
[**datasets_controller_find_one_orig_datablock_and_update**](DatasetsApi.md#datasets_controller_find_one_orig_datablock_and_update) | **PATCH** /api/v3/datasets/{id}/origdatablocks/{fk} | 
[**datasets_controller_fullfacet**](DatasetsApi.md#datasets_controller_fullfacet) | **GET** /api/v3/datasets/fullfacet | 
[**datasets_controller_fullquery**](DatasetsApi.md#datasets_controller_fullquery) | **GET** /api/v3/datasets/fullquery | 
[**datasets_controller_metadata_keys**](DatasetsApi.md#datasets_controller_metadata_keys) | **GET** /api/v3/datasets/metadataKeys | 
[**datasets_controller_thumbnail**](DatasetsApi.md#datasets_controller_thumbnail) | **GET** /api/v3/datasets/{id}/thumbnail | 


# **datasets_controller_append_to_array_field**
> object datasets_controller_append_to_array_field(id, field_name)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
field_name = 'field_name_example' # str | 

    try:
        api_response = api_instance.datasets_controller_append_to_array_field(id, field_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_append_to_array_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **field_name** | **str**|  | 

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

# **datasets_controller_count**
> datasets_controller_count()



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    
    try:
        api_instance.datasets_controller_count()
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **datasets_controller_create**
> Dataset datasets_controller_create(create_dataset_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    create_dataset_dto = scicat_new_be_pack.CreateDatasetDto() # CreateDatasetDto | 

    try:
        api_response = api_instance.datasets_controller_create(create_dataset_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dataset_dto** | [**CreateDatasetDto**](CreateDatasetDto.md)|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_controller_create_attachment**
> object datasets_controller_create_attachment(id, create_attachment_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
create_attachment_dto = scicat_new_be_pack.CreateAttachmentDto() # CreateAttachmentDto | 

    try:
        api_response = api_instance.datasets_controller_create_attachment(id, create_attachment_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_create_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_attachment_dto** | [**CreateAttachmentDto**](CreateAttachmentDto.md)|  | 

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

# **datasets_controller_create_datablock**
> object datasets_controller_create_datablock(id, create_datablock_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
create_datablock_dto = scicat_new_be_pack.CreateDatablockDto() # CreateDatablockDto | 

    try:
        api_response = api_instance.datasets_controller_create_datablock(id, create_datablock_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_create_datablock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_datablock_dto** | [**CreateDatablockDto**](CreateDatablockDto.md)|  | 

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

# **datasets_controller_create_orig_datablock**
> object datasets_controller_create_orig_datablock(id, create_origdatablock_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
create_origdatablock_dto = scicat_new_be_pack.CreateOrigdatablockDto() # CreateOrigdatablockDto | 

    try:
        api_response = api_instance.datasets_controller_create_orig_datablock(id, create_origdatablock_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_create_orig_datablock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_origdatablock_dto** | [**CreateOrigdatablockDto**](CreateOrigdatablockDto.md)|  | 

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

# **datasets_controller_find_all**
> object datasets_controller_find_all(filter=filter)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    filter = None # object | Database filters to apply when retrieve all datasets (optional)

    try:
        api_response = api_instance.datasets_controller_find_all(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**object**](.md)| Database filters to apply when retrieve all datasets | [optional] 

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

# **datasets_controller_find_all_attachments**
> list[Attachment] datasets_controller_find_all_attachments(id)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.datasets_controller_find_all_attachments(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_all_attachments: %s\n" % e)
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

# **datasets_controller_find_all_datablocks**
> list[Datablock] datasets_controller_find_all_datablocks(id)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.datasets_controller_find_all_datablocks(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_all_datablocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Datablock]**](Datablock.md)

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

# **datasets_controller_find_all_orig_datablocks**
> list[OrigDatablock] datasets_controller_find_all_orig_datablocks(id)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.datasets_controller_find_all_orig_datablocks(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_all_orig_datablocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[OrigDatablock]**](OrigDatablock.md)

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

# **datasets_controller_find_by_id**
> object datasets_controller_find_by_id(id)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.datasets_controller_find_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_by_id: %s\n" % e)
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

# **datasets_controller_find_by_id_and_delete**
> object datasets_controller_find_by_id_and_delete(id)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.datasets_controller_find_by_id_and_delete(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_by_id_and_delete: %s\n" % e)
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

# **datasets_controller_find_by_id_and_update**
> object datasets_controller_find_by_id_and_update(id, update_dataset_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
update_dataset_dto = scicat_new_be_pack.UpdateDatasetDto() # UpdateDatasetDto | 

    try:
        api_response = api_instance.datasets_controller_find_by_id_and_update(id, update_dataset_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_by_id_and_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_dataset_dto** | [**UpdateDatasetDto**](UpdateDatasetDto.md)|  | 

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

# **datasets_controller_find_by_id_replace_or_create**
> object datasets_controller_find_by_id_replace_or_create(id, update_dataset_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
update_dataset_dto = scicat_new_be_pack.UpdateDatasetDto() # UpdateDatasetDto | 

    try:
        api_response = api_instance.datasets_controller_find_by_id_replace_or_create(id, update_dataset_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_by_id_replace_or_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_dataset_dto** | [**UpdateDatasetDto**](UpdateDatasetDto.md)|  | 

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

# **datasets_controller_find_one**
> object datasets_controller_find_one(filter=filter)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    filter = 'filter_example' # str | Database filter to apply when finding a Dataset (optional)

    try:
        api_response = api_instance.datasets_controller_find_one(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Database filter to apply when finding a Dataset | [optional] 

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

# **datasets_controller_find_one_attachment_and_remove**
> object datasets_controller_find_one_attachment_and_remove(id, fk)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 

    try:
        api_response = api_instance.datasets_controller_find_one_attachment_and_remove(id, fk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_one_attachment_and_remove: %s\n" % e)
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

# **datasets_controller_find_one_attachment_and_update**
> object datasets_controller_find_one_attachment_and_update(id, fk, update_attachment_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 
update_attachment_dto = scicat_new_be_pack.UpdateAttachmentDto() # UpdateAttachmentDto | 

    try:
        api_response = api_instance.datasets_controller_find_one_attachment_and_update(id, fk, update_attachment_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_one_attachment_and_update: %s\n" % e)
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

# **datasets_controller_find_one_datablock_and_remove**
> object datasets_controller_find_one_datablock_and_remove(id, fk)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 

    try:
        api_response = api_instance.datasets_controller_find_one_datablock_and_remove(id, fk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_one_datablock_and_remove: %s\n" % e)
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

# **datasets_controller_find_one_datablock_and_update**
> object datasets_controller_find_one_datablock_and_update(id, fk, update_datablock_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 
update_datablock_dto = scicat_new_be_pack.UpdateDatablockDto() # UpdateDatablockDto | 

    try:
        api_response = api_instance.datasets_controller_find_one_datablock_and_update(id, fk, update_datablock_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_one_datablock_and_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fk** | **str**|  | 
 **update_datablock_dto** | [**UpdateDatablockDto**](UpdateDatablockDto.md)|  | 

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

# **datasets_controller_find_one_orig_datablock_and_remove**
> object datasets_controller_find_one_orig_datablock_and_remove(id, fk)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 

    try:
        api_response = api_instance.datasets_controller_find_one_orig_datablock_and_remove(id, fk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_one_orig_datablock_and_remove: %s\n" % e)
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

# **datasets_controller_find_one_orig_datablock_and_update**
> object datasets_controller_find_one_orig_datablock_and_update(id, fk, update_origdatablock_dto)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 
update_origdatablock_dto = scicat_new_be_pack.UpdateOrigdatablockDto() # UpdateOrigdatablockDto | 

    try:
        api_response = api_instance.datasets_controller_find_one_orig_datablock_and_update(id, fk, update_origdatablock_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_find_one_orig_datablock_and_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fk** | **str**|  | 
 **update_origdatablock_dto** | [**UpdateOrigdatablockDto**](UpdateOrigdatablockDto.md)|  | 

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

# **datasets_controller_fullfacet**
> list[object] datasets_controller_fullfacet(filters=filters)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    filters = None # object | Database filter to apply when retrieve all datasets (optional)

    try:
        api_response = api_instance.datasets_controller_fullfacet(filters=filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_fullfacet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**object**](.md)| Database filter to apply when retrieve all datasets | [optional] 

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

# **datasets_controller_fullquery**
> object datasets_controller_fullquery(filters=filters)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    filters = None # object | Database filter to apply when retrieve all datasets (optional)

    try:
        api_response = api_instance.datasets_controller_fullquery(filters=filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_fullquery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**object**](.md)| Database filter to apply when retrieve all datasets | [optional] 

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

# **datasets_controller_metadata_keys**
> list[str] datasets_controller_metadata_keys(filters=filters)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    filters = None # object | Database filter to apply when retrieve all metadata keys (optional)

    try:
        api_response = api_instance.datasets_controller_metadata_keys(filters=filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_metadata_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**object**](.md)| Database filter to apply when retrieve all metadata keys | [optional] 

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

# **datasets_controller_thumbnail**
> object datasets_controller_thumbnail(id)



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
    api_instance = scicat_new_be_pack.DatasetsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.datasets_controller_thumbnail(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->datasets_controller_thumbnail: %s\n" % e)
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


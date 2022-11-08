# scicat_new_be_pack.ProposalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proposals_controller_create**](ProposalsApi.md#proposals_controller_create) | **POST** /api/v3/proposals | 
[**proposals_controller_create_attachment**](ProposalsApi.md#proposals_controller_create_attachment) | **POST** /api/v3/proposals/{id}/attachments | 
[**proposals_controller_create_dataset**](ProposalsApi.md#proposals_controller_create_dataset) | **POST** /api/v3/proposals/{id}/datasets | 
[**proposals_controller_find_all**](ProposalsApi.md#proposals_controller_find_all) | **GET** /api/v3/proposals | 
[**proposals_controller_find_all_attachments**](ProposalsApi.md#proposals_controller_find_all_attachments) | **GET** /api/v3/proposals/{id}/attachments | 
[**proposals_controller_find_all_datasets**](ProposalsApi.md#proposals_controller_find_all_datasets) | **GET** /api/v3/proposals/{id}/datasets | 
[**proposals_controller_find_one**](ProposalsApi.md#proposals_controller_find_one) | **GET** /api/v3/proposals/{id} | 
[**proposals_controller_find_one_attachment_and_remove**](ProposalsApi.md#proposals_controller_find_one_attachment_and_remove) | **DELETE** /api/v3/proposals/{id}/attachments/{fk} | 
[**proposals_controller_find_one_attachment_and_update**](ProposalsApi.md#proposals_controller_find_one_attachment_and_update) | **PATCH** /api/v3/proposals/{id}/attachments/{fk} | 
[**proposals_controller_find_one_dataset_and_remove**](ProposalsApi.md#proposals_controller_find_one_dataset_and_remove) | **DELETE** /api/v3/proposals/{id}/datasets/{fk} | 
[**proposals_controller_find_one_dataset_and_update**](ProposalsApi.md#proposals_controller_find_one_dataset_and_update) | **PATCH** /api/v3/proposals/{id}/datasets/{fk} | 
[**proposals_controller_fullfacet**](ProposalsApi.md#proposals_controller_fullfacet) | **GET** /api/v3/proposals/fullfacet | 
[**proposals_controller_fullquery**](ProposalsApi.md#proposals_controller_fullquery) | **GET** /api/v3/proposals/fullquery | 
[**proposals_controller_remove**](ProposalsApi.md#proposals_controller_remove) | **DELETE** /api/v3/proposals/{id} | 
[**proposals_controller_update**](ProposalsApi.md#proposals_controller_update) | **PATCH** /api/v3/proposals/{id} | 


# **proposals_controller_create**
> Proposal proposals_controller_create(create_proposal_dto)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    create_proposal_dto = scicat_new_be_pack.CreateProposalDto() # CreateProposalDto | 

    try:
        api_response = api_instance.proposals_controller_create(create_proposal_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_proposal_dto** | [**CreateProposalDto**](CreateProposalDto.md)|  | 

### Return type

[**Proposal**](Proposal.md)

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

# **proposals_controller_create_attachment**
> Attachment proposals_controller_create_attachment(id, create_attachment_dto)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 
create_attachment_dto = scicat_new_be_pack.CreateAttachmentDto() # CreateAttachmentDto | 

    try:
        api_response = api_instance.proposals_controller_create_attachment(id, create_attachment_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_create_attachment: %s\n" % e)
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

# **proposals_controller_create_dataset**
> Dataset proposals_controller_create_dataset(id)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.proposals_controller_create_dataset(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_create_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Dataset**](Dataset.md)

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

# **proposals_controller_find_all**
> list[Proposal] proposals_controller_find_all(filters=filters)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    filters = 'filters_example' # str | Database filters to apply when retrieve all proposals (optional)

    try:
        api_response = api_instance.proposals_controller_find_all(filters=filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Database filters to apply when retrieve all proposals | [optional] 

### Return type

[**list[Proposal]**](Proposal.md)

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

# **proposals_controller_find_all_attachments**
> list[Attachment] proposals_controller_find_all_attachments(id)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.proposals_controller_find_all_attachments(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_find_all_attachments: %s\n" % e)
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

# **proposals_controller_find_all_datasets**
> object proposals_controller_find_all_datasets(id)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.proposals_controller_find_all_datasets(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_find_all_datasets: %s\n" % e)
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

# **proposals_controller_find_one**
> object proposals_controller_find_one(id)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.proposals_controller_find_one(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_find_one: %s\n" % e)
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

# **proposals_controller_find_one_attachment_and_remove**
> object proposals_controller_find_one_attachment_and_remove(id, fk)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 

    try:
        api_response = api_instance.proposals_controller_find_one_attachment_and_remove(id, fk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_find_one_attachment_and_remove: %s\n" % e)
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

# **proposals_controller_find_one_attachment_and_update**
> object proposals_controller_find_one_attachment_and_update(id, fk, update_attachment_dto)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 
update_attachment_dto = scicat_new_be_pack.UpdateAttachmentDto() # UpdateAttachmentDto | 

    try:
        api_response = api_instance.proposals_controller_find_one_attachment_and_update(id, fk, update_attachment_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_find_one_attachment_and_update: %s\n" % e)
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

# **proposals_controller_find_one_dataset_and_remove**
> object proposals_controller_find_one_dataset_and_remove(id, fk)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 

    try:
        api_response = api_instance.proposals_controller_find_one_dataset_and_remove(id, fk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_find_one_dataset_and_remove: %s\n" % e)
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

# **proposals_controller_find_one_dataset_and_update**
> object proposals_controller_find_one_dataset_and_update(id, fk, update_raw_dataset_dto)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 
fk = 'fk_example' # str | 
update_raw_dataset_dto = scicat_new_be_pack.UpdateRawDatasetDto() # UpdateRawDatasetDto | 

    try:
        api_response = api_instance.proposals_controller_find_one_dataset_and_update(id, fk, update_raw_dataset_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_find_one_dataset_and_update: %s\n" % e)
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

# **proposals_controller_fullfacet**
> list[object] proposals_controller_fullfacet()



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    
    try:
        api_response = api_instance.proposals_controller_fullfacet()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_fullfacet: %s\n" % e)
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

# **proposals_controller_fullquery**
> list[Proposal] proposals_controller_fullquery()



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    
    try:
        api_response = api_instance.proposals_controller_fullquery()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_fullquery: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Proposal]**](Proposal.md)

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

# **proposals_controller_remove**
> object proposals_controller_remove(id)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.proposals_controller_remove(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_remove: %s\n" % e)
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

# **proposals_controller_update**
> object proposals_controller_update(id, update_proposal_dto)



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
    api_instance = scicat_new_be_pack.ProposalsApi(api_client)
    id = 'id_example' # str | 
update_proposal_dto = scicat_new_be_pack.UpdateProposalDto() # UpdateProposalDto | 

    try:
        api_response = api_instance.proposals_controller_update(id, update_proposal_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProposalsApi->proposals_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_proposal_dto** | [**UpdateProposalDto**](UpdateProposalDto.md)|  | 

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


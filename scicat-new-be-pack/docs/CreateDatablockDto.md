# CreateDatablockDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**created_by** | **str** | Functional or user account name who created this instance | 
**updated_by** | **str** | Functional or user account name who last updated this instance | 
**dataset_id** | **str** |  | 
**archive_id** | **str** |  | 
**size** | **float** |  | 
**packed_size** | **float** |  | 
**chk_alg** | **str** |  | 
**version** | **str** |  | 
**data_file_list** | [**list[DataFile]**](DataFile.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


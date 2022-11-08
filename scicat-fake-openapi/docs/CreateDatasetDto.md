# CreateDatasetDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**created_by** | **str** | Functional or user account name who created this instance | [optional] 
**updated_by** | **str** | Functional or user account name who last updated this instance | [optional] 
**owner** | **str** |  | 
**owner_email** | **str** |  | [optional] 
**orcid_of_owner** | **str** |  | [optional] 
**contact_email** | **str** |  | 
**source_folder** | **str** |  | 
**source_folder_host** | **str** |  | [optional] 
**size** | **float** |  | [optional] 
**packed_size** | **float** |  | [optional] 
**number_of_files** | **float** |  | [optional] 
**number_of_files_archived** | **float** |  | [optional] 
**creation_time** | **datetime** |  | 
**type** | **str** |  | 
**validation_status** | **str** |  | [optional] 
**keywords** | **list[str]** |  | [optional] 
**description** | **str** | Dataset description | [optional] 
**dataset_name** | **str** |  | 
**classification** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**is_published** | **bool** |  | 
**history** | **list[object]** |  | [optional] 
**datasetlifecycle** | [**Lifecycle**](Lifecycle.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**instrument_id** | **str** |  | [optional] 
**techniques** | [**list[Technique]**](Technique.md) |  | [optional] 
**shared_with** | **list[str]** |  | [optional] 
**creation_location** | **str** |  | 
**principal_investigator** | **str** |  | 
**scientific_metadata** | [**object**](.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



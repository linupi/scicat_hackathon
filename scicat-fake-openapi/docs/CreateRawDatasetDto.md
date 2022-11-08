# CreateRawDatasetDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**created_by** | **str** | Functional or user account name who created this instance | 
**updated_by** | **str** | Functional or user account name who last updated this instance | 
**owner** | **str** |  | 
**owner_email** | **str** |  | 
**orcid_of_owner** | **str** |  | 
**contact_email** | **str** |  | 
**source_folder** | **str** |  | 
**source_folder_host** | **str** |  | 
**size** | **float** |  | 
**packed_size** | **float** |  | 
**number_of_files** | **float** |  | 
**number_of_files_archived** | **float** |  | 
**creation_time** | **datetime** |  | 
**type** | **str** |  | 
**validation_status** | **str** |  | 
**keywords** | **list[str]** |  | 
**description** | **str** | Dataset description | 
**dataset_name** | **str** |  | 
**classification** | **str** |  | 
**license** | **str** |  | 
**version** | **str** |  | 
**is_published** | **bool** |  | 
**history** | **list[object]** |  | 
**datasetlifecycle** | [**Lifecycle**](Lifecycle.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**instrument_id** | **str** |  | 
**techniques** | [**list[Technique]**](Technique.md) |  | 
**shared_with** | **list[str]** |  | 
**principal_investigator** | **str** |  | 
**end_time** | **datetime** |  | 
**creation_location** | **str** |  | 
**data_format** | **str** |  | 
**scientific_metadata** | [**object**](.md) |  | 
**proposal_id** | **str** |  | 
**sample_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



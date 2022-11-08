# Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**instrument_group** | **str** | Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data. | [optional] 
**created_by** | **str** |  | 
**updated_by** | **str** |  | 
**id** | **str** |  | 
**thumbnail** | **str** | Contains a thumbnail preview in base64 encoded png format for a given dataset | 
**caption** | **str** | Attachment caption to show in frontend | 
**dataset_id** | **str** |  | [optional] 
**proposal_id** | **str** |  | [optional] 
**sample_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



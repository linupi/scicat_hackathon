# CreateProposalDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**created_by** | **str** | Functional or user account name who created this instance | 
**updated_by** | **str** | Functional or user account name who last updated this instance | 
**proposal_id** | **str** |  | 
**pi_email** | **str** |  | 
**pi_firstname** | **str** |  | 
**pi_lastname** | **str** |  | 
**email** | **str** |  | 
**firstname** | **str** |  | 
**lastname** | **str** |  | 
**title** | **str** |  | 
**abstract** | **str** |  | 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



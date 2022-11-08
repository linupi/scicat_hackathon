# Proposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**instrument_group** | **str** | Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data. | [optional] 
**created_by** | **str** |  | 
**updated_by** | **str** |  | 
**proposal_id** | **str** | Globally unique identifier of a proposal, eg. PID-prefix/internal-proposal-number. PID prefix is auto prepended | 
**pi_email** | **str** | Email of principal investigator | 
**pi_firstname** | **str** | First name of principal investigator | 
**pi_lastname** | **str** | Last name of principal investigator | 
**email** | **str** | Email of main proposer | 
**firstname** | **str** | First name of main proposer | 
**lastname** | **str** | Last name of main proposer | 
**title** | **str** | The title of the proposal | 
**abstract** | **str** | The proposal abstract | 
**start_time** | **datetime** | The date when the data collection starts | [optional] 
**end_time** | **datetime** | The date when data collection finishes | [optional] 
**attachments** | [**list[Attachment]**](Attachment.md) | Small less than 16 MB attachments, envisaged for png/jpeg previews | 
**datasets** | [**list[Dataset]**](Dataset.md) |  | 
**measurement_period_list** | [**MeasurementPeriod**](MeasurementPeriod.md) | Embedded information used inside proposals to define which type of experiment as to be pursued where (at which intrument) and when. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



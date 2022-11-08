# UpdatePolicyDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | [optional] 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | [optional] 
**created_by** | **str** | Functional or user account name who created this instance | [optional] 
**updated_by** | **str** | Functional or user account name who last updated this instance | [optional] 
**manager** | **list[str]** |  | [optional] 
**tape_redundancy** | **str** |  | [optional] 
**auto_archive** | **bool** |  | [optional] 
**auto_archive_delay** | **float** |  | [optional] 
**archive_email_notification** | **bool** |  | [optional] 
**archive_emails_to_be_notified** | **list[str]** |  | [optional] 
**retrieve_email_notification** | **bool** |  | [optional] 
**retrieve_emails_to_be_notified** | **list[str]** |  | [optional] 
**embargo_period** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**instrument_group** | **str** | Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data. | [optional] 
**created_by** | **str** |  | 
**updated_by** | **str** |  | 
**id** | **str** |  | 
**manager** | **list[str]** | Defines the emails of users that can modify the policy parameters | 
**tape_redundancy** | **str** | Defines the level of redundancy in storage to minimize loss of data. Allowed values are low, medium, high. Low could e.g. mean one tape copy only, medium could mean two tape copies and high two geo-redundant tape copies | 
**auto_archive** | **bool** | Flag to indicate that a dataset should be automatically archived after ingest. If false then archive delay is ignored | 
**auto_archive_delay** | **float** | Number of days after dataset creation that (remaining) datasets are archived automatically | 
**archive_email_notification** | **bool** | Flag is true when an email notification should be sent to archiveEmailsToBeNotified upon an archive job creation | 
**archive_emails_to_be_notified** | **list[str]** | Array of additional email addresses that should be notified up an archive job creation | 
**retrieve_email_notification** | **bool** | Flag is true when an email notification should be sent to retrieveEmailsToBeNotified upon a retrieval job creation | 
**retrieve_emails_to_be_notified** | **list[str]** | Array of additional email addresses that should be notified up a retrieval job creation | 
**embargo_period** | **float** | Number of years after dataset creation before the dataset becomes public | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



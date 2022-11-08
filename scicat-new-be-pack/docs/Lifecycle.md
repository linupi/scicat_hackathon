# Lifecycle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archivable** | **bool** | Flag which is true, if dataset is available to be archived and no archive job for this dataset exists yet. | [optional] 
**retrievable** | **bool** | Flag which is true, if dataset is stored on archive system and is ready to be retrieved. | [optional] 
**publishable** | **bool** | Flag which is true, if dataset can be published. Usually requires a longterm storage option on tape or similar. | [optional] 
**date_of_disk_purging** | **datetime** | Day when dataset will be removed from disk, assuming that is already stored on tape. | [optional] 
**archive_retention_time** | **datetime** | Day when the dataset&#39;s future fate will be evaluated again, e.g. to decide if the dataset can be deleted from archive. | [optional] 
**date_of_publishing** | **datetime** | Day when dataset is supposed to become public according to data policy | [optional] 
**published_on** | **datetime** | Day when dataset was published. | [optional] 
**is_on_central_disk** | **bool** | Flag which is true, if full dataset is available on central fileserver. If false data needs to be copied from decentral storage place to  a cache server before the ingest. This information needs to be transferred to the archive system at archive time | [optional] 
**archive_status_message** | **str** | Short string defining current status of Dataset with respect to storage on disk/tape. | [optional] 
**retrieve_status_message** | **str** | Latest message for this dataset concerning retrieve from archive system. | [optional] 
**archive_return_message** | [**object**](.md) | Detailed status or error message returned by archive system when archiving this dataset. | [optional] 
**retrieve_return_message** | [**object**](.md) | Detailed status or error message returned by archive system when retrieving this dataset. | [optional] 
**exported_to** | **str** | Location of the last export destination. | [optional] 
**retrieve_integrity_check** | **bool** | Set to true when checksum tests after retrieve of datasets were successful | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



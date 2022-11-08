# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_job_initiator** | **str** | The email of the person initiating the job request | 
**type** | **str** | Type of job, e.g. archive, retrieve etc | 
**creation_time** | **datetime** | Time when job is created. Format according to chapter 5.6 internet date/time format in RFC 3339 | 
**execution_time** | **datetime** | Time when job should be executed. If not specified then the Job will be executed asap. Format according to chapter 5.6 internet date/time format in RFC 3339 | 
**job_params** | [**object**](.md) | Object of key-value pairs defining job input parameters, e.g. &#39;desinationPath&#39; for retrieve jobs or &#39;tapeCopies&#39; for archive jobs | 
**job_status_message** | **str** | Defines current status of job lifecycle | 
**dataset_list** | **list[str]** | Array of objects with keys: pid, files. The value for the pid key defines the dataset ID, the value for the files key is an array of file names. This array is either an empty array, implying that all files within the dataset are selected or an explicit list of dataset-relative file paths, which should be selected | 
**job_result_object** | [**object**](.md) | Detailed return value after job is finished | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



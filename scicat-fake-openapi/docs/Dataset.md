# Dataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**instrument_group** | **str** | Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data. | [optional] 
**created_by** | **str** |  | 
**updated_by** | **str** |  | 
**pid** | **str** | Persistent Identifier for datasets derived from UUIDv4 and prepended automatically by site specific PID prefix like 20.500.12345/ | 
**owner** | **str** | Owner or custodian of the data set, usually first name + lastname. The string may contain a list of persons, which should then be seperated by semicolons. | 
**owner_email** | **str** | Email of owner or of custodian of the data set. The string may contain a list of emails, which should then be seperated by semicolons. | 
**orcid_of_owner** | **str** | ORCID of owner/custodian. The string may contain a list of ORCID, which should then be separated by semicolons. | 
**contact_email** | **str** | Email of contact person for this dataset. The string may contain a list of emails, which should then be seperated by semicolons. | 
**source_folder** | **str** | Absolute file path on file server containing the files of this dataset, e.g. /some/path/to/sourcefolder. In case of a single file dataset, e.g. HDF5 data, it contains the path up to, but excluding the filename. Trailing slashes are removed. | 
**source_folder_host** | **str** | DNS host name of file server hosting sourceFolder, optionally including protocol e.g. [protocol://]fileserver1.example.com | 
**size** | **float** | Total size of all source files contained in source folder on disk when unpacked | 
**packed_size** | **float** | Total size of all datablock package files created for this dataset | 
**number_of_files** | **float** | Total number of lines in filelisting of all OrigDatablocks for this dataset | 
**number_of_files_archived** | **float** | Total number of lines in filelisting of all Datablocks for this dataset | 
**creation_time** | **datetime** | Time when dataset became fully available on disk, i.e. all containing files have been written. Format according to chapter 5.6 internet date/time format in RFC 3339. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server. | 
**type** | **str** | Characterize type of dataset, either &#39;base&#39; or &#39;raw&#39; or &#39;derived&#39;. Autofilled when choosing the proper inherited models | 
**validation_status** | **str** | Defines a level of trust, e.g. a measure of how much data was verified or used by other persons | 
**keywords** | **list[str]** | Array of tags associated with the meaning or contents of this dataset. Values should ideally come from defined vocabularies, taxonomies, ontologies or knowledge graphs | 
**description** | **str** | Free text explanation of contents of dataset | 
**dataset_name** | **str** | A name for the dataset, given by the creator to carry some semantic meaning. Useful for display purposes e.g. instead of displaying the pid. Will be autofilled if missing using info from sourceFolder | 
**classification** | **str** | ACIA information about AUthenticity,COnfidentiality,INtegrity and AVailability requirements of dataset. E.g. AV(ailabilty)&#x3D;medium could trigger the creation of a two tape copies. Format &#39;AV&#x3D;medium,CO&#x3D;low&#39; | 
**license** | **str** | Name of license under which data can be used | 
**version** | **str** | Version of API used in creation of dataset | 
**is_published** | **bool** | Flag is true when data are made publically available | 
**history** | **list[object]** | List of objects containing old value and new value | 
**datasetlifecycle** | [**Lifecycle**](Lifecycle.md) | For each dataset there exists an embedded dataset lifecycle document which describes the current status of the dataset during its lifetime with respect to the storage handling systems | 
**created_at** | **datetime** | Date when dataset was created. | 
**updated_at** | **datetime** | Date when the dataset was last modified. | 
**instrument_id** | **str** | ID of instrument where the data was created | [optional] 
**techniques** | [**list[Technique]**](Technique.md) | Stores the metadata information for techniques | 
**shared_with** | **list[str]** | List of users that the dataset has been shared with | 
**attachments** | [**list[Attachment]**](Attachment.md) | Small less than 16 MB attachments, envisaged for png/jpeg previews | 
**origdatablocks** | [**list[OrigDatablock]**](OrigDatablock.md) | Container list all files and their attributes which make up a dataset. Usually Filled at the time the datasets metadata is created in the data catalog. Can be used by subsequent archiving processes to create the archived datasets. | 
**datablocks** | [**list[Datablock]**](Datablock.md) | When archiving a dataset all files contained in the dataset are listed here together with their checksum information. Several datablocks can be created if the file listing is too long for a single datablock. This partitioning decision is done by the archiving system to allow for chunks of datablocks with managable sizes. E.g a dataset consisting of 10 TB of data could be split into 10 datablocks of about 1 TB each. The upper limit set by the data catalog system itself is given by the fact that documents must be smaller than 16 MB, which typically allows for datasets of about 100000 files. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



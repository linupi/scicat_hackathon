# Datablock

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_group** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**access_groups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | 
**instrument_group** | **str** | Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data. | [optional] 
**created_by** | **str** |  | 
**updated_by** | **str** |  | 
**id** | **str** | Catalog internal UUIDv4 for datablock | 
**dataset_id** | **str** | PID of the dataset to which the datablock belongs | 
**archive_id** | **str** | Unique identifier given bey archive system to the stored datablock. This id is used when data is retrieved back. | 
**size** | **float** | Total size in bytes of all files in datablock when unpacked | 
**packed_size** | **float** | Size of datablock package file | 
**chk_alg** | **str** | Algoritm used for calculation of checksums, e.g. sha2 | 
**version** | **str** | Version string defining format of how data is packed and stored in archive | 
**data_file_list** | **list[str]** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



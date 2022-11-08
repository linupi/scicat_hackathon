# MeasurementPeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **str** | Instrument or beamline identifier where measurement was pursued, e.g. /PSI/SLS/TOMCAT | 
**start** | **datetime** | Time when measurement period started, format according to chapter 5.6 internet date/time format in RFC 3339. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server | 
**end** | **datetime** | Time when measurement period ended, format according to chapter 5.6 internet date/time format in RFC 3339. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server | 
**comment** | **str** | Additional information relevant for this measurement period, e.g. if different accounts were used for data taking | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



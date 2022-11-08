# coding: utf-8

"""
    Dacat API

    SciCat backend API  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from scicat_new_be_pack.configuration import Configuration


class CreateDerivedDatasetDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'owner_group': 'str',
        'access_groups': 'list[str]',
        'created_by': 'str',
        'updated_by': 'str',
        'owner': 'str',
        'owner_email': 'str',
        'orcid_of_owner': 'str',
        'contact_email': 'str',
        'source_folder': 'str',
        'source_folder_host': 'str',
        'size': 'float',
        'packed_size': 'float',
        'number_of_files': 'float',
        'number_of_files_archived': 'float',
        'creation_time': 'datetime',
        'type': 'str',
        'validation_status': 'str',
        'keywords': 'list[str]',
        'description': 'str',
        'dataset_name': 'str',
        'classification': 'str',
        'license': 'str',
        'version': 'str',
        'is_published': 'bool',
        'history': 'list[object]',
        'datasetlifecycle': 'Lifecycle',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'instrument_id': 'str',
        'techniques': 'list[Technique]',
        'shared_with': 'list[str]',
        'investigator': 'str',
        'input_datasets': 'list[str]',
        'used_software': 'list[str]',
        'job_parameters': 'object',
        'job_log_data': 'str',
        'scientific_metadata': 'object'
    }

    attribute_map = {
        'owner_group': 'ownerGroup',
        'access_groups': 'accessGroups',
        'created_by': 'createdBy',
        'updated_by': 'updatedBy',
        'owner': 'owner',
        'owner_email': 'ownerEmail',
        'orcid_of_owner': 'orcidOfOwner',
        'contact_email': 'contactEmail',
        'source_folder': 'sourceFolder',
        'source_folder_host': 'sourceFolderHost',
        'size': 'size',
        'packed_size': 'packedSize',
        'number_of_files': 'numberOfFiles',
        'number_of_files_archived': 'numberOfFilesArchived',
        'creation_time': 'creationTime',
        'type': 'type',
        'validation_status': 'validationStatus',
        'keywords': 'keywords',
        'description': 'description',
        'dataset_name': 'datasetName',
        'classification': 'classification',
        'license': 'license',
        'version': 'version',
        'is_published': 'isPublished',
        'history': 'history',
        'datasetlifecycle': 'datasetlifecycle',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'instrument_id': 'instrumentId',
        'techniques': 'techniques',
        'shared_with': 'sharedWith',
        'investigator': 'investigator',
        'input_datasets': 'inputDatasets',
        'used_software': 'usedSoftware',
        'job_parameters': 'jobParameters',
        'job_log_data': 'jobLogData',
        'scientific_metadata': 'scientificMetadata'
    }

    def __init__(self, owner_group=None, access_groups=None, created_by=None, updated_by=None, owner=None, owner_email=None, orcid_of_owner=None, contact_email=None, source_folder=None, source_folder_host=None, size=None, packed_size=None, number_of_files=None, number_of_files_archived=None, creation_time=None, type=None, validation_status=None, keywords=None, description=None, dataset_name=None, classification=None, license=None, version=None, is_published=None, history=None, datasetlifecycle=None, created_at=None, updated_at=None, instrument_id=None, techniques=None, shared_with=None, investigator=None, input_datasets=None, used_software=None, job_parameters=None, job_log_data=None, scientific_metadata=None, local_vars_configuration=None):  # noqa: E501
        """CreateDerivedDatasetDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner_group = None
        self._access_groups = None
        self._created_by = None
        self._updated_by = None
        self._owner = None
        self._owner_email = None
        self._orcid_of_owner = None
        self._contact_email = None
        self._source_folder = None
        self._source_folder_host = None
        self._size = None
        self._packed_size = None
        self._number_of_files = None
        self._number_of_files_archived = None
        self._creation_time = None
        self._type = None
        self._validation_status = None
        self._keywords = None
        self._description = None
        self._dataset_name = None
        self._classification = None
        self._license = None
        self._version = None
        self._is_published = None
        self._history = None
        self._datasetlifecycle = None
        self._created_at = None
        self._updated_at = None
        self._instrument_id = None
        self._techniques = None
        self._shared_with = None
        self._investigator = None
        self._input_datasets = None
        self._used_software = None
        self._job_parameters = None
        self._job_log_data = None
        self._scientific_metadata = None
        self.discriminator = None

        self.owner_group = owner_group
        self.access_groups = access_groups
        self.created_by = created_by
        self.updated_by = updated_by
        self.owner = owner
        self.owner_email = owner_email
        self.orcid_of_owner = orcid_of_owner
        self.contact_email = contact_email
        self.source_folder = source_folder
        self.source_folder_host = source_folder_host
        self.size = size
        self.packed_size = packed_size
        self.number_of_files = number_of_files
        self.number_of_files_archived = number_of_files_archived
        self.creation_time = creation_time
        self.type = type
        self.validation_status = validation_status
        self.keywords = keywords
        self.description = description
        self.dataset_name = dataset_name
        self.classification = classification
        self.license = license
        self.version = version
        self.is_published = is_published
        self.history = history
        self.datasetlifecycle = datasetlifecycle
        self.created_at = created_at
        self.updated_at = updated_at
        self.instrument_id = instrument_id
        self.techniques = techniques
        self.shared_with = shared_with
        self.investigator = investigator
        self.input_datasets = input_datasets
        self.used_software = used_software
        self.job_parameters = job_parameters
        self.job_log_data = job_log_data
        self.scientific_metadata = scientific_metadata

    @property
    def owner_group(self):
        """Gets the owner_group of this CreateDerivedDatasetDto.  # noqa: E501

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :return: The owner_group of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._owner_group

    @owner_group.setter
    def owner_group(self, owner_group):
        """Sets the owner_group of this CreateDerivedDatasetDto.

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :param owner_group: The owner_group of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_group is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_group`, must not be `None`")  # noqa: E501

        self._owner_group = owner_group

    @property
    def access_groups(self):
        """Gets the access_groups of this CreateDerivedDatasetDto.  # noqa: E501

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :return: The access_groups of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_groups

    @access_groups.setter
    def access_groups(self, access_groups):
        """Sets the access_groups of this CreateDerivedDatasetDto.

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :param access_groups: The access_groups of this CreateDerivedDatasetDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and access_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `access_groups`, must not be `None`")  # noqa: E501

        self._access_groups = access_groups

    @property
    def created_by(self):
        """Gets the created_by of this CreateDerivedDatasetDto.  # noqa: E501

        Functional or user account name who created this instance  # noqa: E501

        :return: The created_by of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CreateDerivedDatasetDto.

        Functional or user account name who created this instance  # noqa: E501

        :param created_by: The created_by of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this CreateDerivedDatasetDto.  # noqa: E501

        Functional or user account name who last updated this instance  # noqa: E501

        :return: The updated_by of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this CreateDerivedDatasetDto.

        Functional or user account name who last updated this instance  # noqa: E501

        :param updated_by: The updated_by of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_by is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_by`, must not be `None`")  # noqa: E501

        self._updated_by = updated_by

    @property
    def owner(self):
        """Gets the owner of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The owner of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateDerivedDatasetDto.


        :param owner: The owner of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def owner_email(self):
        """Gets the owner_email of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The owner_email of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """Sets the owner_email of this CreateDerivedDatasetDto.


        :param owner_email: The owner_email of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_email is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_email`, must not be `None`")  # noqa: E501

        self._owner_email = owner_email

    @property
    def orcid_of_owner(self):
        """Gets the orcid_of_owner of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The orcid_of_owner of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._orcid_of_owner

    @orcid_of_owner.setter
    def orcid_of_owner(self, orcid_of_owner):
        """Sets the orcid_of_owner of this CreateDerivedDatasetDto.


        :param orcid_of_owner: The orcid_of_owner of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and orcid_of_owner is None:  # noqa: E501
            raise ValueError("Invalid value for `orcid_of_owner`, must not be `None`")  # noqa: E501

        self._orcid_of_owner = orcid_of_owner

    @property
    def contact_email(self):
        """Gets the contact_email of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The contact_email of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this CreateDerivedDatasetDto.


        :param contact_email: The contact_email of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contact_email is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_email`, must not be `None`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def source_folder(self):
        """Gets the source_folder of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The source_folder of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._source_folder

    @source_folder.setter
    def source_folder(self, source_folder):
        """Sets the source_folder of this CreateDerivedDatasetDto.


        :param source_folder: The source_folder of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source_folder is None:  # noqa: E501
            raise ValueError("Invalid value for `source_folder`, must not be `None`")  # noqa: E501

        self._source_folder = source_folder

    @property
    def source_folder_host(self):
        """Gets the source_folder_host of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The source_folder_host of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._source_folder_host

    @source_folder_host.setter
    def source_folder_host(self, source_folder_host):
        """Sets the source_folder_host of this CreateDerivedDatasetDto.


        :param source_folder_host: The source_folder_host of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source_folder_host is None:  # noqa: E501
            raise ValueError("Invalid value for `source_folder_host`, must not be `None`")  # noqa: E501

        self._source_folder_host = source_folder_host

    @property
    def size(self):
        """Gets the size of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The size of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateDerivedDatasetDto.


        :param size: The size of this CreateDerivedDatasetDto.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def packed_size(self):
        """Gets the packed_size of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The packed_size of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: float
        """
        return self._packed_size

    @packed_size.setter
    def packed_size(self, packed_size):
        """Sets the packed_size of this CreateDerivedDatasetDto.


        :param packed_size: The packed_size of this CreateDerivedDatasetDto.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and packed_size is None:  # noqa: E501
            raise ValueError("Invalid value for `packed_size`, must not be `None`")  # noqa: E501

        self._packed_size = packed_size

    @property
    def number_of_files(self):
        """Gets the number_of_files of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The number_of_files of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: float
        """
        return self._number_of_files

    @number_of_files.setter
    def number_of_files(self, number_of_files):
        """Sets the number_of_files of this CreateDerivedDatasetDto.


        :param number_of_files: The number_of_files of this CreateDerivedDatasetDto.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and number_of_files is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_files`, must not be `None`")  # noqa: E501

        self._number_of_files = number_of_files

    @property
    def number_of_files_archived(self):
        """Gets the number_of_files_archived of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The number_of_files_archived of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: float
        """
        return self._number_of_files_archived

    @number_of_files_archived.setter
    def number_of_files_archived(self, number_of_files_archived):
        """Sets the number_of_files_archived of this CreateDerivedDatasetDto.


        :param number_of_files_archived: The number_of_files_archived of this CreateDerivedDatasetDto.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and number_of_files_archived is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_files_archived`, must not be `None`")  # noqa: E501

        self._number_of_files_archived = number_of_files_archived

    @property
    def creation_time(self):
        """Gets the creation_time of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The creation_time of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this CreateDerivedDatasetDto.


        :param creation_time: The creation_time of this CreateDerivedDatasetDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and creation_time is None:  # noqa: E501
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def type(self):
        """Gets the type of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The type of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateDerivedDatasetDto.


        :param type: The type of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def validation_status(self):
        """Gets the validation_status of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The validation_status of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """Sets the validation_status of this CreateDerivedDatasetDto.


        :param validation_status: The validation_status of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and validation_status is None:  # noqa: E501
            raise ValueError("Invalid value for `validation_status`, must not be `None`")  # noqa: E501

        self._validation_status = validation_status

    @property
    def keywords(self):
        """Gets the keywords of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The keywords of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this CreateDerivedDatasetDto.


        :param keywords: The keywords of this CreateDerivedDatasetDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and keywords is None:  # noqa: E501
            raise ValueError("Invalid value for `keywords`, must not be `None`")  # noqa: E501

        self._keywords = keywords

    @property
    def description(self):
        """Gets the description of this CreateDerivedDatasetDto.  # noqa: E501

        Dataset description  # noqa: E501

        :return: The description of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDerivedDatasetDto.

        Dataset description  # noqa: E501

        :param description: The description of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def dataset_name(self):
        """Gets the dataset_name of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The dataset_name of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this CreateDerivedDatasetDto.


        :param dataset_name: The dataset_name of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dataset_name is None:  # noqa: E501
            raise ValueError("Invalid value for `dataset_name`, must not be `None`")  # noqa: E501

        self._dataset_name = dataset_name

    @property
    def classification(self):
        """Gets the classification of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The classification of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this CreateDerivedDatasetDto.


        :param classification: The classification of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and classification is None:  # noqa: E501
            raise ValueError("Invalid value for `classification`, must not be `None`")  # noqa: E501

        self._classification = classification

    @property
    def license(self):
        """Gets the license of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The license of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this CreateDerivedDatasetDto.


        :param license: The license of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and license is None:  # noqa: E501
            raise ValueError("Invalid value for `license`, must not be `None`")  # noqa: E501

        self._license = license

    @property
    def version(self):
        """Gets the version of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The version of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateDerivedDatasetDto.


        :param version: The version of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def is_published(self):
        """Gets the is_published of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The is_published of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        """Sets the is_published of this CreateDerivedDatasetDto.


        :param is_published: The is_published of this CreateDerivedDatasetDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_published is None:  # noqa: E501
            raise ValueError("Invalid value for `is_published`, must not be `None`")  # noqa: E501

        self._is_published = is_published

    @property
    def history(self):
        """Gets the history of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The history of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: list[object]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this CreateDerivedDatasetDto.


        :param history: The history of this CreateDerivedDatasetDto.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and history is None:  # noqa: E501
            raise ValueError("Invalid value for `history`, must not be `None`")  # noqa: E501

        self._history = history

    @property
    def datasetlifecycle(self):
        """Gets the datasetlifecycle of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The datasetlifecycle of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: Lifecycle
        """
        return self._datasetlifecycle

    @datasetlifecycle.setter
    def datasetlifecycle(self, datasetlifecycle):
        """Sets the datasetlifecycle of this CreateDerivedDatasetDto.


        :param datasetlifecycle: The datasetlifecycle of this CreateDerivedDatasetDto.  # noqa: E501
        :type: Lifecycle
        """
        if self.local_vars_configuration.client_side_validation and datasetlifecycle is None:  # noqa: E501
            raise ValueError("Invalid value for `datasetlifecycle`, must not be `None`")  # noqa: E501

        self._datasetlifecycle = datasetlifecycle

    @property
    def created_at(self):
        """Gets the created_at of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The created_at of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateDerivedDatasetDto.


        :param created_at: The created_at of this CreateDerivedDatasetDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The updated_at of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateDerivedDatasetDto.


        :param updated_at: The updated_at of this CreateDerivedDatasetDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def instrument_id(self):
        """Gets the instrument_id of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The instrument_id of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this CreateDerivedDatasetDto.


        :param instrument_id: The instrument_id of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_id`, must not be `None`")  # noqa: E501

        self._instrument_id = instrument_id

    @property
    def techniques(self):
        """Gets the techniques of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The techniques of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: list[Technique]
        """
        return self._techniques

    @techniques.setter
    def techniques(self, techniques):
        """Sets the techniques of this CreateDerivedDatasetDto.


        :param techniques: The techniques of this CreateDerivedDatasetDto.  # noqa: E501
        :type: list[Technique]
        """
        if self.local_vars_configuration.client_side_validation and techniques is None:  # noqa: E501
            raise ValueError("Invalid value for `techniques`, must not be `None`")  # noqa: E501

        self._techniques = techniques

    @property
    def shared_with(self):
        """Gets the shared_with of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The shared_with of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_with

    @shared_with.setter
    def shared_with(self, shared_with):
        """Sets the shared_with of this CreateDerivedDatasetDto.


        :param shared_with: The shared_with of this CreateDerivedDatasetDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and shared_with is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_with`, must not be `None`")  # noqa: E501

        self._shared_with = shared_with

    @property
    def investigator(self):
        """Gets the investigator of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The investigator of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._investigator

    @investigator.setter
    def investigator(self, investigator):
        """Sets the investigator of this CreateDerivedDatasetDto.


        :param investigator: The investigator of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and investigator is None:  # noqa: E501
            raise ValueError("Invalid value for `investigator`, must not be `None`")  # noqa: E501

        self._investigator = investigator

    @property
    def input_datasets(self):
        """Gets the input_datasets of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The input_datasets of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_datasets

    @input_datasets.setter
    def input_datasets(self, input_datasets):
        """Sets the input_datasets of this CreateDerivedDatasetDto.


        :param input_datasets: The input_datasets of this CreateDerivedDatasetDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and input_datasets is None:  # noqa: E501
            raise ValueError("Invalid value for `input_datasets`, must not be `None`")  # noqa: E501

        self._input_datasets = input_datasets

    @property
    def used_software(self):
        """Gets the used_software of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The used_software of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._used_software

    @used_software.setter
    def used_software(self, used_software):
        """Sets the used_software of this CreateDerivedDatasetDto.


        :param used_software: The used_software of this CreateDerivedDatasetDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and used_software is None:  # noqa: E501
            raise ValueError("Invalid value for `used_software`, must not be `None`")  # noqa: E501

        self._used_software = used_software

    @property
    def job_parameters(self):
        """Gets the job_parameters of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The job_parameters of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: object
        """
        return self._job_parameters

    @job_parameters.setter
    def job_parameters(self, job_parameters):
        """Sets the job_parameters of this CreateDerivedDatasetDto.


        :param job_parameters: The job_parameters of this CreateDerivedDatasetDto.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and job_parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `job_parameters`, must not be `None`")  # noqa: E501

        self._job_parameters = job_parameters

    @property
    def job_log_data(self):
        """Gets the job_log_data of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The job_log_data of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: str
        """
        return self._job_log_data

    @job_log_data.setter
    def job_log_data(self, job_log_data):
        """Sets the job_log_data of this CreateDerivedDatasetDto.


        :param job_log_data: The job_log_data of this CreateDerivedDatasetDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and job_log_data is None:  # noqa: E501
            raise ValueError("Invalid value for `job_log_data`, must not be `None`")  # noqa: E501

        self._job_log_data = job_log_data

    @property
    def scientific_metadata(self):
        """Gets the scientific_metadata of this CreateDerivedDatasetDto.  # noqa: E501


        :return: The scientific_metadata of this CreateDerivedDatasetDto.  # noqa: E501
        :rtype: object
        """
        return self._scientific_metadata

    @scientific_metadata.setter
    def scientific_metadata(self, scientific_metadata):
        """Sets the scientific_metadata of this CreateDerivedDatasetDto.


        :param scientific_metadata: The scientific_metadata of this CreateDerivedDatasetDto.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and scientific_metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `scientific_metadata`, must not be `None`")  # noqa: E501

        self._scientific_metadata = scientific_metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateDerivedDatasetDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDerivedDatasetDto):
            return True

        return self.to_dict() != other.to_dict()

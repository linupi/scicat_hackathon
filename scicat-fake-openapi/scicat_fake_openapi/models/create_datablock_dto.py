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

from scicat_fake_openapi.configuration import Configuration


class CreateDatablockDto(object):
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
        'dataset_id': 'str',
        'archive_id': 'str',
        'size': 'float',
        'packed_size': 'float',
        'chk_alg': 'str',
        'version': 'str',
        'data_file_list': 'list[DataFile]'
    }

    attribute_map = {
        'owner_group': 'ownerGroup',
        'access_groups': 'accessGroups',
        'created_by': 'createdBy',
        'updated_by': 'updatedBy',
        'dataset_id': 'datasetId',
        'archive_id': 'archiveId',
        'size': 'size',
        'packed_size': 'packedSize',
        'chk_alg': 'chkAlg',
        'version': 'version',
        'data_file_list': 'dataFileList'
    }

    def __init__(self, owner_group=None, access_groups=None, created_by=None, updated_by=None, dataset_id=None, archive_id=None, size=None, packed_size=None, chk_alg=None, version=None, data_file_list=None, local_vars_configuration=None):  # noqa: E501
        """CreateDatablockDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner_group = None
        self._access_groups = None
        self._created_by = None
        self._updated_by = None
        self._dataset_id = None
        self._archive_id = None
        self._size = None
        self._packed_size = None
        self._chk_alg = None
        self._version = None
        self._data_file_list = None
        self.discriminator = None

        self.owner_group = owner_group
        self.access_groups = access_groups
        self.created_by = created_by
        self.updated_by = updated_by
        self.dataset_id = dataset_id
        self.archive_id = archive_id
        self.size = size
        self.packed_size = packed_size
        self.chk_alg = chk_alg
        self.version = version
        self.data_file_list = data_file_list

    @property
    def owner_group(self):
        """Gets the owner_group of this CreateDatablockDto.  # noqa: E501

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :return: The owner_group of this CreateDatablockDto.  # noqa: E501
        :rtype: str
        """
        return self._owner_group

    @owner_group.setter
    def owner_group(self, owner_group):
        """Sets the owner_group of this CreateDatablockDto.

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :param owner_group: The owner_group of this CreateDatablockDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_group is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_group`, must not be `None`")  # noqa: E501

        self._owner_group = owner_group

    @property
    def access_groups(self):
        """Gets the access_groups of this CreateDatablockDto.  # noqa: E501

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :return: The access_groups of this CreateDatablockDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_groups

    @access_groups.setter
    def access_groups(self, access_groups):
        """Sets the access_groups of this CreateDatablockDto.

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :param access_groups: The access_groups of this CreateDatablockDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and access_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `access_groups`, must not be `None`")  # noqa: E501

        self._access_groups = access_groups

    @property
    def created_by(self):
        """Gets the created_by of this CreateDatablockDto.  # noqa: E501

        Functional or user account name who created this instance  # noqa: E501

        :return: The created_by of this CreateDatablockDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CreateDatablockDto.

        Functional or user account name who created this instance  # noqa: E501

        :param created_by: The created_by of this CreateDatablockDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this CreateDatablockDto.  # noqa: E501

        Functional or user account name who last updated this instance  # noqa: E501

        :return: The updated_by of this CreateDatablockDto.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this CreateDatablockDto.

        Functional or user account name who last updated this instance  # noqa: E501

        :param updated_by: The updated_by of this CreateDatablockDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_by is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_by`, must not be `None`")  # noqa: E501

        self._updated_by = updated_by

    @property
    def dataset_id(self):
        """Gets the dataset_id of this CreateDatablockDto.  # noqa: E501


        :return: The dataset_id of this CreateDatablockDto.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this CreateDatablockDto.


        :param dataset_id: The dataset_id of this CreateDatablockDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dataset_id is None:  # noqa: E501
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def archive_id(self):
        """Gets the archive_id of this CreateDatablockDto.  # noqa: E501


        :return: The archive_id of this CreateDatablockDto.  # noqa: E501
        :rtype: str
        """
        return self._archive_id

    @archive_id.setter
    def archive_id(self, archive_id):
        """Sets the archive_id of this CreateDatablockDto.


        :param archive_id: The archive_id of this CreateDatablockDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and archive_id is None:  # noqa: E501
            raise ValueError("Invalid value for `archive_id`, must not be `None`")  # noqa: E501

        self._archive_id = archive_id

    @property
    def size(self):
        """Gets the size of this CreateDatablockDto.  # noqa: E501


        :return: The size of this CreateDatablockDto.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateDatablockDto.


        :param size: The size of this CreateDatablockDto.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def packed_size(self):
        """Gets the packed_size of this CreateDatablockDto.  # noqa: E501


        :return: The packed_size of this CreateDatablockDto.  # noqa: E501
        :rtype: float
        """
        return self._packed_size

    @packed_size.setter
    def packed_size(self, packed_size):
        """Sets the packed_size of this CreateDatablockDto.


        :param packed_size: The packed_size of this CreateDatablockDto.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and packed_size is None:  # noqa: E501
            raise ValueError("Invalid value for `packed_size`, must not be `None`")  # noqa: E501

        self._packed_size = packed_size

    @property
    def chk_alg(self):
        """Gets the chk_alg of this CreateDatablockDto.  # noqa: E501


        :return: The chk_alg of this CreateDatablockDto.  # noqa: E501
        :rtype: str
        """
        return self._chk_alg

    @chk_alg.setter
    def chk_alg(self, chk_alg):
        """Sets the chk_alg of this CreateDatablockDto.


        :param chk_alg: The chk_alg of this CreateDatablockDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and chk_alg is None:  # noqa: E501
            raise ValueError("Invalid value for `chk_alg`, must not be `None`")  # noqa: E501

        self._chk_alg = chk_alg

    @property
    def version(self):
        """Gets the version of this CreateDatablockDto.  # noqa: E501


        :return: The version of this CreateDatablockDto.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateDatablockDto.


        :param version: The version of this CreateDatablockDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def data_file_list(self):
        """Gets the data_file_list of this CreateDatablockDto.  # noqa: E501


        :return: The data_file_list of this CreateDatablockDto.  # noqa: E501
        :rtype: list[DataFile]
        """
        return self._data_file_list

    @data_file_list.setter
    def data_file_list(self, data_file_list):
        """Sets the data_file_list of this CreateDatablockDto.


        :param data_file_list: The data_file_list of this CreateDatablockDto.  # noqa: E501
        :type: list[DataFile]
        """
        if self.local_vars_configuration.client_side_validation and data_file_list is None:  # noqa: E501
            raise ValueError("Invalid value for `data_file_list`, must not be `None`")  # noqa: E501

        self._data_file_list = data_file_list

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
        if not isinstance(other, CreateDatablockDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDatablockDto):
            return True

        return self.to_dict() != other.to_dict()

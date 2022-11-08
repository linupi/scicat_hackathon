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


class OrigDatablock(object):
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
        'instrument_group': 'str',
        'created_by': 'str',
        'updated_by': 'str',
        'id': 'str',
        'dataset_id': 'str',
        'size': 'float',
        'data_file_list': 'list[str]'
    }

    attribute_map = {
        'owner_group': 'ownerGroup',
        'access_groups': 'accessGroups',
        'instrument_group': 'instrumentGroup',
        'created_by': 'createdBy',
        'updated_by': 'updatedBy',
        'id': '_id',
        'dataset_id': 'datasetId',
        'size': 'size',
        'data_file_list': 'dataFileList'
    }

    def __init__(self, owner_group=None, access_groups=None, instrument_group=None, created_by=None, updated_by=None, id=None, dataset_id=None, size=None, data_file_list=None, local_vars_configuration=None):  # noqa: E501
        """OrigDatablock - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner_group = None
        self._access_groups = None
        self._instrument_group = None
        self._created_by = None
        self._updated_by = None
        self._id = None
        self._dataset_id = None
        self._size = None
        self._data_file_list = None
        self.discriminator = None

        self.owner_group = owner_group
        self.access_groups = access_groups
        if instrument_group is not None:
            self.instrument_group = instrument_group
        self.created_by = created_by
        self.updated_by = updated_by
        self.id = id
        self.dataset_id = dataset_id
        self.size = size
        self.data_file_list = data_file_list

    @property
    def owner_group(self):
        """Gets the owner_group of this OrigDatablock.  # noqa: E501

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :return: The owner_group of this OrigDatablock.  # noqa: E501
        :rtype: str
        """
        return self._owner_group

    @owner_group.setter
    def owner_group(self, owner_group):
        """Sets the owner_group of this OrigDatablock.

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :param owner_group: The owner_group of this OrigDatablock.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_group is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_group`, must not be `None`")  # noqa: E501

        self._owner_group = owner_group

    @property
    def access_groups(self):
        """Gets the access_groups of this OrigDatablock.  # noqa: E501

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :return: The access_groups of this OrigDatablock.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_groups

    @access_groups.setter
    def access_groups(self, access_groups):
        """Sets the access_groups of this OrigDatablock.

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :param access_groups: The access_groups of this OrigDatablock.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and access_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `access_groups`, must not be `None`")  # noqa: E501

        self._access_groups = access_groups

    @property
    def instrument_group(self):
        """Gets the instrument_group of this OrigDatablock.  # noqa: E501

        Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data.  # noqa: E501

        :return: The instrument_group of this OrigDatablock.  # noqa: E501
        :rtype: str
        """
        return self._instrument_group

    @instrument_group.setter
    def instrument_group(self, instrument_group):
        """Sets the instrument_group of this OrigDatablock.

        Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data.  # noqa: E501

        :param instrument_group: The instrument_group of this OrigDatablock.  # noqa: E501
        :type: str
        """

        self._instrument_group = instrument_group

    @property
    def created_by(self):
        """Gets the created_by of this OrigDatablock.  # noqa: E501


        :return: The created_by of this OrigDatablock.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OrigDatablock.


        :param created_by: The created_by of this OrigDatablock.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this OrigDatablock.  # noqa: E501


        :return: The updated_by of this OrigDatablock.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this OrigDatablock.


        :param updated_by: The updated_by of this OrigDatablock.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_by is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_by`, must not be `None`")  # noqa: E501

        self._updated_by = updated_by

    @property
    def id(self):
        """Gets the id of this OrigDatablock.  # noqa: E501


        :return: The id of this OrigDatablock.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrigDatablock.


        :param id: The id of this OrigDatablock.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def dataset_id(self):
        """Gets the dataset_id of this OrigDatablock.  # noqa: E501

        PID of the dataset to which the orig datablock belongs.  # noqa: E501

        :return: The dataset_id of this OrigDatablock.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this OrigDatablock.

        PID of the dataset to which the orig datablock belongs.  # noqa: E501

        :param dataset_id: The dataset_id of this OrigDatablock.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dataset_id is None:  # noqa: E501
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def size(self):
        """Gets the size of this OrigDatablock.  # noqa: E501

        Total size in bytes of all files contained in the dataFileList  # noqa: E501

        :return: The size of this OrigDatablock.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OrigDatablock.

        Total size in bytes of all files contained in the dataFileList  # noqa: E501

        :param size: The size of this OrigDatablock.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def data_file_list(self):
        """Gets the data_file_list of this OrigDatablock.  # noqa: E501

        Embedded schema definition for which fields are required for each file  # noqa: E501

        :return: The data_file_list of this OrigDatablock.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_file_list

    @data_file_list.setter
    def data_file_list(self, data_file_list):
        """Sets the data_file_list of this OrigDatablock.

        Embedded schema definition for which fields are required for each file  # noqa: E501

        :param data_file_list: The data_file_list of this OrigDatablock.  # noqa: E501
        :type: list[str]
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
        if not isinstance(other, OrigDatablock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrigDatablock):
            return True

        return self.to_dict() != other.to_dict()

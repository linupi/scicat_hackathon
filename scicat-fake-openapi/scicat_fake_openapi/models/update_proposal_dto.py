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


class UpdateProposalDto(object):
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
        'proposal_id': 'str',
        'pi_email': 'str',
        'pi_firstname': 'str',
        'pi_lastname': 'str',
        'email': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'title': 'str',
        'abstract': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'owner_group': 'ownerGroup',
        'access_groups': 'accessGroups',
        'created_by': 'createdBy',
        'updated_by': 'updatedBy',
        'proposal_id': 'proposalId',
        'pi_email': 'pi_email',
        'pi_firstname': 'pi_firstname',
        'pi_lastname': 'pi_lastname',
        'email': 'email',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'title': 'title',
        'abstract': 'abstract',
        'start_time': 'startTime',
        'end_time': 'endTime'
    }

    def __init__(self, owner_group=None, access_groups=None, created_by=None, updated_by=None, proposal_id=None, pi_email=None, pi_firstname=None, pi_lastname=None, email=None, firstname=None, lastname=None, title=None, abstract=None, start_time=None, end_time=None, local_vars_configuration=None):  # noqa: E501
        """UpdateProposalDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner_group = None
        self._access_groups = None
        self._created_by = None
        self._updated_by = None
        self._proposal_id = None
        self._pi_email = None
        self._pi_firstname = None
        self._pi_lastname = None
        self._email = None
        self._firstname = None
        self._lastname = None
        self._title = None
        self._abstract = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if owner_group is not None:
            self.owner_group = owner_group
        if access_groups is not None:
            self.access_groups = access_groups
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if proposal_id is not None:
            self.proposal_id = proposal_id
        if pi_email is not None:
            self.pi_email = pi_email
        if pi_firstname is not None:
            self.pi_firstname = pi_firstname
        if pi_lastname is not None:
            self.pi_lastname = pi_lastname
        if email is not None:
            self.email = email
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if title is not None:
            self.title = title
        if abstract is not None:
            self.abstract = abstract
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def owner_group(self):
        """Gets the owner_group of this UpdateProposalDto.  # noqa: E501

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :return: The owner_group of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._owner_group

    @owner_group.setter
    def owner_group(self, owner_group):
        """Sets the owner_group of this UpdateProposalDto.

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :param owner_group: The owner_group of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._owner_group = owner_group

    @property
    def access_groups(self):
        """Gets the access_groups of this UpdateProposalDto.  # noqa: E501

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :return: The access_groups of this UpdateProposalDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_groups

    @access_groups.setter
    def access_groups(self, access_groups):
        """Sets the access_groups of this UpdateProposalDto.

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :param access_groups: The access_groups of this UpdateProposalDto.  # noqa: E501
        :type: list[str]
        """

        self._access_groups = access_groups

    @property
    def created_by(self):
        """Gets the created_by of this UpdateProposalDto.  # noqa: E501

        Functional or user account name who created this instance  # noqa: E501

        :return: The created_by of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UpdateProposalDto.

        Functional or user account name who created this instance  # noqa: E501

        :param created_by: The created_by of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this UpdateProposalDto.  # noqa: E501

        Functional or user account name who last updated this instance  # noqa: E501

        :return: The updated_by of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this UpdateProposalDto.

        Functional or user account name who last updated this instance  # noqa: E501

        :param updated_by: The updated_by of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def proposal_id(self):
        """Gets the proposal_id of this UpdateProposalDto.  # noqa: E501


        :return: The proposal_id of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._proposal_id

    @proposal_id.setter
    def proposal_id(self, proposal_id):
        """Sets the proposal_id of this UpdateProposalDto.


        :param proposal_id: The proposal_id of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._proposal_id = proposal_id

    @property
    def pi_email(self):
        """Gets the pi_email of this UpdateProposalDto.  # noqa: E501


        :return: The pi_email of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._pi_email

    @pi_email.setter
    def pi_email(self, pi_email):
        """Sets the pi_email of this UpdateProposalDto.


        :param pi_email: The pi_email of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._pi_email = pi_email

    @property
    def pi_firstname(self):
        """Gets the pi_firstname of this UpdateProposalDto.  # noqa: E501


        :return: The pi_firstname of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._pi_firstname

    @pi_firstname.setter
    def pi_firstname(self, pi_firstname):
        """Sets the pi_firstname of this UpdateProposalDto.


        :param pi_firstname: The pi_firstname of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._pi_firstname = pi_firstname

    @property
    def pi_lastname(self):
        """Gets the pi_lastname of this UpdateProposalDto.  # noqa: E501


        :return: The pi_lastname of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._pi_lastname

    @pi_lastname.setter
    def pi_lastname(self, pi_lastname):
        """Sets the pi_lastname of this UpdateProposalDto.


        :param pi_lastname: The pi_lastname of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._pi_lastname = pi_lastname

    @property
    def email(self):
        """Gets the email of this UpdateProposalDto.  # noqa: E501


        :return: The email of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateProposalDto.


        :param email: The email of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this UpdateProposalDto.  # noqa: E501


        :return: The firstname of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UpdateProposalDto.


        :param firstname: The firstname of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UpdateProposalDto.  # noqa: E501


        :return: The lastname of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UpdateProposalDto.


        :param lastname: The lastname of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def title(self):
        """Gets the title of this UpdateProposalDto.  # noqa: E501


        :return: The title of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateProposalDto.


        :param title: The title of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def abstract(self):
        """Gets the abstract of this UpdateProposalDto.  # noqa: E501


        :return: The abstract of this UpdateProposalDto.  # noqa: E501
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract):
        """Sets the abstract of this UpdateProposalDto.


        :param abstract: The abstract of this UpdateProposalDto.  # noqa: E501
        :type: str
        """

        self._abstract = abstract

    @property
    def start_time(self):
        """Gets the start_time of this UpdateProposalDto.  # noqa: E501


        :return: The start_time of this UpdateProposalDto.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UpdateProposalDto.


        :param start_time: The start_time of this UpdateProposalDto.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this UpdateProposalDto.  # noqa: E501


        :return: The end_time of this UpdateProposalDto.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UpdateProposalDto.


        :param end_time: The end_time of this UpdateProposalDto.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

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
        if not isinstance(other, UpdateProposalDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateProposalDto):
            return True

        return self.to_dict() != other.to_dict()
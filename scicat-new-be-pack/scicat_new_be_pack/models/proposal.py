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


class Proposal(object):
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
        'end_time': 'datetime',
        'attachments': 'list[Attachment]',
        'datasets': 'list[Dataset]',
        'measurement_period_list': 'MeasurementPeriod'
    }

    attribute_map = {
        'owner_group': 'ownerGroup',
        'access_groups': 'accessGroups',
        'instrument_group': 'instrumentGroup',
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
        'end_time': 'endTime',
        'attachments': 'attachments',
        'datasets': 'datasets',
        'measurement_period_list': 'MeasurementPeriodList'
    }

    def __init__(self, owner_group=None, access_groups=None, instrument_group=None, created_by=None, updated_by=None, proposal_id=None, pi_email=None, pi_firstname=None, pi_lastname=None, email=None, firstname=None, lastname=None, title=None, abstract=None, start_time=None, end_time=None, attachments=None, datasets=None, measurement_period_list=None, local_vars_configuration=None):  # noqa: E501
        """Proposal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owner_group = None
        self._access_groups = None
        self._instrument_group = None
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
        self._attachments = None
        self._datasets = None
        self._measurement_period_list = None
        self.discriminator = None

        self.owner_group = owner_group
        self.access_groups = access_groups
        if instrument_group is not None:
            self.instrument_group = instrument_group
        self.created_by = created_by
        self.updated_by = updated_by
        self.proposal_id = proposal_id
        self.pi_email = pi_email
        self.pi_firstname = pi_firstname
        self.pi_lastname = pi_lastname
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.abstract = abstract
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.attachments = attachments
        self.datasets = datasets
        self.measurement_period_list = measurement_period_list

    @property
    def owner_group(self):
        """Gets the owner_group of this Proposal.  # noqa: E501

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :return: The owner_group of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._owner_group

    @owner_group.setter
    def owner_group(self, owner_group):
        """Sets the owner_group of this Proposal.

        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151  # noqa: E501

        :param owner_group: The owner_group of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_group is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_group`, must not be `None`")  # noqa: E501

        self._owner_group = owner_group

    @property
    def access_groups(self):
        """Gets the access_groups of this Proposal.  # noqa: E501

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :return: The access_groups of this Proposal.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_groups

    @access_groups.setter
    def access_groups(self, access_groups):
        """Sets the access_groups of this Proposal.

        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users  # noqa: E501

        :param access_groups: The access_groups of this Proposal.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and access_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `access_groups`, must not be `None`")  # noqa: E501

        self._access_groups = access_groups

    @property
    def instrument_group(self):
        """Gets the instrument_group of this Proposal.  # noqa: E501

        Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data.  # noqa: E501

        :return: The instrument_group of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._instrument_group

    @instrument_group.setter
    def instrument_group(self, instrument_group):
        """Sets the instrument_group of this Proposal.

        Optional additional groups which have read and write access to the data. Users which are member in one of the groups listed here are allowed to access this data.  # noqa: E501

        :param instrument_group: The instrument_group of this Proposal.  # noqa: E501
        :type: str
        """

        self._instrument_group = instrument_group

    @property
    def created_by(self):
        """Gets the created_by of this Proposal.  # noqa: E501


        :return: The created_by of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Proposal.


        :param created_by: The created_by of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this Proposal.  # noqa: E501


        :return: The updated_by of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Proposal.


        :param updated_by: The updated_by of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_by is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_by`, must not be `None`")  # noqa: E501

        self._updated_by = updated_by

    @property
    def proposal_id(self):
        """Gets the proposal_id of this Proposal.  # noqa: E501

        Globally unique identifier of a proposal, eg. PID-prefix/internal-proposal-number. PID prefix is auto prepended  # noqa: E501

        :return: The proposal_id of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._proposal_id

    @proposal_id.setter
    def proposal_id(self, proposal_id):
        """Sets the proposal_id of this Proposal.

        Globally unique identifier of a proposal, eg. PID-prefix/internal-proposal-number. PID prefix is auto prepended  # noqa: E501

        :param proposal_id: The proposal_id of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and proposal_id is None:  # noqa: E501
            raise ValueError("Invalid value for `proposal_id`, must not be `None`")  # noqa: E501

        self._proposal_id = proposal_id

    @property
    def pi_email(self):
        """Gets the pi_email of this Proposal.  # noqa: E501

        Email of principal investigator  # noqa: E501

        :return: The pi_email of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._pi_email

    @pi_email.setter
    def pi_email(self, pi_email):
        """Sets the pi_email of this Proposal.

        Email of principal investigator  # noqa: E501

        :param pi_email: The pi_email of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pi_email is None:  # noqa: E501
            raise ValueError("Invalid value for `pi_email`, must not be `None`")  # noqa: E501

        self._pi_email = pi_email

    @property
    def pi_firstname(self):
        """Gets the pi_firstname of this Proposal.  # noqa: E501

        First name of principal investigator  # noqa: E501

        :return: The pi_firstname of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._pi_firstname

    @pi_firstname.setter
    def pi_firstname(self, pi_firstname):
        """Sets the pi_firstname of this Proposal.

        First name of principal investigator  # noqa: E501

        :param pi_firstname: The pi_firstname of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pi_firstname is None:  # noqa: E501
            raise ValueError("Invalid value for `pi_firstname`, must not be `None`")  # noqa: E501

        self._pi_firstname = pi_firstname

    @property
    def pi_lastname(self):
        """Gets the pi_lastname of this Proposal.  # noqa: E501

        Last name of principal investigator  # noqa: E501

        :return: The pi_lastname of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._pi_lastname

    @pi_lastname.setter
    def pi_lastname(self, pi_lastname):
        """Sets the pi_lastname of this Proposal.

        Last name of principal investigator  # noqa: E501

        :param pi_lastname: The pi_lastname of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pi_lastname is None:  # noqa: E501
            raise ValueError("Invalid value for `pi_lastname`, must not be `None`")  # noqa: E501

        self._pi_lastname = pi_lastname

    @property
    def email(self):
        """Gets the email of this Proposal.  # noqa: E501

        Email of main proposer  # noqa: E501

        :return: The email of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Proposal.

        Email of main proposer  # noqa: E501

        :param email: The email of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this Proposal.  # noqa: E501

        First name of main proposer  # noqa: E501

        :return: The firstname of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this Proposal.

        First name of main proposer  # noqa: E501

        :param firstname: The firstname of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and firstname is None:  # noqa: E501
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this Proposal.  # noqa: E501

        Last name of main proposer  # noqa: E501

        :return: The lastname of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this Proposal.

        Last name of main proposer  # noqa: E501

        :param lastname: The lastname of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and lastname is None:  # noqa: E501
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501

        self._lastname = lastname

    @property
    def title(self):
        """Gets the title of this Proposal.  # noqa: E501

        The title of the proposal  # noqa: E501

        :return: The title of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Proposal.

        The title of the proposal  # noqa: E501

        :param title: The title of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def abstract(self):
        """Gets the abstract of this Proposal.  # noqa: E501

        The proposal abstract  # noqa: E501

        :return: The abstract of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract):
        """Sets the abstract of this Proposal.

        The proposal abstract  # noqa: E501

        :param abstract: The abstract of this Proposal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and abstract is None:  # noqa: E501
            raise ValueError("Invalid value for `abstract`, must not be `None`")  # noqa: E501

        self._abstract = abstract

    @property
    def start_time(self):
        """Gets the start_time of this Proposal.  # noqa: E501

        The date when the data collection starts  # noqa: E501

        :return: The start_time of this Proposal.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Proposal.

        The date when the data collection starts  # noqa: E501

        :param start_time: The start_time of this Proposal.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Proposal.  # noqa: E501

        The date when data collection finishes  # noqa: E501

        :return: The end_time of this Proposal.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Proposal.

        The date when data collection finishes  # noqa: E501

        :param end_time: The end_time of this Proposal.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def attachments(self):
        """Gets the attachments of this Proposal.  # noqa: E501

        Small less than 16 MB attachments, envisaged for png/jpeg previews  # noqa: E501

        :return: The attachments of this Proposal.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Proposal.

        Small less than 16 MB attachments, envisaged for png/jpeg previews  # noqa: E501

        :param attachments: The attachments of this Proposal.  # noqa: E501
        :type: list[Attachment]
        """
        if self.local_vars_configuration.client_side_validation and attachments is None:  # noqa: E501
            raise ValueError("Invalid value for `attachments`, must not be `None`")  # noqa: E501

        self._attachments = attachments

    @property
    def datasets(self):
        """Gets the datasets of this Proposal.  # noqa: E501


        :return: The datasets of this Proposal.  # noqa: E501
        :rtype: list[Dataset]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this Proposal.


        :param datasets: The datasets of this Proposal.  # noqa: E501
        :type: list[Dataset]
        """
        if self.local_vars_configuration.client_side_validation and datasets is None:  # noqa: E501
            raise ValueError("Invalid value for `datasets`, must not be `None`")  # noqa: E501

        self._datasets = datasets

    @property
    def measurement_period_list(self):
        """Gets the measurement_period_list of this Proposal.  # noqa: E501

        Embedded information used inside proposals to define which type of experiment as to be pursued where (at which intrument) and when.  # noqa: E501

        :return: The measurement_period_list of this Proposal.  # noqa: E501
        :rtype: MeasurementPeriod
        """
        return self._measurement_period_list

    @measurement_period_list.setter
    def measurement_period_list(self, measurement_period_list):
        """Sets the measurement_period_list of this Proposal.

        Embedded information used inside proposals to define which type of experiment as to be pursued where (at which intrument) and when.  # noqa: E501

        :param measurement_period_list: The measurement_period_list of this Proposal.  # noqa: E501
        :type: MeasurementPeriod
        """
        if self.local_vars_configuration.client_side_validation and measurement_period_list is None:  # noqa: E501
            raise ValueError("Invalid value for `measurement_period_list`, must not be `None`")  # noqa: E501

        self._measurement_period_list = measurement_period_list

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
        if not isinstance(other, Proposal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Proposal):
            return True

        return self.to_dict() != other.to_dict()
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


class UpdateJobDto(object):
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
        'email_job_initiator': 'str',
        'type': 'str',
        'creation_time': 'datetime',
        'execution_time': 'datetime',
        'job_params': 'object',
        'job_status_message': 'str',
        'dataset_list': 'object',
        'job_result_object': 'object'
    }

    attribute_map = {
        'email_job_initiator': 'emailJobInitiator',
        'type': 'type',
        'creation_time': 'creationTime',
        'execution_time': 'executionTime',
        'job_params': 'jobParams',
        'job_status_message': 'jobStatusMessage',
        'dataset_list': 'datasetList',
        'job_result_object': 'jobResultObject'
    }

    def __init__(self, email_job_initiator=None, type=None, creation_time=None, execution_time=None, job_params=None, job_status_message=None, dataset_list=None, job_result_object=None, local_vars_configuration=None):  # noqa: E501
        """UpdateJobDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_job_initiator = None
        self._type = None
        self._creation_time = None
        self._execution_time = None
        self._job_params = None
        self._job_status_message = None
        self._dataset_list = None
        self._job_result_object = None
        self.discriminator = None

        if email_job_initiator is not None:
            self.email_job_initiator = email_job_initiator
        if type is not None:
            self.type = type
        if creation_time is not None:
            self.creation_time = creation_time
        if execution_time is not None:
            self.execution_time = execution_time
        if job_params is not None:
            self.job_params = job_params
        if job_status_message is not None:
            self.job_status_message = job_status_message
        if dataset_list is not None:
            self.dataset_list = dataset_list
        if job_result_object is not None:
            self.job_result_object = job_result_object

    @property
    def email_job_initiator(self):
        """Gets the email_job_initiator of this UpdateJobDto.  # noqa: E501


        :return: The email_job_initiator of this UpdateJobDto.  # noqa: E501
        :rtype: str
        """
        return self._email_job_initiator

    @email_job_initiator.setter
    def email_job_initiator(self, email_job_initiator):
        """Sets the email_job_initiator of this UpdateJobDto.


        :param email_job_initiator: The email_job_initiator of this UpdateJobDto.  # noqa: E501
        :type: str
        """

        self._email_job_initiator = email_job_initiator

    @property
    def type(self):
        """Gets the type of this UpdateJobDto.  # noqa: E501


        :return: The type of this UpdateJobDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateJobDto.


        :param type: The type of this UpdateJobDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def creation_time(self):
        """Gets the creation_time of this UpdateJobDto.  # noqa: E501


        :return: The creation_time of this UpdateJobDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this UpdateJobDto.


        :param creation_time: The creation_time of this UpdateJobDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def execution_time(self):
        """Gets the execution_time of this UpdateJobDto.  # noqa: E501


        :return: The execution_time of this UpdateJobDto.  # noqa: E501
        :rtype: datetime
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this UpdateJobDto.


        :param execution_time: The execution_time of this UpdateJobDto.  # noqa: E501
        :type: datetime
        """

        self._execution_time = execution_time

    @property
    def job_params(self):
        """Gets the job_params of this UpdateJobDto.  # noqa: E501


        :return: The job_params of this UpdateJobDto.  # noqa: E501
        :rtype: object
        """
        return self._job_params

    @job_params.setter
    def job_params(self, job_params):
        """Sets the job_params of this UpdateJobDto.


        :param job_params: The job_params of this UpdateJobDto.  # noqa: E501
        :type: object
        """

        self._job_params = job_params

    @property
    def job_status_message(self):
        """Gets the job_status_message of this UpdateJobDto.  # noqa: E501


        :return: The job_status_message of this UpdateJobDto.  # noqa: E501
        :rtype: str
        """
        return self._job_status_message

    @job_status_message.setter
    def job_status_message(self, job_status_message):
        """Sets the job_status_message of this UpdateJobDto.


        :param job_status_message: The job_status_message of this UpdateJobDto.  # noqa: E501
        :type: str
        """

        self._job_status_message = job_status_message

    @property
    def dataset_list(self):
        """Gets the dataset_list of this UpdateJobDto.  # noqa: E501


        :return: The dataset_list of this UpdateJobDto.  # noqa: E501
        :rtype: object
        """
        return self._dataset_list

    @dataset_list.setter
    def dataset_list(self, dataset_list):
        """Sets the dataset_list of this UpdateJobDto.


        :param dataset_list: The dataset_list of this UpdateJobDto.  # noqa: E501
        :type: object
        """

        self._dataset_list = dataset_list

    @property
    def job_result_object(self):
        """Gets the job_result_object of this UpdateJobDto.  # noqa: E501


        :return: The job_result_object of this UpdateJobDto.  # noqa: E501
        :rtype: object
        """
        return self._job_result_object

    @job_result_object.setter
    def job_result_object(self, job_result_object):
        """Sets the job_result_object of this UpdateJobDto.


        :param job_result_object: The job_result_object of this UpdateJobDto.  # noqa: E501
        :type: object
        """

        self._job_result_object = job_result_object

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
        if not isinstance(other, UpdateJobDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateJobDto):
            return True

        return self.to_dict() != other.to_dict()

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


class UpdatePublishedDataDto(object):
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
        'id': 'str',
        'doi': 'str',
        'affiliation': 'str',
        'creator': 'list[str]',
        'publisher': 'str',
        'publication_year': 'float',
        'title': 'str',
        'url': 'str',
        'abstract': 'str',
        'data_description': 'str',
        'resource_type': 'str',
        'number_of_files': 'float',
        'size_of_archive': 'float',
        'pid_array': 'list[str]',
        'authors': 'list[str]',
        'registered_time': 'datetime',
        'status': 'str',
        'scicat_user': 'str',
        'thumbnail': 'str',
        'related_publications': 'list[str]',
        'download_link': 'str'
    }

    attribute_map = {
        'id': '_id',
        'doi': 'doi',
        'affiliation': 'affiliation',
        'creator': 'creator',
        'publisher': 'publisher',
        'publication_year': 'publicationYear',
        'title': 'title',
        'url': 'url',
        'abstract': 'abstract',
        'data_description': 'dataDescription',
        'resource_type': 'resourceType',
        'number_of_files': 'numberOfFiles',
        'size_of_archive': 'sizeOfArchive',
        'pid_array': 'pidArray',
        'authors': 'authors',
        'registered_time': 'registeredTime',
        'status': 'status',
        'scicat_user': 'scicatUser',
        'thumbnail': 'thumbnail',
        'related_publications': 'relatedPublications',
        'download_link': 'downloadLink'
    }

    def __init__(self, id=None, doi=None, affiliation=None, creator=None, publisher=None, publication_year=None, title=None, url=None, abstract=None, data_description=None, resource_type=None, number_of_files=None, size_of_archive=None, pid_array=None, authors=None, registered_time=None, status=None, scicat_user=None, thumbnail=None, related_publications=None, download_link=None, local_vars_configuration=None):  # noqa: E501
        """UpdatePublishedDataDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._doi = None
        self._affiliation = None
        self._creator = None
        self._publisher = None
        self._publication_year = None
        self._title = None
        self._url = None
        self._abstract = None
        self._data_description = None
        self._resource_type = None
        self._number_of_files = None
        self._size_of_archive = None
        self._pid_array = None
        self._authors = None
        self._registered_time = None
        self._status = None
        self._scicat_user = None
        self._thumbnail = None
        self._related_publications = None
        self._download_link = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if doi is not None:
            self.doi = doi
        if affiliation is not None:
            self.affiliation = affiliation
        if creator is not None:
            self.creator = creator
        if publisher is not None:
            self.publisher = publisher
        if publication_year is not None:
            self.publication_year = publication_year
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if abstract is not None:
            self.abstract = abstract
        if data_description is not None:
            self.data_description = data_description
        if resource_type is not None:
            self.resource_type = resource_type
        if number_of_files is not None:
            self.number_of_files = number_of_files
        if size_of_archive is not None:
            self.size_of_archive = size_of_archive
        if pid_array is not None:
            self.pid_array = pid_array
        if authors is not None:
            self.authors = authors
        if registered_time is not None:
            self.registered_time = registered_time
        if status is not None:
            self.status = status
        if scicat_user is not None:
            self.scicat_user = scicat_user
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if related_publications is not None:
            self.related_publications = related_publications
        if download_link is not None:
            self.download_link = download_link

    @property
    def id(self):
        """Gets the id of this UpdatePublishedDataDto.  # noqa: E501


        :return: The id of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatePublishedDataDto.


        :param id: The id of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def doi(self):
        """Gets the doi of this UpdatePublishedDataDto.  # noqa: E501


        :return: The doi of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """Sets the doi of this UpdatePublishedDataDto.


        :param doi: The doi of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._doi = doi

    @property
    def affiliation(self):
        """Gets the affiliation of this UpdatePublishedDataDto.  # noqa: E501


        :return: The affiliation of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._affiliation

    @affiliation.setter
    def affiliation(self, affiliation):
        """Sets the affiliation of this UpdatePublishedDataDto.


        :param affiliation: The affiliation of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._affiliation = affiliation

    @property
    def creator(self):
        """Gets the creator of this UpdatePublishedDataDto.  # noqa: E501


        :return: The creator of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this UpdatePublishedDataDto.


        :param creator: The creator of this UpdatePublishedDataDto.  # noqa: E501
        :type: list[str]
        """

        self._creator = creator

    @property
    def publisher(self):
        """Gets the publisher of this UpdatePublishedDataDto.  # noqa: E501


        :return: The publisher of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this UpdatePublishedDataDto.


        :param publisher: The publisher of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def publication_year(self):
        """Gets the publication_year of this UpdatePublishedDataDto.  # noqa: E501


        :return: The publication_year of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: float
        """
        return self._publication_year

    @publication_year.setter
    def publication_year(self, publication_year):
        """Sets the publication_year of this UpdatePublishedDataDto.


        :param publication_year: The publication_year of this UpdatePublishedDataDto.  # noqa: E501
        :type: float
        """

        self._publication_year = publication_year

    @property
    def title(self):
        """Gets the title of this UpdatePublishedDataDto.  # noqa: E501


        :return: The title of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdatePublishedDataDto.


        :param title: The title of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this UpdatePublishedDataDto.  # noqa: E501


        :return: The url of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdatePublishedDataDto.


        :param url: The url of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def abstract(self):
        """Gets the abstract of this UpdatePublishedDataDto.  # noqa: E501


        :return: The abstract of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract):
        """Sets the abstract of this UpdatePublishedDataDto.


        :param abstract: The abstract of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._abstract = abstract

    @property
    def data_description(self):
        """Gets the data_description of this UpdatePublishedDataDto.  # noqa: E501


        :return: The data_description of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._data_description

    @data_description.setter
    def data_description(self, data_description):
        """Sets the data_description of this UpdatePublishedDataDto.


        :param data_description: The data_description of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._data_description = data_description

    @property
    def resource_type(self):
        """Gets the resource_type of this UpdatePublishedDataDto.  # noqa: E501


        :return: The resource_type of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this UpdatePublishedDataDto.


        :param resource_type: The resource_type of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def number_of_files(self):
        """Gets the number_of_files of this UpdatePublishedDataDto.  # noqa: E501


        :return: The number_of_files of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: float
        """
        return self._number_of_files

    @number_of_files.setter
    def number_of_files(self, number_of_files):
        """Sets the number_of_files of this UpdatePublishedDataDto.


        :param number_of_files: The number_of_files of this UpdatePublishedDataDto.  # noqa: E501
        :type: float
        """

        self._number_of_files = number_of_files

    @property
    def size_of_archive(self):
        """Gets the size_of_archive of this UpdatePublishedDataDto.  # noqa: E501


        :return: The size_of_archive of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: float
        """
        return self._size_of_archive

    @size_of_archive.setter
    def size_of_archive(self, size_of_archive):
        """Sets the size_of_archive of this UpdatePublishedDataDto.


        :param size_of_archive: The size_of_archive of this UpdatePublishedDataDto.  # noqa: E501
        :type: float
        """

        self._size_of_archive = size_of_archive

    @property
    def pid_array(self):
        """Gets the pid_array of this UpdatePublishedDataDto.  # noqa: E501


        :return: The pid_array of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._pid_array

    @pid_array.setter
    def pid_array(self, pid_array):
        """Sets the pid_array of this UpdatePublishedDataDto.


        :param pid_array: The pid_array of this UpdatePublishedDataDto.  # noqa: E501
        :type: list[str]
        """

        self._pid_array = pid_array

    @property
    def authors(self):
        """Gets the authors of this UpdatePublishedDataDto.  # noqa: E501


        :return: The authors of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this UpdatePublishedDataDto.


        :param authors: The authors of this UpdatePublishedDataDto.  # noqa: E501
        :type: list[str]
        """

        self._authors = authors

    @property
    def registered_time(self):
        """Gets the registered_time of this UpdatePublishedDataDto.  # noqa: E501


        :return: The registered_time of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: datetime
        """
        return self._registered_time

    @registered_time.setter
    def registered_time(self, registered_time):
        """Sets the registered_time of this UpdatePublishedDataDto.


        :param registered_time: The registered_time of this UpdatePublishedDataDto.  # noqa: E501
        :type: datetime
        """

        self._registered_time = registered_time

    @property
    def status(self):
        """Gets the status of this UpdatePublishedDataDto.  # noqa: E501


        :return: The status of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdatePublishedDataDto.


        :param status: The status of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def scicat_user(self):
        """Gets the scicat_user of this UpdatePublishedDataDto.  # noqa: E501


        :return: The scicat_user of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._scicat_user

    @scicat_user.setter
    def scicat_user(self, scicat_user):
        """Sets the scicat_user of this UpdatePublishedDataDto.


        :param scicat_user: The scicat_user of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._scicat_user = scicat_user

    @property
    def thumbnail(self):
        """Gets the thumbnail of this UpdatePublishedDataDto.  # noqa: E501


        :return: The thumbnail of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this UpdatePublishedDataDto.


        :param thumbnail: The thumbnail of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def related_publications(self):
        """Gets the related_publications of this UpdatePublishedDataDto.  # noqa: E501


        :return: The related_publications of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_publications

    @related_publications.setter
    def related_publications(self, related_publications):
        """Sets the related_publications of this UpdatePublishedDataDto.


        :param related_publications: The related_publications of this UpdatePublishedDataDto.  # noqa: E501
        :type: list[str]
        """

        self._related_publications = related_publications

    @property
    def download_link(self):
        """Gets the download_link of this UpdatePublishedDataDto.  # noqa: E501


        :return: The download_link of this UpdatePublishedDataDto.  # noqa: E501
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        """Sets the download_link of this UpdatePublishedDataDto.


        :param download_link: The download_link of this UpdatePublishedDataDto.  # noqa: E501
        :type: str
        """

        self._download_link = download_link

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
        if not isinstance(other, UpdatePublishedDataDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatePublishedDataDto):
            return True

        return self.to_dict() != other.to_dict()

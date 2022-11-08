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


class PublishedData(object):
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
        'download_link': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
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
        'download_link': 'downloadLink',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, doi=None, affiliation=None, creator=None, publisher=None, publication_year=None, title=None, url=None, abstract=None, data_description=None, resource_type=None, number_of_files=None, size_of_archive=None, pid_array=None, authors=None, registered_time=None, status=None, scicat_user=None, thumbnail=None, related_publications=None, download_link=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """PublishedData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

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
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.doi = doi
        if affiliation is not None:
            self.affiliation = affiliation
        self.creator = creator
        self.publisher = publisher
        self.publication_year = publication_year
        self.title = title
        if url is not None:
            self.url = url
        self.abstract = abstract
        self.data_description = data_description
        self.resource_type = resource_type
        if number_of_files is not None:
            self.number_of_files = number_of_files
        if size_of_archive is not None:
            self.size_of_archive = size_of_archive
        self.pid_array = pid_array
        if authors is not None:
            self.authors = authors
        self.registered_time = registered_time
        self.status = status
        if scicat_user is not None:
            self.scicat_user = scicat_user
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if related_publications is not None:
            self.related_publications = related_publications
        if download_link is not None:
            self.download_link = download_link
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def doi(self):
        """Gets the doi of this PublishedData.  # noqa: E501

        Digital Object Identifier  # noqa: E501

        :return: The doi of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """Sets the doi of this PublishedData.

        Digital Object Identifier  # noqa: E501

        :param doi: The doi of this PublishedData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and doi is None:  # noqa: E501
            raise ValueError("Invalid value for `doi`, must not be `None`")  # noqa: E501

        self._doi = doi

    @property
    def affiliation(self):
        """Gets the affiliation of this PublishedData.  # noqa: E501

        Creator Affiliation  # noqa: E501

        :return: The affiliation of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._affiliation

    @affiliation.setter
    def affiliation(self, affiliation):
        """Sets the affiliation of this PublishedData.

        Creator Affiliation  # noqa: E501

        :param affiliation: The affiliation of this PublishedData.  # noqa: E501
        :type: str
        """

        self._affiliation = affiliation

    @property
    def creator(self):
        """Gets the creator of this PublishedData.  # noqa: E501

        Creator of dataset/dataset collection  # noqa: E501

        :return: The creator of this PublishedData.  # noqa: E501
        :rtype: list[str]
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PublishedData.

        Creator of dataset/dataset collection  # noqa: E501

        :param creator: The creator of this PublishedData.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and creator is None:  # noqa: E501
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def publisher(self):
        """Gets the publisher of this PublishedData.  # noqa: E501

        Dataset publisher  # noqa: E501

        :return: The publisher of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this PublishedData.

        Dataset publisher  # noqa: E501

        :param publisher: The publisher of this PublishedData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and publisher is None:  # noqa: E501
            raise ValueError("Invalid value for `publisher`, must not be `None`")  # noqa: E501

        self._publisher = publisher

    @property
    def publication_year(self):
        """Gets the publication_year of this PublishedData.  # noqa: E501

        Year of publication   # noqa: E501

        :return: The publication_year of this PublishedData.  # noqa: E501
        :rtype: float
        """
        return self._publication_year

    @publication_year.setter
    def publication_year(self, publication_year):
        """Sets the publication_year of this PublishedData.

        Year of publication   # noqa: E501

        :param publication_year: The publication_year of this PublishedData.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and publication_year is None:  # noqa: E501
            raise ValueError("Invalid value for `publication_year`, must not be `None`")  # noqa: E501

        self._publication_year = publication_year

    @property
    def title(self):
        """Gets the title of this PublishedData.  # noqa: E501

        Title  # noqa: E501

        :return: The title of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PublishedData.

        Title  # noqa: E501

        :param title: The title of this PublishedData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def url(self):
        """Gets the url of this PublishedData.  # noqa: E501

        Full URL to the landing page for this DOI  # noqa: E501

        :return: The url of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PublishedData.

        Full URL to the landing page for this DOI  # noqa: E501

        :param url: The url of this PublishedData.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def abstract(self):
        """Gets the abstract of this PublishedData.  # noqa: E501

        Abstract text for published datasets  # noqa: E501

        :return: The abstract of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract):
        """Sets the abstract of this PublishedData.

        Abstract text for published datasets  # noqa: E501

        :param abstract: The abstract of this PublishedData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and abstract is None:  # noqa: E501
            raise ValueError("Invalid value for `abstract`, must not be `None`")  # noqa: E501

        self._abstract = abstract

    @property
    def data_description(self):
        """Gets the data_description of this PublishedData.  # noqa: E501

        Link to description of how to re-use data  # noqa: E501

        :return: The data_description of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._data_description

    @data_description.setter
    def data_description(self, data_description):
        """Sets the data_description of this PublishedData.

        Link to description of how to re-use data  # noqa: E501

        :param data_description: The data_description of this PublishedData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data_description is None:  # noqa: E501
            raise ValueError("Invalid value for `data_description`, must not be `None`")  # noqa: E501

        self._data_description = data_description

    @property
    def resource_type(self):
        """Gets the resource_type of this PublishedData.  # noqa: E501

        e.g. raw/ derived  # noqa: E501

        :return: The resource_type of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PublishedData.

        e.g. raw/ derived  # noqa: E501

        :param resource_type: The resource_type of this PublishedData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def number_of_files(self):
        """Gets the number_of_files of this PublishedData.  # noqa: E501

        Number of files  # noqa: E501

        :return: The number_of_files of this PublishedData.  # noqa: E501
        :rtype: float
        """
        return self._number_of_files

    @number_of_files.setter
    def number_of_files(self, number_of_files):
        """Sets the number_of_files of this PublishedData.

        Number of files  # noqa: E501

        :param number_of_files: The number_of_files of this PublishedData.  # noqa: E501
        :type: float
        """

        self._number_of_files = number_of_files

    @property
    def size_of_archive(self):
        """Gets the size_of_archive of this PublishedData.  # noqa: E501

        Size of archive  # noqa: E501

        :return: The size_of_archive of this PublishedData.  # noqa: E501
        :rtype: float
        """
        return self._size_of_archive

    @size_of_archive.setter
    def size_of_archive(self, size_of_archive):
        """Sets the size_of_archive of this PublishedData.

        Size of archive  # noqa: E501

        :param size_of_archive: The size_of_archive of this PublishedData.  # noqa: E501
        :type: float
        """

        self._size_of_archive = size_of_archive

    @property
    def pid_array(self):
        """Gets the pid_array of this PublishedData.  # noqa: E501

        Array of one or more PIDS which make up the published data  # noqa: E501

        :return: The pid_array of this PublishedData.  # noqa: E501
        :rtype: list[str]
        """
        return self._pid_array

    @pid_array.setter
    def pid_array(self, pid_array):
        """Sets the pid_array of this PublishedData.

        Array of one or more PIDS which make up the published data  # noqa: E501

        :param pid_array: The pid_array of this PublishedData.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and pid_array is None:  # noqa: E501
            raise ValueError("Invalid value for `pid_array`, must not be `None`")  # noqa: E501

        self._pid_array = pid_array

    @property
    def authors(self):
        """Gets the authors of this PublishedData.  # noqa: E501

        List of Names of authors of the to be published data  # noqa: E501

        :return: The authors of this PublishedData.  # noqa: E501
        :rtype: list[str]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this PublishedData.

        List of Names of authors of the to be published data  # noqa: E501

        :param authors: The authors of this PublishedData.  # noqa: E501
        :type: list[str]
        """

        self._authors = authors

    @property
    def registered_time(self):
        """Gets the registered_time of this PublishedData.  # noqa: E501

        Time when doi is successfully registered  # noqa: E501

        :return: The registered_time of this PublishedData.  # noqa: E501
        :rtype: datetime
        """
        return self._registered_time

    @registered_time.setter
    def registered_time(self, registered_time):
        """Sets the registered_time of this PublishedData.

        Time when doi is successfully registered  # noqa: E501

        :param registered_time: The registered_time of this PublishedData.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and registered_time is None:  # noqa: E501
            raise ValueError("Invalid value for `registered_time`, must not be `None`")  # noqa: E501

        self._registered_time = registered_time

    @property
    def status(self):
        """Gets the status of this PublishedData.  # noqa: E501

        Indication of position in publication workflow e.g. doiRegistered  # noqa: E501

        :return: The status of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublishedData.

        Indication of position in publication workflow e.g. doiRegistered  # noqa: E501

        :param status: The status of this PublishedData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def scicat_user(self):
        """Gets the scicat_user of this PublishedData.  # noqa: E501

        The username of the user that clicks the publish button in the client  # noqa: E501

        :return: The scicat_user of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._scicat_user

    @scicat_user.setter
    def scicat_user(self, scicat_user):
        """Sets the scicat_user of this PublishedData.

        The username of the user that clicks the publish button in the client  # noqa: E501

        :param scicat_user: The scicat_user of this PublishedData.  # noqa: E501
        :type: str
        """

        self._scicat_user = scicat_user

    @property
    def thumbnail(self):
        """Gets the thumbnail of this PublishedData.  # noqa: E501

        Small, less than 16 MB base 64 image preview of dataset  # noqa: E501

        :return: The thumbnail of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this PublishedData.

        Small, less than 16 MB base 64 image preview of dataset  # noqa: E501

        :param thumbnail: The thumbnail of this PublishedData.  # noqa: E501
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def related_publications(self):
        """Gets the related_publications of this PublishedData.  # noqa: E501

        List of URLs pointing to related publications like DOI URLS of journal articles  # noqa: E501

        :return: The related_publications of this PublishedData.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_publications

    @related_publications.setter
    def related_publications(self, related_publications):
        """Sets the related_publications of this PublishedData.

        List of URLs pointing to related publications like DOI URLS of journal articles  # noqa: E501

        :param related_publications: The related_publications of this PublishedData.  # noqa: E501
        :type: list[str]
        """

        self._related_publications = related_publications

    @property
    def download_link(self):
        """Gets the download_link of this PublishedData.  # noqa: E501

        URL pointing to page from which data can be downloaded  # noqa: E501

        :return: The download_link of this PublishedData.  # noqa: E501
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        """Sets the download_link of this PublishedData.

        URL pointing to page from which data can be downloaded  # noqa: E501

        :param download_link: The download_link of this PublishedData.  # noqa: E501
        :type: str
        """

        self._download_link = download_link

    @property
    def created_at(self):
        """Gets the created_at of this PublishedData.  # noqa: E501

        Date when the published data was created  # noqa: E501

        :return: The created_at of this PublishedData.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PublishedData.

        Date when the published data was created  # noqa: E501

        :param created_at: The created_at of this PublishedData.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PublishedData.  # noqa: E501

        Date when the published data was last updated  # noqa: E501

        :return: The updated_at of this PublishedData.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PublishedData.

        Date when the published data was last updated  # noqa: E501

        :param updated_at: The updated_at of this PublishedData.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, PublishedData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublishedData):
            return True

        return self.to_dict() != other.to_dict()

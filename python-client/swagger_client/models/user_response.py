# coding: utf-8

"""
    MarketPay API

    API for Smart Contracts and Payments  # noqa: E501

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'person_type': 'str',
        'kyc_level': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'id': 'str',
        'creation_date': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'person_type': 'PersonType',
        'kyc_level': 'KYCLevel',
        'email': 'Email',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'id': 'Id',
        'creation_date': 'CreationDate',
        'tag': 'Tag'
    }

    def __init__(self, person_type=None, kyc_level=None, email=None, first_name=None, last_name=None, id=None, creation_date=None, tag=None):  # noqa: E501
        """UserResponse - a model defined in Swagger"""  # noqa: E501

        self._person_type = None
        self._kyc_level = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._id = None
        self._creation_date = None
        self._tag = None
        self.discriminator = None

        if person_type is not None:
            self.person_type = person_type
        if kyc_level is not None:
            self.kyc_level = kyc_level
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if id is not None:
            self.id = id
        if creation_date is not None:
            self.creation_date = creation_date
        if tag is not None:
            self.tag = tag

    @property
    def person_type(self):
        """Gets the person_type of this UserResponse.  # noqa: E501

        Type of user  # noqa: E501

        :return: The person_type of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._person_type

    @person_type.setter
    def person_type(self, person_type):
        """Sets the person_type of this UserResponse.

        Type of user  # noqa: E501

        :param person_type: The person_type of this UserResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Natural", "Legal", "Fees"]  # noqa: E501
        if person_type not in allowed_values:
            raise ValueError(
                "Invalid value for `person_type` ({0}), must be one of {1}"  # noqa: E501
                .format(person_type, allowed_values)
            )

        self._person_type = person_type

    @property
    def kyc_level(self):
        """Gets the kyc_level of this UserResponse.  # noqa: E501

          # noqa: E501

        :return: The kyc_level of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._kyc_level

    @kyc_level.setter
    def kyc_level(self, kyc_level):
        """Sets the kyc_level of this UserResponse.

          # noqa: E501

        :param kyc_level: The kyc_level of this UserResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "LIGHT", "REGULAR"]  # noqa: E501
        if kyc_level not in allowed_values:
            raise ValueError(
                "Invalid value for `kyc_level` ({0}), must be one of {1}"  # noqa: E501
                .format(kyc_level, allowed_values)
            )

        self._kyc_level = kyc_level

    @property
    def email(self):
        """Gets the email of this UserResponse.  # noqa: E501

        The user's email address - must be a valid email  # noqa: E501

        :return: The email of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserResponse.

        The user's email address - must be a valid email  # noqa: E501

        :param email: The email of this UserResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this UserResponse.  # noqa: E501

        The name of the user  # noqa: E501

        :return: The first_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserResponse.

        The name of the user  # noqa: E501

        :param first_name: The first_name of this UserResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserResponse.  # noqa: E501

        The last name of the user  # noqa: E501

        :return: The last_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserResponse.

        The last name of the user  # noqa: E501

        :param last_name: The last_name of this UserResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def id(self):
        """Gets the id of this UserResponse.  # noqa: E501

        The item's ID  # noqa: E501

        :return: The id of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserResponse.

        The item's ID  # noqa: E501

        :param id: The id of this UserResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def creation_date(self):
        """Gets the creation_date of this UserResponse.  # noqa: E501

        When the item was created  # noqa: E501

        :return: The creation_date of this UserResponse.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this UserResponse.

        When the item was created  # noqa: E501

        :param creation_date: The creation_date of this UserResponse.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def tag(self):
        """Gets the tag of this UserResponse.  # noqa: E501

        Custom data that you can add to this item  # noqa: E501

        :return: The tag of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this UserResponse.

        Custom data that you can add to this item  # noqa: E501

        :param tag: The tag of this UserResponse.  # noqa: E501
        :type: str
        """

        self._tag = tag

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UserResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
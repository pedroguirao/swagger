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

from swagger_client.models.address import Address  # noqa: F401,E501


class BankAccountIbanPost(object):
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
        'iban': 'str',
        'bic': 'str',
        'tag': 'str',
        'owner_address': 'Address',
        'owner_name': 'str'
    }

    attribute_map = {
        'iban': 'IBAN',
        'bic': 'BIC',
        'tag': 'Tag',
        'owner_address': 'OwnerAddress',
        'owner_name': 'OwnerName'
    }

    def __init__(self, iban=None, bic=None, tag=None, owner_address=None, owner_name=None):  # noqa: E501
        """BankAccountIbanPost - a model defined in Swagger"""  # noqa: E501

        self._iban = None
        self._bic = None
        self._tag = None
        self._owner_address = None
        self._owner_name = None
        self.discriminator = None

        if iban is not None:
            self.iban = iban
        if bic is not None:
            self.bic = bic
        if tag is not None:
            self.tag = tag
        if owner_address is not None:
            self.owner_address = owner_address
        if owner_name is not None:
            self.owner_name = owner_name

    @property
    def iban(self):
        """Gets the iban of this BankAccountIbanPost.  # noqa: E501


        :return: The iban of this BankAccountIbanPost.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this BankAccountIbanPost.


        :param iban: The iban of this BankAccountIbanPost.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def bic(self):
        """Gets the bic of this BankAccountIbanPost.  # noqa: E501


        :return: The bic of this BankAccountIbanPost.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this BankAccountIbanPost.


        :param bic: The bic of this BankAccountIbanPost.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def tag(self):
        """Gets the tag of this BankAccountIbanPost.  # noqa: E501


        :return: The tag of this BankAccountIbanPost.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this BankAccountIbanPost.


        :param tag: The tag of this BankAccountIbanPost.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def owner_address(self):
        """Gets the owner_address of this BankAccountIbanPost.  # noqa: E501


        :return: The owner_address of this BankAccountIbanPost.  # noqa: E501
        :rtype: Address
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this BankAccountIbanPost.


        :param owner_address: The owner_address of this BankAccountIbanPost.  # noqa: E501
        :type: Address
        """

        self._owner_address = owner_address

    @property
    def owner_name(self):
        """Gets the owner_name of this BankAccountIbanPost.  # noqa: E501


        :return: The owner_name of this BankAccountIbanPost.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this BankAccountIbanPost.


        :param owner_name: The owner_name of this BankAccountIbanPost.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

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
        if issubclass(BankAccountIbanPost, dict):
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
        if not isinstance(other, BankAccountIbanPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

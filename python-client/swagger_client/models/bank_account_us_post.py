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


class BankAccountUsPost(object):
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
        'account_number': 'str',
        'aba': 'str',
        'deposit_account_type': 'str',
        'tag': 'str',
        'owner_address': 'Address',
        'owner_name': 'str'
    }

    attribute_map = {
        'account_number': 'AccountNumber',
        'aba': 'ABA',
        'deposit_account_type': 'DepositAccountType',
        'tag': 'Tag',
        'owner_address': 'OwnerAddress',
        'owner_name': 'OwnerName'
    }

    def __init__(self, account_number=None, aba=None, deposit_account_type=None, tag=None, owner_address=None, owner_name=None):  # noqa: E501
        """BankAccountUsPost - a model defined in Swagger"""  # noqa: E501

        self._account_number = None
        self._aba = None
        self._deposit_account_type = None
        self._tag = None
        self._owner_address = None
        self._owner_name = None
        self.discriminator = None

        if account_number is not None:
            self.account_number = account_number
        if aba is not None:
            self.aba = aba
        if deposit_account_type is not None:
            self.deposit_account_type = deposit_account_type
        if tag is not None:
            self.tag = tag
        if owner_address is not None:
            self.owner_address = owner_address
        if owner_name is not None:
            self.owner_name = owner_name

    @property
    def account_number(self):
        """Gets the account_number of this BankAccountUsPost.  # noqa: E501


        :return: The account_number of this BankAccountUsPost.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this BankAccountUsPost.


        :param account_number: The account_number of this BankAccountUsPost.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def aba(self):
        """Gets the aba of this BankAccountUsPost.  # noqa: E501


        :return: The aba of this BankAccountUsPost.  # noqa: E501
        :rtype: str
        """
        return self._aba

    @aba.setter
    def aba(self, aba):
        """Sets the aba of this BankAccountUsPost.


        :param aba: The aba of this BankAccountUsPost.  # noqa: E501
        :type: str
        """

        self._aba = aba

    @property
    def deposit_account_type(self):
        """Gets the deposit_account_type of this BankAccountUsPost.  # noqa: E501


        :return: The deposit_account_type of this BankAccountUsPost.  # noqa: E501
        :rtype: str
        """
        return self._deposit_account_type

    @deposit_account_type.setter
    def deposit_account_type(self, deposit_account_type):
        """Sets the deposit_account_type of this BankAccountUsPost.


        :param deposit_account_type: The deposit_account_type of this BankAccountUsPost.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "CHECKING", "SAVINGS"]  # noqa: E501
        if deposit_account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deposit_account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deposit_account_type, allowed_values)
            )

        self._deposit_account_type = deposit_account_type

    @property
    def tag(self):
        """Gets the tag of this BankAccountUsPost.  # noqa: E501


        :return: The tag of this BankAccountUsPost.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this BankAccountUsPost.


        :param tag: The tag of this BankAccountUsPost.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def owner_address(self):
        """Gets the owner_address of this BankAccountUsPost.  # noqa: E501


        :return: The owner_address of this BankAccountUsPost.  # noqa: E501
        :rtype: Address
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this BankAccountUsPost.


        :param owner_address: The owner_address of this BankAccountUsPost.  # noqa: E501
        :type: Address
        """

        self._owner_address = owner_address

    @property
    def owner_name(self):
        """Gets the owner_name of this BankAccountUsPost.  # noqa: E501


        :return: The owner_name of this BankAccountUsPost.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this BankAccountUsPost.


        :param owner_name: The owner_name of this BankAccountUsPost.  # noqa: E501
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
        if issubclass(BankAccountUsPost, dict):
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
        if not isinstance(other, BankAccountUsPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
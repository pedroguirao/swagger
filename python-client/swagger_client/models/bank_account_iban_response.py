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


class BankAccountIbanResponse(object):
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
        'type': 'str',
        'owner_address': 'Address',
        'owner_name': 'str',
        'user_id': 'str',
        'active': 'bool',
        'bank_account_number': 'str',
        'id': 'str',
        'creation_date': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'iban': 'IBAN',
        'bic': 'BIC',
        'type': 'Type',
        'owner_address': 'OwnerAddress',
        'owner_name': 'OwnerName',
        'user_id': 'UserId',
        'active': 'Active',
        'bank_account_number': 'BankAccountNumber',
        'id': 'Id',
        'creation_date': 'CreationDate',
        'tag': 'Tag'
    }

    def __init__(self, iban=None, bic=None, type=None, owner_address=None, owner_name=None, user_id=None, active=None, bank_account_number=None, id=None, creation_date=None, tag=None):  # noqa: E501
        """BankAccountIbanResponse - a model defined in Swagger"""  # noqa: E501

        self._iban = None
        self._bic = None
        self._type = None
        self._owner_address = None
        self._owner_name = None
        self._user_id = None
        self._active = None
        self._bank_account_number = None
        self._id = None
        self._creation_date = None
        self._tag = None
        self.discriminator = None

        if iban is not None:
            self.iban = iban
        if bic is not None:
            self.bic = bic
        if type is not None:
            self.type = type
        if owner_address is not None:
            self.owner_address = owner_address
        if owner_name is not None:
            self.owner_name = owner_name
        if user_id is not None:
            self.user_id = user_id
        if active is not None:
            self.active = active
        if bank_account_number is not None:
            self.bank_account_number = bank_account_number
        if id is not None:
            self.id = id
        if creation_date is not None:
            self.creation_date = creation_date
        if tag is not None:
            self.tag = tag

    @property
    def iban(self):
        """Gets the iban of this BankAccountIbanResponse.  # noqa: E501


        :return: The iban of this BankAccountIbanResponse.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this BankAccountIbanResponse.


        :param iban: The iban of this BankAccountIbanResponse.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def bic(self):
        """Gets the bic of this BankAccountIbanResponse.  # noqa: E501


        :return: The bic of this BankAccountIbanResponse.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this BankAccountIbanResponse.


        :param bic: The bic of this BankAccountIbanResponse.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def type(self):
        """Gets the type of this BankAccountIbanResponse.  # noqa: E501


        :return: The type of this BankAccountIbanResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BankAccountIbanResponse.


        :param type: The type of this BankAccountIbanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["IBAN", "GB", "US", "CA", "OTHER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def owner_address(self):
        """Gets the owner_address of this BankAccountIbanResponse.  # noqa: E501


        :return: The owner_address of this BankAccountIbanResponse.  # noqa: E501
        :rtype: Address
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this BankAccountIbanResponse.


        :param owner_address: The owner_address of this BankAccountIbanResponse.  # noqa: E501
        :type: Address
        """

        self._owner_address = owner_address

    @property
    def owner_name(self):
        """Gets the owner_name of this BankAccountIbanResponse.  # noqa: E501


        :return: The owner_name of this BankAccountIbanResponse.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this BankAccountIbanResponse.


        :param owner_name: The owner_name of this BankAccountIbanResponse.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def user_id(self):
        """Gets the user_id of this BankAccountIbanResponse.  # noqa: E501


        :return: The user_id of this BankAccountIbanResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BankAccountIbanResponse.


        :param user_id: The user_id of this BankAccountIbanResponse.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def active(self):
        """Gets the active of this BankAccountIbanResponse.  # noqa: E501


        :return: The active of this BankAccountIbanResponse.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BankAccountIbanResponse.


        :param active: The active of this BankAccountIbanResponse.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def bank_account_number(self):
        """Gets the bank_account_number of this BankAccountIbanResponse.  # noqa: E501


        :return: The bank_account_number of this BankAccountIbanResponse.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """Sets the bank_account_number of this BankAccountIbanResponse.


        :param bank_account_number: The bank_account_number of this BankAccountIbanResponse.  # noqa: E501
        :type: str
        """

        self._bank_account_number = bank_account_number

    @property
    def id(self):
        """Gets the id of this BankAccountIbanResponse.  # noqa: E501

        The item's ID  # noqa: E501

        :return: The id of this BankAccountIbanResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BankAccountIbanResponse.

        The item's ID  # noqa: E501

        :param id: The id of this BankAccountIbanResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def creation_date(self):
        """Gets the creation_date of this BankAccountIbanResponse.  # noqa: E501

        When the item was created  # noqa: E501

        :return: The creation_date of this BankAccountIbanResponse.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this BankAccountIbanResponse.

        When the item was created  # noqa: E501

        :param creation_date: The creation_date of this BankAccountIbanResponse.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def tag(self):
        """Gets the tag of this BankAccountIbanResponse.  # noqa: E501

        Custom data that you can add to this item  # noqa: E501

        :return: The tag of this BankAccountIbanResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this BankAccountIbanResponse.

        Custom data that you can add to this item  # noqa: E501

        :param tag: The tag of this BankAccountIbanResponse.  # noqa: E501
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
        if issubclass(BankAccountIbanResponse, dict):
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
        if not isinstance(other, BankAccountIbanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

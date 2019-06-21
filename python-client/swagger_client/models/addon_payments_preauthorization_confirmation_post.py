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

from swagger_client.models.money import Money  # noqa: F401,E501


class AddonPaymentsPreauthorizationConfirmationPost(object):
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
        'tag': 'str',
        'credited_wallet_id': 'str',
        'debited_funds': 'Money',
        'fees': 'Money'
    }

    attribute_map = {
        'tag': 'Tag',
        'credited_wallet_id': 'CreditedWalletId',
        'debited_funds': 'DebitedFunds',
        'fees': 'Fees'
    }

    def __init__(self, tag=None, credited_wallet_id=None, debited_funds=None, fees=None):  # noqa: E501
        """AddonPaymentsPreauthorizationConfirmationPost - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._credited_wallet_id = None
        self._debited_funds = None
        self._fees = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if credited_wallet_id is not None:
            self.credited_wallet_id = credited_wallet_id
        if debited_funds is not None:
            self.debited_funds = debited_funds
        if fees is not None:
            self.fees = fees

    @property
    def tag(self):
        """Gets the tag of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501


        :return: The tag of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AddonPaymentsPreauthorizationConfirmationPost.


        :param tag: The tag of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def credited_wallet_id(self):
        """Gets the credited_wallet_id of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501


        :return: The credited_wallet_id of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501
        :rtype: str
        """
        return self._credited_wallet_id

    @credited_wallet_id.setter
    def credited_wallet_id(self, credited_wallet_id):
        """Sets the credited_wallet_id of this AddonPaymentsPreauthorizationConfirmationPost.


        :param credited_wallet_id: The credited_wallet_id of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501
        :type: str
        """

        self._credited_wallet_id = credited_wallet_id

    @property
    def debited_funds(self):
        """Gets the debited_funds of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501


        :return: The debited_funds of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501
        :rtype: Money
        """
        return self._debited_funds

    @debited_funds.setter
    def debited_funds(self, debited_funds):
        """Sets the debited_funds of this AddonPaymentsPreauthorizationConfirmationPost.


        :param debited_funds: The debited_funds of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501
        :type: Money
        """

        self._debited_funds = debited_funds

    @property
    def fees(self):
        """Gets the fees of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501


        :return: The fees of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501
        :rtype: Money
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this AddonPaymentsPreauthorizationConfirmationPost.


        :param fees: The fees of this AddonPaymentsPreauthorizationConfirmationPost.  # noqa: E501
        :type: Money
        """

        self._fees = fees

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
        if issubclass(AddonPaymentsPreauthorizationConfirmationPost, dict):
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
        if not isinstance(other, AddonPaymentsPreauthorizationConfirmationPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
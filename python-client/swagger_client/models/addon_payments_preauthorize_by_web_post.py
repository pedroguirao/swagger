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


class AddonPaymentsPreauthorizeByWebPost(object):
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
        'save_card': 'bool',
        'card_id': 'str',
        'author_id': 'str',
        'statement_descriptor': 'str',
        'success_url': 'str',
        'cancel_url': 'str',
        'debited_funds': 'Money',
        'language': 'str'
    }

    attribute_map = {
        'tag': 'Tag',
        'save_card': 'SaveCard',
        'card_id': 'CardId',
        'author_id': 'AuthorId',
        'statement_descriptor': 'StatementDescriptor',
        'success_url': 'SuccessUrl',
        'cancel_url': 'CancelUrl',
        'debited_funds': 'DebitedFunds',
        'language': 'Language'
    }

    def __init__(self, tag=None, save_card=None, card_id=None, author_id=None, statement_descriptor=None, success_url=None, cancel_url=None, debited_funds=None, language=None):  # noqa: E501
        """AddonPaymentsPreauthorizeByWebPost - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._save_card = None
        self._card_id = None
        self._author_id = None
        self._statement_descriptor = None
        self._success_url = None
        self._cancel_url = None
        self._debited_funds = None
        self._language = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if save_card is not None:
            self.save_card = save_card
        if card_id is not None:
            self.card_id = card_id
        if author_id is not None:
            self.author_id = author_id
        if statement_descriptor is not None:
            self.statement_descriptor = statement_descriptor
        self.success_url = success_url
        self.cancel_url = cancel_url
        if debited_funds is not None:
            self.debited_funds = debited_funds
        if language is not None:
            self.language = language

    @property
    def tag(self):
        """Gets the tag of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The tag of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AddonPaymentsPreauthorizeByWebPost.


        :param tag: The tag of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def save_card(self):
        """Gets the save_card of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The save_card of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: bool
        """
        return self._save_card

    @save_card.setter
    def save_card(self, save_card):
        """Sets the save_card of this AddonPaymentsPreauthorizeByWebPost.


        :param save_card: The save_card of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: bool
        """

        self._save_card = save_card

    @property
    def card_id(self):
        """Gets the card_id of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The card_id of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this AddonPaymentsPreauthorizeByWebPost.


        :param card_id: The card_id of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: str
        """

        self._card_id = card_id

    @property
    def author_id(self):
        """Gets the author_id of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The author_id of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this AddonPaymentsPreauthorizeByWebPost.


        :param author_id: The author_id of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: str
        """

        self._author_id = author_id

    @property
    def statement_descriptor(self):
        """Gets the statement_descriptor of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The statement_descriptor of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """Sets the statement_descriptor of this AddonPaymentsPreauthorizeByWebPost.


        :param statement_descriptor: The statement_descriptor of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: str
        """

        self._statement_descriptor = statement_descriptor

    @property
    def success_url(self):
        """Gets the success_url of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The success_url of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """Sets the success_url of this AddonPaymentsPreauthorizeByWebPost.


        :param success_url: The success_url of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: str
        """
        if success_url is None:
            raise ValueError("Invalid value for `success_url`, must not be `None`")  # noqa: E501

        self._success_url = success_url

    @property
    def cancel_url(self):
        """Gets the cancel_url of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The cancel_url of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this AddonPaymentsPreauthorizeByWebPost.


        :param cancel_url: The cancel_url of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: str
        """
        if cancel_url is None:
            raise ValueError("Invalid value for `cancel_url`, must not be `None`")  # noqa: E501

        self._cancel_url = cancel_url

    @property
    def debited_funds(self):
        """Gets the debited_funds of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The debited_funds of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: Money
        """
        return self._debited_funds

    @debited_funds.setter
    def debited_funds(self, debited_funds):
        """Sets the debited_funds of this AddonPaymentsPreauthorizeByWebPost.


        :param debited_funds: The debited_funds of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: Money
        """

        self._debited_funds = debited_funds

    @property
    def language(self):
        """Gets the language of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501


        :return: The language of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AddonPaymentsPreauthorizeByWebPost.


        :param language: The language of this AddonPaymentsPreauthorizeByWebPost.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "CA", "DE", "EN", "DA", "ES", "ET", "GL", "FI", "FR", "EL", "EU", "HU", "IT", "NL", "NO", "PL", "PT", "SK", "SV", "CS"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

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
        if issubclass(AddonPaymentsPreauthorizeByWebPost, dict):
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
        if not isinstance(other, AddonPaymentsPreauthorizeByWebPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

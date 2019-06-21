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


class PayOutBankwireResponse(object):
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
        'author_id': 'str',
        'credited_user_id': 'str',
        'debited_funds': 'Money',
        'credited_funds': 'Money',
        'fees': 'Money',
        'status': 'str',
        'result_code': 'str',
        'result_message': 'str',
        'execution_date': 'int',
        'type': 'str',
        'nature': 'str',
        'debited_wallet_id': 'str',
        'credited_wallet_id': 'str',
        'payment_type': 'str',
        'bank_account_id': 'str',
        'bank_wire_ref': 'str',
        'id': 'str',
        'creation_date': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'author_id': 'AuthorId',
        'credited_user_id': 'CreditedUserId',
        'debited_funds': 'DebitedFunds',
        'credited_funds': 'CreditedFunds',
        'fees': 'Fees',
        'status': 'Status',
        'result_code': 'ResultCode',
        'result_message': 'ResultMessage',
        'execution_date': 'ExecutionDate',
        'type': 'Type',
        'nature': 'Nature',
        'debited_wallet_id': 'DebitedWalletId',
        'credited_wallet_id': 'CreditedWalletId',
        'payment_type': 'PaymentType',
        'bank_account_id': 'BankAccountId',
        'bank_wire_ref': 'BankWireRef',
        'id': 'Id',
        'creation_date': 'CreationDate',
        'tag': 'Tag'
    }

    def __init__(self, author_id=None, credited_user_id=None, debited_funds=None, credited_funds=None, fees=None, status=None, result_code=None, result_message=None, execution_date=None, type=None, nature=None, debited_wallet_id=None, credited_wallet_id=None, payment_type=None, bank_account_id=None, bank_wire_ref=None, id=None, creation_date=None, tag=None):  # noqa: E501
        """PayOutBankwireResponse - a model defined in Swagger"""  # noqa: E501

        self._author_id = None
        self._credited_user_id = None
        self._debited_funds = None
        self._credited_funds = None
        self._fees = None
        self._status = None
        self._result_code = None
        self._result_message = None
        self._execution_date = None
        self._type = None
        self._nature = None
        self._debited_wallet_id = None
        self._credited_wallet_id = None
        self._payment_type = None
        self._bank_account_id = None
        self._bank_wire_ref = None
        self._id = None
        self._creation_date = None
        self._tag = None
        self.discriminator = None

        if author_id is not None:
            self.author_id = author_id
        if credited_user_id is not None:
            self.credited_user_id = credited_user_id
        if debited_funds is not None:
            self.debited_funds = debited_funds
        if credited_funds is not None:
            self.credited_funds = credited_funds
        if fees is not None:
            self.fees = fees
        if status is not None:
            self.status = status
        if result_code is not None:
            self.result_code = result_code
        if result_message is not None:
            self.result_message = result_message
        if execution_date is not None:
            self.execution_date = execution_date
        if type is not None:
            self.type = type
        if nature is not None:
            self.nature = nature
        if debited_wallet_id is not None:
            self.debited_wallet_id = debited_wallet_id
        if credited_wallet_id is not None:
            self.credited_wallet_id = credited_wallet_id
        if payment_type is not None:
            self.payment_type = payment_type
        if bank_account_id is not None:
            self.bank_account_id = bank_account_id
        if bank_wire_ref is not None:
            self.bank_wire_ref = bank_wire_ref
        if id is not None:
            self.id = id
        if creation_date is not None:
            self.creation_date = creation_date
        if tag is not None:
            self.tag = tag

    @property
    def author_id(self):
        """Gets the author_id of this PayOutBankwireResponse.  # noqa: E501


        :return: The author_id of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this PayOutBankwireResponse.


        :param author_id: The author_id of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._author_id = author_id

    @property
    def credited_user_id(self):
        """Gets the credited_user_id of this PayOutBankwireResponse.  # noqa: E501


        :return: The credited_user_id of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._credited_user_id

    @credited_user_id.setter
    def credited_user_id(self, credited_user_id):
        """Sets the credited_user_id of this PayOutBankwireResponse.


        :param credited_user_id: The credited_user_id of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._credited_user_id = credited_user_id

    @property
    def debited_funds(self):
        """Gets the debited_funds of this PayOutBankwireResponse.  # noqa: E501


        :return: The debited_funds of this PayOutBankwireResponse.  # noqa: E501
        :rtype: Money
        """
        return self._debited_funds

    @debited_funds.setter
    def debited_funds(self, debited_funds):
        """Sets the debited_funds of this PayOutBankwireResponse.


        :param debited_funds: The debited_funds of this PayOutBankwireResponse.  # noqa: E501
        :type: Money
        """

        self._debited_funds = debited_funds

    @property
    def credited_funds(self):
        """Gets the credited_funds of this PayOutBankwireResponse.  # noqa: E501


        :return: The credited_funds of this PayOutBankwireResponse.  # noqa: E501
        :rtype: Money
        """
        return self._credited_funds

    @credited_funds.setter
    def credited_funds(self, credited_funds):
        """Sets the credited_funds of this PayOutBankwireResponse.


        :param credited_funds: The credited_funds of this PayOutBankwireResponse.  # noqa: E501
        :type: Money
        """

        self._credited_funds = credited_funds

    @property
    def fees(self):
        """Gets the fees of this PayOutBankwireResponse.  # noqa: E501


        :return: The fees of this PayOutBankwireResponse.  # noqa: E501
        :rtype: Money
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this PayOutBankwireResponse.


        :param fees: The fees of this PayOutBankwireResponse.  # noqa: E501
        :type: Money
        """

        self._fees = fees

    @property
    def status(self):
        """Gets the status of this PayOutBankwireResponse.  # noqa: E501


        :return: The status of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PayOutBankwireResponse.


        :param status: The status of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "SUCCEEDED", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def result_code(self):
        """Gets the result_code of this PayOutBankwireResponse.  # noqa: E501


        :return: The result_code of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this PayOutBankwireResponse.


        :param result_code: The result_code of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._result_code = result_code

    @property
    def result_message(self):
        """Gets the result_message of this PayOutBankwireResponse.  # noqa: E501


        :return: The result_message of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_message

    @result_message.setter
    def result_message(self, result_message):
        """Sets the result_message of this PayOutBankwireResponse.


        :param result_message: The result_message of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._result_message = result_message

    @property
    def execution_date(self):
        """Gets the execution_date of this PayOutBankwireResponse.  # noqa: E501


        :return: The execution_date of this PayOutBankwireResponse.  # noqa: E501
        :rtype: int
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """Sets the execution_date of this PayOutBankwireResponse.


        :param execution_date: The execution_date of this PayOutBankwireResponse.  # noqa: E501
        :type: int
        """

        self._execution_date = execution_date

    @property
    def type(self):
        """Gets the type of this PayOutBankwireResponse.  # noqa: E501


        :return: The type of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PayOutBankwireResponse.


        :param type: The type of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PAYIN", "PAYOUT", "TRANSFER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def nature(self):
        """Gets the nature of this PayOutBankwireResponse.  # noqa: E501


        :return: The nature of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._nature

    @nature.setter
    def nature(self, nature):
        """Sets the nature of this PayOutBankwireResponse.


        :param nature: The nature of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["REGULAR", "REFUND", "REPUDIATION", "SETTLEMENT"]  # noqa: E501
        if nature not in allowed_values:
            raise ValueError(
                "Invalid value for `nature` ({0}), must be one of {1}"  # noqa: E501
                .format(nature, allowed_values)
            )

        self._nature = nature

    @property
    def debited_wallet_id(self):
        """Gets the debited_wallet_id of this PayOutBankwireResponse.  # noqa: E501


        :return: The debited_wallet_id of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._debited_wallet_id

    @debited_wallet_id.setter
    def debited_wallet_id(self, debited_wallet_id):
        """Sets the debited_wallet_id of this PayOutBankwireResponse.


        :param debited_wallet_id: The debited_wallet_id of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._debited_wallet_id = debited_wallet_id

    @property
    def credited_wallet_id(self):
        """Gets the credited_wallet_id of this PayOutBankwireResponse.  # noqa: E501


        :return: The credited_wallet_id of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._credited_wallet_id

    @credited_wallet_id.setter
    def credited_wallet_id(self, credited_wallet_id):
        """Sets the credited_wallet_id of this PayOutBankwireResponse.


        :param credited_wallet_id: The credited_wallet_id of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._credited_wallet_id = credited_wallet_id

    @property
    def payment_type(self):
        """Gets the payment_type of this PayOutBankwireResponse.  # noqa: E501


        :return: The payment_type of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this PayOutBankwireResponse.


        :param payment_type: The payment_type of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "BANK_WIRE"]  # noqa: E501
        if payment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_type, allowed_values)
            )

        self._payment_type = payment_type

    @property
    def bank_account_id(self):
        """Gets the bank_account_id of this PayOutBankwireResponse.  # noqa: E501


        :return: The bank_account_id of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._bank_account_id

    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        """Sets the bank_account_id of this PayOutBankwireResponse.


        :param bank_account_id: The bank_account_id of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._bank_account_id = bank_account_id

    @property
    def bank_wire_ref(self):
        """Gets the bank_wire_ref of this PayOutBankwireResponse.  # noqa: E501


        :return: The bank_wire_ref of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._bank_wire_ref

    @bank_wire_ref.setter
    def bank_wire_ref(self, bank_wire_ref):
        """Sets the bank_wire_ref of this PayOutBankwireResponse.


        :param bank_wire_ref: The bank_wire_ref of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._bank_wire_ref = bank_wire_ref

    @property
    def id(self):
        """Gets the id of this PayOutBankwireResponse.  # noqa: E501

        The item's ID  # noqa: E501

        :return: The id of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PayOutBankwireResponse.

        The item's ID  # noqa: E501

        :param id: The id of this PayOutBankwireResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def creation_date(self):
        """Gets the creation_date of this PayOutBankwireResponse.  # noqa: E501

        When the item was created  # noqa: E501

        :return: The creation_date of this PayOutBankwireResponse.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this PayOutBankwireResponse.

        When the item was created  # noqa: E501

        :param creation_date: The creation_date of this PayOutBankwireResponse.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def tag(self):
        """Gets the tag of this PayOutBankwireResponse.  # noqa: E501

        Custom data that you can add to this item  # noqa: E501

        :return: The tag of this PayOutBankwireResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PayOutBankwireResponse.

        Custom data that you can add to this item  # noqa: E501

        :param tag: The tag of this PayOutBankwireResponse.  # noqa: E501
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
        if issubclass(PayOutBankwireResponse, dict):
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
        if not isinstance(other, PayOutBankwireResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
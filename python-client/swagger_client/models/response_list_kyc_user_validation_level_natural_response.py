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

from swagger_client.models.kyc_user_validation_level_natural_response import KycUserValidationLevelNaturalResponse  # noqa: F401,E501


class ResponseListKycUserValidationLevelNaturalResponse(object):
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
        'values': 'list[KycUserValidationLevelNaturalResponse]',
        'total': 'int'
    }

    attribute_map = {
        'values': 'Values',
        'total': 'Total'
    }

    def __init__(self, values=None, total=None):  # noqa: E501
        """ResponseListKycUserValidationLevelNaturalResponse - a model defined in Swagger"""  # noqa: E501

        self._values = None
        self._total = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if total is not None:
            self.total = total

    @property
    def values(self):
        """Gets the values of this ResponseListKycUserValidationLevelNaturalResponse.  # noqa: E501


        :return: The values of this ResponseListKycUserValidationLevelNaturalResponse.  # noqa: E501
        :rtype: list[KycUserValidationLevelNaturalResponse]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ResponseListKycUserValidationLevelNaturalResponse.


        :param values: The values of this ResponseListKycUserValidationLevelNaturalResponse.  # noqa: E501
        :type: list[KycUserValidationLevelNaturalResponse]
        """

        self._values = values

    @property
    def total(self):
        """Gets the total of this ResponseListKycUserValidationLevelNaturalResponse.  # noqa: E501


        :return: The total of this ResponseListKycUserValidationLevelNaturalResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ResponseListKycUserValidationLevelNaturalResponse.


        :param total: The total of this ResponseListKycUserValidationLevelNaturalResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(ResponseListKycUserValidationLevelNaturalResponse, dict):
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
        if not isinstance(other, ResponseListKycUserValidationLevelNaturalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

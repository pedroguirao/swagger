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

from swagger_client.models.kyc_natural_user_data_dto import KycNaturalUserDataDto  # noqa: F401,E501
from swagger_client.models.kyc_validation_per_level_status import KycValidationPerLevelStatus  # noqa: F401,E501


class KycValidationUserStatusResponse(object):
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
        'user_data': 'KycNaturalUserDataDto',
        'validations': 'list[KycValidationPerLevelStatus]'
    }

    attribute_map = {
        'user_data': 'UserData',
        'validations': 'Validations'
    }

    def __init__(self, user_data=None, validations=None):  # noqa: E501
        """KycValidationUserStatusResponse - a model defined in Swagger"""  # noqa: E501

        self._user_data = None
        self._validations = None
        self.discriminator = None

        if user_data is not None:
            self.user_data = user_data
        if validations is not None:
            self.validations = validations

    @property
    def user_data(self):
        """Gets the user_data of this KycValidationUserStatusResponse.  # noqa: E501


        :return: The user_data of this KycValidationUserStatusResponse.  # noqa: E501
        :rtype: KycNaturalUserDataDto
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this KycValidationUserStatusResponse.


        :param user_data: The user_data of this KycValidationUserStatusResponse.  # noqa: E501
        :type: KycNaturalUserDataDto
        """

        self._user_data = user_data

    @property
    def validations(self):
        """Gets the validations of this KycValidationUserStatusResponse.  # noqa: E501


        :return: The validations of this KycValidationUserStatusResponse.  # noqa: E501
        :rtype: list[KycValidationPerLevelStatus]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """Sets the validations of this KycValidationUserStatusResponse.


        :param validations: The validations of this KycValidationUserStatusResponse.  # noqa: E501
        :type: list[KycValidationPerLevelStatus]
        """

        self._validations = validations

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
        if issubclass(KycValidationUserStatusResponse, dict):
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
        if not isinstance(other, KycValidationUserStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

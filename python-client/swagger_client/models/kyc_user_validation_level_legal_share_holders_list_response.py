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

from swagger_client.models.kyc_user_validation_share_holder_list_item_response_natural import KycUserValidationShareHolderListItemResponseNatural  # noqa: F401,E501


class KycUserValidationLevelLegalShareHoldersListResponse(object):
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
        'share_holders': 'list[KycUserValidationShareHolderListItemResponseNatural]'
    }

    attribute_map = {
        'share_holders': 'ShareHolders'
    }

    def __init__(self, share_holders=None):  # noqa: E501
        """KycUserValidationLevelLegalShareHoldersListResponse - a model defined in Swagger"""  # noqa: E501

        self._share_holders = None
        self.discriminator = None

        if share_holders is not None:
            self.share_holders = share_holders

    @property
    def share_holders(self):
        """Gets the share_holders of this KycUserValidationLevelLegalShareHoldersListResponse.  # noqa: E501


        :return: The share_holders of this KycUserValidationLevelLegalShareHoldersListResponse.  # noqa: E501
        :rtype: list[KycUserValidationShareHolderListItemResponseNatural]
        """
        return self._share_holders

    @share_holders.setter
    def share_holders(self, share_holders):
        """Sets the share_holders of this KycUserValidationLevelLegalShareHoldersListResponse.


        :param share_holders: The share_holders of this KycUserValidationLevelLegalShareHoldersListResponse.  # noqa: E501
        :type: list[KycUserValidationShareHolderListItemResponseNatural]
        """

        self._share_holders = share_holders

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
        if issubclass(KycUserValidationLevelLegalShareHoldersListResponse, dict):
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
        if not isinstance(other, KycUserValidationLevelLegalShareHoldersListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

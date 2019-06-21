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


class RedsysPayByWebResponse(object):
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
        'pay_in_id': 'str',
        'url': 'str',
        'ds_signature_version': 'str',
        'ds_merchant_parameters': 'str',
        'ds_signature': 'str'
    }

    attribute_map = {
        'pay_in_id': 'PayInId',
        'url': 'Url',
        'ds_signature_version': 'Ds_SignatureVersion',
        'ds_merchant_parameters': 'Ds_MerchantParameters',
        'ds_signature': 'Ds_Signature'
    }

    def __init__(self, pay_in_id=None, url=None, ds_signature_version=None, ds_merchant_parameters=None, ds_signature=None):  # noqa: E501
        """RedsysPayByWebResponse - a model defined in Swagger"""  # noqa: E501

        self._pay_in_id = None
        self._url = None
        self._ds_signature_version = None
        self._ds_merchant_parameters = None
        self._ds_signature = None
        self.discriminator = None

        if pay_in_id is not None:
            self.pay_in_id = pay_in_id
        if url is not None:
            self.url = url
        if ds_signature_version is not None:
            self.ds_signature_version = ds_signature_version
        if ds_merchant_parameters is not None:
            self.ds_merchant_parameters = ds_merchant_parameters
        if ds_signature is not None:
            self.ds_signature = ds_signature

    @property
    def pay_in_id(self):
        """Gets the pay_in_id of this RedsysPayByWebResponse.  # noqa: E501


        :return: The pay_in_id of this RedsysPayByWebResponse.  # noqa: E501
        :rtype: str
        """
        return self._pay_in_id

    @pay_in_id.setter
    def pay_in_id(self, pay_in_id):
        """Sets the pay_in_id of this RedsysPayByWebResponse.


        :param pay_in_id: The pay_in_id of this RedsysPayByWebResponse.  # noqa: E501
        :type: str
        """

        self._pay_in_id = pay_in_id

    @property
    def url(self):
        """Gets the url of this RedsysPayByWebResponse.  # noqa: E501


        :return: The url of this RedsysPayByWebResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RedsysPayByWebResponse.


        :param url: The url of this RedsysPayByWebResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def ds_signature_version(self):
        """Gets the ds_signature_version of this RedsysPayByWebResponse.  # noqa: E501


        :return: The ds_signature_version of this RedsysPayByWebResponse.  # noqa: E501
        :rtype: str
        """
        return self._ds_signature_version

    @ds_signature_version.setter
    def ds_signature_version(self, ds_signature_version):
        """Sets the ds_signature_version of this RedsysPayByWebResponse.


        :param ds_signature_version: The ds_signature_version of this RedsysPayByWebResponse.  # noqa: E501
        :type: str
        """

        self._ds_signature_version = ds_signature_version

    @property
    def ds_merchant_parameters(self):
        """Gets the ds_merchant_parameters of this RedsysPayByWebResponse.  # noqa: E501


        :return: The ds_merchant_parameters of this RedsysPayByWebResponse.  # noqa: E501
        :rtype: str
        """
        return self._ds_merchant_parameters

    @ds_merchant_parameters.setter
    def ds_merchant_parameters(self, ds_merchant_parameters):
        """Sets the ds_merchant_parameters of this RedsysPayByWebResponse.


        :param ds_merchant_parameters: The ds_merchant_parameters of this RedsysPayByWebResponse.  # noqa: E501
        :type: str
        """

        self._ds_merchant_parameters = ds_merchant_parameters

    @property
    def ds_signature(self):
        """Gets the ds_signature of this RedsysPayByWebResponse.  # noqa: E501


        :return: The ds_signature of this RedsysPayByWebResponse.  # noqa: E501
        :rtype: str
        """
        return self._ds_signature

    @ds_signature.setter
    def ds_signature(self, ds_signature):
        """Sets the ds_signature of this RedsysPayByWebResponse.


        :param ds_signature: The ds_signature of this RedsysPayByWebResponse.  # noqa: E501
        :type: str
        """

        self._ds_signature = ds_signature

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
        if issubclass(RedsysPayByWebResponse, dict):
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
        if not isinstance(other, RedsysPayByWebResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

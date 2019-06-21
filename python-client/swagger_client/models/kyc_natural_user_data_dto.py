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

from swagger_client.models.property_validation_country import PropertyValidationCountry  # noqa: F401,E501
from swagger_client.models.property_validation_date_nullable import PropertyValidationDateNullable  # noqa: F401,E501
from swagger_client.models.property_validation_string import PropertyValidationString  # noqa: F401,E501
from swagger_client.models.t_address_validation_result import TAddressValidationResult  # noqa: F401,E501
from swagger_client.models.t_kyc_file_details import TKycFileDetails  # noqa: F401,E501
from swagger_client.models.t_telephone_validation_result import TTelephoneValidationResult  # noqa: F401,E501


class KycNaturalUserDataDto(object):
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
        'email': 'PropertyValidationString',
        'first_name': 'PropertyValidationString',
        'last_name': 'PropertyValidationString',
        'address': 'TAddressValidationResult',
        'telephone': 'TTelephoneValidationResult',
        'birthday': 'PropertyValidationDateNullable',
        'nationality': 'PropertyValidationCountry',
        'country_of_residence': 'PropertyValidationCountry',
        'occupation': 'PropertyValidationString',
        'id_card': 'PropertyValidationString',
        'id_card_document': 'TKycFileDetails'
    }

    attribute_map = {
        'email': 'Email',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'address': 'Address',
        'telephone': 'Telephone',
        'birthday': 'Birthday',
        'nationality': 'Nationality',
        'country_of_residence': 'CountryOfResidence',
        'occupation': 'Occupation',
        'id_card': 'IdCard',
        'id_card_document': 'IdCardDocument'
    }

    def __init__(self, email=None, first_name=None, last_name=None, address=None, telephone=None, birthday=None, nationality=None, country_of_residence=None, occupation=None, id_card=None, id_card_document=None):  # noqa: E501
        """KycNaturalUserDataDto - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._last_name = None
        self._address = None
        self._telephone = None
        self._birthday = None
        self._nationality = None
        self._country_of_residence = None
        self._occupation = None
        self._id_card = None
        self._id_card_document = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if address is not None:
            self.address = address
        if telephone is not None:
            self.telephone = telephone
        if birthday is not None:
            self.birthday = birthday
        if nationality is not None:
            self.nationality = nationality
        if country_of_residence is not None:
            self.country_of_residence = country_of_residence
        if occupation is not None:
            self.occupation = occupation
        if id_card is not None:
            self.id_card = id_card
        if id_card_document is not None:
            self.id_card_document = id_card_document

    @property
    def email(self):
        """Gets the email of this KycNaturalUserDataDto.  # noqa: E501


        :return: The email of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: PropertyValidationString
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this KycNaturalUserDataDto.


        :param email: The email of this KycNaturalUserDataDto.  # noqa: E501
        :type: PropertyValidationString
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this KycNaturalUserDataDto.  # noqa: E501

        The name of the user  # noqa: E501

        :return: The first_name of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: PropertyValidationString
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this KycNaturalUserDataDto.

        The name of the user  # noqa: E501

        :param first_name: The first_name of this KycNaturalUserDataDto.  # noqa: E501
        :type: PropertyValidationString
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this KycNaturalUserDataDto.  # noqa: E501

        The last name of the user  # noqa: E501

        :return: The last_name of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: PropertyValidationString
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this KycNaturalUserDataDto.

        The last name of the user  # noqa: E501

        :param last_name: The last_name of this KycNaturalUserDataDto.  # noqa: E501
        :type: PropertyValidationString
        """

        self._last_name = last_name

    @property
    def address(self):
        """Gets the address of this KycNaturalUserDataDto.  # noqa: E501

        The address  # noqa: E501

        :return: The address of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: TAddressValidationResult
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this KycNaturalUserDataDto.

        The address  # noqa: E501

        :param address: The address of this KycNaturalUserDataDto.  # noqa: E501
        :type: TAddressValidationResult
        """

        self._address = address

    @property
    def telephone(self):
        """Gets the telephone of this KycNaturalUserDataDto.  # noqa: E501


        :return: The telephone of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: TTelephoneValidationResult
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this KycNaturalUserDataDto.


        :param telephone: The telephone of this KycNaturalUserDataDto.  # noqa: E501
        :type: TTelephoneValidationResult
        """

        self._telephone = telephone

    @property
    def birthday(self):
        """Gets the birthday of this KycNaturalUserDataDto.  # noqa: E501

        The date of birth of the user - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before)  # noqa: E501

        :return: The birthday of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: PropertyValidationDateNullable
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this KycNaturalUserDataDto.

        The date of birth of the user - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before)  # noqa: E501

        :param birthday: The birthday of this KycNaturalUserDataDto.  # noqa: E501
        :type: PropertyValidationDateNullable
        """

        self._birthday = birthday

    @property
    def nationality(self):
        """Gets the nationality of this KycNaturalUserDataDto.  # noqa: E501

        The user’s nationality. ISO 3166-1 alpha-2 format is expected  # noqa: E501

        :return: The nationality of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: PropertyValidationCountry
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this KycNaturalUserDataDto.

        The user’s nationality. ISO 3166-1 alpha-2 format is expected  # noqa: E501

        :param nationality: The nationality of this KycNaturalUserDataDto.  # noqa: E501
        :type: PropertyValidationCountry
        """

        self._nationality = nationality

    @property
    def country_of_residence(self):
        """Gets the country_of_residence of this KycNaturalUserDataDto.  # noqa: E501

        The user’s country of residence. ISO 3166-1 alpha-2 format is expected  # noqa: E501

        :return: The country_of_residence of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: PropertyValidationCountry
        """
        return self._country_of_residence

    @country_of_residence.setter
    def country_of_residence(self, country_of_residence):
        """Sets the country_of_residence of this KycNaturalUserDataDto.

        The user’s country of residence. ISO 3166-1 alpha-2 format is expected  # noqa: E501

        :param country_of_residence: The country_of_residence of this KycNaturalUserDataDto.  # noqa: E501
        :type: PropertyValidationCountry
        """

        self._country_of_residence = country_of_residence

    @property
    def occupation(self):
        """Gets the occupation of this KycNaturalUserDataDto.  # noqa: E501

        User’s occupation, ie. Work  # noqa: E501

        :return: The occupation of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: PropertyValidationString
        """
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        """Sets the occupation of this KycNaturalUserDataDto.

        User’s occupation, ie. Work  # noqa: E501

        :param occupation: The occupation of this KycNaturalUserDataDto.  # noqa: E501
        :type: PropertyValidationString
        """

        self._occupation = occupation

    @property
    def id_card(self):
        """Gets the id_card of this KycNaturalUserDataDto.  # noqa: E501


        :return: The id_card of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: PropertyValidationString
        """
        return self._id_card

    @id_card.setter
    def id_card(self, id_card):
        """Sets the id_card of this KycNaturalUserDataDto.


        :param id_card: The id_card of this KycNaturalUserDataDto.  # noqa: E501
        :type: PropertyValidationString
        """

        self._id_card = id_card

    @property
    def id_card_document(self):
        """Gets the id_card_document of this KycNaturalUserDataDto.  # noqa: E501

        Identity card file reference  # noqa: E501

        :return: The id_card_document of this KycNaturalUserDataDto.  # noqa: E501
        :rtype: TKycFileDetails
        """
        return self._id_card_document

    @id_card_document.setter
    def id_card_document(self, id_card_document):
        """Sets the id_card_document of this KycNaturalUserDataDto.

        Identity card file reference  # noqa: E501

        :param id_card_document: The id_card_document of this KycNaturalUserDataDto.  # noqa: E501
        :type: TKycFileDetails
        """

        self._id_card_document = id_card_document

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
        if issubclass(KycNaturalUserDataDto, dict):
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
        if not isinstance(other, KycNaturalUserDataDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

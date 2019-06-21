# coding: utf-8

"""
    MarketPay API

    API for Smart Contracts and Payments  # noqa: E501

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.pay_ins_addon_payments_api import PayInsAddonPaymentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPayInsAddonPaymentsApi(unittest.TestCase):
    """PayInsAddonPaymentsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.pay_ins_addon_payments_api.PayInsAddonPaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pay_ins_addon_payments_addon_payments_get_payment(self):
        """Test case for pay_ins_addon_payments_addon_payments_get_payment

        """
        pass

    def test_pay_ins_addon_payments_addon_payments_get_preauthorization(self):
        """Test case for pay_ins_addon_payments_addon_payments_get_preauthorization

        """
        pass

    def test_pay_ins_addon_payments_addon_payments_post_payment_by_web(self):
        """Test case for pay_ins_addon_payments_addon_payments_post_payment_by_web

        """
        pass

    def test_pay_ins_addon_payments_addon_payments_post_payment_direct(self):
        """Test case for pay_ins_addon_payments_addon_payments_post_payment_direct

        """
        pass

    def test_pay_ins_addon_payments_addon_payments_post_preauthorization_by_web(self):
        """Test case for pay_ins_addon_payments_addon_payments_post_preauthorization_by_web

        """
        pass

    def test_pay_ins_addon_payments_addon_payments_post_preauthorization_cancellation(self):
        """Test case for pay_ins_addon_payments_addon_payments_post_preauthorization_cancellation

        """
        pass

    def test_pay_ins_addon_payments_addon_payments_post_preauthorization_confirmation(self):
        """Test case for pay_ins_addon_payments_addon_payments_post_preauthorization_confirmation

        """
        pass

    def test_pay_ins_addon_payments_addon_payments_post_refund(self):
        """Test case for pay_ins_addon_payments_addon_payments_post_refund

        """
        pass


if __name__ == '__main__':
    unittest.main()
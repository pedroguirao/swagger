# coding: utf-8

# flake8: noqa
"""
    MarketPay API

    API for Smart Contracts and Payments  # noqa: E501

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.addon_payments_pay_by_web_post import AddonPaymentsPayByWebPost
from swagger_client.models.addon_payments_pay_by_web_response import AddonPaymentsPayByWebResponse
from swagger_client.models.addon_payments_pay_direct_post import AddonPaymentsPayDirectPost
from swagger_client.models.addon_payments_pay_direct_response import AddonPaymentsPayDirectResponse
from swagger_client.models.addon_payments_pay_ins_response import AddonPaymentsPayInsResponse
from swagger_client.models.addon_payments_preauthorization_cancellation_post import AddonPaymentsPreauthorizationCancellationPost
from swagger_client.models.addon_payments_preauthorization_cancellation_response import AddonPaymentsPreauthorizationCancellationResponse
from swagger_client.models.addon_payments_preauthorization_confirmation_post import AddonPaymentsPreauthorizationConfirmationPost
from swagger_client.models.addon_payments_preauthorization_confirmation_response import AddonPaymentsPreauthorizationConfirmationResponse
from swagger_client.models.addon_payments_preauthorize_by_web_post import AddonPaymentsPreauthorizeByWebPost
from swagger_client.models.addon_payments_preauthorize_by_web_response import AddonPaymentsPreauthorizeByWebResponse
from swagger_client.models.addon_payments_preauthorize_response import AddonPaymentsPreauthorizeResponse
from swagger_client.models.addon_payments_refund_post import AddonPaymentsRefundPost
from swagger_client.models.addon_payments_refund_response import AddonPaymentsRefundResponse
from swagger_client.models.address import Address
from swagger_client.models.aplazame_order_item import AplazameOrderItem
from swagger_client.models.aplazame_pay_by_web_post import AplazamePayByWebPost
from swagger_client.models.aplazame_pay_by_web_response import AplazamePayByWebResponse
from swagger_client.models.aplazame_pay_ins_response import AplazamePayInsResponse
from swagger_client.models.aplazame_refund_payment_post import AplazameRefundPaymentPost
from swagger_client.models.aplazame_refund_response import AplazameRefundResponse
from swagger_client.models.bank_account_ca_post import BankAccountCaPost
from swagger_client.models.bank_account_ca_response import BankAccountCaResponse
from swagger_client.models.bank_account_gb_post import BankAccountGbPost
from swagger_client.models.bank_account_gb_response import BankAccountGbResponse
from swagger_client.models.bank_account_iban_post import BankAccountIbanPost
from swagger_client.models.bank_account_iban_response import BankAccountIbanResponse
from swagger_client.models.bank_account_other_post import BankAccountOtherPost
from swagger_client.models.bank_account_other_response import BankAccountOtherResponse
from swagger_client.models.bank_account_response import BankAccountResponse
from swagger_client.models.bank_account_us_post import BankAccountUsPost
from swagger_client.models.bank_account_us_response import BankAccountUsResponse
from swagger_client.models.bankwire_pay_in_bank_account import BankwirePayInBankAccount
from swagger_client.models.card_put import CardPut
from swagger_client.models.card_response import CardResponse
from swagger_client.models.custom_api_error_response import CustomApiErrorResponse
from swagger_client.models.customer import Customer
from swagger_client.models.document_file_status import DocumentFileStatus
from swagger_client.models.entity_tag_header_value import EntityTagHeaderValue
from swagger_client.models.event_response import EventResponse
from swagger_client.models.example_user_natural_post import ExampleUserNaturalPost
from swagger_client.models.file_result import FileResult
from swagger_client.models.form_field import FormField
from swagger_client.models.hook_post import HookPost
from swagger_client.models.hook_put import HookPut
from swagger_client.models.hook_response import HookResponse
from swagger_client.models.kyc_board_member_container_dto import KycBoardMemberContainerDto
from swagger_client.models.kyc_board_member_response import KycBoardMemberResponse
from swagger_client.models.kyc_document_details import KycDocumentDetails
from swagger_client.models.kyc_file_upload_response import KycFileUploadResponse
from swagger_client.models.kyc_identification_request import KycIdentificationRequest
from swagger_client.models.kyc_legal_user_data_dto import KycLegalUserDataDto
from swagger_client.models.kyc_natural_user_data_dto import KycNaturalUserDataDto
from swagger_client.models.kyc_share_holder_container_dto import KycShareHolderContainerDto
from swagger_client.models.kyc_share_holder_response import KycShareHolderResponse
from swagger_client.models.kyc_user_legal_put import KycUserLegalPut
from swagger_client.models.kyc_user_natural_put import KycUserNaturalPut
from swagger_client.models.kyc_user_validation_board_member_list_item_response import KycUserValidationBoardMemberListItemResponse
from swagger_client.models.kyc_user_validation_board_member_post import KycUserValidationBoardMemberPost
from swagger_client.models.kyc_user_validation_board_member_put import KycUserValidationBoardMemberPut
from swagger_client.models.kyc_user_validation_level_legal_board_members_list_response import KycUserValidationLevelLegalBoardMembersListResponse
from swagger_client.models.kyc_user_validation_level_legal_response import KycUserValidationLevelLegalResponse
from swagger_client.models.kyc_user_validation_level_legal_share_holders_list_response import KycUserValidationLevelLegalShareHoldersListResponse
from swagger_client.models.kyc_user_validation_level_natural_response import KycUserValidationLevelNaturalResponse
from swagger_client.models.kyc_user_validation_share_holder_list_item_response_natural import KycUserValidationShareHolderListItemResponseNatural
from swagger_client.models.kyc_user_validation_share_holder_natural_post import KycUserValidationShareHolderNaturalPost
from swagger_client.models.kyc_user_validation_share_holder_natural_put import KycUserValidationShareHolderNaturalPut
from swagger_client.models.kyc_validation_per_level_status import KycValidationPerLevelStatus
from swagger_client.models.kyc_validation_request_response import KycValidationRequestResponse
from swagger_client.models.kyc_validation_user_legal_status_response import KycValidationUserLegalStatusResponse
from swagger_client.models.kyc_validation_user_status_response import KycValidationUserStatusResponse
from swagger_client.models.money import Money
from swagger_client.models.pay_in_bankwire_post import PayInBankwirePost
from swagger_client.models.pay_in_bankwire_refund_post import PayInBankwireRefundPost
from swagger_client.models.pay_in_bankwire_refund_response import PayInBankwireRefundResponse
from swagger_client.models.pay_in_bankwire_response import PayInBankwireResponse
from swagger_client.models.pay_out_bankwire_post import PayOutBankwirePost
from swagger_client.models.pay_out_bankwire_response import PayOutBankwireResponse
from swagger_client.models.payment_addon_payments_data import PaymentAddonPaymentsData
from swagger_client.models.payment_redsys_data import PaymentRedsysData
from swagger_client.models.payment_web_pay_data import PaymentWebPayData
from swagger_client.models.plugin_pay_in_post import PluginPayInPost
from swagger_client.models.plugin_pay_ins_response import PluginPayInsResponse
from swagger_client.models.plugin_pay_out_post import PluginPayOutPost
from swagger_client.models.plugin_pay_out_response import PluginPayOutResponse
from swagger_client.models.preauthorization_addon_payments_data import PreauthorizationAddonPaymentsData
from swagger_client.models.preauthorization_redsys_data import PreauthorizationRedsysData
from swagger_client.models.property_validation_country import PropertyValidationCountry
from swagger_client.models.property_validation_date_nullable import PropertyValidationDateNullable
from swagger_client.models.property_validation_decimal import PropertyValidationDecimal
from swagger_client.models.property_validation_string import PropertyValidationString
from swagger_client.models.redsys_pay_by_web_post import RedsysPayByWebPost
from swagger_client.models.redsys_pay_by_web_response import RedsysPayByWebResponse
from swagger_client.models.redsys_pay_ins_response import RedsysPayInsResponse
from swagger_client.models.redsys_preauthorization_cancellation_post import RedsysPreauthorizationCancellationPost
from swagger_client.models.redsys_preauthorization_cancellation_response import RedsysPreauthorizationCancellationResponse
from swagger_client.models.redsys_preauthorization_confirmation_post import RedsysPreauthorizationConfirmationPost
from swagger_client.models.redsys_preauthorization_confirmation_response import RedsysPreauthorizationConfirmationResponse
from swagger_client.models.redsys_preauthorize_by_web_post import RedsysPreauthorizeByWebPost
from swagger_client.models.redsys_preauthorize_by_web_response import RedsysPreauthorizeByWebResponse
from swagger_client.models.redsys_preauthorize_response import RedsysPreauthorizeResponse
from swagger_client.models.redsys_refund_post import RedsysRefundPost
from swagger_client.models.redsys_refund_response import RedsysRefundResponse
from swagger_client.models.refund_addon_payments_data import RefundAddonPaymentsData
from swagger_client.models.refund_reason import RefundReason
from swagger_client.models.refund_redsys_data import RefundRedsysData
from swagger_client.models.response_list_card_response import ResponseListCardResponse
from swagger_client.models.response_list_kyc_user_validation_level_legal_response import ResponseListKycUserValidationLevelLegalResponse
from swagger_client.models.response_list_kyc_user_validation_level_natural_response import ResponseListKycUserValidationLevelNaturalResponse
from swagger_client.models.response_list_transaction_response import ResponseListTransactionResponse
from swagger_client.models.response_list_transfer_methods_response import ResponseListTransferMethodsResponse
from swagger_client.models.response_list_transfer_response import ResponseListTransferResponse
from swagger_client.models.response_list_user_legal_response import ResponseListUserLegalResponse
from swagger_client.models.response_list_user_response import ResponseListUserResponse
from swagger_client.models.response_list_wallet_client_instrument_response import ResponseListWalletClientInstrumentResponse
from swagger_client.models.response_list_wallet_response import ResponseListWalletResponse
from swagger_client.models.string_segment import StringSegment
from swagger_client.models.t_address_validation_result import TAddressValidationResult
from swagger_client.models.t_kyc_file_details import TKycFileDetails
from swagger_client.models.t_telephone_validation_result import TTelephoneValidationResult
from swagger_client.models.telephone import Telephone
from swagger_client.models.transaction_response import TransactionResponse
from swagger_client.models.transfer_methods_response import TransferMethodsResponse
from swagger_client.models.transfer_post import TransferPost
from swagger_client.models.transfer_response import TransferResponse
from swagger_client.models.user_legal_post import UserLegalPost
from swagger_client.models.user_legal_put import UserLegalPut
from swagger_client.models.user_legal_response import UserLegalResponse
from swagger_client.models.user_natural_post import UserNaturalPost
from swagger_client.models.user_natural_put import UserNaturalPut
from swagger_client.models.user_natural_response import UserNaturalResponse
from swagger_client.models.user_response import UserResponse
from swagger_client.models.wallet_balance import WalletBalance
from swagger_client.models.wallet_client_instrument_response import WalletClientInstrumentResponse
from swagger_client.models.wallet_post import WalletPost
from swagger_client.models.wallet_put import WalletPut
from swagger_client.models.wallet_query_balances_by_ids_post import WalletQueryBalancesByIdsPost
from swagger_client.models.wallet_response import WalletResponse
from swagger_client.models.web_pay_pay_by_web_post import WebPayPayByWebPost
from swagger_client.models.web_pay_pay_by_web_response import WebPayPayByWebResponse
from swagger_client.models.web_pay_pay_ins_response import WebPayPayInsResponse
from swagger_client.models.web_pay_refund_post import WebPayRefundPost
from swagger_client.models.web_pay_refund_response import WebPayRefundResponse
from swagger_client.models.web_pay_token_delete_response import WebPayTokenDeleteResponse
from swagger_client.models.web_pay_token_request_post import WebPayTokenRequestPost
from swagger_client.models.web_pay_tokenization_response import WebPayTokenizationResponse
from swagger_client.models.web_pay_tokenize_by_web_response import WebPayTokenizeByWebResponse

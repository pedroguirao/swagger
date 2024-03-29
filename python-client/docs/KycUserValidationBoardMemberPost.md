# KycUserValidationBoardMemberPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s email address - must be a valid email | [optional] 
**first_name** | **str** | The name of the user | [optional] 
**last_name** | **str** | The last name of the user | [optional] 
**birthday** | **int** | The date of birth of the user - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before) | [optional] 
**nationality** | **str** | The user’s nationality. ISO 3166-1 alpha-2 format is expected | [optional] 
**country_of_residence** | **str** | The user’s country of residence. ISO 3166-1 alpha-2 format is expected | [optional] 
**telephone** | [**Telephone**](Telephone.md) |  | [optional] 
**id_card** | **str** |  | [optional] 
**occupation** | **str** |  | [optional] 
**id_card_document** | [**KycDocumentDetails**](KycDocumentDetails.md) |  | [optional] 
**address** | [**Address**](Address.md) | The address | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



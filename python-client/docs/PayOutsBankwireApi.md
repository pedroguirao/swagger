# swagger_client.PayOutsBankwireApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_outs_bankwire_get**](PayOutsBankwireApi.md#pay_outs_bankwire_get) | **GET** /v2.1/PayOutsBankwire/payments/{PayOutId} | 
[**pay_outs_bankwire_post**](PayOutsBankwireApi.md#pay_outs_bankwire_post) | **POST** /v2.1/PayOutsBankwire/payments/direct | 


# **pay_outs_bankwire_get**
> PayOutBankwireResponse pay_outs_bankwire_get(pay_out_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PayOutsBankwireApi(swagger_client.ApiClient(configuration))
pay_out_id = 789 # int | 

try:
    api_response = api_instance.pay_outs_bankwire_get(pay_out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayOutsBankwireApi->pay_outs_bankwire_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_out_id** | **int**|  | 

### Return type

[**PayOutBankwireResponse**](PayOutBankwireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_outs_bankwire_post**
> PayOutBankwireResponse pay_outs_bankwire_post(bankwire_pay_out=bankwire_pay_out)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PayOutsBankwireApi(swagger_client.ApiClient(configuration))
bankwire_pay_out = swagger_client.PayOutBankwirePost() # PayOutBankwirePost |  (optional)

try:
    api_response = api_instance.pay_outs_bankwire_post(bankwire_pay_out=bankwire_pay_out)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayOutsBankwireApi->pay_outs_bankwire_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankwire_pay_out** | [**PayOutBankwirePost**](PayOutBankwirePost.md)|  | [optional] 

### Return type

[**PayOutBankwireResponse**](PayOutBankwireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


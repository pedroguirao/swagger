# swagger_client.PayInsAplazameApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_ins_aplazame_aplazame_get_payment**](PayInsAplazameApi.md#pay_ins_aplazame_aplazame_get_payment) | **GET** /v2.1/PayInsAplazame/payments/{PayInId} | 
[**pay_ins_aplazame_aplazame_post_payment_by_web**](PayInsAplazameApi.md#pay_ins_aplazame_aplazame_post_payment_by_web) | **POST** /v2.1/PayInsAplazame/payments/web | 
[**pay_ins_aplazame_refund**](PayInsAplazameApi.md#pay_ins_aplazame_refund) | **POST** /v2.1/PayInsAplazame/payments/{PayInId}/refunds | 


# **pay_ins_aplazame_aplazame_get_payment**
> AplazamePayInsResponse pay_ins_aplazame_aplazame_get_payment(pay_in_id)



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
api_instance = swagger_client.PayInsAplazameApi(swagger_client.ApiClient(configuration))
pay_in_id = 'pay_in_id_example' # str | 

try:
    api_response = api_instance.pay_ins_aplazame_aplazame_get_payment(pay_in_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAplazameApi->pay_ins_aplazame_aplazame_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **str**|  | 

### Return type

[**AplazamePayInsResponse**](AplazamePayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_aplazame_aplazame_post_payment_by_web**
> AplazamePayByWebResponse pay_ins_aplazame_aplazame_post_payment_by_web(aplazame_pay_in=aplazame_pay_in)



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
api_instance = swagger_client.PayInsAplazameApi(swagger_client.ApiClient(configuration))
aplazame_pay_in = swagger_client.AplazamePayByWebPost() # AplazamePayByWebPost |  (optional)

try:
    api_response = api_instance.pay_ins_aplazame_aplazame_post_payment_by_web(aplazame_pay_in=aplazame_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAplazameApi->pay_ins_aplazame_aplazame_post_payment_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aplazame_pay_in** | [**AplazamePayByWebPost**](AplazamePayByWebPost.md)|  | [optional] 

### Return type

[**AplazamePayByWebResponse**](AplazamePayByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_aplazame_refund**
> AplazameRefundResponse pay_ins_aplazame_refund(pay_in_id, aplazame_refund=aplazame_refund)



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
api_instance = swagger_client.PayInsAplazameApi(swagger_client.ApiClient(configuration))
pay_in_id = 'pay_in_id_example' # str | 
aplazame_refund = swagger_client.AplazameRefundPaymentPost() # AplazameRefundPaymentPost |  (optional)

try:
    api_response = api_instance.pay_ins_aplazame_refund(pay_in_id, aplazame_refund=aplazame_refund)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAplazameApi->pay_ins_aplazame_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **str**|  | 
 **aplazame_refund** | [**AplazameRefundPaymentPost**](AplazameRefundPaymentPost.md)|  | [optional] 

### Return type

[**AplazameRefundResponse**](AplazameRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


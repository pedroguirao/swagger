# swagger_client.PayInsWebPayApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_ins_web_pay_delete_web_pay_token**](PayInsWebPayApi.md#pay_ins_web_pay_delete_web_pay_token) | **DELETE** /v2.1/PayInsWebPay/token/{TokenId} | 
[**pay_ins_web_pay_get_web_pay_tokenization**](PayInsWebPayApi.md#pay_ins_web_pay_get_web_pay_tokenization) | **GET** /v2.1/PayInsWebPay/token/{TokenId} | 
[**pay_ins_web_pay_web_pay_get_payment**](PayInsWebPayApi.md#pay_ins_web_pay_web_pay_get_payment) | **GET** /v2.1/PayInsWebPay/payments/{PayInId} | 
[**pay_ins_web_pay_web_pay_post_payment_by_web**](PayInsWebPayApi.md#pay_ins_web_pay_web_pay_post_payment_by_web) | **POST** /v2.1/PayInsWebPay/payments/web | 
[**pay_ins_web_pay_web_pay_post_refund**](PayInsWebPayApi.md#pay_ins_web_pay_web_pay_post_refund) | **POST** /v2.1/PayInsWebPay/payments/{PayInId}/refunds | 
[**pay_ins_web_pay_web_pay_save_card**](PayInsWebPayApi.md#pay_ins_web_pay_web_pay_save_card) | **POST** /v2.1/PayInsWebPay/token/web | 


# **pay_ins_web_pay_delete_web_pay_token**
> WebPayTokenDeleteResponse pay_ins_web_pay_delete_web_pay_token(token_id)



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
api_instance = swagger_client.PayInsWebPayApi(swagger_client.ApiClient(configuration))
token_id = 789 # int | 

try:
    api_response = api_instance.pay_ins_web_pay_delete_web_pay_token(token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsWebPayApi->pay_ins_web_pay_delete_web_pay_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

[**WebPayTokenDeleteResponse**](WebPayTokenDeleteResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_web_pay_get_web_pay_tokenization**
> WebPayTokenizationResponse pay_ins_web_pay_get_web_pay_tokenization(token_id)



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
api_instance = swagger_client.PayInsWebPayApi(swagger_client.ApiClient(configuration))
token_id = 789 # int | 

try:
    api_response = api_instance.pay_ins_web_pay_get_web_pay_tokenization(token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsWebPayApi->pay_ins_web_pay_get_web_pay_tokenization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

[**WebPayTokenizationResponse**](WebPayTokenizationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_web_pay_web_pay_get_payment**
> WebPayPayInsResponse pay_ins_web_pay_web_pay_get_payment(pay_in_id)



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
api_instance = swagger_client.PayInsWebPayApi(swagger_client.ApiClient(configuration))
pay_in_id = 789 # int | 

try:
    api_response = api_instance.pay_ins_web_pay_web_pay_get_payment(pay_in_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsWebPayApi->pay_ins_web_pay_web_pay_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**|  | 

### Return type

[**WebPayPayInsResponse**](WebPayPayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_web_pay_web_pay_post_payment_by_web**
> WebPayPayByWebResponse pay_ins_web_pay_web_pay_post_payment_by_web(web_pay_pay_in=web_pay_pay_in)



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
api_instance = swagger_client.PayInsWebPayApi(swagger_client.ApiClient(configuration))
web_pay_pay_in = swagger_client.WebPayPayByWebPost() # WebPayPayByWebPost |  (optional)

try:
    api_response = api_instance.pay_ins_web_pay_web_pay_post_payment_by_web(web_pay_pay_in=web_pay_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsWebPayApi->pay_ins_web_pay_web_pay_post_payment_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_pay_pay_in** | [**WebPayPayByWebPost**](WebPayPayByWebPost.md)|  | [optional] 

### Return type

[**WebPayPayByWebResponse**](WebPayPayByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_web_pay_web_pay_post_refund**
> WebPayRefundResponse pay_ins_web_pay_web_pay_post_refund(pay_in_id, web_pay_refund=web_pay_refund)



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
api_instance = swagger_client.PayInsWebPayApi(swagger_client.ApiClient(configuration))
pay_in_id = 789 # int | 
web_pay_refund = swagger_client.WebPayRefundPost() # WebPayRefundPost |  (optional)

try:
    api_response = api_instance.pay_ins_web_pay_web_pay_post_refund(pay_in_id, web_pay_refund=web_pay_refund)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsWebPayApi->pay_ins_web_pay_web_pay_post_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**|  | 
 **web_pay_refund** | [**WebPayRefundPost**](WebPayRefundPost.md)|  | [optional] 

### Return type

[**WebPayRefundResponse**](WebPayRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_web_pay_web_pay_save_card**
> WebPayTokenizeByWebResponse pay_ins_web_pay_web_pay_save_card(web_pay_save_card=web_pay_save_card)



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
api_instance = swagger_client.PayInsWebPayApi(swagger_client.ApiClient(configuration))
web_pay_save_card = swagger_client.WebPayTokenRequestPost() # WebPayTokenRequestPost |  (optional)

try:
    api_response = api_instance.pay_ins_web_pay_web_pay_save_card(web_pay_save_card=web_pay_save_card)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsWebPayApi->pay_ins_web_pay_web_pay_save_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_pay_save_card** | [**WebPayTokenRequestPost**](WebPayTokenRequestPost.md)|  | [optional] 

### Return type

[**WebPayTokenizeByWebResponse**](WebPayTokenizeByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


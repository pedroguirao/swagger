# swagger_client.PayInsRedsysApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_ins_redsys_redsys_get_payment**](PayInsRedsysApi.md#pay_ins_redsys_redsys_get_payment) | **GET** /v2.1/PayInsRedsys/payments/{PayInId} | 
[**pay_ins_redsys_redsys_get_preauthorization**](PayInsRedsysApi.md#pay_ins_redsys_redsys_get_preauthorization) | **GET** /v2.1/PayInsRedsys/preauthorizations/{PreauthorizationId} | 
[**pay_ins_redsys_redsys_post_payment_by_web**](PayInsRedsysApi.md#pay_ins_redsys_redsys_post_payment_by_web) | **POST** /v2.1/PayInsRedsys/payments/web | 
[**pay_ins_redsys_redsys_post_preauthorization_by_web**](PayInsRedsysApi.md#pay_ins_redsys_redsys_post_preauthorization_by_web) | **POST** /v2.1/PayInsRedsys/preauthorizations/web | 
[**pay_ins_redsys_redsys_post_preauthorization_cancellation**](PayInsRedsysApi.md#pay_ins_redsys_redsys_post_preauthorization_cancellation) | **POST** /v2.1/PayInsRedsys/preauthorizations/{PreauthorizationId}/cancellation | 
[**pay_ins_redsys_redsys_post_preauthorization_confirmation**](PayInsRedsysApi.md#pay_ins_redsys_redsys_post_preauthorization_confirmation) | **POST** /v2.1/PayInsRedsys/preauthorizations/{PreauthorizationId}/confirmation | 
[**pay_ins_redsys_redsys_post_refund**](PayInsRedsysApi.md#pay_ins_redsys_redsys_post_refund) | **POST** /v2.1/PayInsRedsys/payments/{PayInId}/refunds | 


# **pay_ins_redsys_redsys_get_payment**
> RedsysPayInsResponse pay_ins_redsys_redsys_get_payment(pay_in_id)



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
api_instance = swagger_client.PayInsRedsysApi(swagger_client.ApiClient(configuration))
pay_in_id = 789 # int | 

try:
    api_response = api_instance.pay_ins_redsys_redsys_get_payment(pay_in_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_redsys_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**|  | 

### Return type

[**RedsysPayInsResponse**](RedsysPayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_redsys_get_preauthorization**
> RedsysPreauthorizeResponse pay_ins_redsys_redsys_get_preauthorization(preauthorization_id)



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
api_instance = swagger_client.PayInsRedsysApi(swagger_client.ApiClient(configuration))
preauthorization_id = 789 # int | 

try:
    api_response = api_instance.pay_ins_redsys_redsys_get_preauthorization(preauthorization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_redsys_get_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**|  | 

### Return type

[**RedsysPreauthorizeResponse**](RedsysPreauthorizeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_redsys_post_payment_by_web**
> RedsysPayByWebResponse pay_ins_redsys_redsys_post_payment_by_web(x_webhook=x_webhook, redsys_pay_in=redsys_pay_in)



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
api_instance = swagger_client.PayInsRedsysApi(swagger_client.ApiClient(configuration))
x_webhook = 'x_webhook_example' # str |  (optional)
redsys_pay_in = swagger_client.RedsysPayByWebPost() # RedsysPayByWebPost |  (optional)

try:
    api_response = api_instance.pay_ins_redsys_redsys_post_payment_by_web(x_webhook=x_webhook, redsys_pay_in=redsys_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_redsys_post_payment_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_webhook** | **str**|  | [optional] 
 **redsys_pay_in** | [**RedsysPayByWebPost**](RedsysPayByWebPost.md)|  | [optional] 

### Return type

[**RedsysPayByWebResponse**](RedsysPayByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_redsys_post_preauthorization_by_web**
> RedsysPreauthorizeByWebResponse pay_ins_redsys_redsys_post_preauthorization_by_web(redsys_preauthorization=redsys_preauthorization)



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
api_instance = swagger_client.PayInsRedsysApi(swagger_client.ApiClient(configuration))
redsys_preauthorization = swagger_client.RedsysPreauthorizeByWebPost() # RedsysPreauthorizeByWebPost |  (optional)

try:
    api_response = api_instance.pay_ins_redsys_redsys_post_preauthorization_by_web(redsys_preauthorization=redsys_preauthorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_redsys_post_preauthorization_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redsys_preauthorization** | [**RedsysPreauthorizeByWebPost**](RedsysPreauthorizeByWebPost.md)|  | [optional] 

### Return type

[**RedsysPreauthorizeByWebResponse**](RedsysPreauthorizeByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_redsys_post_preauthorization_cancellation**
> RedsysPreauthorizationCancellationResponse pay_ins_redsys_redsys_post_preauthorization_cancellation(preauthorization_id, redsys_preauthorization_cancellation=redsys_preauthorization_cancellation)



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
api_instance = swagger_client.PayInsRedsysApi(swagger_client.ApiClient(configuration))
preauthorization_id = 789 # int | 
redsys_preauthorization_cancellation = swagger_client.RedsysPreauthorizationCancellationPost() # RedsysPreauthorizationCancellationPost |  (optional)

try:
    api_response = api_instance.pay_ins_redsys_redsys_post_preauthorization_cancellation(preauthorization_id, redsys_preauthorization_cancellation=redsys_preauthorization_cancellation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_redsys_post_preauthorization_cancellation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**|  | 
 **redsys_preauthorization_cancellation** | [**RedsysPreauthorizationCancellationPost**](RedsysPreauthorizationCancellationPost.md)|  | [optional] 

### Return type

[**RedsysPreauthorizationCancellationResponse**](RedsysPreauthorizationCancellationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_redsys_post_preauthorization_confirmation**
> RedsysPreauthorizationConfirmationResponse pay_ins_redsys_redsys_post_preauthorization_confirmation(preauthorization_id, redsys_preauthorization_confirmation=redsys_preauthorization_confirmation)



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
api_instance = swagger_client.PayInsRedsysApi(swagger_client.ApiClient(configuration))
preauthorization_id = 789 # int | 
redsys_preauthorization_confirmation = swagger_client.RedsysPreauthorizationConfirmationPost() # RedsysPreauthorizationConfirmationPost |  (optional)

try:
    api_response = api_instance.pay_ins_redsys_redsys_post_preauthorization_confirmation(preauthorization_id, redsys_preauthorization_confirmation=redsys_preauthorization_confirmation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_redsys_post_preauthorization_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**|  | 
 **redsys_preauthorization_confirmation** | [**RedsysPreauthorizationConfirmationPost**](RedsysPreauthorizationConfirmationPost.md)|  | [optional] 

### Return type

[**RedsysPreauthorizationConfirmationResponse**](RedsysPreauthorizationConfirmationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_redsys_post_refund**
> RedsysRefundResponse pay_ins_redsys_redsys_post_refund(pay_in_id, redsys_refund=redsys_refund)



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
api_instance = swagger_client.PayInsRedsysApi(swagger_client.ApiClient(configuration))
pay_in_id = 789 # int | 
redsys_refund = swagger_client.RedsysRefundPost() # RedsysRefundPost |  (optional)

try:
    api_response = api_instance.pay_ins_redsys_redsys_post_refund(pay_in_id, redsys_refund=redsys_refund)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_redsys_post_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**|  | 
 **redsys_refund** | [**RedsysRefundPost**](RedsysRefundPost.md)|  | [optional] 

### Return type

[**RedsysRefundResponse**](RedsysRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


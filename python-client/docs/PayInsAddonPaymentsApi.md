# swagger_client.PayInsAddonPaymentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_ins_addon_payments_addon_payments_get_payment**](PayInsAddonPaymentsApi.md#pay_ins_addon_payments_addon_payments_get_payment) | **GET** /v2.1/PayInsAddonPayments/payments/{PayInId} | 
[**pay_ins_addon_payments_addon_payments_get_preauthorization**](PayInsAddonPaymentsApi.md#pay_ins_addon_payments_addon_payments_get_preauthorization) | **GET** /v2.1/PayInsAddonPayments/preauthorizations/{PreauthorizationId} | 
[**pay_ins_addon_payments_addon_payments_post_payment_by_web**](PayInsAddonPaymentsApi.md#pay_ins_addon_payments_addon_payments_post_payment_by_web) | **POST** /v2.1/PayInsAddonPayments/payments/web | 
[**pay_ins_addon_payments_addon_payments_post_payment_direct**](PayInsAddonPaymentsApi.md#pay_ins_addon_payments_addon_payments_post_payment_direct) | **POST** /v2.1/PayInsAddonPayments/payments/direct | 
[**pay_ins_addon_payments_addon_payments_post_preauthorization_by_web**](PayInsAddonPaymentsApi.md#pay_ins_addon_payments_addon_payments_post_preauthorization_by_web) | **POST** /v2.1/PayInsAddonPayments/preauthorizations/web | 
[**pay_ins_addon_payments_addon_payments_post_preauthorization_cancellation**](PayInsAddonPaymentsApi.md#pay_ins_addon_payments_addon_payments_post_preauthorization_cancellation) | **POST** /v2.1/PayInsAddonPayments/preauthorizations/{PreauthorizationId}/cancellation | 
[**pay_ins_addon_payments_addon_payments_post_preauthorization_confirmation**](PayInsAddonPaymentsApi.md#pay_ins_addon_payments_addon_payments_post_preauthorization_confirmation) | **POST** /v2.1/PayInsAddonPayments/preauthorizations/{PreauthorizationId}/confirmation | 
[**pay_ins_addon_payments_addon_payments_post_refund**](PayInsAddonPaymentsApi.md#pay_ins_addon_payments_addon_payments_post_refund) | **POST** /v2.1/PayInsAddonPayments/payments/{PayInId}/refunds | 


# **pay_ins_addon_payments_addon_payments_get_payment**
> AddonPaymentsPayInsResponse pay_ins_addon_payments_addon_payments_get_payment(pay_in_id)



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
api_instance = swagger_client.PayInsAddonPaymentsApi(swagger_client.ApiClient(configuration))
pay_in_id = 789 # int | 

try:
    api_response = api_instance.pay_ins_addon_payments_addon_payments_get_payment(pay_in_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAddonPaymentsApi->pay_ins_addon_payments_addon_payments_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**|  | 

### Return type

[**AddonPaymentsPayInsResponse**](AddonPaymentsPayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_addon_payments_addon_payments_get_preauthorization**
> AddonPaymentsPreauthorizeResponse pay_ins_addon_payments_addon_payments_get_preauthorization(preauthorization_id)



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
api_instance = swagger_client.PayInsAddonPaymentsApi(swagger_client.ApiClient(configuration))
preauthorization_id = 789 # int | 

try:
    api_response = api_instance.pay_ins_addon_payments_addon_payments_get_preauthorization(preauthorization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAddonPaymentsApi->pay_ins_addon_payments_addon_payments_get_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**|  | 

### Return type

[**AddonPaymentsPreauthorizeResponse**](AddonPaymentsPreauthorizeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_addon_payments_addon_payments_post_payment_by_web**
> AddonPaymentsPayByWebResponse pay_ins_addon_payments_addon_payments_post_payment_by_web(x_webhook=x_webhook, addon_payments_pay_in=addon_payments_pay_in)



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
api_instance = swagger_client.PayInsAddonPaymentsApi(swagger_client.ApiClient(configuration))
x_webhook = 'x_webhook_example' # str |  (optional)
addon_payments_pay_in = swagger_client.AddonPaymentsPayByWebPost() # AddonPaymentsPayByWebPost |  (optional)

try:
    api_response = api_instance.pay_ins_addon_payments_addon_payments_post_payment_by_web(x_webhook=x_webhook, addon_payments_pay_in=addon_payments_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAddonPaymentsApi->pay_ins_addon_payments_addon_payments_post_payment_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_webhook** | **str**|  | [optional] 
 **addon_payments_pay_in** | [**AddonPaymentsPayByWebPost**](AddonPaymentsPayByWebPost.md)|  | [optional] 

### Return type

[**AddonPaymentsPayByWebResponse**](AddonPaymentsPayByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_addon_payments_addon_payments_post_payment_direct**
> AddonPaymentsPayDirectResponse pay_ins_addon_payments_addon_payments_post_payment_direct(addon_payments_pay_in=addon_payments_pay_in)



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
api_instance = swagger_client.PayInsAddonPaymentsApi(swagger_client.ApiClient(configuration))
addon_payments_pay_in = swagger_client.AddonPaymentsPayDirectPost() # AddonPaymentsPayDirectPost |  (optional)

try:
    api_response = api_instance.pay_ins_addon_payments_addon_payments_post_payment_direct(addon_payments_pay_in=addon_payments_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAddonPaymentsApi->pay_ins_addon_payments_addon_payments_post_payment_direct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_payments_pay_in** | [**AddonPaymentsPayDirectPost**](AddonPaymentsPayDirectPost.md)|  | [optional] 

### Return type

[**AddonPaymentsPayDirectResponse**](AddonPaymentsPayDirectResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_addon_payments_addon_payments_post_preauthorization_by_web**
> AddonPaymentsPreauthorizeByWebResponse pay_ins_addon_payments_addon_payments_post_preauthorization_by_web(addon_payments_preauthorization=addon_payments_preauthorization)



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
api_instance = swagger_client.PayInsAddonPaymentsApi(swagger_client.ApiClient(configuration))
addon_payments_preauthorization = swagger_client.AddonPaymentsPreauthorizeByWebPost() # AddonPaymentsPreauthorizeByWebPost |  (optional)

try:
    api_response = api_instance.pay_ins_addon_payments_addon_payments_post_preauthorization_by_web(addon_payments_preauthorization=addon_payments_preauthorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAddonPaymentsApi->pay_ins_addon_payments_addon_payments_post_preauthorization_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_payments_preauthorization** | [**AddonPaymentsPreauthorizeByWebPost**](AddonPaymentsPreauthorizeByWebPost.md)|  | [optional] 

### Return type

[**AddonPaymentsPreauthorizeByWebResponse**](AddonPaymentsPreauthorizeByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_addon_payments_addon_payments_post_preauthorization_cancellation**
> AddonPaymentsPreauthorizationCancellationResponse pay_ins_addon_payments_addon_payments_post_preauthorization_cancellation(preauthorization_id, addon_payments_preauthorization_cancellation=addon_payments_preauthorization_cancellation)



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
api_instance = swagger_client.PayInsAddonPaymentsApi(swagger_client.ApiClient(configuration))
preauthorization_id = 789 # int | 
addon_payments_preauthorization_cancellation = swagger_client.AddonPaymentsPreauthorizationCancellationPost() # AddonPaymentsPreauthorizationCancellationPost |  (optional)

try:
    api_response = api_instance.pay_ins_addon_payments_addon_payments_post_preauthorization_cancellation(preauthorization_id, addon_payments_preauthorization_cancellation=addon_payments_preauthorization_cancellation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAddonPaymentsApi->pay_ins_addon_payments_addon_payments_post_preauthorization_cancellation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**|  | 
 **addon_payments_preauthorization_cancellation** | [**AddonPaymentsPreauthorizationCancellationPost**](AddonPaymentsPreauthorizationCancellationPost.md)|  | [optional] 

### Return type

[**AddonPaymentsPreauthorizationCancellationResponse**](AddonPaymentsPreauthorizationCancellationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_addon_payments_addon_payments_post_preauthorization_confirmation**
> AddonPaymentsPreauthorizationConfirmationResponse pay_ins_addon_payments_addon_payments_post_preauthorization_confirmation(preauthorization_id, addon_payments_preauthorization_confirmation=addon_payments_preauthorization_confirmation)



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
api_instance = swagger_client.PayInsAddonPaymentsApi(swagger_client.ApiClient(configuration))
preauthorization_id = 789 # int | 
addon_payments_preauthorization_confirmation = swagger_client.AddonPaymentsPreauthorizationConfirmationPost() # AddonPaymentsPreauthorizationConfirmationPost |  (optional)

try:
    api_response = api_instance.pay_ins_addon_payments_addon_payments_post_preauthorization_confirmation(preauthorization_id, addon_payments_preauthorization_confirmation=addon_payments_preauthorization_confirmation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAddonPaymentsApi->pay_ins_addon_payments_addon_payments_post_preauthorization_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**|  | 
 **addon_payments_preauthorization_confirmation** | [**AddonPaymentsPreauthorizationConfirmationPost**](AddonPaymentsPreauthorizationConfirmationPost.md)|  | [optional] 

### Return type

[**AddonPaymentsPreauthorizationConfirmationResponse**](AddonPaymentsPreauthorizationConfirmationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_addon_payments_addon_payments_post_refund**
> AddonPaymentsRefundResponse pay_ins_addon_payments_addon_payments_post_refund(pay_in_id, addon_payments_refund=addon_payments_refund)



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
api_instance = swagger_client.PayInsAddonPaymentsApi(swagger_client.ApiClient(configuration))
pay_in_id = 789 # int | 
addon_payments_refund = swagger_client.AddonPaymentsRefundPost() # AddonPaymentsRefundPost |  (optional)

try:
    api_response = api_instance.pay_ins_addon_payments_addon_payments_post_refund(pay_in_id, addon_payments_refund=addon_payments_refund)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsAddonPaymentsApi->pay_ins_addon_payments_addon_payments_post_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**|  | 
 **addon_payments_refund** | [**AddonPaymentsRefundPost**](AddonPaymentsRefundPost.md)|  | [optional] 

### Return type

[**AddonPaymentsRefundResponse**](AddonPaymentsRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


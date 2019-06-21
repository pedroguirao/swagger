# swagger_client.PluginTransferClientApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plugin_transfer_client_plugin_client_confirm_pay_in**](PluginTransferClientApi.md#plugin_transfer_client_plugin_client_confirm_pay_in) | **POST** /v2.1/PayInsClient/payments/{IntentId}/confirm | 
[**plugin_transfer_client_plugin_client_get_payment**](PluginTransferClientApi.md#plugin_transfer_client_plugin_client_get_payment) | **GET** /v2.1/PayInsClient/payments/{PayInId} | 
[**plugin_transfer_client_plugin_client_pay_in_create_post**](PluginTransferClientApi.md#plugin_transfer_client_plugin_client_pay_in_create_post) | **POST** /v2.1/PayInsClient/payments | 


# **plugin_transfer_client_plugin_client_confirm_pay_in**
> PluginPayInsResponse plugin_transfer_client_plugin_client_confirm_pay_in(intent_id)



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
api_instance = swagger_client.PluginTransferClientApi(swagger_client.ApiClient(configuration))
intent_id = 789 # int | 

try:
    api_response = api_instance.plugin_transfer_client_plugin_client_confirm_pay_in(intent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginTransferClientApi->plugin_transfer_client_plugin_client_confirm_pay_in: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intent_id** | **int**|  | 

### Return type

[**PluginPayInsResponse**](PluginPayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugin_transfer_client_plugin_client_get_payment**
> PluginPayInsResponse plugin_transfer_client_plugin_client_get_payment(pay_in_id)



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
api_instance = swagger_client.PluginTransferClientApi(swagger_client.ApiClient(configuration))
pay_in_id = 789 # int | 

try:
    api_response = api_instance.plugin_transfer_client_plugin_client_get_payment(pay_in_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginTransferClientApi->plugin_transfer_client_plugin_client_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**|  | 

### Return type

[**PluginPayInsResponse**](PluginPayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugin_transfer_client_plugin_client_pay_in_create_post**
> PluginPayInsResponse plugin_transfer_client_plugin_client_pay_in_create_post(plugin_pay_in=plugin_pay_in)



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
api_instance = swagger_client.PluginTransferClientApi(swagger_client.ApiClient(configuration))
plugin_pay_in = swagger_client.PluginPayInPost() # PluginPayInPost |  (optional)

try:
    api_response = api_instance.plugin_transfer_client_plugin_client_pay_in_create_post(plugin_pay_in=plugin_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginTransferClientApi->plugin_transfer_client_plugin_client_pay_in_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_pay_in** | [**PluginPayInPost**](PluginPayInPost.md)|  | [optional] 

### Return type

[**PluginPayInsResponse**](PluginPayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


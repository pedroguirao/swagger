# swagger_client.PluginTransferPayOutClientApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plugin_transfer_pay_out_client_plugin_pay_out_post**](PluginTransferPayOutClientApi.md#plugin_transfer_pay_out_client_plugin_pay_out_post) | **POST** /v2.1/PayOutsPlugin | 
[**plugin_transfer_pay_out_client_pluging_get_pay_out**](PluginTransferPayOutClientApi.md#plugin_transfer_pay_out_client_pluging_get_pay_out) | **GET** /v2.1/PayOutsPlugin/{PayOutId} | 


# **plugin_transfer_pay_out_client_plugin_pay_out_post**
> PluginPayOutResponse plugin_transfer_pay_out_client_plugin_pay_out_post(plugin_pay_out=plugin_pay_out)



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
api_instance = swagger_client.PluginTransferPayOutClientApi(swagger_client.ApiClient(configuration))
plugin_pay_out = swagger_client.PluginPayOutPost() # PluginPayOutPost |  (optional)

try:
    api_response = api_instance.plugin_transfer_pay_out_client_plugin_pay_out_post(plugin_pay_out=plugin_pay_out)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginTransferPayOutClientApi->plugin_transfer_pay_out_client_plugin_pay_out_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_pay_out** | [**PluginPayOutPost**](PluginPayOutPost.md)|  | [optional] 

### Return type

[**PluginPayOutResponse**](PluginPayOutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plugin_transfer_pay_out_client_pluging_get_pay_out**
> PluginPayOutResponse plugin_transfer_pay_out_client_pluging_get_pay_out(pay_out_id)



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
api_instance = swagger_client.PluginTransferPayOutClientApi(swagger_client.ApiClient(configuration))
pay_out_id = 789 # int | 

try:
    api_response = api_instance.plugin_transfer_pay_out_client_pluging_get_pay_out(pay_out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginTransferPayOutClientApi->plugin_transfer_pay_out_client_pluging_get_pay_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_out_id** | **int**|  | 

### Return type

[**PluginPayOutResponse**](PluginPayOutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


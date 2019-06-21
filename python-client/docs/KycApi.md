# swagger_client.KycApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kyc_delete_legal_board_member**](KycApi.md#kyc_delete_legal_board_member) | **DELETE** /v2.1/Kyc/users/legal/{UserId}/boardmembers/{BoardMemberId} | 
[**kyc_delete_legal_share_holder_natural**](KycApi.md#kyc_delete_legal_share_holder_natural) | **DELETE** /v2.1/Kyc/users/legal/{UserId}/shareholders/natural/{ShareHolderId} | 
[**kyc_get_file**](KycApi.md#kyc_get_file) | **GET** /v2.1/Kyc/document/{DocumentId} | 
[**kyc_get_legal**](KycApi.md#kyc_get_legal) | **GET** /v2.1/Kyc/users/legal/{UserId} | View a Legal User
[**kyc_get_legal_board_member**](KycApi.md#kyc_get_legal_board_member) | **GET** /v2.1/Kyc/users/legal/{UserId}/boardmembers/{BoardMemberId} | 
[**kyc_get_legal_board_members**](KycApi.md#kyc_get_legal_board_members) | **GET** /v2.1/Kyc/users/legal/{UserId}/boardmembers | 
[**kyc_get_legal_list**](KycApi.md#kyc_get_legal_list) | **GET** /v2.1/Kyc/users/legal | List all Legal User
[**kyc_get_legal_share_holder_natural**](KycApi.md#kyc_get_legal_share_holder_natural) | **GET** /v2.1/Kyc/users/legal/{UserId}/shareholders/natural/{ShareHolderId} | 
[**kyc_get_legal_share_holders**](KycApi.md#kyc_get_legal_share_holders) | **GET** /v2.1/Kyc/users/legal/{UserId}/shareholders/natural | 
[**kyc_get_natura_list**](KycApi.md#kyc_get_natura_list) | **GET** /v2.1/Kyc/users/natural | List all Natural User
[**kyc_get_natural**](KycApi.md#kyc_get_natural) | **GET** /v2.1/Kyc/users/natural/{UserId} | View a Natural User
[**kyc_get_validation**](KycApi.md#kyc_get_validation) | **GET** /v2.1/Kyc/users/natural/{UserId}/validation | 
[**kyc_get_validation_legal**](KycApi.md#kyc_get_validation_legal) | **GET** /v2.1/Kyc/users/legal/{UserId}/validation | 
[**kyc_post_document**](KycApi.md#kyc_post_document) | **POST** /v2.1/Kyc/users/{UserId}/documents/new/{DocumentType} | Uploads a new document and uploads a file. If the document already exists it will be replaced.
[**kyc_post_document_board_member**](KycApi.md#kyc_post_document_board_member) | **POST** /v2.1/Kyc/users/legal/{UserId}/boardmember/{BoardMemberId}/documents/new/{DocumentType} | Uploads a new document. If the document already exists it will be replaced.
[**kyc_post_document_shareholder**](KycApi.md#kyc_post_document_shareholder) | **POST** /v2.1/Kyc/users/legal/{UserId}/shareholder/{ShareholderId}/documents/new/{DocumentType} | Uploads a new document and uploads a file. If the document already exists it will be replaced.
[**kyc_post_legal**](KycApi.md#kyc_post_legal) | **POST** /v2.1/Kyc/users/legal/{UserId} | Update a Legal User Kyc Data
[**kyc_post_legal_board_member**](KycApi.md#kyc_post_legal_board_member) | **POST** /v2.1/Kyc/users/legal/{UserId}/boardmembers | 
[**kyc_post_legal_share_holder**](KycApi.md#kyc_post_legal_share_holder) | **POST** /v2.1/Kyc/users/legal/{UserId}/shareholders/natural | 
[**kyc_post_natural**](KycApi.md#kyc_post_natural) | **POST** /v2.1/Kyc/users/natural/{UserId} | Update a Natural User Kyc Data
[**kyc_put_document**](KycApi.md#kyc_put_document) | **PUT** /v2.1/Kyc/users/{UserId}/documents/add/{DocumentType} | Adds files to a document.
[**kyc_put_document_board_member**](KycApi.md#kyc_put_document_board_member) | **PUT** /v2.1/Kyc/users/legal/{UserId}/boardmember/{BoardMemberId}/documents/add/{DocumentType} | Uploads a new document. If the document already exists it will be replaced.
[**kyc_put_document_shareholder**](KycApi.md#kyc_put_document_shareholder) | **PUT** /v2.1/Kyc/users/legal/{UserId}/shareholder/{ShareholderId}/documents/add/{DocumentType} | Adds files to a document.
[**kyc_put_legal**](KycApi.md#kyc_put_legal) | **PUT** /v2.1/Kyc/users/legal/{UserId} | Update a Legal User
[**kyc_put_legal_board_member**](KycApi.md#kyc_put_legal_board_member) | **PUT** /v2.1/Kyc/users/legal/{UserId}/boardmembers/{BoardMemberId} | 
[**kyc_put_legal_share_holder**](KycApi.md#kyc_put_legal_share_holder) | **PUT** /v2.1/Kyc/users/legal/{UserId}/shareholders/natural/{ShareHolderId} | 
[**kyc_put_request**](KycApi.md#kyc_put_request) | **PUT** /v2.1/Kyc/users/natural/{UserId}/requestValidation | 
[**kyc_put_request_legal**](KycApi.md#kyc_put_request_legal) | **PUT** /v2.1/Kyc/users/legal/{UserId}/requestValidation | 


# **kyc_delete_legal_board_member**
> str kyc_delete_legal_board_member(board_member_id, user_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
board_member_id = 789 # int | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.kyc_delete_legal_board_member(board_member_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_delete_legal_board_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_member_id** | **int**|  | 
 **user_id** | **str**|  | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_delete_legal_share_holder_natural**
> str kyc_delete_legal_share_holder_natural(user_id, share_holder_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 
share_holder_id = 789 # int | 

try:
    api_response = api_instance.kyc_delete_legal_share_holder_natural(user_id, share_holder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_delete_legal_share_holder_natural: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **share_holder_id** | **int**|  | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_file**
> file kyc_get_file(document_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
document_id = 789 # int | 

try:
    api_response = api_instance.kyc_get_file(document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**|  | 

### Return type

[**file**](file.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_legal**
> KycUserValidationLevelLegalResponse kyc_get_legal(user_id)

View a Legal User



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | The Id of a legal user

try:
    # View a Legal User
    api_response = api_instance.kyc_get_legal(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_legal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a legal user | 

### Return type

[**KycUserValidationLevelLegalResponse**](KycUserValidationLevelLegalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_legal_board_member**
> KycUserValidationBoardMemberListItemResponse kyc_get_legal_board_member(board_member_id, user_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
board_member_id = 789 # int | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.kyc_get_legal_board_member(board_member_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_legal_board_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_member_id** | **int**|  | 
 **user_id** | **str**|  | 

### Return type

[**KycUserValidationBoardMemberListItemResponse**](KycUserValidationBoardMemberListItemResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_legal_board_members**
> KycUserValidationLevelLegalBoardMembersListResponse kyc_get_legal_board_members(user_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 

try:
    api_response = api_instance.kyc_get_legal_board_members(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_legal_board_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**KycUserValidationLevelLegalBoardMembersListResponse**](KycUserValidationLevelLegalBoardMembersListResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_legal_list**
> ResponseListKycUserValidationLevelLegalResponse kyc_get_legal_list(page=page, per_page=per_page, name_contains=name_contains, fiscal_id_contains=fiscal_id_contains)

List all Legal User



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
page = 56 # int | The page number of results you wish to return (optional)
per_page = 56 # int | The number of results to return per page (optional)
name_contains = 'name_contains_example' # str |  (optional)
fiscal_id_contains = 'fiscal_id_contains_example' # str |  (optional)

try:
    # List all Legal User
    api_response = api_instance.kyc_get_legal_list(page=page, per_page=per_page, name_contains=name_contains, fiscal_id_contains=fiscal_id_contains)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_legal_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number of results you wish to return | [optional] 
 **per_page** | **int**| The number of results to return per page | [optional] 
 **name_contains** | **str**|  | [optional] 
 **fiscal_id_contains** | **str**|  | [optional] 

### Return type

[**ResponseListKycUserValidationLevelLegalResponse**](ResponseListKycUserValidationLevelLegalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_legal_share_holder_natural**
> KycUserValidationShareHolderListItemResponseNatural kyc_get_legal_share_holder_natural(user_id, share_holder_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 
share_holder_id = 789 # int | 

try:
    api_response = api_instance.kyc_get_legal_share_holder_natural(user_id, share_holder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_legal_share_holder_natural: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **share_holder_id** | **int**|  | 

### Return type

[**KycUserValidationShareHolderListItemResponseNatural**](KycUserValidationShareHolderListItemResponseNatural.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_legal_share_holders**
> KycUserValidationLevelLegalShareHoldersListResponse kyc_get_legal_share_holders(user_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 

try:
    api_response = api_instance.kyc_get_legal_share_holders(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_legal_share_holders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**KycUserValidationLevelLegalShareHoldersListResponse**](KycUserValidationLevelLegalShareHoldersListResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_natura_list**
> ResponseListKycUserValidationLevelNaturalResponse kyc_get_natura_list(page=page, per_page=per_page, first_name_contains=first_name_contains, last_name_contains=last_name_contains, id_card_contains=id_card_contains)

List all Natural User



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
page = 56 # int | The page number of results you wish to return (optional)
per_page = 56 # int | The number of results to return per page (optional)
first_name_contains = 'first_name_contains_example' # str |  (optional)
last_name_contains = 'last_name_contains_example' # str |  (optional)
id_card_contains = 'id_card_contains_example' # str |  (optional)

try:
    # List all Natural User
    api_response = api_instance.kyc_get_natura_list(page=page, per_page=per_page, first_name_contains=first_name_contains, last_name_contains=last_name_contains, id_card_contains=id_card_contains)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_natura_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number of results you wish to return | [optional] 
 **per_page** | **int**| The number of results to return per page | [optional] 
 **first_name_contains** | **str**|  | [optional] 
 **last_name_contains** | **str**|  | [optional] 
 **id_card_contains** | **str**|  | [optional] 

### Return type

[**ResponseListKycUserValidationLevelNaturalResponse**](ResponseListKycUserValidationLevelNaturalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_natural**
> KycUserValidationLevelNaturalResponse kyc_get_natural(user_id)

View a Natural User



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | The Id of a natural user

try:
    # View a Natural User
    api_response = api_instance.kyc_get_natural(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_natural: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a natural user | 

### Return type

[**KycUserValidationLevelNaturalResponse**](KycUserValidationLevelNaturalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_validation**
> KycValidationUserStatusResponse kyc_get_validation(user_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 

try:
    api_response = api_instance.kyc_get_validation(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**KycValidationUserStatusResponse**](KycValidationUserStatusResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_get_validation_legal**
> KycValidationUserLegalStatusResponse kyc_get_validation_legal(user_id)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 

try:
    api_response = api_instance.kyc_get_validation_legal(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_get_validation_legal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**KycValidationUserLegalStatusResponse**](KycValidationUserLegalStatusResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_post_document**
> KycFileUploadResponse kyc_post_document(document_type, file, user_id, file_content_type=file_content_type)

Uploads a new document and uploads a file. If the document already exists it will be replaced.

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
document_type = 'document_type_example' # str | 
file = '/path/to/file.txt' # file | 
user_id = 789 # int | 
file_content_type = 'file_content_type_example' # str | Mime type of the uploaded file. This parameter overrides the type associated to the file. (optional)

try:
    # Uploads a new document and uploads a file. If the document already exists it will be replaced.
    api_response = api_instance.kyc_post_document(document_type, file, user_id, file_content_type=file_content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_post_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type** | **str**|  | 
 **file** | **file**|  | 
 **user_id** | **int**|  | 
 **file_content_type** | **str**| Mime type of the uploaded file. This parameter overrides the type associated to the file. | [optional] 

### Return type

[**KycFileUploadResponse**](KycFileUploadResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_post_document_board_member**
> KycFileUploadResponse kyc_post_document_board_member(board_member_id, document_type, file, user_id, file_content_type=file_content_type)

Uploads a new document. If the document already exists it will be replaced.

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
board_member_id = 789 # int | 
document_type = 'document_type_example' # str | 
file = '/path/to/file.txt' # file | 
user_id = 789 # int | 
file_content_type = 'file_content_type_example' # str |  (optional)

try:
    # Uploads a new document. If the document already exists it will be replaced.
    api_response = api_instance.kyc_post_document_board_member(board_member_id, document_type, file, user_id, file_content_type=file_content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_post_document_board_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_member_id** | **int**|  | 
 **document_type** | **str**|  | 
 **file** | **file**|  | 
 **user_id** | **int**|  | 
 **file_content_type** | **str**|  | [optional] 

### Return type

[**KycFileUploadResponse**](KycFileUploadResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_post_document_shareholder**
> KycFileUploadResponse kyc_post_document_shareholder(document_type, file, shareholder_id, user_id, file_content_type=file_content_type)

Uploads a new document and uploads a file. If the document already exists it will be replaced.

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
document_type = 'document_type_example' # str | 
file = '/path/to/file.txt' # file | 
shareholder_id = 789 # int | 
user_id = 789 # int | 
file_content_type = 'file_content_type_example' # str | Mime type of the uploaded file. This parameter overrides the type associated to the file. (optional)

try:
    # Uploads a new document and uploads a file. If the document already exists it will be replaced.
    api_response = api_instance.kyc_post_document_shareholder(document_type, file, shareholder_id, user_id, file_content_type=file_content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_post_document_shareholder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type** | **str**|  | 
 **file** | **file**|  | 
 **shareholder_id** | **int**|  | 
 **user_id** | **int**|  | 
 **file_content_type** | **str**| Mime type of the uploaded file. This parameter overrides the type associated to the file. | [optional] 

### Return type

[**KycFileUploadResponse**](KycFileUploadResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_post_legal**
> KycUserValidationLevelLegalResponse kyc_post_legal(user_id, kyc_user_legal=kyc_user_legal)

Update a Legal User Kyc Data

Note that the Birthday field is a timestamp, but be careful to ensure that the time is midnight UTC (otherwise a local time can be understood as 23h UTC, and therefore rendering the wrong date which will present problems when needing to validate the KYC identity)

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | The Id of a user
kyc_user_legal = swagger_client.KycUserLegalPut() # KycUserLegalPut | UserLegal Kyc detail params (optional)

try:
    # Update a Legal User Kyc Data
    api_response = api_instance.kyc_post_legal(user_id, kyc_user_legal=kyc_user_legal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_post_legal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **kyc_user_legal** | [**KycUserLegalPut**](KycUserLegalPut.md)| UserLegal Kyc detail params | [optional] 

### Return type

[**KycUserValidationLevelLegalResponse**](KycUserValidationLevelLegalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_post_legal_board_member**
> KycBoardMemberResponse kyc_post_legal_board_member(user_id, board_member=board_member)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 
board_member = swagger_client.KycUserValidationBoardMemberPost() # KycUserValidationBoardMemberPost |  (optional)

try:
    api_response = api_instance.kyc_post_legal_board_member(user_id, board_member=board_member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_post_legal_board_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **board_member** | [**KycUserValidationBoardMemberPost**](KycUserValidationBoardMemberPost.md)|  | [optional] 

### Return type

[**KycBoardMemberResponse**](KycBoardMemberResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_post_legal_share_holder**
> KycShareHolderResponse kyc_post_legal_share_holder(user_id, share_holder_natural=share_holder_natural)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 
share_holder_natural = swagger_client.KycUserValidationShareHolderNaturalPost() # KycUserValidationShareHolderNaturalPost |  (optional)

try:
    api_response = api_instance.kyc_post_legal_share_holder(user_id, share_holder_natural=share_holder_natural)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_post_legal_share_holder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **share_holder_natural** | [**KycUserValidationShareHolderNaturalPost**](KycUserValidationShareHolderNaturalPost.md)|  | [optional] 

### Return type

[**KycShareHolderResponse**](KycShareHolderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_post_natural**
> KycUserValidationLevelNaturalResponse kyc_post_natural(user_id, kyc_user_natural=kyc_user_natural)

Update a Natural User Kyc Data

Note that the Birthday field is a timestamp, but be careful to ensure that the time is midnight UTC (otherwise a local time can be understood as 23h UTC, and therefore rendering the wrong date which will present problems when needing to validate the KYC identity)

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | The Id of a user
kyc_user_natural = swagger_client.KycUserNaturalPut() # KycUserNaturalPut | UserNatural Kyc detail params (optional)

try:
    # Update a Natural User Kyc Data
    api_response = api_instance.kyc_post_natural(user_id, kyc_user_natural=kyc_user_natural)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_post_natural: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **kyc_user_natural** | [**KycUserNaturalPut**](KycUserNaturalPut.md)| UserNatural Kyc detail params | [optional] 

### Return type

[**KycUserValidationLevelNaturalResponse**](KycUserValidationLevelNaturalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_put_document**
> KycFileUploadResponse kyc_put_document(document_type, file, user_id, file_content_type=file_content_type)

Adds files to a document.

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
document_type = 'document_type_example' # str | 
file = '/path/to/file.txt' # file | 
user_id = 789 # int | 
file_content_type = 'file_content_type_example' # str | Mime type of the uploaded file. This parameter overrides the type associated to the file. (optional)

try:
    # Adds files to a document.
    api_response = api_instance.kyc_put_document(document_type, file, user_id, file_content_type=file_content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_put_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type** | **str**|  | 
 **file** | **file**|  | 
 **user_id** | **int**|  | 
 **file_content_type** | **str**| Mime type of the uploaded file. This parameter overrides the type associated to the file. | [optional] 

### Return type

[**KycFileUploadResponse**](KycFileUploadResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_put_document_board_member**
> KycFileUploadResponse kyc_put_document_board_member(board_member_id, document_type, file, user_id, file_content_type=file_content_type)

Uploads a new document. If the document already exists it will be replaced.

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
board_member_id = 789 # int | 
document_type = 'document_type_example' # str | 
file = '/path/to/file.txt' # file | 
user_id = 789 # int | 
file_content_type = 'file_content_type_example' # str |  (optional)

try:
    # Uploads a new document. If the document already exists it will be replaced.
    api_response = api_instance.kyc_put_document_board_member(board_member_id, document_type, file, user_id, file_content_type=file_content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_put_document_board_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_member_id** | **int**|  | 
 **document_type** | **str**|  | 
 **file** | **file**|  | 
 **user_id** | **int**|  | 
 **file_content_type** | **str**|  | [optional] 

### Return type

[**KycFileUploadResponse**](KycFileUploadResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_put_document_shareholder**
> KycFileUploadResponse kyc_put_document_shareholder(document_type, file, share_holder_id, user_id, file_content_type=file_content_type)

Adds files to a document.

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
document_type = 'document_type_example' # str | 
file = '/path/to/file.txt' # file | 
share_holder_id = 789 # int | 
user_id = 789 # int | 
file_content_type = 'file_content_type_example' # str | Mime type of the uploaded file. This parameter overrides the type associated to the file. (optional)

try:
    # Adds files to a document.
    api_response = api_instance.kyc_put_document_shareholder(document_type, file, share_holder_id, user_id, file_content_type=file_content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_put_document_shareholder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type** | **str**|  | 
 **file** | **file**|  | 
 **share_holder_id** | **int**|  | 
 **user_id** | **int**|  | 
 **file_content_type** | **str**| Mime type of the uploaded file. This parameter overrides the type associated to the file. | [optional] 

### Return type

[**KycFileUploadResponse**](KycFileUploadResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_put_legal**
> KycUserValidationLevelLegalResponse kyc_put_legal(user_id, user_legal=user_legal)

Update a Legal User

Note that the LegalRepresentativeBirthday field is a timestamp, but be careful to ensure that the time is midnight UTC (otherwise a local time can be understood as 23h UTC, and therefore rendering the wrong date which will present problems when needing to validate the KYC identity)

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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | The Id of a user
user_legal = swagger_client.KycUserLegalPut() # KycUserLegalPut | UserLegal Object params (optional)

try:
    # Update a Legal User
    api_response = api_instance.kyc_put_legal(user_id, user_legal=user_legal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_put_legal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **user_legal** | [**KycUserLegalPut**](KycUserLegalPut.md)| UserLegal Object params | [optional] 

### Return type

[**KycUserValidationLevelLegalResponse**](KycUserValidationLevelLegalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_put_legal_board_member**
> KycBoardMemberResponse kyc_put_legal_board_member(board_member_id, user_id, board_member=board_member)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
board_member_id = 789 # int | 
user_id = 'user_id_example' # str | 
board_member = swagger_client.KycUserValidationBoardMemberPut() # KycUserValidationBoardMemberPut |  (optional)

try:
    api_response = api_instance.kyc_put_legal_board_member(board_member_id, user_id, board_member=board_member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_put_legal_board_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_member_id** | **int**|  | 
 **user_id** | **str**|  | 
 **board_member** | [**KycUserValidationBoardMemberPut**](KycUserValidationBoardMemberPut.md)|  | [optional] 

### Return type

[**KycBoardMemberResponse**](KycBoardMemberResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_put_legal_share_holder**
> KycUserValidationShareHolderListItemResponseNatural kyc_put_legal_share_holder(user_id, share_holder_id, share_holder_natural=share_holder_natural)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 
share_holder_id = 789 # int | 
share_holder_natural = swagger_client.KycUserValidationShareHolderNaturalPut() # KycUserValidationShareHolderNaturalPut |  (optional)

try:
    api_response = api_instance.kyc_put_legal_share_holder(user_id, share_holder_id, share_holder_natural=share_holder_natural)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_put_legal_share_holder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **share_holder_id** | **int**|  | 
 **share_holder_natural** | [**KycUserValidationShareHolderNaturalPut**](KycUserValidationShareHolderNaturalPut.md)|  | [optional] 

### Return type

[**KycUserValidationShareHolderListItemResponseNatural**](KycUserValidationShareHolderListItemResponseNatural.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_put_request**
> KycValidationRequestResponse kyc_put_request(user_id, validation_request=validation_request)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 
validation_request = swagger_client.KycIdentificationRequest() # KycIdentificationRequest |  (optional)

try:
    api_response = api_instance.kyc_put_request(user_id, validation_request=validation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_put_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **validation_request** | [**KycIdentificationRequest**](KycIdentificationRequest.md)|  | [optional] 

### Return type

[**KycValidationRequestResponse**](KycValidationRequestResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kyc_put_request_legal**
> KycValidationRequestResponse kyc_put_request_legal(user_id, validation_request=validation_request)



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
api_instance = swagger_client.KycApi(swagger_client.ApiClient(configuration))
user_id = 789 # int | 
validation_request = swagger_client.KycIdentificationRequest() # KycIdentificationRequest |  (optional)

try:
    api_response = api_instance.kyc_put_request_legal(user_id, validation_request=validation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->kyc_put_request_legal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **validation_request** | [**KycIdentificationRequest**](KycIdentificationRequest.md)|  | [optional] 

### Return type

[**KycValidationRequestResponse**](KycValidationRequestResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json;odata.metadata=minimal;odata.streaming=true, application/json;odata.metadata=minimal;odata.streaming=false, application/json;odata.metadata=minimal, application/json;odata.metadata=full;odata.streaming=true, application/json;odata.metadata=full;odata.streaming=false, application/json;odata.metadata=full, application/json;odata.metadata=none;odata.streaming=true, application/json;odata.metadata=none;odata.streaming=false, application/json;odata.metadata=none, application/json;odata.streaming=true, application/json;odata.streaming=false, application/json, application/xml, application/prs.odatatestxx-odata, text/plain, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


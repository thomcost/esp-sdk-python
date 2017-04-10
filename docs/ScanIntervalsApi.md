# esp_sdk.ScanIntervalsApi

All URIs are relative to *http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ScanIntervalsApi.md#create) | **POST** /api/v2/scan_intervals.json_api | Create a(n) Scan Interval
[**destroy**](ScanIntervalsApi.md#destroy) | **DELETE** /api/v2/scan_intervals/{id}.json_api | Remove a(n) Scan Interval
[**list**](ScanIntervalsApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/scan_intervals.json_api | Get a list of Scan Intervals
[**show**](ScanIntervalsApi.md#show) | **GET** /api/v2/scan_intervals/{id}.json_api | Show a single Scan Interval
[**update**](ScanIntervalsApi.md#update) | **PATCH** /api/v2/scan_intervals/{id}.json_api | Update a(n) Scan Interval


# **create**
> ScanInterval create(external_account_id, interval, service_id)

Create a(n) Scan Interval

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
external_account_id = 56 # int | The ID of the external account this scan interval is for
interval = 56 # int | The interval, in minutes, this service will be scanned
service_id = 56 # int | The service ID this scan interval is for

try: 
    # Create a(n) Scan Interval
    api_response = api_instance.create(external_account_id, interval, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**| The ID of the external account this scan interval is for | 
 **interval** | **int**| The interval, in minutes, this service will be scanned | 
 **service_id** | **int**| The service ID this scan interval is for | 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy**
> object destroy(id)

Remove a(n) Scan Interval

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int | Scan Interval Id

try: 
    # Remove a(n) Scan Interval
    api_response = api_instance.destroy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scan Interval Id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(external_account_id, page=page, filter=filter, include=include)

Get a list of Scan Intervals

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
external_account_id = 56 # int | 
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)

try: 
    # Get a list of Scan Intervals
    api_response = api_instance.list(external_account_id, page=page, filter=filter, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_account_id** | **int**|  | 
 **page** | [**dict(str, str)**](str.md)| Page Number | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching | [optional] 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> ScanInterval show(id, include=include)

Show a single Scan Interval

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int | Scan Interval Id
include = 'include_example' # str | Included Objects (optional)

try: 
    # Show a single Scan Interval
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scan Interval Id | 
 **include** | **str**| Included Objects | [optional] 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ScanInterval update(id, external_account_id, interval, service_id)

Update a(n) Scan Interval

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.ScanIntervalsApi()
id = 56 # int | Scan Interval Id
external_account_id = 56 # int | The ID of the external account this scan interval is for
interval = 56 # int | The interval, in minutes, this service will be scanned
service_id = 56 # int | The service ID this scan interval is for

try: 
    # Update a(n) Scan Interval
    api_response = api_instance.update(id, external_account_id, interval, service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanIntervalsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scan Interval Id | 
 **external_account_id** | **int**| The ID of the external account this scan interval is for | 
 **interval** | **int**| The interval, in minutes, this service will be scanned | 
 **service_id** | **int**| The service ID this scan interval is for | 

### Return type

[**ScanInterval**](ScanInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

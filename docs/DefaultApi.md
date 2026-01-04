# quantumdmn.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_member**](DefaultApi.md#add_project_member) | **POST** /projects/{projectID}/members | Add Project Member
[**batch_get_users**](DefaultApi.md#batch_get_users) | **POST** /users/batch | Batch Get Organization Users
[**create_definition**](DefaultApi.md#create_definition) | **POST** /projects/{projectID}/definitions | Create Definition
[**create_project**](DefaultApi.md#create_project) | **POST** /projects | Create Project
[**create_subscription_upgrade_transaction**](DefaultApi.md#create_subscription_upgrade_transaction) | **POST** /billing/upgrade-transaction | Create Subscription Upgrade Transaction
[**delete_definition**](DefaultApi.md#delete_definition) | **DELETE** /projects/{projectID}/definitions/{definitionID} | Delete Definition
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /projects/{projectID} | Delete Project
[**evaluate_by_xmlid**](DefaultApi.md#evaluate_by_xmlid) | **POST** /projects/{projectID}/definitions/by-xml-id/{xmlDefinitionID}/evaluate | Evaluate definition by XML definition ID
[**evaluate_design**](DefaultApi.md#evaluate_design) | **POST** /evaluate/design | Evaluate DMN Design
[**evaluate_design_batch**](DefaultApi.md#evaluate_design_batch) | **POST** /evaluate/design/batch | Batch evaluate a DMN design with multiple inputs
[**evaluate_stored**](DefaultApi.md#evaluate_stored) | **POST** /projects/{projectID}/definitions/{definitionID}/evaluate | Evaluate Stored Definition
[**get_customer_portal_session**](DefaultApi.md#get_customer_portal_session) | **GET** /subscription/portal-session | Get Customer Portal Session
[**get_definition**](DefaultApi.md#get_definition) | **GET** /projects/{projectID}/definitions/{definitionID} | Get Definition
[**get_definition_by_xmlid**](DefaultApi.md#get_definition_by_xmlid) | **GET** /projects/{projectID}/definitions/by-xml-id/{xmlDefinitionID} | Get definition by XML definition ID
[**get_execution**](DefaultApi.md#get_execution) | **GET** /projects/{projectID}/executions/{executionID} | Get Execution
[**get_frontend_config**](DefaultApi.md#get_frontend_config) | **GET** /config | Get Frontend Configuration
[**get_health**](DefaultApi.md#get_health) | **GET** /health | Health Check
[**get_limits**](DefaultApi.md#get_limits) | **GET** /limits | Get Quota Limits
[**get_overview**](DefaultApi.md#get_overview) | **GET** /overview | Get Overview Dashboard Data
[**get_project**](DefaultApi.md#get_project) | **GET** /projects/{projectID} | Get Project
[**get_tier**](DefaultApi.md#get_tier) | **GET** /tiers/{tierID} | Get Tier
[**get_user_permissions**](DefaultApi.md#get_user_permissions) | **GET** /permissions | Get User Permissions
[**get_version**](DefaultApi.md#get_version) | **GET** /version | Version
[**list_definition_versions**](DefaultApi.md#list_definition_versions) | **GET** /projects/{projectID}/definitions/by-definition-id/{definitionId} | List all versions of a specific definition_id
[**list_definitions**](DefaultApi.md#list_definitions) | **GET** /projects/{projectID}/definitions | List Definitions
[**list_executions**](DefaultApi.md#list_executions) | **GET** /projects/{projectID}/definitions/{definitionID}/executions | List Executions for Definition
[**list_latest_definitions**](DefaultApi.md#list_latest_definitions) | **GET** /projects/{projectID}/definitions/latest | List Latest Definitions (one per definition_id)
[**list_project_executions**](DefaultApi.md#list_project_executions) | **GET** /projects/{projectID}/executions | List All Executions for Project
[**list_project_members**](DefaultApi.md#list_project_members) | **GET** /projects/{projectID}/members | List Project Members
[**list_projects**](DefaultApi.md#list_projects) | **GET** /projects | List Projects
[**list_tiers**](DefaultApi.md#list_tiers) | **GET** /tiers | List Tiers
[**list_users**](DefaultApi.md#list_users) | **GET** /users | List Organization Users
[**remove_project_member**](DefaultApi.md#remove_project_member) | **DELETE** /projects/{projectID}/members/{userID} | Remove Project Member
[**run_simulation**](DefaultApi.md#run_simulation) | **POST** /projects/{projectID}/definitions/{definitionID}/simulate | Run Simulation on Historical Data
[**update_customer_settings**](DefaultApi.md#update_customer_settings) | **PATCH** /settings | Update Customer Settings
[**update_definition**](DefaultApi.md#update_definition) | **PUT** /projects/{projectID}/definitions/{definitionID} | Update Definition
[**update_project_member_role**](DefaultApi.md#update_project_member_role) | **PUT** /projects/{projectID}/members/{userID} | Update Project Member Role


# **add_project_member**
> ProjectMember add_project_member(project_id, add_project_member_request)

Add Project Member

### Example


```python
import quantumdmn
from quantumdmn.models.add_project_member_request import AddProjectMemberRequest
from quantumdmn.models.project_member import ProjectMember
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    add_project_member_request = quantumdmn.AddProjectMemberRequest() # AddProjectMemberRequest | 

    try:
        # Add Project Member
        api_response = api_instance.add_project_member(project_id, add_project_member_request)
        print("The response of DefaultApi->add_project_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_project_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **add_project_member_request** | [**AddProjectMemberRequest**](AddProjectMemberRequest.md)|  | 

### Return type

[**ProjectMember**](ProjectMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_get_users**
> List[OrganizationUser] batch_get_users(batch_get_users_request)

Batch Get Organization Users

Retrieve multiple users by their IDs. Available to all authenticated organization members.

### Example


```python
import quantumdmn
from quantumdmn.models.batch_get_users_request import BatchGetUsersRequest
from quantumdmn.models.organization_user import OrganizationUser
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    batch_get_users_request = quantumdmn.BatchGetUsersRequest() # BatchGetUsersRequest | 

    try:
        # Batch Get Organization Users
        api_response = api_instance.batch_get_users(batch_get_users_request)
        print("The response of DefaultApi->batch_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->batch_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_get_users_request** | [**BatchGetUsersRequest**](BatchGetUsersRequest.md)|  | 

### Return type

[**List[OrganizationUser]**](OrganizationUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_definition**
> Definition create_definition(project_id, create_definition_request)

Create Definition

### Example


```python
import quantumdmn
from quantumdmn.models.create_definition_request import CreateDefinitionRequest
from quantumdmn.models.definition import Definition
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    create_definition_request = quantumdmn.CreateDefinitionRequest() # CreateDefinitionRequest | 

    try:
        # Create Definition
        api_response = api_instance.create_definition(project_id, create_definition_request)
        print("The response of DefaultApi->create_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **create_definition_request** | [**CreateDefinitionRequest**](CreateDefinitionRequest.md)|  | 

### Return type

[**Definition**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(create_project_request)

Create Project

### Example


```python
import quantumdmn
from quantumdmn.models.create_project_request import CreateProjectRequest
from quantumdmn.models.project import Project
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    create_project_request = quantumdmn.CreateProjectRequest() # CreateProjectRequest | 

    try:
        # Create Project
        api_response = api_instance.create_project(create_project_request)
        print("The response of DefaultApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_upgrade_transaction**
> CreateSubscriptionUpgradeTransaction200Response create_subscription_upgrade_transaction(create_subscription_upgrade_transaction_request)

Create Subscription Upgrade Transaction

Creates a Paddle transaction to upgrade/downgrade the current subscription

### Example


```python
import quantumdmn
from quantumdmn.models.create_subscription_upgrade_transaction200_response import CreateSubscriptionUpgradeTransaction200Response
from quantumdmn.models.create_subscription_upgrade_transaction_request import CreateSubscriptionUpgradeTransactionRequest
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    create_subscription_upgrade_transaction_request = quantumdmn.CreateSubscriptionUpgradeTransactionRequest() # CreateSubscriptionUpgradeTransactionRequest | 

    try:
        # Create Subscription Upgrade Transaction
        api_response = api_instance.create_subscription_upgrade_transaction(create_subscription_upgrade_transaction_request)
        print("The response of DefaultApi->create_subscription_upgrade_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_subscription_upgrade_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription_upgrade_transaction_request** | [**CreateSubscriptionUpgradeTransactionRequest**](CreateSubscriptionUpgradeTransactionRequest.md)|  | 

### Return type

[**CreateSubscriptionUpgradeTransaction200Response**](CreateSubscriptionUpgradeTransaction200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | No active subscription |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_definition**
> delete_definition(project_id, definition_id)

Delete Definition

### Example


```python
import quantumdmn
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    definition_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Definition
        api_instance.delete_definition(project_id, definition_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **definition_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Delete Project

### Example


```python
import quantumdmn
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Project
        api_instance.delete_project(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_by_xmlid**
> Dict[str, EvaluationResult] evaluate_by_xmlid(project_id, xml_definition_id, evaluate_stored_request, version=version)

Evaluate definition by XML definition ID

Evaluate a decision using XML definition ID (uses latest version unless version parameter specified)

### Example


```python
import quantumdmn
from quantumdmn.models.evaluate_stored_request import EvaluateStoredRequest
from quantumdmn.models.evaluation_result import EvaluationResult
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    xml_definition_id = 'xml_definition_id_example' # str | The XML definition ID from the DMN model
    evaluate_stored_request = quantumdmn.EvaluateStoredRequest() # EvaluateStoredRequest | 
    version = 56 # int | Specific version number (defaults to latest version) (optional)

    try:
        # Evaluate definition by XML definition ID
        api_response = api_instance.evaluate_by_xmlid(project_id, xml_definition_id, evaluate_stored_request, version=version)
        print("The response of DefaultApi->evaluate_by_xmlid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->evaluate_by_xmlid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **xml_definition_id** | **str**| The XML definition ID from the DMN model | 
 **evaluate_stored_request** | [**EvaluateStoredRequest**](EvaluateStoredRequest.md)|  | 
 **version** | **int**| Specific version number (defaults to latest version) | [optional] 

### Return type

[**Dict[str, EvaluationResult]**](EvaluationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_design**
> Dict[str, EvaluationResult] evaluate_design(evaluate_design_request)

Evaluate DMN Design

### Example


```python
import quantumdmn
from quantumdmn.models.evaluate_design_request import EvaluateDesignRequest
from quantumdmn.models.evaluation_result import EvaluationResult
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    evaluate_design_request = quantumdmn.EvaluateDesignRequest() # EvaluateDesignRequest | 

    try:
        # Evaluate DMN Design
        api_response = api_instance.evaluate_design(evaluate_design_request)
        print("The response of DefaultApi->evaluate_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->evaluate_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluate_design_request** | [**EvaluateDesignRequest**](EvaluateDesignRequest.md)|  | 

### Return type

[**Dict[str, EvaluationResult]**](EvaluationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_design_batch**
> BatchEvaluationResponse evaluate_design_batch(batch_evaluate_design_request)

Batch evaluate a DMN design with multiple inputs

### Example


```python
import quantumdmn
from quantumdmn.models.batch_evaluate_design_request import BatchEvaluateDesignRequest
from quantumdmn.models.batch_evaluation_response import BatchEvaluationResponse
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    batch_evaluate_design_request = quantumdmn.BatchEvaluateDesignRequest() # BatchEvaluateDesignRequest | 

    try:
        # Batch evaluate a DMN design with multiple inputs
        api_response = api_instance.evaluate_design_batch(batch_evaluate_design_request)
        print("The response of DefaultApi->evaluate_design_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->evaluate_design_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_evaluate_design_request** | [**BatchEvaluateDesignRequest**](BatchEvaluateDesignRequest.md)|  | 

### Return type

[**BatchEvaluationResponse**](BatchEvaluationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch evaluation successful |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_stored**
> Dict[str, EvaluationResult] evaluate_stored(project_id, definition_id, evaluate_stored_request)

Evaluate Stored Definition

### Example


```python
import quantumdmn
from quantumdmn.models.evaluate_stored_request import EvaluateStoredRequest
from quantumdmn.models.evaluation_result import EvaluationResult
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    definition_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    evaluate_stored_request = quantumdmn.EvaluateStoredRequest() # EvaluateStoredRequest | 

    try:
        # Evaluate Stored Definition
        api_response = api_instance.evaluate_stored(project_id, definition_id, evaluate_stored_request)
        print("The response of DefaultApi->evaluate_stored:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->evaluate_stored: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **definition_id** | **UUID**|  | 
 **evaluate_stored_request** | [**EvaluateStoredRequest**](EvaluateStoredRequest.md)|  | 

### Return type

[**Dict[str, EvaluationResult]**](EvaluationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_portal_session**
> GetCustomerPortalSession200Response get_customer_portal_session()

Get Customer Portal Session

Returns a generated link to the Paddle Customer Portal

### Example


```python
import quantumdmn
from quantumdmn.models.get_customer_portal_session200_response import GetCustomerPortalSession200Response
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # Get Customer Portal Session
        api_response = api_instance.get_customer_portal_session()
        print("The response of DefaultApi->get_customer_portal_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_customer_portal_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCustomerPortalSession200Response**](GetCustomerPortalSession200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden (No subscription) |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_definition**
> Definition get_definition(project_id, definition_id)

Get Definition

### Example


```python
import quantumdmn
from quantumdmn.models.definition import Definition
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    definition_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Definition
        api_response = api_instance.get_definition(project_id, definition_id)
        print("The response of DefaultApi->get_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **definition_id** | **UUID**|  | 

### Return type

[**Definition**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_definition_by_xmlid**
> Definition get_definition_by_xmlid(project_id, xml_definition_id, version=version)

Get definition by XML definition ID

Get the latest version of a definition by its XML definition ID, or a specific version if provided

### Example


```python
import quantumdmn
from quantumdmn.models.definition import Definition
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    xml_definition_id = 'xml_definition_id_example' # str | The XML definition ID from the DMN model
    version = 56 # int | Specific version number (defaults to latest version) (optional)

    try:
        # Get definition by XML definition ID
        api_response = api_instance.get_definition_by_xmlid(project_id, xml_definition_id, version=version)
        print("The response of DefaultApi->get_definition_by_xmlid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_definition_by_xmlid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **xml_definition_id** | **str**| The XML definition ID from the DMN model | 
 **version** | **int**| Specific version number (defaults to latest version) | [optional] 

### Return type

[**Definition**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution**
> Execution get_execution(project_id, execution_id)

Get Execution

### Example


```python
import quantumdmn
from quantumdmn.models.execution import Execution
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    execution_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Execution
        api_response = api_instance.get_execution(project_id, execution_id)
        print("The response of DefaultApi->get_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **execution_id** | **UUID**|  | 

### Return type

[**Execution**](Execution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_frontend_config**
> FrontendConfig get_frontend_config()

Get Frontend Configuration

Returns configuration required by the frontend application (OIDC settings)

### Example


```python
import quantumdmn
from quantumdmn.models.frontend_config import FrontendConfig
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # Get Frontend Configuration
        api_response = api_instance.get_frontend_config()
        print("The response of DefaultApi->get_frontend_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_frontend_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FrontendConfig**](FrontendConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health**
> GetHealth200Response get_health()

Health Check

### Example


```python
import quantumdmn
from quantumdmn.models.get_health200_response import GetHealth200Response
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # Health Check
        api_response = api_instance.get_health()
        print("The response of DefaultApi->get_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetHealth200Response**](GetHealth200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_limits**
> Quota get_limits()

Get Quota Limits

### Example


```python
import quantumdmn
from quantumdmn.models.quota import Quota
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # Get Quota Limits
        api_response = api_instance.get_limits()
        print("The response of DefaultApi->get_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_limits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Quota**](Quota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overview**
> OverviewResponse get_overview()

Get Overview Dashboard Data

Returns aggregated statistics for the overview dashboard including KPI charts and quota status.

### Example


```python
import quantumdmn
from quantumdmn.models.overview_response import OverviewResponse
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # Get Overview Dashboard Data
        api_response = api_instance.get_overview()
        print("The response of DefaultApi->get_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_overview: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OverviewResponse**](OverviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_id)

Get Project

### Example


```python
import quantumdmn
from quantumdmn.models.project import Project
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Project
        api_response = api_instance.get_project(project_id)
        print("The response of DefaultApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tier**
> Tier get_tier(tier_id)

Get Tier

### Example


```python
import quantumdmn
from quantumdmn.models.tier import Tier
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    tier_id = 'tier_id_example' # str | 

    try:
        # Get Tier
        api_response = api_instance.get_tier(tier_id)
        print("The response of DefaultApi->get_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_id** | **str**|  | 

### Return type

[**Tier**](Tier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_permissions**
> UserPermissions get_user_permissions()

Get User Permissions

Returns the current user's global role and all project-level permissions

### Example


```python
import quantumdmn
from quantumdmn.models.user_permissions import UserPermissions
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # Get User Permissions
        api_response = api_instance.get_user_permissions()
        print("The response of DefaultApi->get_user_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserPermissions**](UserPermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> GetVersion200Response get_version()

Version

### Example


```python
import quantumdmn
from quantumdmn.models.get_version200_response import GetVersion200Response
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # Version
        api_response = api_instance.get_version()
        print("The response of DefaultApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetVersion200Response**](GetVersion200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_definition_versions**
> PaginatedDefinitionsResponse list_definition_versions(project_id, definition_id, page=page, page_size=page_size)

List all versions of a specific definition_id

### Example


```python
import quantumdmn
from quantumdmn.models.paginated_definitions_response import PaginatedDefinitionsResponse
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    definition_id = 'definition_id_example' # str | 
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Number of items per page (max 100) (optional) (default to 20)

    try:
        # List all versions of a specific definition_id
        api_response = api_instance.list_definition_versions(project_id, definition_id, page=page, page_size=page_size)
        print("The response of DefaultApi->list_definition_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_definition_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **definition_id** | **str**|  | 
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (max 100) | [optional] [default to 20]

### Return type

[**PaginatedDefinitionsResponse**](PaginatedDefinitionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_definitions**
> PaginatedDefinitionsResponse list_definitions(project_id, page=page, page_size=page_size)

List Definitions

### Example


```python
import quantumdmn
from quantumdmn.models.paginated_definitions_response import PaginatedDefinitionsResponse
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Number of items per page (max 100) (optional) (default to 20)

    try:
        # List Definitions
        api_response = api_instance.list_definitions(project_id, page=page, page_size=page_size)
        print("The response of DefaultApi->list_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_definitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (max 100) | [optional] [default to 20]

### Return type

[**PaginatedDefinitionsResponse**](PaginatedDefinitionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_executions**
> PaginatedExecutionsResponse list_executions(project_id, definition_id, xml_definition_id=xml_definition_id, start_date=start_date, page=page, page_size=page_size)

List Executions for Definition

### Example


```python
import quantumdmn
from quantumdmn.models.paginated_executions_response import PaginatedExecutionsResponse
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    definition_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    xml_definition_id = 'xml_definition_id_example' # str | Filter by XML Definition ID (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter executions after this date (ISO 8601) (optional)
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Number of items per page (max 100) (optional) (default to 20)

    try:
        # List Executions for Definition
        api_response = api_instance.list_executions(project_id, definition_id, xml_definition_id=xml_definition_id, start_date=start_date, page=page, page_size=page_size)
        print("The response of DefaultApi->list_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **definition_id** | **UUID**|  | 
 **xml_definition_id** | **str**| Filter by XML Definition ID | [optional] 
 **start_date** | **datetime**| Filter executions after this date (ISO 8601) | [optional] 
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (max 100) | [optional] [default to 20]

### Return type

[**PaginatedExecutionsResponse**](PaginatedExecutionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_latest_definitions**
> PaginatedDefinitionsResponse list_latest_definitions(project_id, page=page, page_size=page_size)

List Latest Definitions (one per definition_id)

### Example


```python
import quantumdmn
from quantumdmn.models.paginated_definitions_response import PaginatedDefinitionsResponse
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Number of items per page (max 100) (optional) (default to 20)

    try:
        # List Latest Definitions (one per definition_id)
        api_response = api_instance.list_latest_definitions(project_id, page=page, page_size=page_size)
        print("The response of DefaultApi->list_latest_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_latest_definitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (max 100) | [optional] [default to 20]

### Return type

[**PaginatedDefinitionsResponse**](PaginatedDefinitionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_executions**
> PaginatedExecutionsResponse list_project_executions(project_id, xml_definition_id=xml_definition_id, page=page, page_size=page_size)

List All Executions for Project

### Example


```python
import quantumdmn
from quantumdmn.models.paginated_executions_response import PaginatedExecutionsResponse
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    xml_definition_id = 'xml_definition_id_example' # str | Filter by XML Definition ID (optional)
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    page_size = 20 # int | Number of items per page (max 100) (optional) (default to 20)

    try:
        # List All Executions for Project
        api_response = api_instance.list_project_executions(project_id, xml_definition_id=xml_definition_id, page=page, page_size=page_size)
        print("The response of DefaultApi->list_project_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_project_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **xml_definition_id** | **str**| Filter by XML Definition ID | [optional] 
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (max 100) | [optional] [default to 20]

### Return type

[**PaginatedExecutionsResponse**](PaginatedExecutionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_members**
> List[ProjectMember] list_project_members(project_id)

List Project Members

### Example


```python
import quantumdmn
from quantumdmn.models.project_member import ProjectMember
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # List Project Members
        api_response = api_instance.list_project_members(project_id)
        print("The response of DefaultApi->list_project_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_project_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**List[ProjectMember]**](ProjectMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> List[Project] list_projects()

List Projects

### Example


```python
import quantumdmn
from quantumdmn.models.project import Project
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # List Projects
        api_response = api_instance.list_projects()
        print("The response of DefaultApi->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tiers**
> List[Tier] list_tiers()

List Tiers

### Example


```python
import quantumdmn
from quantumdmn.models.tier import Tier
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)

    try:
        # List Tiers
        api_response = api_instance.list_tiers()
        print("The response of DefaultApi->list_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_tiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Tier]**](Tier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> List[OrganizationUser] list_users(search=search)

List Organization Users

### Example


```python
import quantumdmn
from quantumdmn.models.organization_user import OrganizationUser
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    search = 'search_example' # str | Search by email or username (optional)

    try:
        # List Organization Users
        api_response = api_instance.list_users(search=search)
        print("The response of DefaultApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search by email or username | [optional] 

### Return type

[**List[OrganizationUser]**](OrganizationUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_member**
> remove_project_member(project_id, user_id)

Remove Project Member

### Example


```python
import quantumdmn
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove Project Member
        api_instance.remove_project_member(project_id, user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->remove_project_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_simulation**
> SimulationResponse run_simulation(project_id, definition_id, simulation_request)

Run Simulation on Historical Data

### Example


```python
import quantumdmn
from quantumdmn.models.simulation_request import SimulationRequest
from quantumdmn.models.simulation_response import SimulationResponse
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    definition_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    simulation_request = quantumdmn.SimulationRequest() # SimulationRequest | 

    try:
        # Run Simulation on Historical Data
        api_response = api_instance.run_simulation(project_id, definition_id, simulation_request)
        print("The response of DefaultApi->run_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->run_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **definition_id** | **UUID**|  | 
 **simulation_request** | [**SimulationRequest**](SimulationRequest.md)|  | 

### Return type

[**SimulationResponse**](SimulationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Simulation successful |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_settings**
> update_customer_settings(update_customer_settings_request)

Update Customer Settings

### Example


```python
import quantumdmn
from quantumdmn.models.update_customer_settings_request import UpdateCustomerSettingsRequest
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    update_customer_settings_request = quantumdmn.UpdateCustomerSettingsRequest() # UpdateCustomerSettingsRequest | 

    try:
        # Update Customer Settings
        api_instance.update_customer_settings(update_customer_settings_request)
    except Exception as e:
        print("Exception when calling DefaultApi->update_customer_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_customer_settings_request** | [**UpdateCustomerSettingsRequest**](UpdateCustomerSettingsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_definition**
> Definition update_definition(project_id, definition_id, update_definition_request)

Update Definition

### Example


```python
import quantumdmn
from quantumdmn.models.definition import Definition
from quantumdmn.models.update_definition_request import UpdateDefinitionRequest
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    definition_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_definition_request = quantumdmn.UpdateDefinitionRequest() # UpdateDefinitionRequest | 

    try:
        # Update Definition
        api_response = api_instance.update_definition(project_id, definition_id, update_definition_request)
        print("The response of DefaultApi->update_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **definition_id** | **UUID**|  | 
 **update_definition_request** | [**UpdateDefinitionRequest**](UpdateDefinitionRequest.md)|  | 

### Return type

[**Definition**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_member_role**
> ProjectMember update_project_member_role(project_id, user_id, update_project_member_role_request)

Update Project Member Role

### Example


```python
import quantumdmn
from quantumdmn.models.project_member import ProjectMember
from quantumdmn.models.update_project_member_role_request import UpdateProjectMemberRoleRequest
from quantumdmn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = quantumdmn.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with quantumdmn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quantumdmn.DefaultApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    user_id = 'user_id_example' # str | 
    update_project_member_role_request = quantumdmn.UpdateProjectMemberRoleRequest() # UpdateProjectMemberRoleRequest | 

    try:
        # Update Project Member Role
        api_response = api_instance.update_project_member_role(project_id, user_id, update_project_member_role_request)
        print("The response of DefaultApi->update_project_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_project_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **user_id** | **str**|  | 
 **update_project_member_role_request** | [**UpdateProjectMemberRoleRequest**](UpdateProjectMemberRoleRequest.md)|  | 

### Return type

[**ProjectMember**](ProjectMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


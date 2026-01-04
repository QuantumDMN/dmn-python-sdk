# FrontendConfigOidc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority** | **str** | OIDC authority URL (issuer) | 
**client_id** | **str** | OIDC client ID for the web application | 

## Example

```python
from quantumdmn.models.frontend_config_oidc import FrontendConfigOidc

# TODO update the JSON string below
json = "{}"
# create an instance of FrontendConfigOidc from a JSON string
frontend_config_oidc_instance = FrontendConfigOidc.from_json(json)
# print the JSON string representation of the object
print(FrontendConfigOidc.to_json())

# convert the object into a dict
frontend_config_oidc_dict = frontend_config_oidc_instance.to_dict()
# create an instance of FrontendConfigOidc from a dict
frontend_config_oidc_from_dict = FrontendConfigOidc.from_dict(frontend_config_oidc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UpdateCustomerSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_overage** | **bool** |  | [optional] 

## Example

```python
from quantumdmn.models.update_customer_settings_request import UpdateCustomerSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerSettingsRequest from a JSON string
update_customer_settings_request_instance = UpdateCustomerSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomerSettingsRequest.to_json())

# convert the object into a dict
update_customer_settings_request_dict = update_customer_settings_request_instance.to_dict()
# create an instance of UpdateCustomerSettingsRequest from a dict
update_customer_settings_request_from_dict = UpdateCustomerSettingsRequest.from_dict(update_customer_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



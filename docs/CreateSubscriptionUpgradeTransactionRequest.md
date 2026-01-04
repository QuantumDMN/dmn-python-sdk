# CreateSubscriptionUpgradeTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_id** | **str** |  | 

## Example

```python
from quantumdmn.models.create_subscription_upgrade_transaction_request import CreateSubscriptionUpgradeTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionUpgradeTransactionRequest from a JSON string
create_subscription_upgrade_transaction_request_instance = CreateSubscriptionUpgradeTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionUpgradeTransactionRequest.to_json())

# convert the object into a dict
create_subscription_upgrade_transaction_request_dict = create_subscription_upgrade_transaction_request_instance.to_dict()
# create an instance of CreateSubscriptionUpgradeTransactionRequest from a dict
create_subscription_upgrade_transaction_request_from_dict = CreateSubscriptionUpgradeTransactionRequest.from_dict(create_subscription_upgrade_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TierFeaturesConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits** | **int** |  | [optional] 
**overcharge_price_per100_credits** | **int** |  | [optional] 
**limits** | [**TierLimits**](TierLimits.md) |  | [optional] 
**features** | **Dict[str, bool]** |  | [optional] 

## Example

```python
from quantumdmn.models.tier_features_config import TierFeaturesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TierFeaturesConfig from a JSON string
tier_features_config_instance = TierFeaturesConfig.from_json(json)
# print the JSON string representation of the object
print(TierFeaturesConfig.to_json())

# convert the object into a dict
tier_features_config_dict = tier_features_config_instance.to_dict()
# create an instance of TierFeaturesConfig from a dict
tier_features_config_from_dict = TierFeaturesConfig.from_dict(tier_features_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



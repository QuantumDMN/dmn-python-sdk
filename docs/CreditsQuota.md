# CreditsQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**overcharge_price** | **int** |  | [optional] 
**overcharge_enabled** | **bool** |  | [optional] 

## Example

```python
from quantumdmn.models.credits_quota import CreditsQuota

# TODO update the JSON string below
json = "{}"
# create an instance of CreditsQuota from a JSON string
credits_quota_instance = CreditsQuota.from_json(json)
# print the JSON string representation of the object
print(CreditsQuota.to_json())

# convert the object into a dict
credits_quota_dict = credits_quota_instance.to_dict()
# create an instance of CreditsQuota from a dict
credits_quota_from_dict = CreditsQuota.from_dict(credits_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



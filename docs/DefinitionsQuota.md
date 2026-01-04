# DefinitionsQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Max definitions allowed per project (tier limit) | [optional] 
**projects** | [**List[ProjectUsage]**](ProjectUsage.md) |  | [optional] 

## Example

```python
from quantumdmn.models.definitions_quota import DefinitionsQuota

# TODO update the JSON string below
json = "{}"
# create an instance of DefinitionsQuota from a JSON string
definitions_quota_instance = DefinitionsQuota.from_json(json)
# print the JSON string representation of the object
print(DefinitionsQuota.to_json())

# convert the object into a dict
definitions_quota_dict = definitions_quota_instance.to_dict()
# create an instance of DefinitionsQuota from a dict
definitions_quota_from_dict = DefinitionsQuota.from_dict(definitions_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



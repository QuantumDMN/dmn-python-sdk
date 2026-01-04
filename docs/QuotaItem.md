# QuotaItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 

## Example

```python
from quantumdmn.models.quota_item import QuotaItem

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaItem from a JSON string
quota_item_instance = QuotaItem.from_json(json)
# print the JSON string representation of the object
print(QuotaItem.to_json())

# convert the object into a dict
quota_item_dict = quota_item_instance.to_dict()
# create an instance of QuotaItem from a dict
quota_item_from_dict = QuotaItem.from_dict(quota_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



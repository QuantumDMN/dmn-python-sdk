# HitRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** |  | [optional] 
**outputs** | [**FeelValue**](FeelValue.md) |  | [optional] 

## Example

```python
from quantumdmn.models.hit_rule import HitRule

# TODO update the JSON string below
json = "{}"
# create an instance of HitRule from a JSON string
hit_rule_instance = HitRule.from_json(json)
# print the JSON string representation of the object
print(HitRule.to_json())

# convert the object into a dict
hit_rule_dict = hit_rule_instance.to_dict()
# create an instance of HitRule from a dict
hit_rule_from_dict = HitRule.from_dict(hit_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



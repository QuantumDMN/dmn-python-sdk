# DailyStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**requests** | **int** |  | [optional] 
**credits** | **int** |  | [optional] 

## Example

```python
from quantumdmn.models.daily_stat import DailyStat

# TODO update the JSON string below
json = "{}"
# create an instance of DailyStat from a JSON string
daily_stat_instance = DailyStat.from_json(json)
# print the JSON string representation of the object
print(DailyStat.to_json())

# convert the object into a dict
daily_stat_dict = daily_stat_instance.to_dict()
# create an instance of DailyStat from a dict
daily_stat_from_dict = DailyStat.from_dict(daily_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



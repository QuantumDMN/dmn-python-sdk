# KpiTrendDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from quantumdmn.models.kpi_trend_data_inner import KpiTrendDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of KpiTrendDataInner from a JSON string
kpi_trend_data_inner_instance = KpiTrendDataInner.from_json(json)
# print the JSON string representation of the object
print(KpiTrendDataInner.to_json())

# convert the object into a dict
kpi_trend_data_inner_dict = kpi_trend_data_inner_instance.to_dict()
# create an instance of KpiTrendDataInner from a dict
kpi_trend_data_inner_from_dict = KpiTrendDataInner.from_dict(kpi_trend_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



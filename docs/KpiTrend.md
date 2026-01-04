# KpiTrend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kpi_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**data** | [**List[KpiTrendDataInner]**](KpiTrendDataInner.md) |  | [optional] 

## Example

```python
from quantumdmn.models.kpi_trend import KpiTrend

# TODO update the JSON string below
json = "{}"
# create an instance of KpiTrend from a JSON string
kpi_trend_instance = KpiTrend.from_json(json)
# print the JSON string representation of the object
print(KpiTrend.to_json())

# convert the object into a dict
kpi_trend_dict = kpi_trend_instance.to_dict()
# create an instance of KpiTrend from a dict
kpi_trend_from_dict = KpiTrend.from_dict(kpi_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



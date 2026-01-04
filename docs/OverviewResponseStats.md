# OverviewResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_requests** | **int** |  | [optional] 
**total_credits** | **int** |  | [optional] 
**requests_trend** | [**List[DailyStat]**](DailyStat.md) |  | [optional] 
**credits_trend** | [**List[DailyStat]**](DailyStat.md) |  | [optional] 
**kpi_trends** | [**List[KpiTrend]**](KpiTrend.md) |  | [optional] 

## Example

```python
from quantumdmn.models.overview_response_stats import OverviewResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewResponseStats from a JSON string
overview_response_stats_instance = OverviewResponseStats.from_json(json)
# print the JSON string representation of the object
print(OverviewResponseStats.to_json())

# convert the object into a dict
overview_response_stats_dict = overview_response_stats_instance.to_dict()
# create an instance of OverviewResponseStats from a dict
overview_response_stats_from_dict = OverviewResponseStats.from_dict(overview_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



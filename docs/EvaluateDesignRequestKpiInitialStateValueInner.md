# EvaluateDesignRequestKpiInitialStateValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[EvaluateDesignRequestKpiInitialStateValueInnerMetricsInner]**](EvaluateDesignRequestKpiInitialStateValueInnerMetricsInner.md) |  | 
**timestamp** | **datetime** | Timestamp of the measurement (ISO 8601) | 

## Example

```python
from quantumdmn.models.evaluate_design_request_kpi_initial_state_value_inner import EvaluateDesignRequestKpiInitialStateValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluateDesignRequestKpiInitialStateValueInner from a JSON string
evaluate_design_request_kpi_initial_state_value_inner_instance = EvaluateDesignRequestKpiInitialStateValueInner.from_json(json)
# print the JSON string representation of the object
print(EvaluateDesignRequestKpiInitialStateValueInner.to_json())

# convert the object into a dict
evaluate_design_request_kpi_initial_state_value_inner_dict = evaluate_design_request_kpi_initial_state_value_inner_instance.to_dict()
# create an instance of EvaluateDesignRequestKpiInitialStateValueInner from a dict
evaluate_design_request_kpi_initial_state_value_inner_from_dict = EvaluateDesignRequestKpiInitialStateValueInner.from_dict(evaluate_design_request_kpi_initial_state_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



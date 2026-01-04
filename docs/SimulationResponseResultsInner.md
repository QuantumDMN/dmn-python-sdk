# SimulationResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** |  | [optional] 
**executed_at** | **datetime** |  | [optional] 
**inputs** | **Dict[str, object]** |  | [optional] 
**results** | [**Dict[str, EvaluationResult]**](EvaluationResult.md) |  | [optional] 

## Example

```python
from quantumdmn.models.simulation_response_results_inner import SimulationResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimulationResponseResultsInner from a JSON string
simulation_response_results_inner_instance = SimulationResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(SimulationResponseResultsInner.to_json())

# convert the object into a dict
simulation_response_results_inner_dict = simulation_response_results_inner_instance.to_dict()
# create an instance of SimulationResponseResultsInner from a dict
simulation_response_results_inner_from_dict = SimulationResponseResultsInner.from_dict(simulation_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



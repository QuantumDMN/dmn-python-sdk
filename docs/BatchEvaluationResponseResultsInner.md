# BatchEvaluationResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** |  | [optional] 
**inputs** | **Dict[str, object]** |  | [optional] 
**results** | [**Dict[str, EvaluationResult]**](EvaluationResult.md) |  | [optional] 

## Example

```python
from quantumdmn.models.batch_evaluation_response_results_inner import BatchEvaluationResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEvaluationResponseResultsInner from a JSON string
batch_evaluation_response_results_inner_instance = BatchEvaluationResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(BatchEvaluationResponseResultsInner.to_json())

# convert the object into a dict
batch_evaluation_response_results_inner_dict = batch_evaluation_response_results_inner_instance.to_dict()
# create an instance of BatchEvaluationResponseResultsInner from a dict
batch_evaluation_response_results_inner_from_dict = BatchEvaluationResponseResultsInner.from_dict(batch_evaluation_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



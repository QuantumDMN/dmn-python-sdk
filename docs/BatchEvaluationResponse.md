# BatchEvaluationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BatchEvaluationResponseResultsInner]**](BatchEvaluationResponseResultsInner.md) |  | [optional] 

## Example

```python
from quantumdmn.models.batch_evaluation_response import BatchEvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEvaluationResponse from a JSON string
batch_evaluation_response_instance = BatchEvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(BatchEvaluationResponse.to_json())

# convert the object into a dict
batch_evaluation_response_dict = batch_evaluation_response_instance.to_dict()
# create an instance of BatchEvaluationResponse from a dict
batch_evaluation_response_from_dict = BatchEvaluationResponse.from_dict(batch_evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



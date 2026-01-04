# BatchEvaluateDesignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xml** | **str** | The DMN XML definition to evaluate | [optional] 
**inputs** | **List[Dict[str, object]]** | List of input contexts (rows) to evaluate | [optional] 

## Example

```python
from quantumdmn.models.batch_evaluate_design_request import BatchEvaluateDesignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEvaluateDesignRequest from a JSON string
batch_evaluate_design_request_instance = BatchEvaluateDesignRequest.from_json(json)
# print the JSON string representation of the object
print(BatchEvaluateDesignRequest.to_json())

# convert the object into a dict
batch_evaluate_design_request_dict = batch_evaluate_design_request_instance.to_dict()
# create an instance of BatchEvaluateDesignRequest from a dict
batch_evaluate_design_request_from_dict = BatchEvaluateDesignRequest.from_dict(batch_evaluate_design_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



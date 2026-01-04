# EvaluateStoredRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 
**context** | [**Dict[str, FeelValue]**](FeelValue.md) |  | 
**decision_services** | **List[str]** | List of Decision Services to evaluate | [optional] 
**decisions** | **List[str]** | List of Decision or Decision Service names to evaluate | [optional] 

## Example

```python
from quantumdmn.models.evaluate_stored_request import EvaluateStoredRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluateStoredRequest from a JSON string
evaluate_stored_request_instance = EvaluateStoredRequest.from_json(json)
# print the JSON string representation of the object
print(EvaluateStoredRequest.to_json())

# convert the object into a dict
evaluate_stored_request_dict = evaluate_stored_request_instance.to_dict()
# create an instance of EvaluateStoredRequest from a dict
evaluate_stored_request_from_dict = EvaluateStoredRequest.from_dict(evaluate_stored_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



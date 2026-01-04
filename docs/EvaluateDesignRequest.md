# EvaluateDesignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xml** | **str** |  | 
**context** | [**Dict[str, FeelValue]**](FeelValue.md) |  | [optional] 
**decision_services** | **List[str]** | Names of the Decision Services to evaluate (optional) | [optional] 
**decisions** | **List[str]** | List of Decision or Decision Service names to evaluate (optional) | [optional] 

## Example

```python
from quantumdmn.models.evaluate_design_request import EvaluateDesignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluateDesignRequest from a JSON string
evaluate_design_request_instance = EvaluateDesignRequest.from_json(json)
# print the JSON string representation of the object
print(EvaluateDesignRequest.to_json())

# convert the object into a dict
evaluate_design_request_dict = evaluate_design_request_instance.to_dict()
# create an instance of EvaluateDesignRequest from a dict
evaluate_design_request_from_dict = EvaluateDesignRequest.from_dict(evaluate_design_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



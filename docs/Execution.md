# Execution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**definition_id** | **UUID** |  | 
**executed_at** | **datetime** |  | 
**executed_by** | **str** |  | [optional] 
**inputs** | [**Dict[str, FeelValue]**](FeelValue.md) |  | 
**outputs** | [**FeelValue**](FeelValue.md) |  | 
**xml_definition_id** | **str** |  | [optional] 

## Example

```python
from quantumdmn.models.execution import Execution

# TODO update the JSON string below
json = "{}"
# create an instance of Execution from a JSON string
execution_instance = Execution.from_json(json)
# print the JSON string representation of the object
print(Execution.to_json())

# convert the object into a dict
execution_dict = execution_instance.to_dict()
# create an instance of Execution from a dict
execution_from_dict = Execution.from_dict(execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



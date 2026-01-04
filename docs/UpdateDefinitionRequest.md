# UpdateDefinitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xml** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from quantumdmn.models.update_definition_request import UpdateDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDefinitionRequest from a JSON string
update_definition_request_instance = UpdateDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDefinitionRequest.to_json())

# convert the object into a dict
update_definition_request_dict = update_definition_request_instance.to_dict()
# create an instance of UpdateDefinitionRequest from a dict
update_definition_request_from_dict = UpdateDefinitionRequest.from_dict(update_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



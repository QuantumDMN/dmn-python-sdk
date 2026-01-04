# CreateDefinitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**xml** | **str** |  | 
**version** | **int** |  | [optional] 

## Example

```python
from quantumdmn.models.create_definition_request import CreateDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDefinitionRequest from a JSON string
create_definition_request_instance = CreateDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDefinitionRequest.to_json())

# convert the object into a dict
create_definition_request_dict = create_definition_request_instance.to_dict()
# create an instance of CreateDefinitionRequest from a dict
create_definition_request_from_dict = CreateDefinitionRequest.from_dict(create_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



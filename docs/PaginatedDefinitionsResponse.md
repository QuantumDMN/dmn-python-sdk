# PaginatedDefinitionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Definition]**](Definition.md) |  | 
**pagination** | [**PaginationMetadata**](PaginationMetadata.md) |  | 

## Example

```python
from quantumdmn.models.paginated_definitions_response import PaginatedDefinitionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDefinitionsResponse from a JSON string
paginated_definitions_response_instance = PaginatedDefinitionsResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedDefinitionsResponse.to_json())

# convert the object into a dict
paginated_definitions_response_dict = paginated_definitions_response_instance.to_dict()
# create an instance of PaginatedDefinitionsResponse from a dict
paginated_definitions_response_from_dict = PaginatedDefinitionsResponse.from_dict(paginated_definitions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



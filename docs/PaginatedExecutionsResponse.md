# PaginatedExecutionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Execution]**](Execution.md) |  | 
**pagination** | [**PaginationMetadata**](PaginationMetadata.md) |  | 

## Example

```python
from quantumdmn.models.paginated_executions_response import PaginatedExecutionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExecutionsResponse from a JSON string
paginated_executions_response_instance = PaginatedExecutionsResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedExecutionsResponse.to_json())

# convert the object into a dict
paginated_executions_response_dict = paginated_executions_response_instance.to_dict()
# create an instance of PaginatedExecutionsResponse from a dict
paginated_executions_response_from_dict = PaginatedExecutionsResponse.from_dict(paginated_executions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



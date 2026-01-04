# BatchGetUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | 

## Example

```python
from quantumdmn.models.batch_get_users_request import BatchGetUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchGetUsersRequest from a JSON string
batch_get_users_request_instance = BatchGetUsersRequest.from_json(json)
# print the JSON string representation of the object
print(BatchGetUsersRequest.to_json())

# convert the object into a dict
batch_get_users_request_dict = batch_get_users_request_instance.to_dict()
# create an instance of BatchGetUsersRequest from a dict
batch_get_users_request_from_dict = BatchGetUsersRequest.from_dict(batch_get_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



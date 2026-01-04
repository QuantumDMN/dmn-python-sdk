# AddProjectMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from quantumdmn.models.add_project_member_request import AddProjectMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddProjectMemberRequest from a JSON string
add_project_member_request_instance = AddProjectMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AddProjectMemberRequest.to_json())

# convert the object into a dict
add_project_member_request_dict = add_project_member_request_instance.to_dict()
# create an instance of AddProjectMemberRequest from a dict
add_project_member_request_from_dict = AddProjectMemberRequest.from_dict(add_project_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



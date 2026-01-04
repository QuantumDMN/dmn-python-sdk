# UpdateProjectMemberRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from quantumdmn.models.update_project_member_role_request import UpdateProjectMemberRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectMemberRoleRequest from a JSON string
update_project_member_role_request_instance = UpdateProjectMemberRoleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectMemberRoleRequest.to_json())

# convert the object into a dict
update_project_member_role_request_dict = update_project_member_role_request_instance.to_dict()
# create an instance of UpdateProjectMemberRoleRequest from a dict
update_project_member_role_request_from_dict = UpdateProjectMemberRoleRequest.from_dict(update_project_member_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



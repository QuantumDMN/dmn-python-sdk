# UserPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_role** | **str** | User&#39;s global organization role (admin or user) | 
**projects** | [**Dict[str, ProjectPermissions]**](ProjectPermissions.md) | Map of projectID to project permissions | 

## Example

```python
from quantumdmn.models.user_permissions import UserPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of UserPermissions from a JSON string
user_permissions_instance = UserPermissions.from_json(json)
# print the JSON string representation of the object
print(UserPermissions.to_json())

# convert the object into a dict
user_permissions_dict = user_permissions_instance.to_dict()
# create an instance of UserPermissions from a dict
user_permissions_from_dict = UserPermissions.from_dict(user_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



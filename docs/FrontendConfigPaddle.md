# FrontendConfigPaddle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_token** | **str** | Paddle client-side token for checkout | [optional] 
**sandbox** | **bool** | Whether to use Paddle sandbox environment | [optional] 

## Example

```python
from quantumdmn.models.frontend_config_paddle import FrontendConfigPaddle

# TODO update the JSON string below
json = "{}"
# create an instance of FrontendConfigPaddle from a JSON string
frontend_config_paddle_instance = FrontendConfigPaddle.from_json(json)
# print the JSON string representation of the object
print(FrontendConfigPaddle.to_json())

# convert the object into a dict
frontend_config_paddle_dict = frontend_config_paddle_instance.to_dict()
# create an instance of FrontendConfigPaddle from a dict
frontend_config_paddle_from_dict = FrontendConfigPaddle.from_dict(frontend_config_paddle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



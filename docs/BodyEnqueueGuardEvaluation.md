# BodyEnqueueGuardEvaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**ContentCreate**](ContentCreate.md) |  | 
**context** | [**List[ContentCreate]**](ContentCreate.md) |  | 

## Example

```python
from ugc_guard_python.models.body_enqueue_guard_evaluation import BodyEnqueueGuardEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of BodyEnqueueGuardEvaluation from a JSON string
body_enqueue_guard_evaluation_instance = BodyEnqueueGuardEvaluation.from_json(json)
# print the JSON string representation of the object
print(BodyEnqueueGuardEvaluation.to_json())

# convert the object into a dict
body_enqueue_guard_evaluation_dict = body_enqueue_guard_evaluation_instance.to_dict()
# create an instance of BodyEnqueueGuardEvaluation from a dict
body_enqueue_guard_evaluation_from_dict = BodyEnqueueGuardEvaluation.from_dict(body_enqueue_guard_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



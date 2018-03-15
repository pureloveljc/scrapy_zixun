__author__ = "purelove"
__date__ = "2018/2/24 下午8:21"
import json
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
a=json.loads(json_str)
print(a)
print(type(a))

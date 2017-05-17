import requests
import json

r = requests.get("http://httpbin.org/get?name='akui'&email='a_kui@163.con'")
print(type(r.json()))
# result = requests.get("http://httpbin.org/ip")
# dictresult = json.loads(result.content)
# print("您的IP地址为："+dictresult["origin"])
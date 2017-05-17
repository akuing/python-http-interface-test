import requests
import json

name = input("请输入您的名字：")
email= input("请输入您的邮箱：")
dictdata={"name":name,"email":email}
result=requests.post("http://httpbin.org/post",data=dictdata)

# print(result.status_code)
print("返回的状态码：",result.status_code)
print("返回的内容为：")
print(json.dumps(result.json(),indent=4,ensure_ascii=False))
print("上送的内容为：")
print(result.request.headers)
print(result.request.body)

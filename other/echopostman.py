import requests
import json

url="https://postman-echo.com/post"
datastr={"strange":"boom"}
result=requests.post("https://postman-echo.com/get?test=123456")
# result=requests.post(url+"?strangee=boome")
# result=requests.post(url,data=datastr)
print(result.url)
print(result.status_code)
if len(result.text)>0 :
    dictResult=json.JSONDecoder().decode(result.text)
    print(json.dumps(dictResult,indent=1))


